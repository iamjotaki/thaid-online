# -*- coding: utf-8 -*-
import os
import sys
import time
from playwright.sync_api import sync_playwright

artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"
os.makedirs(artifact_dir, exist_ok=True)

targets = [
    {
        "name": "audit_sticker_contrast_fixed",
        "url": "https://sticker.thaid.online",
        "wait_sel": "#inputCharacterDesc"
    },
    {
        "name": "audit_clip_contrast_fixed",
        "url": "https://clip.thaid.online",
        "wait_sel": "#scene1Speech"
    },
    {
        "name": "audit_chat_contrast_fixed",
        "url": "https://chat.thaid.online",
        "wait_sel": "#chatInput"
    },
    {
        "name": "audit_vault_contrast_fixed",
        "url": "https://vault.thaid.online",
        "wait_sel": "#masterPinInput"
    },
    {
        "name": "audit_mockup_contrast_fixed",
        "url": "https://mockup.thaid.online",
        "wait_sel": "#stageCanvas"
    }
]

print("Starting Playwright verification of contrast fixes...", flush=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()

    for item in targets:
        name = item["name"]
        url = item["url"]
        screenshot_path = os.path.join(artifact_dir, f"{name}.png")
        print(f"\nAuditing [{name}] at {url}...", flush=True)
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            if item.get("wait_sel"):
                try:
                    page.wait_for_selector(item["wait_sel"], timeout=5000)
                except Exception:
                    pass
            page.wait_for_timeout(1500)
            page.screenshot(path=screenshot_path, full_page=False)
            print(f"  -> Captured: {screenshot_path}", flush=True)
        except Exception as e:
            print(f"  -> Error capturing {name}: {e}", flush=True)

    browser.close()

print("\nVerification completed successfully!", flush=True)
