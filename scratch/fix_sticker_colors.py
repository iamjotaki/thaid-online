# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ThaiD-Sticker\static\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. inputCharacterDesc text-white -> text-[#171717] font-medium
content = content.replace(
    'id="inputCharacterDesc" type="text" value="ลูกแมวสามสีตัวอ้วนกลม ใส่ผ้าพันคอไหมพรมสีเหลือง ตาโตแป๋วแหวว น่ารักน่าเอ็นดู" placeholder="ระบุคาแรคเตอร์ เช่น ลูกหมาชิบะแก้มป่องใส่หมวกฟาง หรือ เด็กผู้หญิงผมบ็อบสวมเอี๊ยมยีนส์..." class="w-full bg-stone-100 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl px-4 py-2.5 text-sm text-white placeholder-stone-400',
    'id="inputCharacterDesc" type="text" value="ลูกแมวสามสีตัวอ้วนกลม ใส่ผ้าพันคอไหมพรมสีเหลือง ตาโตแป๋วแหวว น่ารักน่าเอ็นดู" placeholder="ระบุคาแรคเตอร์ เช่น ลูกหมาชิบะแก้มป่องใส่หมวกฟาง หรือ เด็กผู้หญิงผมบ็อบสวมเอี๊ยมยีนส์..." class="w-full bg-stone-50 border border-stone-300 rounded-xl px-4 py-2.5 text-sm text-[#171717] font-medium placeholder-stone-400'
)

# 2. Character Definition header text-stone-500 -> text-[#171717]
content = content.replace(
    '<h2 class="text-sm font-bold uppercase tracking-wider text-stone-500 dark:text-[#737373]">กำหนดคาแรคเตอร์ & ลายเส้น (Character Definition)</h2>',
    '<h2 class="text-sm font-bold uppercase tracking-wider text-[#171717]">กำหนดคาแรคเตอร์ & ลายเส้น (Character Definition)</h2>'
)

# 3. จำนวนรูป label & pills
content = content.replace(
    '<span class="text-stone-500 dark:text-[#737373]">จำนวนรูป:</span>',
    '<span class="text-stone-700 font-semibold">จำนวนรูป:</span>'
)
content = content.replace(
    'text-stone-600 dark:text-stone-700 hover:text-[#0569ff]" data-size="8"',
    'text-stone-800 font-bold hover:text-[#0569ff]" data-size="8"'
)
content = content.replace(
    'text-stone-600 dark:text-stone-700 hover:text-[#0569ff]" data-size="16"',
    'text-stone-800 font-bold hover:text-[#0569ff]" data-size="16"'
)
content = content.replace(
    'text-stone-600 dark:text-stone-700 hover:text-[#0569ff]" data-size="24"',
    'text-stone-800 font-bold hover:text-[#0569ff]" data-size="24"'
)

# 4. Art Style header & cards
content = content.replace(
    '<h2 class="text-xs font-bold uppercase tracking-wider text-stone-500 dark:text-[#737373] mb-3">เลือกลายเส้นสติกเกอร์ (Sticker Art Style):</h2>',
    '<h2 class="text-xs font-bold uppercase tracking-wider text-[#171717] mb-3">เลือกลายเส้นสติกเกอร์ (Sticker Art Style):</h2>'
)
content = content.replace(
    '<div class="text-[10px] text-stone-500 dark:text-[#737373] line-clamp-1">',
    '<div class="text-[10px] text-stone-600 font-medium line-clamp-1">'
)

# 5. System Ops header & Die-cut label
content = content.replace(
    '<span class="text-xs font-bold uppercase tracking-wider text-stone-500 dark:text-[#737373]">ระบบ AI เจนเนอเรเตอร์</span>',
    '<span class="text-xs font-bold uppercase tracking-wider text-[#171717]">ระบบ AI เจนเนอเรเตอร์</span>'
)
content = content.replace(
    '<span class="text-xs font-semibold text-stone-500">ขอบขาวไดคัต (LINE Die-Cut):</span>',
    '<span class="text-xs font-semibold text-stone-800">ขอบขาวไดคัต (LINE Die-Cut):</span>'
)

