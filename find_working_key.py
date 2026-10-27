import sqlite3
from cryptography.fernet import Fernet
from google import genai

conn = sqlite3.connect(r'C:\ThaiD-Vault\vault.db')
cur = conn.cursor()
cur.execute("SELECT value FROM settings WHERE key = 'encryption_key'")
row = cur.fetchone()
f = Fernet(row[0].encode('utf-8'))

keys = []
for item in cur.execute("SELECT password_encrypted FROM vault_items WHERE title LIKE 'Google API Key #%'"):
    try:
        keys.append(f.decrypt(item[0].encode('utf-8')).decode('utf-8'))
    except Exception:
        pass

print(f"Testing {len(keys)} keys from vault...")
working_key = None

for i, k in enumerate(keys[25:50]):
    try:
        client = genai.Client(api_key=k)
        response = client.models.generate_content(
            model='gemini-2.5-flash-image',
            contents='A cute 3D sticker of a happy cat chef',
        )
        for p in response.candidates[0].content.parts:
            if p.inline_data:
                with open("test_key_cat.jpg", "wb") as f_out:
                    f_out.write(p.inline_data.data)
                print(f"SUCCESS with key index {26+i}! Saved test_key_cat.jpg")
                working_key = k
                break
        if working_key:
            break
    except Exception as e:
        err = str(e)
        if '429' in err:
            continue
        print(f"Key {26+i} error:", err[:80])

if not working_key:
    print("No key in this batch had image generation quota.")
