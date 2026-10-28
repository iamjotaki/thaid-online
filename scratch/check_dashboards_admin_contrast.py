# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

new_files = [
    r"C:\ThaiD-Sticker\static\dashboard.html",
    r"C:\ThaiD-Sticker\static\admin.html",
    r"C:\ThaiD-Clip\static\dashboard.html",
    r"C:\ThaiD-Clip\static\admin.html",
    r"C:\ThaiD-Chat\static\dashboard.html",
    r"C:\ThaiD-Chat\static\admin.html",
    r"C:\ThaiD-Mockup\static\dashboard.html",
    r"C:\ThaiD-Mockup\static\admin.html",
    r"C:\ThaiD-Vault\static\admin.html",
    r"C:\ReadAWrite\web_saas_stitch\dashboard.html",
    r"C:\ReadAWrite\web_saas_stitch\admin.html",
    r"C:\ThaiD.online\app\admin\page.tsx"
]

for p in new_files:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Find all text-white occurrences
    tw = [m.start() for m in re.finditer(r'\btext-white\b', c)]
    print(f"\n==========================================")
    print(f"File: {p} (text-white count: {len(tw)})")
    for i, idx in enumerate(tw[:10]):
        snippet = c[max(0, idx-50):min(len(c), idx+60)].replace('\n', ' ')
        print(f"  {i+1}: ...{snippet}...")
