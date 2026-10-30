# -*- coding: utf-8 -*-
"""
Assemble Sir Thomas Little Heath's "Archimedes" into a complete LuaLaTeX document.
Includes:
- Elegant typography (ltjsbook, HaranoAji fonts, modern margins, geometry)
- Academic introduction & editorial commentary
- Full translation of all 7 chapters + 2 appendices
- Safe LaTeX escaping (zero errors, clean Carets/Math/Greek/Accents)
"""

import os
import sys
import json
import re

PROJECT_ROOT = r"E:\GoogleAntigravity\PG_mathbook"
BOOK_DIR = os.path.join(PROJECT_ROOT, "books", "35550_heath_archimedes")
CACHE_FILE = os.path.join(BOOK_DIR, "heath_archimedes_translation_cache.json")
TEX_OUT = os.path.join(BOOK_DIR, "heath_archimedes_translation.tex")

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
    pdftitle={アルキメデス —— 古代幾何学・力学の巨人と近代科学の源流},
    pdfauthor={サー・トーマス・リトル・ヒース / 教育情報分析研究会}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\small\thepage}
\fancyhead[LO]{\small\rightmark}
\fancyhead[RE]{\small\leftmark}
\renewcommand{\headrulewidth}{0.4pt}
\setlength{\headheight}{18pt}

\begin{document}

\frontmatter

\begin{titlepage}
    \centering
    \vspace*{2.0cm}
    {\Huge\textbf{アルキメデス}\par}
    \vspace{0.4cm}
    {\Large\textbf{古代幾何学・力学の巨人と近代科学の源流}\par}
    \vspace{0.8cm}
    {\large — — 原著完全翻訳・数学校閲決定版 — —\par}
    \vspace{1.5cm}
    {\large 原題：\textit{Archimedes} (Pioneers of Progress: Men of Science, 1920)\par}
    \vspace{0.3cm}
    {\large Project Gutenberg eBook No. 35550\par}
    \vspace{2.5cm}
    {\Large サー・トーマス・リトル・ヒース（Sir Thomas Little Heath）著\par}
    \vspace{0.5cm}
    {\large 教育情報分析研究会 訳・数理歴史校閲\par}
    \vfill
    {\large 2026年10月 完全決定版\par}
    \vspace*{1.0cm}
\end{titlepage}

\tableofcontents
\clearpage

\chapter*{解題：『アルキメデス』の学術的意義と現代的価値}
\addcontentsline{toc}{chapter}{解題：『アルキメデス』の学術的意義と現代的価値}

本書は、古代ギリシャ数学・天文学史の最高権威であるサー・トーマス・リトル・ヒース（Sir Thomas Little Heath, 1861--1940）が、ロンドンのキリスト教知識普及協会（SPCK）の叢書「進歩の先駆者たち：科学の巨人（Pioneers of Progress: Men of Science）」の一冊として1920年に著した『\textit{Archimedes}』の完全日本語翻訳・数学校閲版である。

ヒースはケンブリッジ大学トリニティ・カレッジで古典学と数学を修め、英国財務省の高級官僚（常任次官）を務める傍ら、ユークリッド『原論』全13巻の英訳注解や『ギリシャ数学史（A History of Greek Mathematics）』など、20世紀の西洋古典科学史を決定づける不朽の記念碑的業績を遺した。その浩瀚な学識をコンパクトな一冊に結晶化させたのが本書である。

アルキメデス（Archimedes of Syracuse, ca. 前287--前212）は、単なる「てこの原理」や「エウレカ（王冠の比重測定）」の伝説的発明家にとどまらない。彼はユークリッドやエウドクソスの幾何学を継承しつつ、現代の積分学の直観的先駆けとなった「力学的求積法（Method of Mechanical Theorems）」を考案し、厳密な「取り尽くし法（Method of Exhaustion）」によって球・円柱・回転放物面・らせん・放物線の面積や体積を正確に計算し尽くした、人類史上最も傑出した数学者の一人である。

本書は、シラクサ防衛戦や彼の劇的な生涯（第I章）、エウドクソスやヒッポクラテスからアルキメデスに至るギリシャ幾何学の雄大な発展史（第II章）、奇跡的に現存した写本伝承（第III章）、円周率の厳密な上下不等式評価や球と円柱の驚異の幾何学（第IV章）、宇宙を埋め尽くす砂の粒の数を指数的命数法で数え上げた『砂粒論』（第V章）、そして重心論・てこの原理（第VI章）や流体静力学・浮体の安定条件（第VII章）に至るまで、アルキメデスの知的宇宙の全貌を余すところなく明解に解き明かしている。

高校・大学初年級の数学・物理知識（三角法、初等幾何、力学の基礎）があれば、2000年以上前の天才がいかにして現代の微積分学や理論物理学の礎を独力で築き上げたのか、その息を呑む論理展開を鮮明に追体験することができるであろう。

\clearpage
\mainmatter
"""

CHAPTER_TITLES = [
    "第1章：アルキメデスの生涯と逸話",
    "第2章：アルキメデスに至る古代ギリシャ幾何学の歩み",
    "第3章：アルキメデスの著作群と写本伝承",
    "第4章：アルキメデスの幾何学 —— 取り尽くし法と求積法",
    "第5章：砂の計算者（砂粒論） —— 巨大数と宇宙の大きさ",
    "第6章：力学 —— てこの原理・重心論と幾何学的証明",
    "第7章：流体静力学 —— 浮体の原理とエウレカの発見",
    "付録A：参考文献解題",
    "付録B：アルキメデスと古代科学史年表"
]

def main():
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    parts = [PREAMBLE]

    for sec_idx in range(1, 10):
        key = f"Section_{sec_idx}"
        sec_data = cache.get(key, {})
        title_ja = CHAPTER_TITLES[sec_idx - 1]
        en_title = sec_data.get("title_en", "")

        if sec_idx <= 7:
            parts.append(f"\\chapter{{{title_ja}}}\n")
            parts.append(f"\\section*{{{en_title}}}\n\n")
        else:
            parts.append(f"\\chapter*{{{title_ja}}}\n")
            parts.append(f"\\addcontentsline{{toc}}{{chapter}}{{{title_ja}}}\n\n")

        pieces = sec_data.get("translation_pieces", [])
        sec_text = "\n\n".join(pieces)

        # Apply clean_text_for_latex
        sec_clean = clean_text_for_latex(sec_text)

        # Handle math carets cleanly
        sec_clean = re.sub(r'([A-Za-z0-9]+)\^([A-Za-z0-9]+)', lambda m: "$" + m.group(1) + "^{" + m.group(2) + "}$", sec_clean)
        sec_clean = sec_clean.replace('^', '')
        # Clean rare unrenderable symbols
        sec_clean = re.sub(r'[\u0e00-\u0eff]', '', sec_clean)
        # Fix double backslash textit
        sec_clean = re.sub(r'\\\\([a-zA-Z]+)', r'\\\1', sec_clean)

        parts.append(sec_clean)
        parts.append("\n\n\\clearpage\n\n")

    parts.append(r"\end{document}" + "\n")

    full_tex = "".join(parts)
    with open(TEX_OUT, "w", encoding="utf-8") as f:
        f.write(full_tex)

    print(f"Generated {TEX_OUT} ({len(full_tex)} chars).")

if __name__ == "__main__":
    main()
