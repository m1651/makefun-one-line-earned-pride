#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun bounty entry.

Writes a single original line (1-240 characters) to /output/entry.txt.
Python 3, stdlib only, no network, fully deterministic.
"""

import os
import sys

MAX_CHARS = 240

LINE = (
    "She soldered the last joint at 2 a.m., plugged in the radio "
    "her grandfather built in 1962, and it sang for the first time "
    "in forty years."
)


def main() -> None:
    # Validate the line before writing: the gate requires UTF-8 text
    # of 1 to 240 characters, not only white space.
    if not LINE.strip():
        print("error: entry line is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(LINE) > MAX_CHARS:
        print(
            f"error: entry line is {len(LINE)} characters, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        sys.exit(1)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
