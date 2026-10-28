with open(r'C:\ThaiD.online\app\globals.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Update .hero-track
text = re.sub(r'\.hero-track\s*\{[\s\S]*?\}', '''.hero-track {
  min-height: 100vh;
  position: relative;
  background: #ffffff;
}''', text)

# Update .hero-sticky
text = re.sub(r'\.hero-sticky\s*\{[\s\S]*?\}', '''.hero-sticky {
  position: relative;
  height: 100vh;
  min-height: 680px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: visible;
  z-index: 10;
  pointer-events: auto;
}''', text)

# Update .services-sheet-stage
text = re.sub(r'\.services-sheet-stage\s*\{[\s\S]*?\}', '''.services-sheet-stage {
  position: relative;
  z-index: 30;
  background: #ffffff;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
  box-shadow: 0 -20px 50px -10px rgba(0, 0, 0, 0.08), 0 -1px 3px rgba(0, 0, 0, 0.04);
  border-top: 1px solid rgba(0, 0, 0, 0.06);
  margin-top: 0;
  padding-top: 40px;
  scroll-margin-top: 70px;
  transition: transform 0.25s ease-out;
}''', text, count=1)

# Update media query services-sheet-stage
text = re.sub(r'(@media\s*\(min-width:\s*640px\)\s*\{\s*\.services-sheet-stage\s*\{)[\s\S]*?(\})', r'''\1
    border-top-left-radius: 56px;
    border-top-right-radius: 56px;
    margin-top: 0;
    padding-top: 60px;
  \2''', text)

with open(r'C:\ThaiD.online\app\globals.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated globals.css with margin-top: 0 and 100vh hero!")
