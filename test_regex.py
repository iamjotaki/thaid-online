import re

p = r"C:\Auto Post FB\templates\landing.html"
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for Zone 2 saas dropdown
zone2_pattern = r'<!-- Zone 2: Center - SaaS Services Selector Dropdown -->\s*<div class="relative" id="thaidSaasDropdownWrap">[\s\S]*?</div>\s*</div>\s*</div>'
m = re.search(zone2_pattern, text)
print('Found Zone 2:', bool(m))

sub_link_pattern = r'<!-- Sub Home Link -->\s*<a href="https://[a-z0-9.-]+\.thaid\.online" class="hidden sm:inline-flex[\s\S]*?</a>'
m2 = re.search(sub_link_pattern, text)
print('Found Sub Home Link:', bool(m2))
