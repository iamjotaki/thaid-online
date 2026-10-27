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

print(f"Loaded {len(keys)} keys from vault.")

# Try keys starting from index 20 (AIza keys)
for idx, k in enumerate(keys[20:30]):
    print(f"Testing key #{21+idx}: {k[:8]}...")
    client = genai.Client(api_key=k)
    try:
        res = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt='3D cute chubby shiba inu dog sticker with thick white die cut border on clean white background, Pixar 3D style',
            config=dict(number_of_images=1, aspect_ratio='1:1')
        )
        if res.generated_images:
            with open("test_key_success.jpg", "wb") as img_f:
                img_f.write(res.generated_images[0].image.image_bytes)
            print(f"SUCCESS with key #{21+idx}!")
            break
    except Exception as e:
        print(f"Key #{21+idx} failed:", str(e)[:120])
