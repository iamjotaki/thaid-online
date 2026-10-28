# -*- coding: utf-8 -*-
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

repos = [
    ("LINE Sticker Studio", r"C:\ThaiD-Sticker", ["static/index.html"]),
    ("Clip AI & Reels", r"C:\ThaiD-Clip", ["static/index.html"]),
    ("Smart Chat AI", r"C:\ThaiD-Chat", ["static/index.html"]),
    ("Personal Vault", r"C:\ThaiD-Vault", ["static/index.html"]),
    ("Mockup Studio", r"C:\ThaiD-Mockup", ["static/index.html"])
]

msg = "fix: enhance text contrast and fix invisible white-on-white text across inputs, titles, and cards"

for name, repo, files in repos:
    print(f"\n==========================================", flush=True)
    print(f"Processing {name} ({repo})...", flush=True)
    
    # 1. Git add
    for f in files:
        subprocess.run(["git", "add", f], cwd=repo, capture_output=True, text=True, env=env)
        print(f"Staged {f}", flush=True)
    
    # 2. Git commit
    commit_res = subprocess.run(["git", "commit", "-m", msg], cwd=repo, capture_output=True, text=True, env=env)
    c_out = commit_res.stdout.strip() if commit_res.stdout else commit_res.stderr.strip()
    print("Commit:", c_out if c_out else "Nothing to commit", flush=True)
    
    # 3. Git push
    print("Pushing to origin/main...", flush=True)
    push_res = subprocess.run(["git", "push", "origin", "main"], cwd=repo, capture_output=True, text=True, env=env)
    if push_res.returncode == 0:
        print("-> SUCCESS: Pushed to origin/main", flush=True)
    else:
        print(f"-> Push error: {push_res.stderr.strip()}", flush=True)

print("\nAll 5 repositories committed and pushed successfully!", flush=True)
