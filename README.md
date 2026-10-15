# 古典で学び直す数学（PG_mathbook）
### —— いまからでも遅くない、高校までの数学で理解する歴史的名著 ——

Project Gutenberg のパブリックドメイン数学・科学古典（Bookshelf 672 等）をもとに、**50代から80代の大人**（学生時代に数学で挫折してしまった方、大人になってから数学の深遠な美しさに興味をもった方）に向けて編纂・製本された数学学び直しライブラリです。

大学レベルの難解な専門記号を使うのではなく、**中学校・高校で習った数学（方程式、関数のグラフ、三角比、確率の基礎、微分積分の直観的イメージ）** を土台にして、歴史的巨星たちの思考と発見を**原著以上に懇切丁寧に解き明かします**。

原稿は LuaLaTeX（LuaHBTeX + LuaTeX-ja + TikZ）で高品質に組版され、美しい数式と視覚的な図版、用語辞典、総合演習問題を豊富に含んでいます。すべての作品は **50ページ以上の本格的学術・解説書** として製本されています。

---

## 収録カタログ（重複管理システム）

書籍の追加・生成時は `catalog.json` を通じて重複が厳格に管理されています。

| ID | 原著名 | 書籍タイトル | 著者 / 訳・解説 | 章数 | 状態 | 原稿 (TeX) | 完成版 (PDF) | 登録日時 |
|---|---|---|---|---|---|---|---|---|
| 58881 | [**A Philosophical Essay on Probabilities**](https://www.gutenberg.org/ebooks/58881)<br>(Pierre-Simon Laplace) | **確率の哲学的試論 —— 決定論的宇宙観と確率計算の全体系（原著全18章 完全翻訳・数学校閲版）** | **P・S・ラプラス** 著<br>**教育情報分析研究会** 訳・校閲 | 18 (107頁) | 完成 | [laplace_philosophical_essay_translation.tex](books/58881_laplace_probability/laplace_philosophical_essay_translation.tex) | [laplace_philosophical_essay_translation.pdf](books/58881_laplace_probability/laplace_philosophical_essay_translation.pdf) | 2026-10-14 |
| 58881-intro | [**A Philosophical Essay on Probabilities**](https://www.gutenberg.org/ebooks/58881)<br>(Pierre-Simon Laplace) | **古典で学び直すラプラス確率・統計入門 —— 歴史的名著『確率の哲学的試論』を高校までの数学で読み解く** | **教育情報分析研究会** | 12 (58頁) | 完成 | [laplace_probability_intro.tex](books/58881_laplace_probability/laplace_probability_intro.tex) | [laplace_probability_intro.pdf](books/58881_laplace_probability/laplace_probability_intro.pdf) | 2026-10-12 |
| 57359 | [**The Logic of Chance, 3rd edition**](https://www.gutenberg.org/ebooks/57359)<br>(John Venn) | **偶然の論理 —— 客観的頻度論と確率の論理的・物理的基礎（原著全19章 完全翻訳・数学校閲版）** | **ジョン・ヴェン** 著<br>**教育情報分析研究会** 訳・校閲 | 19 (246頁) | 完成 | [venn_logic_of_chance_translation.tex](books/57359_venn_logic_of_chance/venn_logic_of_chance_translation.tex) | [venn_logic_of_chance_translation.pdf](books/57359_venn_logic_of_chance/venn_logic_of_chance_translation.pdf) | 2026-10-15 |
| 57359-intro | [**The Logic of Chance, 3rd edition**](https://www.gutenberg.org/ebooks/57359)<br>(John Venn) | **古典で学び直すヴェン確率論入門 —— 『偶然の論理』と実社会具体例でひもとく客観的データと統計の科学** | **教育情報分析研究会** | 12 (70頁) | 完成 | [venn_logic_of_chance_intro.tex](books/57359_venn_logic_of_chance/venn_logic_of_chance_intro.tex) | [venn_logic_of_chance_intro.pdf](books/57359_venn_logic_of_chance/venn_logic_of_chance_intro.pdf) | 2026-10-14 |
| 15114 | [**An Investigation of the Laws of Thought**](https://www.gutenberg.org/ebooks/15114)<br>(George Boole) | **古典で学び直すブール代数と論理入門 —— 『思考の法則』で学ぶ記号論理・確率・コンピュータの原点** | **教育情報分析研究会** | 12 (67頁) | 完成 | [boole_laws_of_thought_intro.tex](books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.tex) | [boole_laws_of_thought_intro.pdf](books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.pdf) | 2026-10-12 |
| 4763 | [**The Game of Logic**](https://www.gutenberg.org/ebooks/4763)<br>(Lewis Carroll) | **古典で学び直すルイス・キャロル論理学入門 —— 『論理の遊戯』とダイアグラムで楽しむ三段論法と確率の数理** | **教育情報分析研究会** | 12 (58頁) | 完成 | [carroll_game_of_logic_intro.tex](books/4763_carroll_game_of_logic/carroll_game_of_logic_intro.tex) | [carroll_game_of_logic_intro.pdf](books/4763_carroll_game_of_logic/carroll_game_of_logic_intro.pdf) | 2026-10-13 |
| 33283 | [**Calculus Made Easy**](https://www.gutenberg.org/ebooks/33283)<br>(Silvanus P. Thompson) | **古典で学び直す微積分入門 —— 『Calculus Made Easy』で直観的にわかる微分・積分・極限から曲線の数理まで** | **教育情報分析研究会** | 12 (71頁) | 完成 | [thompson_calculus_intro.tex](books/33283_thompson_calculus/thompson_calculus_intro.tex) | [thompson_calculus_intro.pdf](books/33283_thompson_calculus/thompson_calculus_intro.pdf) | 2026-10-13 |
| 37157 | [**Science and Hypothesis**](https://www.gutenberg.org/ebooks/37157)<br>(Henri Poincaré) | **古典で学び直す科学と仮説 —— 数学・幾何学・物理学の基礎をめぐる省察（原著全13章 日本語訳・数学校閲・大人のための丁寧な解説付）** | **アンリ・ポアンカレ** 著<br>**教育情報分析研究会** 訳・校閲・解説 | 13 (159頁) | 完成 | [poincare_science_and_hypothesis_intro.tex](books/37157_poincare_science_and_hypothesis/poincare_science_and_hypothesis_intro.tex) | [poincare_science_and_hypothesis_intro.pdf](books/37157_poincare_science_and_hypothesis/poincare_science_and_hypothesis_intro.pdf) | 2026-10-14 |

---

## リポジトリ構成
```
PG_mathbook/
├── catalog.json                 # 全書籍の重複管理・メタデータ台帳
├── README.md                    # 本目録（原著リンク完備）
├── index.html                   # レスポンシブWebダッシュボード（大人の学び直し統合デザイン）
├── docs/                        # GitHub Pages 公開用静的サイト
└── books/
    └── <ID>_<short_name>/
        ├── <book_name>.tex      # LuaLaTeX原稿ソース
        ├── <book_name>.pdf      # 製本済み高品質PDF（50頁以上）
        └── meta.json            # 書籍個別メタデータ
```

## 組版環境 & 制作システム
- Engine: **LuaLaTeX (LuaHBTeX / TeX Live 2026)**
- Japanese typesetting: `luatexja`, `ltjsbook`
- Figures: `tikz`, `pgfplots`
- Box & Layout: `tcolorbox`, `amsmath`, `amssymb`
- 制作パイプライン (LLM Assistance):
  - **Step 1 (原著直訳)**: `qwen2.5-7b-instruct` (LM Studio @ `http://192.168.128.16:1234/`)
  - **Step 2 (数学校閲)**: `qwen2.5-math-7b-instruct` (LM Studio @ `http://192.168.128.16:1234/`)
  - **Step 3 (大人のための解説講義)**: `gemma4:12b` (Ollama @ `http://192.168.128.62:11434/`)
