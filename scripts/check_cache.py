# -*- coding: utf-8 -*-
import json
import os

p = "books/57359_venn_logic_of_chance/venn_full_translation_math_verified.json"
if os.path.exists(p):
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    print("Completed chapters in cache:", len(d))
    for k in d:
        print(f"{k}: {len(d[k].get('japanese_translation', ''))} chars, title: {d[k].get('title_en', '')}")
else:
    print("Cache file does not exist.")
