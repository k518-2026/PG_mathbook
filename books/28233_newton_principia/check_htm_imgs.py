import re

htm_path = r"E:\GoogleAntigravity\PG_mathbook\books\28233_newton_principia\28233-h.htm"
with open(htm_path, "r", encoding="utf-8", errors="ignore") as f:
    htm = f.read()

imgs = re.findall(r'src=["\']([^"\']+)["\']', htm)
unique_imgs = sorted(list(set(imgs)))
print(f"Total image tags: {len(imgs)}")
print(f"Total unique images: {len(unique_imgs)}")
print("Sample images:", unique_imgs[:20])
