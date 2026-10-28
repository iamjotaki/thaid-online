import os
import re

targets = [
    r'C:\ThaiD-Mockup\static\index.html',
    r'C:\ThaiD-Clip\static\index.html',
    r'C:\ThaiD-Chat\static\index.html',
    r'C:\ThaiD-Sticker\static\index.html',
    r'C:\ReadAWrite\web_saas_stitch\index.html',
    r'C:\Auto Post FB\templates\landing.html',
]

vault_menu_pattern = re.compile(
    r'<a\s+href="https://vault\.thaid\.online"\s+class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">[\s\S]*?</a>\s*',
    re.MULTILINE
)

vault_profile_pattern = re.compile(
    r'<a\s+href="https://vault\.thaid\.online"\s+class="flex items-center justify-between px-2 py-1\.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors">[\s\S]*?</a>\s*',
    re.MULTILINE
)

for path in targets:
    if not os.path.exists(path):
        print("Missing:", path)
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Remove from saas dropdown
    c = vault_menu_pattern.sub('', c)
    # 2. Update 7 เครื่องมือ to 6 เครื่องมือ
    c = c.replace('7 เครื่องมือ', '6 เครื่องมือ')
    # 3. Remove from profile dropdown
    c = vault_profile_pattern.sub('', c)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Updated {path}: vault removed cleanly!")
