# -*- coding: utf-8 -*-
"""
Generate LuaLaTeX document for John Venn #57359
"The Logic of Chance, 3rd edition" (原著全19章 完全翻訳・数学校閲版)
"""

import json
import re
import os

CACHE_FILE = "books/57359_venn_logic_of_chance/venn_full_translation_math_verified.json"
OUTPUT_TEX = "books/57359_venn_logic_of_chance/venn_logic_of_chance_translation.tex"

ROMAN_TITLES = {
    "I": ("第1章", "確率の系列（The Series of Probability）", "頻度論の基礎・確率命題と論理命題の差異・無限系列の極限と変動"),
    "II": ("第2章", "系列の配置と形成・誤差の法則（Arrangement and Formation of the Series. Laws of Error）", "誤差法則の普遍性批判・非対称分布・最小二乗法と実在のタイプ"),
    "III": ("第3章", "系列の起源と因果の過程（Origin or Process of Causation of the Series）", "対象と作用因・自然種と自由意志・因果性の物理的基盤"),
    "IV": ("第4章", "系列の発見と証明法（How to Discover and Prove the Series）", "経験的基礎と演繹的推論・理由不十分の原理の無効性・ベルヌーイの定理の限界"),
    "V": ("第5章", "ランダム性の概念（The Conception of Randomness）", "一様分布の公理・幾何学的確率・円周率の乱数性・無作為抽出の数理"),
    "VI": ("第6章", "信念の度合いの測定（Measurement of Belief）", "主観的信念の定量化批判・サンクトペテルブルクのパラドックス・極限としての客観的確率"),
    "VII": ("第7章", "確率における推論規則（The Rules of Inference in Probability）", "加法定理・乗法定理・独立事象・逆確率（ベイズ逆推論）の仮定の恣意性批判"),
    "VIII": ("第8章", "継起の規則（The Rule of Succession）", "ラプラス継起則批判・帰納的飛躍と確率計算の峻別・心理的信念と論理"),
    "IX": ("第9章", "帰納法（Induction）", "帰納的推論と確率の境界・クラス所属の困難性・生命保険と個別事象の価値"),
    "X": ("第10章", "偶然・因果性・設計（Chance, Causation and Design）", "偶然と自然法則・自由意志統計・数値定数と設計論の数理批判"),
    "XI": ("第11章", "実質論理学と形式論理学（Material and Formal Logic）", "客観的頻度観と概念論的観点の対比・仮説検証における言語の限界"),
    "XII": ("第12章", "時間性と相対性の諸帰結（Consequences of the Previous Distinctions）", "事象生起前後の確率・時間無関係性の原則・確率の相対性批判"),
    "XIII": ("第13章", "様相論（On Modality）", "様相命題と確率・アリストテレスからカントまでの様相論・法学における証明度"),
    "XIV": ("第14章", "確率論における諸誤謬（Fallacies）", "事後判断の誤謬・無作為と作為の混同・倍額賭け（マーチンゲール）の破綻・大数の錯覚"),
    "XV": ("第15章", "保険と賭博（Insurance and Gambling）", "不確実性の低減（保険）と増大（賭博）・数学的期待値と道徳的期待値の限界"),
    "XVI": ("第16章", "証言への確率論の適用（Application of Probability to Testimony）", "証言信憑性の統計的評価・前提条件の不成立・証言連鎖の数学的分析"),
    "XVII": ("第17章", "異常な言説・奇跡の信憑性（Credibility of Extraordinary Stories）", "並外れた主張の事前確率・証人の一般的信頼度と個別信頼度・奇跡と異常の峻別"),
    "XVIII": ("第18章", "平均の性質と種類（Nature and Use of an Average, and Different Kinds of Average）", "算術平均・幾何平均・最頻値・中央値・平均二乗誤差とゴルトンの測定法"),
    "XIX": ("第19章", "真理への近似手段としての平均理論（Theory of the Average as Means of Approximation）", "誤差曲線の縮小（逆問題と順問題）・標本平均の極限分布・天文学的観測の総合")
}

def clean_latex(text):
    text = text.replace("次のように翻訳します：", "")
    text = text.replace("以下の文章を忠実に日本語に翻訳します：", "")
    text = text.replace("以下が忠実な日本語翻訳です：", "")
    text = text.replace("忠実に日本語へ翻訳いたします：", "")
    text = text.replace("以下が翻訳です：", "")

    # Clean stray OCR or translation artifacts
    text = text.replace("£", "$p$")
    text = text.replace("\\、", "、")
    text = text.replace("\\}", "}")
    text = text.replace(r"\±", r"\pm")
    text = text.replace(r"-\frac{1}{500}", r"$-\frac{1}{500}$")

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

\definecolor{vennblue}{RGB}{15, 45, 85}
\definecolor{goldaccent}{RGB}{175, 125, 20}
\definecolor{softblue}{RGB}{240, 246, 253}
\definecolor{darkslate}{RGB}{25, 40, 55}
\definecolor{boxframe}{RGB}{35, 75, 125}

