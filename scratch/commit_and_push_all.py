# -*- coding: utf-8 -*-
import subprocess
import os
import sys

env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

tasks = [
    {
        "name": "Novel Studio (ReadAWrite)",
        "repo": r"C:\ReadAWrite",
        "files": ["server_saas.py", "web_saas_stitch/admin.html", "web_saas_stitch/dashboard.html"],
        "msg": "feat: add user member dashboard (/dashboard) and novel studio admin portal (/admin)",
        "remotes": [("thaid-studio", "main")]
    },
    {
        "name": "LINE Sticker Creator",
        "repo": r"C:\ThaiD-Sticker",
        "files": ["app.py", "static/admin.html", "static/dashboard.html"],
        "msg": "feat: add user member dashboard (/dashboard) and sticker admin portal (/admin)",
        "remotes": [("origin", "main")]
    },
    {
        "name": "Clip AI & Reels",
        "repo": r"C:\ThaiD-Clip",
        "files": ["app.py", "static/admin.html", "static/dashboard.html"],
        "msg": "feat: add user member dashboard (/dashboard) and clip admin portal (/admin)",
        "remotes": [("origin", "main")]
    },
    {
        "name": "Smart Chat AI",
        "repo": r"C:\ThaiD-Chat",
        "files": ["app.py", "static/admin.html", "static/dashboard.html"],
        "msg": "feat: add user member dashboard (/dashboard) and smart chat admin portal (/admin)",
        "remotes": [("origin", "main")]
    },
    {
        "name": "Mockup AI Studio",
        "repo": r"C:\ThaiD-Mockup",
        "files": ["app.py", "static/admin.html", "static/dashboard.html"],
        "msg": "feat: add user member dashboard (/dashboard) and mockup admin portal (/admin)",
        "remotes": [("origin", "main")]
    },
    {
        "name": "Personal Vault",
        "repo": r"C:\ThaiD-Vault",
        "files": ["app.py", "static/admin.html"],
        "msg": "feat: add personal vault dashboard (/dashboard) and vault security admin portal (/admin)",
        "remotes": [("origin", "main")]
    },
    {
        "name": "ThaiD Central Hub & Admin",
        "repo": r"C:\ThaiD.online",
        "files": ["app/admin/page.tsx"],
        "msg": "feat: link all saas member dashboards and admin portals in central super admin",
        "remotes": [("origin", "main")]
    }
]

for task in tasks:
    repo = task["repo"]
    name = task["name"]
    print(f"\n==========================================", flush=True)
    print(f"Processing {name} ({repo})...", flush=True)
    
    # 1. Git add specific files
    for f in task["files"]:
        add_res = subprocess.run(["git", "add", f], cwd=repo, capture_output=True, text=True, env=env)
        if add_res.returncode != 0:
            print(f"Error adding {f}: {add_res.stderr.strip()}", flush=True)
        else:
            print(f"Staged {f}", flush=True)
    
    # 2. Git commit
    commit_res = subprocess.run(["git", "commit", "-m", task["msg"]], cwd=repo, capture_output=True, text=True, env=env)
    c_out = commit_res.stdout.strip() if commit_res.stdout else commit_res.stderr.strip()
    print("Commit:", c_out if c_out else "Nothing new to commit", flush=True)
    
    # 3. Git push
    for remote, branch in task["remotes"]:
        print(f"Pushing to {remote}/{branch}...", flush=True)
        push_res = subprocess.run(["git", "push", remote, branch], cwd=repo, capture_output=True, text=True, env=env)
        if push_res.returncode == 0:
            print(f"-> SUCCESS: Pushed to {remote}/{branch}", flush=True)
        else:
            print(f"-> Push error: {push_res.stderr.strip()}", flush=True)

print("\nAll 7 repositories processed successfully!", flush=True)
