import time
import os
import sys

os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_xY7kvd5NqIZJ@ep-curly-dew-b5v7f22f-pooler.c-7.us-east-2.aws.neon.tech/neondb?sslmode=require'
sys.path.insert(0, r'C:\Auto Post FB')

from database import get_connection

t0 = time.time()
with get_connection() as conn:
    t_conn = time.time() - t0
    cursor = conn.cursor()
    
    t0 = time.time()
    cursor.execute("SELECT COUNT(*) FROM articles")
    c = cursor.fetchone()[0]
    t_count = time.time() - t0
    
    t0 = time.time()
    cursor.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 15 OFFSET 0")
    rows = cursor.fetchall()
    t_fetch = time.time() - t0

    print(f"t_conn={t_conn:.3f}s, t_count={t_count:.3f}s, t_fetch={t_fetch:.3f}s, total={t_conn+t_count+t_fetch:.3f}s")
