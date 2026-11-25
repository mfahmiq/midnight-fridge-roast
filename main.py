#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun text bounty entry.

Writes one funny single-line roast of a smart fridge that refuses to
open after midnight to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The entry line (84 characters, 86 bytes, one line, spoken at the fridge door):

    My fridge has a VIP list after midnight, and apparently I'm not
    on it — I live here.

Why this line won the internal tournament (16 candidates, pairwise
against the judge brief in weight order — see CANDIDATES.md): it is
a one-line roast of exactly the target (a smart fridge refusing to
open after midnight); the punchline is a genuine surprise turn
("I live here" — the owner is not on his own fridge's VIP list);
it is tight, one joke, reads cleanly aloud; and the laugh comes
directly from the fridge's petty rule, not from generic smart-home
grumbling.

Deterministic, Python standard library only. Self-verifies the entry:
UTF-8 text, 1-200 characters, a single line, not whitespace-only.
Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "My fridge has a VIP list after midnight, "
    "and apparently I'm not on it — I live here."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification: UTF-8, 1-200 chars, single line, not whitespace-only.
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if not 1 <= len(ENTRY) <= 200:
        print(f"FAIL: entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1

    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry must be a single line", file=sys.stderr)
        return 1

    if not ENTRY.strip():
        print("FAIL: entry must not be whitespace-only", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)

    # Re-read and confirm the written file matches exactly.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY:
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
