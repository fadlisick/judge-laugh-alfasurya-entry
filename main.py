"""Make the AI Judge Laugh - one-line office joke entry.

Writes a single joke line about office life to /output/entry.txt.
The program takes no input and produces exactly one line, no trailing
newline, so the grader reads the joke exactly as written.
"""

import os
from pathlib import Path

JOKE = "The best part of working from home is muting myself to sigh in surround sound."


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke line must be 1-200 characters")
    if "\n" in JOKE:
        raise ValueError("joke line must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
