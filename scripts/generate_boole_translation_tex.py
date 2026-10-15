# -*- coding: utf-8 -*-
"""
Generate LuaLaTeX document for George Boole #15114
"An Investigation of the Laws of Thought" (原著全22章 完全翻訳・数学校閲版)
"""

import json
import re
import os

CACHE_FILE = "books/15114_boole_laws_of_thought/boole_full_translation_math_verified.json"
OUTPUT_TEX = "books/15114_boole_laws_of_thought/boole_laws_of_thought_translation.tex"

TITLES = {
    "I": ("第1章", "本研究の性質と構想（Nature and Design of this Work）", "精神の思考法則の探究・数学的論理学の基礎・言語と記号の哲学的役割"),
    "II": ("第2章", "記号全般および論理学に特有の記号について（Signs and their Laws）", "名辞記号・結合記号（＋, －）・積記号・交換法則・分配法則とべき等律 $x^2 = x$"),
    "III": ("第3章", "思考の演算法則からの論理記号法則の演繹（Derivation of the Laws）", "二値代数の公理系・排中律と無矛盾律・0と1の宇宙的解釈"),
    "IV": ("第4章", "一次命題および二次命題への分類（Division of Propositions）", "事物の関係を表す一次命題と命題間の真偽関係を表す二次命題の構造"),
    "V": ("第5章", "記号的推論の根本原理と展開理論（Principles of Symbolic Reasoning）", "ブール展開定理 $f(x) = f(1)x + f(0)(1-x)$・係数の代数的解釈"),
    "VI": ("第6章", "論理方程式の一般的解釈法（Of Interpretation）", "未知記号の陽的表現・分数形係数 $\\frac{1}{0}, \\frac{0}{0}$ の完全な論理的意味"),
    "VII": ("第7章", "消去理論（Of Elimination）", "連立論理方程式からの媒介変数の完全消去法・論理的帰結の純化"),
    "VIII": ("第8章", "命題体系の還元法（Of Reduction）", "連立方程式の単一方程式への還元 $V = 0$・二乗和と同値性"),
    "IX": ("第9章", "記号計算の省略法・簡便法（Methods of Abbreviation）", "対称性・同値変形・論理式の計算量削減アルゴリズム"),
    "X": ("第10章", "完全なる論理体系の条件（Conditions of a Perfect Method）", "記号的手法の普遍性・形式的一貫性と論理的必然性"),
    "XI": ("第11章", "二次命題とその記号表現（Of Secondary Propositions）", "時間・条件・仮言命題のブール代数的定式化"),
    "XII": ("第12章", "二次命題の処理法（Methods in Secondary Propositions）", "仮言的三段論法・選言的三段論法の代数方程式解法"),
    "XIII": ("第13章", "サミュエル・クラークおよびスピノザの哲学的論証の分析（Clarke and Spinoza）", "存在論的証明・神の必然的実在性・スピノザ『エチカ』の記号論理的厳密批判"),
    "XIV": ("第14章", "還元法による方程式体系の分析実例（Example of Analysis）", "複合的論理条件の完全還元と具体的演繹の展開"),
    "XV": ("第15章", "アリストテレス論理学とその現代的拡張の批判的検討（Aristotelian Logic）", "伝統的三段論法全式のブール代数による完全包摂と限界の超越"),
    "XVI": ("第16章", "確率論の基礎理論（On the Theory of Probabilities）", "論理学から確率論への自然な架橋・事象の代数と確率測度"),
    "XVII": ("第17章", "確率論における一般解法の証明（General Method in Probabilities）", "任意条件付き確率問題の代数方程式体系への帰着定理"),
    "XVIII": ("第18章", "一般解法の初等的実例（Elementary Illustrations）", "独立試行・排反事象・複合事象の確率計算の検証"),
    "XIX": ("第19章", "統計的条件と極限不等式（Of Statistical Conditions）", "経験的データ間の論理的不等式・確率の上下限決定法"),
    "XX": ("第20章", "原因と結果の連鎖に関する問題（Problems on Causes）", "原因の確率・観測結果からの事後推論・ベイズ逆確率の代数的再構築"),
    "XXI": ("第21章", "判断・陪審・証言の確率への特殊応用（Probability of Judgements）", "裁判官・陪審員の合議・複数証言の信憑性と冤罪確率"),
    "XXII": ("第22章", "科学の本質と人間の知性の構造について（Constitution of the Intellect）", "数学的論理学が照らし出す人間精神の認識論的本質と哲学的展望")
}

