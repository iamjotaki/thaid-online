import subprocess
import os

video_path = r"C:\ThaiD-Clip\output\test_run\clip_test_run.mp4"
out_frame = r"C:\ThaiD.online\public\cards\clip_real_1.jpg"

if os.path.exists(video_path):
    cmd = ["ffmpeg", "-y", "-ss", "00:00:02", "-i", video_path, "-vframes", "1", "-q:v", "2", out_frame]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("FFmpeg extracted frame:", res.returncode, "Exists:", os.path.exists(out_frame))
else:
    print("Video not found:", video_path)
