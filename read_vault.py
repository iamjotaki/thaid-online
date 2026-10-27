import sqlite3
from cryptography.fernet import Fernet

conn = sqlite3.connect(r'C:\ThaiD-Vault\vault.db')
cur = conn.cursor()
cur.execute("SELECT value FROM settings WHERE key = 'encryption_key'")
row = cur.fetchone()
if row:
    f = Fernet(row[0].encode('utf-8'))
    for item in cur.execute('SELECT title, username, password_encrypted FROM vault_items'):
        try:
            pwd = f.decrypt(item[2].encode('utf-8')).decode('utf-8')
            print("VAULT ITEM:", item[0], "|", item[1], "|", pwd[:10] + '...')
        except Exception:
            pass
