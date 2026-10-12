import os
import json
import sys

CATALOG_PATH = 'e:/GoogleAntigravity/PG_mathbook/catalog.json'

def load_catalog():
    if os.path.exists(CATALOG_PATH):
        with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"books": []}

cat = load_catalog()
for b in cat.get("books", []):
    b["author"] = "教育情報分析研究会"
    b_id = str(b.get("gutenberg_id"))
    b["gutenberg_url"] = f"https://www.gutenberg.org/ebooks/{b_id}"

with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
    json.dump(cat, f, ensure_ascii=False, indent=2)

print("Updated catalog.json with gutenberg_url for all books.")
