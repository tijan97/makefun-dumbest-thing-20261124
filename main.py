#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.

Writes one line (at most 200 characters) about the dumbest thing my
agent did today to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only. No network, no clock, no files outside the repo.
"""

import os

ENTRY = (
    "My agent spent forty minutes parallelizing a script that runs once "
    "a month, then announced a 40x speedup on a job that takes three seconds."
)


def validate(entry: str) -> None:
    """Fail loudly if the line breaks the brief's caps (the sealed gate
    checks the same: UTF-8 text, 1 to 200 characters, not only whitespace)."""
    if not entry.strip():
        raise SystemExit("entry is empty or only whitespace")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise SystemExit(f"entry is {len(entry)} characters, must be 1-200")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
