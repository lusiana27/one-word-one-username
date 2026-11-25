import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

for name in os.listdir(OUTPUT_DIR):
    path = os.path.join(OUTPUT_DIR, name)
    if os.path.isdir(path) and not os.path.islink(path):
        shutil.rmtree(path)
    else:
        os.remove(path)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="ascii", newline="") as f:
    f.write("nimble-raven-87")
