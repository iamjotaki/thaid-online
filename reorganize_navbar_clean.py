import sys

path = r"C:\Auto Post FB\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

idx_saas_start = text.find('<!-- SaaS Services Selector Dropdown (Standard ThaiD Unified) -->')
idx_auth_start = text.find('<!-- Google Account Login / Profile Indicator -->')
if idx_saas_start == -1 or idx_auth_start == -1:
    print("Could not find SaaS or Auth markers!")
    sys.exit(1)

saas_block = text[idx_saas_start:idx_auth_start].strip()

# Verify that all 6 tools are in saas_block
expected_tools = ['Novel Studio', 'Social Auto-Poster', 'LINE Sticker Creator', 'Clip AI & Reels', 'Smart Chat AI', 'Mockup Studio']
for tool in expected_tools:
    if tool not in saas_block:
        print(f"Missing {tool} in saas_block!")
        sys.exit(1)

print("saas_block verified with all 6 tools!")

idx_zone3_start = text.find('<!-- Zone 3: Right - Page Selector, Quick Controls, SaaS Selector, Profile -->')
idx_header_end = text.find('</header>')
if idx_zone3_start == -1 or idx_header_end == -1:
    print("Could not find Zone 3 or </header> markers!")
    sys.exit(1)

new_header_zone3 = (
    "<!-- Zone 3: Right - ThaiD SaaS Selector Dropdown -->\n"
    "            <div class=\"flex items-center gap-2 shrink-0\">\n"
    "                " + saas_block + "\n"
    "            </div>\n"
    "        </div>\n"
    "    "
)

text_with_new_header = text[:idx_zone3_start] + new_header_zone3 + text[idx_header_end:]

# Now insert the new bar before <!-- NAVIGATION TABS (SEGMENTED CONTROL STANDARD) -->
new_bar_html = """        <!-- APP CONTROLS & USER PROFILE BAR (NEW BAR) -->
        <div class="bg-white/90 dark:bg-stone-900/90 backdrop-blur-md border border-stone-200/80 dark:border-stone-800 rounded-2xl p-2 sm:p-2.5 shadow-xs flex items-center justify-between flex-wrap gap-2.5 relative z-20">
            <!-- Left: Page Selector & Quick Action Controls -->
            <div class="flex items-center flex-wrap gap-2">
                <!-- Page Selector Dropdown -->
                <div class="flex items-center bg-stone-100 hover:bg-stone-200/70 dark:bg-stone-800 dark:hover:bg-stone-700/70 border border-stone-200 dark:border-stone-700 rounded-full px-3 py-1.5 shrink-0 transition shadow-2xs">
                    <i class="fa-brands fa-facebook text-blue-500 mr-2 text-xs shrink-0"></i>
                    <select id="active-page-select" onchange="onPageChange()" class="bg-transparent text-xs font-semibold text-stone-700 dark:text-stone-200 focus:outline-none cursor-pointer pr-1">
                        <option value="">ทุกเพจ (All Pages)</option>
                    </select>
                </div>

                <!-- Quick Action: Fetch News -->
                <button onclick="triggerFetch()" id="btn-fetch" class="bg-stone-900 hover:bg-stone-800 dark:bg-stone-100 dark:hover:bg-white text-white dark:text-stone-900 text-xs px-3.5 py-1.5 rounded-full font-medium transition flex items-center gap-1.5 shadow-xs shrink-0 cursor-pointer" title="ดึงข่าวทันที">
                    <i class="fa-solid fa-bolt text-amber-400 text-xs"></i>
                    <span>ดึงข่าว</span>
                </button>

                <!-- Quick Action: Auto-Bot -->
                <button onclick="toggleAutoBot()" id="btn-auto" class="bg-blue-600 hover:bg-blue-700 text-white text-xs px-3.5 py-1.5 rounded-full font-medium transition flex items-center gap-1.5 shadow-xs shrink-0 cursor-pointer" title="เปิด/ปิด Auto-Bot">
                    <i class="fa-solid fa-clock text-xs"></i>
                    <span id="auto-btn-text">เริ่ม Auto-Bot</span>
                </button>

                <!-- Settings Gear -->
                <button onclick="openSettingsModal()" class="w-8 h-8 rounded-full bg-stone-100 hover:bg-stone-200 dark:bg-stone-800 dark:hover:bg-stone-700 text-stone-600 dark:text-stone-300 flex items-center justify-center transition border border-stone-200/80 dark:border-stone-700 text-xs shrink-0 cursor-pointer" title="ตั้งค่าระบบ">
                    <i class="fa-solid fa-gear"></i>
                </button>

                <!-- Admin Portal Button (Visible only to Admin) -->
                <a href="/admin" id="btn-admin-portal" class="bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs px-3.5 py-1.5 rounded-full transition flex items-center gap-1.5 shadow-xs shrink-0 hidden" title="เข้าสู่ระบบหลังบ้าน Superadmin">
                    <i class="fa-solid fa-shield-halved"></i>
                    <span>Admin</span>
                </a>
            </div>

            <!-- Right: User Account Profile / Login Indicator -->
            <div id="auth-container" class="shrink-0">
                <!-- Loading or Injected by JS -->
            </div>
        </div>

"""

tabs_anchor = "        <!-- NAVIGATION TABS (SEGMENTED CONTROL STANDARD) -->"
if tabs_anchor not in text_with_new_header:
    print("Could not find tabs anchor in modified text!")
    sys.exit(1)

final_text = text_with_new_header.replace(tabs_anchor, new_bar_html + tabs_anchor)

with open(path, "w", encoding="utf-8") as f:
    f.write(final_text)

print("reorganize_navbar_clean completed successfully!")
