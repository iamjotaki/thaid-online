import re

path = r"C:\Auto Post FB\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

func_code = """        function handleImageError(img, idx) {
            img.onerror = null;
            if (img.parentElement) {
                img.parentElement.innerHTML = `
                    <div class="w-full h-full flex flex-col items-center justify-center p-3 text-center bg-stone-50 dark:bg-stone-950">
                        <i class="fa-solid fa-image text-stone-300 dark:text-stone-700 text-2xl mb-1"></i>
                        <button onclick="openCardModal(${idx})" class="text-xs text-blue-600 hover:underline font-semibold">
                            + สร้าง Social Card
                        </button>
                    </div>
                `;
            }
        }

        async function loadNews(page = 1) {"""

if "function handleImageError" not in text:
    text = text.replace("        async function loadNews(page = 1) {", func_code)

# Replace any onerror on img in loadNews
text = re.sub(r'onerror="this\.onerror=null;[^"]+"', 'onerror="handleImageError(this, ${idx})"', text)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("fix_img_error completed successfully!")
