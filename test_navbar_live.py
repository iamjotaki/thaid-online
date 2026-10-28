import asyncio
import sys
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})
        print("Navigating to https://thaid.online ...")
        await page.goto('https://thaid.online', wait_until='networkidle')
        await page.wait_for_timeout(1000)
        
        # 1. Guest state
        await page.screenshot(path=r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_master_nav_guest.png')
        print("1. Saved guest navbar screenshot")

        # 2. Click SaaS dropdown
        saas_btn = page.locator('button:has-text("เลือกบริการ SaaS")')
        if await saas_btn.count() > 0:
            await saas_btn.first.click()
            await page.wait_for_timeout(600)
            await page.screenshot(path=r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_master_nav_saas_menu.png')
            print("2. Saved SaaS dropdown screenshot")
            await saas_btn.first.click()
            await page.wait_for_timeout(300)

        # 3. Click Login
        login_btn = page.locator('button:has-text("เข้าสู่ระบบ")')
        if await login_btn.count() > 0:
            await login_btn.first.click()
            await page.wait_for_timeout(600)
            await page.screenshot(path=r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_master_nav_auth_modal.png')
            print("3. Saved auth modal screenshot")

            # 4. Click Demo login
            demo_btn = page.locator('text=Admin Boss')
            if await demo_btn.count() > 0:
                await demo_btn.first.click()
                await page.wait_for_timeout(600)
                await page.screenshot(path=r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_master_nav_logged_in.png')
                print("4. Saved logged-in avatar screenshot")

                # 5. Click Profile avatar
                avatar_btn = page.locator('button[title="Admin Boss"]')
                if await avatar_btn.count() > 0:
                    await avatar_btn.first.click()
                    await page.wait_for_timeout(600)
                    await page.screenshot(path=r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_master_nav_profile_menu.png')
                    print("5. Saved profile menu screenshot")

        await browser.close()
        print("Verification complete!")

asyncio.run(main())
