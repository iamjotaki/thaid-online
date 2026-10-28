# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Auto Post FB\templates\landing.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "text-white" in l:
        print(f"Line {i+1}: {l.strip()}")
