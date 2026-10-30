# -*- coding: utf-8 -*-
"""
Generate complete translation LaTeX file for PG#22599
Smith & Karpinski: The Hindu-Arabic Numerals
"""

import os
import re
import sys
import json

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = r"E:\GoogleAntigravity\PG_mathbook"
BOOK_DIR = os.path.join(PROJECT_ROOT, "books", "22599_smith_hindu_arabic_numerals")
CACHE_FILE = os.path.join(BOOK_DIR, "smith_hindu_arabic_numerals_translation_cache.json")
TEX_OUT = os.path.join(BOOK_DIR, "smith_hindu_arabic_numerals_translation.tex")

sys.path.insert(0, os.path.join(PROJECT_ROOT, "scripts"))
from safe_latex_cleaner import clean_text_for_latex

PREAMBLE = r"""\documentclass[a4paper,11pt,openany]{ltjsbook}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{geometry}
\geometry{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,shapes.geometric}

\definecolor{primaryblue}{RGB}{20, 60, 110}
\definecolor{darkslate}{RGB}{35, 45, 60}
\definecolor{accentcrimson}{RGB}{160, 30, 45}
\definecolor{softblue}{RGB}{238, 244, 252}

\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=darkslate,
    urlcolor=primaryblue,
    pdftitle={インド・アラビア数字の歴史 —— ゼロの発見と近世記数法の革新},
    pdfauthor={デイヴィッド・ユージーン・スミス、ルイ・チャールズ・カーピンスキー / 教育情報分析研究会}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\setlength{\headheight}{17.5pt}
\renewcommand{\headrulewidth}{0.4pt}

\title{
    {\huge\bfseries\gtfamily インド・アラビア数字の歴史}\\[14pt]
    {\Large ゼロの発見と近世記数法の革新}\\[8pt]
    {\large —— 原著完全翻訳・数学校閲版 ——}\\[16pt]
    {\normalsize 原題：\textit{The Hindu-Arabic Numerals} (Project Gutenberg eBook No. 22599)}
}
\author{
    \textbf{デイヴィッド・ユージーン・スミス}（David Eugene Smith）\\
    \textbf{ルイ・チャールズ・カーピンスキー}（Louis Charles Karpinski） 著\\[12pt]
    \textbf{教育情報分析研究会} 訳・数理歴史校閲
}
\date{2026年10月 完全決定版}

\begin{document}
\maketitle
\frontmatter
\tableofcontents
\clearpage

\chapter*{解題：『インド・アラビア数字の歴史』の学術的意義}
\addcontentsline{toc}{chapter}{解題：『インド・アラビア数字の歴史』の学術的意義}

本書は、アメリカ数学史研究のパイオニアであるコロンビア大学教授デイヴィッド・ユージーン・スミス（David Eugene Smith, 1860--1944）とミシガン大学教授ルイ・チャールズ・カーピンスキー（Louis Charles Karpinski, 1878--1956）による名著『\textit{The Hindu-Arabic Numerals}』（1911年刊）の完全日本語翻訳・数学校閲版である。

今日、人類のあらゆる科学技術、経済取引、日常的計算の根幹を支えている「$0, 1, 2, 3, 4, 5, 6, 7, 8, 9$」という10個の記号と、それらに位置による重み付けを与える「十進位取り記数法（place value system）」は、古代インドで発明され、中世アラビア世界を経由して西欧中世・ルネサンス期へと伝播した。

本書は、古代インドのアショーカ王碑文（紀元前3世紀）やブラーフミー文字、ナーナー・ガート石刻、グワリオール碑文（876年の最古の確定ゼロ刻印）にまで遡り、アル＝フワーリズミーやアル＝キンディーらイスラム黄金期の数学者たちの貢献、さらにはシルヴェステル2世（教皇ゲルベルト）のアバクス（算盤）革命、レオナルド・フィボナッチの『算盤の書（Liber Abaci）』によるヨーロッパへの本格的受容、そして15世紀の印刷術普及に至る1500年以上にわたるドラマを、膨大な一次史料と碑文・写本証拠に基づいて緻密に論証した記念碑的労作である。

高校までの数学的基礎知識（位取りの概念や初等代数・算術操作）をもつ読者であれば、人類最大の知的発明の一つである「記数法革命」の全貌を鮮明に追体験することができるであろう。

\clearpage
\mainmatter
"""

CHAPTER_TITLES = [
    "第1章：インド・アラビア数字の起源に関する初期の諸説",
    "第2章：位取り記法を伴わない初期のインド数字",
    "第3章：位取り記法を伴う後期のインド数字",
    "第4章：記号「ゼロ」の起源と誕生",
    "第5章：ボエティウスによるヨーロッパへの数字導入をめぐる問題",
    "第6章：アラビア世界における数字の発展と受容",
    "第7章：ヨーロッパへの数字の本格的導入",
    "第8章：ヨーロッパ各地における数字の普及と計算革命"
]


def main():
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    parts = [PREAMBLE]

    for ch_idx in range(1, 9):
        key = f"Chapter_{ch_idx}"
        ch_data = cache.get(key, {})
        title_ja = CHAPTER_TITLES[ch_idx - 1]
        en_title = ch_data.get("title_en", "")

        parts.append(f"\\chapter{{{title_ja}}}\n")
        parts.append(f"\\section*{{{en_title}}}\n\n")

        jp_text = ch_data.get("japanese_translation", "")
        # Apply clean_text_for_latex
        jp_clean = clean_text_for_latex(jp_text)
        parts.append(jp_clean)
        parts.append("\n\n\\clearpage\n\n")

    parts.append(r"\end{document}" + "\n")

    full_tex = "".join(parts)
    with open(TEX_OUT, "w", encoding="utf-8") as f:
        f.write(full_tex)

    print(f"Generated {TEX_OUT} ({len(full_tex)} chars).")


if __name__ == "__main__":
    main()
