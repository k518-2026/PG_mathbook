# -*- coding: utf-8 -*-
"""
Generate LuaLaTeX document for Poincare "Science and Hypothesis" (#37157)
Step1/2 translation (math verified) + Step3 high-school lecture + TikZ figures.
"""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIR = "books/37157_poincare_science_and_hypothesis/"
CACHE_FILE = DIR + "poincare_all_steps_cache.json"
OUTPUT_TEX = DIR + "poincare_science_and_hypothesis_intro.tex"

ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII"]

TITLES = {
    "I": "数学的推論の性質", "II": "数学的量と経験", "III": "非ユークリッド幾何学",
    "IV": "空間と幾何学", "V": "経験と幾何学", "VI": "古典力学",
    "VII": "相対運動と絶対運動", "VIII": "エネルギーと熱力学", "IX": "物理学における仮説",
    "X": "現代物理学の理論", "XI": "確率論の計算", "XII": "光学と電磁気学",
    "XIII": "電気力学とローレンツの理論",
}

# ---------------------------------------------------------------- figures
FIGS = {}

FIGS["I"] = (r"""
\begin{tikzpicture}[scale=1]
  \foreach \i in {0,1,2,3,4,5} {
    \draw[fill=blue!15,draw=blue!60!black,rotate around={-\i*8:(\i*1.5+0.3,0)}] (\i*1.5,0) rectangle (\i*1.5+0.3,1.4);
  }
  \foreach \i in {0,1,2,3,4} {
    \draw[->,thick,red!70!black] (\i*1.5+0.5,1.6) to[bend left=40] (\i*1.5+1.4,1.6);
  }
  \node[below] at (0.15,-0.1) {$P(1)$};
  \node[below] at (1.65,-0.1) {$P(2)$};
  \node[below] at (3.15,-0.1) {$P(3)$};
  \node[below] at (4.65,-0.1) {$\cdots$};
  \node[below] at (6.15,-0.1) {$P(n)$};
  \node[below] at (7.65,-0.1) {$P(n{+}1)$};
  \node[above,red!70!black] at (4,2.3) {$P(n)\Rightarrow P(n+1)$};
\end{tikzpicture}""", "数学的帰納法のドミノ倒し：最初が倒れ（$P(1)$）、$P(n)$が$P(n+1)$を倒すなら、全てが倒れる")

FIGS["II"] = (r"""
\begin{tikzpicture}
  \draw[->,thick] (-0.5,0) -- (10.5,0);
  \foreach \x/\l in {0/0,2.5/1,5/2,7.5/3,10/4} { \draw (\x,0.1)--(\x,-0.1) node[below]{$\l$}; }
  \fill[blue!25] (0,0.15) rectangle (4.1,0.5);
  \fill[red!25] (4.1,0.15) rectangle (10,0.5);
  \draw[very thick,green!50!black] (4.1,-0.5)--(4.1,1.3);
  \node at (2,0.85) {集合 $A$ ($x^2<2$)};
  \node at (7,0.85) {集合 $B$ ($x^2>2$)};
  \node[green!50!black,above] at (4.1,1.3) {切断：$\sqrt2$};
\end{tikzpicture}""", "デデキントの切断：数直線を二つの集合 $A$, $B$ に分ける切れ目が実数を定める")

FIGS["III"] = (r"""
\begin{tikzpicture}[scale=1.0]
  \draw[thick,fill=blue!5] (0,0) circle (3);
  \draw[thick,blue!70!black] (-3,0) -- (3,0);
  \draw[thick,red!70!black] (-1.5,2.598) .. controls (-0.6,0.5) and (0.6,0.5) .. (1.5,2.598);
  \draw[thick,green!50!black] (-1.5,-2.598) .. controls (-0.5,-0.9) and (0.5,-0.9) .. (1.5,-2.598);
  \fill (-1.5,2.598) circle (1.5pt); \fill (1.5,2.598) circle (1.5pt);
  \node[blue!70!black] at (0.5,0.2) {直線};
  \node at (0,-3.4) {ポアンカレ円板：円周上は無限遠};
\end{tikzpicture}""", "ポアンカレ円板モデル：円周に直交する円弧が「直線」となり、同一直線外の点を通る平行線が無数に引ける")

