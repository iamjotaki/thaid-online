import urllib.request
import json

url = "https://vault.thaid.online/api/auth/verify-pin"

print("--- Testing Live Brute-Force Rate Limiting ---")
for i in range(1, 4):
    payload = json.dumps({"pin": f"wrong_{i}"}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}, method="POST")
    try:
        urllib.request.urlopen(req)
        print(f"Attempt {i}: Unexpected success")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"Attempt {i}: HTTP {e.code} -> {body}")

print("\n--- Testing Live Legitimate Unlock with 2026 ---")
payload = json.dumps({"pin": "2026"}).encode("utf-8")
req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}, method="POST")
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"Success! Token received: {res.get('token')[:8]}... Message: {res.get('message')}")
        token = res.get('token')
        
        # Test fetching vault items
        items_url = "https://vault.thaid.online/api/items"
        ireq = urllib.request.Request(items_url, headers={"X-Vault-Token": token, "User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(ireq) as iresp:
            items = json.loads(iresp.read().decode("utf-8"))
            print(f"Total Vault Items retrieved: {len(items)} items!")
except urllib.error.HTTPError as e:
    print(f"Unlock error: HTTP {e.code} -> {e.read().decode('utf-8')}")
