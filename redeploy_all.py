import sys, time
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import deploy_app, get_statuses

print("Triggering deployments for all apps 1 to 8...")
for app_id in [1, 2, 3, 4, 5, 6, 7, 8]:
    try:
        deploy_app(app_id)
        time.sleep(1)
    except Exception as e:
        print(f"Error deploying app {app_id}: {e}")

print("\nDeployment triggered. Current statuses:")
stats = get_statuses()
for aid, d in sorted(stats.items()):
    print(f"App {aid} ({d['name']}): {d['status']} [{d['commit']}]")
