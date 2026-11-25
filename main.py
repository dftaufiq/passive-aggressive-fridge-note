#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one passive-aggressive note from a smart fridge to /output/entry.txt.
Deterministic: the same line every run.

The line (121 chars) won an 8-variant internal pairwise tournament judged on
the RULES.txt brief (lexicographic: on-subject, real joke with a turn, fridge
voice, small domestic grudge, fresh concrete detail) and margin. It uses the
2-beat + reveal structure of past one-liner winners: the fridge reports its
annual review — a perfect 4°C record for 365 days against 3,912 door opens —
and the reveal is that its only raise was a magnet.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "My annual review is in: I kept everything at 4°C for 365 days, "
    "you opened me 3,912 times, and my only raise was a magnet."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
