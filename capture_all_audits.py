import os
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

sites = [
    ("social", "https://social.thaid.online"),
    ("sticker", "https://sticker.thaid.online"),
    ("clip", "https://clip.thaid.online"),
    ("chat", "https://chat.thaid.online"),
    ("mockup", "https://mockup.thaid.online")
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    for name, url in sites:
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=15000)
            btn = page.locator("button:has-text('เลือกบริการ SaaS')")
            if btn.count() > 0:
                btn.first.click()
                page.wait_for_timeout(800)
            out_path = os.path.join(ARTIFACT_DIR, f"audit_{name}_6_tools.png")
            page.screenshot(path=out_path)
            print(f"Captured {out_path}")
        except Exception as e:
            print(f"Error on {name}: {e}")
        page.close()
    browser.close()
