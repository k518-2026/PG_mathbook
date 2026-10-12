# PG_mathbook: プロジェクト・グーテンベルク古典数学入門シリーズ

Project Gutenberg のパブリックドメイン数学古典（Bookshelf 672 等）をもとに、ローカルLLM（google/gemma-3-4b）および現代的教育解説を加味して制作された、高校生向け数学入門書の蓄積リポジトリです。

原稿は LuaLaTeX（LuaHBTeX + LuaTeX-ja + TikZ）で高品質に組版され、美しい数式と視覚的な図版を豊富に含んでいます。

---

## 収録カタログ（重複管理システム）

書籍の追加・生成時は `catalog.json` を通じて重複が厳格に管理されています。

| ID | 原著名 | 入門書タイトル | 著者 | 章数 | 状態 | 原稿 (TeX) | 完成版 (PDF) | 登録日時 |
|---|---|---|---|---|---|---|---|---|
| 58881 | [**A Philosophical Essay on Probabilities**](https://www.gutenberg.org/ebooks/58881)<br>(Pierre-Simon Laplace) | **高校生のためのラプラス確率・統計入門 —— 歴史的名著『確率の哲学的試論』で解き明かす数学の神髄** | **教育情報分析研究会** | 6 | 完成 | [laplace_probability_intro.tex](books/58881_laplace_probability/laplace_probability_intro.tex) | [laplace_probability_intro.pdf](books/58881_laplace_probability/laplace_probability_intro.pdf) | 2026-10-12 |
| 57359 | [**The Logic of Chance, 3rd edition**](https://www.gutenberg.org/ebooks/57359)<br>(John Venn) | **高校生のためのヴェン確率論入門 —— 『偶然の論理』とヴェン図でひもとく客観的データと統計の科学** | **教育情報分析研究会** | 6 | 完成 | [venn_logic_of_chance_intro.tex](books/57359_venn_logic_of_chance/venn_logic_of_chance_intro.tex) | [venn_logic_of_chance_intro.pdf](books/57359_venn_logic_of_chance/venn_logic_of_chance_intro.pdf) | 2026-10-12 |
| 15114 | [**An Investigation of the Laws of Thought**](https://www.gutenberg.org/ebooks/15114)<br>(George Boole) | **高校生のためのブール代数と確率論入門 —— 『思考の法則』で学ぶ論理・確率・コンピュータの数学** | **教育情報分析研究会** | 8 | 完成 | [boole_laws_of_thought_intro.tex](books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.tex) | [boole_laws_of_thought_intro.pdf](books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.pdf) | 2026-10-12 |

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
