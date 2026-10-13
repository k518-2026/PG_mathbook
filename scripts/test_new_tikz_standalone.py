# -*- coding: utf-8 -*-
"""
Generate and render all 12 TikZ figures as standalone PNGs to visually verify zero overlap.
"""
import os, subprocess, re

LATEX_TEMPLATE = r'''\documentclass[preview,border=12pt]{standalone}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,calc,patterns,backgrounds}

\definecolor{primaryblue}{RGB}{24, 76, 120}
\definecolor{softblue}{RGB}{235, 243, 250}
\definecolor{darkslate}{RGB}{44, 62, 80}
\definecolor{warmamber}{RGB}{217, 119, 6}
\definecolor{softamber}{RGB}{254, 243, 199}
\definecolor{crimson}{RGB}{185, 28, 28}
\definecolor{softrose}{RGB}{255, 228, 230}
\definecolor{accentgreen}{RGB}{16, 120, 70}
\definecolor{softgreen}{RGB}{236, 253, 245}

\begin{document}
{BODY}
\end{document}
'''

def get_figures():
    figs = {}
    
    # ---------------------------------------------------------
    # Fig 1.1: 2大基本記号 d と \int の直観的構造
    # ---------------------------------------------------------
    figs[1] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Outer container
    \draw[thick, fill=softblue, draw=primaryblue, rounded corners=6pt] (-7.6, -4.2) rectangle (7.6, 4.0);
    \node[draw=primaryblue, fill=white, rounded corners=4pt, inner sep=5pt] at (0, 3.2) {\bfseries シルバヌス・P・トンプソン『Calculus Made Easy』の基本精神};
    
    % Differentiation box
    \node[draw=primaryblue, fill=white, rounded corners=4pt, align=center, text width=3.8cm, inner sep=6pt] at (-4.7, 0.9) {
        \textbf{微分（$d$：細分化）}\\[3pt]
        \footnotesize ラテン語 \textit{differentia}\\[2pt]
        \footnotesize ほんの少しの微小増分 $dx$\\[2pt]
        \footnotesize 「微小なかけら」への分解
    };
    
    % Integration box
    \node[draw=crimson, fill=softrose, rounded corners=4pt, align=center, text width=3.8cm, inner sep=6pt] at (4.7, 0.9) {
        \textbf{積分（$\int$：総和化）}\\[3pt]
        \footnotesize ラテン語 \textit{summa}（長いS）\\[2pt]
        \footnotesize 微小量 $f(x)dx$ の連続和\\[2pt]
        \footnotesize 「全体」の組み立て・復元
    };
    
    % Center arrows with clear spacing
    \draw[->, very thick, warmamber] (-2.2, 1.4) -- (2.2, 1.4);
    \node[above=3pt] at (0, 1.4) {\bfseries\small 微分と積分は互いに逆演算};
    \draw[<-, very thick, warmamber] (-2.2, 0.5) -- (2.2, 0.5);
    \node[below=3pt] at (0, 0.5) {\footnotesize 過程の逆行（Reversing the Process）};
    
    % Bottom quote box safely inside outer rectangle
    \node[draw=darkslate, fill=softgreen, rounded corners=4pt, text width=13.6cm, align=center, inner sep=6pt] at (0, -2.6) {
        \textbf{トンプソンの箴言}：\textit{What one fool can do, another can.}\\
        \footnotesize （一人の人間が理解できる美しい真理は、他のどんな人間にも必ず直観的に理解できる）
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 2.1: 正方形の幾何学的拡大と2次微小量
    # ---------------------------------------------------------
    figs[2] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Original Square
    \fill[softblue] (0, 0) rectangle (3.5, 3.5);
    \draw[thick, primaryblue] (0, 0) rectangle (3.5, 3.5);
    \node at (1.75, 1.75) {\large\textbf{元の正方形} $x^2$};
    
    % Strips dx
    \fill[softamber] (0, 3.5) rectangle (3.5, 4.3);
    \draw[thick, warmamber] (0, 3.5) rectangle (3.5, 4.3);
    \node at (1.75, 3.9) {\footnotesize 高さ $dx$ の帯：$x \cdot dx$};
    
    \fill[softamber] (3.5, 0) rectangle (4.3, 3.5);
    \draw[thick, warmamber] (3.5, 0) rectangle (4.3, 3.5);
    \node[rotate=-90] at (3.9, 1.75) {\footnotesize 幅 $dx$ の帯：$x \cdot dx$};
    
    % Corner (dx)^2
    \fill[softrose] (3.5, 3.5) rectangle (4.3, 4.3);
    \draw[thick, crimson] (3.5, 3.5) rectangle (4.3, 4.3);
    
    \draw[->, thick, crimson] (4.9, 4.7) -- (4.05, 4.05);
    \node[above right, crimson] at (4.4, 4.6) {\footnotesize 極小正方形 $(dx)^2$（2次微小量）};
    
    % Dimensions
    \draw[<->, thick] (0, -0.4) -- (3.5, -0.4) node[midway, below] {$x$};
    \draw[<->, thick] (3.5, -0.4) -- (4.3, -0.4) node[midway, below] {$dx$};
    \draw[<->, thick] (-0.4, 0) -- (-0.4, 3.5) node[midway, left] {$x$};
    \draw[<->, thick] (-0.4, 3.5) -- (-0.4, 4.3) node[midway, left] {$dx$};
    
    % Expansion Box
    \node[draw=accentgreen, fill=softgreen, rounded corners=4pt, text width=6.2cm, inner sep=7pt] at (7.8, 2.1) {
        \textbf{微小増分の展開}\\[4pt]
        $(x + dx)^2 = x^2 + 2x dx + (dx)^2$\\[4pt]
        \footnotesize $\bullet$ 1次微小量：$2x dx$（本質的増分）\\
        $\bullet$ 2次微小量：$(dx)^2$（桁違いに極小）\\[4pt]
        \normalsize \textbf{結論}：極限 $dx \to 0$ において $(dx)^2$ は\\
        安全に無視され、$\frac{d(x^2)}{dx} = 2x$ となる！
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 3.1: 割線から接線への極限推移と瞬間変化率
    # ---------------------------------------------------------
    figs[3] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Top Header Box
    \node[draw=warmamber, fill=softamber, rounded corners=4pt, inner sep=5pt] at (4.0, 4.7) {
        \bfseries 相対的成長度：$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \frac{dy}{dx}$（瞬間の変化率）
    };
    
    % Axes
    \draw[->, thick] (0, 0) -- (8.2, 0) node[right] {\footnotesize 入力 $x$};
    \draw[->, thick] (0, 0) -- (0, 3.8) node[left] {\footnotesize 出力 $y$};
    
    % Curve y = 0.05 x^2 + 0.2 x + 0.6
    \draw[very thick, primaryblue, domain=0.8:6.5, samples=50] plot (\x, {0.05*\x*\x + 0.2*\x + 0.6});
    \node[above, primaryblue] at (1.8, 2.2) {\bfseries\footnotesize 曲線 $y = f(x)$};
    
    % Points P and Q
    \coordinate (P) at (2.0, 1.2);
    \coordinate (Q) at (5.2, 2.99);
    
    % Secant line (dashed): slope = (2.99-1.2)/3.2 = 0.56
    \draw[thick, dashed, darkslate] (0.8, 0.53) -- (6.6, 3.78);
    \node[right, darkslate] at (6.6, 3.78) {\bfseries\footnotesize 割線の傾き $\frac{\Delta y}{\Delta x}$};
    
    % Tangent line at P: slope = 2*0.05*2 + 0.2 = 0.4
    \draw[very thick, crimson] (0.8, 0.72) -- (4.8, 2.32);
    % Tangent label placed strictly between x=2.0 and x=5.2 underneath tangent line
    \node[below=3pt, crimson] at (3.8, 1.35) {\bfseries\scriptsize 接線の傾き $\frac{dy}{dx} = f'(x)$};
    
    % Points
    \filldraw[crimson] (P) circle (2pt) node[above left=2pt, darkslate] {$P(x, y)$};
    \filldraw[primaryblue] (Q) circle (2pt) node[below right=2pt, darkslate] {$Q(x+\Delta x, y+\Delta y)$};
    
    % Vertical projection dashed lines
    \draw[dotted, thick] (P) -- (2.0, 0) node[below] {$x$};
    \draw[dotted, thick] (Q) -- (5.2, 0) node[below] {$x + \Delta x$};
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 4.1: ベキ関数の微分公式における指数体系
    # ---------------------------------------------------------
    figs[4] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Outer Frame
    \draw[thick, fill=softblue, draw=primaryblue, rounded corners=6pt] (-7.6, -4.2) rectangle (7.6, 4.0);
    \node[draw=primaryblue, fill=white, rounded corners=4pt, inner sep=5pt] at (0, 3.2) {\bfseries ベキ関数 $y = x^n$ の微分公式とその完全体系};
    
    % 3 Columns
    \node[draw=primaryblue, fill=white, rounded corners=4pt, text width=3.8cm, align=center, inner sep=5pt] at (-4.8, 0.9) {
        \textbf{自然数指数 $n \in \mathbb{N}$}\\[3pt]
        \small $y = x^1 \implies y' = 1$\\[2pt]
        $y = x^2 \implies y' = 2x$\\[2pt]
        $y = x^3 \implies y' = 3x^2$\\[3pt]
        \footnotesize 一般則：$y' = n x^{n-1}$
    };
    
    \node[draw=warmamber, fill=softamber, rounded corners=4pt, text width=3.8cm, align=center, inner sep=5pt] at (0, 0.9) {
        \textbf{負の整数（反比例）}\\[3pt]
        \small $y = x^{-1} = \frac{1}{x} \implies y' = -\frac{1}{x^2}$\\[2pt]
        $y = x^{-2} = \frac{1}{x^2} \implies y' = -\frac{2}{x^3}$\\[4pt]
        \footnotesize ベキ乗規則が完全成立！
    };
    
    \node[draw=accentgreen, fill=softgreen, rounded corners=4pt, text width=3.8cm, align=center, inner sep=5pt] at (4.8, 0.9) {
        \textbf{有理数指数（根号）}\\[3pt]
        \small $y = x^{1/2} = \sqrt{x} \implies y' = \frac{1}{2\sqrt{x}}$\\[2pt]
        $y = x^{1/3} = \sqrt[3]{x} \implies y' = \frac{1}{3\sqrt[3]{x^2}}$\\[4pt]
        \footnotesize 実数全体 $n \in \mathbb{R}$ へ拡張
    };
    
    % Bottom General Rule Box
    \node[draw=darkslate, fill=white, rounded corners=4pt, text width=13.6cm, align=center, inner sep=6pt] at (0, -2.6) {
        \textbf{トンプソンの普遍則}：定数倍 $c$ を含む一般形\\[2pt]
        \normalsize $\frac{d}{dx}(c x^n) \;=\; c \cdot n x^{n-1}$ は数学全般の礎石である
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 5.1: 長方形の面積変化による積の微分公式
    # ---------------------------------------------------------
    figs[5] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Original Rectangle u x v
    \fill[softblue] (0, 0) rectangle (3.8, 2.8);
    \draw[thick, primaryblue] (0, 0) rectangle (3.8, 2.8);
    \node at (1.9, 1.4) {\large\textbf{元の面積} $y = u \cdot v$};
    
    % Top strip: u * dv
    \fill[softamber] (0, 2.8) rectangle (3.8, 3.6);
    \draw[thick, warmamber] (0, 2.8) rectangle (3.8, 3.6);
    \node at (1.9, 3.2) {\footnotesize 上の増加帯：$u \cdot dv$};
    
    % Right strip: v * du (width 1.4cm for comfortable text)
    \fill[softamber] (3.8, 0) rectangle (5.2, 2.8);
    \draw[thick, warmamber] (3.8, 0) rectangle (5.2, 2.8);
    \node[align=center] at (4.5, 1.4) {\footnotesize 右の帯\\[2pt] $v \cdot du$};
    
    % Corner: du * dv
    \fill[softrose] (3.8, 2.8) rectangle (5.2, 3.6);
    \draw[thick, crimson] (3.8, 2.8) rectangle (5.2, 3.6);
    
    % Label for corner
    \draw[->, thick, crimson] (4.5, 4.5) -- (4.5, 3.7);
    \node[above, crimson] at (4.5, 4.5) {\footnotesize 極小長方形 $du \cdot dv$（2次微小量）};
    
    % Dimensions
    \draw[<->, thick] (0, -0.4) -- (3.8, -0.4) node[midway, below] {$u$};
    \draw[<->, thick] (3.8, -0.4) -- (5.2, -0.4) node[midway, below] {$du$};
    \draw[<->, thick] (-0.4, 0) -- (-0.4, 2.8) node[midway, left] {$v$};
    \draw[<->, thick] (-0.4, 2.8) -- (-0.4, 3.6) node[midway, left] {$dv$};
    
    % Algebra Box at Right (starting cleanly at x=6.8)
    \node[draw=accentgreen, fill=softgreen, rounded corners=4pt, text width=6.2cm, inner sep=6pt] at (10.0, 2.0) {
        \textbf{積の増分公式}\\[3pt]
        $d(uv) = (u + du)(v + dv) - uv$\\[2pt]
        $\phantom{d(uv)} = u \cdot dv + v \cdot du + du \cdot dv$\\[3pt]
        \footnotesize $\bullet$ 1次増分：$u \cdot dv + v \cdot du$\\
        $\bullet$ 2次増分：$du \cdot dv \to 0$（消去）\\[4pt]
        \normalsize \textbf{両辺を $dx$ で割ると：}\\[3pt]
        $\frac{d(uv)}{dx} = u \frac{dv}{dx} + v \frac{du}{dx}$
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 6.1: 連鎖律（チェイン・ルール）のメカニズム
    # ---------------------------------------------------------
    figs[6] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Outer Frame
    \draw[thick, fill=softamber!30, draw=warmamber, rounded corners=6pt] (-7.6, -4.2) rectangle (7.6, 4.0);
    \node[draw=warmamber, fill=white, rounded corners=4pt, inner sep=5pt] at (0, 3.2) {\bfseries 合成関数の微分法（連鎖律・チェインルール）のメカニズム};
    
    % 3 Variable Nodes
    \node[draw=primaryblue, fill=white, rounded corners=4pt, text width=3.4cm, align=center, inner sep=6pt] at (-5.0, 0.9) {
        \textbf{入力変数 $x$}\\[3pt]
        \footnotesize 微小変動 $dx$\\[4pt]
        \scriptsize すべての変化の源泉
    };
    
    \node[draw=accentgreen, fill=softgreen, rounded corners=4pt, text width=3.4cm, align=center, inner sep=6pt] at (0, 0.9) {
        \textbf{中間変数 $u = g(x)$}\\[3pt]
        \footnotesize 伝播量 $du = g'(x)dx$\\[4pt]
        \scriptsize ギア1の伝達比 $\frac{du}{dx}$
    };
    
    \node[draw=crimson, fill=softrose, rounded corners=4pt, text width=3.4cm, align=center, inner sep=6pt] at (5.0, 0.9) {
        \textbf{出力変数 $y = f(u)$}\\[3pt]
        \footnotesize 最終変動 $dy = f'(u)du$\\[4pt]
        \scriptsize ギア2の伝達比 $\frac{dy}{du}$
    };
    
    % Interconnecting Arrows with clear above/below labels
    \draw[->, very thick, warmamber] (-3.1, 0.9) -- (-1.9, 0.9);
    \node[above=4pt] at (-2.5, 0.9) {\bfseries\footnotesize $\frac{du}{dx}$};
    
    \draw[->, very thick, warmamber] (1.9, 0.9) -- (3.1, 0.9);
    \node[above=4pt] at (2.5, 0.9) {\bfseries\footnotesize $\frac{dy}{du}$};
    
    % Bottom Formula Box
    \node[draw=darkslate, fill=white, rounded corners=4pt, text width=13.6cm, align=center, inner sep=6pt] at (0, -2.6) {
        \textbf{連鎖律の代数公式}：\Large $\frac{dy}{dx} \;=\; \frac{dy}{du} \cdot \frac{du}{dx}$\\[3pt]
        \footnotesize （中間変数 $u$ の微小変化率を掛け合わせることで、合成関数の微分は一瞬で解ける）
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 7.1: 物体の運動における位置・速度・加速度
    # ---------------------------------------------------------
    figs[7] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Outer Frame
    \draw[thick, fill=softblue, draw=primaryblue, rounded corners=6pt] (-7.6, -4.2) rectangle (7.6, 4.0);
    \node[draw=primaryblue, fill=white, rounded corners=4pt, inner sep=5pt] at (0, 3.2) {\bfseries 時間変化と第2次導関数：運動力学の微積分階層};
    
    % 3 Kinematic Boxes
    \node[draw=primaryblue, fill=white, rounded corners=4pt, text width=3.4cm, align=center, inner sep=6pt] at (-5.0, 0.9) {
        \textbf{位置 $s(t)$}\\[3pt]
        \footnotesize 空間座標 $[\mathrm{m}]$\\[4pt]
        \scriptsize 自由落下 $s = \frac{1}{2}gt^2$
    };
    
    \node[draw=warmamber, fill=softamber, rounded corners=4pt, text width=3.4cm, align=center, inner sep=6pt] at (0, 0.9) {
        \textbf{速度 $v(t) = \frac{ds}{dt}$}\\[3pt]
        \footnotesize 1次導関数 $[\mathrm{m/s}]$\\[4pt]
        \scriptsize 瞬間の進行ペース $gt$
    };
    
    \node[draw=crimson, fill=softrose, rounded corners=4pt, text width=3.4cm, align=center, inner sep=6pt] at (5.0, 0.9) {
        \textbf{加速度 $a(t) = \frac{d^2s}{dt^2}$}\\[3pt]
        \footnotesize 2次導関数 $[\mathrm{m/s^2}]$\\[4pt]
        \scriptsize 重力加速度 $g$（定数）
    };
    
    % Interconnecting Arrows with clear labels
    \draw[->, very thick, warmamber] (-3.1, 0.9) -- (-1.9, 0.9);
    \node[above=4pt] at (-2.5, 0.9) {\footnotesize 微分 $\frac{d}{dt}$};
    
    \draw[->, very thick, warmamber] (1.9, 0.9) -- (3.1, 0.9);
    \node[above=4pt] at (2.5, 0.9) {\footnotesize 微分 $\frac{d}{dt}$};
    
    % Bottom Newton Box
    \node[draw=darkslate, fill=white, rounded corners=4pt, text width=13.6cm, align=center, inner sep=6pt] at (0, -2.6) {
        \textbf{ニュートンの運動方程式}：\Large $F \;=\; m \cdot a \;=\; m \frac{d^2s}{dt^2}$\\[3pt]
        \footnotesize （力は質量 $\times$ 位置の第2次導関数である）
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 8.1: 極大・極小における接線の傾きと凹凸判定
    # ---------------------------------------------------------
    figs[8] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Axes
    \draw[->, thick] (0, 0) -- (8.5, 0) node[right] {$x$};
    \draw[->, thick] (0, 0) -- (0, 4.6) node[above] {$y = f(x)$};
    
    % Cubic curve: Max at x=2.8, Min at x=5.8, Inflection at x=4.3
    \draw[very thick, primaryblue, domain=1.4:6.3, samples=50] 
        plot (\x, {0.12*(\x-4.3)*(\x-4.3)*(\x-4.3) - 0.81*(\x-4.3) + 2.8});
    
    % Local Max: x=2.8, y=3.61
    \coordinate (MaxPt) at (2.8, 3.61);
    \filldraw[crimson] (MaxPt) circle (2pt);
    \draw[thick, dashed, crimson] (1.8, 3.61) -- (3.8, 3.61);
    \draw[dotted, thick] (MaxPt) -- (2.8, 0) node[below] {$x_{\mathrm{max}}$};
    \node[above=8pt, crimson] at (MaxPt) {\bfseries\small 極大値 $\left(\frac{dy}{dx} = 0,\ \frac{d^2y}{dx^2} < 0\right)$};
    
    % Inflection point: x=4.3, y=2.8, callout to top-right empty area
    \coordinate (InfPt) at (4.3, 2.8);
    \filldraw[darkslate] (InfPt) circle (2pt);
    \draw[->, thick, darkslate] (5.4, 3.5) -- (4.45, 2.9);
    \node[above right, darkslate] at (5.3, 3.4) {\footnotesize\textbf{変曲点} $\left(\frac{d^2y}{dx^2} = 0\right)$};
    
    % Local Min: x=5.8, y=1.99
    \coordinate (MinPt) at (5.8, 1.99);
    \filldraw[accentgreen] (MinPt) circle (2pt);
    \draw[thick, dashed, accentgreen] (4.8, 1.99) -- (6.8, 1.99);
    \draw[dotted, thick] (MinPt) -- (5.8, 0) node[below] {$x_{\mathrm{min}}$};
    \node[below=8pt, accentgreen] at (MinPt) {\bfseries\small 極小値 $\left(\frac{dy}{dx} = 0,\ \frac{d^2y}{dx^2} > 0\right)$};
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 9.1: ネイピア数 e の幾何学的自己同一性
    # ---------------------------------------------------------
    figs[9] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Axes
    \draw[->, thick] (-3.8, 0) -- (4.0, 0) node[right] {$x$};
    \draw[->, thick] (0, 0) -- (0, 4.8) node[above] {$y$};
    
    % Curve y = e^x
    \draw[very thick, primaryblue, domain=-3.5:1.35, samples=60] plot (\x, {exp(\x)});
    \node[right, primaryblue] at (1.35, 3.8) {\bfseries 指数関数 $y = e^x$};
    
    % Point at x=1, y=e=2.718
    \coordinate (EPt) at (1.0, 2.718);
    \filldraw[crimson] (EPt) circle (2pt);
    
    % Tangent line: y = e*x
    \draw[thick, dashed, crimson] (0, 0) -- (1.4, 3.805);
    \node[right, crimson] at (1.4, 2.6) {\footnotesize 接線（傾き $= e$）};
    
    % Projections with y=e clearly above dashed line
    \draw[dotted, thick] (EPt) -- (1.0, 0);
    \draw[dotted, thick] (EPt) -- (0, 2.718);
    \node[above=2pt, primaryblue] at (0.5, 2.718) {\footnotesize $y = e$};
    
    % Box at left (fully clear of y axis)
    \node[draw=accentgreen, fill=softgreen, rounded corners=4pt, text width=2.9cm, align=center, inner sep=6pt] at (-2.3, 3.4) {
        \textbf{自己増殖の奇跡}\\[4pt]
        $\frac{d}{dx}(e^x) = e^x$\\[4pt]
        \footnotesize 傾き $=$ 高さ
    };
    
    % Subtangent at bottom
    \node[below=2pt] at (1.0, 0) {$x = 1$};
    \draw[<->, thick, warmamber] (0, -0.6) -- (1.0, -0.6);
    \node[below=3pt, warmamber] at (0.5, -0.6) {\footnotesize 次接線長 $= 1$（一定）};
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 10.1: 三角関数と円運動の微分
    # ---------------------------------------------------------
    figs[10] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Axes
    \draw[->, thick] (-3.4, 0) -- (3.6, 0) node[right] {\footnotesize $\cos\theta$};
    \draw[->, thick] (0, -3.2) -- (0, 3.6) node[above] {\footnotesize $\sin\theta$};
    
    % Circle radius 2.6
    \draw[thick, darkslate] (0, 0) circle (2.6);
    
    % Angle theta = 45 deg
    % P = (2.6 cos 45, 2.6 sin 45) = (1.838, 1.838)
    \coordinate (P) at (1.838, 1.838);
    \draw[very thick, primaryblue] (0, 0) -- (P);
    \node[below right=2pt, primaryblue] at (0.9, 0.8) {\footnotesize 半径 $r=1$};
    \filldraw[primaryblue] (P) circle (2pt) node[right=3pt] {$P(\cos\theta, \sin\theta)$};
    
    % Angle arc
    \draw[->, thick, warmamber] (0.7, 0) arc (0:45:0.7);
    \node[warmamber] at (0.95, 0.4) {\footnotesize $\theta$};
    
    % Velocity vector (tangent, length 1.6)
    % VEnd = (0.707, 2.969)
    \coordinate (VEnd) at (0.707, 2.969);
    \draw[->, very thick, crimson] (P) -- (VEnd);
    % Velocity vector label inside triangle, below-left of tangent arrow
    \node[below left=2pt, crimson] at (1.25, 2.45) {\bfseries\footnotesize 速度ベクトル $\vec{v}$};
    
    % Components of velocity vector:
    % 1. Vertical component: up from P: (1.838, 1.838) -> (1.838, 2.969)
    \draw[thick, dashed, crimson] (P) -- (1.838, 2.969);
    \node[right=2pt, crimson] at (1.838, 2.4) {\footnotesize 垂直：$\cos\theta$};
    % 2. Horizontal component: left from (1.838, 2.969) -> (0.707, 2.969)
    \draw[thick, dashed, crimson] (1.838, 2.969) -- (VEnd);
    \node[above=2pt, crimson] at (1.27, 2.98) {\footnotesize 水平：$-\sin\theta$};
    
    % Bottom Summary Box
    \node[draw=primaryblue, fill=softblue, rounded corners=4pt, text width=11.0cm, align=center, inner sep=5pt] at (0, -3.7) {
        \textbf{三角関数の導関数}：$\frac{d}{d\theta}(\sin\theta) = \cos\theta$、\quad $\frac{d}{d\theta}(\cos\theta) = -\sin\theta$
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 11.1: 微分の逆演算としての積分と積分定数
    # ---------------------------------------------------------
    figs[11] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Outer Frame
    \draw[thick, fill=softrose!30, draw=crimson, rounded corners=6pt] (-7.6, -4.2) rectangle (7.6, 4.0);
    \node[draw=crimson, fill=white, rounded corners=4pt, inner sep=5pt] at (0, 3.2) {\bfseries 微分と積分の双対性：過程の逆行（Reversing the Process）};
    
    % Left Box: Primitive Functions
    \node[draw=primaryblue, fill=white, rounded corners=4pt, text width=4.0cm, align=center, inner sep=6pt] at (-4.8, 0.9) {
        \textbf{原始関数族}\\[3pt]
        \Large $F(x) + C$\\[3pt]
        \footnotesize 積分定数 $C$ の任意性\\[2pt]
        \footnotesize 例：$\frac{1}{3}x^3 + C$\\[3pt]
        \scriptsize 「元の滑らかな全体」
    };
    
    % Right Box: Derivatives
    \node[draw=accentgreen, fill=white, rounded corners=4pt, text width=4.0cm, align=center, inner sep=6pt] at (4.8, 0.9) {
        \textbf{導関数 $f(x)$}\\[3pt]
        \footnotesize 瞬間の傾き・変化率\\[3pt]
        \footnotesize 例：$x^2$\\[4pt]
        \scriptsize 「微小なかけらの勢い」
    };
    
    % Center Arrows with clear labels (gap: -2.8 to 2.8 = 5.6cm)
    \draw[->, very thick, primaryblue] (-2.4, 1.4) -- (2.4, 1.4);
    \node[above=3pt] at (0, 1.4) {\bfseries\small 微分演算 $\frac{d}{dx}$（定数 $C$ の消失）};
    
    \draw[<-, very thick, crimson] (-2.4, 0.4) -- (2.4, 0.4);
    \node[below=3pt] at (0, 0.4) {\bfseries\small 不定積分 $\int \dots dx$（定数 $C$ の創出）};
    
    % Bottom Formula Box
    \node[draw=darkslate, fill=white, rounded corners=4pt, text width=13.6cm, align=center, inner sep=6pt] at (0, -2.6) {
        \textbf{基本積分公式}：\Large $\int x^n dx = \frac{1}{n+1}x^{n+1} + C \quad (n \neq -1)$、\quad $\int \frac{1}{x}dx = \ln|x| + C \quad (n = -1)$
    };
\end{tikzpicture}'''

    # ---------------------------------------------------------
    # Fig 12.1: 短冊の微小面積による区分求積と基本定理
    # ---------------------------------------------------------
    figs[12] = r'''\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]
    % Top Header Box
    \node[draw=warmamber, fill=softamber, rounded corners=4pt, inner sep=5pt] at (4.0, 4.6) {
        \bfseries 微積分学の基本定理：$\frac{dS}{dx} = f(x) \iff \int_a^b f(x)dx = F(b) - F(a)$
    };
    
    % Axes
    \draw[->, thick] (0, 0) -- (8.2, 0) node[right] {$x$};
    \draw[->, thick] (0, 0) -- (0, 3.8) node[left] {$y$};
    
    % Curve y = 0.04 x^2 + 0.12 x + 0.8
    \draw[very thick, primaryblue, domain=0.8:7.2, samples=60] plot (\x, {0.04*\x*\x + 0.12*\x + 0.8});
    \node[above left, primaryblue] at (6.8, 3.6) {\bfseries\footnotesize 曲線 $y = f(x)$};
    
    % a=1.8, b=6.2
    \coordinate (A) at (1.8, 0);
    \coordinate (B) at (6.2, 0);
    
    % Shaded Area S(x) from a=1.8 to x=3.6
    \fill[softblue, opacity=0.8] (1.8, 0) -- plot[domain=1.8:3.6] (\x, {0.04*\x*\x + 0.12*\x + 0.8}) -- (3.6, 0) -- cycle;
    \node at (2.7, 0.7) {\small\textbf{面積 $S(x)$}};
    
    % Strip dx at [3.6, 4.1]
    \fill[softamber] (3.6, 0) -- plot[domain=3.6:4.1] (\x, {0.04*\x*\x + 0.12*\x + 0.8}) -- (4.1, 0) -- cycle;
    \draw[thick, warmamber] (3.6, 0) -- (3.6, {0.04*3.6*3.6 + 0.12*3.6 + 0.8}) 
                         -- (4.1, {0.04*4.1*4.1 + 0.12*4.1 + 0.8}) -- (4.1, 0);
    
    % Strip label with clear arrow pointing from upper left
    \draw[<-, thick, warmamber] (3.85, 1.4) -- (2.6, 2.5);
    \node[above, warmamber] at (2.6, 2.5) {\bfseries\footnotesize 微小短冊 $dS \approx f(x)dx$};
    
    % Boundaries
    \draw[dotted, thick] (1.8, {0.04*1.8*1.8 + 0.12*1.8 + 0.8}) -- (1.8, 0) node[below] {$a$};
    \draw[dotted, thick] (6.2, {0.04*6.2*6.2 + 0.12*6.2 + 0.8}) -- (6.2, 0) node[below] {$b$};
    
    % Sub-labels on x axis
    \node[below=2pt] at (3.6, 0) {\footnotesize $x$};
    \node[below=14pt] at (4.1, 0) {\footnotesize $x+dx$};
\end{tikzpicture}'''
    return figs

def main():
    figs = get_figures()
    out_dir = 'test_figs_refined'
    os.makedirs(out_dir, exist_ok=True)
    
    for i in range(1, 13):
        prefix = os.path.join(out_dir, f'fig_{i:02d}')
        tex_path = f"{prefix}.tex"
        pdf_path = f"{prefix}.pdf"
        
        full_tex = LATEX_TEMPLATE.replace('{BODY}', figs[i])
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(full_tex)
        
        res = subprocess.run(['lualatex', '-interaction=nonstopmode', f'fig_{i:02d}.tex'], cwd=out_dir, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error compiling fig_{i:02d}:")
            print(res.stdout[-400:])
        else:
            # render png
            subprocess.run(['pdftoppm', '-png', '-r', '150', f'fig_{i:02d}.pdf', f'fig_{i:02d}'], cwd=out_dir, check=True)
            print(f"Rendered fig_{i:02d} successfully.")

if __name__ == '__main__':
    main()
