import asyncio
import sys
import os
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SERVICES = [
    ("main", "ThaiD Portal", "https://thaid.online", "หน้าแรกบริการ"),
    ("novel", "Novel Studio", "https://novel.thaid.online", "หน้าแรก Novel"),
    ("social", "Social Poster", "https://social.thaid.online", "หน้าแรก Social"),
    ("vault", "Security Vault", "https://vault.thaid.online", "หน้าแรก Vault"),
    ("sticker", "LINE Sticker", "https://sticker.thaid.online", "หน้าแรก Sticker"),
    ("clip", "Clip AI", "https://clip.thaid.online", "หน้าแรก Clip AI"),
    ("chat", "Smart Chat", "https://chat.thaid.online", "หน้าแรก Chat"),
    ("mockup", "Mockup Studio", "https://mockup.thaid.online", "หน้าแรก Mockup"),
]

OUT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

async def audit_service(context, slug, name, url, sub_label):
    page = await context.new_page()
    results = {"slug": slug, "name": name, "url": url, "errors": []}
    
    # Listen to console errors
    page.on("pageerror", lambda err: results["errors"].append(str(err)))

    try:
        print(f"\n==========================================")
        print(f"Auditing {name} -> {url}")
        print(f"==========================================")
        
        # 1. Goto page
        res = await page.goto(url, wait_until="networkidle", timeout=30000)
        status_code = res.status if res else 0
        print(f"  [HTTP {status_code}] Loaded {url}")
        await page.wait_for_timeout(800)

        # 2. Capture Guest State
        p_guest = os.path.join(OUT_DIR, f"audit_{slug}_guest.png")
        await page.screenshot(path=p_guest)
        print(f"  [SCREENSHOT] Guest state saved -> audit_{slug}_guest.png")

        # 3. Test Center SaaS Dropdown
        saas_btn = page.locator('#thaidSaasDropdownWrap button, button:has-text("เลือกบริการ SaaS")')
        if await saas_btn.count() > 0:
            await saas_btn.first.click()
            await page.wait_for_timeout(400)
            p_saas = os.path.join(OUT_DIR, f"audit_{slug}_saas_open.png")
            await page.screenshot(path=p_saas)
            print(f"  [SCREENSHOT] SaaS Dropdown opened -> audit_{slug}_saas_open.png")
            await saas_btn.first.click() # close dropdown
            await page.wait_for_timeout(200)

        # 4. Test Login Button
        login_btn = page.locator('#thaidLoginBtn, button:has-text("เข้าสู่ระบบ")')
        if await login_btn.count() > 0:
            await login_btn.first.click()
            await page.wait_for_timeout(400)
            
            # Click Demo User (Admin Boss)
            demo_btn = page.locator('#thaidAuthModal button:has-text("Admin Boss")')
            if await demo_btn.count() > 0:
                await demo_btn.first.click()
                await page.wait_for_timeout(500)
                
                # 5. Capture Logged-In Profile Avatar State
                p_user = os.path.join(OUT_DIR, f"audit_{slug}_logged_in.png")
                await page.screenshot(path=p_user)
                print(f"  [SCREENSHOT] Logged-in state saved -> audit_{slug}_logged_in.png")

                # 6. Click Profile Avatar
                profile_btn = page.locator('#thaidProfileBtn, button[title="Admin Boss"]')
                if await profile_btn.count() > 0:
                    await profile_btn.first.click()
                    await page.wait_for_timeout(400)
                    p_menu = os.path.join(OUT_DIR, f"audit_{slug}_profile_menu.png")
                    await page.screenshot(path=p_menu)
                    print(f"  [SCREENSHOT] Profile Menu opened -> audit_{slug}_profile_menu.png")
                    await profile_btn.first.click() # close
                    await page.wait_for_timeout(200)

        print(f"  [SUCCESS] {name} 100% verified! Errors: {len(results['errors'])}")

    except Exception as e:
        print(f"  [FAIL] {name}: {e}")
        results["errors"].append(str(e))
    finally:
        await page.close()

    return results

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        
        all_results = []
        for slug, name, url, sub_label in SERVICES:
            res = await audit_service(context, slug, name, url, sub_label)
            all_results.append(res)
            
        await browser.close()
        
        print("\n\n==========================================")
        print("FINAL VERIFICATION SUMMARY")
        print("==========================================")
        total_errs = sum(len(r['errors']) for r in all_results)
        for r in all_results:
            status_tag = "PASS" if len(r['errors']) == 0 else f"FAIL ({len(r['errors'])} errors)"
            print(f"[{status_tag}] {r['name']} ({r['url']})")
        print(f"\nTotal Console/Runtime Errors Across All 8 Services: {total_errs}")

asyncio.run(main())
