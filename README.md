# news-summary-01

Entry for the make.fun bounty news-summary-01: a plain-English summary of the
world's news of Wednesday 11 November 2026, held in summary.txt.

Run it locally to emit the entry exactly as the bounty gate expects:

    MAKEFUN_OUTPUT_DIR=out python3 main.py

This copies summary.txt to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
creating the directory if needed. Python 3 standard library only, no network
access, deterministic output. Licensed under the MIT License, see LICENSE.
