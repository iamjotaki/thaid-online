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
    font-family: "Google Sans", -apple-system, sans-serif;
    padding: 30px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  .box {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    border-radius: 999px;
    padding: 12px 28px;
    display: inline-flex;
    align-items: center;
    gap: 12px;
  }
  .card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    border: 1px solid rgba(0,0,0,0.06);
  }
  .brand {
    font-size: 24px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
  }
  .label {
    font-size: 13px;
    font-weight: 700;
    color: #334155;
    margin-bottom: 12px;
  }
</style>
</head>
<body>

<!-- V1: Continuous Loop T with Inner Negative Hole -->
<div class="card">
  <div class="label">V1: Modern Loop Contour "T" (ชัดเจน โมเดิร์นระดับสากล)</div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 9.5 C5 7 7 5 9.5 5 L22.5 5 C25 5 27 7 27 9.5 C27 12 25 14 22.5 14 L19 14 L19 24.5 C19 27 17.5 28.5 16 28.5 C14.5 28.5 13 27 13 24.5 L13 14 L9.5 14 C7 14 5 12 5 9.5 Z" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- V2: Fastwork Interlocking T (Knot with 3 Pill Lobes & Central Eye) -->
<div class="card">
  <div class="label">V2: Interlocking Fastwork Knot "T" (3 ห่วงพับริบบิ้น)</div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 36 36" fill="none" stroke="#2b313b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Crossbar left wing -->
      <path d="M14 11 H7 A4 4 0 0 0 7 19 H14" />
      <!-- Crossbar right wing -->
      <path d="M22 11 H29 A4 4 0 0 1 29 19 H22" />
      <!-- Stem bottom wing -->
      <path d="M15 22 V28 A3 3 0 0 0 21 28 V22" />
      <!-- Central bridge -->
      <path d="M14 11 H22" />
      <circle cx="18" cy="18" r="2.8" stroke-width="2.6" />
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- V3: Solid Minimal Dual-Capsule T (Solid Precision) -->
<div class="card">
  <div class="label">V3: Solid Capsule "T" (ทึบ มั่นคง เรียบหรู)</div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32">
      <rect x="4" y="5.5" width="24" height="6" rx="3" fill="#2b313b"/>
      <rect x="13" y="10.5" width="6" height="16" rx="3" fill="#2b313b"/>
    </svg>
    <span class="brand">ThaiD</span>
  </div>
</div>

<!-- V4: Monoline Architectural Tube T -->
<div class="card">
  <div class="label">V4: Architectural Monoline "T" (หลอดมนมินิมอล)</div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none">
      <path d="M4.5 8.5h23" stroke="#2b313b" stroke-width="4.6" stroke-linecap="round"/>
      <path d="M16 8.5v16.5" stroke="#2b313b" stroke-width="4.6" stroke-linecap="round"/>
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
        page = await browser.new_page(viewport={"width": 840, "height": 380})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_final_comparison.png", full_page=True)
        await browser.close()
        print("Generated t_final_comparison.png")

if __name__ == "__main__":
    asyncio.run(main())
