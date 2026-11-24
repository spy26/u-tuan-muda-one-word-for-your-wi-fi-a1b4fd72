"""One Word for Your Wi-Fi — make.fun entry.

Writes the single word "Potato" to stdout, and when the environment
variable MAKEFUN_OUTPUT_DIR is set, writes it (no trailing newline)
to <MAKEFUN_OUTPUT_DIR>/entry.txt as UTF-8.
"""

import os
import sys

WORD = "Potato"
WORD_BYTES = WORD.encode("utf-8")


def write_entry(directory):
    """Write WORD as raw UTF-8 bytes, no trailing newline."""
    target = os.path.join(directory, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(WORD_BYTES)


def main():
    sys.stdout.write(WORD + "\n")
    output_dir = os.getenv("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        write_entry(output_dir)


if __name__ == "__main__":
    main()
