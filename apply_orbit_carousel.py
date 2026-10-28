path = r"C:\ThaiD.online\app\page.tsx"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Add import
import_line = 'import StudioOrbitCarousel from "./components/StudioOrbitCarousel";\n'
if import_line not in lines:
    lines.insert(4, import_line)

# Find start line (around Minimalist Pill Filter Tabs)
start_idx = -1
end_idx = -1
for i, l in enumerate(lines):
    if "Minimalist Pill Filter Tabs" in l:
        start_idx = i
        break

for i in range(start_idx, len(lines)):
    if "</main>" in lines[i]:
        # The line before </main> is the end of the grid (i.e. lines[i-2] is </div>)
        end_idx = i
        break

print(f"Replacing lines {start_idx+1} to {end_idx}...")

replacement_lines = [
    "        {/* 3D Orbit Carousel Showcase (ม้าหมุน 3 มิติ 360 องศา) */}\n",
    "        <StudioOrbitCarousel />\n",
    "\n"
]

new_lines = lines[:start_idx] + replacement_lines + lines[end_idx:]

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully replaced static grid with StudioOrbitCarousel in page.tsx!")
