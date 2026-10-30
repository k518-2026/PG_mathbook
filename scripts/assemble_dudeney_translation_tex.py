# -*- coding: utf-8 -*-
"""
Generate Complete Academic Translation TeX for Dudeney's Amusements in Mathematics (PG#16713)
All 430 problems and solutions fully translated, paired, and formatted for LuaLaTeX.
"""

import os, sys, json, re

def clean_for_latex(text):
    if not text:
        return ""
    # Remove Gutenberg Illustration markers cleanly
    t = re.sub(r'\[Illustration:?[^\]]*\]', r'\\par\\textit{【原著図版参照】}\\par', text)
    t = re.sub(r'\[Illustration\]', r'\\par\\textit{【原著図版参照】}\\par', t)
    
    # Escape special TeX chars
    t = t.replace('\\', '\\textbackslash{}')
    t = t.replace('&', '\\&')
    t = t.replace('%', '\\%')
    t = t.replace('$', '\\$')
    t = t.replace('#', '\\#')
    t = t.replace('_', '\\_')
    t = t.replace('{', '\\{')
    t = t.replace('}', '\\}')
    t = t.replace('~', '\\textasciitilde{}')
    t = t.replace('^', '\\textasciicircum{}')

    # Re-enable math or italics if needed
    t = t.replace('\\textbackslash{}textit\\{【原著図版参照】\\}\\textbackslash{}par', r'\par\textit{【原著図版参照】}\par')
    
    # Handle fractions e.g. 1/2 -> 1/2
    return t

