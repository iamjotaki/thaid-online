import os
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()

        print("Navigating to https://thaid.online ...")
        page.goto("https://thaid.online", wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(1000)

        # 1. Capture Page 1 at scrollY = 0 (Must be 100% full screen Hero, no half-cut)
        p1 = os.path.join(ARTIFACT_DIR, "audit_hero_full_page1.png")
        page.screenshot(path=p1)
        print(f"Captured initial view: {p1}")

        # Check scrollY
        sy0 = page.evaluate("window.scrollY")
        print(f"Initial scrollY: {sy0}px")

        # 2. Simulate slight wheel down to trigger Auto-Snap to Page 2
        print("Simulating small wheel down to trigger auto-snap...")
        page.mouse.wheel(0, 45)
        page.wait_for_timeout(1600)

        sy1 = page.evaluate("window.scrollY")
        print(f"ScrollY after auto-snap: {sy1}px")

        # 3. Capture Page 2 (3D Orbit Carousel)
        p2 = os.path.join(ARTIFACT_DIR, "audit_page2_3d_orbit_carousel.png")
        page.screenshot(path=p2)
        print(f"Captured page 2 view: {p2}")

        browser.close()

if __name__ == "__main__":
    run()
