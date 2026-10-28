path = r"C:\ThaiD.online\app\page.tsx"
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace handleScrollDown and insert auto-snap hook
old_block = """  const handleScrollDown = () => {
    const target = document.getElementById("services-directory");
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    } else {
      window.scrollTo({ top: window.innerHeight * 1.4, behavior: "smooth" });
    }
  };"""

new_block = """  const handleScrollDown = () => {
    const target = document.getElementById("services-directory");
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    } else {
      window.scrollTo({ top: window.innerHeight * 0.9, behavior: "smooth" });
    }
  };

  // Auto-Snap to Page 2 on scroll down (เด้งหน้าที่ 2 ขึ้นมาอัตโนมัติ ไม่เมื่อยนิ้ว):
  useEffect(() => {
    let isSnapping = false;
    let touchStartY = 0;

    const snapToPage2 = () => {
      if (isSnapping) return;
      const target = document.getElementById("services-directory");
      if (target) {
        isSnapping = true;
        target.scrollIntoView({ behavior: "smooth" });
        setTimeout(() => {
          isSnapping = false;
        }, 1000);
      }
    };

    const handleWheel = (e: WheelEvent) => {
      if (!isSnapping && window.scrollY < 200 && e.deltaY > 8) {
        snapToPage2();
      }
    };

    const handleTouchStart = (e: TouchEvent) => {
      touchStartY = e.touches[0].clientY;
    };

    const handleTouchMove = (e: TouchEvent) => {
      if (isSnapping) return;
      const currentY = e.touches[0].clientY;
      const diff = touchStartY - currentY;
      if (window.scrollY < 160 && diff > 20) {
        snapToPage2();
      }
    };

    window.addEventListener("wheel", handleWheel, { passive: true });
    window.addEventListener("touchstart", handleTouchStart, { passive: true });
    window.addEventListener("touchmove", handleTouchMove, { passive: true });

    return () => {
      window.removeEventListener("wheel", handleWheel);
      window.removeEventListener("touchstart", handleTouchStart);
      window.removeEventListener("touchmove", handleTouchMove);
    };
  }, []);"""

if old_block in text:
    text = text.replace(old_block, new_block)
    print("Replaced handleScrollDown and added auto-snap hook!")
else:
    # Try normalized CRLF
    old_block_crlf = old_block.replace('\n', '\r\n')
    if old_block_crlf in text:
        text = text.replace(old_block_crlf, new_block.replace('\n', '\r\n'))
        print("Replaced with CRLF!")
    else:
        print("Could not match old_block!")

# Update scatter factor to be responsive
text = text.replace("const scatterFactor = Math.min(1, progress / 0.72);", "const scatterFactor = Math.min(1, progress / 0.55);")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated page.tsx successfully!")
