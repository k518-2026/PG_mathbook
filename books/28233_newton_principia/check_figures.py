import re

htm_path = r"E:\GoogleAntigravity\PG_mathbook\books\28233_newton_principia\28233-h.htm"
with open(htm_path, "r", encoding="utf-8", errors="ignore") as f:
    htm = f.read()

imgs = re.findall(r'src=["\']([^"\']+)["\']', htm)
unique_imgs = sorted(list(set(imgs)))
non_symbol_imgs = [img for img in unique_imgs if not img.startswith("images/$")]
print(f"Non-symbol figures count: {len(non_symbol_imgs)}")
print("Sample geometric figures:", non_symbol_imgs[:25])
