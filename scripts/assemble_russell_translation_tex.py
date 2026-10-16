# -*- coding: utf-8 -*-
"""
Generate complete LaTeX document for:
バートランド・ラッセル『神秘主義と論理、その他の試論』
(原著全10篇・序文 完全翻訳・数理論理校閲版)
Gutenberg eBook #25447
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("scripts"))
from safe_latex_cleaner import clean_text_for_latex

CACHE_FILE = "books/25447_russell_mathematical_philosophy/russell_full_translation_cache.json"
SECTIONS_FILE = "books/25447_russell_mathematical_philosophy/russell_sections.json"
OUTPUT_TEX = "books/25447_russell_mathematical_philosophy/russell_mysticism_and_logic_translation.tex"

PREAMBLE = r"""\documentclass[a4paper,11pt,openany]{ltjsbook}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{geometry}
\geometry{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}
\usepackage{graphicx}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{fancyhdr}

\definecolor{russellblue}{RGB}{18, 48, 92}
\definecolor{softblue}{RGB}{240, 246, 253}
\definecolor{darkslate}{RGB}{30, 42, 56}
\definecolor{deepcrimson}{RGB}{145, 28, 42}
\definecolor{warmgold}{RGB}{175, 120, 20}

\hypersetup{
    colorlinks=true,
    linkcolor=russellblue,
    citecolor=darkslate,
    urlcolor=deepcrimson,
    pdftitle={神秘主義と論理 —— 原著完全直訳・数理論理校閲版},
    pdfauthor={バートランド・ラッセル}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\renewcommand{\headrulewidth}{0.4pt}

\title{
    {\huge\bfseries\gtfamily 神秘主義と論理、その他の試論}\\[12pt]
    {\Large\gtfamily —— 論理原子論・無限の数学・科学的認識論の全体系 ——}\\[18pt]
    {\large 原題：\textit{Mysticism and Logic and Other Essays} (1917)}\\[6pt]
    {\normalsize Project Gutenberg eBook \#25447}
}
\author{\textbf{バートランド・ラッセル} 著\\[4pt]教育情報分析研究会 訳・数理論理校閲}
\date{2026年10月 完全決定版}

\begin{document}

\maketitle

\frontmatter

\chapter*{訳者まえがき：20世紀数理哲学の金字塔}
\addcontentsline{toc}{chapter}{訳者まえがき：20世紀数理哲学の金字塔}

バートランド・ラッセル（Bertrand Russell, 1872--1970）が著した『神秘主義と論理、その他の試論（原題：\textit{Mysticism and Logic and Other Essays}）』は、ノーベル文学賞を受賞した稀代の知性であり、現代数理論理学・記号論理学・分析哲学の創始者であるラッセルの最も重要かつ美しく格調高い10篇の論文を収めた歴史的傑作集です（Project Gutenberg eBook \#25447）。

本書においてラッセルは、古代ギリシャのヘラクレイトスやプラトン以来の人類の知的探求を駆動してきた「神秘的衝動」と「科学的・論理的衝動」の対立と調和を鮮やかに論じる表題作をはじめ、冷厳な数学的真理の崇高な美を讃えた「数学の研究」、カントールの無限集合論やゼノンのパラドックスを明快に解決した現代数学の到達点を示す「数学と形而上学者たち」、そして現代物理学の時空と知覚経験を厳密な論理構築によって架橋する「センス・データと物理学との関係」「原因の概念について」「直接体験による知識と記述による知識」に至るまで、その思想の全貌を惜しみなく展開しています。

本完全翻訳・数理論理校閲版では、一切の要約や省略を排し、ラッセルの英語原文（序文および全10章）の重厚な文体、精密な論理の歩み、引用文献・脚注に至るまで忠実に日本語へ直訳いたしました。さらに、登場する集合論・実無限・関係論理・物理学的時空概念を厳密に校閲・検証し、ラッセルの知の建築を完全に追体験できる学術的決定版として組版・製本いたしました。

\clearpage
\tableofcontents
\clearpage

\mainmatter
"""

POSTAMBLE = r"""
\backmatter

\chapter*{解題：ラッセルの論理原子論と現代科学・数学の基礎}
\addcontentsline{toc}{chapter}{解題：ラッセルの論理原子論と現代科学・数学の基礎}

バートランド・ラッセルの哲学体系の核心は、「不完全で主観的な人間の知覚や言語の曖昧さを、厳密な論理分析と数学的構成によって脱神話化すること」にあります。

ホワイトヘッドとの記念碑的共著『プリンキピア・マテマティカ（数学原理）』において、算術と解析の全体系を純粋論理学から演繹しようとしたラッセルは、本書『神秘主義と論理』に収められた諸論考において、その数理的厳密さを現実世界の実在性や物理学の認識論へと果敢に拡張しました。

とりわけ「センス・データと物理学の関係」における「推論された実体ではなく、論理的構成物としての物理的客体」という公理的定式化（オッカムの剃刀の論理学的極限）は、現代の場の量子論、情報幾何学、認知科学における実在論論争の先駆をなすものです。また、「記述の理論（Theory of Descriptions）」は、存在しない対象（例：「現在のフランス国王」）をめぐる数千年来の形而上学の混乱を、命題関数の量化記号によって一挙に氷解させました。

ラッセルが示した「感情や願望による甘美な慰めを退け、事実と論理の冷厳な光を直視する勇気」は、現代を生きる知的生活者にとっても、永遠に色褪せない理性の羅針盤であり続けることでしょう。

\end{document}
"""

def generate_tex():
    if not os.path.exists(CACHE_FILE):
        print(f"Error: {CACHE_FILE} not found.")
        return False
    if not os.path.exists(SECTIONS_FILE):
        print(f"Error: {SECTIONS_FILE} not found.")
        return False

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    with open(SECTIONS_FILE, "r", encoding="utf-8") as f:
        meta_sections = json.load(f)

    tex_parts = [PREAMBLE]

    for sec in meta_sections:
        num = sec["number"]
        title_en = sec["title_en"]
        title_ja = sec.get("title_ja", title_en)
        key = f"Sec_{num}"

        if key not in cache or not cache[key].get("japanese_translation"):
            print(f"Error: {key} not found or incomplete in cache.")
            return False

        raw_trans = cache[key]["japanese_translation"]
        clean_trans = clean_text_for_latex(raw_trans)

        if num == "PREFACE":
            ch_tex = f"""\\chapter*{{序文（Preface）}}
\\addcontentsline{{toc}}{{chapter}}{{序文（Preface）}}

{clean_trans}
"""
        else:
            ch_tex = f"""\\chapter{{第{num}章：{title_ja}\\\\[2mm]\\normalsize\\textit{{{title_en}}}}}

{clean_trans}
"""
        tex_parts.append(ch_tex)

    tex_parts.append(POSTAMBLE)

    full_tex = "\n\n".join(tex_parts)
    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_tex)

    print(f"Successfully generated {OUTPUT_TEX} ({len(full_tex)} chars).")
    return True

if __name__ == "__main__":
    generate_tex()
