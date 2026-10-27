import os
import math
from PIL import Image, ImageDraw, ImageFont

os.makedirs("c:/ThaiD.online/public/avatars", exist_ok=True)

# Generate 10 high-resolution vibrant creator avatars
creators = [
    ("chapavich", "#0569ff", "#00d2ff", "C", "Chapavich T."),
    ("weng", "#171717", "#3b82f6", "W", "Weng Kitsana"),
    ("leobeer", "#e85a2d", "#f59e0b", "L", "LEOBEER"),
    ("slayalldeep", "#ec4899", "#8b5cf6", "S", "SlayAllDeep"),
    ("bold", "#10b981", "#059669", "B", "Bold Studio"),
    ("buttercup", "#f59e0b", "#ef4444", "B", "Buttercup AI"),
    ("pakincht", "#6366f1", "#a855f7", "P", "Pakinchit"),
    ("peter", "#0284c7", "#06b6d4", "P", "Peter Visuals"),
    ("mod", "#8b5cf6", "#ec4899", "M", "MOD SUPACHA"),
    ("nam", "#14b8a6", "#3b82f6", "N", "Nguyen Van Nam")
]

for name, color1, color2, initial, full in creators:
    size = 256
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw circular gradient or styled circle
    for r in range(size // 2, 0, -1):
        ratio = r / (size // 2)
        # interpolate colors
        # Let's draw outer circle
        pass
        
    # Draw circle
    draw.ellipse([8, 8, size - 8, size - 8], fill=color1, outline="#ffffff", width=6)
    
    # Draw decorative geometric elements
    draw.ellipse([size * 0.25, size * 0.15, size * 0.75, size * 0.65], fill=color2)
    draw.ellipse([size * 0.15, size * 0.65, size * 0.85, size * 1.35], fill="#1f242d")
    
    path = f"c:/ThaiD.online/public/avatars/{name}.png"
    img.save(path, "PNG")
    print(f"Created {path}")

print("Avatars generated successfully!")
