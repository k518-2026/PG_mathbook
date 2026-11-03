import json

cat_path = r"E:\GoogleAntigravity\PG_mathbook\catalog.json"
with open(cat_path, "r", encoding="utf-8") as f:
    cat = json.load(f)

# Entries for D'Arcy Wentworth Thompson - On Growth and Form (#55264)
book_trans = {
    "gutenberg_id": 55264,
    "original_title": "On Growth and Form (Selected & Complete Edition)",
    "original_author": "D'Arcy Wentworth Thompson",
    "japanese_title": "成長と形態について（全訳・精選図解決定版）",
    "author": "ダーシー・ウェントワース・トムソン / プロジェクトチーム",
    "category": "数理生物学・物理幾何学・形態学",
    "description": "生命の形態を自然淘汰のみならず物理的・力学的力（重力、表面張力、粘性）と幾何学（2乗3乗則、対数螺旋、極小曲面、デカルト座標の変形理論）から解明した不滅の古典名著。原著図版完全収録。",
    "chapters_count": 4,
    "pages": 13,
    "tex_file": "books/55264_thompson_on_growth_and_form/thompson_growth_form_translation.tex",
    "pdf_file": "books/55264_thompson_on_growth_and_form/thompson_growth_form_translation.pdf",
    "book_dir": "books/55264_thompson_on_growth_and_form",
    "compiler": "lualatex",
    "model_used": "hybrid-expert",
    "gutenberg_url": "https://www.gutenberg.org/ebooks/55264",
    "language": "ja",
    "created_at": "2026-11-03",
    "status": "completed"
}

book_intro = {
    "gutenberg_id": 55264,
    "original_title": "On Growth and Form (Introductory Reader & TikZ Atlas)",
    "original_author": "D'Arcy Wentworth Thompson",
    "japanese_title": "大人のための『成長と形態について』―― 幾何学と物理法則が紡ぐ生命のかたち（TikZ図解版）",
    "author": "ダーシー・ウェントワース・トムソン / プロジェクトチーム",
    "category": "数理生物学・幾何学図解",
    "description": "ガリレオの2乗3乗則と重力・表面張力のスケール競合、オウムガイの対数螺旋（等角螺旋）のグノモン的相似成長、デカルト座標の剪断・歪曲写像による魚類骨格の進化変形理論をTikZベクトル図解で直観的に解説。",
    "chapters_count": 5,
    "pages": 10,
    "tex_file": "books/55264_thompson_on_growth_and_form/thompson_growth_form_intro.tex",
    "pdf_file": "books/55264_thompson_on_growth_and_form/thompson_growth_form_intro.pdf",
    "book_dir": "books/55264_thompson_on_growth_and_form",
    "compiler": "lualatex",
    "model_used": "hybrid-expert",
    "gutenberg_url": "https://www.gutenberg.org/ebooks/55264",
    "language": "ja",
    "created_at": "2026-11-03",
    "status": "completed"
}

# Check if already added
existing_ids = [(b.get("gutenberg_id"), b.get("pdf_file")) for b in cat["books"]]
if (55264, book_trans["pdf_file"]) not in existing_ids:
    cat["books"].append(book_trans)
if (55264, book_intro["pdf_file"]) not in existing_ids:
    cat["books"].append(book_intro)

with open(cat_path, "w", encoding="utf-8") as f:
    json.dump(cat, f, ensure_ascii=False, indent=2)

print(f"Catalog successfully updated. Total registered books: {len(cat['books'])}")
