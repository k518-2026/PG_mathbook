import json

cat_path = r"E:\GoogleAntigravity\PG_mathbook\catalog.json"
with open(cat_path, "r", encoding="utf-8") as f:
    cat = json.load(f)

# Entries for Sir Isaac Newton - Principia (#28233)
book_trans = {
    "gutenberg_id": 28233,
    "original_title": "The Mathematical Principles of Natural Philosophy (Principia)",
    "original_author": "Sir Isaac Newton",
    "japanese_title": "自然哲学の数学的諸原理（プリンキピア）全訳・精選決定版",
    "author": "アイザック・ニュートン / プロジェクトチーム",
    "category": "物理数学・古典力学・天体力学",
    "description": "天上の惑星運動と地上の物体の落下を同一の力学法則で統合した近代科学の金字塔。質量・慣性力・絶対時空の定義、運動の3法則、初等および最終比の幾何学的極限法、中心力場におけるケプラー第2法則（面積速度一定）の幾何学的証明、万有引力逆2乗則、世界の体系を原著幾何図版とともに完全収録。",
    "chapters_count": 5,
    "pages": 11,
    "tex_file": "books/28233_newton_principia/newton_principia_translation.tex",
    "pdf_file": "books/28233_newton_principia/newton_principia_translation.pdf",
    "book_dir": "books/28233_newton_principia",
    "compiler": "lualatex",
    "model_used": "hybrid-expert",
    "gutenberg_url": "https://www.gutenberg.org/ebooks/28233",
    "language": "ja",
    "created_at": "2026-11-04",
    "status": "completed"
}

book_intro = {
    "gutenberg_id": "28233-intro",
    "original_title": "The Mathematical Principles of Natural Philosophy (Introductory Reader & TikZ Atlas)",
    "original_author": "Sir Isaac Newton",
    "japanese_title": "大人のためのプリンキピア入門 —— 幾何学で読み解く万有引力と微積分の原点（TikZ図解版）",
    "author": "アイザック・ニュートン / プロジェクトチーム",
    "category": "物理幾何学・科学思想入門",
    "description": "ニュートンはなぜ微分方程式を使わずに幾何学で宇宙を解き明かしたのか？運動の3法則、初等および最終比（極限法）、そして中心力と慣性運動の合成によって面積速度一定（ケプラー第2法則）が幾何学的に導かれる感動のプロセスを、鮮やかなTikZベクター図解で完全講義。",
    "chapters_count": 5,
    "pages": 8,
    "tex_file": "books/28233_newton_principia/newton_principia_intro.tex",
    "pdf_file": "books/28233_newton_principia/newton_principia_intro.pdf",
    "book_dir": "books/28233_newton_principia",
    "compiler": "lualatex",
    "model_used": "hybrid-expert",
    "gutenberg_url": "https://www.gutenberg.org/ebooks/28233",
    "language": "ja",
    "created_at": "2026-11-04",
    "status": "completed"
}

# Check if already in catalog
existing_keys = [(str(b.get("gutenberg_id")), b.get("pdf_file")) for b in cat["books"]]
if (str(book_trans["gutenberg_id"]), book_trans["pdf_file"]) not in existing_keys:
    cat["books"].append(book_trans)
if (str(book_intro["gutenberg_id"]), book_intro["pdf_file"]) not in existing_keys:
    cat["books"].append(book_intro)

with open(cat_path, "w", encoding="utf-8") as f:
    json.dump(cat, f, ensure_ascii=False, indent=2)

print(f"catalog.json updated. Total books: {len(cat['books'])}")
