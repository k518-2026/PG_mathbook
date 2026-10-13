# -*- coding: utf-8 -*-
"""
Generate LuaLaTeX document for Laplace #58881
"A Philosophical Essay on Probabilities" (全訳・数学校閲版)
"""

import json
import re

CACHE_FILE = "books/58881_laplace_probability/processed_translation_math_verified.json"
OUTPUT_TEX = "books/58881_laplace_probability/laplace_philosophical_essay_translation.tex"

ROMAN_TITLES = {
    "I": ("第1章", "序論（Introduction）", "確率論の哲学的動機と人間精神の認識論的基礎"),
    "II": ("第2章", "確率について（Concerning Probability）", "決定論的宇宙観・ラプラスの悪魔と主観的確率の定義"),
    "III": ("第3章", "確率計算の一般原理（General Principles of the Calculus）", "同等確からしさ・独立試行・条件付き確率・ベイズの逆確率（10の根本原理）"),
    "IV": ("第4章", "希望値について（Concerning Hope）", "数学的期待値と道徳的期待値（モラル・ホープ / 効用理論）"),
    "V": ("第5章", "確率計算の解析的方法（Analytical Methods）", "母関数理論・有限差分方程式・ラプラス変換と漸近積分展開"),
    "VI": ("第6章", "偶然の遊戯（Games of Chance）", "公平な賭け・破産の確率・サイコロとトランプの組合せ論"),
    "VII": ("第7章", "等しいと仮定された偶然に潜在する未知の不平等", "前提条件のゆらぎと事後検証によるベイズ的修正"),
    "VIII": ("第8章", "事象の無限回の反復から生じる極限確率法則", "大数の法則・中心極限定理・ド・モアブル＝ラプラスの定理と正規分布"),
    "IX": ("第9章", "自然哲学への確率計算の応用", "天文学的観測データの誤差論・最小二乗法・太陽系の力学的安定性"),
    "X": ("第10章", "道徳科学（人文・社会科学）への応用", "人間行動の統計法則と意思決定論への展開"),
    "XI": ("第11章", "証言の確率について（Probability of Testimonies）", "伝言連鎖による信憑性の減衰・複数証言の総合・歴史的批判"),
    "XII": ("第12章", "議会の選択と決定について（Selections of Assemblies）", "多数決原理・投票制度の数理比較（ボルダ方式とコンドルセ基準）"),
    "XIII": ("第13章", "裁判における判決の確率について", "陪審員制度・冤罪確率の最小化と法的証明度"),
    "XIV": ("第14章", "生命表・平均余命・婚姻に関する確率論", "人口動態統計・死亡率曲線・天然痘ワクチンの有効性分析"),
    "XV": ("第15章", "事象の確率に依存する制度の利益", "海上保険・生命保険・年金基金とリスク分散の数理"),
    "XVI": ("第16章", "確率評価における人間の錯覚と誤謬", "ギャンブラーの誤謬・認知バイアスと迷信の批判"),
    "XVII": ("第17章", "確実性に接近するための諸手段", "帰納法・類推・仮説検証・科学的方法論の哲学的基礎"),
    "XVIII": ("第18章", "1816年までの確率論の歴史的概観", "パスカル、フェルマー、ホイヘンスからベルヌーイ、ベイズ、ラプラスまでの展開史")
}

