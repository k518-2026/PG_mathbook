import re

with open("books/33283_thompson_calculus/33283-t.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Let's find \Chapter[... followed by newlines
pattern = r'\\Chapter(?:Star)?\[([^\]]*)\](?:\s*\{([^}]+)\})?(?:\s*\{([^}]+)\})?'
for m in re.finditer(pattern, text):
    start = m.start()
    snippet = text[start:start+180].replace('\n', ' ')
    print(snippet)
