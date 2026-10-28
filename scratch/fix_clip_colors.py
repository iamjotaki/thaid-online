# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ThaiD-Clip\static\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Timeline header
content = content.replace(
    '<h3 class="font-bold text-sm text-white">ลำดับฉากวิดีโอ (Timeline & Script Scenes)</h3>',
    '<h3 class="font-bold text-sm text-[#171717]">ลำดับฉากวิดีโอ (Timeline & Script Scenes)</h3>'
)

# 2. Scene titles
content = content.replace(
    '<span class="font-bold text-xs text-white">ฉากที่ 1: คำเปิดหยุดนิ้วโป้ง (The Hook)</span>',
    '<span class="font-bold text-xs text-[#171717]">ฉากที่ 1: คำเปิดหยุดนิ้วโป้ง (The Hook)</span>'
)
content = content.replace(
    '<span class="font-bold text-xs text-white">ฉากที่ 2: จุดเด่น & ความคุ้มค่า (The Value)</span>',
    '<span class="font-bold text-xs text-[#171717]">ฉากที่ 2: จุดเด่น & ความคุ้มค่า (The Value)</span>'
)
content = content.replace(
    '<span class="font-bold text-xs text-white">ฉากที่ 3: ปิดการขาย (Call-To-Action)</span>',
    '<span class="font-bold text-xs text-[#171717]">ฉากที่ 3: ปิดการขาย (Call-To-Action)</span>'
)

# 3. Model selector
content = content.replace(
    'class="bg-stone-100 dark:bg-stone-800 border border-stone-200 dark:border-stone-700 text-xs rounded-lg px-2 py-1 text-white font-medium focus:outline-none"',
    'class="bg-stone-50 border border-stone-300 text-xs rounded-lg px-2 py-1 text-[#171717] font-semibold focus:outline-none"'
)

# 4. Textareas & inputs in scenes
# Replace bg-white dark:bg-stone-800 border ... text-white -> bg-stone-50 border border-stone-300 rounded-lg p-2 text-xs text-[#171717] font-medium
content = content.replace(
    'class="w-full bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 rounded-lg p-2 text-xs text-white focus:outline-none focus:border-[#0569ff]"',
    'class="w-full bg-stone-50 border border-stone-300 rounded-lg p-2 text-xs text-[#171717] font-medium focus:outline-none focus:border-[#0569ff]"'
)
content = content.replace(
    'class="w-full bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 rounded-lg px-2 py-1 text-xs text-white focus:outline-none"',
    'class="w-full bg-stone-50 border border-stone-300 rounded-lg px-2 py-1 text-xs text-[#171717] font-medium focus:outline-none"'
)
content = content.replace(
    'class="w-full bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 rounded-lg px-2 py-1 text-xs text-white focus:outline-none font-mono"',
    'class="w-full bg-stone-50 border border-stone-300 rounded-lg px-2 py-1 text-xs text-[#171717] font-mono focus:outline-none"'
)

# 5. Scene labels: text-stone-500 dark:text-[#737373] -> text-stone-700 font-semibold
content = content.replace(
    'class="block text-[11px] text-stone-500 dark:text-[#737373] mb-0.5"',
    'class="block text-[11px] text-stone-700 font-semibold mb-0.5"'
)
content = content.replace(
    'class="block text-[10px] text-stone-500 dark:text-[#737373] mb-0.5"',
    'class="block text-[10px] text-stone-700 font-semibold mb-0.5"'
)

# 6. Loading text
content = content.replace(
    '<p class="text-xs font-bold text-white" id="loadingText">กำลังเรนเดอร์วิดีโอ 9:16...</p>',
    '<p class="text-xs font-bold text-[#171717]" id="loadingText">กำลังเรนเดอร์วิดีโอ 9:16...</p>'
)

# 7. Left controls / generator settings
content = content.replace(
    '<span class="text-xs font-bold uppercase tracking-wider text-stone-500 dark:text-[#737373]">ตัวสร้างคลิปวิดีโอ 9:16</span>',
    '<span class="text-xs font-bold uppercase tracking-wider text-[#171717]">ตัวสร้างคลิปวิดีโอ 9:16</span>'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("ThaiD-Clip static/index.html patched with high-contrast text!")
