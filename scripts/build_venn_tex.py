import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

BOOK_DIR = 'e:/GoogleAntigravity/PG_mathbook/books/57359_venn_logic_of_chance'
CACHE_FILE = os.path.join(BOOK_DIR, 'gemma_generated_cache.json')
TEX_FILE = os.path.join(BOOK_DIR, 'venn_logic_of_chance_intro.tex')

with open(CACHE_FILE, 'r', encoding='utf-8') as f:
    cache = json.load(f)

def tex_escape(text):
    lines = text.split('\n')
    res = []
    for line in lines:
        line = line.strip()
        if not line:
            res.append('')
            continue
        if line.startswith('### '):
            res.append(r'\subsubsection*{' + line[4:].strip() + '}')
        elif line.startswith('## '):
            res.append(r'\subsection*{' + line[3:].strip() + '}')
        elif line.startswith('# '):
            res.append(r'\subsection*{' + line[2:].strip() + '}')
        elif line.startswith('*   ') or line.startswith('-   '):
            res.append(r'\begin{itemize}\item ' + line[4:].strip() + r'\end{itemize}')
        else:
            parts = line.split('**')
            if len(parts) > 1:
                new_line = ""
                for i, p in enumerate(parts):
                    if i % 2 == 1:
                        new_line += r"\textbf{" + p + "}"
                    else:
                        new_line += p
                line = new_line
            res.append(line)
    return '\n\n'.join(res)

foreword_txt = tex_escape(cache['foreword'])
ch1_intro_txt = tex_escape(cache['ch1_intro'])
ch1_col_txt = tex_escape(cache['ch1_column'])
ch2_intro_txt = tex_escape(cache['ch2_intro'])
ch2_col_txt = tex_escape(cache['ch2_column'])
ch3_intro_txt = tex_escape(cache['ch3_intro'])
ch3_col_txt = tex_escape(cache['ch3_column'])
ch4_intro_txt = tex_escape(cache['ch4_intro'])
ch4_col_txt = tex_escape(cache['ch4_column'])
ch5_intro_txt = tex_escape(cache['ch5_intro'])
ch5_col_txt = tex_escape(cache['ch5_column'])
ch6_intro_txt = tex_escape(cache['ch6_intro'])
ch6_col_txt = tex_escape(cache['ch6_column'])
afterword_txt = tex_escape(cache['afterword'])

