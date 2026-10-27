import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://thaid.online", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # Check logo text and Vault existence
        logo_text = await page.locator('header a[href="https://thaid.online"]').inner_text()
        vault_count = await page.locator('header a[href*="vault"]').count()
        lang_text = await page.locator('header button').inner_text()

        print(f"Live Logo text: '{logo_text.strip()}'")
        print(f"Live Vault button count: {vault_count}")
        print(f"Live Language text: '{lang_text.strip()}'")

        header = page.locator('header')
        await header.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/live_header_crop.png")
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/live_header_full.png")
        print("Captured live screenshots")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
