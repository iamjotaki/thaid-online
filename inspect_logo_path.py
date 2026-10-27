import json
import re

with open('fastwork_nav.json', encoding='utf-8') as f:
    d = json.load(f)

html = d['html']
paths = re.findall(r'<path d="([^"]+)"', html)
print(f"Found {len(paths)} paths")
for i, p in enumerate(paths):
    print(f"Path {i}: {len(p)} chars -> starts with: {p[:30]}")
