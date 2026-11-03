import re

with open(r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\55264-h.htm", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect Chapter XI in HTML
ch11_match = re.search(r'(CHAPTER XI[\s\S]*?)(?=CHAPTER XII)', html, re.IGNORECASE)
if ch11_match:
    ch11_html = ch11_match.group(1)
    imgs = re.findall(r'src=["\']([^"\']+)["\']', ch11_html)
    print("Chapter XI length:", len(ch11_html))
    print("Images count:", len(imgs))
    print("Sample images:", imgs[:10])
