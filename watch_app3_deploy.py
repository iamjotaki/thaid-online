import time, sys
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import get_statuses

print("Watching App 3 deployment...")
for i in range(35):
    time.sleep(6)
    stats = get_statuses()
    d = stats.get(3, {"name": "?", "status": "none", "commit": "none"})
    print(f"Check #{i+1}: App 3 ({d['name']}) -> {d['status']} [{d['commit']}]")
    sys.stdout.flush()
    if d['status'] == 'finished' and d['commit'].startswith('e7b21eb'):
        print("\nApp 3 deployed successfully with commit e7b21eb!")
        break
    if d['status'] == 'failed':
        print("\nApp 3 deployment failed!")
        break
