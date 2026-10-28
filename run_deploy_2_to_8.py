import sys, time
sys.path.append(r'C:\ThaiD.online')
from deploy_batch import deploy_app, get_statuses

print('Queueing deployments for apps 2 through 8...')
for app_id in [2, 3, 4, 5, 6, 7, 8]:
    deploy_app(app_id)
    time.sleep(1)

print('\nInitial deployment statuses:')
stats = get_statuses()
for aid, d in sorted(stats.items()):
    print(f"App {aid} ({d['name']}): {d['status']} [{d['commit']}]")
