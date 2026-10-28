# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Auto Post FB\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's find inputs, textareas, headings with text-white or text-stone-100/200/300/400
inputs = re.findall(r'<input[^>]+class=[\'\"][^\'\"]*text-white[^\'\"]*[\'\"][^>]*>', text)
print(f"Inputs with text-white in Auto Post FB: {len(inputs)}")
for inp in inputs[:10]:
    print(" ", inp)

textareas = re.findall(r'<textarea[^>]+class=[\'\"][^\'\"]*text-white[^\'\"]*[\'\"][^>]*>', text)
print(f"Textareas with text-white in Auto Post FB: {len(textareas)}")
for ta in textareas[:10]:
    print(" ", ta)

# Let's find cards with bg-white or bg-stone-50 that contain text-white directly
headings = re.findall(r'<h[1-6][^>]+class=[\'\"][^\'\"]*text-white[^\'\"]*[\'\"][^>]*>', text)
print(f"Headings with text-white in Auto Post FB: {len(headings)}")
for h in headings[:10]:
    print(" ", h)
