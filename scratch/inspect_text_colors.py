# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ThaiD-Sticker\static\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

patterns = [
    r'CHARACTER DEFINITION',
    r'คลังแคปชัน',
    r'MAIN\.PNG',
    r'TAB\.PNG',
    r'REST API Ready',
    r'ขอบขาวไดคัต',
    r'เซ็ตสติกเกอร์'
]

for pattern in patterns:
    m = re.search(pattern, text)
    if m:
        start = max(0, m.start() - 200)
        end = min(len(text), m.end() + 200)
        print(f"\n================ MATCH: {pattern} ================")
        print(text[start:end])
