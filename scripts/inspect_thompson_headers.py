import json

with open('books/33283_thompson_calculus/thompson_chapters.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, ch in enumerate(data):
    lines = ch['text'].split('\n')
    header_lines = [l.strip() for l in lines[:10] if any(k in l for k in ['\\Chapter', '\\AltChapter', '\\ChapterStar'])]
    print(f"{i+1:2d}: arg1={repr(ch.get('arg1'))} arg2={repr(ch.get('arg2'))} -> {header_lines}")
