# -*- coding: utf-8 -*-
"""
Generate complete LaTeX document for:
アルベルト・アインシュタイン『特殊および一般相対性理論について』
(原著全32節・付録4篇 完全翻訳・数学校閲版)
Gutenberg eBook #30155
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("scripts"))
from safe_latex_cleaner import clean_text_for_latex

CACHE_FILE = "books/30155_einstein_relativity/einstein_full_translation_cache.json"
OUTPUT_TEX = "books/30155_einstein_relativity/einstein_relativity_translation.tex"

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

\definecolor{primaryblue}{RGB}{20, 60, 110}
\definecolor{softblue}{RGB}{238, 244, 252}
\definecolor{darkslate}{RGB}{35, 45, 60}
\definecolor{warmgold}{RGB}{185, 125, 20}
\definecolor{softgold}{RGB}{254, 249, 235}
\definecolor{accentcrimson}{RGB}{160, 30, 45}

\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=darkslate,
    urlcolor=accentcrimson,
    pdftitle={特殊および一般相対性理論について —— 原著完全直訳・数学校閲版},
    pdfauthor={アルベルト・アインシュタイン}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\renewcommand{\headrulewidth}{0.4pt}

\title{
    {\huge\bfseries\gtfamily 特殊および一般相対性理論について}\\[12pt]
    {\Large\gtfamily —— 原典完全直訳・数学校閲・学術決定版 ——}\\[18pt]
    {\large 原題：\textit{Relativity: The Special and the General Theory} (1916/1920)}\\[6pt]
    {\normalsize Project Gutenberg eBook \#30155}
}
\author{\textbf{アルベルト・アインシュタイン} 著\\[4pt]教育情報分析研究会 訳・数学校閲}
\date{2026年10月 完全決定版}

\begin{document}

\maketitle

\frontmatter

\chapter*{訳者まえがき：アインシュタイン自筆の普及的名著}
\addcontentsline{toc}{chapter}{訳者まえがき：アインシュタイン自筆の普及的名著}

アルベルト・アインシュタイン（Albert Einstein, 1879--1955）が自ら一般の読者に向けて執筆した唯一の本格的解説書『特殊および一般相対性理論について（原題：\textit{Über die spezielle und die allgemeine Relativitätstheorie, gemeinverständlich}）』は、1916年に初版が出版され、1920年にロバート・W・ローソン（Robert W. Lawson）によって英語に翻訳されました（Project Gutenberg eBook \#30155）。

一般にアインシュタインの論文といえば難解なテンソル計算や重力方程式が想起されますが、本書におけるアインシュタインの筆致は驚くほど平易かつ誠実です。彼は序文においてルートヴィヒ・ボルツマンの格言「エレガンス（優雅さ）の追求は仕立屋と靴屋に任せるべきである」を引用し、技巧的なレトリックを排して、概念の必然性と物理的意味を徹底して明快に説き明かしています。

本全訳・数学校閲版では、一切の要約や省略を行わず、アインシュタインの原著英文（全32節および付録4篇）の論理構造と数理的展開を完全に日本語へ直訳いたしました。さらに、各節の数式と時空変換の数理的整合性を厳密に確認・校閲し、原典の論理を正確に追体験できる構成としております。

\clearpage
\tableofcontents
\clearpage

\mainmatter
"""

POSTAMBLE = r"""
\backmatter

\chapter*{解題：相対性理論の誕生と20世紀物理学の革命}
\addcontentsline{toc}{chapter}{解題：相対性理論の誕生と20世紀物理学の革命}

アインシュタインの思考の軌跡を振り返るとき、私たちが目撃するのは「常識に対する冷徹な批判」と「対称性と不変性への絶対的な確信」です。

特殊相対性理論（1905年）は、光速度不変の原理とガリレイの相対性原理を両立させるために、人類が数千年にわたって自明視してきた「絶対時間」と「絶対空間」の概念を根底から解体しました。動く時計の遅れ、ローレンツ収縮、そして質量とエネルギーの等価性 $E = mc^2$ は、すべてこの幾何学的時空（ミンコフスキー空間）の必然的帰結として演繹されます。

さらに一般相対性理論（1915年）では、「等価原理」を手掛かりとして、ニュートン力学における「遠隔作用としての万有引力」を「物質とエネルギーによって歪められた時空の曲率（リーマン幾何学）」として幾何学的に完全に書き直しました。1919年のエディントンによる皆既日食観測での光線湾曲の確認は、世界中の科学界に衝撃を与え、アインシュタインの名を不滅のものとしました。

本全訳版が、原典の精緻な論理と物理的直観をそのままに味わうための不朽の道標となることを切に願います。

\end{document}
"""

def generate_tex_from_cache():
    if not os.path.exists(CACHE_FILE):
        print(f"Cache file {CACHE_FILE} not found.")
        return False

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    with open("books/30155_einstein_relativity/einstein_sections.json", "r", encoding="utf-8") as f:
        meta_sections = json.load(f)

    tex_parts = [PREAMBLE]
    current_part = None
    
    for sec_meta in meta_sections:
        num = sec_meta["number"]
        part = sec_meta["part"]
        title_en = sec_meta["title_en"]
        key = f"Sec_{num}"

        if key not in cache or not cache[key].get("japanese_translation"):
            print(f"Section {num} is not finished in cache yet.")
            return False

        sec_data = cache[key]
        trans_text = clean_text_for_latex(sec_data["japanese_translation"])
        
        # Part transition
        if part != current_part and part in ["Part I", "Part II", "Part III", "Appendix"]:
            current_part = part
            if part == "Part I":
                tex_parts.append("\\part{特殊相対性理論（The Special Theory of Relativity）}\n\n")
            elif part == "Part II":
                tex_parts.append("\\part{一般相対性理論（The General Theory of Relativity）}\n\n")
            elif part == "Part III":
                tex_parts.append("\\part{宇宙全体に関する考察（Considerations on the Universe as a Whole）}\n\n")
            elif part == "Appendix":
                tex_parts.append("\\part{付録（Appendices）}\n\n")

        # Heading
        if num == "Preface":
            ch_tex = f"""\\chapter*{{原著序文（Preface）}}
\\addcontentsline{{toc}}{{chapter}}{{原著序文（Preface）}}

{trans_text}
"""
        elif num.startswith("App_"):
            app_label = num.replace("App_", "付録 ")
            ch_tex = f"""\\chapter{{{app_label}：{title_en}}}

{trans_text}
"""
        else:
            ch_tex = f"""\\chapter{{第{num}節：{title_en}}}

{trans_text}
"""

        tex_parts.append(ch_tex)

    tex_parts.append(POSTAMBLE)
    
    full_doc = "\n\n\\clearpage\n".join(tex_parts)
    
    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_doc)

    print(f"Successfully generated {OUTPUT_TEX} ({len(full_doc)} bytes)")
    return True

if __name__ == "__main__":
    generate_tex_from_cache()
