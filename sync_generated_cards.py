import os
import shutil
import glob

artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec"
dest_dir = r"c:\ThaiD.online\public\cards"

pattern = os.path.join(artifact_dir, "*_gen_*.jpg")
files = glob.glob(pattern)
print(f"Found {len(files)} generated files:")

mapping = {
    "mockup_gen_1": "mockup_gen_1.jpg",
    "mockup_gen_2": "mockup_gen_2.jpg",
    "novel_gen_1": "novel_gen_1.jpg",
    "novel_gen_2": "novel_gen_2.jpg",
    "sticker_gen_1": "sticker_gen_1.jpg",
    "sticker_gen_2": "sticker_gen_2.jpg",
    "social_gen_1": "social_gen_1.jpg",
    "chat_gen_1": "chat_gen_1.jpg",
    "clip_gen_1": "clip_gen_1.jpg",
    "vault_gen_1": "vault_gen_1.jpg",
}

for f in files:
    fname = os.path.basename(f)
    for prefix, target_name in mapping.items():
        if fname.startswith(prefix):
            target_path = os.path.join(dest_dir, target_name)
            shutil.copy2(f, target_path)
            print(f"Copied {fname} -> {target_name} ({os.path.getsize(target_path)} bytes)")
