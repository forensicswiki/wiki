#!/usr/bin/env python3
"""Check (and optionally fix) non-ASCII whitespace and punctuation in Forensics Wiki Markdown.

The style guide asks authors to "use the ASCII character set for punctuation
as much as possible". Non-ASCII whitespace (no-break spaces that creep in
from copy & paste) and non-ASCII punctuation (smart quotes, long dashes,
ellipses) undermine searching, diffing and consistent rendering, so this
tool flags both in Markdown prose.

A character is flagged when, by its Unicode category, it is:

  * non-ASCII whitespace : category Zs (e.g. U+00A0, U+2009, U+3000) plus the
    invisible glue characters (soft hyphen U+00AD, zero-width space U+200B,
    zero-width non-joiner U+200C, zero-width joiner U+200D, word joiner
    U+2060, BOM U+FEFF)
  * non-ASCII punctuation: category P* above the ASCII range (e.g. the smart
    quotes U+2018-U+201D, the en/em dashes U+2013/U+2014 and the ellipsis
    U+2026)

Non-ASCII letters (e.g. accented personal names) are deliberately not
flagged; only whitespace and punctuation are in scope.

Never flagged: fenced code blocks, HTML comments, inline code spans,
autolinks, the URL part of Markdown links and inline HTML tags.

Usage:
    python check_nonascii.py [--check | --fix] [paths ...]

Defaults to --check over the docs directory and exits 1 when non-ASCII
characters are found, so it can be used as a CI check. --fix rewrites the
files in place, replacing the flagged characters with their ASCII
equivalents where unambiguous (whitespace becomes a space, quotes become
straight quotes, dashes become '-' and the ellipsis becomes '...');
characters without a safe ASCII equivalent are left in place and reported.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# Spans that are never prose (inline code, autolinks, link URL parts and
# inline HTML tags, which may legitimately contain non-ASCII in attributes).
INLINE_CODE = re.compile(r"`[^`\n]*`")
AUTOLINK = re.compile(r"<[a-zA-Z][a-zA-Z0-9+.\-]*:[^<>\s]*>|<[^<>\s]*@[^<>\s]*>")
LINKURL = re.compile(r"\]\([^)\n]*\)")
HTML_TAG = re.compile(r"<[A-Za-z][^<>]*>")

# Invisible glue characters: not whitespace (category Cf) and not flagged by
# the Zs test, but they break searchability just as much as real spaces do.
INVISIBLE = {
    "\u00ad",  # soft hyphen
    "\u200b",  # zero-width space
    "\u200c",  # zero-width non-joiner
    "\u200d",  # zero-width joiner
    "\u2060",  # word joiner
    "\ufeff",  # zero-width no-break space (BOM)
}

# Non-ASCII characters that --fix can safely replace by hand.
FIXABLE = {
    "\u2018": "'",    # left single quotation mark
    "\u2019": "'",    # right single quotation mark
    "\u201c": '"',    # left double quotation mark
    "\u201d": '"',    # right double quotation mark
    "\u2013": "-",    # en dash
    "\u2014": "-",    # em dash
    "\u2026": "...",  # horizontal ellipsis
}


def prose_lines(path: Path) -> list[tuple[int, str]]:
    """(lineno, line) for every line that may contain prose.

    Fenced code blocks and HTML comments never contain prose and are skipped
    (a line that closes a multi-line comment still contributes its prose
    after the closing '-->').
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
    """Spans of inline code, autolinks, link URLs and HTML tags in a line."""
    spans = []
    for pattern in (INLINE_CODE, AUTOLINK, LINKURL, HTML_TAG):
        spans.extend(m.span() for m in pattern.finditer(line))
    return spans


def is_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= pos < end for start, end in spans)


def is_nonascii_whitespace(ch: str) -> bool:
    return ord(ch) > 127 and (
        unicodedata.category(ch) == "Zs" or ch in INVISIBLE
    )


def is_nonascii_punctuation(ch: str) -> bool:
    return ord(ch) > 127 and unicodedata.category(ch).startswith("P")


def find_targets(line: str) -> set[int]:
    """Positions of non-ASCII whitespace or punctuation on this prose line."""
    spans = protected_spans(line)
    return {
        i
        for i, ch in enumerate(line)
        if (is_nonascii_whitespace(ch) or is_nonascii_punctuation(ch))
        and not is_protected(i, spans)
    }


