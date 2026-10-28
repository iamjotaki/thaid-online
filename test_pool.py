import time
import psycopg2
from psycopg2 import pool

db_url = 'postgresql://neondb_owner:npg_faSu3RjviGh8@ep-curly-dew-b5v7f22f-pooler.c-7.us-east-2.aws.neon.tech/neondb?sslmode=require'
pg_pool = pool.ThreadedConnectionPool(minconn=1, maxconn=5, dsn=db_url)

for i in range(5):
    t0 = time.time()
    conn = pg_pool.getconn()
    cur = conn.cursor()
    cur.execute("SELECT id, title, source, status, published_at, count(*) OVER() as full_count FROM articles ORDER BY id DESC LIMIT 15")
    rows = cur.fetchall()
    total = rows[0][-1] if rows else 0
    cur.close()
    pg_pool.putconn(conn)
    t = time.time() - t0
    print(f"Single query #{i+1} time: {t:.3f}s (total: {total}, items: {len(rows)})")
