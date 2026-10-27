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
    padding: 30px;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  .header-wrap {
    max-width: 900px;
    margin: 0 auto;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
    border-radius: 999px;
    padding: 10px 24px;
  }
  .lang-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 999px;
    border: 1px solid rgba(0,0,0,0.08);
    background: rgba(255,255,255,0.8);
    font-size: 12px;
    font-weight: 700;
    color: #2b313b;
  }
  .brand {
    font-size: 22px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 10px;
  }
</style>
</head>
<body>

<div>
  <div style="font-size: 13px; font-weight: bold; color: #64748b; margin-bottom: 8px; text-align: center;">
    Preview 1: Modern Loop Contour "T" (แนะนำที่สุด — คลีน มินิมอล ระดับพรีเมียม สื่อถึง ThaiD ได้สมบูรณ์แบบ)
  </div>
  <div class="header-wrap">
    <div class="brand">
      <svg width="25" height="25" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">
        <path d="M5 9.5 C5 7 7 5 9.5 5 L22.5 5 C25 5 27 7 27 9.5 C27 12 25 14 22.5 14 L19 14 L19 24.5 C19 27 17.5 28.5 16 28.5 C14.5 28.5 13 27 13 24.5 L13 14 L9.5 14 C7 14 5 12 5 9.5 Z" />
      </svg>
      <span>ThaiD</span>
    </div>
    <div class="lang-btn">
      <span>🌐</span>
      <span>TH</span>
      <span>˅</span>
    </div>
  </div>
</div>

<div>
  <div style="font-size: 13px; font-weight: bold; color: #64748b; margin-bottom: 8px; text-align: center;">
    Preview 2: Interlocking Fastwork Knot "T" (คงโครงสร้าง 3 ห่วงรูตรงกลางแบบเดิม แต่จัดเป็นทรงตัว T)
  </div>
  <div class="header-wrap">
    <div class="brand">
      <svg width="25" height="25" viewBox="0 0 36 36" fill="none" stroke="#2b313b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 11 H7 A4 4 0 0 0 7 19 H14" />
        <path d="M22 11 H29 A4 4 0 0 1 29 19 H22" />
        <path d="M15 22 V28 A3 3 0 0 0 21 28 V22" />
        <path d="M14 11 H22" />
        <circle cx="18" cy="18" r="2.8" stroke-width="2.6" />
      </svg>
      <span>ThaiD</span>
    </div>
    <div class="lang-btn">
      <span>🌐</span>
      <span>TH</span>
      <span>˅</span>
    </div>
  </div>
</div>

</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 960, "height": 300})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/header_t_previews.png")
        await browser.close()
        print("Generated header_t_previews.png")

if __name__ == "__main__":
    asyncio.run(main())
