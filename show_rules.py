import json

with open('fastwork_details.json', 'r', encoding='utf-8') as f:
    rules = json.load(f)

for r in rules:
    sel = r.get('selector', '')
    if any(k in sel for k in ['scroll-cue', 'hero-cta', 'profile-name', 'card-hit', 'profile-cover', 'avatar']):
        print("=== " + sel + " ===")
        print(r.get('css', ''))