FIGS["IV"] = (r"""
\begin{tikzpicture}
  \begin{scope}[blend mode=multiply]
    \fill[red!35] (0,0) circle (1.6);
    \fill[blue!35] (2,0) circle (1.6);
    \fill[green!35] (1,-1.7) circle (1.6);
  \end{scope}
  \draw (0,0) circle (1.6) (2,0) circle (1.6) (1,-1.7) circle (1.6);
  \node at (-0.5,0.6) {視覚空間};
  \node at (2.5,0.6) {触覚空間};
  \node at (1,-2.6) {運動空間};
  \node at (1,-0.5) {\small 幾何学的空間};
\end{tikzpicture}""", "三つの感覚空間（視覚・触覚・運動）の重なりとして構成される幾何学的空間")

FIGS["V"] = (r"""
\begin{tikzpicture}
  \draw[thick,fill=gray!15] (0,0) rectangle (1.2,0.8);
  \node at (0.6,0.4) {物体};
  \draw[->,thick] (1.2,0.4) -- (4.2,0.4);
  \draw[->,thick,dashed] (1.2,0.4) .. controls (2.5,1.4) and (3.2,1.4) .. (4.2,1.2);
  \node[above] at (2.7,0.5) {光線};
  \draw[fill=yellow!40] (5,0.8) circle (0.35);
  \node at (5,0.1) {目};
  \node at (2.7,-0.9) {幾何学の公理は物理法則と不可分};
\end{tikzpicture}""", "剛体の運動と光の直進性：幾何学的測定は物理的対象を通じてのみ行われる")

FIGS["VI"] = (r"""
\begin{tikzpicture}[node distance=3cm]
  \node[draw,circle,fill=blue!10,minimum size=1.5cm] (F) at (90:2) {力 $F$};
  \node[draw,circle,fill=green!10,minimum size=1.5cm] (M) at (210:2) {質量 $m$};
  \node[draw,circle,fill=red!10,minimum size=1.5cm] (A) at (330:2) {加速度 $a$};
  \draw[->,thick] (F) to[bend right] node[left,font=\small]{を定める} (M);
  \draw[->,thick] (M) to[bend right] node[below,font=\small]{を定める} (A);
  \draw[->,thick] (A) to[bend right] node[right,font=\small]{を定める} (F);
  \node at (0,0) {$F=ma$};
\end{tikzpicture}""", "ニュートンの第二法則 $F=ma$ における定義の循環：力・質量・加速度は互いに規定し合う")

FIGS["VII"] = (r"""
\begin{tikzpicture}[scale=1.0]
  \draw[thick] (-2,0)--(-2,3) (2,0)--(2,3) (-2,0)--(2,0);
  \draw[blue!70!black,very thick,domain=-2:2,samples=40] plot (\x,{1.2+0.35*\x*\x});
  \fill[blue!20] (-2,0) rectangle (2,1.2);
  \fill[blue!20,domain=-2:2,samples=40] (-2,1.2) -- plot (\x,{1.2+0.35*\x*\x}) -- (2,1.2) -- cycle;
  \draw[->,thick,red!70!black] (0,3.4) arc (180:0:0.6 and 0.2);
  \node at (0,-0.5) {回転するバケツの水面：放物線 $z=\frac{\omega^2}{2g}r^2$};
\end{tikzpicture}""", "ニュートンのバケツ：水面の凹みは絶対回転の証拠か、それとも宇宙の質量への相対回転か")

FIGS["VIII"] = (r"""
\begin{tikzpicture}
  \draw[->] (0,0)--(7,0) node[right]{時刻 $t$};
  \draw[->] (0,0)--(0,3.5) node[above]{エネルギー};
  \draw[blue!70!black,very thick,domain=0:6.28,samples=60] plot (\x,{1.5+1.4*cos(\x r)});
  \draw[red!70!black,very thick,domain=0:6.28,samples=60] plot (\x,{1.5-1.4*cos(\x r)});
  \draw[green!50!black,thick,dashed] (0,3) -- (6.4,3);
  \node[blue!70!black] at (1,3.1) {位置 $U$};
  \node[red!70!black] at (3.2,0.0) [below] {運動 $K$};
  \node[green!50!black,right] at (6.4,3) {$E=K+U$};
\end{tikzpicture}""", "振り子のエネルギー保存：位置エネルギー $U$ と運動エネルギー $K$ が入れ替わっても総和 $E$ は一定")

