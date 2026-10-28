import asyncio
from playwright.async_api import async_playwright
import os

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

URLS = {
    "portal": ("https://thaid.online", "audit_nav_portal.png", "audit_nav_portal_dropdown.png"),
    "social": ("https://social.thaid.online", "audit_nav_social.png", "audit_nav_social_dropdown.png"),
    "novel": ("https://novel.thaid.online", "audit_nav_novel.png", "audit_nav_novel_dropdown.png"),
    "sticker": ("https://sticker.thaid.online", "audit_nav_sticker.png", None),
    "clip": ("https://clip.thaid.online", "audit_nav_clip.png", None),
    "chat": ("https://chat.thaid.online", "audit_nav_chat.png", None),
    "mockup": ("https://mockup.thaid.online", "audit_nav_mockup.png", None),
}

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        
        results = {}
        for name, (url, nav_shot, drop_shot) in URLS.items():
            page = await context.new_page()
            try:
                print(f"Loading {url}...")
                await page.goto(url, wait_until="networkidle", timeout=25000)
                await asyncio.sleep(0.5)
                
                # Check for any "หน้าแรก" link in navbar
                home_links = await page.locator("nav a:has-text('หน้าแรก')").count()
                
                # Check dropdown button exists in nav
                saas_btn = page.locator("button:has-text('เลือกบริการ SaaS')").first
                has_saas_btn = await saas_btn.count() > 0
                
                print(f"[{name}] home_links_in_nav: {home_links}, has_saas_btn: {has_saas_btn}")
                results[name] = {"home_links": home_links, "has_saas_btn": has_saas_btn}
                
                # Screenshot navbar area
                shot_path = os.path.join(ARTIFACT_DIR, nav_shot)
                await page.screenshot(path=shot_path, clip={"x": 0, "y": 0, "width": 1440, "height": 180})
                print(f"[{name}] Saved navbar screenshot: {shot_path}")
                
                # Test opening dropdown if drop_shot is requested
                if drop_shot and has_saas_btn:
                    await saas_btn.click()
                    await asyncio.sleep(0.5)
                    drop_path = os.path.join(ARTIFACT_DIR, drop_shot)
                    await page.screenshot(path=drop_path, clip={"x": 800, "y": 0, "width": 640, "height": 500})
                    print(f"[{name}] Saved dropdown screenshot: {drop_path}")
            except Exception as e:
                print(f"[{name}] Error: {e}")
                results[name] = {"error": str(e)}
            finally:
                await page.close()
                
        await browser.close()
        print("\nAll Audit Results:")
        for k, v in results.items():
            print(f"  {k}: {v}")

if __name__ == "__main__":
    asyncio.run(run())
