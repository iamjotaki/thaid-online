import asyncio
from playwright.async_api import async_playwright

async def check_scroll_1100():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://thaid.online", wait_until="networkidle")
        
        # Total height of page
        h = await page.evaluate("document.body.scrollHeight")
        print(f"Total page scrollHeight: {h}")
        
        # Scroll to 1500
        await page.evaluate("window.scrollTo(0, 1600)")
        await page.wait_for_timeout(500)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/thaid_services_scroll_1600.png")
        print("Captured thaid_services_scroll_1600.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(check_scroll_1100())