FIGS["IX"] = (r"""
\begin{tikzpicture}
  \begin{scope}[blend mode=multiply]
    \fill[blue!30] (0,0) circle (1.7);
    \fill[red!30] (2.2,0) circle (1.7);
    \fill[green!30] (1.1,-1.9) circle (1.7);
  \end{scope}
  \draw (0,0) circle (1.7) (2.2,0) circle (1.7) (1.1,-1.9) circle (1.7);
  \node at (-0.4,0.5) {\small 検証可能};
  \node at (2.6,0.5) {\small 一般化};
  \node at (1.1,-2.7) {\small 見かけの仮説};
  \node at (1.1,-0.6) {\small 理論};
\end{tikzpicture}""", "物理学における仮説の三分類：検証可能な仮説・一般化・見かけの（便宜的）仮説")

FIGS["X"] = (r"""
\begin{tikzpicture}
  \draw[decorate,decoration={coil,aspect=0.5,segment length=4mm,amplitude=3mm}] (0,0)--(3,0);
  \draw[thick,fill=blue!20] (3,-0.5) rectangle (4.2,0.5);
  \node at (3.6,0) {$m$};
  \draw[thick] (0,-0.8)--(0,0.8);
  \draw[->,thick] (3.6,0.9)--(4.8,0.9) node[right]{$x$};
  \node at (2.2,-1.5) {$m\ddot x = -kx$ \quad 力学モデルと微分方程式の対応};
\end{tikzpicture}""", "現象論的方程式と力学モデルの対応：同じ方程式を満たす異なる力学模型が無数に存在する")

FIGS["XI"] = (r"""
\begin{tikzpicture}
  \begin{scope}
    \draw[->] (-3.2,0)--(3.4,0) node[right]{$x$};
    \draw[->] (0,0)--(0,2.7);
    \fill[blue!20,domain=-1:1,samples=40] (-1,0) -- plot (\x,{2.3*exp(-\x*\x*2)}) -- (1,0) -- cycle;
    \draw[blue!70!black,very thick,domain=-3:3,samples=60] plot (\x,{2.3*exp(-\x*\x*2)});
    \node at (0,-0.5) {正規分布};
  \end{scope}
  \begin{scope}[xshift=7cm]
    \draw[thick,fill=green!10] (0,0.8) circle (1.5);
    \foreach \i in {0,...,7} {
      \draw (0,0.8) -- ++({45*\i}:1.5);
      \node at ($(0,0.8)+({45*\i+22.5}:1.1)$) {\small \ifodd\i 黒\else 赤\fi};
    }
    \node at (0,-1.1) {ルーレット};
  \end{scope}
\end{tikzpicture}""", "偶然の数学：微小な原因の違いが巨大な結果を生み（ルーレット）、多数集まれば正規分布にしたがう")

FIGS["XII"] = (r"""
\begin{tikzpicture}
  \draw[->] (0,0)--(8.5,0) node[right]{進行方向};
  \draw[red!70!black,very thick,domain=0:8,samples=80] plot (\x,{1.2*sin(\x*90)});
  \draw[blue!70!black,very thick,dashed,domain=0:8,samples=80] plot (\x,{0.8*sin(\x*90)});
  \node[red!70!black] at (1,1.6) {電場 $\mathbf E$};
  \node[blue!70!black] at (3,-1.6) {磁場 $\mathbf B$};
\end{tikzpicture}""", "電磁波：電場と磁場が互いに直交して振動しながら光速で進む（マクスウェル方程式）")

FIGS["XIII"] = (r"""
\begin{tikzpicture}
  \draw[->] (0,0)--(7,0) node[right]{速度 $v/c$};
  \draw[->] (0,0)--(0,4) node[above]{質量 $m/m_0$};
  \draw[blue!70!black,very thick,domain=0:0.94,samples=60] plot ({6.2*\x},{1/sqrt(1-\x*\x)});
  \draw[dashed] (6.2,0)--(6.2,3.9);
  \node[below] at (6.2,0) {$1$};
  \node[left] at (0,1) {$1$};
  \node[blue!70!black] at (2.2,2) {$m=\dfrac{m_0}{\sqrt{1-v^2/c^2}}$};
\end{tikzpicture}""", "ローレンツ理論：速度が光速に近づくと見かけの質量が無限に増大する")

