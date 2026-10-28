# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\ThaiD-Vault\static\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Title
content = content.replace(
    '<h1 class="text-2xl font-bold tracking-tight text-white">ThaiD Personal Vault</h1>',
    '<h1 class="text-2xl font-bold tracking-tight text-[#171717]">ThaiD Personal Vault</h1>'
)

# 2. Master PIN input
content = content.replace(
    'class="w-full text-center text-3xl tracking-widest py-3.5 px-4 rounded-2xl bg-stone-100 dark:bg-white/5 border border-stone-300 dark:border-black/[0.08] text-white focus:outline-none focus:ring-2 focus:ring-[#0569ff] transition-all"',
    'class="w-full text-center text-3xl tracking-widest py-3.5 px-4 rounded-2xl bg-stone-50 border border-stone-300 text-[#171717] font-bold focus:outline-none focus:ring-2 focus:ring-[#0569ff] transition-all"'
)

# 3. Stats numbers
content = content.replace(
    '<div class="text-xl font-bold tracking-tight text-white" id="statTotalItems">0</div>',
    '<div class="text-xl font-bold tracking-tight text-[#171717]" id="statTotalItems">0</div>'
)
content = content.replace(
    '<div class="text-xl font-bold tracking-tight text-white" id="statTotalCategories">0</div>',
    '<div class="text-xl font-bold tracking-tight text-[#171717]" id="statTotalCategories">0</div>'
)
content = content.replace(
    '<div class="text-xl font-bold tracking-tight text-white" id="statFavorites">0</div>',
    '<div class="text-xl font-bold tracking-tight text-[#171717]" id="statFavorites">0</div>'
)

# 4. Search input
content = content.replace(
    'class="w-full pl-9 pr-4 py-2 rounded-xl bg-stone-100 dark:bg-white/5 border border-stone-200 dark:border-black/[0.08] text-sm text-white placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0569ff] transition-all"',
    'class="w-full pl-9 pr-4 py-2 rounded-xl bg-stone-50 border border-stone-300 text-sm text-[#171717] font-medium placeholder-stone-500 focus:outline-none focus:ring-2 focus:ring-[#0569ff] transition-all"'
)

# 5. Modal titles
content = content.replace(
    '<h2 class="text-base font-bold text-white" id="itemModalTitle">เพิ่มรายการใหม่</h2>',
    '<h2 class="text-base font-bold text-[#171717]" id="itemModalTitle">เพิ่มรายการใหม่</h2>'
)
content = content.replace(
    '<h2 class="text-base font-bold text-white">จัดการหมวดหมู่ (Categories)</h2>',
    '<h2 class="text-base font-bold text-[#171717]">จัดการหมวดหมู่ (Categories)</h2>'
)
content = content.replace(
    '<h2 class="text-base font-bold text-white">เปลี่ยนรหัส Master PIN</h2>',
    '<h2 class="text-base font-bold text-[#171717]">เปลี่ยนรหัส Master PIN</h2>'
)
content = content.replace(
    '<h2 class="text-base font-bold text-white">สำรองข้อมูล & กู้คืน (Backup)</h2>',
    '<h2 class="text-base font-bold text-[#171717]">สำรองข้อมูล & กู้คืน (Backup)</h2>'
)

# 6. Toast
content = content.replace(
    'class="fixed bottom-6 right-6 z-50 hidden bg-white text-white px-4 py-3 rounded-2xl border border-black/[0.08] shadow-2xl flex items-center gap-2.5 text-xs font-semibold"',
    'class="fixed bottom-6 right-6 z-50 hidden bg-[#171717] text-white px-4 py-3 rounded-2xl border border-black/[0.08] shadow-2xl flex items-center gap-2.5 text-xs font-semibold"'
)

# 7. JS item & category rendering
content = content.replace(
    '<h3 class="text-base font-bold text-white leading-snug group-hover:text-[#0569ff] transition-colors">',
    '<h3 class="text-base font-bold text-[#171717] leading-snug group-hover:text-[#0569ff] transition-colors">'
)
content = content.replace(
    '<div class="text-xs font-bold text-white flex items-center gap-2">',
    '<div class="text-xs font-bold text-[#171717] flex items-center gap-2">'
)

# 8. Modal form inputs text-white
content = content.replace(
    'class="w-full px-3 py-2 text-xs rounded-xl bg-stone-100 dark:bg-white/5 border border-stone-200 dark:border-black/[0.08] text-white focus:ring-2 focus:ring-[#0569ff] focus:outline-none"',
    'class="w-full px-3 py-2 text-xs rounded-xl bg-stone-50 border border-stone-300 text-[#171717] font-medium focus:ring-2 focus:ring-[#0569ff] focus:outline-none"'
)
content = content.replace(
    'class="w-full pl-3 pr-10 py-2 text-xs rounded-xl bg-stone-100 dark:bg-white/5 border border-stone-200 dark:border-black/[0.08] font-mono text-white focus:ring-2 focus:ring-[#0569ff] focus:outline-none"',
    'class="w-full pl-3 pr-10 py-2 text-xs rounded-xl bg-stone-50 border border-stone-300 font-mono text-[#171717] font-semibold focus:ring-2 focus:ring-[#0569ff] focus:outline-none"'
)
content = content.replace(
    'class="w-full px-3 py-2 text-xs rounded-xl bg-white dark:bg-white/5 border border-stone-200 dark:border-black/[0.08] text-white focus:ring-2 focus:ring-[#0569ff] focus:outline-none"',
    'class="w-full px-3 py-2 text-xs rounded-xl bg-stone-50 border border-stone-300 text-[#171717] font-medium focus:ring-2 focus:ring-[#0569ff] focus:outline-none"'
)
content = content.replace(
    'class="w-full text-center text-xl tracking-widest py-2.5 px-3 rounded-xl bg-stone-100 dark:bg-white/5 border border-stone-200 dark:border-black/[0.08] text-white focus:ring-2 focus:ring-[#0569ff] focus:outline-none"',
    'class="w-full text-center text-xl tracking-widest py-2.5 px-3 rounded-xl bg-stone-50 border border-stone-300 text-[#171717] font-bold focus:ring-2 focus:ring-[#0569ff] focus:outline-none"'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("ThaiD-Vault static/index.html patched with high-contrast text!")
