#!/usr/bin/env python3
"""Validate the tags in Forensics Wiki article front matter.

Articles carry their tags in the YAML front matter, for example:

    ---
    tags:
      - Disk Analysis
      - Tools
    ---

Only the tags registered in scripts/allowed_tags.yml may be used. The tag
tables in style_guide.md carry the descriptions of the registered tags,
and this file is the machine-readable registry. Unregistered tags would
show up as stray tag pages on the site and split related articles over
near-duplicate tags, so they are flagged here instead.

Files without front matter or without a 'tags' key (e.g. community.md or
index.md) are not articles and are skipped.

Usage:
    python check_tags.py [--check | --list] [--config allowed_tags.yml] [paths ...]

Defaults to --check over the docs directory and exits 1 when an
unregistered tag is found, so it can be used as a CI check. --list shows
every registered tag with the number of articles that use it.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# The registry lives next to this script, so the check works from any
# working directory.
DEFAULT_CONFIG = Path(__file__).resolve().parent / "allowed_tags.yml"

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
TAGS_KEY = re.compile(r"^tags:\s*(#.*)?$")
TAG_ITEM = re.compile(r"^\s+-\s+(.+?)\s*$")


def load_registered_tags(config: Path) -> list[str]:
    """The tags registered under 'tags:' in the YAML config file."""
    if not config.is_file():
        raise SystemExit(f"error: tag registry not found: {config}")
    tags = []
    in_tags = False
    for raw in config.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if TAGS_KEY.match(raw):
            in_tags = True
            continue
        item = TAG_ITEM.match(raw)
        if item and in_tags:
            tags.append(item.group(1))
            continue
        if in_tags:
            break  # another top-level key ends the list
        if raw.startswith("tags:"):
            raise SystemExit(
                f"error: {config}: unsupported 'tags' syntax; use a block "
                "list of '- tag' items (see the file header)")
    if not tags:
        raise SystemExit(f"error: no tags registered in {config}")
    return tags


def front_matter_tags(path: Path) -> list[tuple[int, str, str]]:
    """(lineno, tag, line) for each tag in the article front matter.

    Line numbers point at the tag item itself, so the report can quote
    the line. Returns [] for files without front matter or without a
    'tags' key.
    """
    m = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    if not m:
        return []
    tags = []
    in_tags = False
    for lineno, line in enumerate(m.group(1).split("\n"), start=2):
        if TAGS_KEY.match(line):
            in_tags = True
            continue
        item = TAG_ITEM.match(line)
        if item and in_tags:
            tags.append((lineno, item.group(1), line))
            continue
        if in_tags and line and not line[0].isspace():
            break  # another top-level key ends the tag list
        if line.startswith("tags:"):
            raise ValueError(
                "unsupported inline 'tags' syntax in the front matter; "
                "use a block list of '- tag' items")
    return tags


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


def check_file(path: Path, allowed: set[str], config: Path) -> tuple[int, list[str]]:
    """Report the unregistered tags of one article.

    Returns (unknown_tag_count, error_messages).
    """
    try:
        found = front_matter_tags(path)
    except ValueError as exc:
        return 0, [str(exc)]
    unknown = 0
    for lineno, tag, line in found:
        if tag in allowed:
            continue
        unknown += 1
        print(f"{path}:{lineno}: unregistered tag {tag!r} (add it to "
              f"{config}, and a description to style_guide.md) | "
              f"{line.strip()[:100]}")
    return unknown, []


def count_tags(path: Path) -> tuple[Counter[str], list[str]]:
    """(usage counter, error_messages) of the tags of one article."""
    try:
        return Counter(tag for _lineno, tag, _line in front_matter_tags(path)), []
    except ValueError as exc:
        return Counter(), [str(exc)]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Flag tags in article front matter that are not "
        "registered in the tag registry.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="report unregistered tags and exit 1 if found "
                      "(default)")
    mode.add_argument("--list", action="store_true",
                      help="show the registered tags and how the articles "
                      "use them")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG),
                        help="tag registry YAML file (default: %(default)s)")
    parser.add_argument("paths", nargs="*", default=["docs"],
                        help="Markdown files or directories (default: docs)")
    args = parser.parse_args(argv)

    config = Path(args.config)
    registered = load_registered_tags(config)
    allowed = set(registered)
    files = markdown_files(args.paths)

    if args.list:
        usage: Counter[str] = Counter()
        errors: list[tuple[Path, str]] = []
        for path in files:
            file_usage, file_errors = count_tags(path)
            usage.update(file_usage)
            errors.extend((path, message) for message in file_errors)
        for tag in registered:
            n = usage.get(tag, 0)
            mark = "" if n else "  (unused)"
            print(f"{n:5d}  {tag}{mark}")
        for path, message in errors:
            print(f"{path}: error: {message}")
        print(f"\n{len(registered)} registered tag(s), "
              f"{sum(1 for t in registered if usage.get(t))} used by "
              "articles.")
        return 1 if errors else 0

    total = 0
    affected = 0
    errors = 0
    for path in files:
        unknown, errs = check_file(path, allowed, config)
        total += unknown
        errors += len(errs)
        if errs:
            for err in errs:
                print(f"{path}: error: {err}")
        if unknown:
            affected += 1

    if total:
        print(f"\nFound {total} unregistered tag(s) in {affected} file(s).")
        print(f"Register them in {config} (and in the tag tables of "
              "style_guide.md) or use an existing tag.")
        return 1
    if errors:
        print(f"\n{errors} front matter error(s).")
        return 1
    print("No unregistered tags found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
