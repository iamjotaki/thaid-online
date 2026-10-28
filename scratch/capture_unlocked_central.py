# -*- coding: utf-8 -*-
import os
import time
from playwright.sync_api import sync_playwright

artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"
os.makedirs(artifact_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()

    print("Navigating to https://thaid.online/admin...", flush=True)
    page.goto("https://thaid.online/admin", wait_until="networkidle", timeout=25000)
    page.wait_for_timeout(1000)

    # Fill PIN
    pin_input = page.locator("input[type='password']")
    if pin_input.count() > 0:
        pin_input.fill("888888")
        page.keyboard.press("Enter")
        page.wait_for_timeout(2000)

    # Screenshot unlocked main dashboard with container grid showing both buttons
    shot1 = os.path.join(artifact_dir, "audit_central_admin_unlocked.png")
    page.screenshot(path=shot1, full_page=False)
    print(f"Captured: {shot1}", flush=True)

    # Open SaaS switcher dropdown in navbar
    saas_btn = page.locator("button:has-text('เครือข่ายแอป')")
    if saas_btn.count() > 0:
        saas_btn.click()
        page.wait_for_timeout(1000)
        shot2 = os.path.join(artifact_dir, "audit_central_admin_dropdown_unlocked.png")
        page.screenshot(path=shot2, full_page=False)
        print(f"Captured: {shot2}", flush=True)

    browser.close()

print("All unlocked screenshots captured successfully!", flush=True)
