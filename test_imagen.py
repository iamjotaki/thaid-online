import os
from google import genai
from google.genai import types

def get_key():
    with open(r'C:\Auto Post FB\.env', 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.startswith('GEMINI_API_KEY='):
                return line.split('=', 1)[1].strip().strip('"\'')
    return None

api_key = get_key()
print("Key found:", bool(api_key))

if api_key:
    client = genai.Client(api_key=api_key)
    try:
        result = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt='A luxury skincare cosmetic bottle on a sleek white marble podium, studio lighting, minimal, 8k, elegant',
            config=dict(
                number_of_images=1,
                aspect_ratio='1:1',
            )
        )
        for i, img in enumerate(result.generated_images):
            with open(f"test_imagen_{i}.png", "wb") as f:
                f.write(img.image.image_bytes)
        print("Generated imagen test image successfully!")
    except Exception as e:
        print("Imagen error:", e)
