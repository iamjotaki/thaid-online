import urllib.request
import ssl
import time

ENDPOINTS = [
    ("ThaiD Main Portal", "https://thaid.online"),
    ("Novel AI Pro Studio", "https://novel.thaid.online"),
    ("Social Auto-Poster", "https://social.thaid.online"),
    ("ThaiD Vault", "https://vault.thaid.online"),
    ("LINE Sticker Studio", "https://sticker.thaid.online"),
    ("AI Clip Studio", "https://clip.thaid.online"),
    ("LINE Smart Chatbot", "https://chat.thaid.online"),
    ("Mockup AI Studio", "https://mockup.thaid.online"),
]

def check_all():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print(f"{'Endpoint':<23} | {'Status':<6} | {'Time':<6} | {'White Canvas':<14} | {'Google Sans':<12} | {'Card/Tokens'}")
    print("-" * 80)

    for name, url in ENDPOINTS:
        t0 = time.time()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
                elapsed = time.time() - t0
                status = resp.status
                body = resp.read().decode('utf-8', errors='ignore')
                has_white = ('#ffffff' in body.lower() or 'bg-white' in body) and ('#171717' in body or '#1f242d' in body or 'rgb(255' in body)
                has_font = 'Google Sans' in body or 'Google+Sans' in body
                has_cards = 'fastwork-white-card' in body or 'rounded-full' in body or 'box-shadow' in body or 'card' in body
                print(f"{name:<23} | {status:<6} | {elapsed:.2f}s | {str(has_white):<14} | {str(has_font):<12} | {str(has_cards)}")
        except Exception as e:
            elapsed = time.time() - t0
            print(f"{name:<23} | ERROR  | {elapsed:.2f}s | {e}")

if __name__ == '__main__':
    check_all()
