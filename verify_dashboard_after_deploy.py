import asyncio
import time
import os
from playwright.async_api import async_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

async def run_audit():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 1050})
        page = await context.new_page()
        
        print("Navigating to https://social.thaid.online/?login=1 ...")
        await page.goto("https://social.thaid.online/?login=1", wait_until="networkidle")
        await asyncio.sleep(0.5)
        
        # Log in via mock login API
        await page.evaluate("""
            async () => {
                await fetch('/api/auth/google/mock_login', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({email: 'admin@lfcautonews.com', name: 'Admin Boss', role: 'admin'})
                });
            }
        """)
        
        print("Logged in, measuring /dashboard speed...")
        t0 = time.time()
        await page.goto("https://social.thaid.online/dashboard", wait_until="domcontentloaded")
        t_dom = time.time() - t0
        print(f"/dashboard DOMContentLoaded in {t_dom:.2f} seconds!")
        
        # Wait for cards to render
        try:
            await page.wait_for_selector('#news-container > div:not(.text-center)', timeout=8000)
            print("Cards rendered successfully!")
        except Exception as e:
            print("Wait for cards note:", e)

        # Wait for stats to populate
        for _ in range(10):
            stat = await page.evaluate("() => document.getElementById('stat-total')?.innerText")
            if stat and stat != '0':
                print(f"Stats populated: {stat} articles total!")
                break
            await asyncio.sleep(0.5)
            
        await asyncio.sleep(1)
        
        # 1. Full page overview screenshot
        shot1 = os.path.join(ARTIFACT_DIR, "audit_dashboard_thaid_standard.png")
        await page.screenshot(path=shot1, full_page=False)
        print(f"Saved: {shot1}")
        
        # 2. Header and top navbar screenshot
        shot_nav = os.path.join(ARTIFACT_DIR, "audit_dashboard_nav.png")
        await page.screenshot(path=shot_nav, clip={"x": 0, "y": 0, "width": 1440, "height": 380})
        print(f"Saved: {shot_nav}")
        
        # 3. Dropdown open screenshot
        saas_btn = page.locator("#thaidSaasBtn")
        if await saas_btn.count() > 0:
            await saas_btn.click()
            await asyncio.sleep(0.5)
            shot_drop = os.path.join(ARTIFACT_DIR, "audit_dashboard_dropdown.png")
            await page.screenshot(path=shot_drop, clip={"x": 800, "y": 0, "width": 640, "height": 550})
            print(f"Saved: {shot_drop}")
            await saas_btn.click()
            await asyncio.sleep(0.3)
            
        # 4. Scroll to first article card & buttons
        await page.evaluate("window.scrollTo(0, 500)")
        await asyncio.sleep(0.5)
        shot_cards = os.path.join(ARTIFACT_DIR, "audit_dashboard_cards.png")
        await page.screenshot(path=shot_cards, clip={"x": 0, "y": 200, "width": 1440, "height": 800})
        print(f"Saved: {shot_cards}")
        
        # 5. Scroll to pagination bar at the bottom of news
        pag = page.locator("#news-pagination")
        if await pag.count() > 0:
            await pag.scroll_into_view_if_needed()
            await asyncio.sleep(0.5)
            shot_pag = os.path.join(ARTIFACT_DIR, "audit_dashboard_pagination.png")
            await page.screenshot(path=shot_pag, clip={"x": 0, "y": 500, "width": 1440, "height": 500})
            print(f"Saved: {shot_pag}")
            
        await browser.close()
        print("Audit screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(run_audit())
