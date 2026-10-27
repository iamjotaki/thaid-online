import sqlite3
from cryptography.fernet import Fernet
from google import genai

conn = sqlite3.connect(r'C:\ThaiD-Vault\vault.db')
cur = conn.cursor()
cur.execute("SELECT value FROM settings WHERE key = 'encryption_key'")
row = cur.fetchone()
f = Fernet(row[0].encode('utf-8'))

for item in cur.execute("SELECT password_encrypted FROM vault_items WHERE title LIKE 'Google API Key #%'"):
    try:
        k = f.decrypt(item[0].encode('utf-8')).decode('utf-8')
        if k.startswith('AIza'):
            client = genai.Client(api_key=k)
            models = client.models.list()
            print("Connected! Available models:")
            for m in models:
                if 'image' in m.name or 'imagen' in m.name:
                    print("-", m.name, m.supported_actions if hasattr(m, 'supported_actions') else '')
            break
    except Exception as e:
        pass
