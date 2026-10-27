import asyncio
from playwright.async_api import async_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    background: #f8fafc;
    font-family: "Google Sans", -apple-system, sans-serif;
    padding: 40px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .box {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
    border-radius: 999px;
    padding: 10px 24px;
    display: inline-flex;
    align-items: center;
    gap: 12px;
  }
  .brand {
    font-size: 22px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
  }
  .title {
    font-size: 14px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 6px;
  }
</style>
</head>
<body>

<!-- Design A: Organic Interlocking Fastwork Knot T (Continuous Single Path) -->
<div>
  <div class="title">Design A: Organic Fastwork Knot "T" (เส้นเดียววนครบ 3 ห่วง มีรูกลาง)</div>
  <div class="box">
    <svg width="25" height="25" viewBox="0 0 36 36" fill="none" stroke="#2b313b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M18 17 C15 13 8 13 8 17 C8 21 15 21 18 17 C21 13 28 13 28 17 C28 21 21 21 18 17 Z" />
      <path d="M18 17 C15 20 15 29 18 29 C21 29 21 20 18 17 Z" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design B: Balanced 3-Petal Fastwork T (Symmetrical Wings & Stem) -->
<div>
  <div class="title">Design B: Balanced 3-Lobe T Knot (ปีกกว้างซ้ายขวา ก้านล่างมน ลายเส้นเดียวกับรูปที่แคปมา)</div>
  <div class="box">
    <svg width="25" height="25" viewBox="0 0 36 36" fill="none" stroke="#2b313b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <!-- Left petal -->
      <path d="M15 15 C11 11 5 12 5 16 C5 20 11 21 15 17" />
      <!-- Right petal -->
      <path d="M21 15 C25 11 31 12 31 16 C31 20 25 21 21 17" />
      <!-- Bottom stem petal -->
      <path d="M16 20 C13 24 14 31 18 31 C22 31 23 24 20 20" />
      <!-- Center connecting circle -->
      <circle cx="18" cy="17" r="2.8" stroke-width="2.5" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design C: Modern Rounded Tube T (Cleanest Minimal) -->
<div>
  <div class="title">Design C: Modern Clean Monoline T (หลอดมนมินิมอล โมเดิร์นระดับโลก)</div>
  <div class="box">
    <svg width="25" height="25" viewBox="0 0 32 32" fill="none">
      <path d="M4.5 8.5h23" stroke="#2b313b" stroke-width="4.4" stroke-linecap="round"/>
      <path d="M16 8.5v16.5" stroke="#2b313b" stroke-width="4.4" stroke-linecap="round"/>
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design D: Continuous Fluid Ribbon T (Solid Contour / Outline) -->
<div>
  <div class="title">Design D: Continuous Fluid Ribbon T (ริบบิ้นขอบมนชิ้นเดียว)</div>
  <div class="box">
    <svg width="25" height="25" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 9 C5 6.5 7 5 9.5 5 L22.5 5 C25 5 27 6.5 27 9 C27 11.5 25 13 22.5 13 L19 13 L19 24 C19 26.5 17.5 28 16 28 C14.5 28 13 26.5 13 24 L13 13 L9.5 13 C7 13 5 11.5 5 9 Z" />
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
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_logo_v6.png", full_page=True)
        await browser.close()
        print("Generated t_logo_v6.png")

if __name__ == "__main__":
    asyncio.run(main())
