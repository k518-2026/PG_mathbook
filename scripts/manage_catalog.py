# -*- coding: utf-8 -*-
import os
import json

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(PROJECT_ROOT, "catalog.json")
README_PATH = os.path.join(PROJECT_ROOT, "README.md")


def load_catalog():
    if os.path.exists(CATALOG_PATH):
        with open(CATALOG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"books": []}


def save_catalog(catalog):
    os.makedirs(os.path.dirname(CATALOG_PATH), exist_ok=True)
    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
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
    md_content = """# 古典で学び直す数学（PG_mathbook）
### —— いまからでも遅くない、高校までの数学で理解する歴史的名著 ——

Project Gutenberg のパブリックドメイン数学・科学古典（Bookshelf 672 等）をもとに、**50代から80代の大人**（学生時代に数学で挫折してしまった方、大人になってから数学の深遠な美しさに興味をもった方）に向けて編纂・製本された数学学び直しライブラリです。

大学レベルの難解な専門記号を使うのではなく、**中学校・高校で習った数学（方程式、関数のグラフ、三角比、確率の基礎、微分積分の直観的イメージ）** を土台にして、歴史的巨星たちの思考と発見を**原著以上に懇切丁寧に解き明かします**。

原稿は LuaLaTeX（LuaHBTeX + LuaTeX-ja + TikZ）で高品質に組版され、美しい数式と視覚的な図版、用語辞典、総合演習問題を豊富に含んでいます。すべての作品は **50ページ以上の本格的学術・解説書** として製本されています。

---

## 収録カタログ（重複管理システム）

書籍の追加・生成時は `catalog.json` を通じて重複が厳格に管理されています。

| ID | 原著名 | 書籍タイトル | 著者 / 訳・解説 | 章数 | 状態 | 原稿 (TeX) | 完成版 (PDF) | 登録日時 |
|---|---|---|---|---|---|---|---|---|
"""
    for b in catalog.get("books", []):
        b_id = b.get("gutenberg_id", "")
        base_id = str(b_id).replace("-intro", "")
        g_url = b.get("gutenberg_url", f"https://www.gutenberg.org/ebooks/{base_id}")
        orig = f"[**{b.get('original_title', '')}**]({g_url})<br>({b.get('original_author', '')})"
        title = f"**{b.get('japanese_title', '')}**"
        author = f"**{b.get('author', '教育情報分析研究会')}**"
        chapters = f"{b.get('chapters_count', '-')} ({b.get('pages', '-')}頁)"
        status = b.get("status", "完成")
        tex_link = f"[{os.path.basename(b.get('tex_file', ''))}]({b.get('tex_file', '')})" if b.get("tex_file") else "-"
        pdf_link = f"[{os.path.basename(b.get('pdf_file', ''))}]({b.get('pdf_file', '')})" if b.get("pdf_file") else "-"
        date = str(b.get("created_at", ""))[:10]
        md_content += f"| {b_id} | {orig} | {title} | {author} | {chapters} | {status} | {tex_link} | {pdf_link} | {date} |\n"

    md_content += """
---

## リポジトリ構成
```
PG_mathbook/
├── catalog.json                 # 全書籍の重複管理・メタデータ台帳
├── book_queue.json              # 自動翻訳・入門書生成キュー
├── README.md                    # 本目録（原著リンク完備）
├── index.html                   # レスポンシブWebダッシュボード（大人の学び直し統合デザイン）
├── docs/                        # GitHub Pages 公開用静的サイト
└── books/
    └── <ID>_<short_name>/
        ├── <book_name>.tex      # LuaLaTeX原稿ソース
        ├── <book_name>.pdf      # 製本済み高品質PDF
        └── meta.json            # 書籍個別メタデータ
```

## 組版環境 & 自動制作システム
- Engine: **LuaLaTeX (LuaHBTeX / TeX Live 2026)**
- Japanese typesetting: `luatexja`, `ltjsbook`
- Figures: `tikz`, `pgfplots`
- Box & Layout: `tcolorbox`, `amsmath`, `amssymb`
- 制作パイプライン (LM Studio @ `http://192.168.128.16:1234/`):
  - **Step 1 (原著直訳)**: `qwen2.5-7b-instruct`
  - **Step 2 (数学校閲)**: `qwen2.5-math-7b-instruct`
  - **Step 3 (大人のための学び直し解説講義)**: `qwen2.5-7b-instruct`
"""
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(md_content)
    print("[重複管理] README.md のカタログ表を更新しました。")


if __name__ == "__main__":
    cat = load_catalog()
    print("Current catalog entries:", len(cat.get("books", [])))
