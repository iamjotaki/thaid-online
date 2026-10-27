import asyncio
from playwright.async_api import async_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    background: #fafafa;
    font-family: "Google Sans", -apple-system, sans-serif;
    padding: 40px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .preview {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 999px;
    padding: 8px 22px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
  }
  .brand {
    font-size: 21px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
  }
</style>
</head>
<body>

<!-- Option 1A: Refined Fastwork Tri-Loop "T" (Geometric Balanced) -->
<div>
  <div style="font-size: 13px; font-weight: bold; margin-bottom: 6px;">Option 1: Fastwork-style Tri-Loop "T" (3 ห่วงเชื่อมกันแบบโคลฟเวอร์เดิม)</div>
  <div class="preview">
    <svg width="24" height="24" viewBox="0 0 36 36" fill="none" stroke="#2b313b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <path d="M14 11 H7 a4 4 0 0 0 0 8 h7" />
      <path d="M22 11 h7 a4 4 0 0 1 0 8 h-7" />
      <path d="M15 22 v7 a3 3 0 0 0 6 0 v-7" />
      <path d="M14 11 h8" />
      <circle cx="18" cy="18" r="3" stroke-width="2.6" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Option 2A: Continuous Fluid Ribbon Loop "T" -->
<div>
  <div style="font-size: 13px; font-weight: bold; margin-bottom: 6px;">Option 2: Continuous Fluid Ribbon "T" (เส้นริบบิ้นมนชิ้นเดียวต่อกัน)</div>
  <div class="preview">
    <svg width="24" height="24" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 9 C5 6.5 7 5 9.5 5 L22.5 5 C25 5 27 6.5 27 9 C27 11.5 25 13 22.5 13 L19 13 L19 24 C19 26.5 17.5 28 16 28 C14.5 28 13 26.5 13 24 L13 13 L9.5 13 C7 13 5 11.5 5 9 Z" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Option 3A: Minimalist Capsule Tube "T" -->
<div>
  <div style="font-size: 13px; font-weight: bold; margin-bottom: 6px;">Option 3: Minimalist Capsule Tube "T" (แท่งมนคลีนหรู)</div>
  <div class="preview">
    <svg width="24" height="24" viewBox="0 0 32 32" fill="none">
      <path d="M4 8h24" stroke="#2b313b" stroke-width="4.5" stroke-linecap="round"/>
      <path d="M16 8v17" stroke="#2b313b" stroke-width="4.5" stroke-linecap="round"/>
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Option 4A: Intersecting Möbius Loop "T" -->
<div>
  <div style="font-size: 13px; font-weight: bold; margin-bottom: 6px;">Option 4: Dynamic Tech Flow "T" (คานบนตรง ปลายก้านตวัดมน)</div>
  <div class="preview">
    <svg width="24" height="24" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 8h22M16 8v13a5 5 0 0 0 5 5" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 650, "height": 550})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_logo_v5.png", full_page=True)
        await browser.close()
        print("Generated t_logo_v5.png")

if __name__ == "__main__":
    asyncio.run(main())
