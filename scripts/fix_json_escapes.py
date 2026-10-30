import json
import re

with open("books/16713_dudeney_amusements_in_mathematics/dudeney_full_japanese_cache.json", "r", encoding="utf-8") as f:
    raw = f.read()

# Replace any backslash that is not followed by ", \, /, b, f, n, r, t, or uXXXX
# In Python, we can do this safely:
def replacer(match):
    # match.group(0) is the backslash and the next character
    ch = match.group(1)
    if ch in ['"', '\\', '/', 'b', 'f', 'n', 'r', 't']:
        return match.group(0)
    elif ch == 'u':
        # check if 4 hex digits follow
        return match.group(0)
    else:
        return '\\\\' + ch

fixed = re.sub(r'\\(.)', replacer, raw, flags=re.DOTALL)

try:
    data = json.loads(fixed, strict=False)
    print("Success! Total keys:", len(data))
    with open("books/16713_dudeney_amusements_in_mathematics/dudeney_full_japanese_cache.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Saved clean cache JSON.")
except Exception as e:
    print("Error:", e)
