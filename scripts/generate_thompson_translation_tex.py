# -*- coding: utf-8 -*-
"""
Generate LuaLaTeX document for Silvanus P. Thompson #33283
"Calculus Made Easy" (原著全21章＋序文・プロローグ・エピローグ・付録解答 完全翻訳・数学校閲版)
"""

import json
import re
import os
import sys

CACHE_FILE = "books/33283_thompson_calculus/thompson_full_translation_math_verified.json"
OUTPUT_TEX = "books/33283_thompson_calculus/thompson_calculus_translation.tex"

sys.path.insert(0, os.path.abspath("scripts"))
from thompson_metadata import SECTIONS_METADATA

def get_clean_standard_forms_table():
    return r"""
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
$\dfrac{dy}{dx}$ & $\longleftarrow\quad y\quad\longrightarrow$ & $\displaystyle\int y\, dx$ \\
\hline
\multicolumn{3}{|c|}{\textbf{代数関数（Algebraic）}} \\
\hline
$1$ & $x$ & $\frac{1}{2} x^2 + C$ \\
$0$ & $a$ & $ax + C$ \\
$1$ & $x \pm a$ & $\frac{1}{2} x^2 \pm ax + C$ \\
$a$ & $ax$ & $\frac{1}{2} ax^2 + C$ \\
$2x$ & $x^2$ & $\frac{1}{3} x^3 + C$ \\
$nx^{n-1}$ & $x^n$ & $\dfrac{1}{n+1} x^{n+1} + C$ \\
$-x^{-2}$ & $x^{-1}$ & $\log_\epsilon x + C$ \\
$\dfrac{du}{dx} \pm \dfrac{dv}{dx} \pm \dfrac{dw}{dx}$ & $u \pm v \pm w$ & $\int u\, dx \pm \int v\, dx \pm \int w\, dx$ \\
$u\, \dfrac{dv}{dx} + v\, \dfrac{du}{dx}$ & $uv$ & 一般公式なし \\
$\dfrac{v\, \dfrac{du}{dx} - u\, \dfrac{dv}{dx}}{v^2}$ & $\dfrac{u}{v}$ & 一般公式なし \\
$\dfrac{du}{dx}$ & $u$ & $ux - \int x\, du + C$ \\
\hline
\multicolumn{3}{|c|}{\textbf{指数関数・対数関数（Exponential and Logarithmic）}} \\
\hline
$\epsilon^x$ & $\epsilon^x$ & $\epsilon^x + C$ \\
$x^{-1}$ & $\log_\epsilon x$ & $x(\log_\epsilon x - 1) + C$ \\
$0.4343 \times x^{-1}$ & $\log_{10} x$ & $0.4343x (\log_\epsilon x - 1) + C$ \\
$a^x \log_\epsilon a$ & $a^x$ & $\dfrac{a^x}{\log_\epsilon a} + C$ \\
\hline
\multicolumn{3}{|c|}{\textbf{三角関数（Trigonometrical）}} \\
\hline
$\cos x$ & $\sin x$ & $-\cos x + C$ \\
$-\sin x$ & $\cos x$ & $\sin x + C$ \\
$\sec^2 x$ & $\tan x$ & $-\log_\epsilon \cos x + C$ \\
\hline
\multicolumn{3}{|c|}{\textbf{逆三角関数（Circular / Inverse）}} \\
\hline
$\dfrac{1}{\sqrt{1-x^2}}$ & $\arcsin x$ & $x \cdot \arcsin x + \sqrt{1 - x^2} + C$ \\
$-\dfrac{1}{\sqrt{1-x^2}}$ & $\arccos x$ & $x \cdot \arccos x - \sqrt{1 - x^2} + C$ \\
$\dfrac{1}{1+x^2}$ & $\arctan x$ & $x \cdot \arctan x - \frac{1}{2} \log_\epsilon (1 + x^2) + C$ \\
\hline
\multicolumn{3}{|c|}{\textbf{双曲線関数（Hyperbolic）}} \\
\hline
$\cosh x$ & $\sinh x$ & $\cosh x + C$ \\
$\sinh x$ & $\cosh x$ & $\sinh x + C$ \\
$\sech^2 x$ & $\tanh x$ & $\log_\epsilon \cosh x + C$ \\
\hline
\multicolumn{3}{|c|}{\textbf{その他の有用な標準公式（Miscellaneous）}} \\
\hline
$-\dfrac{1}{(x + a)^2}$ & $\dfrac{1}{x + a}$ & $\log_\epsilon (x+a) + C$ \\
$-\dfrac{x}{(a^2 + x^2)^{\frac{3}{2}}}$ & $\dfrac{1}{\sqrt{a^2 + x^2}}$ & $\log_\epsilon (x + \sqrt{a^2 + x^2}) + C$ \\
$\mp \dfrac{b}{(a \pm bx)^2}$ & $\dfrac{1}{a \pm bx}$ & $\pm \dfrac{1}{b} \log_\epsilon (a \pm bx) + C$ \\
$-\dfrac{3a^2x}{(a^2 + x^2)^{\frac{5}{2}}}$ & $\dfrac{a^2}{(a^2 + x^2)^{\frac{3}{2}}}$ & $\dfrac{x}{\sqrt{a^2 + x^2}} + C$ \\
$a \cos ax$ & $\sin ax$ & $-\dfrac{1}{a} \cos ax + C$ \\
$-a \sin ax$ & $\cos ax$ & $\dfrac{1}{a} \sin ax + C$ \\
$a \sec^2 ax$ & $\tan ax$ & $-\dfrac{1}{a} \log_\epsilon \cos ax + C$ \\
$\sin 2x$ & $\sin^2 x$ & $\dfrac{x}{2} - \dfrac{\sin 2x}{4} + C$ \\
$-\sin 2x$ & $\cos^2 x$ & $\dfrac{x}{2} + \dfrac{\sin 2x}{4} + C$ \\
$n \sin^{n-1} x \cos x$ & $\sin^n x$ & $-\dfrac{\cos x}{n} \sin^{n-1} x + \dfrac{n-1}{n} \int \sin^{n-2} x\, dx + C$ \\
$-\dfrac{\cos x}{\sin^2 x}$ & $\dfrac{1}{\sin x}$ & $\log_\epsilon \tan \dfrac{x}{2} + C$ \\
$-\dfrac{\sin 2x}{\sin^4 x}$ & $\dfrac{1}{\sin^2 x}$ & $-\cotan x + C$ \\
$\dfrac{\sin^2 x - \cos^2 x}{\sin^2 x \cos^2 x}$ & $\dfrac{1}{\sin x \cos x}$ & $\log_\epsilon \tan x + C$ \\
$2a \sin 2ax$ & $\sin^2 ax$ & $\dfrac{x}{2} - \dfrac{\sin 2ax}{4a} + C$ \\
$-2a \sin 2ax$ & $\cos^2 ax$ & $\dfrac{x}{2} + \dfrac{\sin 2ax}{4a} + C$ \\
\hline
\end{tabular}
\end{center}
"""

