with open(r'C:\ThaiD.online\app\page.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Update onScroll logic in page.tsx
old_onscroll = """            const rect = trackRef.current.getBoundingClientRect();
            const trackScrollable = trackRef.current.offsetHeight - window.innerHeight;
            
            // Calculate scroll ratio through the 200vh track
            const currentScroll = -rect.top;
            const progress = Math.min(1, Math.max(0, currentScroll / Math.max(1, trackScrollable)));
            
            // Studio motion curves: scatter completes within first 75% of track scroll
            const scatterFactor = Math.min(1, progress / 0.55);
            const opacity = Math.max(0, 1 - scatterFactor);
            const scatter = scatterFactor;"""

new_onscroll = """            const scroll = window.scrollY;
            const threshold = Math.max(1, window.innerHeight * 0.75);
            const progress = Math.min(1, Math.max(0, scroll / threshold));
            
            const scatter = progress;
            const opacity = Math.max(0, 1 - progress);"""

if old_onscroll in text:
    text = text.replace(old_onscroll, new_onscroll)
    print("Replaced onScroll logic!")
else:
    old_crlf = old_onscroll.replace('\n', '\r\n')
    if old_crlf in text:
        text = text.replace(old_crlf, new_onscroll.replace('\n', '\r\n'))
        print("Replaced onScroll logic with CRLF!")
    else:
        print("Could not match old_onscroll, using regex...")
        text = re.sub(
            r'const rect = trackRef\.current\.getBoundingClientRect\(\);[\s\S]*?const scatter = scatterFactor;',
            new_onscroll,
            text
        )
        print("Regex replaced onScroll logic!")

# Update auto-snap wheel threshold to be clean
text = text.replace("window.scrollY < 200 && e.deltaY > 8", "window.scrollY < 80 && e.deltaY > 15")
text = text.replace("window.scrollY < 160 && diff > 20", "window.scrollY < 60 && diff > 25")

with open(r'C:\ThaiD.online\app\page.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated page.tsx successfully!")
