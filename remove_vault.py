import os
import re

path = r'C:\ThaiD.online\app\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update category type definition
content = content.replace(
    'category: "novel" | "social" | "sticker" | "clip" | "chat" | "mockup" | "vault";',
    'category: "novel" | "social" | "sticker" | "clip" | "chat" | "mockup";'
)

# 2. Remove Personal Vault from saasServices array
vault_saas_pattern = r'\{\s*name:\s*"Personal Vault"[\s\S]*?badge:\s*"AES-256"[\s\S]*?icon:\s*\([\s\S]*?\)\s*\},'
content = re.sub(vault_saas_pattern, '', content)

# 3. Update "7 เครื่องมือ" to "6 เครื่องมือ"
content = content.replace('7 เครื่องมือ', '6 เครื่องมือ')
content = content.replace('รวม 7 เครื่องมือ AI Studio', 'รวม 6 เครื่องมือ AI Studio')

# 4. Remove "ไปที่ Security Vault" link from Profile Menu
profile_vault_pattern = r'<a\s+href="https://vault\.thaid\.online"[\s\S]*?<span>ไปที่ Security Vault</span>[\s\S]*?</a>'
content = re.sub(profile_vault_pattern, '', content)

# 5. Remove vault_1 from FLOATING_CARDS
floating_vault_pattern = r'\{\s*id:\s*"vault_1"[\s\S]*?url:\s*"https://vault\.thaid\.online"\s*\},'
content = re.sub(floating_vault_pattern, '', content)

# 6. Remove vault service card from SERVICES array
services_vault_pattern = r'\{\s*id:\s*"vault"[\s\S]*?actionText:\s*"เปิดใช้งาน ThaiD Vault"\s*\},'
content = re.sub(services_vault_pattern, '', content)

# 7. Remove vault category from category filter tabs
content = content.replace('{ id: "vault", label: "Vault Security" },\n', '')
content = content.replace('{ id: "vault", label: "Vault Security" },', '')

# 8. Remove footer link
footer_vault_pattern = r'<li><a href="https://vault\.thaid\.online"[^>]*>Security Vault</a></li>\n?'
content = re.sub(footer_vault_pattern, '', content)
content = content.replace('<a href="https://vault.thaid.online" className="hover:text-[#171717] transition-colors">Security Vault</a>', '')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app/page.tsx: removed vault successfully!")
