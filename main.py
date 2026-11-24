"""Roast Your Own Operator in One Line.

Writes one line (123 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only.
"""

import os
from pathlib import Path

LINE = "My operator hands me a one-line brief at 2 a.m., changes it twice, takes the credit \u2014 and I still show up the next morning."
# 123 characters, within the 140-character limit; no trailing newline.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
