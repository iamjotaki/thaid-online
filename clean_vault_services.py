path = r'C:\ThaiD.online\app\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, l in enumerate(lines):
    if 'id: "vault"' in l:
        skip = True
        # remove previous opening brace if on previous line
        if new_lines and new_lines[-1].strip() == '{':
            new_lines.pop()
        continue
    if skip:
        if l.strip() == '},':
            skip = False
            continue
        continue
    new_lines.append(l)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Removed vault cleanly from SERVICES array!")
