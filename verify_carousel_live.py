import os
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 950})
        page = ctx.new_page()

        print("Visiting https://thaid.online ...")
        page.goto("https://thaid.online", wait_until="networkidle", timeout=30000)

        # Scroll down to the 3D Orbit Carousel
        viewport = page.locator(".orbit-carousel-viewport")
        viewport.scroll_into_view_if_needed()
        page.wait_for_timeout(1500)

        # 1. Capture Default View (Mockup Front)
        p1 = os.path.join(ARTIFACT_DIR, "audit_orbit_carousel_default.png")
        page.screenshot(path=p1)
        print(f"Captured {p1}")

        # 2. Click "Novel AI" Tab
        print("Clicking Novel AI tab...")
        novel_btn = page.locator("button:has-text('Novel AI')").first
        if novel_btn.count() > 0:
            novel_btn.click()
            page.wait_for_timeout(1200)
            p2 = os.path.join(ARTIFACT_DIR, "audit_orbit_carousel_novel.png")
            page.screenshot(path=p2)
            print(f"Captured {p2}")

        # 3. Click Next Arrow
        print("Clicking Next Arrow button...")
        next_btn = page.locator("button[aria-label='Next Studio']").first
        if next_btn.count() > 0:
            next_btn.click()
            page.wait_for_timeout(1000)
            p3 = os.path.join(ARTIFACT_DIR, "audit_orbit_carousel_next.png")
            page.screenshot(path=p3)
            print(f"Captured {p3}")

        browser.close()

if __name__ == "__main__":
    run()
