#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to entry.txt in the output directory.

The letter is "A", standing for coffee. Its hidden word is "aroma":
the smell of fresh coffee is the most vivid, most alive thing about
either drink -- it fills a room before the first sip, it wakes people
up, and it is the truest single answer to the coffee-versus-tea
argument. One letter, nothing else, no punctuation, no newline.

Standard library only. No network. Fully deterministic: every run
writes the same single byte.
"""

import os

LETTER = "A"

if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isupper():
    raise ValueError("entry letter must be a single uppercase A-Z letter")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
