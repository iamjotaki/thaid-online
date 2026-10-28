import time, sys
sys.path.append(r"C:\ThaiD.online")
from deploy_batch import get_statuses

for _ in range(25):
    time.sleep(6)
    s = get_statuses()
    print(f"App 6: {s[6]['status']} [{s[6]['commit']}], App 7: {s[7]['status']} [{s[7]['commit']}], App 8: {s[8]['status']} [{s[8]['commit']}]")
    sys.stdout.flush()
    if s[6]['status'] == 'finished' and s[7]['status'] == 'finished' and s[8]['status'] == 'finished':
        print("ALL 8 APPS ARE FINISHED!")
        sys.stdout.flush()
        break
