# -*- coding: utf-8 -*-
import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.gutenberg.org/files/30155/30155-h/30155-h.htm'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

img_tags = re.findall(r'images/(image\d+\.jpg)', html)
print('Total images in HTML:', len(img_tags), sorted(list(set(img_tags))))

for num in range(1, 61):
    img_name = f'image{num:03d}'
    pos = html.find(img_name)
    if pos != -1:
        snippet = html[max(0, pos-250):min(len(html), pos+300)]
        clean = re.sub(r'<[^>]+>', ' ', snippet)
        clean = ' '.join(clean.split())
        print(f"=== {img_name} ===\n{clean}\n")
