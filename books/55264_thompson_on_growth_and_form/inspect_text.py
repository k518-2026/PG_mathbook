import json
import re

text_path = r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\pg55264.txt"
with open(text_path, "r", encoding="utf-8") as f:
    text = f.read()

manifest_path = r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\thompson_chapters_manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

print(f"Loaded manifest with {len(manifest)} chapters.")
for item in manifest[:3]:
    ch_text = text[item['start_pos']:item['end_pos']]
    print(f"=== {item['number']}: {item['title']} ===")
    lines = [l.strip() for l in ch_text.split('\n') if l.strip()]
    print(f"Lines count: {len(lines)}")
    print("First 3 non-empty lines:")
    for l in lines[:3]:
        print("  ", l[:80])
    print()
