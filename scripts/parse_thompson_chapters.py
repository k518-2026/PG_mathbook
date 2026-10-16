import re

with open("books/33283_thompson_calculus/33283-t.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect \Chapter with 3 arguments or 2 arguments
pattern = r'\\Chapter(?:\[[^\]]*\])?\{([^}]+)\}\{([^}]+)\}'
matches = list(re.finditer(pattern, text))
print(f"Total \\Chapter matches: {len(matches)}")
for m in matches:
    print(f"Number: {m.group(1):8s} | Title: {m.group(2)}")
