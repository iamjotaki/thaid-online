# -*- coding: utf-8 -*-
import os
import sys
import time
from playwright.sync_api import sync_playwright

artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"
os.makedirs(artifact_dir, exist_ok=True)

targets = [
    # 1. Central Admin
    {
        "name": "audit_central_admin_updated",
        "url": "https://thaid.online/admin",
        "actions": lambda page: [
            page.fill("#pinInput", "1234"),
            page.click("button:has-text('เข้าสู่ระบบแดชบอร์ด')"),
            page.wait_for_timeout(1500)
        ]
    },
    # 2. Novel Studio
    {
        "name": "audit_novel_dashboard",
        "url": "https://novel.thaid.online/dashboard",
        "actions": None
    },
    {
        "name": "audit_novel_admin",
        "url": "https://novel.thaid.online/admin",
        "actions": lambda page: [
            page.fill("#pinInput", "1234"),
            page.click("button:has-text('เข้าสู่ระบบหลังบ้าน')"),
            page.wait_for_timeout(1000)
        ]
    },
    # 3. Social Auto-Poster
    {
        "name": "audit_social_dashboard",
        "url": "https://social.thaid.online/dashboard",
        "actions": None
    },
    {
        "name": "audit_social_admin",
        "url": "https://social.thaid.online/admin",
        "actions": None
    },
    # 4. Personal Vault
    {
        "name": "audit_vault_dashboard",
        "url": "https://vault.thaid.online/dashboard",
        "actions": None
    },
    {
        "name": "audit_vault_admin",
        "url": "https://vault.thaid.online/admin",
        "actions": lambda page: [
            page.fill("#pinInput", "1234"),
            page.click("button:has-text('เข้าสู่ระบบหลังบ้าน')"),
            page.wait_for_timeout(1000)
        ]
    },
    # 5. LINE Sticker Creator
    {
        "name": "audit_sticker_dashboard",
        "url": "https://sticker.thaid.online/dashboard",
        "actions": None
    },
    {
        "name": "audit_sticker_admin",
        "url": "https://sticker.thaid.online/admin",
        "actions": lambda page: [
            page.fill("#pinInput", "1234"),
            page.click("button:has-text('เข้าสู่ระบบหลังบ้าน')"),
            page.wait_for_timeout(1000)
        ]
    },
    # 6. Clip AI & Reels
    {
        "name": "audit_clip_dashboard",
        "url": "https://clip.thaid.online/dashboard",
        "actions": None
    },
    {
        "name": "audit_clip_admin",
        "url": "https://clip.thaid.online/admin",
        "actions": lambda page: [
            page.fill("#pinInput", "1234"),
            page.click("button:has-text('เข้าสู่ระบบหลังบ้าน')"),
            page.wait_for_timeout(1000)
        ]
    },
    # 7. Smart Chat AI
    {
        "name": "audit_chat_dashboard",
        "url": "https://chat.thaid.online/dashboard",
        "actions": None
    },
    {
        "name": "audit_chat_admin",
        "url": "https://chat.thaid.online/admin",
        "actions": lambda page: [
            page.fill("#pinInput", "1234"),
            page.click("button:has-text('เข้าสู่ระบบหลังบ้าน')"),
            page.wait_for_timeout(1000)
        ]
    },
    # 8. Mockup Studio
    {
        "name": "audit_mockup_dashboard",
        "url": "https://mockup.thaid.online/dashboard",
        "actions": None
    },
    {
        "name": "audit_mockup_admin",
        "url": "https://mockup.thaid.online/admin",
        "actions": lambda page: [
            page.fill("#pinInput", "1234"),
            page.click("button:has-text('เข้าสู่ระบบหลังบ้าน')"),
            page.wait_for_timeout(1000)
        ]
    }
]

print(f"Starting Playwright audit for {len(targets)} targets...", flush=True)

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
            page.goto(url, wait_until="networkidle", timeout=25000)
            page.wait_for_timeout(1500)
            if item["actions"]:
                try:
                    item["actions"](page)
                except Exception as act_err:
                    print(f"  Actions warning for {name}: {act_err}", flush=True)
            
            page.screenshot(path=screenshot_path, full_page=False)
            print(f"  -> Captured: {screenshot_path}", flush=True)
        except Exception as e:
            print(f"  -> Error capturing {name}: {e}", flush=True)

    browser.close()

print("\nAll Playwright audits completed!", flush=True)
