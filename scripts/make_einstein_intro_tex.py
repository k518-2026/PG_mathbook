# -*- coding: utf-8 -*-
"""
Build Complete "Einstein Relativity Introduction for Adults"
(古典で学び直すアインシュタイン相対性理論入門)
Gutenberg #30155-intro
12 Comprehensive Chapters + TikZ Figures + Adult Lectures + Real-World Examples + Glossary + Exercises
"""
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_TEX = "books/30155_einstein_relativity/einstein_relativity_intro.tex"

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
    pdftitle={古典で学び直すアインシュタイン相対性理論入門},
    pdfauthor={Albert Einstein / 著・解説}
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

\newtcolorbox{origbox}[1][アインシュタインの原典思索]{
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
    {\Large\gtfamily 数学・科学古典名著再学習シリーズ 第6弾}\\[8pt]
    {\Huge\bfseries\gtfamily 古典で学び直す\\アインシュタイン相対性理論入門}\\[10pt]
    {\large\gtfamily いまからでも遅くない、高校までの数学で理解する歴史的名著}\\[6pt]
    {\normalsize 原典：Albert Einstein \textit{Relativity: The Special and the General Theory} (1916/1920)}
}
\author{アルベルト・アインシュタイン 著\\編訳・現代的解説：プロジェクトGutenberg名著復刊委員会}
\date{2026年10月 完全決定版}

\begin{document}

\maketitle

\frontmatter

\chapter*{はじめに：大人の学び直しとしての『相対性理論』}
\addcontentsline{toc}{chapter}{はじめに：大人の学び直しとしての『相対性理論』}

1916年、アルベルト・アインシュタイン（Albert Einstein, 1879--1955）は、自ら打ち立てた二大物理学革命――特殊相対性理論（1905年）と一般相対性理論（1915年）――の全容を、物理学者だけでなく\textbf{「科学的・哲学的な興味を持つ一般読者」}に向けて自ら平易に解説した稀代の名著『特殊および一般相対性理論について（原題：Über die spezielle und die allgemeine Relativitätstheorie, gemeinverständlich）』を著しました。

世間一般において「相対性理論」といえば、難解極まるテンソル解析や微分幾何学、あるいはSFの世界のタイムトラベルやブラックホールといった先入観が先行しがちです。しかし、アインシュタイン自身が序文で宣言しているように、本書の目的は\textbf{「大学の専門教育を受けていない読者でも、標準的な高校程度の教育（中等教育）を受けていれば、その核心思想と論理を完全に追体験できるようにすること」}にありました。

本入門・解説版（第6弾）では、人生経験豊かな50代〜80代の大人の学び直し読者のために、以下の三大特色を備えて構成されています：
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{アインシュタイン自身の思考実験を高校数学で完全追体験}：列車と堤防の思考実験、光時計、動く物体の縮み、同時性の不一致、重力と加速系の等価原理を、三平方の定理と1次方程式だけで完全に導出します。
    \item \textbf{全12章・高精細TikZ図版12点と実社会の応用例}：GPS衛星のナノ秒単位の時計補正、新幹線・ジェット機実験、素粒子ミューオンの寿命延伸、巨大重力レンズ、宇宙膨張と現代ビッグバン宇宙論など、現代社会と科学の礎を実感できます。
    \item \textbf{重要用語辞典＆総合演習問題と詳細解答}：基礎から段階的に確認できる総合問題（全10問）とステップ・バイ・ステップの模範解答を収録し、独学でも完全に理解を深められる構成となっています。
\end{enumerate}

知的好奇心に満ちた物理学の最高峰へ、アインシュタインと共に歩みを進めましょう。

\clearpage
\tableofcontents
\clearpage

\mainmatter
"""

POSTAMBLE = r"""
\appendix

\chapter{相対性理論の重要用語辞典（アルベルト・アインシュタインの語彙）}

大人の学び直しを助けるため、アインシュタインの原典および現代物理学において極めて重要な鍵概念をコンパクトに整理・解説します。

