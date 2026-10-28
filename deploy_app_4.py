import sys, time
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import deploy_app, get_statuses

print("Deploying App 4 (ThaiD-Vault)...")
deploy_app(4)

for i in range(25):
    time.sleep(5)
    s = get_statuses()
    d = s.get(4, {})
    status = d.get('status', 'none')
    commit = d.get('commit', 'none')
    print(f"Check {i+1}: App 4 is {status} [{commit}]")
    sys.stdout.flush()
    if status == 'finished' and commit.startswith('04796b9'):
        print("Vault deployed successfully!")
        break
