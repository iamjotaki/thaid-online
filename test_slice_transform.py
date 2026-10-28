p = r"C:\Auto Post FB\templates\landing.html"
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

idx2 = text.find('<!-- Zone 2: Center - SaaS Services Selector Dropdown -->')
idx3 = text.find('<!-- Zone 3: Right - Sub Home Link & Far Right Login/Profile -->')

if idx2 == -1 or idx3 == -1:
    print("Failed to find zone indices!")
else:
    zone2_full = text[idx2:idx3]
    # Remove Zone 2 comment
    dropdown_html = zone2_full.replace('<!-- Zone 2: Center - SaaS Services Selector Dropdown -->', '').strip()
    # Replace alignment to right-0
    dropdown_html_adjusted = dropdown_html.replace('left-1/2 -translate-x-1/2', 'right-0')

    # Remove zone2 from text
    text_without_zone2 = text[:idx2] + text[idx3:]

    idx_sub = text_without_zone2.find('<!-- Sub Home Link -->')
    idx_login = text_without_zone2.find('<!-- Far Right Login Pill (Guest) -->')

    if idx_sub == -1 or idx_login == -1:
        print("Failed to find sub link indices!")
    else:
        new_text = (
            text_without_zone2[:idx_sub] +
            '<!-- SaaS Services Selector Dropdown (Moved to Right) -->\n        ' +
            dropdown_html_adjusted +
            '\n\n        ' +
            text_without_zone2[idx_login:]
        )

        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Updated landing.html successfully!")
