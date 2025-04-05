import re
import sys
from collections import Counter

if len(sys.argv) < 2:
    print("Molimo unesite putanju do log fajla kao argument.")
    sys.exit(1)

log_file_path = sys.argv[1]

file_pattern = re.compile(r'\b(?:[\w.]+\.)+\w+\.(cs|kt|java|py)\b')

error_files = Counter()

with open(log_file_path, "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            match = file_pattern.search(line)
            if match:
                error_files[match.group()] += 1

top_files = error_files.most_common(5)

print("Top 5 fajlova za popravku:\n")
for i, (filename, count) in enumerate(top_files, 1):
    print(f"{i}. {filename} — {count} grešaka")