# ---------------------------------------------------------------- cleaning
CJK_FIX = {"验": "験", "审": "審", "证": "証", "说": "説", "实": "実", "义": "義", "论": "論",
           "几": "幾", "何": "何", "学": "学", "间": "間", "关": "関", "点": "点", "线": "線",
           "对": "対", "无": "無", "时": "時", "为": "為", "这": "この", "个": "個", "从": "から",
           "数": "数", "与": "と", "开": "開", "让": "させる", "还": "まだ", "们": "たち"}

MATH_SPLIT = re.compile(r'(\$\$.*?\$\$|\$[^$\n]*?\$|\\\(.*?\\\)|\\\[.*?\\\])', re.S)


def fix_text_part(p):
    for k, v in CJK_FIX.items():
        p = p.replace(k, v)
    p = p.replace("\\", "")
    p = p.replace("%", "\\%").replace("#", "\\#").replace("&", "\\&")
    p = p.replace("_", "\\_").replace("^", "").replace("~", "\\textasciitilde{}")
    p = p.replace("{", "\\{").replace("}", "\\}")
    p = p.replace("²", "$^2$").replace("³", "$^3$").replace("¥", "")
    p = p.replace("$", "")
    return p


def fix_math_part(m):
    for k, v in CJK_FIX.items():
        m = m.replace(k, v)
    return m


def clean_inline(text):
    """Escape plain text; keep balanced math; convert **bold**."""
    # protect math
    parts = MATH_SPLIT.split(text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # math: if it has Japanese chars, wrap them in \text
            part = fix_math_part(part)
            out.append(part)
        else:
            out.append(fix_text_part(part))
    s = "".join(out)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)\*(?!\*)', r'\\textit{\1}', s)
    s = s.replace("*", "")
    s = s.replace("`", "")
    return s


def clean_translation(text):
    for junk in ["次のように翻訳します：", "以下の文章を忠実に日本語に翻訳します：",
                 "以下に翻訳します。", "翻訳：", "了解しました。"]:
        text = text.replace(junk, "")
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return "\n\n".join(clean_inline(re.sub(r'\s*\n\s*', '', p)) for p in paras)


def md_to_latex(text):
    lines = text.split("\n")
    out = []
    in_list = False
    for ln in lines:
        s = ln.rstrip()
        st = s.strip()
        m_item = re.match(r'^(?:[\*\-]\s+|\d+\.\s+)(.*)$', st)
        if m_item:
            if not in_list:
                out.append("\\begin{itemize}[leftmargin=2em]")
                in_list = True
            out.append("\\item " + clean_inline(m_item.group(1)))
            continue
        if in_list and st == "":
            out.append("\\end{itemize}")
            in_list = False
            out.append("")
            continue
        if in_list:
            out.append("\\end{itemize}")
            in_list = False
        if re.match(r'^-{3,}$', st):
            continue
        m_h = re.match(r'^(#{1,6})\s*(.*)$', st)
        if m_h:
            title = clean_inline(m_h.group(2).replace("**", ""))
            if len(m_h.group(1)) <= 3:
                out.append("\\subsection*{" + title + "}")
            else:
                out.append("\\paragraph{" + title + "}")
            continue
        out.append(clean_inline(s) if st else "")
    if in_list:
        out.append("\\end{itemize}")
    res = "\n".join(out)
    res = re.sub(r'\n{3,}', '\n\n', res)
    return res


