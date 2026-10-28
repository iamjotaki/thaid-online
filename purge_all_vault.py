import re

# 1. Update C:\ThaiD.online\app\page.tsx
page_path = r"C:\ThaiD.online\app\page.tsx"
with open(page_path, 'r', encoding='utf-8') as f:
    page_content = f.read()

# Remove vault_1 block
floating_card_pattern = r'\{\s*id:\s*"vault_1",[\s\S]*?price:\s*"Hardware Key",\s*\},?'
page_content = re.sub(floating_card_pattern, '', page_content)

with open(page_path, 'w', encoding='utf-8') as f:
    f.write(page_content)
print("Updated page.tsx: removed vault_1 card")

# 2. Update C:\ThaiD.online\app\components\OrbitShowcase.tsx
orbit_path = r"C:\ThaiD.online\app\components\OrbitShowcase.tsx"
with open(orbit_path, 'r', encoding='utf-8') as f:
    orbit_content = f.read()

orbit_vault_pattern = r'\{\s*id:\s*"vault",[\s\S]*?badge:\s*"Military Security",\s*\},?'
orbit_content = re.sub(orbit_vault_pattern, '', orbit_content)

with open(orbit_path, 'w', encoding='utf-8') as f:
    f.write(orbit_content)
print("Updated OrbitShowcase.tsx: removed vault item")

# 3. Update all 6 subdomains: footers & extra references
subs = [
    r"C:\ReadAWrite\web_saas_stitch\index.html",
    r"C:\Auto Post FB\templates\landing.html",
    r"C:\ThaiD-Sticker\static\index.html",
    r"C:\ThaiD-Clip\static\index.html",
    r"C:\ThaiD-Chat\static\index.html",
    r"C:\ThaiD-Mockup\static\index.html"
]

for sub in subs:
    with open(sub, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Remove any footer or body link to vault.thaid.online
    c = re.sub(r'<a\s+href="https://vault\.thaid\.online"[^>]*>[\s\S]*?</a>\s*', '', c)
    # Replace "ThaiD Vault" mentions in chat
    c = c.replace("80 คีย์จาก ThaiD Vault", "80 คีย์ความเร็วสูงระดับ Enterprise")
    
    with open(sub, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Purged vault links from {sub}")

# 4. Clean up ThaiD-Vault index.html JS
vault_html = r"C:\ThaiD-Vault\static\index.html"
with open(vault_html, 'r', encoding='utf-8') as f:
    vc = f.read()

# Remove unused toggleThaiDSaasMenu function
vc = re.sub(r'function toggleThaiDSaasMenu\(\)[\s\S]*?function openThaiDSaasMenu', 'function openThaiDSaasMenu', vc)
vc = re.sub(r'function openThaiDSaasMenu\(\)[\s\S]*?function closeThaiDSaasMenu', 'function closeThaiDSaasMenu', vc)
vc = re.sub(r'function closeThaiDSaasMenu\(\)[\s\S]*?function toggleThaiDUserMenu', 'function toggleThaiDUserMenu', vc)

with open(vault_html, 'w', encoding='utf-8') as f:
    f.write(vc)
print("Cleaned up ThaiD-Vault index.html JS")
