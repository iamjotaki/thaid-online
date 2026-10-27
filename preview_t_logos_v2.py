import asyncio
from playwright.async_api import async_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    background: #f1f5f9;
    font-family: -apple-system, BlinkMacSystemFont, "Google Sans", "Segoe UI", Roboto, sans-serif;
    padding: 40px;
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  .card {
    background: white;
    border-radius: 16px;
    padding: 20px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 16px rgba(0,0,0,0.04);
    max-width: 600px;
  }
  .preview {
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 999px;
    padding: 8px 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.02);
  }
  .title {
    font-size: 14px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 4px;
  }
  .desc {
    font-size: 12px;
    color: #64748b;
  }
  .brand {
    font-size: 22px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
  }
</style>
</head>
<body>

<!-- Design A: T-Knot (3-lobe Fastwork knot rearranged into a T: Left wing, Right wing, Down stem) -->
<div class="card">
  <div>
    <div class="title">Design A: Fastwork T-Knot (Tri-Lobe T Ribbon)</div>
    <div class="desc">เหมือนไอคอนเดิมของ Fastwork ทุกอย่าง แต่จัดวาง 3 แฉกเป็นปีกซ้าย-ขวา-ล่าง ให้เป็นตัว T</div>
  </div>
  <div class="preview">
    <svg width="26" height="26" viewBox="0 0 46 46" fill="none" stroke="#2b313b" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round">
      <!-- 3-lobe T shape: Left lobe, right lobe, bottom lobe with central hollow junction -->
      <path d="M14 13 H7 a5 5 0 0 0 0 10 h7 M32 13 h7 a5 5 0 0 1 0 10 h-7 M18 28 v9 a5 5 0 0 0 10 0 v-9 M14 13 h18 M14 23 h4 v5 M32 23 h-4 v5" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design B: Continuous Monoline Loop T (Smooth single-stroke closed path) -->
<div class="card">
  <div>
    <div class="title">Design B: Fluid Ribbon Loop T</div>
    <div class="desc">เส้น Ribbon โค้งมนต่อเนื่องเป็นทรงตัว T ลายเส้นหนานุ่มแบบ Fastwork</div>
  </div>
  <div class="preview">
    <svg width="26" height="26" viewBox="0 0 36 36" fill="none" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 10 C6 7 8 5 11 5 L25 5 C28 5 30 7 30 10 C30 13 28 15 25 15 L21 15 L21 28 C21 31 19 33 18 33 C17 33 15 31 15 28 L15 15 L11 15 C8 15 6 13 6 10 Z" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design C: Modern Rounded Tube T (Clean, minimal, high-tech) -->
<div class="card">
  <div>
    <div class="title">Design C: Modern Rounded Tube T</div>
    <div class="desc">ท่อขอบมนคู่ตัดกัน ทันสมัย สะอาดตา มองออกว่าเป็นตัว T ทันที</div>
  </div>
  <div class="preview">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none">
      <path d="M5 9h22" stroke="#2b313b" stroke-width="4.5" stroke-linecap="round"/>
      <path d="M16 9v17" stroke="#2b313b" stroke-width="4.5" stroke-linecap="round"/>
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design D: Isometric Interlocking T (Hexagonal Fastwork Knot) -->
<div class="card">
  <div>
    <div class="title">Design D: Isometric Interlocking T</div>
    <div class="desc">ลายเส้นหักมุมมุมมองไอโซเมตริก คล้ายโลโก้เทคระดับโลก</div>
  </div>
  <div class="preview">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 9h20M16 9v16M11 25h10" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design E: Bold Geometric Pill T (Solid Fastwork App Icon Style) -->
<div class="card">
  <div>
    <div class="title">Design E: Dual Solid Pill T</div>
    <div class="desc">แผ่นเม็ดยาสองแท่งประกบกัน ทึบ มั่นคง สไตล์โมเดิร์น UI</div>
  </div>
  <div class="preview">
    <svg width="26" height="26" viewBox="0 0 32 32">
      <rect x="4" y="5" width="24" height="6.5" rx="3.25" fill="#2b313b"/>
      <rect x="12.75" y="10.5" width="6.5" height="16" rx="3.25" fill="#2b313b"/>
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- Design F: Geometric Loop Knot (True Fastwork Knot T) -->
<div class="card">
  <div>
    <div class="title">Design F: True Fastwork Knot "T"</div>
    <div class="desc">โคลฟเวอร์ปมเชือก 3 ห่วง แต่ห่วงขวา-ซ้าย-ล่าง ชัดเจนว่าเป็นตัว T</div>
  </div>
  <div class="preview">
    <svg width="26" height="26" viewBox="0 0 40 40" fill="none" stroke="#2b313b" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">
      <!-- Top bar loop with left & right ends, center stem loop going down -->
      <path d="M10 12 C6 12 5 16 9 17 L16 17 L16 28 C16 32 24 32 24 28 L24 17 L31 17 C35 16 34 12 30 12 L10 12 Z" />
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
        page = await browser.new_page(viewport={"width": 750, "height": 920})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_logo_v2.png", full_page=True)
        await browser.close()
        print("Generated t_logo_v2.png")

if __name__ == "__main__":
    asyncio.run(main())
