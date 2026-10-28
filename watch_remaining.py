import time, sys
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import get_statuses

apps = [3, 5, 6, 7, 8]

for i in range(50):
    time.sleep(7)
    stats = get_statuses()
    all_done = True
    print(f"--- Check #{i+1} ---")
    for aid in [1, 2, 3, 5, 6, 7, 8]:
        d = stats.get(aid, {"name": "?", "status": "none", "commit": "none"})
        print(f"App {aid} ({d['name']}): {d['status']} [{d['commit']}]")
        if d['status'] != 'finished':
            all_done = False
    sys.stdout.flush()
    if all_done:
        print("\nALL APPS DEPLOYED SUCCESSFULLY!")
        sys.stdout.flush()
        break
