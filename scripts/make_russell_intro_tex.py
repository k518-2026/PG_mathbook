# -*- coding: utf-8 -*-
"""
Generate complete TeX source for:
『古典で学び直すラッセル数理哲学入門 —— いまからでも遅くない、高校までの数学で理解する歴史的名著』
(Project Gutenberg eBook #25447-intro)
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_TEX = "books/25447_russell_mathematical_philosophy/russell_mathematical_philosophy_intro.tex"

PREAMBLE = r"""\documentclass[11pt,a4paper,titlepage]{ltjsbook}

\usepackage{luatexja}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{geometry}
\geometry{top=23mm,bottom=23mm,left=23mm,right=23mm}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathmorphing,shapes.geometric,backgrounds}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{enumitem}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!70!black,
    citecolor=green!50!black,
    urlcolor=teal!80!black,
    pdftitle={古典で学び直すラッセル数理哲学入門},
    pdfauthor={Bertrand Russell / 著・解説}
}

% Custom boxes
\newtcolorbox{lecturebox}[1][大人のための徹底解説講義]{
    enhanced,
    colback=blue!5!white,
    colframe=blue!65!black,
    fonttitle=\bfseries\gtfamily,
    title={#1},
    arc=2mm,
    breakable,
    boxrule=1pt,
    top=3mm, bottom=3mm, left=3mm, right=3mm
}

\newtcolorbox{origbox}[1][バートランド・ラッセルの原典思索]{
    enhanced,
    colback=yellow!5!white,
    colframe=orange!70!black,
    fonttitle=\bfseries\gtfamily,
    title={#1},
    arc=2mm,
    breakable,
    boxrule=1pt,
    top=3mm, bottom=3mm, left=3mm, right=3mm
}

\newtcolorbox{examplebox}[1]{
    enhanced,
    colback=green!5!white,
    colframe=teal!70!black,
    fonttitle=\bfseries\gtfamily,
    title={#1},
    arc=2mm,
    breakable,
    boxrule=1pt,
    top=3mm, bottom=3mm, left=3mm, right=3mm
}

\newtcolorbox{exercisebox}[1]{
    enhanced,
    colback=purple!5!white,
    colframe=purple!70!black,
    fonttitle=\bfseries\gtfamily,
    title={#1},
    arc=2mm,
    breakable,
    boxrule=1pt,
    top=3mm, bottom=3mm, left=3mm, right=3mm
}

\title{
    {\Large\gtfamily 数学・科学古典名著再学習シリーズ 第7弾}\\[8pt]
    {\Huge\bfseries\gtfamily 古典で学び直す\\ラッセル数理哲学入門}\\[10pt]
    {\large\gtfamily いまからでも遅くない、高校までの数学で理解する歴史的名著}\\[6pt]
    {\normalsize 原典：Bertrand Russell \textit{Mysticism and Logic and Other Essays} (1917/1918)}
}
\author{バートランド・ラッセル 著\\編訳・現代的解説：プロジェクトGutenberg名著復刊委員会}
\date{2026年10月 完全決定版}

\begin{document}

\maketitle

\frontmatter

\chapter*{はじめに：大人の学び直しとしての『数理哲学』}
\addcontentsline{toc}{chapter}{はじめに：大人の学び直しとしての『数理哲学』}

20世紀を代表する知の巨人、バートランド・ラッセル（Bertrand Russell, 1872--1970）。彼はノーベル文学賞を受賞した卓越した散文の巨匠であると同時に、アルフレッド・ノース・ホワイトヘッドと共に大著『プリンキピア・マテマティカ（数学原理）』を著し、現代の記号論理学とコンピュータ科学の礎を築いた不滅の数理哲学者です。

ラッセルの名著『神秘主義と論理（原題：Mysticism and Logic and Other Essays, 1917/1918）』は、数学の専門家だけでなく、\textbf{「ものごとを筋道立てて深く考えたいすべての人々」}に向けて書かれた、知的冒険の最高峰です。

「数学とは何か？」「無限とは何か？」「因果関係とは何か？」「論理的な正しさとは何か？」――私たちが学校教育で計算規則として機械的に覚えさせられた数学の概念を、ラッセルは驚くほど平易で美しい散文によって、その哲学的な魂を呼び覚ましてくれます。

本入門・解説版（第7弾）では、人生経験豊かな50代〜80代の大人の学び直し読者のために、以下の三大特色を備えて構成されています：
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{ラッセルの論理哲学を高校数学の知識で完全追体験}：集合のパラドックス（理髪師の謎）、型理論の階層、ゼノンのパラドックスの無限等比級数による解決、カントールの無限集合（$\aleph_0$）と実数の対角線論法、記述理論の記号論理を、三段論法と基礎代数だけで完全に解き明かします。
    \item \textbf{全12章・高精細TikZ図版12点と実社会の応用例}：現代のサイバーセキュリティ（型付き言語Rust/TypeScript）、スマートコントラクト、自動運転車の知覚と記述、スーパーコンピュータの気象予測と微分方程式、AI時代の自動定理証明系（Lean 4）など、現代社会を支える数理の骨格を実感できます。
    \item \textbf{重要用語辞典＆総合演習問題と詳細解答}：基礎から論理的思考力を鍛える総合演習問題（全10問）と懇切丁寧なステップ解説を収録し、独学でも完全に理解を深められる構成となっています。
\end{enumerate}

感情に流されず、真理の冷徹な美しさと向き合う至福の知的旅へ、ラッセルと共に出発しましょう。

\clearpage
\tableofcontents
\clearpage

\mainmatter
"""

POSTAMBLE = r"""
\appendix

\chapter{数理哲学の重要用語辞典（バートランド・ラッセルの語彙）}

大人の学び直しを助けるため、ラッセルの数理哲学および現代論理学における最重要概念をコンパクトに整理・解説します。

\begin{description}[font=\normalfont\bfseries\gtfamily]
    \item[論理主義（Logicism）] すべての純粋数学の概念（数、関数、極限など）は純粋論理学の概念だけで定義可能であり、すべての数学の定理は論理学の公理と推論規則のみから演繹できるという立場。フレーゲ、ラッセル、ホワイトヘッドが推進した。
    \item[ラッセルのパラドックス（Russell's Paradox）] 「自分自身を要素として含まない集合全体の集合 $R = \{x \mid x \notin x\}$」を考えると、$R \in R \iff R \notin R$ となり、素朴集合論が自己言及によって矛盾に陥るという発見（1901年）。
    \item[階型理論（型理論：Theory of Types）] パラドックスを排除するために対象を個体（タイプ0）、集合（タイプ1）、集合の集合（タイプ2）と階層化し、上位タイプのみが下位タイプを要素に取れるとした文法理論。現代プログラミング言語の型システムの祖。
    \item[可算無限（Countable Infinity, $\aleph_0$）] 自然数全体の集合 $\mathbb{N}$ と1対1対応がつく無限集合の大きさ（濃度）。偶数、整数、有理数（分数）全体の集合はいずれも可算無限である。
    \item[非可算無限（Uncountable Infinity, 連続体濃度）] 実数全体の集合のように、自然数と1対1対応がつかない真に高次の無限。カントールの対角線論法によって証明された。
    \item[記述理論（Theory of Descriptions）] 「現在のフランス国王」のような確定記述を含む文を、存在記号 $\exists$ と論理積 $\land$ を用いた論理式へと解剖し、存在しない対象について語る日常言語の曖昧さを解消したラッセルの言語分析理論。
    \item[直接親知（Acquaintance）] いかなる推論や概念的媒介も経ずに、直接的・直観的に意識に与えられる知識。自己の感覚与格（色の知覚、痛みなど）や直接の意識体験。
    \item[記述による知識（Knowledge by Description）] 直接親知される感覚与格を手掛かりとして、客観的対象の性質を論理的に構成・推論して得られる知識。物理世界の物体や他者の心についての知識。
    \item[オッカムの剃刀（Occam's Razor）] 「必要なしに存在者を増やしてはならない」という思考の節約原理。ラッセルは「推論された未知の実体よりも、感覚データからの論理的構成物を好め」と応用した。
    \item[因果律の追放（Critique of Causality）] 原因が結果を物理的に引き起こすという擬人的な因果概念を排し、現代物理学の基本構造は時間変数を含む微分方程式の「関数関係の恒常性」であるとする主張。
    \item[論理的原子論（Logical Atomism）] 世界は相互に独立した「論理的原子（事実）」から構成されており、言語と論理の精密な分析を通じて世界の客観的構造を解明できるとするラッセルの哲学。
    \item[対話型定理証明系（Interactive Theorem Prover）] ラッセルの形式論理と型理論を計算機上に実装し、数学の証明の完全性を一行ずつ自動検証するソフトウェア（Lean 4, Coq, Isabelleなど）。
\end{description}

\chapter{総合演習問題と詳細ステップ解説（論理と数学の基礎力養成）}

本章では、高校数学（命題論理、集合、無限等比級数、背理法）を用いて自らの頭で考え、ラッセル数理哲学の核心を体得するための総合演習問題を全10問収録しました。

\begin{exercisebox}{第1問：ド・モルガンの法則と真理値表の完全証明}
命題 $P, Q$ に対し、高校数学Iで学ぶド・モルガンの法則
\[
\neg (P \lor Q) \iff (\neg P) \land (\neg Q)
\]
を真理値表（$P, Q$ の真偽値 $T, F$ の全4通り）を作成して厳密に証明せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
$P, Q$ の真偽の組み合わせ全4通りについて真理値表を作成する：
\begin{center}
\begin{tabular}{cc|c|c|c|c|c}
\toprule
$P$ & $Q$ & $P \lor Q$ & $\neg (P \lor Q)$ & $\neg P$ & $\neg Q$ & $(\neg P) \land (\neg Q)$ \\
\midrule
$T$ & $T$ & $T$ & \textbf{F} & $F$ & $F$ & \textbf{F} \\
$T$ & $F$ & $T$ & \textbf{F} & $F$ & $T$ & \textbf{F} \\
$F$ & $T$ & $T$ & \textbf{F} & $T$ & $F$ & \textbf{F} \\
$F$ & $F$ & $F$ & \textbf{T} & $T$ & $T$ & \textbf{T} \\
\bottomrule
\end{tabular}
\end{center}
第4列 $\neg (P \lor Q)$ と第7列 $(\neg P) \land (\neg Q)$ の真偽値は、4つのケースすべてにおいて完全に一致している（F, F, F, T）。
したがって、両者は論理的に同値（$\iff$）であることが機械的に証明された。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第2問：理髪師のパラドックスの記号論理的背理法}
村の全員の集合を $M$、理髪師を $b \in M$ とする。述語 $S(x, y)$ を「$x$ は $y$ の髭を剃る」とする。\\
理髪師の規則は「任意の村人 $x$ に対し、$S(b, x) \iff \neg S(x, x)$」である。\\
この規則に $x = b$ を代入したときに生じる矛盾を背理法で明快に示せ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
理髪師の規則の全称命題 $\forall x \in M \, [S(b, x) \iff \neg S(x, x)]$ において、$x$ として理髪師自身 $b$ を代入する。すると、
\[
S(b, b) \iff \neg S(b, b)
\]
が得られる。\\
命題 $P$ を $S(b, b)$（理髪師は自分の髭を剃る）と置くと、上の式は $P \iff \neg P$ となる。
\begin{itemize}
\item もし $P$ が真（$T$）なら、$\neg P$ は偽（$F$）となり、$T \iff F$ となって矛盾。
\item もし $P$ が偽（$F$）なら、$\neg P$ は真（$T$）となり、$F \iff T$ となって矛盾。
\end{itemize}
排中律（命題は真か偽のいずれかである）により、いかなる真理値も割り当てることができず、前提である規則を満たす理髪師 $b$ は論理的に存在し得ない（そのような条件づけ自体が自己矛盾である）ことが証明された。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第3問：ゼノンのパラドックスと無限等比級数の収束}
時速 $120\,\text{km}$（$= \frac{100}{3}\,\text{m/s}$）の新幹線が、前方 $1000\,\text{m}$ を時速 $24\,\text{km}$（$= \frac{20}{3}\,\text{m/s}$）で走る普通列車を追いかける。\\
(1) 新幹線が普通列車の直前の位置に達する各ステップの所要時間を数列 $\{t_n\}$ として表せ。\\
(2) 無限等比級数の和の公式 $S = \frac{a}{1 - r}$ を用いて、新幹線が普通列車に追いつくまでの総時間を秒単位で計算せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
速度比は $r = \frac{24\,\text{km/h}}{120\,\text{km/h}} = \frac{1}{5} = 0.2$ である。\\
第1ステップ：新幹線が最初の距離 $1000\,\text{m}$ を進む時間 $t_1$ は
\[
t_1 = \frac{1000}{\frac{100}{3}} = 30\,\text{秒}
\]
この30秒間に普通列車は $1000 \times \frac{1}{5} = 200\,\text{m}$ 進む。\\
第2ステップ：新幹線がこの $200\,\text{m}$ を進む時間 $t_2$ は $t_2 = t_1 \times \frac{1}{5} = 6\,\text{秒}$。\\
一般に第 $n$ ステップの所要時間は $t_n = 30 \times (0.2)^{n-1}$ 秒となる。\\
\textbf{(2) の解：}
新幹線が追いつくまでの無限個のステップの合計時間 $T$ は、初項 $a = 30$、公比 $r = 0.2$ の無限等比級数である：
\[
T = \sum_{n=1}^\infty 30 \times (0.2)^{n-1} = \frac{30}{1 - 0.2} = \frac{30}{0.8} = 37.5\,\text{秒}
\]
ステップの分割が無限に細かく続いても、経過時間の総和は $37.5$ 秒でピタリと収束し、新幹線は何の滞りもなく普通列車に追いつく。ゼノンの幻惑は極限の数理によって完全に解消される。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第4問：カントールの対角線論法（実数の非可算性の証明）}
0以上1未満の実数がもしすべて自然数と1対1に対応づけられ、$x_1, x_2, x_3, \dots$ と一列にリスト化できたと仮定する。\\
各実数を2進数の無限小数で表し、
\[
x_n = 0.b_{n1} b_{n2} b_{n3} \dots \quad (b_{ni} \in \{0, 1\})
\]
とする。\\
(1) 対角成分 $b_{nn}$ を反転させた新しい数列 $c_n = 1 - b_{nn}$ を定義したとき、実数 $y = 0.c_1 c_2 c_3 \dots$ がリスト内のどの $x_n$ とも一致しないことを示せ。\\
(2) この背理法から導かれる結論を簡潔に述べよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
任意の自然数 $k$ を選ぶ。実数 $y$ の小数第 $k$ 位の数字は $c_k = 1 - b_{kk}$ であるのに対し、リストの第 $k$ 番目の実数 $x_k$ の小数第 $k$ 位の数字は $b_{kk}$ である。
$b_{kk} \in \{0, 1\}$ であるから、$c_k \neq b_{kk}$ は常に成り立つ。
したがって、実数 $y$ は小数第 $k$ 位において $x_k$ と必ず異なる値を持つ。$k$ は任意の自然数であるから、$y$ はリストにあるいかなる実数 $x_1, x_2, x_3, \dots$ のどれとも一致しない。\\
\textbf{(2) の解：}
「すべての実数をリスト化した」という前提から、リストから漏れている実数 $y$ が必ず存在するという矛盾が導かれた。したがって、区間 $[0, 1)$ の実数全体の集合は可算無限ではなく、自然数全体の集合よりも真に大きい非可算無限（濃度 $2^{\aleph_0}$）であることが背理法により厳密に証明された。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第5問：自然数全体の集合と偶数全体の集合の1対1対応}
自然数全体の集合を $\mathbb{N} = \{1, 2, 3, 4, \dots\}$、正の偶数全体の集合を $2\mathbb{N} = \{2, 4, 6, 8, \dots\}$ とする。\\
(1) 関数 $f(n) = 2n$ が、$\mathbb{N}$ から $2\mathbb{N}$ への全単射（1対1かつ上への写像）であることを証明せよ。\\
(2) 有限集合では「真部分集合の要素数は全体より真に小さい」のに対し、無限集合では「部分が全体と対等になり得る」というデデキントの無限の定義の本質を述べよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
\begin{itemize}
\item 単射性：$f(n_1) = f(n_2) \implies 2n_1 = 2n_2 \implies n_1 = n_2$。したがって異なる自然数は必ず異なる偶数に対応する。
\item 全射性：任意の偶数 $m \in 2\mathbb{N}$ に対し、$m = 2k$ となる自然数 $k = m/2 \in \mathbb{N}$ が必ず存在する。
\end{itemize}
単射かつ全射であるから、写像 $f$ は全単射である。\\
\textbf{(2) の解：}
有限集合では、一部を取り除けば要素数は必ず減ります。しかし無限集合では、奇数という無限個の要素をまるまる取り除いた偶数だけの部分集合であっても、全単射 $f(n)=2n$ によって元の自然数全体と寸分の狂いもなく1対1に対応づけることができます。「自分自身の真部分集合と対等（同濃度）になれる」ことこそが、無限集合だけが持つ驚くべき本質的特徴なのです。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第6問：ラッセルの記述理論の記号論理式展開}
「現在のフランス国王は禿頭である」という文を述語論理式で記述する。\\
述語 $K(x)$ を「$x$ は現在のフランス国王である」、$B(x)$ を「$x$ は禿頭である」とする。\\
(1) この文を論理記号（$\exists, \forall, \land, \to$）を用いて厳密に立式せよ。\\
(2) なぜこの論理式が、現実の宇宙において「偽（False）」と一意に評価されるのかを解説せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
ラッセルの記述理論に従い、存在・唯一性・属性の3条件を結合すると：
\[
\exists x \, [ K(x) \land \forall y (K(y) \to y = x) \land B(x) ]
\]
言葉で直訳すれば、「ある $x$ が存在して、(1) $x$ はフランス国王であり、(2) フランス国王であるいかなる $y$ も $x$ と同一であり、(3) かつ $x$ は禿頭である」となる。\\
\textbf{(2) の解：}
現実の世界において、フランス国王である人物 $x$ は誰一人存在しない。したがって、部分命題 $K(x)$ を満たす対象が領域内に存在せず、存在量化命題 $\exists x [ K(x) \land \dots ]$ 全体の真偽値は直ちに「偽（False）」となる。
文法上の主語「フランス国王」に惑わされることなく、客観的事実と論理の規則に基づいて真偽を明快に確定できる。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第7問：三段論法の形式的妥当性と健全性}
次の2つの推論について、形式的妥当性（Validity）と健全性（Soundness）を判定せよ。\\
推論A：\\
前提1：すべての鳥は飛ぶことができる。\\
前提2：ペンギンは鳥である。\\
結論：ゆえに、ペンギンは飛ぶことができる。\\
推論B：\\
前提1：すべての偶数は2で割り切れる。\\
前提2：12は偶数である。\\
結論：ゆえに、12は2で割り切れる。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\begin{itemize}
\item \textbf{推論Aの判定：}
\textbf{妥当であるが、不健全。}\\
論理の形式としては「$\forall x (P(x) \to Q(x))$ かつ $P(a) \implies Q(a)$」であり、推論の鎖自体には何の飛躍もなく論理的に妥当（Valid）である。しかし、前提1「すべての鳥は飛ぶことができる」が現実の生物学的事実として偽（ダチョウやペンギンは飛べない）であるため、論証全体としては健全（Sound）ではない。
\item \textbf{推論Bの判定：}
\textbf{妥当かつ健全。}\\
論理的推論形式が妥当であるだけでなく、前提1（数学的定義）も前提2（計算的事実）も真であるため、結論の真理性が絶対的に保証された健全な論証である。
\end{itemize}
ラッセルが強調したように、論理学は推論の形式的妥当性を保証し、個別科学が前提の事実的真理性を検証する。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第8問：ブール代数による排他的論理和（XOR）の回路表現}
二値論理変数 $A, B \in \{0, 1\}$ に対し、排他的論理和 $A \oplus B$（$A$ と $B$ が異なるときだけ1）を考える。\\
(1) 基本的な論理積（AND：$\cdot$）、論理和（OR：$+$）、論理否定（NOT：$\bar{A}$）のみを用いて $A \oplus B$ のブール代数式を表現せよ。\\
(2) ラッセルの論理主義が指摘した「数学の加算の最下層」において、2進数の1桁の足し算（半加算器）の和（Sum）がなぜ $A \oplus B$、繰り上がり（Carry）がなぜ $A \cdot B$ に一致するのかを示せ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
排他的論理和 $A \oplus B$ は、「$A$ が真で $B$ が偽、または $A$ が偽で $B$ が真」であるから、
\[
A \oplus B = (A \land \neg B) \lor (\neg A \land B) = A \cdot \bar{B} + \bar{A} \cdot B
\]
\textbf{(2) の解：}
2進数の足し算 $A + B$ の結果は以下の通りである：
\begin{center}
\begin{tabular}{cc|c|c|c}
\toprule
$A$ & $B$ & 算術の和 $A+B$ & 1桁目の値（Sum） & 繰り上がり（Carry） \\
\midrule
0 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 \\
1 & 0 & 1 & 1 & 0 \\
1 & 1 & 2 (2進数で10) & 0 & 1 \\
\bottomrule
\end{tabular}
\end{center}
Sumの列（0, 1, 1, 0）はまさに $A \oplus B$ の真理値と完全に一致し、Carryの列（0, 0, 0, 1）は $A \cdot B$（AND）の真理値と完全に一致する。
コンピュータのCPUが行うすべての計算の根底には、ラッセルやブールが解明した純粋論理演算がそのまま埋め込まれている。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第9問：オッカムの剃刀と感覚与格からの論理的構成}
目の前にある「1本の鉛筆」を眺める。視点を変えると鉛筆の角度は変わり、部屋の照明を落とすと鉛筆の色は暗く変わり、手で握ると硬い触覚が得られる。\\
(1) 「目に見えない神秘的な鉛筆の実体」を想定する素朴実在論に対し、ラッセルが提唱した「知覚された無数の感覚与格の相関関係として鉛筆を論理的に構成する」という方法論を説明せよ。\\
(2) なぜこの考え方が、最新の3次元コンピュータグラフィックス（NeRF：ニューラル放射場）やLiDAR点群処理と本質的に同一であるのかを述べよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
伝統的な哲学は、変化する感覚の背後に「不変の鉛筆の実体（物自体）」という検証不能な幽霊を想定しがちでした。ラッセルはオッカムの剃刀を用い、「科学的に必要なのは、視点 $(x, y, z)$ や照明条件に応じて体系的に変化する感覚与格（見え、感触）の集まりと、それらを結びつける数学的法則だけである」と喝破しました。鉛筆とは、それらの感覚与格の論理的関係（クラス）そのものとして定義すれば十分であり、余計な形而上学的実体を仮定する必要はないのです。\\
\textbf{(2) の解：}
現代のNeRF（Neural Radiance Fields）技術は、物体の物理的実体を直接スキャンするのではなく、様々な角度から撮影した数十枚の2次元写真（感覚データ）から、光線方程式を解くことで3次元空間内の色と密度を逆算・再構成します。まさにラッセルが説いた「多数の視点の感覚与格から客観的世界を論理的に構成するアルゴリズム」が、現代のAI画像技術として完璧に実現されています。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第10問：微分方程式による惑星の軌道決定（因果律の超越）}
質量 $M$ の太陽の周りを回る惑星の位置ベクトルを $\mathbf{r}(t)$ とする。ニュートン力学の運動方程式は
\[
\frac{d^2 \mathbf{r}}{dt^2} = - \frac{GM}{|\mathbf{r}|^3} \mathbf{r}
\]
である。\\
(1) この方程式において、「原因」や「結果」という言葉を使わずに、現在のある時刻 $t_0$ における位置 $\mathbf{r}(t_0)$ と速度 $\frac{d\mathbf{r}}{dt}(t_0)$（初期条件）が与えられたとき、未来の任意の時刻 $t > t_0$ の位置が一意に決定される数学的メカニズム（微分方程式の初期値問題の解の一意性）を説明せよ。\\
(2) ラッセルが論じた「過去も未来も時間変数 $t$ に関して対称であり、因果関係という擬人的な物語は物理学の数理には存在しない」という結論の意義をまとめよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
この方程式は、2階の常微分方程式です。微分方程式の基本定理（コーシー・ピカールの存在と一意性の定理）により、初期時刻 $t_0$ における位置 $\mathbf{r}(t_0)$ と速度 $\mathbf{v}(t_0)$ の2つのベクトルが定まれば、未来の任意の時刻 $t$ における軌道 $\mathbf{r}(t)$ は数学的にただ1つに定まります。そこに「太陽の引力が原因で、惑星が動くのが結果だ」というような人間の物語を差し挟む余地はありません。すべては「位置と加速度のあいだの微分方程式という関数関係」に従って淡々と計算されるだけです。\\
\textbf{(2) の解：}
時間を逆転させて $t \to -t$ と変換しても、加速度 $\frac{d^2 \mathbf{r}}{dt^2}$ の符号は変わりません。したがって、この方程式は未来を予測できるのと全く同じ精度で、過去の軌道 $\mathbf{r}(-t)$ を逆算して決定できます。「過去が原因で未来が決まる」という人間の一方向的な時間感覚は、物理法則の数理的骨格そのものには含まれていません。世界を情念から解放し、不変の数理的関係として捉え直すことこそ、ラッセル数理哲学の究極の到達点です。\qed
\end{exercisebox}

