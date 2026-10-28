import time, sys
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import deploy_app, get_statuses

apps = [1, 2, 3, 5, 6, 7, 8]
print(f"Triggering deployment for apps: {apps}")
for aid in apps:
    deploy_app(aid)
    time.sleep(1)

print("\nMonitoring deployments...")
sys.stdout.flush()

for i in range(40):
    time.sleep(7)
    stats = get_statuses()
    all_done = True
    print(f"\n--- Check #{i+1} ---")
    for aid in apps:
        d = stats.get(aid, {"name": "?", "status": "none", "commit": "none"})
        print(f"App {aid} ({d['name']}): {d['status']} [{d['commit']}]")
        if d['status'] != 'finished':
            all_done = False
    sys.stdout.flush()
    if all_done:
        print("\nAll 7 apps deployed successfully!")
        sys.stdout.flush()
        break
