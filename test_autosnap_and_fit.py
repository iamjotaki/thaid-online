import os
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()

        print("Visiting https://thaid.online ...")
        page.goto("https://thaid.online", wait_until="networkidle", timeout=30000)

        # 1. Test Auto-Snap: wheel down by 30px while at top
        print("Testing Auto-Snap: simulating small wheel down from hero...")
        page.mouse.wheel(0, 40)
        page.wait_for_timeout(1500) # Wait for smooth auto-scroll to complete

        scrollY = page.evaluate("window.scrollY")
        print(f"Current scrollY after auto-snap wheel: {scrollY}px")

        # Capture landed position
        out_snap = os.path.join(ARTIFACT_DIR, "audit_autosnap_landed.png")
        page.screenshot(path=out_snap)
        print(f"Captured {out_snap}")

        # 2. Check Card Bounding Box & Fit
        viewport = page.locator(".orbit-carousel-viewport")
        viewport.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)

        out_fit = os.path.join(ARTIFACT_DIR, "audit_card_fit_no_clipping.png")
        page.screenshot(path=out_fit)
        print(f"Captured {out_fit}")

        # Measure top card position
        front_card = page.locator(".orbit-carousel-card").first
        box = front_card.bounding_box()
        print(f"Front card bounding box: {box}")

        browser.close()

if __name__ == "__main__":
    run()