tex_content = r"""\documentclass[11pt,a4paper,openany]{ltjsbook}

% ====================================================================
% パッケージ設定
% ====================================================================
\usepackage{luatexja}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{top=28mm,bottom=28mm,left=25mm,right=25mm}

\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc,shapes,backgrounds,patterns}

\usepackage[most]{tcolorbox}
\usepackage[hidelinks,pdfusetitle]{hyperref}

% ====================================================================
% スタイル＆カラー定義
% ====================================================================
\definecolor{primaryblue}{RGB}{20, 80, 110}
\definecolor{accentgreen}{RGB}{20, 120, 80}
\definecolor{warmamber}{RGB}{180, 95, 20}
\definecolor{softpurple}{RGB}{100, 50, 120}

% ヴェンの原典引用ボックス
\newtcolorbox{vennbox}[1][]{
  colback=primaryblue!6!white,
  colframe=primaryblue!85!black,
  fonttitle=\bfseries\sffamily,
  title={【ヴェンの言葉】John Venn's Original Insight},
  arc=3mm,
  boxrule=1.2pt,
  left=4mm,right=4mm,top=3mm,bottom=3mm,
  #1
}

% Gemma先生の語りかけボックス
\newtcolorbox{gammabox}[1][]{
  colback=accentgreen!6!white,
  colframe=accentgreen!85!black,
  fonttitle=\bfseries\sffamily,
  title={【Gemma先生の語りかけ】データの海へ漕ぎ出そう},
  arc=3mm,
  boxrule=1.2pt,
  left=4mm,right=4mm,top=3mm,bottom=3mm,
  #1
}

% 探究コラムボックス
\newtcolorbox{columnbox}[1][]{
  colback=warmamber!6!white,
  colframe=warmamber!85!black,
  fonttitle=\bfseries\sffamily,
  title={【探究コラム】高校生のための数理エッセイ},
  arc=3mm,
  boxrule=1.2pt,
  left=4mm,right=4mm,top=3mm,bottom=3mm,
  #1
}

% 例題＆演習ボックス
\newtcolorbox{exambox}[1]{
  colback=softpurple!5!white,
  colframe=softpurple!80!black,
  fonttitle=\bfseries\sffamily,
  title={例題：#1},
  arc=2mm,
  boxrule=1pt,
  left=3.5mm,right=3.5mm,top=2.5mm,bottom=2.5mm
}

% 定理・公式ボックス
\newtcolorbox{formulabox}[1]{
  colback=white,
  colframe=primaryblue!70!black,
  fonttitle=\bfseries\sffamily,
  title={重要公式・定義：#1},
  arc=2mm,
  boxrule=1pt,
  left=3.5mm,right=3.5mm,top=2.5mm,bottom=2.5mm
}

% ====================================================================
% タイトル情報（著者は教育情報分析研究会）
% ====================================================================
\title{
  \vspace{-10mm}
  {\Huge\bfseries\sffamily 高校生のためのヴェン確率論入門}\\[4mm]
  {\Large\sffamily 『偶然の論理』とヴェン図でひもとく客観的データと統計の科学}\\[8mm]
  {\color{primaryblue}\rule{12cm}{1.5pt}}\\[2mm]
  {\small\itshape Project Gutenberg Classic Mathematics Collection}\\[-2mm]
  {\color{primaryblue}\rule{12cm}{0.5pt}}
}
\author{
  \textbf{教育情報分析研究会}\\[2mm]
  {\small （原著：ジョン・ヴェン \textit{The Logic of Chance, 3rd ed.} / Project Gutenberg \#57359）}
}
\date{2026年10月 制版}

\begin{document}

\maketitle

% ====================================================================
% まえがき
% ====================================================================
\frontmatter

\chapter*{まえがき：ヴェン図の生みの親が遺した、もう一つの大傑作}
\addcontentsline{toc}{chapter}{まえがき}

""" + foreword_txt + r"""

\bigskip
高校数学Aの教科書を開くと、最初に登場する親しみ深い図鑑——それが円の重なり合いで集合を表す「ヴェン図（Venn Diagram）」です。この図を考案したイギリスの論理学者ジョン・ヴェン（John Venn, 1834--1923）が、生涯をかけて打ち立てたもう一つの記念碑的業績こそが、1866年に初版が出版された名著『偶然の論理』（\textit{The Logic of Chance}、Project Gutenberg EBook \#57359）です。

前作『高校生のためのラプラス確率・統計入門』で紹介したラプラスの「主観的・信念」に基づく確率に対し、ヴェンは「客観的な事実とデータの系列（頻度主義）」というまったく新しい視点で確率を再定義しました。現代のデータサイエンス、AIの機械学習、そして高校数学B・Cの「統計的な推測」の真のルーツがここにあります。

\tableofcontents

\mainmatter

% ====================================================================
% 第1章
% ====================================================================
\chapter{ヴェン図の生みの親が挑んだ謎 —— 「確率」とは心の確信か、客観的事実か？}

\begin{vennbox}
\textit{“Probability has been much too often regarded as a mere measure of belief, whereas it is essentially concerned with the facts of the outer world as shown by the statistical series.”}\\
\hfill —— John Venn, \textit{The Logic of Chance}, Introduction
\tcblower
【日本語訳】「確率はあまりにも長い間、単なる『心の確信の度合い』として扱われすぎてきた。しかし確率は本質的に、統計的系列が示す外の世界の客観的事実に関わるものなのである。」
\end{vennbox}

\section{主観的確率から客観的頻度論へのパラダイムシフト}

\begin{gammabox}
""" + ch1_intro_txt + r"""
\end{gammabox}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.95]
  % 3つの集合のヴェン図
  \draw[thick, fill=gray!8] (-3.8,-3.2) rectangle (3.8,3.2);
  \node at (3.4, 2.8) {$U$ (全体集合)};
  
  \coordinate (A) at (-1, 0.8);
  \coordinate (B) at (1, 0.8);
  \coordinate (C) at (0, -0.8);
  
  \fill[primaryblue!15] (A) circle (1.8);
  \fill[accentgreen!15] (B) circle (1.8);
  \fill[warmamber!15] (C) circle (1.8);
  
  \draw[thick, primaryblue] (A) circle (1.8);
  \draw[thick, accentgreen] (B) circle (1.8);
  \draw[thick, warmamber] (C) circle (1.8);
  
  \node at (-1.8, 1.8) {\textbf{$A$}};
  \node at (1.8, 1.8) {\textbf{$B$}};
  \node at (0, -2.4) {\textbf{$C$}};
  
  \node at (0, 0.2) {\small $A \cap B \cap C$};
  \node at (0, 1.4) {\footnotesize $A \cap B$};
  \node at (-1.1, -0.4) {\footnotesize $A \cap C$};
  \node at (1.1, -0.4) {\footnotesize $B \cap C$};
\end{tikzpicture}
\caption{ジョン・ヴェンが考案した3集合のヴェン図：論理の重なり合いを視覚化する革命}
\end{figure}

\begin{columnbox}
""" + ch1_col_txt + r"""
\end{columnbox}

% ====================================================================
% 第2章
% ====================================================================
\chapter{無限の系列と相対度数 —— 頻度主義確率の誕生}

\begin{vennbox}
\textit{“When we say that the probability of a coin falling head is one-half, we mean that in the long run the proportion of heads to whole throws will tend towards this fractional limit.”}\\
\hfill —— John Venn, \textit{The Logic of Chance}, Chapter I
\tcblower
【日本語訳】「コインの表が出る確率が2分の1であると言うとき、私たちが意味しているのは、無限に試行を続けた極限において、全投てき回数に対する表の割合がこの値へと近づくということである。」
\end{vennbox}

\section{「確率系列」と統計的規則性}

\begin{gammabox}
""" + ch2_intro_txt + r"""
\end{gammabox}

\begin{formulabox}{頻度主義的確率（統計的確率）の定義}
ある試行を $n$ 回繰り返したとき、事象 $A$ が起きた回数を $r_n$ とする。試行回数 $n$ を限りなく大きくしたとき、相対度数 $\dfrac{r_n}{n}$ が一定の値 $p$ に近づくならば、この極限値 $p$ を事象 $A$ の確率と定義する：
\[
P(A) = \lim_{n \to \infty} \frac{r_n}{n} = p
\]
\end{formulabox}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.95]
  \draw[thick, ->] (0,0) -- (10.5,0) node[right] {$n$ (投てき回数)};
  \draw[thick, ->] (0,0) -- (0,4.2) node[above] {相対度数 $\frac{r_n}{n}$};
  
  % y=0.5 の基準線
  \draw[dashed, red, line width=1.2pt] (0, 2) -- (10, 2) node[right] {$p = 0.5$};
  
  % 相対度数の収束プロット
  \draw[line width=1.1pt, primaryblue] 
    (0.2, 3.8) -- (0.5, 1.2) -- (1.0, 2.7) -- (1.5, 1.6) -- (2.0, 2.4) --
    (3.0, 1.8) -- (4.0, 2.2) -- (5.0, 1.9) -- (6.5, 2.08) -- (8.0, 1.96) -- (10.0, 2.01);
    
  \node[circle, fill=primaryblue, inner sep=1.5pt] at (10.0, 2.01) {};
  \node[below] at (1, 0) {\small 10};
  \node[below] at (3, 0) {\small 50};
  \node[below] at (6, 0) {\small 200};
  \node[below] at (10, 0) {\small 1000回};
  
  \node[left] at (0, 2) {\small $0.5$};
  \node[left] at (0, 4) {\small $1.0$};
\end{tikzpicture}
\caption{コイン投げにおける試行回数 $n$ の増大と、相対度数の $0.5$ への収束プロセス}
\end{figure}

\begin{columnbox}
""" + ch2_col_txt + r"""
\end{columnbox}

% ====================================================================
% 第3章
% ====================================================================
\chapter{ランダムとは何か？ —— 「偶然」の幾何学と落とし穴}

\begin{vennbox}
\textit{“Randomness cannot be postulated in the abstract without reference to some definite physical framework or geometrical area.”}\\
\hfill —— John Venn, \textit{The Logic of Chance}, Chapter V
\tcblower
【日本語訳】「ランダムさ（無作為性）とは、明確な物理的枠組みや幾何学的領域への言及なしに、抽象的に仮定することはできない。」
\end{vennbox}

\section{幾何学的確率と一様分布}

\begin{gammabox}
""" + ch3_intro_txt + r"""
\end{gammabox}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.95]
  % 平行線
  \draw[thick, gray] (-4, 2) -- (4, 2);
  \draw[thick, gray] (-4, 0) -- (4, 0);
  \draw[thick, gray] (-4, -2) -- (4, -2);
  
  \draw[<->, >=Stealth, primaryblue] (-3.5, 0) -- (-3.5, 2) node[midway, left] {間隔 $D$};
  
  % 交差する針
  \draw[line width=1.6pt, warmamber] (-1, 0.4) -- (0.2, 1.8);
  \node[above, warmamber] at (-0.4, 1.1) {交差する針};
  
  % 交差しない針
  \draw[line width=1.6pt, accentgreen] (1.5, 0.5) -- (2.8, 1.1);
  \node[below, accentgreen] at (2.1, 0.8) {交差しない針};
  
  \node[align=center] at (0, -2.8) {\small ビュフォンの針問題：交差する確率 $P = \dfrac{2L}{\pi D}$ \quad ($L \le D$ のとき)};
\end{tikzpicture}
\caption{ビュフォンの針の実験：偶然の投てきから円周率 $\pi$ を導く幾何学的確率}
\end{figure}

\begin{columnbox}
""" + ch3_col_txt + r"""
\end{columnbox}

% ====================================================================
% 第4章
% ====================================================================
\chapter{論理と確率の架け橋 —— ヴェン図で解く条件付き確率}

\begin{vennbox}
\textit{“Every conditional statement in logic corresponds to a restricted universe of discourse in mathematics.”}\\
\hfill —— John Venn, \textit{Symbolic Logic}
\tcblower
【日本語訳】「論理学におけるすべての条件付き言明は、数学における『言及領域（全体集合）の限定』に対応している。」
\end{vennbox}

\section{条件付き確率を「ズームイン」で理解する}

\begin{gammabox}
""" + ch4_intro_txt + r"""
\end{gammabox}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9]
  % 通常の全体空間
  \draw[thick, fill=gray!8] (-4,-1.8) rectangle (4,1.8);
  \node at (3.6, 1.4) {$S$};
  
  \draw[thick, fill=primaryblue!15] (-1,0) circle (1.4);
  \draw[thick, fill=accentgreen!15] (1,0) circle (1.4);
  
  \begin{scope}
    \clip (-1,0) circle (1.4);
    \fill[softpurple!40] (1,0) circle (1.4);
  \end{scope}
  
  \draw[line width=1.5pt, primaryblue] (-1,0) circle (1.4);
  \node at (-1.5,0) {\textbf{$A$}};
  \node at (1.5,0) {\textbf{$B$}};
  \node at (0,0) {\small $A \cap B$};
  
  \node[align=center] at (0,-2.4) {
    \textbf{条件付き確率：$P(B \mid A) = \dfrac{P(A \cap B)}{P(A)}$}\\
    \small 「$A$ が起きた」という条件は、全体空間 $S$ を捨て去り、$A$ を新しい全体（分母）とすること！
  };
\end{tikzpicture}
\caption{ヴェン図による条件付き確率の幾何学的解釈：全体集合の縮小}
\end{figure}

\begin{columnbox}
""" + ch4_col_txt + r"""
\end{columnbox}

% ====================================================================
% 第5章
% ====================================================================
\chapter{誤差の法則と不完全な現実 —— 正規分布の限界と非対称データ}

\begin{vennbox}
\textit{“Nature does not always present us with the symmetrical bell curve. The statistics of social life, of wealth, and of human ability are frequently lopsided and skewed.”}\\
\hfill —— John Venn, \textit{The Logic of Chance}, Chapter II
\tcblower
【日本語訳】「自然は常に左右対称な釣鐘型曲線を私たちに見せてくれるとは限らない。社会生活や富、人間の能力に関する統計は、しばしば片側に歪んでいる。」
\end{vennbox}

\section{歪んだ分布（Skewness）と外れ値の重要性}

\begin{gammabox}
""" + ch5_intro_txt + r"""
\end{gammabox}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9]
  % 正規分布（対称）
  \draw[thick, ->] (-4.5,0) -- (-0.5,0) node[right] {$x$};
  \draw[thick, ->] (-2.5,0) -- (-2.5,2.5) node[above] {$f(x)$};
  \draw[primaryblue, line width=1.3pt, domain=-4.2:-0.8, samples=50] plot (\x, {2.0*exp(-2*(\x+2.5)*(\x+2.5))});
  \node[below] at (-2.5, -0.2) {\small 対称（正規分布）};
  \node at (-2.5, -0.7) {\footnotesize 平均値 $=$ 中央値};

  % 右に歪んだ分布（非対称：所得など）
  \draw[thick, ->] (0.5,0) -- (5.5,0) node[right] {$x$};
  \draw[thick, ->] (1.0,0) -- (1.0,2.5) node[above] {$g(x)$};
  \draw[warmamber, line width=1.3pt, domain=1.05:5.2, samples=60] plot (\x, {3.5*(\x-1.0)*exp(-1.8*(\x-1.0))});
  \node[below] at (3.0, -0.2) {\small 右に裾が長い歪んだ分布};
  \node at (3.0, -0.7) {\footnotesize 最頻値 $<$ 中央値 $<$ 平均値};
\end{tikzpicture}
\caption{ヴェンが喝破した理想的対称分布（正規分布）と現実社会の非対称分布}
\end{figure}

\begin{columnbox}
""" + ch5_col_txt + r"""
\end{columnbox}

% ====================================================================
% 第6章
% ====================================================================
\chapter{データから真実を推し量る —— 帰納法と現代の統計的推測}

\begin{vennbox}
\textit{“Induction is the truly creative step in science; it is the leap from the observed finite series to the unobserved universal reality.”}\\
\hfill —— John Venn, \textit{The Logic of Chance}, Part III
\tcblower
【日本語訳】「帰納法こそが科学における真に創造的な飛躍である。それは観測された有限の系列から、まだ観測されていない普遍的実在へと跳ぶことなのだ。」
\end{vennbox}

\section{帰納の論理と仮説検定の第一歩}

\begin{gammabox}
""" + ch6_intro_txt + r"""
\end{gammabox}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.95]
  % 仮説検定の正規分布
  \draw[thick, ->] (-3.8,0) -- (3.8,0) node[right] {$Z$};
  \draw[thick, ->] (0,0) -- (0,2.6) node[above] {$f(z)$};
  
  \draw[domain=-3.5:3.5, samples=70, line width=1.3pt, primaryblue] 
    plot (\x, {2.2 * exp(-\x*\x / 2)});
    
  % 棄却域（右裾 5%）
  \fill[softpurple!40, domain=1.64:3.5, samples=30] 
    (1.64,0) -- plot (\x, {2.2 * exp(-\x*\x / 2)}) -- (3.5,0) -- cycle;
    
  \draw[dashed, softpurple, thick] (1.64,0) -- (1.64, {2.2 * exp(-1.64*1.64/2)});
  \node[softpurple, above right] at (1.7, 0.4) {\small 棄却域（有意水準 $5\%$）};
  \node at (0, 0.8) {\small 採択域（偶然で説明可能）};
\end{tikzpicture}
\caption{統計的仮説検定の概念：偶然の確率が低すぎる結果を「有意」と判定する}
\end{figure}

\begin{columnbox}
""" + ch6_col_txt + r"""
\end{columnbox}

% ====================================================================
% あとがき
% ====================================================================
\backmatter

\chapter*{あとがき：2つの巨人の眼を持って未来へ}
\addcontentsline{toc}{chapter}{あとがき}

""" + afterword_txt + r"""

\vspace{10mm}
\begin{flushright}
2026年10月\\
\textbf{教育情報分析研究会}
\end{flushright}

\end{document}
"""

with open(TEX_FILE, 'w', encoding='utf-8') as f:
    f.write(tex_content)

print(f"Successfully generated {TEX_FILE} ({len(tex_content)} chars)")
