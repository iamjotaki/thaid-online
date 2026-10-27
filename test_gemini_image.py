import sqlite3
from cryptography.fernet import Fernet
from google import genai
from google.genai import types

conn = sqlite3.connect(r'C:\ThaiD-Vault\vault.db')
cur = conn.cursor()
cur.execute("SELECT value FROM settings WHERE key = 'encryption_key'")
row = cur.fetchone()
f = Fernet(row[0].encode('utf-8'))

key = None
for item in cur.execute("SELECT password_encrypted FROM vault_items WHERE title LIKE 'Google API Key #%'"):
    try:
        k = f.decrypt(item[0].encode('utf-8')).decode('utf-8')
        if k.startswith('AIza'):
            key = k
            break
    except Exception:
        pass

print("Using key:", key[:8])
client = genai.Client(api_key=key)

try:
    response = client.models.generate_content(
        model='gemini-2.5-flash-image',
        contents='A cute 3D Pixar clay render of a chubby Shiba Inu puppy sticker with thick white die cut border on pure white background',
    )
    print("Response parts count:", len(response.candidates[0].content.parts))
    for i, p in enumerate(response.candidates[0].content.parts):
        if p.inline_data:
            print(f"Part {i} is image! mime: {p.inline_data.mime_type}")
            with open("test_flash_image.jpg", "wb") as img_out:
                img_out.write(p.inline_data.data)
            print("Successfully saved test_flash_image.jpg!")
        else:
            print(f"Part {i} text: {p.text[:100] if p.text else ''}")
except Exception as e:
    print("Error:", e)
