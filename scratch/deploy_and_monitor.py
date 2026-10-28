# -*- coding: utf-8 -*-
import time
import sys
import os

sys.path.append(r"C:\ThaiD.online")
from deploy_batch import deploy_app, get_statuses

apps_to_deploy = [1, 2, 4, 5, 6, 7, 8]

print(f"Triggering Coolify deployments for apps: {apps_to_deploy}...", flush=True)
for aid in apps_to_deploy:
    deploy_app(aid)
    time.sleep(1.5)

print("\nDeployments queued. Waiting for completion...", flush=True)

start_time = time.time()
max_wait = 600  # 10 minutes maximum

while time.time() - start_time < max_wait:
    time.sleep(12)
    stats = get_statuses()
    
    pending = []
    running = []
    finished = []
    failed = []
    
    print("\n-------------------------------------------", flush=True)
    print(f"Deployment Status [{int(time.time() - start_time)}s elapsed]:", flush=True)
    for aid in apps_to_deploy:
        info = stats.get(aid, {"name": f"App {aid}", "status": "unknown", "commit": "???"})
        st = info["status"]
        commit = info["commit"]
        name = info["name"].split(":")[0]
        print(f"  App {aid} ({name}): {st} [{commit}]", flush=True)
        if st in ["queued", "pending"]:
            pending.append(aid)
        elif st in ["in_progress"]:
            running.append(aid)
        elif st in ["finished"]:
            finished.append(aid)
        else:
            failed.append(aid)
    
    if len(finished) == len(apps_to_deploy):
        print("\nAll 7 applications have finished deployment successfully!", flush=True)
        break
    elif failed:
        print(f"\nWarning: apps failed or unknown: {failed}", flush=True)

print("\nDeployment monitoring complete.", flush=True)
