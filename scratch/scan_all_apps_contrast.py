# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

apps = [
    ("ThaiD-Clip", r"C:\ThaiD-Clip\static\index.html"),
    ("ThaiD-Chat", r"C:\ThaiD-Chat\static\index.html"),
    ("ThaiD-Mockup", r"C:\ThaiD-Mockup\static\index.html"),
    ("ThaiD-Vault", r"C:\ThaiD-Vault\static\index.html"),
    ("ReadAWrite", r"C:\ReadAWrite\web_saas_stitch\index.html"),
    ("Auto Post FB", r"C:\Auto Post FB\templates\index.html")
]

for name, path in apps:
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    print(f"\n==========================================")
    print(f"APP: {name} ({path})")
    
    # Find text-white not inside dark buttons (e.g. not followed by or inside bg-black / bg-[#171717] / bg-blue / bg-emerald)
    # Let's inspect all text-white occurrences
    tw_matches = [m.start() for m in re.finditer(r'\btext-white\b', content)]
    print(f"Total text-white occurrences: {len(tw_matches)}")
    for i, idx in enumerate(tw_matches[:15]):
        start = max(0, idx - 60)
        end = min(len(content), idx + 80)
        snippet = content[start:end].replace('\n', ' ')
        print(f"  {i+1}: ...{snippet}...")
