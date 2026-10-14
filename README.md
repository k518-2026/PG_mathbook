# PG_mathbook: プロジェクト・グーテンベルク古典数学入門シリーズ

Project Gutenberg のパブリックドメイン数学古典（Bookshelf 672 等）をもとに、ローカルLLM（google/gemma-3-4b / gemma4:12b）および現代的教育解説を加味して制作された、高校生向け数学入門書の蓄積リポジトリです。

原稿は LuaLaTeX（LuaHBTeX + LuaTeX-ja + TikZ）で高品質に組版され、美しい数式と視覚的な図版、用語辞典、総合演習問題を豊富に含んでいます。すべての作品は **50ページ以上の本格的入門書** として製本されています。

---

## 収録カタログ（重複管理システム）

書籍の追加・生成時は `catalog.json` を通じて重複が厳格に管理されています。

| ID | 原著名 | 書籍タイトル | 著者 / 訳者 | 章数 | 状態 | 原稿 (TeX) | 完成版 (PDF) | 登録日時 |
|---|---|---|---|---|---|---|---|---|
| 58881 | [**A Philosophical Essay on Probabilities**](https://www.gutenberg.org/ebooks/58881)<br>(Pierre-Simon Laplace) | **確率の哲学的試論 —— 決定論的宇宙観と確率計算の全体系（原著全18章 完全翻訳・数学校閲版）** | **P・S・ラプラス** 著<br>**教育情報分析研究会** 訳・校閲 | 18 (108頁) | 完成 | [laplace_philosophical_essay_translation.tex](books/58881_laplace_probability/laplace_philosophical_essay_translation.tex) | [laplace_philosophical_essay_translation.pdf](books/58881_laplace_probability/laplace_philosophical_essay_translation.pdf) | 2026-10-14 |
| 58881-intro | [**A Philosophical Essay on Probabilities**](https://www.gutenberg.org/ebooks/58881)<br>(Pierre-Simon Laplace) | **高校生のためのラプラス確率・統計入門 —— 決定論的宇宙観・10の原理から最小二乗法・道徳科学まで** | **教育情報分析研究会** | 12 (58頁) | 完成 | [laplace_probability_intro.tex](books/58881_laplace_probability/laplace_probability_intro.tex) | [laplace_probability_intro.pdf](books/58881_laplace_probability/laplace_probability_intro.pdf) | 2026-10-12 |
| 57359 | [**The Logic of Chance, 3rd edition**](https://www.gutenberg.org/ebooks/57359)<br>(John Venn) | **高校生のためのヴェン確率論入門 —— 客観的頻度論・確率系列からランダム性の数理・平均論まで** | **教育情報分析研究会** | 12 (62頁) | 完成 | [venn_logic_of_chance_intro.tex](books/57359_venn_logic_of_chance/venn_logic_of_chance_intro.tex) | [venn_logic_of_chance_intro.pdf](books/57359_venn_logic_of_chance/venn_logic_of_chance_intro.pdf) | 2026-10-12 |
| 15114 | [**An Investigation of the Laws of Thought**](https://www.gutenberg.org/ebooks/15114)<br>(George Boole) | **高校生のためのブール代数と確率論入門 —— 思考の法則から記号論理・確率の代数化・コンピュータ回路まで** | **教育情報分析研究会** | 12 (67頁) | 完成 | [boole_laws_of_thought_intro.tex](books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.tex) | [boole_laws_of_thought_intro.pdf](books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.pdf) | 2026-10-12 |
| 4763 | [**The Game of Logic**](https://www.gutenberg.org/ebooks/4763)<br>(Lewis Carroll) | **高校生のためのルイス・キャロル論理学入門 —— 『論理の遊戯』とダイアグラムで楽しむ記号論理・三段論法・確率の数理** | **教育情報分析研究会** | 12 (58頁) | 完成 | [carroll_game_of_logic_intro.tex](books/4763_carroll_game_of_logic/carroll_game_of_logic_intro.tex) | [carroll_game_of_logic_intro.pdf](books/4763_carroll_game_of_logic/carroll_game_of_logic_intro.pdf) | 2026-10-13 |
| 33283 | [**Calculus Made Easy**](https://www.gutenberg.org/ebooks/33283)<br>(Silvanus P. Thompson) | **高校生のための微積分入門 —— 『Calculus Made Easy』で直観的にわかる微分・積分・極限から物理・曲線の数理まで** | **教育情報分析研究会** | 12 (71頁) | 完成 | [thompson_calculus_intro.tex](books/33283_thompson_calculus/thompson_calculus_intro.tex) | [thompson_calculus_intro.pdf](books/33283_thompson_calculus/thompson_calculus_intro.pdf) | 2026-10-13 |
| 37157 | [**Science and Hypothesis**](https://www.gutenberg.org/ebooks/37157)<br>(Henri Poincaré) | **科学と仮説 —— 数学・幾何学・物理学の基礎をめぐる省察（原著全13章 日本語訳・数学校閲・高校生向け解説付）** | **アンリ・ポアンカレ** 著<br>**教育情報分析研究会** 訳・校閲・解説 | 13 (159頁) | 完成 | [poincare_science_and_hypothesis_intro.tex](books/37157_poincare_science_and_hypothesis/poincare_science_and_hypothesis_intro.tex) | [poincare_science_and_hypothesis_intro.pdf](books/37157_poincare_science_and_hypothesis/poincare_science_and_hypothesis_intro.pdf) | 2026-10-14 |

---

## リポジトリ構成
```
PG_mathbook/
├── catalog.json                 # 全書籍の重複管理・メタデータ台帳
├── README.md                    # 本目録（原著リンク完備）
├── index.html                   # レスポンシブWebダッシュボード
├── docs/                        # GitHub Pages 公開用静的サイト
└── books/
    └── <ID>_<short_name>/
        ├── <book_name>.tex      # LuaLaTeX原稿ソース
        ├── <book_name>.pdf      # 製本済み高品質PDF（50頁以上）
        └── meta.json            # 書籍個別メタデータ
```

## 組版環境
- Engine: **LuaLaTeX (LuaHBTeX / TeX Live 2026)**
- Japanese typesetting: `luatexja`, `ltjsbook`
- Figures: `tikz`, `pgfplots`
- Box & Layout: `tcolorbox`, `amsmath`, `amssymb`
- LLM Assistance:
  - `gemma4:12b` (Ollama @ `http://192.168.128.62:11434/`)
  - `google/gemma-3-4b` (LM Studio @ `http://192.168.128.16:1234/`)
