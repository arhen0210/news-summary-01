"""Emits the news-summary-01 entry: summary.txt copied to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
import shutil

OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT = "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "summary.txt")
    out_dir = os.environ.get(OUTPUT_ENV, DEFAULT_OUTPUT)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    return dst


if __name__ == "__main__":
    print("wrote", main())
