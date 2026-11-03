import os
import re
import urllib.request
import time

html_path = r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\55264-h.htm"
img_dir = r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\images"
os.makedirs(img_dir, exist_ok=True)

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

imgs = sorted(list(set(re.findall(r'src=["\']([^"\']+)["\']', html))))
base_url = "https://www.gutenberg.org/files/55264/55264-h/"

downloaded = 0
skipped = 0
failed = 0

for img_rel in imgs:
    fname = os.path.basename(img_rel)
    local_path = os.path.join(img_dir, fname)
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        skipped += 1
        continue
    url = base_url + img_rel
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(local_path, "wb") as out_f:
                out_f.write(data)
        downloaded += 1
        if downloaded % 25 == 0:
            print(f"Downloaded {downloaded}/{len(imgs)} images...")
        time.sleep(0.05)
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        failed += 1

print(f"Finished: {downloaded} downloaded, {skipped} skipped, {failed} failed. Total images in folder: {len(os.listdir(img_dir))}")
