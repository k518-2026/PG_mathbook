import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('books/58881_laplace_probability/pg58881_text.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Map of chapters with precise patterns
chapter_defs = [
    ("I", "Introduction", r"CHAPTER\s+I\.\s*\n\s*INTRODUCTION\."),
    ("II", "Concerning Probability", r"CHAPTER\s+II\.\s*\n\s*CONCERNING\s+PROBABILITY\."),
    ("III", "General Principles of the Calculus of Probabilities", r"CHAPTER\s+III\.\s*\n\s*THE\s+GENERAL\s+PRINCIPLES\s+OF\s+THE\s+CALCULUS\s+OF\s+PROBABILITIES\."),
    ("IV", "Concerning Hope", r"CHAPTER\s+IV\.\s*\n\s*CONCERNING\s+HOPE\."),
    ("V", "Analytical Methods of the Calculus of Probabilities", r"CHAPTER\s+V\.\s*\n\s*CONCERNING\s+THE\s+ANALYTICAL\s+METHODS\s+OF\s+THE\s+CALCULUS\s+OF\s+PROBABILITIES\."),
    ("VI", "Games of Chance", r"CHAPTER\s+VI\.\s*\n\s*GAMES\s+OF\s+CHANCE\."),
    ("VII", "Concerning the Unknown Inequalities which may Exist among Chances Supposed to be Equal", r"CHAPTER\s+VII\.\s*\n\s*CONCERNING\s+THE\s+UNKNOWN\s+INEQUALITIES"),
    ("VIII", "Concerning the Laws of Probability which result from the Indefinite Multiplication of Events", r"CHAPTER\s+VIII\.\s*\n\s*CONCERNING\s+THE\s+LAWS\s+OF\s+PROBABILITY"),
    ("IX", "Application of the Calculus of Probabilities to Natural Philosophy", r"CHAPTER\s+IX\.\s*\n\s*THE\s+APPLICATION\s+OF\s+THE\s+CALCULUS\s+OF\s+PROB-\s*ABILITIES\s+TO\s+NATURAL\s+PHILOSOPHY\."),
    ("X", "Application of the Calculus of Probabilities to the Moral Sciences", r"CHAPTER\s+X\.\s*\n\s*APPLICATION\s+OF\s+THE\s+CALCULUS\s+OF\s+PROB-\s*ABILITIES\s+TO\s+THE\s+MORAL\s+SCIENCES\."),
    ("XI", "Concerning the Probability of Testimonies", r"CHAPTER\s+XL\s*\n\s*CONCERNING\s+THE\s+PROBABILITIES\s+OF\s+TESTI-\s*MONIES\."),
    ("XII", "Concerning the Selections and Decisions of Assemblies", r"CHAPTER\s+XII\.\s*\n\s*CONCERNING\s+THE\s+SELECTIONS\s+AND\s+THE\s+DECISIONS\s+OF\s+ASSEMBLIES\."),
    ("XIII", "Concerning the Probability of the Judgments of Tribunals", r"CHAPTER\s+XIII\.\s*\n\s*CONCERNING\s+THE\s+PROBABILITY\s+OF\s+THE\s+JUDG-\s*MENTS\s+OF\s+TRIBUNALS\."),
    ("XIV", "Concerning Tables of Mortality, and the Mean Durations of Life, Marriage, and Some Associations", r"CHAPTER\s+XIV\.\s*\n\s*CONCERNING\s+TABLES\s+OF\s+MORTALITY"),
    ("XV", "Concerning the Benefits of Institutions which Depend upon the Probability of Events", r"CHAPTER\s+XV\.\s*\n\s*CONCERNING\s+THE\s+BENEFITS\s+OF\s+INSTITUTIONS"),
    ("XVI", "Concerning Illusions in the Estimation of Probabilities", r"CHAPTER\s+XVI\.\s*\n\s*CONCERNING\s+ILLUSIONS\s+IN\s+THE\s+ESTIMATION"),
    ("XVII", "Concerning the Various Means of Approaching Certainty", r"CHAPTER\s+XVII\.\s*\n\s*CONCERNING\s+THE\s+VARIOUS\s+MEANS\s+OF\s+APPROACHING\s+CERTAINTY\."),
    ("XVIII", "Historical Notice of the Calculus of Probabilities to 1816", r"CHAPTER\s+XVIII\.\s*\n\s*HISTORICAL\s+NOTICE\s+CONCERNING\s+THE\s+CAL-\s*CULUS\s+OF\s+PROBABILITIES\.")
]

positions = []
for num, title, pat in chapter_defs:
    m = re.search(pat, text[2700:])
    if m:
        start_idx = 2700 + m.start()
        end_idx = 2700 + m.end()
        positions.append((num, title, start_idx, end_idx))
    else:
        print(f"FAILED TO FIND: {num} - {title}")

print(f"Successfully matched {len(positions)} / 18 chapters!")

chapters = []
for i in range(len(positions)):
    num, title, start_idx, end_idx = positions[i]
    next_start = positions[i+1][2] if i + 1 < len(positions) else len(text)
    ch_text = text[end_idx:next_start].strip()
    
    # Clean running page headers
    ch_text = re.sub(r'\n\s*\d+\s+A\s+PHILOSOPHICAL\s+ESSAY\s+ON\s+PROBABILITIES\.\s*\n', '\n', ch_text)
    ch_text = re.sub(r'\n\s*A\s+PHILOSOPHICAL\s+ESSAY\s+ON\s+PROBABILITIES\.\s+\d+\s*\n', '\n', ch_text)
    ch_text = re.sub(r'(\b[a-zA-Z]+)-\s*\n\s*([a-zA-Z]+\b)', r'\1\2', ch_text)
    # Remove single line breaks within sentences, but preserve paragraph breaks
    paragraphs = [p.strip().replace('\n', ' ') for p in ch_text.split('\n\n') if p.strip()]
    clean_body = '\n\n'.join(paragraphs)
    
    chapters.append({
        "number": num,
        "title": title,
        "length": len(clean_body),
        "text": clean_body
    })
    print(f"Chapter {num}: {title} ({len(clean_body)} chars)")

with open('books/58881_laplace_probability/laplace_18_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("Saved all 18 chapters to laplace_18_chapters.json successfully!")