# 6. Caption library header & search input
content = content.replace(
    '<h3 class="font-bold text-sm text-white">คลังแคปชัน & ท่าทาง (530+ ข้อความ)</h3>',
    '<h3 class="font-bold text-sm text-[#171717]">คลังแคปชัน & ท่าทาง (530+ ข้อความ)</h3>'
)
content = content.replace(
    'id="captionSearch" type="text" placeholder="ค้นหาข้อความ เช่น สวัสดี, สู้ๆ, ขอบคุณ..." class="w-full bg-stone-100 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl pl-9 pr-3 py-2 text-xs text-white placeholder-stone-400',
    'id="captionSearch" type="text" placeholder="ค้นหาข้อความ เช่น สวัสดี, สู้ๆ, ขอบคุณ..." class="w-full bg-stone-50 border border-stone-300 rounded-xl pl-9 pr-3 py-2 text-xs text-[#171717] font-medium placeholder-stone-500'
)

# 7. Slots header & label
content = content.replace(
    '<span class="material-symbols-outlined text-[#0569ff] text-[18px]">collections</span>\n              <span>เซ็ตสติกเกอร์: <strong id="slotsCountLabel" class="text-white font-bold">40 รูป</strong></span>',
    '<span class="material-symbols-outlined text-[#0569ff] text-[18px]">collections</span>\n              <span class="text-stone-800 font-medium">เซ็ตสติกเกอร์: <strong id="slotsCountLabel" class="text-[#171717] font-bold">40 รูป</strong></span>'
)
content = content.replace(
    '<span>เซ็ตสติกเกอร์: <strong id="slotsCountLabel" class="text-white font-bold">40 รูป</strong></span>',
    '<span class="text-stone-800 font-medium">เซ็ตสติกเกอร์: <strong id="slotsCountLabel" class="text-[#171717] font-bold">40 รูป</strong></span>'
)
content = content.replace(
    '<span class="text-xs text-stone-500">โหมดพรีวิว:</span>',
    '<span class="text-xs text-stone-700 font-semibold">โหมดพรีวิว:</span>'
)

# 8. View mode pills text color
content = content.replace(
    'class="view-mode-btn active px-2.5 py-1 rounded text-[11px] font-semibold bg-white dark:bg-stone-700 text-white shadow-xs" data-mode="checker"',
    'class="view-mode-btn active px-2.5 py-1 rounded text-[11px] font-semibold bg-[#171717] text-white shadow-xs" data-mode="checker"'
)
content = content.replace(
    'class="view-mode-btn px-2.5 py-1 rounded text-[11px] font-semibold text-stone-500 dark:text-[#737373] hover:text-white" data-mode="line-dark"',
    'class="view-mode-btn px-2.5 py-1 rounded text-[11px] font-semibold text-stone-700 hover:text-black" data-mode="line-dark"'
)
content = content.replace(
    'class="view-mode-btn px-2.5 py-1 rounded text-[11px] font-semibold text-stone-500 dark:text-[#737373] hover:text-white" data-mode="line-light"',
    'class="view-mode-btn px-2.5 py-1 rounded text-[11px] font-semibold text-stone-700 hover:text-black" data-mode="line-light"'
)

# 9. MAIN.PNG and TAB.PNG titles
content = content.replace(
    '<span class="text-xs font-bold text-white">ภาพปกชุดสติกเกอร์</span>',
    '<span class="text-xs font-bold text-[#171717]">ภาพปกชุดสติกเกอร์</span>'
)
content = content.replace(
    '<span class="text-xs font-bold text-white">ไอคอนแถบห้องแชท</span>',
    '<span class="text-xs font-bold text-[#171717]">ไอคอนแถบห้องแชท</span>'
)
content = content.replace(
    '<p class="text-[11px] text-stone-500 dark:text-[#737373] mb-2">แสดงบนหน้าร้าน LINE STORE',
    '<p class="text-[11px] text-stone-600 font-medium mb-2">แสดงบนหน้าร้าน LINE STORE'
)
content = content.replace(
    '<p class="text-[11px] text-stone-500 dark:text-[#737373] mb-2">แสดงบนแถบเลือกสติกเกอร์',
    '<p class="text-[11px] text-stone-600 font-medium mb-2">แสดงบนแถบเลือกสติกเกอร์'
)

# 10. renderCaptionsList JS template
old_caption_template = """            <div class="flex items-center gap-1.5 mb-1">
              <span class="font-bold text-xs text-white">${c.caption}</span>
              <span class="text-[9px] px-1 py-0.2 rounded bg-stone-200 dark:bg-stone-800 text-stone-500 font-mono">${c.category.split('&')[0].trim()}</span>
            </div>
            <p class="text-[10px] text-stone-500 dark:text-[#737373] line-clamp-1">${c.pose}</p>"""

