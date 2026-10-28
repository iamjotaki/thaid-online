import time, os, sys, asyncio
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import get_statuses
from playwright.async_api import async_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"
APPS = [1, 2, 3, 5, 6, 7, 8]

URLS = {
    "portal": ("https://thaid.online", "audit_nav_portal.png", "audit_nav_portal_dropdown.png"),
    "novel": ("https://novel.thaid.online", "audit_nav_novel.png", "audit_nav_novel_dropdown.png"),
    "social": ("https://social.thaid.online", "audit_nav_social.png", "audit_nav_social_dropdown.png"),
    "sticker": ("https://sticker.thaid.online", "audit_nav_sticker.png", None),
    "clip": ("https://clip.thaid.online", "audit_nav_clip.png", None),
    "chat": ("https://chat.thaid.online", "audit_nav_chat.png", None),
    "mockup": ("https://mockup.thaid.online", "audit_nav_mockup.png", None),
}

def wait_for_deployments():
    print("Waiting for deployments to finish...")
    for i in range(60):
        time.sleep(6)
        stats = get_statuses()
        all_finished = True
        status_line = []
        for aid in APPS:
            s = stats.get(aid, {}).get("status", "none")
            c = stats.get(aid, {}).get("commit", "none")
            status_line.append(f"{aid}:{s}[{c}]")
            if s != "finished":
                all_finished = False
        print(f"Check #{i+1}: " + " | ".join(status_line))
        sys.stdout.flush()
        if all_finished:
            print("All deployments finished!")
            return True
    return False

async def verify_all():
    print("Beginning Playwright verification across all 7 apps...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        
        for name, (url, nav_shot, drop_shot) in URLS.items():
            page = await context.new_page()
            try:
                print(f"Testing {name} ({url})...")
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(1)
                
                # Check for sub-home link
                # Should NOT exist
                sub_links = await page.locator("text='หน้าแรก [Sub]'").count()
                portal_links = await page.locator("text='หน้าแรกบริการ'").count()
                print(f"[{name}] sub_home: {sub_links}, portal_home: {portal_links}")
                
                # Navbar screenshot
                if nav_shot:
                    path = os.path.join(ARTIFACT_DIR, nav_shot)
                    await page.screenshot(path=path, clip={"x": 0, "y": 0, "width": 1440, "height": 180})
                    print(f"[{name}] Saved nav shot to {path}")
                    
                # Dropdown test
                if drop_shot:
                    btn = page.locator("button:has-text('เลือกบริการ SaaS')").first
                    if await btn.count() > 0:
                        await btn.click()
                        await asyncio.sleep(0.5)
                        path = os.path.join(ARTIFACT_DIR, drop_shot)
                        await page.screenshot(path=path, clip={"x": 800, "y": 0, "width": 640, "height": 520})
                        print(f"[{name}] Saved dropdown shot to {path}")
            except Exception as e:
                print(f"[{name}] Error: {e}")
            finally:
                await page.close()
                
        await browser.close()
    print("Verification complete!")

if __name__ == "__main__":
    wait_for_deployments()
    asyncio.run(verify_all())
