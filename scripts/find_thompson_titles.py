import re
import json

with open("books/33283_thompson_calculus/33283-t.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Find all \Chapter, \AltChapter, \ChapterStar definitions and uses
pattern = r'(\\Chapter(?:Star)?(?:\[[^\]]*\])?\{[^}]*\}|\x5cAltChapter(?:\[[^\]]*\])?\{[^}]*\})'
matches = re.finditer(pattern, text)
for m in matches:
    start = max(0, m.start() - 20)
    end = min(len(text), m.end() + 100)
    snippet = text[start:end].replace('\n', ' ')
    print(snippet[:120])
