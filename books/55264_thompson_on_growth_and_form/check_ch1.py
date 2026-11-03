import re

with open(r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\55264-h.htm", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect Chapter I in HTML
ch1_match = re.search(r'(CHAPTER I[\s\S]*?)(?=CHAPTER II)', html, re.IGNORECASE)
if ch1_match:
    ch1_html = ch1_match.group(1)
    print("Chapter I length:", len(ch1_html))
    imgs = re.findall(r'src=["\']([^"\']+)["\']', ch1_html)
    print("Images in Chapter I:", imgs)
else:
    print("Chapter I not found by simple regex")
