# -*- coding: utf-8 -*-
import os
import re

# 1. 58881 Laplace
laplace_path = 'books/58881_laplace_probability/laplace_probability_intro.tex'
with open(laplace_path, 'r', encoding='utf-8') as f:
    c = f.read()

old_laplace_title = r'''\title{\Huge\textbf{高校生のためのラプラス確率・統計入門}\\[6mm]
\Large\textbf{決定論的宇宙観・10の原理から最小二乗法・道徳科学まで}\\[4mm]
\large 原著：ピエール＝シモン・ラプラス『確率の哲学的試論』\\[2mm]
\normalsize (Project Gutenberg eBook \#58881: \textit{A Philosophical Essay on Probabilities})}'''

new_laplace_title = r'''\title{\Huge\textbf{古典で学び直すラプラス確率・統計入門}\\[5mm]
\huge\textbf{いまからでも遅くない、高校までの数学で理解する歴史的名著}\\[6mm]
\Large\textbf{決定論的宇宙観・10の原理から最小二乗法・道徳科学まで}\\[4mm]
\large 原著：ピエール＝シモン・ラプラス『確率の哲学的試論』\\[2mm]
\normalsize Project Gutenberg eBook \#58881: \textit{A Philosophical Essay on Probabilities}}'''

c = c.replace(old_laplace_title, new_laplace_title)
c = c.replace('高校生のための重要例題：', '大人の学び直しのための重要例題：')
c = c.replace(r'\chapter{高校生のための総合演習問題と詳細解答}', r'\chapter{読者のための総合演習問題と詳細解答}')
c = c.replace(r'\addcontentsline{toc}{chapter}{高校生のための総合演習問題と詳細解答}', r'\addcontentsline{toc}{chapter}{読者のための総合演習問題と詳細解答}')

