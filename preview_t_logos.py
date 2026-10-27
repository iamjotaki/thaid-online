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
    font-family: -apple-system, BlinkMacSystemFont, "Google Sans", "Segoe UI", Roboto, sans-serif;
    padding: 40px;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  .row {
    display: flex;
    align-items: center;
    gap: 30px;
  }
  .box {
    background: white;
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 999px;
    padding: 10px 24px;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  }
  .label {
    font-size: 13px;
    font-weight: 600;
    color: #64748b;
    margin-bottom: 6px;
  }
  .brand-text {
    font-size: 22px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
  }
</style>
</head>
<body>

<div>
  <div class="label">Option 1: Bold Rounded Modern Monoline "T" (Like Fastwork's pill tube style)</div>
  <div class="box">
    <!-- Continuous pill tube forming a T -->
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 8h22M16 8v18" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<div>
  <div class="label">Option 2: Geometric Architectural "T" with Fastwork Rounded Loop/Knot Vibe</div>
  <div class="box">
    <!-- Loop folded T: ribbon/knot that loops into a T shape -->
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 10h9v16a3 3 0 0 1-3 3h0a3 3 0 0 1-3-3V10m6 0h11" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<div>
  <div class="label">Option 3: Solid Tech Geometric "T" (Hexagon / Precision Cut Icon)</div>
  <div class="box">
    <!-- Solid geometric silhouette T with soft curved vertexes -->
    <svg width="26" height="26" viewBox="0 0 32 32" fill="#2b313b">
      <path d="M5 8a3 3 0 0 1 3-3h16a3 3 0 0 1 3 3v2a3 3 0 0 1-3 3h-5v14a3 3 0 0 1-3 3h0a3 3 0 0 1-3-3V13H8a3 3 0 0 1-3-3V8z" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<div>
  <div class="label">Option 4: Fastwork-style Interlocking Dual-Stroke / Ribbon "T"</div>
  <div class="box">
    <!-- Fastwork-style continuous loop stroke forming a bold T -->
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M7 9h18M16 9v13a4 4 0 0 0 4 4" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<div>
  <div class="label">Option 5: Iconic Brand Mark — Two Layered Pills (Horizontal Floating Bar + Vertical Stem)</div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="#2b313b">
      <!-- Horizontal crossbar pill -->
      <rect x="4" y="5" width="24" height="6.5" rx="3.25" fill="#2b313b" />
      <!-- Vertical pillar with soft corner matching Fastwork -->
      <rect x="12.75" y="10.5" width="6.5" height="16.5" rx="3.25" fill="#2b313b" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<div>
  <div class="label">Option 6: Fastwork Style Möbius Loop "T" (Isometric Knot T)</div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M8 8h16M16 8v16M10 24h12" />
    </svg>
    <span class="brand-text">ThaiD</span>
  </div>
</div>

<div>
  <div class="label">Option 7: Modern Connected Monogram "T" (Fluid Fastwork Curve)</div>
  <div class="box">
    <svg width="26" height="26" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 8c4 0 9-1 11-1s7 1 11 1M16 7v19" />
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
        page = await browser.new_page(viewport={"width": 800, "height": 950})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_logo_options.png", full_page=True)
        await browser.close()
        print("Generated t_logo_options.png")

if __name__ == "__main__":
    asyncio.run(main())