PREAMBLE = r"""\documentclass[a4paper,11pt,openany]{ltjsbook}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{geometry}
\geometry{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{decorations.pathmorphing,calc,positioning,arrows.meta}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{fancyhdr}

\definecolor{poinblue}{RGB}{25,55,95}
\definecolor{goldaccent}{RGB}{180,130,20}
\definecolor{softblue}{RGB}{240,245,252}
\definecolor{softgold}{RGB}{255,248,230}
\hypersetup{colorlinks=true,linkcolor=poinblue,urlcolor=poinblue}

\newtcolorbox{lecturebox}[1][]{enhanced,breakable,colback=softgold,colframe=goldaccent,
  fonttitle=\bfseries\gtfamily,title={高校生のための徹底解説講義},sharp corners,boxrule=0.8pt,
  left=10pt,right=10pt,top=8pt,bottom=8pt,#1}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

\title{\Huge\textbf{科学と仮説}\\[4mm]
\huge\textbf{数学・幾何学・物理学の基礎をめぐる省察}\\[6mm]
\Large\textbf{—— 原著全13章 日本語訳・数学校閲・高校生向け解説付 ——}\\[5mm]
\large 原著：アンリ・ポアンカレ（Henri Poincar\'e, 1902）\\[2mm]
\normalsize Project Gutenberg eBook \#37157: \textit{Science and Hypothesis}}
\author{\textbf{アンリ・ポアンカレ} 著\\[2mm]\textbf{教育情報分析研究会} 訳・数理校閲・解説}
\date{2026年10月 第1版}

\begin{document}
\maketitle
\frontmatter
\chapter*{解題：『科学と仮説』の現代的意義}
\addcontentsline{toc}{chapter}{解題：『科学と仮説』の現代的意義}

アンリ・ポアンカレ（Henri Poincar\'e, 1854--1912）の『科学と仮説』（\textit{La Science et l'Hypoth\`ese}, 1902）は、数学・物理学の基礎に潜む「約束事（規約）」と「仮説」の役割を明らかにした、科学哲学史上の古典である。非ユークリッド幾何学は真偽ではなく便利さで選ばれる「規約」であるとする規約主義、ニュートン力学の原理の循環性、エネルギー保存則、確率と偶然、さらにはローレンツ理論に始まる相対性原理の萌芽まで、20世紀物理学を準備した洞察に満ちている。

本書は、原著英訳（Project Gutenberg \#37157、全13章）を \texttt{qwen2.5-7b-instruct} で日本語訳（Step~1）し、\texttt{qwen2.5-math-7b-instruct} で数学的内容を校閲（Step~2）し、さらに \texttt{gemma4:12b} により各章に高校生にも分かる丁寧な解説講義（Step~3）と図版を付して組版したものである。

\tableofcontents
\mainmatter
"""

POST = r"""
\backmatter
\chapter{訳者・数理校閲後記}
ポアンカレは「科学は事実の集積ではなく、家が石の集積でないのと同じである」と述べた。本書の翻訳・校閲・解説は、複数の言語モデルを役割分担させるワークフローで作成した。数式や概念の細部には今後の校訂の余地がある。読者が原著の精神、すなわち「仮説を自覚的に選び取る科学の態度」を味わう一助となれば幸いである。

\begin{flushright}2026年10月\\教育情報分析研究会\end{flushright}
\end{document}
"""


def main():
    with open(CACHE_FILE, encoding="utf-8") as f:
        data = json.load(f)
    body = []
    for num in ORDER:
        key = f"Chapter_{num}"
        if key not in data:
            print("missing", key)
            continue
        ch = data[key]
        idx = ORDER.index(num) + 1
        title = TITLES[num]
        fig, cap = FIGS[num]
        topic = ch.get("topic_details", "")
        tex = f"\\chapter{{{title}}}\n\\begin{{center}}\\large\\textit{{{clean_inline(topic)}}}\\end{{center}}\n\n"
        tex += "\\section*{この章の見取り図}\n\\begin{center}\n" + fig + "\n\n\\small " + cap + "\n\\end{center}\n\n"
        tex += "\\section{原著の日本語訳}\n" + clean_translation(ch["japanese_translation"]) + "\n\n"
        tex += "\\section{高校生のための解説講義}\n\\begin{lecturebox}\n" + md_to_latex(ch["highschool_lecture"]) + "\n\\end{lecturebox}\n"
        body.append(tex)
    full = PREAMBLE + "\n\n\\clearpage\n".join(body) + POST
    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full)
    print("wrote", OUTPUT_TEX, len(full))


if __name__ == "__main__":
    main()
