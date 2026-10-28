import re

sub_files = [
    r"C:\ReadAWrite\web_saas_stitch\index.html",
    r"C:\Auto Post FB\templates\landing.html",
    r"C:\ThaiD-Sticker\static\index.html",
    r"C:\ThaiD-Clip\static\index.html",
    r"C:\ThaiD-Chat\static\index.html",
    r"C:\ThaiD-Mockup\static\index.html"
]

for p in sub_files:
    print(f"=== Processing {p} ===")
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()

    # Match Zone 2 block:
    # From <!-- Zone 2: Center - SaaS Services Selector Dropdown --> to right before <!-- Zone 3: Right
    zone2_regex = r'(<!-- Zone 2: Center - SaaS Services Selector Dropdown -->\s*<div class="relative" id="thaidSaasDropdownWrap">[\s\S]*?</div>\s*</div>\s*)(?=\s*<!-- Zone 3:)'
    m = re.search(zone2_regex, text)
    if not m:
        # Alternative without trailing </div>
        zone2_regex = r'(<!-- Zone 2: Center - SaaS Services Selector Dropdown -->\s*<div class="relative" id="thaidSaasDropdownWrap">[\s\S]*?</div>\s*)(?=\s*<!-- Zone 3:)'
        m = re.search(zone2_regex, text)
    
    if not m:
        print(f"FAILED to match Zone 2 in {p}!")
        continue

    zone2_full = m.group(1)
    
    # Extract only the div thaidSaasDropdownWrap
    dropdown_match = re.search(r'(<div class="relative" id="thaidSaasDropdownWrap">[\s\S]*?</div>\s*</div>)', zone2_full)
    if not dropdown_match:
        dropdown_match = re.search(r'(<div class="relative" id="thaidSaasDropdownWrap">[\s\S]*?</div>)', zone2_full)
    
    dropdown_html = dropdown_match.group(1)
    # Adjust alignment to right-0
    dropdown_html_adjusted = dropdown_html.replace('left-1/2 -translate-x-1/2', 'right-0')

    # Remove Zone 2 from text
    text_without_zone2 = text.replace(zone2_full, '')

    # Sub Home Link pattern in Zone 3:
    sub_link_pattern = r'<!-- Sub Home Link -->\s*<a href="https://[a-z0-9.-]+\.thaid\.online" class="hidden sm:inline-flex[\s\S]*?</a>'
    
    if not re.search(sub_link_pattern, text_without_zone2):
        print(f"FAILED to match Sub Home Link in {p}!")
        continue

    # Replace Sub Home Link with dropdown_html_adjusted
    new_text = re.sub(sub_link_pattern, f'<!-- SaaS Services Selector Dropdown (Moved to Right) -->\n        {dropdown_html_adjusted.strip()}', text_without_zone2)

    with open(p, 'w', encoding='utf-8') as f:
        f.write(new_text)

    print(f"Successfully updated navbar in {p}!")
