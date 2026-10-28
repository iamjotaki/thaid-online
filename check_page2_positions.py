from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto("https://thaid.online", wait_until="networkidle")
    page.evaluate("window.scrollTo(0, 830)")
    page.wait_for_timeout(600)
    
    t = page.locator("#services-directory h2").bounding_box()
    c = page.locator(".orbit-carousel-card").first.bounding_box()
    print(f"Title: y={t['y']}, height={t['height']}")
    print(f"Front Card: y={c['y']}, height={c['height']}")
    
    # Save landed screenshot
    page.screenshot(path=r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\audit_page2_final_landed.png")
    print("Saved audit_page2_final_landed.png")
    browser.close()
