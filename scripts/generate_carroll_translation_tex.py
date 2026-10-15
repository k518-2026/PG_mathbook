# -*- coding: utf-8 -*-
"""
Generate LuaLaTeX document for Lewis Carroll #4763
"The Game of Logic" (原著全4章 完全翻訳・数学校閲版)
"""

import json
import re
import os

CACHE_FILE = "books/4763_carroll_game_of_logic/carroll_full_translation_math_verified.json"
OUTPUT_TEX = "books/4763_carroll_game_of_logic/carroll_game_of_logic_translation.tex"

TITLES = {
    "I": ("第1章", "古きを捨てて新しきを（New Lamps for Old）", "命題論・三段論法・誤謬論と正方形ダイアグラムによる論理表現"),
    "II": ("第2章", "問いかけの数々（Cross Questions）", "大小ダイアグラムへの命題配置・記号解釈と演習問題体系"),
    "III": ("第3章", "歪んだ答え（Crooked Answers）", "三段論法とダイアグラム配置の詳細解答と記号論理的解法"),
    "IV": ("第4章", "当たるも八卦当たらぬも八卦（Hit or Miss）", "総合論理パズル・誤謬の看破とゲームとしての記号論理")
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

    # Clean stray OCR or translation artifacts
    text = text.replace("£", "$p$")
    text = text.replace("\\、", "、")
    text = text.replace("\\}", "}")
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

    # Replace carets and symbols outside math
    parts = re.split(r'(\$\$.*?\$\$|\$.*?\$|\\\(.*?\\\)|\\\[.*?\\\])', text, flags=re.DOTALL)
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

\definecolor{carrollred}{RGB}{120, 25, 35}
\definecolor{carrollgrey}{RGB}{80, 85, 95}
\definecolor{softpink}{RGB}{253, 246, 247}
\definecolor{darkslate}{RGB}{30, 35, 45}
\definecolor{boxframe}{RGB}{140, 50, 60}

\hypersetup{
    colorlinks=true,
    linkcolor=carrollred,
    citecolor=carrollgrey,
    urlcolor=carrollred
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

\title{\Huge\textbf{論理の遊戯}\\[4mm]
\huge\textbf{ゲームとダイアグラムで楽しむ三段論法と記号論理}\\[6mm]
\Large\textbf{—— 原著全4章 完全翻訳・数学校閲版 ——}\\[5mm]
\large 原著：ルイス・キャロル（Lewis Carroll / Charles L. Dodgson, 1887）\\[2mm]
\normalsize Project Gutenberg eBook \#4763: \textit{The Game of Logic}}

\author{\textbf{ルイス・キャロル} 著\\[2mm]
\textbf{教育情報分析研究会} 訳・数理校閲}
\date{2026年10月 校訂第1版}

\begin{document}

\maketitle

\frontmatter

\chapter*{解題：ルイス・キャロル『論理の遊戯』の数学的・論理学的意義}
\addcontentsline{toc}{chapter}{解題：ルイス・キャロル『論理の遊戯』の数学的・論理学的意義}

『不思議の国のアリス』の著者として世界中で親しまれているルイス・キャロル（本名：チャールズ・ラトウィッジ・ドジソン, 1832--1898）は、オックスフォード大学クライスト・チャーチで26年間にわたり数学講読講師（Mathematical Lecturer）を務めた本物の数学者・論理学者であった。

彼が1887年に著した『論理の遊戯』（\textit{The Game of Logic}）は、アリストテレス以来の伝統的・形式的論理学（三段論法）が持つ形式的な退屈さと難解さを一掃し、正方形のダイアグラム（盤面）と赤・灰のカウンター（駒）を用いて誰でもパズルのように論理推論を楽しめるように設計された、驚くべき先駆的著作である。

本書でキャロルが考案した二重・三重の正方形ダイアグラムは、ベン図（ジョン・ヴェン）と並び、現代のコンピュータ工学における「カルノー図（Karnaugh Map）」の原型をなすものであり、視覚的に論理の真理値や属性の包含関係を決定する画期的な手法であった。

本書は全4章から構成され、
\begin{enumerate}[label=\textbf{第\arabic*章:}]
    \item \textbf{古きを捨てて新しきを（New Lamps for Old）}：命題の本質、三段論法（Syllogism）、誤謬（Fallacies）の分類、および正方形ダイアグラムを用いた推論の基礎。
    \item \textbf{問いかけの数々（Cross Questions）}：小ダイアグラム・大ダイアグラムを用いた命題の表現と記号解釈の徹底演習問題群。
    \item \textbf{歪んだ答え（Crooked Answers）}：第2章の演習に対する詳細な模範解答と、三段論法の具体的導出プロセス。
    \item \textbf{当たるも八卦当たるぬも八卦（Hit or Miss）}：日々の生活や言語の中に潜む論理的推論と誤謬を見抜く総合論理パズル。
\end{enumerate}
を収載している。

本全訳版は、Project Gutenberg eBook \#4763として公開されている1887年初版テキストを底本とし、ローカル大規模言語モデル（\texttt{qwen2.5-7b-instruct} による忠実な翻訳および \texttt{qwen2.5-math-7b-instruct} による数理・LaTeX校閲）を駆使して完全翻訳・製本したものである。

\tableofcontents

\mainmatter
"""

    body_chapters = []
    order = ["I", "II", "III", "IV"]

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

本書は、ルイス・キャロル（チャールズ・L・ドジソン）による知られざる論理学の傑作『論理の遊戯』（\textit{The Game of Logic}, 1887）の全4章を、Project Gutenberg（\#4763）の底本に基づき完全翻訳・数理校閲したものである。

キャロルが目指したのは、堅苦しい学問としての論理学ではなく、知的な歓びとユーモアに満ちた「遊戯（ゲーム）」としての記号論理であった。ダイアグラムの上で駒を動かしながら前提から結論を導き出す快感は、130年以上を経た現代においても全く色あせることはない。

本書が、論理的思考の純粋な楽しさと、アリスの作者が持っていた鋭利な数学的知性に触れる最良の契機となることを願う。

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