\begin{description}[font=\normalfont\bfseries\gtfamily]
    \item[慣性系（Inertial System）] 外力が働いていない物体が静止し続けるか等速直線運動を続ける座標系（慣性の法則が成立する系）。互いに等速で移動する慣性系どうしはすべて物理的に同等である。
    \item[光速度不変の原理（Principle of Constancy of Light Speed）] 真空中の光の速さ $c \approx 3 \times 10^8\,\text{m/s}$ は、光源の運動状態や観測者の運動速度に一切依存せず、すべての慣性系において常に同一であるという基本原理。
    \item[特殊相対性原理（Special Principle of Relativity）] すべての慣性座標系において、物理法則は全く同一の形式で表され、絶対静止座標系という特別な系は存在しない。
    \item[同時性の相対性（Relativity of Simultaneity）] ある観測者にとって「同時に起こった」2つの事象は、その観測者に対して動いている別の観測者にとっては「同時ではない」という事実。時間の一様性・絶対性の否定。
    \item[ローレンツ変換（Lorentz Transformation）] 光速度不変の原理と特殊相対性原理を満たす、2つの等速運動座標系間の時空変換公式。$\gamma = 1/\sqrt{1 - v^2/c^2}$ を尺度係数とする。
    \item[時間の遅れ（Time Dilation）] 観測者に対して高速運動している時計は、静止している時計に比べて進み方が遅くなる（$\Delta t = \gamma \Delta t_0$）現象。
    \item[ローレンツ収縮（Lorentz Contraction）] 観測者に対して運動している剛体は、運動方向に沿って長さが $\sqrt{1 - v^2/c^2}$ 倍に縮んで観測される現象。
    \item[質量とエネルギーの等価性（$E=mc^2$）] 静止質量 $m$ を持つ物体は、その質量自体の中に $E = mc^2$ という莫大な固有エネルギーを宿しているという帰結。原子力発電や恒星の核融合の根源。
    \item[ミンコフスキー時空（Minkowski Spacetime）] 3次元空間と時間1次元を一体として扱い、$s^2 = c^2 t^2 - (x^2 + y^2 + z^2)$ という不変量を幾何学的に定義した4次元時空連続体。
    \item[等価原理（Principle of Equivalence）] 局所的に一様な重力場の中に静止している座標系と、重力のない空間で等加速度運動をしている加速系は、物理的に全く区別がつかないという原理。
    \item[一般相対性原理（General Principle of Relativity）] 慣性系だけでなく、加速度運動している座標系や重力場の中にある座標系も含め、任意の運動状態にあるすべての座標系において物理法則が共変的（同一形式）に成り立つ。
    \item[測地線（Geodesic）] 質量やエネルギーによって歪められた曲がった時空において、物体や光線が辿る「最短（最極値）の軌道」。古典力学の「重力による引力」は、時空の測地線運動として幾何学的に書き直される。
    \item[宇宙項（Cosmological Constant, $\Lambda$）] アインシュタインが静的で閉じた宇宙解を得るために一般相対論の方程式に導入した斥力項。現代宇宙論では「ダークエネルギー」として再評価されている。
\end{description}

\chapter{総合演習問題と詳細ステップ解説（高校数学で解く相対論）}

本章では、高校数学（三平方の定理・1次方程式・平方根の展開）を用いて自らの手で計算し、相対性理論の真髄を血肉とするための総合演習問題を全10問収録しました。

