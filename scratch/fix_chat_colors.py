# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ThaiD-Chat\static\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Simulator tab header
content = content.replace(
    '<h3 class="font-bold text-sm text-white">แอดมิน AI ตอบคำถามเสมือนจริง (AI Admin Sandbox)</h3>',
    '<h3 class="font-bold text-sm text-[#171717]">แอดมิน AI ตอบคำถามเสมือนจริง (AI Admin Sandbox)</h3>'
)

# 2. 3 Feature cards
content = content.replace(
    '<div class="text-xs font-bold text-white mt-1">ตอบกลับทันที 24/7</div>',
    '<div class="text-xs font-bold text-[#171717] mt-1">ตอบกลับทันที 24/7</div>'
)
content = content.replace(
    '<div class="text-xs font-bold text-white mt-1">คลังความรู้ส่วนตัว</div>',
    '<div class="text-xs font-bold text-[#171717] mt-1">คลังความรู้ส่วนตัว</div>'
)
content = content.replace(
    '<div class="text-xs font-bold text-white mt-1">ต้นทุน API 0 บาท</div>',
    '<div class="text-xs font-bold text-[#171717] mt-1">ต้นทุน API 0 บาท</div>'
)
content = content.replace(
    '<div class="text-[10px] text-[#737373]">ไม่ต้องเฝ้าจอ ระบบทำงานตลอดเวลา</div>',
    '<div class="text-[10px] text-stone-600 font-medium">ไม่ต้องเฝ้าจอ ระบบทำงานตลอดเวลา</div>'
)
content = content.replace(
    '<div class="text-[10px] text-[#737373]">ตอบตามโปรไฟล์และสินค้าจริง</div>',
    '<div class="text-[10px] text-stone-600 font-medium">ตอบตามโปรไฟล์และสินค้าจริง</div>'
)
content = content.replace(
    '<div class="text-[10px] text-[#737373]">ใช้ 80 คีย์เวียนฟรี ไม่จำกัด</div>',
    '<div class="text-[10px] text-stone-600 font-medium">ใช้ 80 คีย์เวียนฟรี ไม่จำกัด</div>'
)

# 3. Chat Header & initial message
content = content.replace(
    '<div class="font-bold text-xs text-white" id="chatHeaderName">น้องใจดี (แอดมิน AI)</div>',
    '<div class="font-bold text-xs text-[#171717]" id="chatHeaderName">น้องใจดี (แอดมิน AI)</div>'
)
content = content.replace(
    '<span class="material-symbols-outlined text-white text-[20px] cursor-pointer">arrow_back_ios</span>',
    '<span class="material-symbols-outlined text-stone-700 text-[20px] cursor-pointer">arrow_back_ios</span>'
)
content = content.replace(
    '<div class="bg-white dark:bg-[#2b333d] text-white p-3 rounded-2xl rounded-tl-none shadow-sm leading-relaxed">',
    '<div class="bg-white border border-stone-200 text-[#171717] p-3 rounded-2xl rounded-tl-none shadow-xs leading-relaxed font-medium">'
)

# 4. Chat input box
content = content.replace(
    'class="flex-1 bg-[#1a1f26] border border-black/[0.08] rounded-full px-3.5 py-2 text-xs text-white placeholder-stone-400 focus:outline-none focus:border-emerald-500"',
    'class="flex-1 bg-white border border-stone-300 rounded-full px-3.5 py-2 text-xs text-[#171717] font-medium placeholder-stone-500 focus:outline-none focus:border-emerald-500 shadow-2xs"'
)

# 5. LINE Integration inputs
content = content.replace(
    'class="w-full bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 rounded-lg px-3 py-2 text-xs font-mono text-white"',
    'class="w-full bg-stone-50 border border-stone-300 rounded-lg px-3 py-2 text-xs font-mono text-[#171717]"'
)
content = content.replace(
    'class="w-full bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 rounded-lg p-2.5 text-xs font-mono text-white"',
    'class="w-full bg-stone-50 border border-stone-300 rounded-lg p-2.5 text-xs font-mono text-[#171717]"'
)
content = content.replace(
    '<h3 class="font-bold text-sm text-white">วิธีเชื่อมต่อ LINE Official Account (Webhook Integration)</h3>',
    '<h3 class="font-bold text-sm text-[#171717]">วิธีเชื่อมต่อ LINE Official Account (Webhook Integration)</h3>'
)

# 6. Analytics & Logs stats & headers
content = content.replace(
    '<div class="text-xl font-bold text-white" id="statTotalMsgs">0</div>',
    '<div class="text-xl font-bold text-[#171717]" id="statTotalMsgs">0</div>'
)
content = content.replace(
    '<div class="text-xl font-bold text-white">~0.85s</div>',
    '<div class="text-xl font-bold text-emerald-600">~0.85s</div>'
)
content = content.replace(
    '<h3 class="font-bold text-sm text-white">ประวัติการสนทนาล่าสุด (Recent Chat Logs)</h3>',
    '<h3 class="font-bold text-sm text-[#171717]">ประวัติการสนทนาล่าสุด (Recent Chat Logs)</h3>'
)

# 7. Knowledge Base titles & JS rendering
content = content.replace(
    '<div class="font-bold text-white">${pr.name}</div>',
    '<div class="font-bold text-[#171717]">${pr.name}</div>'
)
content = content.replace(
    '<div class="font-bold text-white mb-1">Q: ${f.question}</div>',
    '<div class="font-bold text-[#171717] mb-1">Q: ${f.question}</div>'
)
content = content.replace(
    '<td class="py-2.5 px-3 font-semibold text-white max-w-[200px] truncate" title="${escapeHtml(l.message)}">${escapeHtml(l.message)}</td>',
    '<td class="py-2.5 px-3 font-semibold text-[#171717] max-w-[200px] truncate" title="${escapeHtml(l.message)}">${escapeHtml(l.message)}</td>'
)

# Also fix the JS chat bubble template
content = content.replace(
    '<div class="bg-white dark:bg-[#2b333d] text-white p-3 rounded-2xl rounded-tl-none shadow-sm leading-relaxed whitespace-pre-wrap">',
    '<div class="bg-white border border-stone-200 text-[#171717] p-3 rounded-2xl rounded-tl-none shadow-xs leading-relaxed whitespace-pre-wrap font-medium">'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("ThaiD-Chat static/index.html patched with high-contrast text!")
