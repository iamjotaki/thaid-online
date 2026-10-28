import asyncio
import sys
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SUBS = [
    ("clip", "https://clip.thaid.online"),
    ("chat", "https://chat.thaid.online"),
    ("sticker", "https://sticker.thaid.online"),
    ("vault", "https://vault.thaid.online"),
]

async def verify_sub(context, name, url):
    page = await context.new_page()
    try:
        print(f"Testing {name} ({url})...")
        await page.goto(url, wait_until='networkidle', timeout=30000)
        await page.wait_for_timeout(800)

        # 1. Guest screenshot
        p_guest = rf'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_{name}_nav_guest.png'
        await page.screenshot(path=p_guest)
        print(f"  [OK] Guest screenshot: {name}")

        # 2. SaaS dropdown
        saas_btn = page.locator('#thaidSaasDropdownWrap button')
        if await saas_btn.count() > 0:
            await saas_btn.first.click()
            await page.wait_for_timeout(400)
            p_saas = rf'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_{name}_nav_saas.png'
            await page.screenshot(path=p_saas)
            await saas_btn.first.click() # close
            await page.wait_for_timeout(200)
            print(f"  [OK] SaaS dropdown: {name}")

        # 3. Login
        login_btn = page.locator('#thaidLoginBtn')
        if await login_btn.count() > 0:
            await login_btn.first.click()
            await page.wait_for_timeout(400)
            demo_btn = page.locator('text=Admin Boss')
            if await demo_btn.count() > 0:
                await demo_btn.first.click()
                await page.wait_for_timeout(400)
                p_user = rf'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\verify_{name}_nav_logged.png'
                await page.screenshot(path=p_user)
                print(f"  [OK] Logged-in profile: {name}")

    except Exception as e:
        print(f"  [ERROR] {name}: {e}")
    finally:
        await page.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        for name, url in SUBS:
            await verify_sub(context, name, url)
        await browser.close()
        print("Batch verification finished!")

asyncio.run(main())
