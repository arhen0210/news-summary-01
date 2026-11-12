# news-summary-01: copies summary.txt (next to this file) into the make.fun
# output directory as entry.txt. Stdlib only, deterministic, no network.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "summary.txt")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
print("wrote", os.path.join(out_dir, "entry.txt"))
