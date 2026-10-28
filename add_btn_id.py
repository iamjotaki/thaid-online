path = r"C:\Auto Post FB\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

if 'id="thaidSaasBtn"' not in text:
    text = text.replace('onclick="toggleThaiDSaasMenu()"', 'id="thaidSaasBtn" onclick="toggleThaiDSaasMenu()"')
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Added thaidSaasBtn id successfully!")
else:
    print("Already has thaidSaasBtn id!")
