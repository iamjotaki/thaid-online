import asyncio
import sys
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})
        print("Opening https://vault.thaid.online ...")
        await page.goto('https://vault.thaid.online', wait_until='networkidle')
        await page.wait_for_timeout(1000)

        # Unlock with PIN 2026
        quick_btn = page.locator('text=คลิกเพื่อปลดล็อกด้วย PIN 2026 ทันที')
        if await quick_btn.count() > 0:
            print("Clicking quick unlock PIN 2026...")
            await quick_btn.first.click()
            await page.wait_for_timeout(2000)

        # Capture screenshot of unlocked dashboard
        p_unlocked = r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\vault_restored_unlocked_96_items.png'
        await page.screenshot(path=p_unlocked)
        print("Saved unlocked screenshot:", p_unlocked)

        # Check items on page
        items = page.locator('.vault-card, [data-item-id], table tbody tr, .grid > div')
        count = await items.count()
        print(f"Elements detected on dashboard: {count}")

        # Check total count badge or text if present
        text = await page.content()
        print("Has 'Google API Key #80'?", "Google API Key #80" in text)
        print("Has 'Spaceship'?", "Spaceship" in text)
        print("Has 'Neon Cloud'?", "Neon Cloud" in text)
        print("Has 'Coolify Control Panel'?", "Coolify Control Panel" in text)

        await browser.close()

asyncio.run(main())