\chapter*{おわりに：理性の光と大人の知性の威厳}
\addcontentsline{toc}{chapter}{おわりに：理性の光と大人の知性の威厳}

バートランド・ラッセルが生涯を通じて追求したのは、\textbf{「いかなる権威や偏見にも屈しない、理性の完全な独立」}でした。

彼は97年の長きにわたる生涯の中で、第一次世界大戦の反戦運動によって投獄され、第二次世界大戦後にはアルバート・アインシュタインと共に「ラッセル＝アインシュタイン宣言」を発表して核兵器廃絶と世界平和を世界に訴え続けました。

その不屈の社会活動を支えていた背骨こそ、若い日に培った\textbf{「数理哲学の冷徹な論理の力」}でした。
どれほど声高なプロパガンダが叫ばれようと、どれほど多くの群衆が熱狂に流されようと、論理的に誤っているものは誤りであり、正当な根拠のない言説は偽である――この透徹した批判的精神を、彼は数学の証明を通じて学び取っていたのです。

人生の円熟期を迎えた50代から80代の読者の皆様が、本書を通じてラッセルの思考を追体験し、日常の雑多な情報に惑わされることなく、静かに自らの頭で筋道立てて考え、普遍なる真理の美しさに触れる喜びを味わっていただけたなら、編訳者一同の最高の喜びです。

