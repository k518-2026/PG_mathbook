import json
import os
import re

cat = json.load(open(r"E:\GoogleAntigravity\PG_mathbook\catalog.json", encoding="utf-8"))
for b in cat["books"]:
    tex_path = os.path.join(r"E:\GoogleAntigravity\PG_mathbook", b["tex_file"])
    if not os.path.exists(tex_path):
        continue
    with open(tex_path, "r", encoding="utf-8", errors="ignore") as fp:
        lines = fp.readlines()
    bad = []
    for idx, l in enumerate(lines):
        l_strip = l.strip()
        if l_strip.startswith("%"):
            continue
        if "**" in l_strip:
            bad.append((idx + 1, l_strip))
    if bad:
        gid = b.get("gutenberg_id")
        tfile = b.get("tex_file")
        print(f"[{gid}] {tfile}: {len(bad)} lines with **")
        for lnum, lstr in bad[:4]:
            print(f"   L{lnum}: {lstr[:85]}")
