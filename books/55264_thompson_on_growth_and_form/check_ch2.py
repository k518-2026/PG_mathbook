import re

with open(r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\55264-h.htm", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect Chapter II in HTML
ch2_match = re.search(r'(CHAPTER II[\s\S]*?)(?=CHAPTER III)', html, re.IGNORECASE)
if ch2_match:
    ch2_html = ch2_match.group(1)
    print("Chapter II length:", len(ch2_html))
    imgs = re.findall(r'src=["\']([^"\']+)["\']', ch2_html)
    print("Images in Chapter II:", imgs)
else:
    print("Chapter II not found by simple regex")
