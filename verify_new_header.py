import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:3000", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # Screenshot the top header area
        header = page.locator('header')
        await header.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/new_header_crop.png")
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/new_header_full.png")
        print("Captured screenshots!")

        # Verify Vault is NOT in header
        vault_exists = await page.locator('header a[href*="vault"]').count()
        print(f"Vault in header count: {vault_exists} (should be 0)")

        # Verify ThaiD text in header
        logo_text = await page.locator('header a[href="https://thaid.online"]').inner_text()
        print(f"Header logo text: '{logo_text.strip()}' (should be 'ThaiD')")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
