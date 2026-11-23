#!/usr/bin/env python3
"""Write the entry word to /output/entry.txt.

The competition takes exactly one word, the first that comes to mind.
Petrichor: the smell of rain on dry earth after a long dry spell.
"""

import os

WORD = "Petrichor"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD + "\n")
    # Round-trip check: the file must hold exactly the word and nothing else.
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != WORD + "\n":
        raise SystemExit(f"entry.txt mismatch: {written!r}")


if __name__ == "__main__":
    main()
