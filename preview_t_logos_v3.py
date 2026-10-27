import asyncio
from playwright.async_api import async_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    background: #ffffff;
    font-family: "Google Sans", -apple-system, sans-serif;
    padding: 60px 40px;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }
  .row {
    display: flex;
    align-items: center;
    gap: 24px;
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
  .brand-text {
    font-size: 24px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
  }
  .title {
    font-size: 15px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 2px;
  }
  .desc {
    font-size: 13px;
    color: #64748b;
  }
</style>
</head>
<body>

<!-- Variation 1: The Fastwork Interlocking Loop T (Exact same stroke & loop topology as Fastwork clover) -->
<div class="row">
  <div style="width: 320px;">
    <div class="title">1. Fastwork Tri-Loop "T" (Knot Topology)</div>
    <div class="desc">ใช้โครงสร้าง 3 ห่วงและรูตรงกลางเหมือน Fastwork ทุกมิติ แต่ดัดเป็นปีกซ้าย-ขวาและก้านล่าง (T)</div>
  </div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 40 40" fill="none" stroke="#2b313b" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">
      <!-- Left loop -->
      <path d="M16 16 C12 16 7 13 7 17 C7 21 12 19 16 19" />
      <!-- Right loop -->
      <path d="M24 16 C28 16 33 13 33 17 C33 21 28 19 24 19" />
      <!-- Bottom stem loop -->
      <path d="M17.5 24 C17.5 29 16 34 20 34 C24 34 22.5 29 22.5 24" />
      <!-- Center ring & bridge -->
      <circle cx="20" cy="18" r="4" stroke-width="3" />
      <path d="M16 16 L24 16 M16 19 L17.5 24 M24 19 L22.5 24" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<!-- Variation 2: Pure Ribbon Loop "T" (Continuous Smooth Pill Tube) -->
<div class="row">
  <div style="width: 320px;">
    <div class="title">2. Pure Ribbon Loop "T" (Fluid & Sleek)</div>
    <div class="desc">เส้นท่อขอบมนลื่นไหล ปลายปีกมนก้านล่างมน โมเดิร์น ลักชัวรี และชัดเจนที่สุด</div>
  </div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 10 C6 7.5 8 6 11 6 L21 6 C24 6 26 7.5 26 10 C26 12.5 24 14 21 14 L18.5 14 L18.5 24 C18.5 26.5 17.5 28 16 28 C14.5 28 13.5 26.5 13.5 24 L13.5 14 L11 14 C8 14 6 12.5 6 10 Z" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<!-- Variation 3: Precision Architectural "T" (Dual Rounded Capsule Bars) -->
<div class="row">
  <div style="width: 320px;">
    <div class="title">3. Minimal Architectural "T" (Dual Capsule)</div>
    <div class="desc">สไตล์มินิมอลแท่งแคปซูล สะอาดตา คมชัด เข้ากับฟอนต์ Google Sans ได้ 100%</div>
  </div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none">
      <path d="M5 8.5h22" stroke="#2b313b" stroke-width="4.8" stroke-linecap="round"/>
      <path d="M16 8.5v16.5" stroke="#2b313b" stroke-width="4.8" stroke-linecap="round"/>
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<!-- Variation 4: Intersecting Möbius Ribbon "T" -->
<div class="row">
  <div style="width: 320px;">
    <div class="title">4. Intersecting Möbius "T" (Curved Tail)</div>
    <div class="desc">ก้านล่างตวัดปลายมนแบบไดนามิก ดูมีชีวิตชีวาและเทคโนโลยี</div>
  </div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 8h20M16 8v12a5 5 0 0 0 5 5" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<!-- Variation 5: Fastwork Clover Re-engineered as T (3-Lobe Hollow Topology) -->
<div class="row">
  <div style="width: 320px;">
    <div class="title">5. Fastwork 3-Lobe True "T" Knot</div>
    <div class="desc">ถอดลายเส้นต้นฉบับ 3 กลีบของ Fastwork มาจัดระเบียบเป็นทรง T ลายเส้นเดียวกับรูปที่คุณส่งมาเป๊ะๆ</div>
  </div>
  <div class="box">
    <!-- SVG that draws the 3 looped lobes of Fastwork in T configuration -->
    <svg width="26" height="26" viewBox="0 0 44 44" fill="none" stroke="#2b313b" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">
      <!-- Left lobe -->
      <path d="M18 16 C14 11 6 12 6 18 C6 24 14 25 18 20" />
      <!-- Right lobe -->
      <path d="M26 16 C30 11 38 12 38 18 C38 24 30 25 26 20" />
      <!-- Bottom lobe -->
      <path d="M19 23 C15 27 16 37 22 37 C28 37 29 27 25 23" />
      <!-- Central loop connecting fillets -->
      <path d="M18 16 C20 18 24 18 26 16 M26 20 C26 22 25 23 25 23 M19 23 C19 22 18 20 18 20" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 800, "height": 850})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_logo_v3.png", full_page=True)
        await browser.close()
        print("Generated t_logo_v3.png")

if __name__ == "__main__":
    asyncio.run(main())