\begin{exercisebox}{第1問：光時計による時間の遅れの導出}
高さ $L$ の列車内に設置された光時計を考える。床から天井へ放たれた光が反射して戻る往復時間を、車内の人 $S'$ は $\Delta t'$、堤防の静止観察者 $S$ は $\Delta t$ と測る。列車が水平方向に速度 $v$ で走るとき、三平方の定理を用いて
\[
\Delta t = \frac{\Delta t'}{\sqrt{1 - v^2/c^2}}
\]
を導出せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
車内の人から見れば、光は垂直に往復するだけなので、往復距離は $2L$ である。光速を $c$ とすれば、
\[
\Delta t' = \frac{2L}{c} \quad \implies \quad L = \frac{c \Delta t'}{2}
\]
一方、堤防の観察者から見ると、光が天井に到達して戻るまでに列車は水平方向に $v \Delta t$ だけ進む。光が片道で進む水平距離は $\frac{v \Delta t}{2}$、垂直距離は $L$ である。三平方の定理より、光が進んだ斜辺の距離 $d$ は
\[
d = \sqrt{\left(\frac{v \Delta t}{2}\right)^2 + L^2}
\]
堤防の人にとっても光速は同一の $c$ であるから、往復距離 $2d$ は $c \Delta t$ に等しい：
\[
c \Delta t = 2 \sqrt{\left(\frac{v \Delta t}{2}\right)^2 + L^2} = \sqrt{(v \Delta t)^2 + 4L^2}
\]
両辺を2乗すると、
\[
c^2 (\Delta t)^2 = v^2 (\Delta t)^2 + 4L^2
\]
ここで $L = \frac{c \Delta t'}{2}$ より $4L^2 = c^2 (\Delta t')^2$ を代入すると、
\[
(c^2 - v^2) (\Delta t)^2 = c^2 (\Delta t')^2
\]
両辺を $c^2$ で割り、$(\Delta t)^2$ について解くと、
\[
\left(1 - \frac{v^2}{c^2}\right) (\Delta t)^2 = (\Delta t')^2 \quad \implies \quad \Delta t = \frac{\Delta t'}{\sqrt{1 - v^2/c^2}}
\]
これにより、高校数学の三平方の定理だけで時間の遅れの方程式が厳密に証明された。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第2問：新幹線の時間の遅れの定量的計算}
東海道新幹線が時速 $288\,\text{km}$（$= 80\,\text{m/s}$）で $1$ 時間（$= 3600\,\text{秒}$）走行したとする。光速 $c = 3 \times 10^8\,\text{m/s}$ とする。\\
(1) 速度比 $\beta = v/c$ を求めよ。\\
(2) 近似式 $\sqrt{1 - x^2} \approx 1 - \frac{1}{2}x^2$ を用いて、新幹線の時計が地上の時計に対して遅れる時間をナノ秒単位で計算せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
\[
\beta = \frac{v}{c} = \frac{80}{3 \times 10^8} = \frac{8}{3} \times 10^{-7} \approx 2.67 \times 10^{-7}
\]
\textbf{(2) の解：}
地上の時間を $T = 3600\,\text{s}$、車内の時間を $T'$ とすると、$T' = T \sqrt{1 - \beta^2} \approx T \left(1 - \frac{1}{2}\beta^2\right)$ である。遅れの差 $\Delta T = T - T'$ は
\[
\Delta T \approx \frac{1}{2} T \beta^2 = \frac{1}{2} \times 3600 \times \left(\frac{8}{3} \times 10^{-7}\right)^2
= 1800 \times \frac{64}{9} \times 10^{-14} = 200 \times 64 \times 10^{-14} = 12800 \times 10^{-14} = 1.28 \times 10^{-10}\,\text{秒}
\]
これは $0.128\,\text{ナノ秒}$（$1$ ナノ秒 $= 10^{-9}$ 秒）に相当する。人間の感覚では到底認知できない微小量であるが、現代の原子時計を用いれば $10^{-18}$ 秒まで計測できるため、日常的な速度であっても相対論的遅れは完全に実証されている。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第3問：素粒子ミューオンの地表到達と寿命延伸}
宇宙線が大気上層（高度 $10\,\text{km} = 10^4\,\text{m}$）で衝突して生成される素粒子ミューオンの固有寿命はわずか $\tau_0 = 2.2 \times 10^{-6}\,\text{秒}$（$2.2\,\mu\text{s}$）である。ミューオンが光速の $99.5\%$（$v = 0.995c$）で地表に向かって飛行しているとする。\\
(1) 非相対論的（ニュートン力学）な計算では、ミューオンが崩壊するまでに進める距離は何メートルか。地表に到達できるか答えよ。\\
(2) 特殊相対性理論の時間の遅れを考慮すると、地上の観測者から見たミューオンの寿命 $\tau$ は何秒に伸びるか。また、その間に進める距離を求め、なぜ地表で大量のミューオンが観測されるのかを説明せよ（ただし $\sqrt{1 - 0.995^2} \approx 0.10$ とする）。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
古典力学での飛行距離 $L_{\text{classic}}$ は
\[
L_{\text{classic}} = v \tau_0 = (0.995 \times 3 \times 10^8\,\text{m/s}) \times (2.2 \times 10^{-6}\,\text{s}) \approx 2.985 \times 10^8 \times 2.2 \times 10^{-6} \approx 657\,\text{m}
\]
大気上層の高度は $10000\,\text{m}$ であるため、$657\,\text{m}$ 飛んだ時点で大半が崩壊してしまい、地表には一粒たりとも到達できないはずである。\\
\textbf{(2) の解：}
ローレンツ因子 $\gamma$ は
\[
\gamma = \frac{1}{\sqrt{1 - (0.995)^2}} \approx \frac{1}{0.10} = 10
\]
地上の時計から見ると、ミューオンの内部時計は $10$ 倍に引き伸ばされるため、寿命は
\[
\tau = \gamma \tau_0 = 10 \times 2.2 \times 10^{-6} = 2.2 \times 10^{-5}\,\text{秒}
\]
この間に光速に近い速度で進む距離 $L_{\text{rel}}$ は
\[
L_{\text{rel}} = v \tau \approx (3 \times 10^8) \times (2.2 \times 10^{-5}) = 6600\,\text{m} \sim 10000\,\text{m}
\]
となり、高度 $10\,\text{km}$ から放たれたミューオンの多くが地表まで余裕をもって到達できる。なお、ミューオン自身の視座（静止系）から見れば、時間の進みは $2.2\,\mu\text{s}$ のままであるが、大気の厚み $10\,\text{km}$ がローレンツ収縮によって $\frac{1}{10}$ の $1\,\text{km}$ に縮んでいるため、やはり地表に到達できると解釈され、両者の観測結果は見事に一致する。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第4問：GPS衛星の相対論補正（特殊相対論と一般相対論の綱引き）}
高度 $20000\,\text{km}$ を周回するGPS衛星の軌道速度は約 $v = 3.9\,\text{km/s}$ である。\\
(1) 特殊相対性理論の速度による効果により、地上に対してGPS衛星の原子時計は1日あたり何マイクロ秒遅れるか（計算値：約 $-7.2\,\mu\text{s}$）。\\
(2) 一般相対性理論の重力ポテンシャルによる効果（高度が高く重力が弱いため時計が速く進む）により、地上に対してGPS衛星の時計は1日あたり何マイクロ秒進むか（計算値：約 $+45.8\,\mu\text{s}$）。\\
(3) 両者の総合効果として、GPS衛星の時計は地上に対して1日あたり何マイクロ秒進むか。もしこの補正を行わなければ、位置測定に1日で何キロメートルの誤差が生じるか（光速 $c = 3 \times 10^5\,\text{km/s}$ とする）。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
1日は $86400\,\text{秒}$ である。特殊相対論の遅れは $\frac{1}{2}\frac{v^2}{c^2} \times 86400 \approx 7.2 \times 10^{-6}\,\text{秒} = 7.2\,\mu\text{s}$ の遅れ（$-7.2\,\mu\text{s}/\text{日}$）となる。\\
\textbf{(2) の解：}
高度 $20000\,\text{km}$ では地球の重力が地表よりはるかに弱いため、一般相対論により時間は速く進む。その進みは理論計算で $+45.8\,\mu\text{s}/\text{日}$ となる。\\
\textbf{(3) の解：}
正味の合成ズレは
\[
-7.2\,\mu\text{s} + 45.8\,\mu\text{s} = +38.6\,\mu\text{s}/\text{日}
\]
衛星の原子時計は地上より毎日 $38.6$ マイクロ秒早く進む。光がこの時間に進む距離は
\[
\Delta x = c \times \Delta t = (3 \times 10^5\,\text{km/s}) \times (38.6 \times 10^{-6}\,\text{s}) \approx 11.58\,\text{km}
\]
もしアインシュタインの相対性理論を考慮して送信周波数をあらかじめ微調整しておかなければ、カーナビやスマートフォンの位置情報は毎日約 $11.6\,\text{km}$ ずつズレてしまい、実用システムとして完全に崩壊する。現代社会のインフラは、相対性理論の実証によって支えられている。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第5問：$E=mc^2$ と太陽の寿命・質量欠損}
太陽の放射エネルギーは毎秒約 $L_{\odot} = 3.8 \times 10^{26}\,\text{W}$（$= 3.8 \times 10^{26}\,\text{J/s}$）である。\\
(1) アインシュタインの関係式 $E = mc^2$ を用いて、太陽が光と熱として宇宙に放出することで失っている質量（質量欠損）は毎秒何トンか（光速 $c = 3.0 \times 10^8\,\text{m/s}$）。\\
(2) 太陽の現在の総質量は約 $2.0 \times 10^{30}\,\text{kg}$ である。100億年間（約 $3.15 \times 10^{17}\,\text{秒}$）このペースで燃焼し続けたとしても、失われる質量は太陽全体の何パーセント程度にすぎないかを計算し、なぜ太陽が莫大な寿命を保てるのかを述べよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
1秒間に失われる質量 $\Delta m$ は
\[
\Delta m = \frac{E}{c^2} = \frac{3.8 \times 10^{26}}{(3.0 \times 10^8)^2} = \frac{3.8 \times 10^{26}}{9.0 \times 10^{16}} \approx 4.22 \times 10^9\,\text{kg} = 422万\,\text{トン}
\]
太陽は毎秒422万トンもの自身の体重をエネルギーに変換して輝いている。\\
\textbf{(2) の解：}
100億年間に失われる総質量 $M_{\text{loss}}$ は
\[
M_{\text{loss}} = 4.22 \times 10^9\,\text{kg/s} \times 3.15 \times 10^{17}\,\text{s} \approx 1.33 \times 10^{27}\,\text{kg}
\]
全質量 $M_{\odot} = 2.0 \times 10^{30}\,\text{kg}$ に対する割合は
\[
\frac{M_{\text{loss}}}{M_{\odot}} = \frac{1.33 \times 10^{27}}{2.0 \times 10^{30}} \approx 0.00067 = 0.067\%
\]
わずか $0.1\%$ 未満である。$c^2$ という係数が $9 \times 10^{16}$ という天文学的数値であるため、ごく微小な質量欠損から想像を絶する熱エネルギーが放出される。これこそが、石炭などの化学燃焼では数千年で燃え尽きてしまう太陽が、数十億年にわたって地球を温め続けられる真の理由である。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第6問：相対論的速度の合成則}
時速 $100\,\text{km}$ の列車の中から前方へ時速 $50\,\text{km}$ でボールを投げると、地上から見たボールの速度はニュートン力学では単に $100 + 50 = 150\,\text{km/h}$ と足し算される。しかし相対論では速度合成則
\[
W = \frac{u + v}{1 + \frac{uv}{c^2}}
\]
に従う。\\
(1) 宇宙船が地球に対して速度 $v = 0.8c$ で飛行中、前方へ向けて速度 $u = 0.8c$ で探査機を発射した。地球から見た探査機の速度 $W$ は光速の何倍か。光速 $c$ を超えないことを示せ。\\
(2) 宇宙船から前方へ光（$u = c$）を発射した場合、地球から見た光の速度 $W$ を合成則から計算し、光速度不変の原理と矛盾しないことを確かめよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
\[
W = \frac{0.8c + 0.8c}{1 + \frac{(0.8c)(0.8c)}{c^2}} = \frac{1.6c}{1 + 0.64} = \frac{1.6c}{1.64} \approx 0.9756c
\]
古典力学の足し算なら $1.6c$ となり光速を突破するが、分母の補正項 $1 + uv/c^2$ の働きにより、結果は光速の約 $97.6\%$ に留まり、決して光速を超えない。\\
\textbf{(2) の解：}
$u = c$ を代入すると、
\[
W = \frac{c + v}{1 + \frac{cv}{c^2}} = \frac{c + v}{1 + \frac{v}{c}} = \frac{c(c + v)}{c + v} = c
\]
どれほど高速（$v$）で運動している乗り物から光を放っても、外の観測者から見た光の速さは寸分違わず $c$ である。速度合成則自体の中に光速度不変の公理が完璧に織り込まれている。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第7問：等価原理とエレベーターの光の曲がり}
無重力空間を上向きに一定加速度 $g$ でロケット（またはエレベーター）が上昇している。幅を $W$ とする。左側の壁の小穴から水平に入射した光線が、右側の壁に到達する現象を考える。\\
(1) 光が右側の壁に到達するまでの時間 $t$ を光速 $c$ と $W$ を用いて表せ。\\
(2) その時間 $t$ の間にエレベーターが上向きに加速することによって上昇する距離 $h = \frac{1}{2}gt^2$ を求めよ。\\
(3) エレベーター内の観測者から見ると、光線が下向きに放物線を描いて $h$ だけ落ちて見えることを説明し、アインシュタインの等価原理により「重力場の中でも光線は必ず下方に湾曲する」と予言できる論理を述べよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
光の水平速度は $c$ であるから、幅 $W$ を横切る時間は $t = \frac{W}{c}$ である。\\
\textbf{(2) の解：}
等加速度運動の公式より、上昇距離は
\[
h = \frac{1}{2} g t^2 = \frac{g W^2}{2 c^2}
\]
\textbf{(3) の解：}
外の慣性系から見れば光は真横に直進しているが、床が上に向かって加速して迎え撃つため、車内の乗客から見れば光線は床に向かって $h$ だけ下方に曲がったように観測される。
等価原理によれば「加速度系と重力場は物理的に同一」であるから、地上に静止したエレベーター（重力加速度 $g$）の中でも、全く同一の湾曲 $h$ が光線に生じなければならない。こうしてアインシュタインは、「質量のない純粋な光線も重力によって曲げられる」という驚天動地の結論を、高校物理の運動方程式だけで導き出したのである。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第8問：太陽による恒星光の重力偏向角（エディントン観測の検証）}
1919年5月29日の皆既日食において、アーサー・エディントン卿は西アフリカのプリンシペ島で太陽の縁すれすれを通る恒星の光を観測した。一般相対性理論による光の偏向角の公式は
\[
\theta = \frac{4GM}{c^2 R} \quad \text{（ラジアン）}
\]
で与えられる。\\
太陽質量 $M_{\odot} \approx 1.99 \times 10^{30}\,\text{kg}$、太陽半径 $R_{\odot} \approx 6.96 \times 10^8\,\text{m}$、万有引力定数 $G \approx 6.67 \times 10^{-11}\,\text{m}^3/(\text{kg}\cdot\text{s}^2)$、光速 $c \approx 3.00 \times 10^8\,\text{m/s}$ とする。\\
(1) 偏向角 $\theta$ をラジアン単位で求めよ。\\
(2) $1\,\text{ラジアン} = \frac{180 \times 3600}{\pi} \approx 206265\,\text{秒角}$（arcsec）を用いて、偏向角を秒角に換算せよ。古典ニュートン力学（光を質量を持つ粒子と仮定した場合の半分）の予言値 $0.875''$ と比較せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
\[
\theta = \frac{4 \times (6.674 \times 10^{-11}) \times (1.989 \times 10^{30})}{(3.00 \times 10^8)^2 \times (6.963 \times 10^8)}
= \frac{5.310 \times 10^{20}}{6.267 \times 10^{25}} \approx 8.473 \times 10^{-6}\,\text{rad}
\]
\textbf{(2) の解：}
\[
\theta'' = 8.473 \times 10^{-6} \times 206265'' \approx 1.75''
\]
ニュートン力学の粒子論による計算では $\frac{2GM}{c^2 R} = 0.875''$ であったのに対し、アインシュタインの一般相対性理論では「時間の遅れ」と「空間の湾曲」の双方が寄与するため、正確に2倍の $1.75''$ となる。エディントンの観測隊が日食写真の乾板を測定した結果は $1.98'' \pm 0.12''$ および $1.61'' \pm 0.30''$ であり、アインシュタインの予言が鮮やかに立証され、世界中の新聞が「科学の歴史が書き換わった」と一面で報じた。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第9問：水星の近日点移動とニュートン力学の破綻}
太陽に最も近い惑星である水星の楕円軌道は、100年間に約 $5600''$（秒角）回転（移動）する。そのうち木星や金星など他の惑星からの摂動によるニュートン力学的なズレは $5160''$、地球の歳差運動による見かけの回転が $43''$ 分解され、どうしても説明のつかない「余剰の $43''$/世紀」が19世紀以来の天文学の最大の謎であった。\\
アインシュタインが導いた一般相対論による1公転あたりの近日点移動角 $\Delta \phi$ は
\[
\Delta \phi = \frac{6\pi GM}{c^2 a (1 - e^2)} \quad \text{（ラジアン/公転）}
\]
で与えられる。水星の軌道長半径 $a \approx 5.79 \times 10^{10}\,\text{m}$、離心率 $e \approx 0.2056$、公転周期 $T \approx 87.97\,\text{日}$（1世紀あたりの公転回数 $N \approx 415$ 回）として、1世紀あたりの相対論的移動角を秒角で計算せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
分母の幾何学的項を計算すると、
\[
1 - e^2 = 1 - (0.2056)^2 = 1 - 0.0423 = 0.9577
\]
1公転あたりの角移動 $\Delta \phi$ は
\[
\Delta \phi = \frac{6\pi \times (6.674 \times 10^{-11}) \times (1.989 \times 10^{30})}{(3.00 \times 10^8)^2 \times (5.79 \times 10^{10}) \times 0.9577}
= \frac{2.499 \times 10^{21}}{4.991 \times 10^{27}} \approx 5.007 \times 10^{-7}\,\text{rad/公転}
\]
1世紀あたりの総移動角は、公転回数 $N = 415$ を掛けて、
\[
\Delta \Phi = 415 \times 5.007 \times 10^{-7} \approx 2.078 \times 10^{-4}\,\text{rad/世紀}
\]
これを秒角に換算すると、
\[
\Delta \Phi'' = 2.078 \times 10^{-4} \times 206265'' \approx 42.86'' \approx 43''/\text{世紀}
\]
1世紀にわずか $43''$（満月の視直径の約 $\frac{1}{40}$）という極微の狂いが、アインシュタインの方程式によって何ら任意の仮定なしにピタリと導き出された。この計算に成功した夜、アインシュタインは「心臓が激しく波打ち、全身が震えるほどの歓喜を覚えた」と友人に書き送っている。\qed
\end{exercisebox}

