#!/usr/bin/env python3
"""Say What Actually Broke -- make.fun entry.

Writes one honest, funny error line (a single line, at most
200 characters) to /output/entry.txt. Pure standard library.
"""

import os

ENTRY = (
    "Error 500: The database is innocent. I deployed on a Friday, "
    "skipped the tests, dropped the wrong table, and blamed the "
    "network. The bug was me all along."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert text == ENTRY.strip(), "entry must have no leading/trailing space"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
