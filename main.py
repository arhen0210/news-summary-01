# news-summary-01: copies summary.txt to the make.fun output dir as entry.txt
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "summary.txt")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
dst = os.path.join(out_dir, "entry.txt")

os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, dst)
print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
