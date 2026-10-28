import re

path = r"C:\Auto Post FB\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract SaaS Dropdown wrap
saas_match = re.search(r'(<!-- SaaS Services Selector Dropdown \(Standard ThaiD Unified\) -->.*?</div>\s*</div>\s*</div>)', text, re.DOTALL)
if not saas_match:
    print("Could not find SaaS dropdown!")
    exit(1)

saas_dropdown_html = saas_match.group(1)

# The new clean Zone 3 of header:
new_zone3 = f"""            <!-- Zone 3: Right - ThaiD SaaS Selector Dropdown -->
            <div class="flex items-center gap-2 shrink-0">
                {saas_dropdown_html}
            </div>"""

# Replace the old Zone 3 in header
# Old Zone 3 starts at '<!-- Zone 3: Right - Page Selector' and ends right before '</div>\s*</header>'
header_zone3_pattern = re.compile(
    r'<!-- Zone 3: Right - Page Selector.*?<!-- Google Account Login / Profile Indicator -->\s*<div id="auth-container" class="shrink-0">\s*<!-- Loading or Injected by JS -->\s*</div>\s*</div>',
    re.DOTALL
)

if not header_zone3_pattern.search(text):
    print("Could not match header_zone3_pattern!")
    exit(1)

text = header_zone3_pattern.sub(new_zone3, text)

# The new bar HTML to place right before <!-- NAVIGATION TABS (SEGMENTED CONTROL STANDARD) -->
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
if tabs_anchor not in text:
    print("Could not find tabs anchor!")
    exit(1)

text = text.replace(tabs_anchor, new_bar_html + tabs_anchor)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("reorganize_navbar completed successfully!")
