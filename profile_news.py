import time
import os
import sys

os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_xY7kvd5NqIZJ@ep-curly-dew-b5v7f22f-pooler.c-7.us-east-2.aws.neon.tech/neondb?sslmode=require'
sys.path.insert(0, r'C:\Auto Post FB')

from database import get_paginated_articles
from ai_rewriter import detect_article_category, get_card_category_and_theme

for i in range(3):
    t0 = time.time()
    paginated = get_paginated_articles(page=1, limit=15)
    t_db = time.time() - t0

    t0 = time.time()
    for art in paginated['items']:
        cat_type = detect_article_category(art.get('title', ''), art.get('summary', ''), art.get('source', ''))
        c_cat, c_theme = get_card_category_and_theme(cat_type, title_source=f"{art.get('title','')} {art.get('source','')}")
    t_loop = time.time() - t0

    print(f"Run {i+1}: DB time = {t_db:.3f}s, Loop time = {t_loop:.3f}s, Total = {t_db + t_loop:.3f}s")