def clean_latex(text):
    # Fix common artifacts
    text = text.replace("次のように翻訳します：", "")
    text = text.replace("以下の文章を忠実に日本語に翻訳します：", "")
    text = text.replace("哲学的確率論への献辞", "")
    text = text.replace("確率に関する論考.", "")
    text = text.replace("確率論の計算.", "")
    text = text.replace("初等原理。", "【初等原理】")
    text = text.replace("第二の原理。", "【第2原理】")
    text = text.replace("第三の原理。", "【第3原理】")
    text = text.replace("第四原理。", "【第4原理】")
    text = text.replace("第五の原理。", "【第5原理】")
    text = text.replace("第六の原理。", "【第6原理】")
    text = text.replace("第七原理。", "【第7原理】")
    text = text.replace("第八原理。", "【第8原理】")
    text = text.replace("第九原理。", "【第9原理】")
    text = text.replace("第十原理。", "【第10原理】")

    # Fix stray OCR symbols
    text = text.replace("£", "$p$")
    text = text.replace("y\\V", "$y \\cdot v$")
    text = text.replace("、第四手では\\、", "、第四手では $\\frac{1}{8}$、")
    text = text.replace("\\、", "、")
    text = text.replace("\\}", "}")
    
    # Fix odd dollar signs / book ad artifacts
    text = text.replace("もし、$に示される関数", "もし、$T$ に示される関数")
    text = text.replace("U$      ある哲学的な確率論的 Essay.", "")
    text = text.replace("利息率が£$5\\%$である場合", "利息率が5\\%である場合")
    text = text.replace("利息率が$p$$5\\%$である場合", "利息率が5\\%である場合")
    text = text.replace(r"\±", r"\pm")
    text = text.replace(r"$p$, \\,", r"$p$, $\frac{1}{4}$,")
    text = re.sub(r'\$\d+(?:\.\d+)?', '', text) # Remove book prices like $1.75

    # Fix OCR artifacts with caret and yen outside math mode
    def clean_math_symbols(m):
        content = m.group(0)
        return content

    # Fix unbracketed frac in text
    text = text.replace(r"-\frac{1}{500}", r"$-\frac{1}{500}$")

    # Replace carets and yens that are outside math environments
    parts = re.split(r'(\$\$.*?\$\$|\$.*?\$|\\\(.*?\\\)|\\\[.*?\\\])', text, flags=re.DOTALL)
    cleaned_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            # Inside math
            cleaned_parts.append(part)
        else:
            # Outside math
            p = part.replace("^", "")
            p = p.replace("¥", "")
            p = p.replace("#", "\\#")
            p = p.replace("²", "$^2$")
            p = p.replace("³", "$^3$")
            p = p.replace("&", "\\&")
            p = p.replace("_", "\\_")
            p = p.replace("~", "\\textasciitilde{}")
            p = p.replace("验", "験") # Japanese kanji
            p = p.replace("审", "審") # Japanese kanji
            cleaned_parts.append(p)
    text = "".join(cleaned_parts)
    
    # Clean up AI preamble remnants
    text = re.sub(r'この翻訳では、原著の論理構造と語調を尊重しつつ[^\n]+\n', '', text)
    
    # Fix any dangling single backslashes before punctuation or Japanese chars
    text = re.sub(r'\\(?=[\u3000-\u9fff\uff00-\uffef、。・])', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def main():
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

\definecolor{laplaceblue}{RGB}{20, 50, 90}
\definecolor{goldaccent}{RGB}{180, 130, 20}
\definecolor{softblue}{RGB}{240, 245, 252}
\definecolor{darkslate}{RGB}{30, 45, 60}
\definecolor{boxframe}{RGB}{40, 80, 130}

\hypersetup{
    colorlinks=true,
    linkcolor=laplaceblue,
    citecolor=goldaccent,
    urlcolor=laplaceblue
}

\newtcolorbox{mathreviewbox}[2][]{
    enhanced,
    breakable,
    colback=softblue,
    colframe=boxframe,
    fonttitle=\bfseries\gtfamily,
    title={#2},
    sharp corners,
    boxrule=0.8pt,
    left=10pt, right=10pt, top=8pt, bottom=8pt,
    #1
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

\title{\Huge\textbf{確率の哲学的試論}\\[4mm]
\huge\textbf{決定論的宇宙観と確率計算の全体系}\\[6mm]
\Large\textbf{—— 原著全18章 完全翻訳・数学校閲版 ——}\\[5mm]
\large 原著：ピエール＝シモン・ラプラス（Pierre-Simon Laplace, 1814）\\[2mm]
\normalsize Project Gutenberg eBook \#58881: \textit{A Philosophical Essay on Probabilities}}

\author{\textbf{ピエール＝シモン・ラプラス} 著\\[2mm]
\textbf{教育情報分析研究会} 訳・数理校閲}
\date{2026年10月 校訂第1版}

\begin{document}

\maketitle

\frontmatter

\chapter*{解題：『確率の哲学的試論』の現代的意義}
\addcontentsline{toc}{chapter}{解題：『確率の哲学的試論』の現代的意義}

ピエール＝シモン・ラプラス（Pierre-Simon, marquis de Laplace, 1749--1827）が1814年に発表した『確率の哲学的試論』（\textit{Essai philosophique sur les probabilités}）は、彼が著した金字塔的巨著『確率の解析的理論』（\textit{Théorie analytique des probabilités}, 1812）の序論として講義された内容を発展させた、数学史上屈指の古典的著作である。

本書は高度な微積分や差分方程式の展開を伴う『解析的理論』のエッセンスを、あらゆる学問的探求者、哲学者、市民に向けて言葉で説き明かした傑作であり、同時に近代科学における「決定論（いわゆるラプラスの悪魔）」の宣言書としても世界史にその名を刻んでいる。

本書の特徴は、コイン投げやサイコロといった偶然の遊戯から出発しながら、条件付き確率、原因の確率（ベイズの定理）、大数の法則、中心極限定理、最小二乗法、そして天文学、測地学、気象学、生命表、保険制度、裁判の陪審員判決、議会の投票理論、さらには人間の認知的錯覚（バイアス）に至るまで、確率論が人間社会と自然認識の全領域を照らす普遍的道具であることを実証した点にある。

本版は、Project Gutenberg（eBook \#58881）として公開されているF.~W.~トラスコットおよびF.~L.~エモリーによる英訳決定版を底本とし、現代的な数理モデル（\texttt{qwen2.5-7b-instruct} による忠実な翻訳および \texttt{qwen2.5-math-7b-instruct} による数理・LaTeX検証）の厳密な照合を経て、全18章の完全翻訳として組版・製本されたものである。

\tableofcontents

\mainmatter
"""

    body_chapters = []
    
    order = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII"]
    
    for num in order:
        key = f"Chapter_{num}"
        if key not in data:
            continue
        ch = data[key]
        ch_meta = ROMAN_TITLES.get(num, (f"第{num}章", ch["title_en"], ""))
        ch_title = f"{ch_meta[1]}"
        ch_subtitle = ch_meta[2]
        
        ja_text = clean_latex(ch["japanese_translation"])
        
        # Format paragraphs into LaTeX paragraphs
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

本書は、ピエール＝シモン・ラプラスによる不朽の名著『確率の哲学的試論』（1814年）の全18章を、Project Gutenberg（\#58881）の底本に基づき完全翻訳・数学校閲したものである。

原著者が序論で力説するように、「人間の知識のほとんどすべては確率的である」。ラプラスが200年前に構想した決定論的宇宙観と、不完全な情報のもとで推論を行うための「原因の確率（ベイズの逆確率）」、「大数の法則」、「母関数法」、「最小二乗法」の体系は、現代のデータサイエンス、機械学習、ベイズ統計学、金融工学、認知科学の礎石そのものである。

本全訳版が、確率論の哲学的源流と数理的精緻さを同時に味わうための貴重な道標となることを願ってやまない。

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