def file_report(path: Path) -> tuple[dict[int, set[int]], dict[int, str]]:
    """All flagged characters of a file.

    Returns (targets, lines): targets maps a line number to the flagged
    character positions on that line, and lines the prose lines for the
    report messages.
    """
    prose = prose_lines(path)
    targets: dict[int, set[int]] = {}
    for lineno, line in prose:
        found = find_targets(line)
        if found:
            targets[lineno] = found
    return targets, {ln: line for ln, line in prose}


def suggested_fix(ch: str) -> str | None:
    """The ASCII replacement --fix applies, or None when there is no safe one."""
    if ch in FIXABLE:
        return FIXABLE[ch]
    if is_nonascii_whitespace(ch):
        return "" if ch in INVISIBLE else " "
    return None


def describe(ch: str) -> str:
    cp = ord(ch)
    name = unicodedata.name(ch, "UNKNOWN")
    kind = "whitespace" if is_nonascii_whitespace(ch) else "punctuation"
    return f"non-ASCII {kind} {name} (U+{cp:04X})"


def hint(ch: str) -> str:
    fix = suggested_fix(ch)
    if fix == "":
        return "remove"
    if fix is not None:
        return f"replace with {fix!r}"
    return "no automatic fix, change manually"


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
    """Print a report for one file; return the number of flagged characters.

    Report one line per distinct character on a line (with its count), so
    a line full of em dashes stays readable.
    """
    targets, lines = file_report(path)
    count = 0
    for lineno in sorted(targets):
        line = lines[lineno]
        by_char: dict[str, int] = {}
        for pos in targets[lineno]:
            by_char[line[pos]] = by_char.get(line[pos], 0) + 1
        for ch in sorted(by_char, key=ord):
            count += by_char[ch]
            suffix = f", {by_char[ch]}x" if by_char[ch] > 1 else ""
            print(f"{path}:{lineno}: {describe(ch)}{suffix}; {hint(ch)} | "
                  f"{line.strip()[:100]}")
    return count


def fix_file(path: Path) -> tuple[int, int]:
    """Replace fixable characters in place; return (fixed, left_in_place)."""
    targets, _lines = file_report(path)
    if not targets:
        return 0, 0
    lines = path.read_text(encoding="utf-8").split("\n")
    fixed = 0
    left = 0
    for lineno in sorted(targets, reverse=True):
        line = lines[lineno - 1]
        for pos in sorted(targets[lineno], reverse=True):
            replacement = suggested_fix(line[pos])
            if replacement is None:
                left += 1
                continue
            line = line[:pos] + replacement + line[pos + 1:]
            fixed += 1
        lines[lineno - 1] = line
    if fixed:
        path.write_text("\n".join(lines), encoding="utf-8")
    return fixed, left


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Flag non-ASCII whitespace and punctuation in Markdown prose.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="report non-ASCII characters and exit 1 if found (default)")
    mode.add_argument("--fix", action="store_true",
                      help="replace non-ASCII characters with ASCII "
                      "equivalents in place")
    parser.add_argument("paths", nargs="*", default=["docs"],
                        help="Markdown files or directories (default: docs)")
    args = parser.parse_args(argv)

    total = 0
    affected = 0
    left_total = 0
    for path in markdown_files(args.paths):
        if args.fix:
            fixed, left = fix_file(path)
            total += fixed
            left_total += left
            if fixed:
                affected += 1
            if fixed or left:
                note = f", {left} left in place" if left else ""
                print(f"{path}: {fixed} character(s) fixed{note}")
        else:
            n = check_file(path)
            total += n
            if n:
                affected += 1

    if args.fix:
        if total:
            print(f"\nFixed {total} non-ASCII character(s) across {affected} file(s).")
        else:
            print("Nothing to fix.")
        if left_total:
            print(f"{left_total} character(s) have no ASCII equivalent and "
                  "were left in place.")
        return 0

    if total:
        print(f"\nFound {total} non-ASCII character(s) in {affected} file(s).")
        print("Run 'python check_nonascii.py --fix docs' to fix the ones that "
              "have an ASCII equivalent.")
        return 1
    print("No non-ASCII whitespace or punctuation found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
