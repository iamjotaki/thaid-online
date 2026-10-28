# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ThaiD-Chat\static\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'\btext-white\b', text)]
print(f"Total occurrences of 'text-white' in ThaiD-Chat/index.html: {len(matches)}")

for i, idx in enumerate(matches):
    start = max(0, idx - 80)
    end = min(len(text), idx + 100)
    snippet = text[start:end].replace('\n', ' ')
    print(f"{i+1:2d}: ...{snippet}...")