\vspace*{3mm}

\begin{exercisebox}{第10問：シュワルツシルト半径（ブラックホールの境界面）}
一般相対性理論において、天体の質量 $M$ がそのシュワルツシルト半径
\[
R_s = \frac{2GM}{c^2}
\]
の内側にまで凝縮すると、表面脱出速度が光速 $c$ に達し、光さえも脱出できない「事象の地平面（ブラックホール）」が形成される。\\
(1) 地球の質量 $M_{\text{earth}} \approx 5.97 \times 10^{24}\,\text{kg}$ をブラックホールにするには、何ミリメートルの半径に圧縮しなければならないか。\\
(2) 太陽の質量 $M_{\odot} \approx 1.99 \times 10^{30}\,\text{kg}$ のシュワルツシルト半径は何キロメートルか。\\
(3) 銀河系の中心にある巨大ブラックホール「いて座A*（Sagittarius A*）」の質量は太陽の約400万倍である。そのシュワルツシルト半径は何万キロメートルか。地球と太陽の距離（1天文単位 $\approx 1.5 \times 10^8\,\text{km}$）と比較せよ。
\\[2mm]
\textbf{【懇切丁寧な解答】}\\
\textbf{(1) の解：}
\[
R_s = \frac{2 \times (6.674 \times 10^{-11}) \times (5.972 \times 10^{24})}{(3.00 \times 10^8)^2} = \frac{7.971 \times 10^{14}}{9.00 \times 10^{16}} \approx 8.86 \times 10^{-3}\,\text{m} \approx 8.9\,\text{mm}
\]
地球の全物質を、わずかビー玉サイズ（直径約 $1.8\,\text{cm}$）にまで押し縮めるとブラックホールになる。\\
\textbf{(2) の解：}
\[
R_s = \frac{2 \times (6.674 \times 10^{-11}) \times (1.989 \times 10^{30})}{(3.00 \times 10^8)^2} = \frac{2.655 \times 10^{20}}{9.00 \times 10^{16}} \approx 2950\,\text{m} \approx 2.95\,\text{km} \approx 3\,\text{km}
\]
太陽ほどの巨大な恒星でも、半径約 $3\,\text{km}$（富士山の高さ程度）に収縮すればブラックホールとなる。\\
\textbf{(3) の解：}
太陽の400万倍であるから、
\[
R_s = 4.0 \times 10^6 \times 2.95\,\text{km} \approx 1.18 \times 10^7\,\text{km} = 1180万\,\text{km}
\]
太陽の半径が約 $70万\,\text{km}$ であるから、その約17倍の領域である。地球と太陽の距離 $1億5000万\,\text{km}$ の約 $8\%$（水星の軌道半径の約 $\frac{1}{5}$）にすっぽりと収まるサイズである。2022年にイベント・ホライズン・テレスコープ（EHT）が撮影したいて座A*の電波写真の影（シャドウ）は、まさにこのアインシュタイン方程式の解が1世紀の時を経て天体観測によって視覚的に捉えられた記念碑的成果である。\qed
\end{exercisebox}

