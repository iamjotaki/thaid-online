import asyncio
from playwright.async_api import async_playwright

async def capture_real_cards():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        print("Navigating to https://thaid.online ...")
        await page.goto("https://thaid.online", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)
        
        # Capture Hero with real cards
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/thaid_real_cards_hero.png")
        print("Captured thaid_real_cards_hero.png")
        
        # Scroll to services directory with real cards
        await page.evaluate("window.scrollTo(0, 1600)")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/thaid_real_cards_directory.png")
        print("Captured thaid_real_cards_directory.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_real_cards())
