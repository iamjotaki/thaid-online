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
    gap: 28px;
  }
  .card {
    background: white;
    border-radius: 18px;
    padding: 24px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    border: 1px solid rgba(0,0,0,0.05);
    max-width: 680px;
  }
  .preview {
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 999px;
    padding: 10px 24px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
  }
  .title {
    font-size: 15px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 4px;
  }
  .desc {
    font-size: 12px;
    color: #64748b;
  }
  .brand {
    font-size: 24px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
  }
</style>
</head>
<body>

<!-- Model 1: Fastwork-Proportioned T-Knot (3 rounded lobes forming the T crossbar & stem with central hole) -->
<div class="card">
  <div>
    <div class="title">Model 1: Fastwork T-Knot (Tri-Lobe Ribbon with Central Hole)</div>
    <div class="desc">เหมือนโคลฟเวอร์ Fastwork ทุกจุด ลายเส้นหนา ปลายมน มีรูกลาง แต่ปีกกว้างซ้าย-ขวา ก้านล่างยาว เป็นตัว T ชัดเจน</div>
  </div>
  <div class="preview">
    <svg width="28" height="28" viewBox="0 0 48 48" fill="none" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round">
      <!-- Left lobe -->
      <path d="M19 16 C12 11 5 13 5 19 C5 25 12 27 19 22" />
      <!-- Right lobe -->
      <path d="M29 16 C36 11 43 13 43 19 C43 25 36 27 29 22" />
      <!-- Bottom lobe (stem) -->
      <path d="M20 25 C16 32 17 41 24 41 C31 41 32 32 28 25" />
      <!-- Top bridge connecting left and right lobes -->
      <path d="M19 16 C22 17.5 26 17.5 29 16" />
      <!-- Center negative space hole -->
      <circle cx="24" cy="21" r="3.2" stroke-width="3.2" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Model 2: The Continuous Modern Loop "T" (Geometric Ribbon) -->
<div class="card">
  <div>
    <div class="title">Model 2: Modern Monoline Loop "T" (Clean Silhouette)</div>
    <div class="desc">เส้น Ribbon วงปิดต่อเนื่องทรงตัว T ขอบมน ลักชัวรี เข้ากับตัวหนังสือ ThaiD ทันที</div>
  </div>
  <div class="preview">
    <svg width="28" height="28" viewBox="0 0 36 36" fill="none" stroke="#2b313b" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 10 C6 7 8 5 11 5 L25 5 C28 5 30 7 30 10 C30 13 28 15 25 15 L21.5 15 L21.5 27 C21.5 30 19.5 32 18 32 C16.5 32 14.5 30 14.5 27 L14.5 15 L11 15 C8 15 6 13 6 10 Z" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Model 3: Fastwork Pill Tube "T" (Dual Rounded Cylinder) -->
<div class="card">
  <div>
    <div class="title">Model 3: Fastwork Minimal Tube "T"</div>
    <div class="desc">มินิมอลแท่งกระบอกมน สไตล์ Clean UI ทันสมัยระดับ Silicon Valley</div>
  </div>
  <div class="preview">
    <svg width="28" height="28" viewBox="0 0 32 32" fill="none">
      <path d="M4 8.5h24" stroke="#2b313b" stroke-width="5" stroke-linecap="round"/>
      <path d="M16 8.5v17.5" stroke="#2b313b" stroke-width="5" stroke-linecap="round"/>
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Model 4: Intersecting Möbius Ribbon "T" (Tech Flow) -->
<div class="card">
  <div>
    <div class="title">Model 4: Intersecting Flow "T" (Möbius Curve)</div>
    <div class="desc">คานบนตรง ปลายก้านล่างตวัดโค้งมนสไตล์โมเดิร์นเทค</div>
  </div>
  <div class="preview">
    <svg width="28" height="28" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 8.5h22M16 8.5v12.5a5.5 5.5 0 0 0 5.5 5.5" />
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
        page = await browser.new_page(viewport={"width": 780, "height": 720})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_logo_v4.png", full_page=True)
        await browser.close()
        print("Generated t_logo_v4.png")

if __name__ == "__main__":
    asyncio.run(main())