new_caption_template = """            <div class="flex items-center gap-1.5 mb-1">
              <span class="font-bold text-xs text-[#171717]">${c.caption}</span>
              <span class="text-[9px] px-1.5 py-0.5 rounded bg-stone-200 text-stone-700 font-semibold font-mono">${c.category.split('&')[0].trim()}</span>
            </div>
            <p class="text-[11px] text-stone-600 font-medium line-clamp-1">${c.pose}</p>"""

content = content.replace(old_caption_template, new_caption_template)

# Also fix the button '+ ใส่ในช่อง' inside renderCaptionsList
content = content.replace(
    'class="px-2 py-1 rounded-lg bg-[#171717]/10 hover:bg-[#171717] text-[#0569ff] hover:text-white dark:text-emerald-400 text-[10px] font-bold transition-colors flex items-center gap-1 opacity-80 group-hover:opacity-100"',
    'class="px-2.5 py-1 rounded-lg bg-blue-50 hover:bg-[#0569ff] text-[#0569ff] hover:text-white border border-blue-200 text-[10px] font-bold transition-colors flex items-center gap-1 shadow-2xs"'
)

# 11. renderStickerGrid JS slot badge
content = content.replace(
    'text-[#1d1d1f] dark:text-stone-700 font-mono text-[10px] font-bold',
    'text-stone-900 font-mono text-[10px] font-bold'
)
content = content.replace(
    'text-[#0569ff] dark:text-emerald-400 truncate max-w-[110px]',
    'text-[#0569ff] font-bold truncate max-w-[110px]'
)

# 12. Modals titles & inputs
content = content.replace(
    '<h3 class="font-bold text-sm text-white">ปรับแต่งไดคัต & ขอบขาว (Remat Studio)</h3>',
    '<h3 class="font-bold text-sm text-[#171717]">ปรับแต่งไดคัต & ขอบขาว (Remat Studio)</h3>'
)
content = content.replace(
    '<h3 class="font-bold text-sm text-white" id="editModalTitle">แก้ไขสติกเกอร์ช่องที่ 1</h3>',
    '<h3 class="font-bold text-sm text-[#171717]" id="editModalTitle">แก้ไขสติกเกอร์ช่องที่ 1</h3>'
)
content = content.replace(
    '<h3 class="font-bold text-sm text-white">โปสเตอร์รวมชุดสติกเกอร์ 4×10 (LINE Composite Sheet)</h3>',
    '<h3 class="font-bold text-sm text-[#171717]">โปสเตอร์รวมชุดสติกเกอร์ 4×10 (LINE Composite Sheet)</h3>'
)
content = content.replace(
    'id="editSlotCaption" type="text" class="w-full bg-stone-100 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl px-3 py-2 text-sm text-white',
    'id="editSlotCaption" type="text" class="w-full bg-stone-50 border border-stone-300 rounded-xl px-3 py-2 text-sm text-[#171717] font-semibold'
)
content = content.replace(
    'id="editSlotPose" rows="3" class="w-full bg-stone-100 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl p-3 text-xs text-white',
    'id="editSlotPose" rows="3" class="w-full bg-stone-50 border border-stone-300 rounded-xl p-3 text-xs text-[#171717] font-medium'
)

# Also fix setViewMode JS toggle classes
content = content.replace(
    "btn.classList.add('bg-white', 'dark:bg-stone-700', 'text-[#1d1d1f]', 'dark:text-white', 'shadow-xs', 'active');",
    "btn.classList.add('bg-[#171717]', 'text-white', 'shadow-xs', 'active');"
)
content = content.replace(
    "btn.classList.remove('bg-white', 'dark:bg-stone-700', 'text-[#1d1d1f]', 'dark:text-white', 'shadow-xs', 'active');",
    "btn.classList.remove('bg-[#171717]', 'text-white', 'shadow-xs', 'active');"
)
content = content.replace(
    "btn.classList.add('text-stone-500', 'dark:text-[#737373]');",
    "btn.classList.add('text-stone-700', 'hover:text-black');"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("ThaiD-Sticker static/index.html patched with high-contrast text!")
