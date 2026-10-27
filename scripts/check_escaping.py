#!/usr/bin/env python3
"""Check (and optionally fix) special characters in Forensics Wiki Markdown prose.

MkDocs renders with the Python-Markdown engine, which does not consume
backslash escapes for '<' and '&' (a backslash shows up literally in the
page), and which passes an unescaped '<word>' in prose through as an HTML
tag that the browser swallows. The reliable way to render a literal '<',
'>' or '&' in prose is the corresponding HTML entity, so this tool enforces:

  * an '&' in prose                    -> '&amp;'
  * a '<token>' placeholder in prose   -> '&lt;token&gt;'
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
import re
import sys
from pathlib import Path

# Spans that are never prose (inline code, autolinks, link URL parts).
INLINE_CODE = re.compile(r"`[^`\n]*`")
AUTOLINK = re.compile(r"<[a-zA-Z][a-zA-Z0-9+.\-]*:[^<>\s]*>|<[^<>\s]*@[^<>\s]*>")
LINKURL = re.compile(r"\]\([^)\n]*\)")

# A '<token>' in prose. The name must not be a known HTML tag, otherwise the
# construct is intentional inline HTML rather than a placeholder.
TOKEN = re.compile(r"<[A-Za-z][A-Za-z0-9 ._\-]*?>")
SPLIT_OPEN = re.compile(r"<[A-Za-z][A-Za-z0-9 ._\-]*[ \t]*$")  # '<word …' at end of line
SPLIT_CLOSE = re.compile(r"^[A-Za-z0-9 ._\-]*>")               # '…>' at start of next line

# An '&' that already starts a valid HTML entity.
ENTITY = re.compile(r"&[a-zA-Z][a-zA-Z0-9]*;|&#[0-9]+;|&#[xX][0-9a-fA-F]+;")

# --fix replacement for each flagged character.
ENTITY_FOR = {"&": "&amp;", "<": "&lt;", ">": "&gt;"}

# Inline HTML the style guide allows (md033 allowed_elements and friends).
VALID_HTML_TAGS = {
    "sup", "sub", "br", "a", "span", "code", "kbd", "mark", "del", "ins",
    "strong", "em", "u", "i", "b", "small", "abbr", "s", "wbr", "img", "ol",
    "ul", "li", "blockquote", "p", "div", "table", "tr", "td", "th", "thead",
    "tbody", "caption", "figure", "figcaption", "details", "summary", "hr",
    "pre", "samp", "var", "q", "cite", "bdi", "bdo", "time", "data", "html",
    "head", "style", "body", "ui", "title", "meta", "link", "script",
    "section", "article",
}


def prose_lines(path: Path) -> list[tuple[int, str]]:
    """(lineno, line) for every line that may contain prose.

    Fenced code blocks and HTML comments never contain prose. A line that
    closes a multi-line comment still contributes the prose after its
    closing '-->'.
    """
    out = []
    in_fence = False
    fence_sig = ""
    in_comment = False
    with path.open(encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
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


def protected_spans(line: str) -> list[tuple[int, int]]:
    """Spans of inline code, autolinks and link URLs in a line."""
    spans = []
    for pattern in (INLINE_CODE, AUTOLINK, LINKURL):
        spans.extend(m.span() for m in pattern.finditer(line))
    return spans


def is_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= pos < end for start, end in spans)


def token_name(fragment: str) -> str:
    """Lower-cased name of a '<name …' or '<name>' fragment, or ''."""
    m = re.match(r"<([A-Za-z][A-Za-z0-9]*)", fragment)
    return m.group(1).lower() if m else ""


def is_placeholder(fragment: str, line: str, start: int) -> bool:
    """Whether the '<…>' at 'start' is a prose placeholder that needs escaping.

    Backslash-escaped '\\<…\\>' is already handled, and a token whose name is
    a known HTML tag is intentional inline HTML.
    """
    if start > 0 and line[start - 1] == "\\":
        return False
    return token_name(fragment) not in VALID_HTML_TAGS


def find_ampersand_targets(line: str, spans: list[tuple[int, int]]) -> set[int]:
    """Positions of '&' in prose that need '&amp;'."""
    targets = set()
    for i, ch in enumerate(line):
        if ch != "&" or is_protected(i, spans):
            continue
        if i > 0 and line[i - 1] == "\\":
            continue  # already backslash-escaped
        if ENTITY.match(line, i):
            continue  # already an HTML entity
        targets.add(i)
    return targets


def find_token_targets(line: str, spans: list[tuple[int, int]]) -> set[int]:
    """Positions of '<' and '>' of '<token>' placeholders that need '&lt;…&gt;'."""
    targets = set()
    for m in TOKEN.finditer(line):
        start, end = m.span()
        if is_protected(start, spans):
            continue
        if not is_placeholder(m.group(0), line, start):
            continue
        targets.update((start, end - 1))
    return targets


def find_split_token_targets(
    prose: list[tuple[int, str]],
) -> tuple[dict[int, set[int]], list[tuple[int, int]]]:
    """Flag '<token>' placeholders broken across a line break.

    The single-line rules above cannot see a '<word …' at the end of one
    prose line and the closing '…>' at the start of the next, so those are
    matched here.

    Returns (targets, pairs): targets maps a line number to the flagged
    positions on that line, and pairs the (open, close) line numbers for
    the extra report message.
    """
    targets: dict[int, set[int]] = {}
    pairs: list[tuple[int, int]] = []
    for (open_ln, open_line), (close_ln, close_line) in zip(prose, prose[1:]):
        open_m = SPLIT_OPEN.search(open_line)
        if not open_m or is_protected(open_m.start(), protected_spans(open_line)):
            continue
        if not is_placeholder(open_m.group(0), open_line, open_m.start()):
            continue
        close_m = SPLIT_CLOSE.match(close_line)
        if not close_m:
            continue
        close_pos = close_m.end() - 1
        if is_protected(close_pos, protected_spans(close_line)):
            continue
        targets.setdefault(open_ln, set()).add(open_m.start())
        targets.setdefault(close_ln, set()).add(close_pos)
        pairs.append((open_ln, close_ln))
    return targets, pairs


def file_report(
    path: Path,
) -> tuple[dict[int, set[int]], list[tuple[int, int]], dict[int, str]]:
    """All escaping targets of one file.

    Returns (targets, pairs, lines): targets maps a line number to the set
    of character positions that need an entity, pairs the split '<token>'
    line pairs for reporting, and lines the prose lines for the messages.
    """
    prose = prose_lines(path)
    targets: dict[int, set[int]] = {}
    for lineno, line in prose:
        spans = protected_spans(line)
        found = find_ampersand_targets(line, spans) | find_token_targets(line, spans)
        if found:
            targets[lineno] = found
    split, pairs = find_split_token_targets(prose)
    for lineno, found in split.items():
        targets.setdefault(lineno, set()).update(found)
    return targets, pairs, {ln: line for ln, line in prose}


def describe(pos: int, line: str) -> str:
    ch = line[pos]
    if ch == "&":
        return "unescaped '&' (use '&amp;')"
    if ch == "<":
        return "unescaped '<' of a '<token>' placeholder (use '&lt;token&gt;')"
    return "unescaped '>' of a '<token>' placeholder (use '&lt;token&gt;')"


def markdown_files(paths: list[str]) -> list[Path]:
    """Expand paths to the Markdown files they refer to (docs/ by default)."""
    files = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.is_file() and path.suffix == ".md":
            files.append(path)
    return files


def check_file(path: Path) -> int:
    """Print a report for one file; return the number of flagged characters."""
    targets, pairs, lines = file_report(path)
    for lineno in sorted(targets):
        for pos in sorted(targets[lineno]):
            print(f"{path}:{lineno}: {describe(pos, lines[lineno])} | "
                  f"{lines[lineno].strip()[:100]}")
    for open_ln, close_ln in pairs:
        print(f"{path}:{open_ln}: '<token>' placeholder is split across lines "
              f"{open_ln} and {close_ln}; keep tokens on one line or "
              f"escape both ends")
    return sum(len(positions) for positions in targets.values())


def fix_file(path: Path) -> int:
    """Escape the flagged characters in place; return the number fixed."""
    targets, _pairs, _lines = file_report(path)
    count = sum(len(positions) for positions in targets.values())
    if not count:
        return 0
    lines = path.read_text(encoding="utf-8").split("\n")
    for lineno in sorted(targets, reverse=True):
        line = lines[lineno - 1]
        for pos in sorted(targets[lineno], reverse=True):
            line = line[:pos] + ENTITY_FOR[line[pos]] + line[pos + 1:]
        lines[lineno - 1] = line
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"{path}: {count} entity(ies) added")
    return count


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Enforce HTML-entity escaping of '<', '>' and '&' in "
        "Markdown prose.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="report unescaped characters and exit 1 if found "
                      "(default)")
    mode.add_argument("--fix", action="store_true",
                      help="escape unescaped characters as HTML entities "
                      "in place")
    parser.add_argument("paths", nargs="*", default=["docs"],
                        help="Markdown files or directories (default: docs)")
    args = parser.parse_args(argv)

    total = 0
    affected = 0
    for path in markdown_files(args.paths):
        n = fix_file(path) if args.fix else check_file(path)
        total += n
        if n:
            affected += 1

    if args.fix:
        if total:
            print(f"\nFixed {total} unescaped character(s) across "
                  f"{affected} file(s).")
        else:
            print("Nothing to fix.")
        return 0

    if total:
        print(f"\nFound {total} unescaped character(s) in {affected} file(s).")
        print("Run 'python check_escaping.py --fix docs' to fix them "
              "automatically.")
        return 1
    print("No unescaped special characters found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