with open(laplace_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated laplace_probability_intro.tex')


# 2. 15114 Boole
boole_path = 'books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.tex'
with open(boole_path, 'r', encoding='utf-8') as f:
    c = f.read()

old_boole_title = r'''\title{\Huge\textbf{高校生のためのブール代数と確率論入門}\\[6mm]
\Large\textbf{思考の法則から記号論理・確率の代数化・コンピュータ回路まで}\\[4mm]
\large 原著：ジョージ・ブール『思考の法則』\\[2mm]
\normalsize (Project Gutenberg eBook \#15114: \textit{An Investigation of the Laws of Thought})}'''

new_boole_title = r'''\title{\Huge\textbf{古典で学び直すブール代数と論理入門}\\[5mm]
\huge\textbf{いまからでも遅くない、高校までの数学で理解する歴史的名著}\\[6mm]
\Large\textbf{思考の法則から記号論理・確率の代数化・コンピュータ回路まで}\\[4mm]
\large 原著：ジョージ・ブール『思考の法則』\\[2mm]
\normalsize Project Gutenberg eBook \#15114: \textit{An Investigation of the Laws of Thought}}'''

c = c.replace(old_boole_title, new_boole_title)
c = c.replace('高校生のための重要例題：', '大人の学び直しのための重要例題：')
c = c.replace(r'\chapter{高校生のための総合演習問題と詳細解答}', r'\chapter{読者のための総合演習問題と詳細解答}')
c = c.replace(r'\addcontentsline{toc}{chapter}{高校生のための総合演習問題と詳細解答}', r'\addcontentsline{toc}{chapter}{読者のための総合演習問題と詳細解答}')

with open(boole_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated boole_laws_of_thought_intro.tex')


# 3. 4763 Carroll
carroll_path = 'books/4763_carroll_game_of_logic/carroll_game_of_logic_intro.tex'
with open(carroll_path, 'r', encoding='utf-8') as f:
    c = f.read()

old_carroll_title = r'''\title{\Huge\textbf{高校生のためのルイス・キャロル論理学入門}\\[6mm]
\Large\textbf{『論理の遊戯』とダイアグラムで楽しむ記号論理・三段論法・確率の数理}\\[4mm]
\large 原著：ルイス・キャロル（チャールズ・ドジソン）『論理の遊戯』\\[2mm]
\normalsize (Project Gutenberg eBook \#4763: \textit{The Game of Logic})}'''

new_carroll_title = r'''\title{\Huge\textbf{古典で学び直すルイス・キャロル論理学入門}\\[5mm]
\huge\textbf{いまからでも遅くない、高校までの数学で理解する歴史的名著}\\[6mm]
\Large\textbf{『論理の遊戯』とダイアグラムで楽しむ記号論理・三段論法・確率の数理}\\[4mm]
\large 原著：ルイス・キャロル（チャールズ・ドジソン）『論理の遊戯』\\[2mm]
\normalsize Project Gutenberg eBook \#4763: \textit{The Game of Logic}}'''

c = c.replace(old_carroll_title, new_carroll_title)
c = c.replace('pdftitle={高校生のためのルイス・キャロル論理学入門}', 'pdftitle={古典で学び直すルイス・キャロル論理学入門}')
c = c.replace(r'\chapter{高校生のための総合演習問題と詳細解答}', r'\chapter{読者のための総合演習問題と詳細解答}')
c = c.replace(r'\addcontentsline{toc}{chapter}{高校生のための総合演習問題と詳細解答}', r'\addcontentsline{toc}{chapter}{読者のための総合演習問題と詳細解答}')

with open(carroll_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated carroll_game_of_logic_intro.tex')


# 4. 33283 Thompson
thompson_path = 'books/33283_thompson_calculus/thompson_calculus_intro.tex'
with open(thompson_path, 'r', encoding='utf-8') as f:
    c = f.read()

old_thompson_title = r'''{\huge\bfseries 高校生のための微積分入門}\\[0.4cm]
{\Large\bfseries —— 『Calculus Made Easy』で直観的にわかる\\微分・積分・極限から物理・曲線の数理まで ——}'''

new_thompson_title = r'''{\Huge\bfseries 古典で学び直す微積分入門}\\[0.4cm]
{\Large\bfseries —— 『Calculus Made Easy』で直観的にわかる\\微分・積分・極限から曲線の数理まで ——}\\[0.4cm]
{\large\bfseries いまからでも遅くない、高校までの数学で理解する歴史的名著}'''

c = c.replace(old_thompson_title, new_thompson_title)
c = c.replace('pdftitle={高校生のための微積分入門 —— 『Calculus Made Easy』で直観的にわかる微分・積分・極限から物理・曲線の数理まで}',
              'pdftitle={古典で学び直す微積分入門 —— 『Calculus Made Easy』で直観的にわかる微分・積分・極限から曲線の数理まで}')
c = c.replace('高校生のための重要例題：', '大人の学び直しのための重要例題：')
c = c.replace(r'\chapter*{付録：高校生のための微積分重要用語辞典}', r'\chapter*{付録：微積分重要用語辞典}')
c = c.replace(r'\addcontentsline{toc}{chapter}{付録：高校生のための微積分重要用語辞典}', r'\addcontentsline{toc}{chapter}{付録：微積分重要用語辞典}')

with open(thompson_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated thompson_calculus_intro.tex')


# 5. 37157 Poincare
poincare_path = 'books/37157_poincare_science_and_hypothesis/poincare_science_and_hypothesis_intro.tex'
with open(poincare_path, 'r', encoding='utf-8') as f:
    c = f.read()

old_poincare_sub = r'''\Large\textbf{—— 原著全13章 日本語訳・数学校閲・高校生向け解説付 ——}'''
new_poincare_sub = r'''\Large\textbf{—— 原著全13章 日本語訳・数学校閲・大人のための丁寧な解説付 ——}'''
c = c.replace(old_poincare_sub, new_poincare_sub)

old_poincare_pre = r'''\title{\Huge\textbf{科学と仮説}\\[4mm]
\huge\textbf{数学・幾何学・物理学の基礎をめぐる省察}\\[6mm]'''
new_poincare_pre = r'''\title{\Huge\textbf{古典で学び直す科学と仮説}\\[4mm]
\huge\textbf{数学・幾何学・物理学の基礎をめぐる省察}\\[6mm]'''
c = c.replace(old_poincare_pre, new_poincare_pre)

c = c.replace('title={高校生のための徹底解説講義}', 'title={大人のための徹底解説講義}')
c = c.replace(r'\section{高校生のための解説講義}', r'\section{大人のための解説講義}')

with open(poincare_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated poincare_science_and_hypothesis_intro.tex')


# 6. meta.json updates
meta_updates = [
    ('books/58881_laplace_probability/meta.json', '古典で学び直すラプラス確率・統計入門 —— 歴史的名著『確率の哲学的試論』を高校までの数学で読み解く'),
    ('books/15114_boole_laws_of_thought/meta.json', '古典で学び直すブール代数と論理入門 —— 『思考の法則』で学ぶ記号論理・確率・コンピュータの原点'),
    ('books/4763_carroll_game_of_logic/meta.json', '古典で学び直すルイス・キャロル論理学入門 —— 『論理の遊戯』とダイアグラムで楽しむ三段論法と確率の数理'),
    ('books/33283_thompson_calculus/meta.json', '古典で学び直す微積分入門 —— 『Calculus Made Easy』で直観的にわかる微分・積分・極限から曲線の数理まで'),
    ('books/57359_venn_logic_of_chance/meta.json', '古典で学び直すヴェン確率論入門 —— 『偶然の論理』と実社会具体例でひもとく客観的データと統計の科学')
]

import json
for mpath, jtitle in meta_updates:
    if os.path.exists(mpath):
        with open(mpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        d['japanese_title'] = jtitle
        with open(mpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f'Updated {mpath}')

print('All replacements completed successfully!')