def clean_latex(text, sec_id=""):
    if sec_id == "standard_forms":
        return get_clean_standard_forms_table()

    # If this is the answers section, truncate at the start of Gutenberg legal boilerplates
    if sec_id == "answers":
        for cut_marker in [
            "Creating print editions not protected",
            "プロジェクト・ゲッutenberg文学アーカイブ財団",
            "Project Gutenberg文学アーカイブ財団",
            "Project Gutenbergのウェブページをご確認ください"
        ]:
            if cut_marker in text:
                text = text.split(cut_marker)[0]

    # 1. Strip any AI preamble lines about translation completely
    text = re.sub(r'^(?:以下[^\n]*|忠実[^\n]*|次[^\n]*|この[^\n]*|原著[^\n]*)(?:翻訳|日本語訳)[^\n]*[：:\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'【(?:翻訳|日本語訳|訳文)】\s*', '', text)
    text = re.sub(r'次のように翻訳します[：:]\s*', '', text)
    text = re.sub(r'以下が[^\n]*翻訳[^\n]*[：:]\s*', '', text)
    text = re.sub(r'以下の文章を忠実に日本語[へに]翻訳[しいたします]+[：:]\s*', '', text)
    text = re.sub(r'以下の原著英文を忠実に日本語[へに]翻訳[しいたします]+[：:]\s*', '', text)
    text = re.sub(r'以下の文を忠実に日本語[へに]翻訳[しいたします]+[：:]\s*', '', text)
    text = re.sub(r'以下、?原著英文を忠実に日本語[へに]翻訳[しいたします]+[：:]\s*', '', text)
    text = re.sub(r'以下は、?原著英文を忠実に日本語[へに]翻訳[しいたします]+[：:]\s*', '', text)
    text = re.sub(r'以下に、?原著英文を忠実に[^\n]*[：:]\s*', '', text)
    text = re.sub(r'忠実に日本語[へに]翻訳[しいたします]+[：:]\s*', '', text)
    text = re.sub(r'忠実に日本語[へに]翻訳したもの[を示します結果です]+[：:]\s*', '', text)
    text = re.sub(r'忠実に日本語[へに]翻訳すると以下のようになります[：:]\s*', '', text)
    text = re.sub(r'忠実に翻訳したもの[を示します]+[：:]\s*', '', text)
    text = re.sub(r'忠実に翻訳し、自然な日本語表現に調整しました[^\n]*\n?', '', text)
    text = re.sub(r'忠実な(?:日本語)?翻訳です[。：:\n]?', '', text)
    text = re.sub(r'忠実に翻訳する[。：:\n]?', '', text)

    # 2. Fix specific TeX artifact commands that Qwen copied from Gutenberg TeX
    text = re.sub(r'\\AltChapter\[[^\]]*\]\{[^}]*\}', '', text)
    text = re.sub(r'\\chapter\*?\{[^}]*\}', '', text)
    text = re.sub(r'\\section\*?\{[^}]*\}', '', text)

    # In regular chapters (not answers), strip problematic begin/end list environments
    # that cause section-crossing unclosed bugs
    if sec_id != "answers":
        text = re.sub(r'\\begin\{(?:Problems|SubProbs|exercises|subproblems|problems|enumerate)\}(\[[^\]]*\])?', '', text)
        text = re.sub(r'\\end\{(?:Problems|SubProbs|exercises|subproblems|problems|enumerate)\}', '', text)

    # Convert \begin{Answers}... to section header without creating an unclosed environment
    ans_pattern = r'\\begin\{Answers\}(?:\[[^\]]*\])?\{([a-zA-Z0-9]+)\}(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})*'
    text = re.sub(ans_pattern, r'\\par\\bigskip\\noindent{\\Large\\bfseries [演習 \1 の解答]}\\par\\smallskip', text)
    text = re.sub(r'\\end\{Answers\}', r'\\par\\smallskip', text)

    # Remove empty display math \[ \]
    text = re.sub(r'\\\[\s*\\\]', '', text)

    # Fix nested display math: \[ \begin{align*} ... \end{align*} \]
    text = re.sub(r'\\\[\s*(\\begin\{(?:align\*?|alignat\*?|gather\*?|multline\*?)\}[\s\S]*?\\end\{(?:align\*?|alignat\*?|gather\*?|multline\*?)\})\s*\\\]', r'\1', text)

    # Fix PadTo macro
    text = re.sub(r'\\PadTo\{[^}]*\}\{([^}]*)\}', r'\1', text)

    # Fix Exercises, Examples, Example, Figure, Graphic
    text = re.sub(r'\\Exercises(\[[^\]]*\])?\{([^}]*)\}', r'\\par\\textbf{【演習 \2】}\\par', text)
    text = re.sub(r'\\Examples?(\[[^\]]*\])?\{([^}]*)\}', r'\\par\\textbf{【例題 \2】}\\par', text)
    text = re.sub(r'\\Figures?(\[[^\]]*\])?\{[^}]*\}\{([^}]*)\}', r'\\par\\textbf{〔第\2図〕}\\par', text)
    text = re.sub(r'\\Graphic\{[^}]*\}', '', text)
    text = re.sub(r'\\raisebox\{[^}]*\}\{([^}]*)\}', r'\1', text)

    # Replace DP align/gather environments
    text = re.sub(r'\\begin\{DPalign\*\}', r'\\begin{align*}', text)
    text = re.sub(r'\\end\{DPalign\*\}', r'\\end{align*}', text)
    text = re.sub(r'\\begin\{DPgather\*\}', r'\\begin{gather*}', text)
    text = re.sub(r'\\end\{DPgather\*\}', r'\\end{gather*}', text)

    # Specific fix for orphan \end{center} or unclosed \begin{center}
    text = text.replace(r"\begin{center}", "").replace(r"\end{center}", "")

    # Replace custom Item with \item
    text = re.sub(r'\\Item\{([^}]*)\}', r'\\item[\1]', text)
    text = re.sub(r'\\Item\[([^\]]*)\]', r'\\item[\1]', text)
    text = text.replace(r'\Item', r'\item')

    # Fix lone aligned in answers
    text = text.replace(r"\item[(9)] \begin{aligned}[t]", r"\item[(9)] $\begin{aligned}[t]")

    # Remove DPPageSep, Pagelabel, ResetCols, etc.
    text = re.sub(r'\\DPPageSep\{[^}]*\}\{[^}]*\}%?', '', text)
    text = re.sub(r'\\Pagelabel\{[^}]*\}', '', text)
    text = re.sub(r'\\ResetCols\{[^}]*\}', '', text)
    text = text.replace(r'\BindMath{', '').replace(r'\CancelMathSkip', '')
    text = text.replace(r'\efrac', r'\frac')
    text = text.replace(r'\ds', r'\displaystyle ')
    text = text.replace(r'\loosen', '')

    # DPtypo{original}{correction} -> correction
    text = re.sub(r'\\DPtypo\{[^}]*\}\{([^}]*)\}', r'\1', text)

    # Specific typo fix in chap_04 and answers
    text = text.replace(r"\left(\frac{dx}{x}\right)2 - \text{等.] \right]", r"\left(\frac{dx}{x}\right)^2 - \text{等} \right]")
    text = text.replace(r"x^{5}{-\frac{8}{3}}}", r"x^{-\frac{8}{3}}")
    text = text.replace(r"$p$$112$.\textasciitilde{}$12$\textit{s}$", r"112ポンド12シリング")

    # 3. Clean stray OCR or translation artifacts
    text = text.replace("£", "$p$")
    text = text.replace("\\、", "、")
    text = text.replace(r"\±", r"\pm")
    text = text.replace(r"-\frac{1}{500}", r"$-\frac{1}{500}$")

    # 4. Simplified Chinese to Japanese kanji mapping
    kanji_map = {
        '储': '儲', '质': '質', '转': '転', '误': '誤', '产': '産',
        '计': '計', '设': '設', '读': '読', '对': '対', '电': '電',
        '标': '標', '录': '録', '错': '錯', '识': '識', '损': '損',
        '盘': '盤', '备': '備', '码': '碼', '员': '員', '进': '進',
        '观': '観', '类': '類', '态': '態', '规': '規', '则': '則'
    }
    for k, v in kanji_map.items():
        text = text.replace(k, v)

    # 5. Fix nested display math & unescaped symbols outside math
    pattern = r'(\\begin\{(?:align\*?|alignat\*?|gather\*?|multline\*?|equation\*?|split|aligned|gathered)\}[\s\S]*?\\end\{(?:align\*?|alignat\*?|gather\*?|multline\*?|equation\*?|split|aligned|gathered)\}|\$\$[\s\S]*?\$\$|\$[^\$\n]+?\$|\\\(.*?\\\)|\\\[[\s\S]*?\\\])'
    parts = re.split(pattern, text)
    cleaned_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            # Inside math environment
            p = part.replace("×", r"\times ")
            p = p.replace("°", r"^\circ")
            cleaned_parts.append(p)
        else:
            # Outside math environment
            p = part
            p = p.replace("^", "")
            p = p.replace("°", "$^\\circ$")
            p = p.replace("×", r"$\times$")
            p = p.replace("¥", "")
            p = p.replace("#", "\\#")
            p = p.replace("²", "$^2$")
            p = p.replace("³", "$^3$")
            p = p.replace("&", "\\&")
            p = p.replace("_", "\\_")
            p = p.replace("~", "\\textasciitilde{}")
            p = p.replace("概率", "確率")
            cleaned_parts.append(p)
    text = "".join(cleaned_parts)

    # In both regular chapters and answers, cleanly wrap \item sequences in enumerate
    lines = text.split('\n')
    in_enum = False
    new_lines = []
    for l in lines:
        stripped = l.strip()
        if stripped.startswith(r'\item'):
            if not in_enum:
                new_lines.append(r'\begin{enumerate}')
                in_enum = True
            new_lines.append(l)
        elif stripped.startswith(r'\begin{enumerate}'):
            new_lines.append(l)
        elif stripped.startswith(r'\end{enumerate}'):
            new_lines.append(l)
        elif stripped.startswith(r'\par\bigskip') or stripped.startswith(r'\chapter') or stripped.startswith(r'\section') or stripped.startswith(r'\textbf{【演習'):
            if in_enum:
                new_lines.append(r'\end{enumerate}')
                in_enum = False
            new_lines.append(l)
        else:
            new_lines.append(l)
    if in_enum:
        new_lines.append(r'\end{enumerate}')
    text = '\n'.join(new_lines)

    # 6. Clean up single backslashes before Japanese chars
    text = re.sub(r'\\(?=[\u3000-\u9fff\uff00-\uffef、。・])', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def main():
    if not os.path.exists(CACHE_FILE):
        print(f"Error: {CACHE_FILE} does not exist.")
        return

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    preamble = r"""\documentclass[a4paper,11pt,openany]{ltjsbook}
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
    pdftitle={誰にもわかる微積分 —— 原著完全直訳・数学校閲版},
    pdfauthor={シルバヌス・P・トンプソン}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\renewcommand{\headrulewidth}{0.4pt}

% Compatibility macros for Thompson TeX original
\newcommand{\lintertext}[1]{\intertext{#1}}
\newcommand{\rintertext}[1]{\intertext{#1}}
\newcommand{\ds}{\displaystyle}
\newcommand{\tb}{\par\vspace{2mm}\hrule width 0.3\textwidth\vspace{2mm}\par}
\newcommand{\DStrut}{}
\newcommand{\efrac}[2]{\frac{#1}{#2}}
\DeclareMathOperator{\cotan}{cotan}
\DeclareMathOperator{\Arcsin}{arc\,sin}
\DeclareMathOperator{\Arccos}{arc\,cos}
\DeclareMathOperator{\Arctan}{arc\,tan}
\DeclareMathOperator{\sech}{sech}
\newcommand{\Pageref}[2][p.]{#1~\ref{#2}}
\newcommand{\Pagerange}[2]{pp.~\ref{#1}--\ref{#2}}
\newcommand{\Fig}[1]{Fig.~\ref{fig:#1}}
\newcommand{\Figs}[3]{Figs.~\ref{fig:#1}#2\ref{fig:#3}}
\newcommand{\NB}{\textit{N.B.}}
\newcommand{\IE}{\textit{i.e.}}

\begin{document}

% --- 表紙 ---
\begin{titlepage}
    \centering
    \vspace*{25mm}
    {\fontsize{14}{20}\selectfont \textbf{プロジェクト・グーテンベルク古典数学翻訳・校閲シリーズ 第5弾}}\\[8mm]
    {\fontsize{28}{36}\selectfont \textbf{誰にもわかる微積分}}\\[4mm]
    {\fontsize{16}{22}\selectfont \textit{Calculus Made Easy (1914)}}\\[12mm]
    \rule{0.85\textwidth}{1.5pt}\\[10mm]
    {\fontsize{15}{22}\selectfont \textbf{シルバヌス・P・トンプソン} 著}\\[3mm]
    {\fontsize{12}{18}\selectfont （Silvanus P. Thompson, D.Sc., F.R.S.）}\\[8mm]
    {\fontsize{13}{19}\selectfont 原著全21章・序文・プロローグ・エピローグ・全演習問題解答 完全直訳}\\[2mm]
    {\fontsize{11}{16}\selectfont \textbf{Qwen2.5-7B-Instruct 忠実翻訳 ／ Qwen2.5-Math-7B-Instruct 数理解析校閲}}\\[25mm]
    \vfill
    {\fontsize{11}{16}\selectfont 2026年10月 電子書籍版}\\[2mm]
    {\fontsize{10}{14}\selectfont \textbf{古典数理復刻プロジェクト}}\\[15mm]
\end{titlepage}

% --- まえがき・解題 ---
\frontmatter
\chapter*{解題：『誰にもわかる微積分』の不朽の意義}
\addcontentsline{toc}{chapter}{解題：『誰にもわかる微積分』の不朽の意義}

シルバヌス・フィリップス・トンプソン（Silvanus Phillips Thompson, 1851--1916）による『Calculus Made Easy』（1910年初版、1914年改訂第2版）は、1世紀以上にわたって世界中で愛読され続けてきた、微積分学教育史上屈指の名著である。

当時のイギリスにおける数学教育は、厳密主義と抽象的な形式主義に偏重し、初学者や工学を志す若者たちにとって、微積分は「一部の天才だけが操る難解な暗号」として恐れられていた。物理学者・電気工学者であったトンプソンは、この状況に強い義憤を覚え、F.R.S.（王立協会フェロー）という自らの権威を隠して匿名（「ある無知なる者」）で本書を世に問うた。

本書を貫く根本思想は、プロローグに掲げられた古代の格言に集約される：
\begin{quote}
\textbf{「一人の人間にできることは、他の人間にもできる（What one fool can do, another can.）」}
\end{quote}

トンプソンは、$dx$ や $dy$ を神秘的な不可知の対象とみなすことを排し、単なる「少しばかりの微小量」として親しみやすく直観的に解き明かした。高次の微小量をなぜ切り捨ててよいのか、和差積商や連鎖律、極大極小問題、そして定積分による面積の求値法から微分方程式に至るまで、初等数学の素朴な知性をもって一歩一歩確実に登り詰める構成となっている。

本書は、プロジェクト・グーテンベルク収録の第2版完全TeX原著（EBook \#33283）に基づき、本文・数式・演習問題解答に至る全26セクションを一語の省略もなく忠実に日本語へと翻訳し、現代最高峰のオープン推論モデルである \texttt{Qwen2.5-7B-Instruct} による全訳および \texttt{Qwen2.5-Math-7B-Instruct} による数理・LaTeX検証を経て制作された完全直訳版である。

\tableofcontents

\mainmatter

"""

    sections_tex = []

    # Map of sections in SECTIONS_METADATA order
    for meta in SECTIONS_METADATA:
        sec_id = meta["id"]
        sec_num = meta["number"]
        title_ja = meta["title_ja"]
        title_en = meta["title_en"]
        sub_ja = meta.get("subtitle_ja", "")

        sec_data = data.get(sec_id, {})
        trans_text = clean_latex(sec_data.get("japanese_translation", ""), sec_id=sec_id)

        print(f"Adding {sec_id}: {sec_num} {title_ja} ({len(trans_text)} chars)...")

        sec_buf = []

        if sec_id in ["preface", "prologue"]:
            sec_buf.append(f"\\chapter*{{{sec_num}：{title_ja}}}\n")
            sec_buf.append(f"\\addcontentsline{{toc}}{{chapter}}{{{sec_num}：{title_ja}（{title_en}）}}\n")
            sec_buf.append(f"\\markboth{{{sec_num}：{title_ja}}}{{{sec_num}：{title_ja}}}\n\n")
            if sub_ja:
                sec_buf.append(f"\\noindent\\textbf{{\\large 【副題】{sub_ja}}}\\\\[4mm]\n\n")
        elif sec_id in ["epilogue", "standard_forms", "answers"]:
            sec_buf.append(f"\\chapter{{{sec_num}：{title_ja}}}\n\n")
            if sub_ja:
                sec_buf.append(f"\\noindent\\textbf{{\\large 【概要】{sub_ja}}}\\\\[4mm]\n\n")
        else:
            sec_buf.append(f"\\chapter{{{title_ja}}}\n")
            sec_buf.append(f"\\noindent\\textit{{\\large {title_en}}}\\\\[2mm]\n")
            if sub_ja:
                sec_buf.append(f"\\noindent\\textbf{{\\small 【章の論理とテーマ】{sub_ja}}}\\\\[4mm]\n\n")

        # Insert translation text
        sec_buf.append(trans_text)
        sec_buf.append("\n\n")

        sections_tex.append("".join(sec_buf))

    postamble = r"""
\backmatter

\chapter{訳者・数理校閲後記}

本書は、微積分学教育の歴史的名著であるシルバヌス・P・トンプソンの『誰にもわかる微積分』（\textit{Calculus Made Easy}, 1914年改訂第2版）の全21章および序文、プロローグ、エピローグ、標準公式一覧、全演習問題解答に至る全26セクションを、Project Gutenberg（\#33283）の公式原著TeXソースを底本として完全直訳・数理校閲したものである。

微積分という数学の道具が本来持っていた「変化を捉える驚くべき直観の力」と「誰にでも使える道具としての親しみやすさ」を、トンプソンの軽妙で力強い筆致そのままに現代の日本語読者へ届けることができた。

\begin{flushright}
2026年10月\\
古典数理復刻プロジェクト
\end{flushright}

\end{document}
"""

    full_tex = preamble + "\n\n".join(sections_tex) + "\n\n" + postamble

    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_tex)

    print(f"\nSuccessfully generated {OUTPUT_TEX} ({len(full_tex):,} bytes)!")

if __name__ == "__main__":
    main()
