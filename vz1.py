import sys
from collections import Counter
import re

if len(sys.argv) < 2:
    print("Greška: nije prosleđen log fajl.")
    sys.exit(1)

log_file_path = sys.argv[1]

with open(log_file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

levels = [re.search(r"\[(.*?)\] (\w+)", line).group(2) for line in lines if re.search(r"\[(.*?)\] (\w+)", line)]
counter = Counter(levels)

print("Analiza nivoa logova:\n")
for level, count in counter.items():
    print(f"{level}: {count}")