\hypersetup{
    colorlinks=true,
    linkcolor=vennblue,
    citecolor=goldaccent,
    urlcolor=vennblue
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

\title{\Huge\textbf{偶然の論理}\\[4mm]
\huge\textbf{客観的頻度論と確率の論理的・物理的基礎}\\[6mm]
\Large\textbf{—— 原著第3版（全19章） 完全翻訳・数学校閲版 ——}\\[5mm]
\large 原著：ジョン・ヴェン（John Venn, 1888 / 3rd edition）\\[2mm]
\normalsize Project Gutenberg eBook \#57359: \textit{The Logic of Chance}}

\author{\textbf{ジョン・ヴェン} 著\\[2mm]
\textbf{教育情報分析研究会} 訳・数理校閲}
\date{2026年10月 校訂第1版}

\begin{document}

\maketitle

\frontmatter

\chapter*{解題：ジョン・ヴェン『偶然の論理』の歴史的射程と現代的意義}
\addcontentsline{toc}{chapter}{解題：ジョン・ヴェン『偶然の論理』の歴史的射程と現代的意義}

「ベン図（Venn Diagram）」の考案者として世界的に知られる英国の論理学者・数学者ジョン・ヴェン（John Venn, 1834--1923）が1866年に初版、1888年に決定版（第3版）を上梓した『偶然の論理』（\textit{The Logic of Chance}）は、近代確率論および統計的推論のパラダイムを根本から転換させた歴史的古典である。

18世紀から19世紀前半にかけて、確率論はラプラス（Laplace）らに代表されるように「人間の無知の尺度」あるいは「理性の信念の度合い」という主観的・認識論的立場が主流であった。これに対しヴェンは、確率は人間精神の主観的状態ではなく、客観的世界において反復される「事象の無限系列（Series of Probability）」における相対頻度の極限としてのみ科学的に定義できると主張した。この**客観的頻度論（Frequency Theory of Probability）**の確立は、のちにチャールズ・パース、リヒャルト・フォン・ミーゼス、コルモゴロフ、さらにはフィッシャーやネイマンらの現代数理統計学へと直結する大水脈となった。

本書は全3部・全19章から構成され、
\begin{enumerate}[label=\textbf{第\Roman*部:}]
    \item \textbf{確率の物理的基礎（Physical Foundations of Probability）}：系列の客観的実在性、誤差法則と実在のタイプ、因果作用、ベルヌーイの定理の適用限界、そしてランダム性の幾何学的・物理的定義（第1章〜第5章）。
    \item \textbf{論理的構築（Logical Superstructure）}：主観的信念測定の欺瞞性、サンクトペテルブルクの逆説、加法・乗法定理、ラプラス継起則批判、帰納法と確率の境界、設計論批判、様相論、およびギャンブラーの誤謬やマーチンゲールの破綻（第6章〜第14章）。
    \item \textbf{確率理論の諸応用（Various Applications）}：生命保険と賭博の経済的本質、証言の信憑性評価、奇跡・異常言説の批判的検証、そして算術平均・幾何平均・最頻値・中央値・平均二乗誤差の数理と真理への近似理論（第15章〜第19章）。
\end{enumerate}
を網羅している。

本全訳版は、Project Gutenberg eBook \#57359として公開されている1888年第3版を底本とし、ローカル大規模言語モデル（\texttt{qwen2.5-7b-instruct} による忠実な翻訳および \texttt{qwen2.5-math-7b-instruct} による数理・LaTeX校閲）を駆使して全19章を忠実に日本語全訳した決定版学術書である。

\tableofcontents

\mainmatter
"""

    body_chapters = []
    order = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX"]

    for num in order:
        key = f"Chapter_{num}"
        if key not in data:
            continue
        ch = data[key]
        ch_meta = ROMAN_TITLES.get(num, (f"第{num}章", ch.get("title_en", f"CHAPTER {num}"), ""))
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

本書は、近代頻度論確率論の不滅の金字塔であるジョン・ヴェンの主著『偶然の論理』（\textit{The Logic of Chance}, 3rd edition, 1888）の全19章を、Project Gutenberg（\#57359）の底本に基づき完全翻訳・数理校閲したものである。

ヴェンが19世紀後半に激しく主張した「客観的頻度論」は、単なる数学的モデルの提唱にとどまらず、因果性、帰納推論、言語の様相、人間の認知バイアス、保険とギャンブルの境界、そして標本平均の極限挙動に至るまで、極めて広大な科学哲学とデータサイエンスのフロンティアを切り拓いた。

ラプラスの古典的・主観的決定論と、ヴェンの客観的・経験的頻度論という二大巨星の全容を並び立つ全訳学術書として手元に置くことは、21世紀の現代においてデータとAI、そして確率的推論に向き合うすべての探求者にとって無上の知的財産となるであろう。

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
