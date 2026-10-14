# -*- coding: utf-8 -*-
import json
import os

cache_file = "books/57359_venn_logic_of_chance/venn_full_translation_math_verified.json"
with open(cache_file, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

pos2 = text.find('"Chapter_II"')
if pos2 != -1:
    valid_part = text[:pos2].rstrip().rstrip(",") + "\n}"
    try:
        d = json.loads(valid_part)
        print("Recovered keys:", list(d.keys()))
        with open(cache_file, "w", encoding="utf-8") as out_f:
            json.dump(d, out_f, ensure_ascii=False, indent=2)
        print("Successfully recovered Chapter I cache!")
    except Exception as e:
        print("Error parsing json:", e)
else:
    print("Chapter_II not found")