\end{document}
"""

def generate_full_tex():
    import scripts.russell_figures as rf
    import scripts.russell_examples as re
    import scripts.russell_chapters as rc
    
    tex_parts = [PREAMBLE]
    
    for ch_num in range(1, 13):
        ch = rc.CHAPTERS[ch_num]
        fig_tikz, fig_cap = rf.FIGS[ch_num]
        example_tex = re.EXAMPLES[ch_num]
        
        part_name = ""
        if ch_num == 1:
            part_name = "\\part{論理主義の夜明けと数学の基礎}\n\n"
        elif ch_num == 5:
            part_name = "\\part{無限・連続体と言語の解剖学}\n\n"
        elif ch_num == 9:
            part_name = "\\part{科学的認識論と現代計算機への飛翔}\n\n"

        ch_tex = f"""{part_name}\\chapter{{{ch['title']}}}
\\begin{{center}}
{{\\Large\\bfseries\\gtfamily {ch['subtitle']}}}
\\end{{center}}
\\vspace*{{2mm}}

\\section*{{本章の視覚的見取り図}}
\\begin{{center}}
{fig_tikz}

\\small\\textbf{{図版解説：}}{fig_cap}
\\end{{center}}
\\vspace*{{2mm}}

\\section*{{バートランド・ラッセルの原典思索}}
\\begin{{origbox}}[原著第{ch_num}章：知の巨人の肉声と思索]
{ch['orig']}
\\end{{origbox}}

\\section*{{大人のための徹底解説講義}}
\\begin{{lecturebox}}[徹底講義：高校数学で読み解く数理哲学]
{ch['lecture']}
\\end{{lecturebox}}

\\vspace*{{3mm}}
{example_tex}
"""
        tex_parts.append(ch_tex)
    
    tex_parts.append(POSTAMBLE)
    
    full_content = "\n\n\\clearpage\n".join(tex_parts)
    
    os.makedirs(os.path.dirname(OUTPUT_TEX), exist_ok=True)
    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    print(f"Successfully generated {OUTPUT_TEX} ({len(full_content)} chars)")

if __name__ == "__main__":
    generate_full_tex()
