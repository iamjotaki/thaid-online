# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Auto Post FB\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Find occurrences of 'text-white' that are not 'dark:text-white' and not inside dark buttons
matches = []
for m in re.finditer(r'(?<!dark:)\btext-white\b', text):
    start = max(0, m.start() - 60)
    end = min(len(text), m.end() + 80)
    snippet = text[start:end].replace('\n', ' ')
    matches.append(snippet)

print(f"Total pure text-white (not dark:text-white) in social index.html: {len(matches)}")
for i, s in enumerate(matches[:30]):
    print(f"{i+1:2d}: ...{s}...")
