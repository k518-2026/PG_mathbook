# -*- coding: utf-8 -*-
"""
Extract clean chapters from Henri Poincare's Science and Hypothesis (#37157)
"""

import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('books/37157_poincare_science_and_hypothesis/pg37157.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Normalize spacing
text = re.sub(r'[ \t]+', ' ', text)

chapter_defs = [
    ("I", "On the Nature of Mathematical Reasoning", r"CHAPTER\s+I\.\s*\n\s*ON\s+THE\s+NATURE\s+OF\s+MATHEMATICAL\s+REASONING"),
    ("II", "Mathematical Magnitude and Experiment", r"CHAPTER\s+II\.\s*\n\s*MATHEMATICAL\s+MAGNITUDE\s+AND\s+EXPERIMENT\."),
    ("III", "Non-Euclidean Geometries", r"CHAPTER\s+III\.\s*\n\s*NON-EUCLIDEAN\s+GEOMETRIES\."),
    ("IV", "Space and Geometry", r"CHAPTER\s+IV\.\s*\n\s*SPACE\s+AND\s+GEOMETRY\."),
    ("V", "Experiment and Geometry", r"CHAPTER\s+V\.\s*\n\s*EXPERIMENT\s+AND\s+GEOMETRY\."),
    ("VI", "The Classical Mechanics", r"CHAPTER\s+VI\.\s*\n\s*THE\s+CLASSICAL\s+MECHANICS\."),
    ("VII", "Relative and Absolute Motion", r"CHAPTER\s+VII\.\s*\n\s*RELATIVE\s+AND\s+ABSOLUTE\s+MOTION\."),
    ("VIII", "Energy and Thermo-Dynamics", r"CHAPTER\s+VIII\.\s*\n\s*ENERGY\s+AND\s+THERMO-DYNAMICS\."),
    ("IX", "Hypotheses in Physics", r"CHAPTER\s+IX\.\s*\n\s*HYPOTHESES\s+IN\s+PHYSICS\."),
    ("X", "The Theories of Modern Physics", r"CHAPTER\s+X\.\s*\n\s*THE\s+THEORIES\s+OF\s+MODERN\s+PHYSICS\."),
    ("XI", "The Calculus of Probabilities", r"CHAPTER\s+XI\.\s*\n\s*THE\s+CALCULUS\s+OF\s+PROBABILITIES\."),
    ("XII", "Optics and Electricity", r"CHAPTER\s+XII\.\w*\s*\n\s*OPTICS\s+AND\s+ELECTRICITY"),
    ("XIII", "Electro-Dynamics", r"CHAPTER\s+XIII\.\s*\n\s*ELECTRO-DYNAMICS\.")
]

positions = []
curr_search = 1000 # After TOC
for num, title, pat in chapter_defs:
    m = re.search(pat, text[curr_search:], re.IGNORECASE)
    if m:
        start_idx = curr_search + m.start()
        end_idx = curr_search + m.end()
        positions.append((num, title, start_idx, end_idx))
        curr_search = end_idx # Move forward sequentially!
    else:
        print(f"FAILED TO FIND: Chapter {num} - {title}")

print(f"Successfully found {len(positions)} / 13 chapters!")

chapters = []
for i in range(len(positions)):
    num, title, start_idx, end_idx = positions[i]
    next_start = positions[i+1][2] if i + 1 < len(positions) else len(text)
    ch_text = text[end_idx:next_start].strip()
    
    # Clean running page headers
    ch_text = re.sub(r'\n\s*\d+\s+SCIENCE\s+AND\s+HYPOTHESIS\.\s*\n', '\n', ch_text, flags=re.IGNORECASE)
    ch_text = re.sub(r'\n\s*SCIENCE\s+AND\s+HYPOTHESIS\.\s+\d+\s*\n', '\n', ch_text, flags=re.IGNORECASE)
    ch_text = re.sub(r'(\b[a-zA-Z]+)-\s*\n\s*([a-zA-Z]+\b)', r'\1\2', ch_text)
    
    paragraphs = [p.strip().replace('\n', ' ') for p in ch_text.split('\n\n') if p.strip()]
    clean_body = '\n\n'.join(paragraphs)
    
    chapters.append({
        "number": num,
        "title": title,
        "length": len(clean_body),
        "text": clean_body
    })
    print(f"Chapter {num}: {title} ({len(clean_body)} chars)")

with open('books/37157_poincare_science_and_hypothesis/poincare_13_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("Saved clean chapters to poincare_13_chapters.json!")
