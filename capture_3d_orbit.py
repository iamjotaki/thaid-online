import os
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 950})
        page = context.new_page()

        print("Navigating to https://thaid.online ...")
        page.goto("https://thaid.online", wait_until="networkidle", timeout=30000)

        # Scroll to 3D Orbit Carousel section
        print("Scrolling to 3D Orbit Carousel...")
        carousel = page.locator(".orbit-carousel-viewport")
        carousel.scroll_into_view_if_needed()
        page.wait_for_timeout(1500)

        # Capture 1: Initial view
        out_1 = os.path.join(ARTIFACT_DIR, "audit_3d_orbit_carousel_live.png")
        page.screenshot(path=out_1)
        print(f"Captured {out_1}")

        # Click on a category tab (e.g. ReadAWrite Pro Studio / Novel)
        novel_tab = page.locator("button:has-text('Novel')").first
        if novel_tab.count() > 0:
            print("Clicking Novel tab to test 3D spin...")
            novel_tab.click()
            page.wait_for_timeout(1200)
            out_2 = os.path.join(ARTIFACT_DIR, "audit_3d_orbit_carousel_spun_novel.png")
            page.screenshot(path=out_2)
            print(f"Captured {out_2}")

        browser.close()

if __name__ == "__main__":
    run()
