import os
from PIL import Image

paths = [
    ("mockup_real_1", r"C:\ThaiD-Mockup\outputs\mockup_1793092259_25d946.jpg"),
    ("mockup_real_2", r"C:\ThaiD-Mockup\outputs\test_composite.jpg"),
    ("sticker_real_1", r"C:\ThaiD-Sticker\output\proj_test_api\composite_preview.png"),
    ("sticker_real_2", r"C:\ThaiD-Sticker\output\test_pack\composite_preview.png"),
    ("sticker_real_3", r"C:\ThaiD-Sticker\output\proj_test_api\01.png"),
    ("novel_real_1", r"C:\ReadAWrite\data\covers\cover_RAW-17F2D1_1792332067.jpg"),
    ("novel_real_2", r"C:\ReadAWrite\data\covers\cover_RAW-6C288F_1792745407.jpg"),
    ("novel_real_3", r"C:\ReadAWrite\data\covers\cover_temp_1792745470497.jpg"),
    ("social_real_1", r"C:\Auto Post FB\downloads\cards\card_1_1792648031.jpg"),
    ("social_real_2", r"C:\Auto Post FB\downloads\cards\card_2_1792648114.jpg"),
    ("social_real_3", r"C:\Auto Post FB\static\generated_posts\flow_post_1792568443353.jpg"),
]

for label, p in paths:
    if os.path.exists(p):
        try:
            im = Image.open(p)
            print(f"[{label}] {p} -> Size: {im.size}, Mode: {im.mode}")
        except Exception as e:
            print(f"[{label}] Error: {e}")
    else:
        print(f"[{label}] NOT FOUND: {p}")
