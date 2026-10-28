# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ThaiD-Mockup\static\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Make headings crisp black
content = content.replace(
    '<h2 class="font-bold text-sm">เลือกหรืออัปโหลดสินค้า (Product Cutout)</h2>',
    '<h2 class="font-bold text-sm text-[#171717]">เลือกหรืออัปโหลดสินค้า (Product Cutout)</h2>'
)
content = content.replace(
    '<h2 class="font-bold text-sm">เลือกฉากหลังพรีเมียม (Luxury Scene)</h2>',
    '<h2 class="font-bold text-sm text-[#171717]">เลือกฉากหลังพรีเมียม (Luxury Scene)</h2>'
)
content = content.replace(
    '<h2 class="font-bold text-sm">ปรับตำแหน่ง แสงเงา และขนาด (Fine-Tuning)</h2>',
    '<h2 class="font-bold text-sm text-[#171717]">ปรับตำแหน่ง แสงเงา และขนาด (Fine-Tuning)</h2>'
)

# Custom prompt input
content = content.replace(
    '<textarea id="customPromptInput" rows="3" class="w-full text-xs p-3 rounded-xl border border-stone-200 dark:border-stone-800 bg-stone-50 dark:bg-black/30 focus:border-brand-500 focus:outline-none resize-none"',
    '<textarea id="customPromptInput" rows="3" class="w-full text-xs p-3 rounded-xl border border-stone-300 bg-stone-50 text-[#171717] font-medium focus:border-brand-500 focus:outline-none resize-none"'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("ThaiD-Mockup static/index.html patched with high-contrast text!")
