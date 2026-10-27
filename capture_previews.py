import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        urls = [
            ("thaid_white_studio.png", "https://thaid.online"),
            ("mockup_white_studio.png", "https://mockup.thaid.online"),
            ("clip_white_studio.png", "https://clip.thaid.online"),
        ]
        
        for filename, url in urls:
            try:
                await page.goto(url, wait_until="networkidle", timeout=15000)
                await page.wait_for_timeout(1000)
                await page.screenshot(path=f"C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/{filename}")
                print(f"Captured {filename}")
            except Exception as e:
                print(f"Error capturing {filename}: {e}")
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
