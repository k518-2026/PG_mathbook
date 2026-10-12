import os
import json
import datetime
import hashlib

CATALOG_PATH = 'e:/GoogleAntigravity/PG_mathbook/catalog.json'
README_PATH = 'e:/GoogleAntigravity/PG_mathbook/README.md'

def load_catalog():
    if os.path.exists(CATALOG_PATH):
        with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"books": []}

def save_catalog(catalog):
    os.makedirs(os.path.dirname(CATALOG_PATH), exist_ok=True)
    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

def is_duplicate(gutenberg_id, catalog=None):
    if catalog is None:
        catalog = load_catalog()
    for book in catalog.get("books", []):
        if str(book.get("gutenberg_id")) == str(gutenberg_id):
            return True
    return False

def register_book(entry):
    catalog = load_catalog()
    # Check duplicate
    existing_idx = None
    for i, b in enumerate(catalog["books"]):
        if str(b.get("gutenberg_id")) == str(entry["gutenberg_id"]):
            existing_idx = i
            break
            
    if existing_idx is not None:
        print(f"[重複管理] Gutenberg ID {entry['gutenberg_id']} は既に登録されています。メタデータを更新します。")
        catalog["books"][existing_idx] = entry
    else:
        print(f"[重複管理] 新規書籍を登録します: Gutenberg ID {entry['gutenberg_id']}")
        catalog["books"].append(entry)
        
    save_catalog(catalog)
    update_readme(catalog)

def update_readme(catalog):
    md_content = """# PG_mathbook: プロジェクト・グーテンベルク古典数学入門シリーズ

Project Gutenberg のパブリックドメイン数学古典（Bookshelf 672 等）をもとに、ローカルLLM（google/gemma-3-4b）および現代的教育解説を加味して制作された、高校生向け数学入門書の蓄積リポジトリです。

原稿は LuaLaTeX（LuaHBTeX + LuaTeX-ja + TikZ）で高品質に組版され、美しい数式と視覚的な図版を豊富に含んでいます。

---

## 収録カタログ（重複管理システム）

書籍の追加・生成時は `catalog.json` を通じて重複が厳格に管理されています。

| ID | 原著名 | 入門書タイトル | 著者 | 章数 | 状態 | 原稿 (TeX) | 完成版 (PDF) | 登録日時 |
|---|---|---|---|---|---|---|---|---|
"""
    for b in catalog.get("books", []):
        b_id = b.get("gutenberg_id", "")
        orig = f"**{b.get('original_title', '')}**<br>({b.get('original_author', '')})"
        title = f"**{b.get('japanese_title', '')}**"
        author = f"**{b.get('author', '教育情報分析研究会')}**"
        chapters = b.get("chapters_count", "-")
        status = b.get("status", "完成")
        tex_link = f"[{os.path.basename(b.get('tex_file', ''))}]({b.get('tex_file', '')})" if b.get('tex_file') else "-"
        pdf_link = f"[{os.path.basename(b.get('pdf_file', ''))}]({b.get('pdf_file', '')})" if b.get('pdf_file') else "-"
        date = b.get("created_at", "")[:10]
        md_content += f"| {b_id} | {orig} | {title} | {author} | {chapters} | {status} | {tex_link} | {pdf_link} | {date} |\n"

    md_content += """
---

## リポジトリ構成
```
PG_mathbook/
├── catalog.json                 # 全書籍の重複管理・メタデータ台帳
├── README.md                    # 本目録
└── books/
    └── <ID>_<short_name>/
        ├── <book_name>.tex      # LuaLaTeX原稿ソース
        ├── <book_name>.pdf      # 製本済み高品質PDF
        └── meta.json            # 書籍個別メタデータ
```

## 組版環境
- Engine: **LuaLaTeX (LuaHBTeX / TeX Live 2026)**
- Japanese typesetting: `luatexja`, `ltjsbook`
- Figures: `tikz`, `pgfplots`
- Box & Layout: `tcolorbox`, `amsmath`, `amssymb`
- LLM Assistance:
  - `google/gemma-3-4b` (LM Studio @ `http://192.168.128.16:1234/`)
  - `gemma4:12b` (Ollama @ `http://192.168.128.62:11434/`)
"""
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("[重複管理] README.md のカタログ表を更新しました。")

if __name__ == '__main__':
    cat = load_catalog()
    print("Current catalog entries:", len(cat.get("books", [])))