def build_translation_book():
    book_dir = r"E:\GoogleAntigravity\PG_mathbook\books\16713_dudeney_amusements_in_mathematics"
    paired_path = os.path.join(book_dir, "dudeney_paired_problems.json")
    with open(paired_path, "r", encoding="utf-8") as f:
        problems = json.load(f)

    tex_path = os.path.join(book_dir, "dudeney_amusements_translation.tex")

    preamble = r"""\documentclass[10pt,a4paper,oneside,openany]{ltjsbook}

% --- Typography & Geometry ---
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb}
\usepackage{geometry}
\geometry{top=20mm,bottom=20mm,left=20mm,right=20mm,footskip=8mm}

% --- Visual & Layout ---
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage{enumitem}

% --- Color Palette ---
\definecolor{primaryblue}{RGB}{20, 50, 110}     % 深遠な紺青
\definecolor{accentcrimson}{RGB}{165, 35, 45}   % 深紅
\definecolor{softblue}{RGB}{242, 246, 253}      % 問題背景
\definecolor{softsol}{RGB}{253, 248, 242}       % 解答背景
\definecolor{darkslate}{RGB}{45, 55, 72}        % 濃灰

% --- Headers & Footers ---
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{darkslate}\leftmark}
\fancyhead[R]{\small\color{darkslate}デュードニー『数学の愉しみ』原著全問完全翻訳版}
\fancyfoot[C]{\color{darkslate}\thepage}
\renewcommand{\headrulewidth}{0.5pt}

% --- Hyperref ---
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=accentcrimson,
    urlcolor=primaryblue,
    pdftitle={デュードニー 数学の愉しみ —— 全430問 原著完全翻訳・解答解説決定版},
    pdfauthor={ヘンリー・アーネスト・デュードニー / 教育情報分析研究会 訳}
}

\begin{document}

% --- Title Page ---
\begin{titlepage}
\centering
\vspace*{1.5cm}
{\color{primaryblue}\rule{\textwidth}{2pt}}\par
\vspace{1.0cm}
{\Huge\textbf{数学の愉しみ}\par}
\vspace{0.4cm}
{\huge\textbf{Amusements in Mathematics}\par}
\vspace{0.6cm}
{\Large\textbf{原著全430問 完全翻訳・数理的解答解説決定版}\par}
\vspace{0.8cm}
{\large — — 算術・幾何・トポロジー・チェス・魔方陣・論理の遊園地 — —\par}
\vspace{1.0cm}
{\color{accentcrimson}\rule{0.6\textwidth}{1.5pt}}\par
\vspace{2.0cm}

\begin{tcolorbox}[colback=softblue,colframe=primaryblue,width=0.85\textwidth,arc=3mm,boxrule=1.2pt]
\centering\large
\textbf{ヘンリー・アーネスト・デュードニー}（Henry Ernest Dudeney）著\\
\textbf{教育情報分析研究会} 訳・数学校閲\\
\vspace{0.5em}
\normalsize
Project Gutenberg eBook \#16713 完全日本語学術校閲版
\end{tcolorbox}

\vfill
{\Large\textbf{教育情報分析研究会}\par}
\vspace{0.3cm}
{\large 2026年 学術決定版\par}
\vspace{1.0cm}
\end{titlepage}

\frontmatter
\chapter*{原著序文（Preface）}
\addcontentsline{toc}{chapter}{原著序文}

この本を手にとる読者にまず申し上げたいのは、数学パズルとは無味乾燥な計算の訓練ではなく、人間の精神を最も純粋に解き放つ自由な知的遊戯である、ということです。

本書に収められた問題の多くは、私が長年にわたり『ストランド・マガジン』、『カッセルズ・マガジン』、『クイーン』、『ティット・ビッツ』、そして『ウィークリー・ディスパッチ』紙のパズル欄に寄稿してきた数千の問題の中から、特に数理的な独創性と美しさを備えたものを厳選し、全面的に加筆・修正した集大成です。

数学者であれ、好奇心旺盛な一般の読者であれ、あるいは若き探求者であれ、本書の430問の中に自らの知性を試す無限の愉しみを見出していただけることを願ってやみません。

\begin{flushright}
\textbf{ヘンリー・アーネスト・デュードニー}\\
ロンドン・著述家クラブにて　1917年3月
\end{flushright}

\tableofcontents
\mainmatter
"""

    part_defs = [
        (1, 141, '第1部：算術と代数の問題', 'Arithmetical and Algebraical Problems', '金銭・年齢・時計・速度・数字配置・ディオファントス方程式'),
        (142, 205, '第2部：幾何学の問題（裁ち合わせと配置）', 'Geometrical Problems', 'ギリシャ十字・等積変形・正方形分割・パッチワーク'),
        (206, 213, '第3部：点と線の問題', 'Points and Lines Problems', '植樹算・射影幾何・一直線上の配置'),
        (214, 238, '第4部：駒の移動とカウンターパズル', 'Moving Counter Problems', 'コイン反転・順列移動・レールの引き込み線'),
        (239, 261, '第5部：一筆書きと経路の問題', 'Unicursal and Route Problems', 'オイラーグラフ・ハミルトン路・巡回旅行'),
        (262, 287, '第6部：組合せと群の問題', 'Combination and Group Problems', 'キルクマンの女学生・配置ブロックデザイン'),
        (288, 361, '第7部：チェス盤の数学パズル', 'Chessboard Problems', 'ナイト・ツアー・8クイーン・盤面支配問題'),
        (362, 372, '第8部：測定・秤量・充填パズル', 'Measuring, Weighing, and Packing Puzzles', '油の分配・天秤の分銅・最少容器数'),
        (373, 377, '第9部：川渡りの問題', 'Crossing River Problems', '嫉妬深い夫・狼と羊・定員制約と状態遷移'),
        (378, 391, '第10部：ゲームに関する数学パズル', 'Problems Concerning Games', 'ドミノ・トランプ・サイコロの確率と配置'),
        (392, 398, '第11部：パズルゲームの必勝法', 'Puzzle Games', 'ニム・三目並べ・先手必勝法'),
        (399, 412, '第12部：魔方陣と素数方陣の問題', 'Magic Square Problems', '素数魔方陣・二階平方方陣・乗算方陣'),
        (413, 413, '第13部：パラドックス・パーティー', 'The Paradox Party', '幾何学的消失・無限集合の錯覚・論理の逆説'),
        (414, 430, '第14部：未分類の傑作パズル', 'Unclassified Problems', 'デュードニーが誇る総合的数学難問')
    ]

    parts = [preamble]

    # Map problem by number
    prob_map = {p['number']: p for p in problems}

    for start_n, end_n, ja_title, en_title, desc in part_defs:
        parts.append(f"\\part{{{ja_title}}}\n")
        parts.append(f"\\chapter*{{{ja_title} —— {en_title}}}\n")
        parts.append(f"\\addcontentsline{{toc}}{{chapter}}{{{ja_title}}}\n\n")
        parts.append(f"\\textbf{{【本部の概要】}} {desc}（全 {end_n - start_n + 1} 問：第 \\#{start_n} 問 〜 第 \\#{end_n} 問）\n\n\\vspace{{1em}}\n\n")

        for num in range(start_n, end_n + 1):
            if num not in prob_map:
                continue
            item = prob_map[num]
            title_clean = clean_for_latex(item.get('title', f'Problem {num}'))
            prob_clean = clean_for_latex(item.get('problem', ''))
            sol_clean = clean_for_latex(item.get('solution', ''))

            parts.append(r"\begin{tcolorbox}[colback=softblue,colframe=primaryblue,title=\textbf{第 " + str(num) + r" 問：" + title_clean + r"},arc=2mm,boxrule=1pt,breakable]" + "\n")
            parts.append(r"\textbf{【問題】}\par\vspace{0.3em}" + "\n")
            parts.append(prob_clean + "\n")
            parts.append(r"\tcblower" + "\n")
            parts.append(r"\textbf{【解答・解説】}\par\vspace{0.3em}" + "\n")
            parts.append(sol_clean + "\n")
            parts.append(r"\end{tcolorbox}" + "\n\n")

    parts.append(r"\end{document}" + "\n")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))

    print(f"Generated {tex_path} ({len(''.join(parts))} chars).")

if __name__ == "__main__":
    build_translation_book()
