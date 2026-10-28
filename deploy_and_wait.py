import time, sys
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import deploy_app, get_statuses

apps_to_deploy = [1, 2, 3, 5, 6, 7, 8]
print(f"Triggering deployment for apps: {apps_to_deploy}")
for aid in apps_to_deploy:
    deploy_app(aid)
    time.sleep(1)

print("\nWaiting for deployments to complete...")
sys.stdout.flush()

for i in range(40):
    time.sleep(8)
    stats = get_statuses()
    all_done = True
    print(f"\n--- Check #{i+1} ---")
    for aid in apps_to_deploy:
        d = stats.get(aid, {"name": "?", "status": "none", "commit": "none"})
        print(f"App {aid} ({d['name']}): {d['status']} [{d['commit']}]")
        if d['status'] != 'finished':
            all_done = False
    sys.stdout.flush()
    if all_done:
        print("\nAll targeted apps finished deploying successfully!")
        sys.stdout.flush()
        break
