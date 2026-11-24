#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short funny rant (<=400 chars, no trailing newline) to
/output/entry.txt: a neighbour, a leaf blower, and three leaves.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")

RANT = (
    "My neighbour fires up his leaf blower every Saturday at 7 a.m. "
    "to move three leaves from his driveway onto mine. Three leaves. "
    "Forty minutes of a machine louder than a jet engine to do a job "
    "gravity was already doing for free."
)


def main() -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one rant, no trailing newline: the gate counts 1-400 chars.
    with ENTRY_PATH.open("w", encoding="utf-8", newline="") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
