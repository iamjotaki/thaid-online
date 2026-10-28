# -*- coding: utf-8 -*-
import time
import sys
import os

sys.path.append(r"C:\ThaiD.online")
from deploy_batch import deploy_app, get_statuses

apps = [5, 6, 7, 4, 8]  # Deploy Sticker first (the user's app), then Clip, Chat, Vault, Mockup

print(f"Triggering Coolify deployments for apps: {apps}...", flush=True)
for aid in apps:
    deploy_app(aid)
    time.sleep(1.5)

print("\nDeployments queued. Waiting for completion...", flush=True)

start_time = time.time()
max_wait = 400

while time.time() - start_time < max_wait:
    time.sleep(12)
    stats = get_statuses()
    
    finished = []
    
    print("\n-------------------------------------------", flush=True)
    print(f"Deployment Status [{int(time.time() - start_time)}s elapsed]:", flush=True)
    for aid in apps:
        info = stats.get(aid, {"name": f"App {aid}", "status": "unknown", "commit": "???"})
        st = info["status"]
        commit = info["commit"]
        name = info["name"].split(":")[0]
        print(f"  App {aid} ({name}): {st} [{commit}]", flush=True)
        if st == "finished":
            finished.append(aid)
    
    if len(finished) == len(apps):
        print("\nAll 5 applications have finished deployment successfully!", flush=True)
        break

print("\nDeployment monitoring complete.", flush=True)
