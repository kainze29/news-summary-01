#!/usr/bin/env python3
"""news-summary-01 entry: write the stored summary to the output file.

The summary (summary.txt, beside this file) is a fixed text written for
Wednesday 11 November 2026. The program does no network access and no
computation that could vary between runs: it reads the file and writes it
unchanged, so two runs always produce the same bytes.

Run locally with:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The grader runs it with /output as the output directory.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = (HERE / "summary.txt").read_text(encoding="utf-8")
    # Fail fast if the stored summary ever breaks the gate (1-2000 chars).
    if not (1 <= len(text) <= 2000 and text.strip()):
        raise SystemExit("summary.txt breaks the 1-2000 character gate")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
