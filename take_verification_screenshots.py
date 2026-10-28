import os
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        # 1. Main portal dropdown
        print("Visiting https://thaid.online ...")
        page.goto("https://thaid.online", wait_until="networkidle")
        # Click dropdown if exists
        try:
            btn = page.locator("button:has-text('เลือกบริการ SaaS')")
            if btn.count() > 0:
                btn.first.click()
                page.wait_for_timeout(1000)
        except Exception as e:
            print("Dropdown click error:", e)
        page.screenshot(path=os.path.join(ARTIFACT_DIR, "audit_main_portal_6_tools.png"), full_page=False)
        print("Saved audit_main_portal_6_tools.png")

        # 2. Vault page (Private Vault, no demo bypass button)
        print("Visiting https://vault.thaid.online ...")
        page.goto("https://vault.thaid.online", wait_until="networkidle")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(ARTIFACT_DIR, "audit_vault_secured_no_demo.png"), full_page=False)
        print("Saved audit_vault_secured_no_demo.png")

        # 3. One of the subdomains (e.g. Novel Studio)
        print("Visiting https://novel.thaid.online ...")
        page.goto("https://novel.thaid.online", wait_until="networkidle")
        try:
            btn = page.locator("button:has-text('เลือกบริการ SaaS')")
            if btn.count() > 0:
                btn.first.click()
                page.wait_for_timeout(1000)
        except Exception as e:
            print("Dropdown click error:", e)
        page.screenshot(path=os.path.join(ARTIFACT_DIR, "audit_novel_6_tools_dropdown.png"), full_page=False)
        print("Saved audit_novel_6_tools_dropdown.png")

        browser.close()

if __name__ == "__main__":
    run()
