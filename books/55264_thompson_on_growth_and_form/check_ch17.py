import re

with open(r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\55264-h.htm", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect Chapter XVII in HTML
ch17_match = re.search(r'(CHAPTER XVII[\s\S]*?)(?=FINIS|THE END|$)', html, re.IGNORECASE)
if ch17_match:
    ch17_html = ch17_match.group(1)
    imgs = re.findall(r'src=["\']([^"\']+)["\']', ch17_html)
    print("Chapter XVII length:", len(ch17_html))
    print("Images count:", len(imgs))
    print("Sample images:", imgs[:10])