def clean_latex(text):
    # Strip any AI preamble lines about translation
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

    # Remove or clean textgreek macros from original Greek citations
    text = re.sub(r'\\textgreek\{[^}]*\}', '〔ギリシャ語原典引用〕', text)

    # Clean stray OCR or translation artifacts
    text = text.replace("£", "$p$")
    text = text.replace("\\、", "、")
    text = text.replace(r"\±", r"\pm")
    text = text.replace(r"-\frac{1}{500}", r"$-\frac{1}{500}$")

    # Simplified Chinese to Japanese kanji mapping
    kanji_map = {
        '储': '儲', '质': '質', '转': '転', '误': '誤', '产': '産',
        '计': '計', '设': '設', '读': '読', '对': '対', '电': '電',
        '标': '標', '录': '録', '错': '錯', '识': '識', '损': '損',
        '盘': '盤', '备': '備', '码': '碼', '员': '員', '进': '進',
        '观': '観', '类': '類', '态': '態', '规': '規', '则': '則'
    }
    for k, v in kanji_map.items():
        text = text.replace(k, v)

    # Fix nested display math: \[ \begin{equation} ... \end{equation} \]
    text = re.sub(r'\\\[\s*(1\s*-\s*x\s*を[\s\S]*?\\setcounter\{equation\}\{0\})', r'1 - x を $\\bar{x}$、1 - y を $\\bar{y}$ などと簡略化して表すと、最後の3つの方程式から\n\\setcounter{equation}{0}', text)
    text = re.sub(r'\\\[\s*(\\begin\{(?:eqnarray\*?|equation\*?|align\*?|gather\*?|multline\*?)\})', r'\1', text)
    text = re.sub(r'(\\end\{(?:eqnarray\*?|equation\*?|align\*?|gather\*?|multline\*?)\})\s*\\\]', r'\1', text)
    text = re.sub(r'\$\$\s*(\\begin\{(?:split|align\*?|gather\*?|multline\*?)\}[\s\S]*?\\end\{(?:split|align\*?|gather\*?|multline\*?)\})\s*\$\$', r'\\[\n\1\n\\]', text)

    # Fix unclosed \left before \\ in multline / align
    text = text.replace(r"\left\{ ww'(1-v) + (1-v)(1-v')(1-w) \\", r"\bigl\{ ww'(1-v) + (1-v)(1-v')(1-w) \\")
    text = text.replace(r"+ v'(1-w)(1-w') \right\}", r"+ v'(1-w)(1-w') \bigr\}")

    # Fix % inside Greek citation
    text = text.replace(r'%\delta\acute{\iota}\kappa\alpha\iota\alpha$', r'\delta\acute{\iota}\kappa\alpha\iota\alpha$')

    # Fix excessive ampersands in eqnarray
    text = text.replace(r'\therefore \quad & & w (1 - sr) + sr (1 - w) z + w (1 - s) (1 - z) &=& 0.', r'\therefore \quad w (1 - sr) + sr (1 - w) z + w (1 - s) (1 - z) &=& 0.')

    # Fix unclosed \text{'s$ in Chapter XV
    text = text.replace(r"Y\text{'s$, 一部の $Y\text{'s$; または否定的な形で現れる可能性があり、すべての非-$Y\text{'s}$, 部分的に非-$Y\text{'s$ である", r"$Y$'s, 一部の $Y$'s; または否定的な形で現れる可能性があり、すべての非-$Y$'s, 部分的に非-$Y$'s である")
    text = text.replace(r"\text{'s$", r"'s$")
    text = text.replace(r"Y\text{'s}$", r"Y$'s")
    text = text.replace(r"Y\text{'s}", r"Y$'s")

    # Fix ampersand inside braces in eqnarray
    text = text.replace(r'x - \{xz (1 - y) &+& xy (1 - z)\};', r'x - xz (1 - y) &-& xy (1 - z);')

    # Fix undefined Proposition environment from AI notes in Chapter XVII
    text = re.sub(r'\\begin\{Proposition\}\{[^}]*\}\{[^}]*\}[\s\S]*?11\.\s*', r'\\textbf{命題 III. 11.} ', text)

    # Fix Chapter XXI equation tag
    text = text.replace(r'kx^i(1-x)^{n-i} + (1-k)x^{n-i}(1-x)^i \right\}. \tag{3}', r'kx^i(1-x)^{n-i} + (1-k)x^{n-i}(1-x)^i \right\}.')

    # Fix array with Japanese characters
    text = text.replace(r'\text{「原因」}& $A_1$ & \text{「存在するとき、事象」}& $E$ & \text{「生じる」；}\\', r'\text{「原因」 $A_1$ が存在するとき、事象 $E$ が生じる；}\\')
    text = re.sub(r"''\s*&\s*\$A_2\$\s*&\s*''\s*&\s*\$E\$\s*&\s*''\s*\\\\", r"\\text{「原因」 $A_2$ が存在するとき、事象 $E$ が生じる；}\\\\", text)
    text = re.sub(r"''\s*&\s*\$A_n\$\s*&\s*''\s*&\s*\$E\$\s*&\s*''", r"\\text{「原因」 $A_n$ が存在するとき、事象 $E$ が生じる；}", text)

    # Fix \begin{array}{c|cc} having too many columns (&)
    text = re.sub(r'\\begin\{array\}\{[^}]*\}', r'\\begin{array}{cccccc}', text)

    # Fix \\&c. -> 等
    text = text.replace(r'\&c.', '等')
    text = text.replace(r'\\&c.', '等')
    text = text.replace(r'&c.', '等')

    # Replace carets and symbols outside math and tabular environments
    env_list = r'eqnarray\*?|equation\*?|align\*?|gather\*?|multline\*?|array|tabular\*?'
    math_pattern = rf'(\\begin\{{(?:{env_list})\}}[\s\S]*?\\end\{{(?:{env_list})\}}|\$\$.*?\$\$|\$.*?\$|\\\(.*?\\\)|\\\[.*?\\\])'
    parts = re.split(math_pattern, text, flags=re.DOTALL)
    cleaned_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            cleaned_parts.append(part)
        else:
            p = part.replace("^", "")
            p = p.replace("¥", "")
            p = p.replace("#", "\\#")
            p = p.replace("²", "$^2$")
            p = p.replace("³", "$^3$")
            p = p.replace("&", "\\&")
            p = p.replace("_", "\\_")
            p = p.replace("~", "\\textasciitilde{}")
            p = p.replace("验", "験")
            p = p.replace("审", "審")
            p = p.replace("概率", "確率")
            cleaned_parts.append(p)
    text = "".join(cleaned_parts)

    # Clean up single backslashes before Japanese chars
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
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{fancyhdr}

