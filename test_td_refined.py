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
    padding: 60px;
    display: flex;
    flex-direction: column;
    gap: 30px;
    align-items: center;
  }
  .preview {
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 999px;
    padding: 10px 24px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
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

<div class="preview">
  <svg width="24" height="24" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <path d="M5.5 7.5h13 M12 7.5v17 M12 7.5c6 0 13 3 13 8.5s-7 8.5-13 8.5" />
  </svg>
  <span class="brand">ThaiD</span>
</div>

</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 400, "height": 200})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/td_monogram_refined.png")
        await browser.close()
        print("Generated td_monogram_refined.png")

if __name__ == "__main__":
    asyncio.run(main())
