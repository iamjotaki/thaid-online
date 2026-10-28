import time, sys
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import get_statuses

print("Watching deployment progress...")
sys.stdout.flush()

for i in range(40):
    time.sleep(8)
    stats = get_statuses()
    all_done = True
    print(f"\n--- Poll #{i+1} ---")
    for aid, d in sorted(stats.items()):
        print(f"App {aid} ({d['name']}): {d['status']} [{d['commit']}]")
        if d['status'] != 'finished':
            all_done = False
    sys.stdout.flush()
    if all_done:
        print("\nAll 8 apps deployed successfully!")
        sys.stdout.flush()
        break