\definecolor{boolegreen}{RGB}{20, 60, 45}
\definecolor{goldaccent}{RGB}{180, 130, 20}
\definecolor{softgreen}{RGB}{242, 248, 244}
\definecolor{darkslate}{RGB}{25, 40, 35}
\definecolor{boxframe}{RGB}{35, 90, 70}

\hypersetup{
    colorlinks=true,
    linkcolor=boolegreen,
    citecolor=goldaccent,
    urlcolor=boolegreen
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

\title{\Huge\textbf{思考の法則}\\[4mm]
\huge\textbf{論理と確率の数学的理論の基礎に関する探究}\\[6mm]
\Large\textbf{—— 原著全22章 完全翻訳・数学校閲版 ——}\\[5mm]
\large 原著：ジョージ・ブール（George Boole, 1854）\\[2mm]
\normalsize Project Gutenberg eBook \#15114: \textit{An Investigation of the Laws of Thought}}

\author{\textbf{ジョージ・ブール} 著\\[2mm]
\textbf{教育情報分析研究会} 訳・数理校閲}
\date{2026年10月 校訂第1版}

\begin{document}

\maketitle

\frontmatter

\chapter*{解題：ジョージ・ブール『思考の法則』の現代的射程と不滅の金字塔}
\addcontentsline{toc}{chapter}{解題：ジョージ・ブール『思考の法則』の現代的射程と不滅の金字塔}

1854年に英国クイーンズ・カレッジ・コークの初代数学教授ジョージ・ブール（George Boole, 1815--1864）が著した『思考の法則』（\textit{An Investigation of the Laws of Thought on Which Are Founded the Mathematical Theories of Logic and Probabilities}）は、アリストテレス以来2000年間定性的な言葉の学問にとどまっていた論理学を、完全に厳密な代数学の体系へと昇華させた数学史・科学哲学史上最大の金字塔である。

ブールが打ち立てた画期的な原理は、人間の思考の根本規則を「二値代数（$x^2 = x$）」という簡潔極まる方程式に集約した点にある。この「ブール代数（Boolean Algebra）」は、1930年代にクロード・シャノンによってスイッチング回路理論と結びつけられ、すべての現代コンピュータ、デジタル集積回路、プログラミング言語、人工知能のアーキテクチャの直接の礎石となった。

本書は単なる記号論理学の教科書にとどまらず、論理学と確率論の深遠な結合を追求した壮大な体系であり、全22章を通じて：
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{論理の代数学的基礎}：名辞記号、結合記号（$+$、$-$）、積記号、交換法則・分配法則、そして根本のべき等律 $x^2 = x$（第1章〜第3章）。
    \item \textbf{命題論と展開・解釈の一般理論}：一次命題と二次命題の分類、ブール展開定理 $f(x) = f(1)x + f(0)(1-x)$、分数形係数 $\frac{1}{0}, \frac{0}{0}$ の完全な論理的解釈法（第4章〜第6章）。
    \item \textbf{消去法・還元法と哲学批判}：連立論理方程式からの変数の完全消去法、単一方程式への還元、およびスピノザ『エチカ』やサミュエル・クラークの神の存在論的論証に対する記号論理的厳密批判（第7章〜第15章）。
    \item \textbf{確率の代数方程式体系}：論理学から確率論への架橋、事象の代数、一般解法の厳密な証明、統計的不等式、原因の確率（ベイズ逆推論の再構築）、裁判と陪審の判定確率、そして人間の知性の構造に関する認識論的総括（第16章〜第22章）。
\end{enumerate}
を網羅している。

本全訳版は、Project Gutenberg eBook \#15114の公式原著TeXテキストを底本とし、ローカル大規模言語モデル（\texttt{qwen2.5-7b-instruct} による忠実な翻訳および \texttt{qwen2.5-math-7b-instruct} による数理・LaTeX校閲）を駆使して全22章を完全に日本語翻訳した決定版学術書である。

\tableofcontents

\mainmatter
"""

    body_chapters = []
    order = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII"]

    for num in order:
        key = f"Chapter_{num}"
        if key not in data:
            continue
        ch = data[key]
        ch_meta = TITLES.get(num, (f"第{num}章", ch.get("title_en", f"CHAPTER {num}"), ""))
        ch_title = f"{ch_meta[1]}"
        ch_subtitle = ch_meta[2]

        ja_text = clean_latex(ch["japanese_translation"])

        paragraphs = ja_text.split("\n\n")
        latex_paragraphs = []
        for p in paragraphs:
            p = p.strip()
            if not p:
                continue
            latex_paragraphs.append(p)

        chapter_tex = f"""\\chapter{{{ch_title}}}
\\label{{ch:{num.lower()}}}

\\begin{{center}}
\\large\\textit{{{ch_subtitle}}}
\\end{{center}}
\\vspace{{4mm}}

""" + "\n\n".join(latex_paragraphs)

        body_chapters.append(chapter_tex)

    postamble = r"""
\backmatter

\chapter{訳者・数理校閲後記}

本書は、近代情報科学・デジタル文明の精神的始祖であるジョージ・ブールの主著『思考の法則』（\textit{An Investigation of the Laws of Thought}, 1854）の全22章を、Project Gutenberg（\#15114）の底本に基づき完全翻訳・数理校閲したものである。

ブールが提示した「論理とは計算である」という洞察は、170年の時を経て、現代の半導体チップ、プログラミング言語、検索エンジン、そして巨大なAIモデルの根底を貫く普遍的原理となった。

本書の全訳版が、論理と確率の数学的源流に触れ、人間精神の思考の深遠さに思いを馳せるすべての探求者にとってかけがえのない道標となることを願ってやまない。

\begin{flushright}
2026年10月\\
教育情報分析研究会
\end{flushright}

\end{document}
"""

    full_tex = preamble + "\n\n" + "\n\n\\newpage\n\n".join(body_chapters) + "\n\n" + postamble

    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_tex)

    print(f"Successfully generated {OUTPUT_TEX} ({len(full_tex)} characters)!")

if __name__ == "__main__":
    main()
