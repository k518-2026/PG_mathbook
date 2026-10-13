import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('books/58881_laplace_probability/pg58881_text.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Normalize multiple spaces within lines but keep paragraphs
text_normalized = re.sub(r'[ \t]+', ' ', text)

# Find chapters by "CHAPTER <ROMAN>." pattern
pattern = re.compile(r'\n\s*CHAPTER\s+([IVXLCDM]+)\.?\s*\n\s*([A-Z\s,;.\'-]+?)\n(?=\s*[A-Z])', re.MULTILINE)

matches = list(pattern.finditer(text_normalized))
print(f"Found {len(matches)} chapter headings after normalization.")

# Let's filter matches that occur after the Table of Contents (approx line 150)
real_matches = [m for m in matches if m.start() > 3000]

print(f"Real chapter headings: {len(real_matches)}")
chapters = []
for i, m in enumerate(real_matches):
    num = m.group(1).strip()
    title = m.group(2).strip().replace('\n', ' ')
    start = m.end()
    end = real_matches[i+1].start() if i + 1 < len(real_matches) else len(text_normalized)
    ch_text = text_normalized[start:end].strip()
    
    # Clean up page headers/numbers like "12 PHILOSOPHICAL ESSAY ON PROBABILITIES."
    ch_text = re.sub(r'\n\s*\d+\s+[A-Z\s,.-]+\.\s*\n', '\n', ch_text)
    ch_text = re.sub(r'\n\s*[A-Z\s,.-]+\.\s+\d+\s*\n', '\n', ch_text)
    
    chapters.append({
        "number": num,
        "title": title,
        "length": len(ch_text),
        "text": ch_text
    })
    print(f"Chapter {num}: {title} ({len(ch_text)} chars)")

with open('books/58881_laplace_probability/parsed_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("Saved to parsed_chapters.json successfully!")
