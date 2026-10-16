import json

with open("books/33283_thompson_calculus/thompson_chapters.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total sections: {len(data)}")
for i, ch in enumerate(data):
    a1 = ch.get("arg1")
    a2 = ch.get("arg2")
    length = ch.get("length", 0)
    print(f"{i+1:2d}: {str(a1):20s} | {str(a2):50s} | {length:6d} chars")
