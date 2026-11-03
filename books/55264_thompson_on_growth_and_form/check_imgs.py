import re
import os

html_path = r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\55264-h.htm"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
print(f"Total image tags: {len(imgs)}")
unique_imgs = sorted(list(set(imgs)))
print(f"Total unique images: {len(unique_imgs)}")
print("Sample:", unique_imgs[:15])
