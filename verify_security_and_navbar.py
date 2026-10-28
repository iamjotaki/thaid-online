import urllib.request
import urllib.parse
import json
import time

subdomains = [
    ("Main Portal", "https://thaid.online"),
    ("Novel Studio", "https://novel.thaid.online"),
    ("Social Poster", "https://social.thaid.online"),
    ("LINE Sticker", "https://sticker.thaid.online"),
    ("Clip AI", "https://clip.thaid.online"),
    ("Smart Chat", "https://chat.thaid.online"),
    ("Mockup Studio", "https://mockup.thaid.online")
]

def check_subdomains():
    print("=== 1. Checking Public SaaS Subdomains for Vault Removal ===")
    all_clean = True
    for name, url in subdomains:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                has_vault_link = "vault.thaid.online" in html
                has_vault_text = "Personal Vault" in html
                has_6_tools = "6 เครื่องมือ" in html
                
                status = "PASS" if (not has_vault_link and not has_vault_text) else "FAIL"
                if status == "FAIL":
                    all_clean = False
                print(f"[{status}] {name} ({url}) | vault_link: {has_vault_link} | vault_text: {has_vault_text} | 6_tools_badge: {has_6_tools}")
        except Exception as e:
            print(f"[ERR] {name} ({url}): {e}")
            all_clean = False
    return all_clean

def check_vault_page():
    print("\n=== 2. Checking Vault Public Page for Secrets / Demo Buttons ===")
    url = "https://vault.thaid.online"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            has_demo_btn = "2026 ทันที" in html or "⚡ คลิกเพื่อปลดล็อก" in html
            has_demo_text = "PIN เริ่มต้นระบบ: 2026" in html
            has_private_badge = "Personal Private Vault" in html
            has_saas_menu = "thaidSaasMenu" in html
            
            print(f"Demo button removed: {not has_demo_btn}")
            print(f"Default PIN 2026 text removed: {not has_demo_text}")
            print(f"Private Vault badge present: {has_private_badge}")
            print(f"Public SaaS dropdown removed from Vault: {not has_saas_menu}")
            return (not has_demo_btn) and (not has_demo_text) and has_private_badge
    except Exception as e:
        print(f"[ERR] Vault page check failed: {e}")
        return False

def check_vault_brute_force_and_auth():
    print("\n=== 3. Checking Vault Brute-Force Rate Limiting & Auth ===")
    url = "https://vault.thaid.online/api/auth/verify-pin"
    
    # Send incorrect PINs and verify rate limiting
    print("Testing incorrect PIN responses...")
    for i in range(1, 7):
        data = json.dumps({"pin": f"wrong_{i}"}).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"Attempt {i}: Unexpected 200 OK: {resp.read().decode()}")
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='ignore')
            print(f"Attempt {i}: HTTP {e.code} - {body}")
            if e.code == 429:
                print(f"-> SUCCESS: Brute-force protection activated on attempt {i}!")
                break
        except Exception as e:
            print(f"Attempt {i}: Error {e}")
            break

if __name__ == "__main__":
    check_subdomains()
    check_vault_page()
