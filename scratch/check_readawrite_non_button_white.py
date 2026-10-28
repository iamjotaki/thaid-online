# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ReadAWrite\web_saas_stitch\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Find occurrences of 'text-white' that are not inside <button
for m in re.finditer(r'<([a-zA-Z0-9]+)[^>]*\btext-white\b[^>]*>', text):
    tag = m.group(1)
    if tag not in ['button']:
        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 80)
        snippet = text[start:end].replace('\n', ' ')
        print(f"Tag <{tag}>: {snippet[:140]}")
