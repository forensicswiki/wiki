#!/usr/bin/env python3
"""Check (and optionally fix) special characters in Forensics Wiki Markdown prose.

MkDocs renders with the Python-Markdown engine, which does not consume
backslash escapes for '<' and '&' (a backslash shows up literally in the
page), and which passes an unescaped '<word>' in prose through as an HTML
tag that the browser swallows. The reliable way to render a literal '<',
'>' or '&' in prose is the corresponding HTML entity, so this tool enforces:

  * an '&' in prose                        -> '&amp;'
  * a '<token>' placeholder in prose       -> '&lt;token&gt;'
    (a token whose name is not a valid HTML tag; valid tags such as
    '<sup>' or '<a href="...">' are intentional inline HTML and skipped)

Never flagged: fenced code blocks, HTML comments, inline code spans,
autolinks, Markdown link URLs, existing HTML entities, and angle brackets
that are already backslash-escaped.

Usage:
    python check_escaping.py [--check | --fix] [paths ...]

Defaults to --check over the docs directory and exits 1 when unescaped
characters are found, so it can be used as a CI check. --fix rewrites the
files in place with HTML entities.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

INLINE_CODE = re.compile(r"`[^`\n]*`")
AUTOLINK = re.compile(r"<[a-zA-Z][a-zA-Z0-9+.\-]*:[^<>\s]*>|<[^<>\s]*@[^<>\s]*>")
LINKURL = re.compile(r"\]\([^)\n]*\)")
TOKEN = re.compile(r"<[A-Za-z][A-Za-z0-9 ._\-]*?>")
ENTITY = re.compile(r"&[a-zA-Z][a-zA-Z0-9]*;|&#[0-9]+;|&#[xX][0-9a-fA-F]+;")
SPLIT_OPEN = re.compile(r"<[A-Za-z][A-Za-z0-9 ._\-]*[ \t]*$")
SPLIT_CLOSE = re.compile(r"^[A-Za-z0-9 ._\-]*>")
ENTITY_FOR = {"&": "&amp;", "<": "&lt;", ">": "&gt;"}
VALID_HTML_TAGS = {
    "sup", "sub", "br", "a", "span", "code", "kbd", "mark", "del", "ins",
    "strong", "em", "u", "i", "b", "small", "abbr", "s", "wbr", "img", "ol",
    "ul", "li", "blockquote", "p", "div", "table", "tr", "td", "th", "thead",
    "tbody", "caption", "figure", "figcaption", "details", "summary", "hr",
    "pre", "samp", "var", "q", "cite", "bdi", "bdo", "time", "data", "html",
    "head", "style", "body", "ui", "title", "meta", "link", "script",
    "section", "article",
}


def prose_lines(path):
    """Return a list of (lineno, line) for prose lines.

    Skips fenced code blocks and HTML comments (a line whose content before
    the closing '-->' is comment-only contributes no prose).
    """
    out = []
    in_fence = False
    fence_sig = ""
    in_comment = False
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            s = line.strip()
            if in_comment:
                if "-->" in s:
                    in_comment = False
                    after = s.split("-->", 1)[1]
                    if after.strip():
                        out.append((lineno, line))
                continue
            if in_fence:
                if s and set(s) <= set(fence_sig):
                    in_fence = False
                continue
            if s.startswith("```") or s.startswith("~~~"):
                in_fence = True
                fence_sig = s[:3]
                continue
            if s.startswith("<!--"):
                if "-->" not in s[4:]:
                    in_comment = True
                continue
            out.append((lineno, line))
    return out


def mask_spans(line):
    """Return a predicate for positions inside inline code, autolinks or link URLs."""
    spans = []
    for pattern in (INLINE_CODE, AUTOLINK, LINKURL):
        for m in pattern.finditer(line):
            spans.append(m.span())

    def in_span(i):
        return any(a <= i < b for a, b in spans)

    return in_span


def token_name(fragment):
    m = re.match(r"<([A-Za-z][A-Za-z0-9]*)", fragment)
    return m.group(1).lower() if m else ""


def line_targets(line):
    """Positions of '&', '<' or '>' on this prose line that need an entity."""
    in_span = mask_spans(line)
    pos = set()
    for i, ch in enumerate(line):
        if ch != "&" or in_span(i):
            continue
        if i > 0 and line[i - 1] == "\\":
            continue
        if ENTITY.match(line, i):
            continue
        pos.add(i)
    for m in TOKEN.finditer(line):
        if in_span(m.start()):
            continue
        if m.start() > 0 and line[m.start() - 1] == "\\":
            continue
        if token_name(m.group(0)) in VALID_HTML_TAGS:
            continue
        pos.add(m.start())
        pos.add(m.end() - 1)
    return pos


def split_token_targets(prose):
    """Find '<word ...' tokens that start at the end of one prose line and
    close with '...>' on the next (a single-line pass cannot see them).

    Returns (targets, pairs): targets maps lineno -> set of char positions;
    pairs is a list of (open_lineno, close_lineno) for reporting.
    """
    targets = {}
    pairs = []
    for k in range(len(prose) - 1):
        ln1, line1 = prose[k]
        ln2, line2 = prose[k + 1]
        m1 = SPLIT_OPEN.search(line1)
        if not m1:
            continue
        i = m1.start()
        if token_name(m1.group(0)) in VALID_HTML_TAGS:
            continue
        if i > 0 and line1[i - 1] == "\\":
            continue
        if mask_spans(line1)(i):
            continue
        m2 = SPLIT_CLOSE.match(line2)
        if not m2:
            continue
        j = m2.end() - 1
        if mask_spans(line2)(j):
            continue
        targets.setdefault(ln1, set()).add(i)
        targets.setdefault(ln2, set()).add(j)
        pairs.append((ln1, ln2))
    return targets, pairs


def collect_targets(path):
    """Return (per-line target positions, split pairs) for one Markdown file."""
    prose = prose_lines(path)
    lines = {ln: line for ln, line in prose}
    targets = {}
    for ln, line in prose:
        t = line_targets(line)
        if t:
            targets[ln] = t
    split_targets, pairs = split_token_targets(prose)
    for ln, t in split_targets.items():
        targets.setdefault(ln, set()).update(t)
    return targets, pairs, lines


def target_message(pos, line):
    ch = line[pos]
    if ch == "&":
        return "unescaped '&' (use '&amp;')"
    if ch == "<":
        return "unescaped '<' of a '<token>' placeholder (use '&lt;token&gt;')"
    return "unescaped '>' of a '<token>' placeholder (use '&lt;token&gt;')"


def md_files(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, fnames in os.walk(p):
                for f in sorted(fnames):
                    if f.endswith(".md"):
                        files.append(os.path.join(root, f))
        elif os.path.isfile(p) and p.endswith(".md"):
            files.append(p)
    return files


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Enforce HTML-entity escaping of '<', '>' and '&' in Markdown prose.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="report unescaped characters and exit 1 if found (default)")
    mode.add_argument("--fix", action="store_true",
                      help="escape unescaped characters as HTML entities in place")
    parser.add_argument("paths", nargs="*", default=["docs"],
                        help="Markdown files or directories (default: docs)")
    args = parser.parse_args(argv)
    fix = args.fix

    violations = 0
    total_fixed = 0
    total_files = 0
    for path in md_files(args.paths):
        targets, pairs, lines = collect_targets(path)
        if not targets:
            continue
        n = sum(len(t) for t in targets.values())
        if fix:
            src = open(path, encoding="utf-8").read().split("\n")
            for ln, pos in sorted(targets.items(), reverse=True):
                line = src[ln - 1]
                for p in sorted(pos, reverse=True):
                    line = line[:p] + ENTITY_FOR[line[p]] + line[p + 1:]
                src[ln - 1] = line
            open(path, "w", encoding="utf-8").write("\n".join(src))
            total_fixed += n
            total_files += 1
            print(f"{path}: {n} entity(ies) added")
        else:
            violations += n
            total_files += 1
            for ln in sorted(targets):
                for p in sorted(targets[ln]):
                    print(f"{path}:{ln}: {target_message(p, lines[ln])}"
                          f" | {lines[ln].strip()[:100]}")
            for ln1, ln2 in pairs:
                print(f"{path}:{ln1}: '<token>' placeholder is split across lines "
                      f"{ln1} and {ln2}; keep tokens on one line or escape both ends")

    if fix:
        if total_fixed:
            print(f"\nFixed {total_fixed} unescaped character(s) across {total_files} file(s).")
        else:
            print("Nothing to fix.")
        return 0

    if violations:
        print(f"\nFound {violations} unescaped character(s) in {total_files} file(s).")
        print("Run 'python check_escaping.py --fix docs' to fix them automatically.")
        return 1
    print("No unescaped special characters found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
