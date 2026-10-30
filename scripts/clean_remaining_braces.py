import json
import re

cache_path = "books/16713_dudeney_amusements_in_mathematics/dudeney_full_japanese_cache.json"
with open(cache_path, "r", encoding="utf-8") as f:
    cache = json.load(f)

text = json.dumps(cache, ensure_ascii=False)
text = text.replace("值", "値")
text = text.replace("夠", "足")
text = text.replace("廁", "側")
text = text.replace("퀸", "クイーン")
text = text.replace("اسمن", "")
text = text.replace("اسم", "")
text = text.replace("ا", "")
text = text.replace("س", "")
text = text.replace("م", "")
text = text.replace("ن", "")

cache = json.loads(text)

p137 = cache["137"]
p137["problem_ja"] = p137["problem_ja"].replace("{", "（").replace("}", "）")

p343 = cache["343"]
p343["solution_ja"] = re.sub(r'[{}\"]', '', p343["solution_ja"])
p343["solution_ja"] = re.sub(r'\s*:\s*', '：', p343["solution_ja"]).strip()

p374 = cache["374"]
p374["solution_ja"] = re.sub(r'[{}\"]', '', p374["solution_ja"])
p374["solution_ja"] = re.sub(r'\s*:\s*', '：', p374["solution_ja"]).strip()

# Check all fields for unbalanced braces
for k, v in cache.items():
    for fld in ["problem_ja", "solution_ja", "title_ja"]:
        s = v.get(fld, "")
        if s.count("{") != s.count("}"):
            v[fld] = s.replace("{", "（").replace("}", "）")

with open(cache_path, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print("Braces and character cleanups completed successfully.")
