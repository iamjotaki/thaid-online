with open(r'C:\ThaiD.online\app\page.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Remove tactile sheet handle
handle_pattern = r'\{\/\*\s*Tactile Sheet Handle[\s\S]*?<\/div>'
text = re.sub(handle_pattern, '', text)

# 2. Extract saasMenuRef block and move it to right zone, removing "หน้าแรกบริการ"
# First find Zone 2
saas_block_match = re.search(r'\{\/\*\s*Zone 2:\s*Center\s*-\s*SaaS Services Selector Dropdown\s*\*\/\}[\s\S]*?(?=\{\/\*\s*Zone 3:)', text)
if not saas_block_match:
    print("Could not find saas_block in page.tsx!")
else:
    saas_block = saas_block_match.group(0)
    # Adjust dropdown menu positioning from left-1/2 -translate-x-1/2 to right-0
    saas_block_adjusted = saas_block.replace("absolute left-1/2 -translate-x-1/2 top-full", "absolute right-0 top-full")
    # Remove Zone 2 comment
    saas_block_adjusted = re.sub(r'\{\/\*\s*Zone 2:\s*Center\s*-\s*SaaS Services Selector Dropdown\s*\*\/\}', '{/* SaaS Services Selector Dropdown (Moved to Right) */}', saas_block_adjusted)

    # Remove Zone 2 from its old place
    text = text.replace(saas_block, '')

    # In Zone 3, remove "หน้าแรกบริการ" link and insert saas_block_adjusted
    sub_home_link_pattern = r'\{\/\*\s*Link to Sub \/ Services Home\s*\*\/\}[\s\S]*?<\/a>'
    text = re.sub(sub_home_link_pattern, saas_block_adjusted.strip(), text)
    print("Transformed page.tsx navbar successfully!")

with open(r'C:\ThaiD.online\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(text)
