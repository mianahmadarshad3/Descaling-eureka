import os
import subprocess

TOKEN = "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" # <--- Put your token inside these quotes
USERNAME = "mianahmadarshad3"
REPO_NAME = "Descaling-eureka"

REMOTE_URL = f"https://{USERNAME}:{TOKEN}@github.com/{USERNAME}/{REPO_NAME}.git"

print("Setting secure remote URL...")
subprocess.run(["git", "remote", "set-url", "origin", REMOTE_URL], check=True)

print("Pushing code to GitHub...")
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)

if result.returncode == 0:
    print("🚀 Success! Your code is live on GitHub.")
else:
    print("❌ Error uploading:")
    print(result.stderr)