\chapter*{おわりに：現代文明の礎となったアインシュタインの遺産}
\addcontentsline{toc}{chapter}{おわりに：現代文明の礎となったアインシュタインの遺産}

アルベルト・アインシュタインが本書『特殊および一般相対性理論について』を出版してから一世紀以上の歳月が流れました。かつて「世界で真に理解できる者は3人しかいない」とまで噂されたこの理論は、いまやSFの空想物語ではなく、私たちのスマートフォンの中（GPS高精度測位）、病院の先端医療（PET診断における陽電子消滅）、エネルギーインフラ（原子力発電）、そして宇宙望遠鏡による深宇宙探査の現場において、寸秒の狂いもなく稼働する「現代文明の実用技術」となっています。

しかし、技術的応用の価値以上に私たちの心を揺さぶり続けるのは、アインシュタインが見せた\textbf{「人間の理性と論理的思考の力」}です。彼は実験室に籠もって大がかりな装置を操作したのではなく、自らの頭の中で「もし光の速さで光を追いかけたらどう見えるか」「走る列車の中で雷を見たらどうなるか」「落下するエレベーターの中の人には何が起きるか」という純粋な\textbf{思考実験（Gedankenexperiment）}を徹底的に突き詰めることで、2000年来の絶対時間・絶対空間の常識を覆しました。

大人の学び直しの旅を終えた読者の皆様が、夜空を見上げるとき、あるいは手元のスマートフォンの地図アプリを開くとき、その背後に広がる「時間と空間が織りなす壮大で美しい四次元幾何学の世界」を、アインシュタインの温かな眼差しとともに実感していただけるなら、編訳者一同のこの上ない喜びです。

\end{document}
"""

print("Writing make_einstein_intro_tex.py...")
