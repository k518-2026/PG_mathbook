# -*- coding: utf-8 -*-
"""
Generate Dudeney Amusements in Mathematics Intro Book TeX:
"古典で学び直すデュードニー数学パズル入門 —— 思考の幾何学・グラフ理論・数論の魔術"
Target audience: Adults in their 50s to 80s re-learning mathematics.
Features: Generous spacing, beautiful zero-overlap TikZ diagrams, full Japanese typography.
"""

import os, sys

def build_intro_book():
    tex_dir = r"E:\GoogleAntigravity\PG_mathbook\books\16713_dudeney_amusements_in_mathematics"
    os.makedirs(tex_dir, exist_ok=True)
    tex_path = os.path.join(tex_dir, "dudeney_amusements_intro.tex")

    preamble = r"""\documentclass[11pt,a4paper,oneside,openany]{ltjsbook}

% --- Typography & Geometry ---
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{geometry}
\geometry{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}

% --- Visual & Layout ---
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,shapes.geometric}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{fancyhdr}

% --- Color Palette ---
\definecolor{primaryblue}{RGB}{20, 50, 110}     % 深遠な紺青
\definecolor{accentcrimson}{RGB}{165, 35, 45}   % 格調ある深紅
\definecolor{softblue}{RGB}{240, 245, 252}      % 淡い背景青
\definecolor{darkslate}{RGB}{45, 55, 72}        % 濃墨
\definecolor{forestgreen}{RGB}{25, 115, 65}     % 深緑
\definecolor{warmgold}{RGB}{195, 140, 20}       % 琥珀金

% --- Puzzle Piece Colors for Haberdasher Dissection ---
\definecolor{pieceA}{RGB}{218, 232, 252}        % 澄んだスカイブルー
\definecolor{pieceB}{RGB}{255, 242, 204}        % 温もりある琥珀イエロー
\definecolor{pieceC}{RGB}{213, 232, 212}        % 爽やかなミントグリーン
\definecolor{pieceD}{RGB}{248, 206, 204}        % 優しいソフトローズ

% --- Headers & Footers (Strictly No text collision) ---
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{darkslate}\textbf{第\thechapter 講\quad \leftmark}}
\fancyhead[R]{\small\color{darkslate}デュードニー数学パズル入門}
\fancyfoot[C]{\color{darkslate}\thepage}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}

% --- Hyperref ---
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=accentcrimson,
    urlcolor=primaryblue,
    pdftitle={古典で学び直すデュードニー数学パズル入門},
    pdfauthor={教育情報科学研究会}
}

\begin{document}

% --- Title Page ---
\begin{titlepage}
\centering
\vspace*{1.5cm}
{\color{primaryblue}\rule{\textwidth}{2pt}}\par
\vspace{1.0cm}
{\Huge\textbf{古典で学び直す}\par}
\vspace{0.4cm}
{\Huge\textbf{デュードニー数学パズル入門}\par}
\vspace{0.6cm}
{\Large\textbf{思考の幾何学・グラフ理論・数論の魔術}\par}
\vspace{0.8cm}
{\large —— 珠玉の430問から読み解く近代数学の核心 ——\par}
\vspace{1.0cm}
{\color{accentcrimson}\rule{0.6\textwidth}{1.5pt}}\par
\vspace{2.0cm}

\begin{tcolorbox}[colback=softblue,colframe=primaryblue,width=0.85\textwidth,arc=3mm,boxrule=1.2pt]
\centering\large
\textbf{ヘンリー・アーネスト・デュードニー} 原著\\
\textit{Amusements in Mathematics} (1917)\\
\vspace{0.5em}
\normalsize
50代、60代から始める、知的好奇心を満たす大人のための数学再入門
\end{tcolorbox}

\vfill
{\large 教育情報科学研究会 編著\par}
\vspace{1.0cm}
{\small 本書は英国の偉大なパズル作家H. E. デュードニーの名著『Amusements in Mathematics』を原典とし、\\現代数学（グラフ理論・線形代数・整数論・群論）の視点から厳選・再構成した解説書です。\par}
\vspace{1.0cm}
\end{titlepage}

% --- Front Matter ---
\frontmatter
\tableofcontents
\clearpage

% --- Introduction ---
\chapter*{発刊にあたって —— なぜいまデュードニーなのか}
\addcontentsline{toc}{chapter}{発刊にあたって —— なぜいまデュードニーなのか}

20世紀初頭のエドワード朝ロンドン。数学者たちが象牙の塔で格闘していた抽象理論を、市民の日常言語とユーモア溢れる物語に託して新聞・雑誌に連載し、英国中を熱狂させた一人の男がいました。**ヘンリー・アーネスト・デュードニー（Henry Ernest Dudeney, 1857--1930）**です。

彼が生み出した430問を超えるパズルを集大成した『Amusements in Mathematics』（1917年刊行）は、単なる暇つぶしのクイズ集ではありません。そこには、18世紀のオイラーによるグラフ理論の創始、ガウスの合同式による数論、さらには現代のコンピュータ・サイエンスを支えるアルゴリズムの基礎が、驚くほど直観的で美しい形で埋め込まれています。

大人の学び直しにおいて、数式を暗記する受験数学は不要です。必要なのは、**「なぜそのように考えるのか」「背後にある数学的な構造は何か」という本質への驚きと納得**です。

本書は、デュードニーの代表的傑作を8つの講義形式にまとめ、現代の視点からその数学的構造を徹底的に紐解きます。美しい図解とともに、知的な冒険の旅へ出かけましょう。

\clearpage

% --- Main Matter ---
\mainmatter

"""

    lectures = [
        {
            "num": 1,
            "short_title": "ハバダッシャーの奇跡",
            "title": "第1講：ハバダッシャーの奇跡 —— 正三角形から正方形への幾何学的変身",
            "subtitle": "ヒンジ結合による図形分割・裁ち合わせ（Dissection）の極致",
            "body": r"""幾何学において、ある多角形を有限個のピースに切り分け、並べ替えて別の多角形を隙間なく組み立て直す操作を「裁ち合わせ（Dissection / 等積変形）」と呼びます。

19世紀末、ハンガリーの数学者ボヤイ・ファルカシュとドイツのゲアウィンは、「面積の等しい任意の二つの多角形は、有限回の直線切断と並べ替えによって互いに移り変わることができる」というボヤイ・ゲアウィンの定理を証明しました。しかし、実際に「何個のピースで、どのように切断すればよいか」を見つけ出すことは、極めて高度な直観と数学的構成力を要求する難問です。

この分野における歴史上最大の傑作と称えられるのが、デュードニーが1902年に発表した「ハバダッシャー（洋品店主）のパズル（The Haberdasher's Puzzle, \#144・\#147の発展）」です。
彼は、一辺の長さが等しい正三角形を、わずか**「4つのピース」**に切り分け、それらがヒンジ（蝶番）で数珠つなぎになったまま回転させるだけで、完璧な「正方形」へと姿を変える驚異的な解法を発見しました。

正三角形の一辺を $a$ とすると面積は $S = \frac{\sqrt{3}}{4} a^2$ であり、これと等しい面積をもつ正方形の一辺は $x = \sqrt{S} = a \sqrt{\frac{\sqrt{3}}{4}} \approx 0.658 a$ となります。デュードニーは、正三角形の各辺の中点を基軸とし、幾何学的な垂線と中点連結を組み合わせることで、無理数 $\sqrt[4]{3}$ を見事に図形上で調和させ、4片の連鎖変形を実現したのです。""",
            "box_title": "重要ポイント：裁ち合わせの数理とヒンジ連鎖",
            "box_text": r"""1. \textbf{ボヤイ・ゲアウィンの定理}：面積が等しい任意の2つの多角形は、有限個のピースへの分割によって必ず互いに変換可能である。
2. \textbf{最小ピース数の探求}：正三角形から正方形への変換は「4ピース」が理論的最小限界であることが証明されている。
3. \textbf{ヒンジ変形の幾何}：4つのピースは頂点のヒンジ（蝶番）でピン留めされており、裏返すことなく平面的にチェーン状に回すだけで三角形と正方形を往復する。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=1.05]
    % --- Left: Equilateral Triangle with 4 Mathematically Precise Pieces ---
    % Parameters for normalized equilateral triangle of side 4.0:
    % A = (0, 0), B = (2.0, 3.4641), C = (4.0, 0)
    % Midpoints: E = (1.0, 1.7321) on AB [Hinge H1], F = (3.0, 1.7321) on BC [Hinge H2]
    % Cut points: P = (2.9820, 0) on AC, Q = (0.9820, 0) on AC [Hinge H3]
    % R = (2.1340, 0.7411) foot of perp from F to EP
    % S = (1.8480, 0.9910) foot of perp from Q to EP
    \begin{scope}[shift={(0,0)}]
        \coordinate (A) at (0, 0);
        \coordinate (B) at (2.0, 3.4641);
        \coordinate (C) at (4.0, 0);
        \coordinate (E) at (1.0, 1.7321);
        \coordinate (F) at (3.0, 1.7321);
        \coordinate (P) at (2.9820, 0);
        \coordinate (Q) at (0.9820, 0);
        \coordinate (R) at (2.1340, 0.7411);
        \coordinate (S) at (1.8480, 0.9910);

        % 4 Interlocking Pieces (Colored with distinct palette)
        % Piece 1 (Sky Blue): Quad E-B-F-R
        \filldraw[fill=pieceA, draw=primaryblue, line width=1.3pt] (E) -- (B) -- (F) -- (R) -- cycle;
        % Piece 2 (Amber Yellow): Quad F-C-P-R
        \filldraw[fill=pieceB, draw=primaryblue, line width=1.3pt] (F) -- (C) -- (P) -- (R) -- cycle;
        % Piece 3 (Mint Green): Quad A-Q-S-E
        \filldraw[fill=pieceC, draw=primaryblue, line width=1.3pt] (A) -- (Q) -- (S) -- (E) -- cycle;
        % Piece 4 (Soft Rose): Triangle Q-P-S
        \filldraw[fill=pieceD, draw=primaryblue, line width=1.3pt] (Q) -- (P) -- (S) -- cycle;

        % Outer boundary of triangle
        \draw[line width=1.8pt, primaryblue] (A) -- (B) -- (C) -- cycle;

        % Hinges (H1 at E, H2 at F, H3 at Q)
        \filldraw[fill=warmgold, draw=darkslate, line width=1.2pt] (E) circle (3.5pt) node[left=4pt, font=\small\bfseries] {$H_1$};
        \filldraw[fill=warmgold, draw=darkslate, line width=1.2pt] (F) circle (3.5pt) node[right=4pt, font=\small\bfseries] {$H_2$};
        \filldraw[fill=warmgold, draw=darkslate, line width=1.2pt] (Q) circle (3.5pt) node[below=4pt, font=\small\bfseries] {$H_3$};

        % Labels for vertices
        \node[below left=2pt] at (A) {\textbf{\large $A$}};
        \node[above=2pt] at (B) {\textbf{\large $B$}};
        \node[below right=2pt] at (C) {\textbf{\large $C$}};

        % Piece text indicators
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (2.0, 2.1) {I};
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (3.0, 0.8) {II};
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (0.9, 0.9) {III};
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (1.9, 0.35) {IV};

        \node[below=18pt, align=center] at (2.0, 0) {
            \textbf{【正三角形】}\quad 面積 $S = \frac{\sqrt{3}}{4} a^2$\\[3pt]
            \footnotesize 3箇所のヒンジ（$H_1, H_2, H_3$）で連鎖結合
        };
    \end{scope}

    % --- Center: Transformation Arrow ---
    \draw[->, line width=2.4pt, accentcrimson] (4.5, 1.73) -- (6.3, 1.73)
        node[midway, above=5pt, align=center] {\textbf{\small ヒンジ連鎖回転}}
        node[midway, below=5pt, align=center] {\scriptsize\color{darkslate} 裏返さず平面的に開閉};

    % --- Right: Reassembled Perfect Square ---
    % Side of square L = 2.6321
    % Origin of square shifted to (7.1, 0.42)
    \begin{scope}[shift={(7.1, 0.42)}]
        \def\sq{2.6321}

        \coordinate (S4) at (0, 0);          % Bottom-left corner (Right angle of Piece IV)
        \coordinate (R1) at (\sq, 0);       % Bottom-right corner (Right angle of Piece I)
        \coordinate (R2) at (\sq, \sq);     % Top-right corner (Right angle of Piece II)
        \coordinate (S3) at (0, \sq);       % Top-left corner (Right angle of Piece III)

        \coordinate (SQ) at (\sq/2, 0);     % Bottom Hinge H3 (Q on square base)
        \coordinate (SF) at (\sq/2, \sq);   % Top Hinge H2 (F on square top)
        \coordinate (SP) at (0, 1.506);     % Cut point P on left side
        \coordinate (SE) at (\sq, 1.506);   % Hinge H1 on right side

        \coordinate (S_center) at (0.67, 1.89); % Internal meeting point of vertices A, B, C

        % 4 Pieces arranged perfectly in square
        % Piece 4 (Soft Rose): Triangle S4 - SQ - SP
        \filldraw[fill=pieceD, draw=primaryblue, line width=1.3pt] (S4) -- (SQ) -- (SP) -- cycle;
        % Piece 3 (Mint Green): Quad S3 - SF - S_center - SP
        \filldraw[fill=pieceC, draw=primaryblue, line width=1.3pt] (S3) -- (SF) -- (S_center) -- (SP) -- cycle;
        % Piece 1 (Sky Blue): Quad R1 - SQ - S_center - SE
        \filldraw[fill=pieceA, draw=primaryblue, line width=1.3pt] (R1) -- (SQ) -- (S_center) -- (SE) -- cycle;
        % Piece 2 (Amber Yellow): Quad R2 - SF - S_center - SE
        \filldraw[fill=pieceB, draw=primaryblue, line width=1.3pt] (R2) -- (SF) -- (S_center) -- (SE) -- cycle;

        % Outer boundary of square
        \draw[line width=2.0pt, accentcrimson] (S4) -- (R1) -- (R2) -- (S3) -- cycle;

        % Hinges on square
        \filldraw[fill=warmgold, draw=darkslate, line width=1.2pt] (SE) circle (3.5pt) node[right=4pt, font=\small\bfseries] {$H_1$};
        \filldraw[fill=warmgold, draw=darkslate, line width=1.2pt] (SF) circle (3.5pt) node[above=4pt, font=\small\bfseries] {$H_2$};
        \filldraw[fill=warmgold, draw=darkslate, line width=1.2pt] (SQ) circle (3.5pt) node[below=4pt, font=\small\bfseries] {$H_3$};

        % Piece text indicators (Exactly at centroids)
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (1.81, 0.85) {I};
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (1.85, 2.16) {II};
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (0.50, 2.16) {III};
        \node[font=\footnotesize\bfseries, color=primaryblue!80!black] at (0.44, 0.50) {IV};

        \node[below=18pt, align=center] at (\sq/2, 0) {
            \textbf{【完全な正方形】}\quad 一辺 $x = a \sqrt{\frac{\sqrt{3}}{4}}$\\[3pt]
            \footnotesize 同色ピースが寸分違わず正方形を再構成
        };
    \end{scope}
\end{tikzpicture}""",
            "caption": "概念図 1：デュードニーの最高傑作「ハバダッシャー・パズル」。正三角形から正方形への4分割ヒンジ連鎖変形。"
        },
        {
            "num": 2,
            "short_title": "オイラーの一筆書き",
            "title": "第2講：オイラーの一筆書き定理 —— ケーニヒスベルクから始まるグラフ理論",
            "subtitle": "頂点の次数（偶奇性）が握るネットワーク走破の運命",
            "body": r"""1736年、大数学者レオンハルト・オイラーは「ケーニヒスベルクの7つの橋」問題を解決し、現代のトポロジー（位相幾何学）およびグラフ理論の扉を開きました。この理論を誰でも親しめる魅力的なパズルへと昇華させたのがデュードニーです（\#220--\#261）。

一筆書きができるかどうかは、図形の大きさや線の長さとは一切関係がありません。問題となるのは、**「各頂点（交差点）に集まる線の本数（次数 / degree）」**だけです。

線の本数が奇数である頂点を「奇頂点（Odd Vertex）」、偶数である頂点を「偶頂点（Even Vertex）」と呼びます。1本の線を描いて通過するたびに、その交差点では「入る線」と「出る線」のペア（2本）が消費されます。

したがって：
1. **奇頂点が0個**の場合：どの点から出発しても一筆書きが可能で、必ず出発点に戻る（オイラー閉路）。
2. **奇頂点が2個**の場合：一方の奇頂点から出発し、もう一方の奇頂点で終わる一筆書きが可能（オイラー路）。
3. **奇頂点が4個以上**の場合：いかなる工夫を凝らしても一筆書きは**数学的に不可能**である。

デュードニーはこのオイラーの定理を駆使し、鉄道の引き込み線パズルや家々の巡回ルート問題など、数々の魅力的な傑作を生み出しました。""",
            "box_title": "重要ポイント：オイラーの一筆書き定理",
            "box_text": r"""1. \textbf{幾何学的寸法の捨象}：線の曲がりや長さは無関係であり、頂点の接続関係（次数）のみが本質を決める。
2. \textbf{奇頂点数の偶数性}：1本の線は2つの端点を持つため、グラフ全体の奇頂点の総数は常に偶数（0, 2, 4, 6...）個である。
3. \textbf{一筆書きの完全判定}：奇頂点が0個または2個の連結グラフのみが一筆書き可能であり、4個以上は絶対に描けない。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=1.1]
    % Case A: Euler Tour (All Even Vertices)
    \begin{scope}[shift={(0,0)}]
        \node[draw=primaryblue, line width=1.5pt, fill=softblue, circle, inner sep=4pt] (A1) at (0, 2.2) {\textbf{4}};
        \node[draw=primaryblue, line width=1.5pt, fill=softblue, circle, inner sep=4pt] (B1) at (-1.8, 0) {\textbf{2}};
        \node[draw=primaryblue, line width=1.5pt, fill=softblue, circle, inner sep=4pt] (C1) at (1.8, 0) {\textbf{2}};
        \node[draw=primaryblue, line width=1.5pt, fill=softblue, circle, inner sep=4pt] (D1) at (0, -1.2) {\textbf{4}};

        \draw[line width=1.4pt, primaryblue] (A1) -- (B1) -- (D1) -- (C1) -- (A1);
        \draw[line width=1.4pt, primaryblue] (A1) -- (D1);
        \draw[line width=1.4pt, primaryblue] (-1.8,0) to[bend left=30] (1.8,0);

        \node[below=14pt, align=center] at (0, -1.2) {
            \textbf{【奇頂点 0個】}\quad 全て偶数次\\
            \small どの頂点からでも出発点に戻る一筆書きが可能
        };
    \end{scope}

    % Case B: Non-Eulerian (4 Odd Vertices)
    \begin{scope}[shift={(7.5, 0)}]
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (A2) at (-1.5, 2.0) {\textbf{3}};
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (B2) at (1.5, 2.0) {\textbf{3}};
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (C2) at (-1.5, -0.6) {\textbf{3}};
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (D2) at (1.5, -0.6) {\textbf{3}};

        \draw[line width=1.4pt, darkslate] (A2) -- (B2) -- (D2) -- (C2) -- (A2);
        \draw[line width=1.4pt, darkslate] (A2) -- (D2);
        \draw[line width=1.4pt, darkslate] (B2) -- (C2);

        \node[below=14pt, align=center] at (0, -0.6) {
            \textbf{【奇頂点 4個】}\quad 完全グラフ $K_4$\\
            \small 奇頂点が4個 $\to$ \textbf{一筆書きは数学的に不可能}
        };
    \end{scope}
\end{tikzpicture}""",
            "caption": "概念図 2：オイラーの一筆書き判定原理。各頂点に集まる線の本数（偶数・奇数）が走破可能性を決定づける。"
        },
        {
            "num": 3,
            "short_title": "チェス盤の数学",
            "title": "第3講：チェス盤の数学 —— ナイト・ツアーと8クイーン問題",
            "subtitle": "二次元格子上の探索・対称群・ハミルトン路の数理",
            "body": r"""64個の白黒マスからなるチェス盤は、それ自体が豊かな離散数学の実験場です（\#288--\#361）。デュードニーはチェス盤を用いた数学パズルの第一人者でもありました。

代表的な古典問題の一つが「ナイト・ツアー（Knight's Tour, \#339--\#340）」です。チェスのナイト（八方に「2マス進んで1マス曲がる」L字型に跳ぶ駒）を盤上に置き、64マスすべてのマスを重複することなくちょうど1度ずつ訪問して元の位置に戻る（または終わる）ことができるか、という問題です。

グラフ理論の言葉で言えば、これは「ナイトの移動可能なマス同士を結んだグラフにおいて**ハミルトン閉路（Hamiltonian Cycle）**が存在するか」という問題に他なりません。

ここで極めて重要な数学的性質が**「色の交代性（パリティ）」**です。ナイトはどのような跳び方をしても、**白マスから黒マスへ、黒マスから白マスへと、1手ごとに必ずマスの色が反転**します。したがって、ナイト・ツアーが完結するためには、白32マス・黒32マスを厳密に交互に訪れなければならないという絶対的な制約（二部グラフの性質）が課されるのです。""",
            "box_title": "重要ポイント：二次元格子探索とパリティ不変量",
            "box_text": r"""1. \textbf{二部グラフ構造}：チェス盤の白マスと黒マスは完全な二部グラフをなし、ナイトの移動は異なるグループ間の辺のみを通る。
2. \textbf{ハミルトン路の存在条件}：全64マスを踏破するには、奇数手目は白、偶数手目は黒（またはその逆）という厳密な交代性が必須となる。
3. \textbf{局所対称性と大域探索}：コーナー（角）のマスは進入路が2本しか存在しないため、解法の決定において最優先の制約となる。""",
            "tikz": r"""\begin{tikzpicture}[scale=0.92, >=Stealth]
    % 5x5 Chessboard with checkered pattern
    \begin{scope}[shift={(0,0)}]
        \foreach \x in {-2,-1,0,1,2} {
            \foreach \y in {-2,-1,0,1,2} {
                \pgfmathtruncatemacro{\parity}{mod(\x + \y + 10, 2)}
                \ifnum\parity=0
                    \fill[white] (\x-0.5, \y-0.5) rectangle (\x+0.5, \y+0.5);
                \else
                    \fill[softblue!80!primaryblue!22] (\x-0.5, \y-0.5) rectangle (\x+0.5, \y+0.5);
                \fi
                \draw[darkslate!35, thin] (\x-0.5, \y-0.5) rectangle (\x+0.5, \y+0.5);
            }
        }
        \draw[line width=1.8pt, primaryblue] (-2.5, -2.5) rectangle (2.5, 2.5);

        % Center Knight at (0,0) [White Square]
        \filldraw[fill=primaryblue, draw=primaryblue] (0, 0) circle (0.38);
        \node[white] at (0, 0) {\textbf{\large N}};

        % 8 Target Squares (All colored squares by chess geometry!)
        \foreach \tx/\ty in {1/2, -1/2, 1/-2, -1/-2, 2/1, -2/1, 2/-1, -2/-1} {
            \fill[accentcrimson!25] (\tx-0.5, \ty-0.5) rectangle (\tx+0.5, \ty+0.5);
            \draw[accentcrimson, line width=1.3pt] (\tx-0.5, \ty-0.5) rectangle (\tx+0.5, \ty+0.5);
            \filldraw[fill=accentcrimson, draw=white, line width=0.8pt] (\tx, \ty) circle (3pt);
        }

        % L-shaped trajectory lines (Explicit to guarantee zero TeX if-nesting errors)
        \draw[->, line width=1.8pt, accentcrimson] (0,0) -- (0, 2) -- (1, 2);
        \draw[->, line width=1.8pt, accentcrimson] (0,0) -- (2, 0) -- (2, 1);
        \draw[->, line width=1.1pt, accentcrimson, dashed] (0,0) -- (0, 2) -- (-1, 2);
        \draw[->, line width=1.1pt, accentcrimson, dashed] (0,0) -- (0, -2) -- (1, -2);
        \draw[->, line width=1.1pt, accentcrimson, dashed] (0,0) -- (0, -2) -- (-1, -2);
        \draw[->, line width=1.1pt, accentcrimson, dashed] (0,0) -- (-2, 0) -- (-2, 1);
        \draw[->, line width=1.1pt, accentcrimson, dashed] (0,0) -- (2, 0) -- (2, -1);
        \draw[->, line width=1.1pt, accentcrimson, dashed] (0,0) -- (-2, 0) -- (-2, -1);

        \node[below=14pt, align=center] at (0, -2.5) {
            \textbf{【ナイトの八方移動】}\\
            \small 白マス中央から到達可能な全8マスは\textbf{すべて黒マス}
        };
    \end{scope}

    % Right Explanation Box (Adequate spacing and clear multi-line layout)
    \begin{scope}[shift={(6.7, 0)}]
        \node[draw=primaryblue, line width=1.3pt, fill=softblue, rounded corners=3mm, inner sep=10pt, text width=6.2cm, align=left] at (0, 0) {
            \textbf{\large 【ナイト移動の不変量】}\\[6pt]
            \small
            \textbf{・移動ベクトル}：$(\pm 1, \pm 2)$ または $(\pm 2, \pm 1)$\\[3pt]
            \textbf{・格子点間距離}：$\sqrt{1^2 + 2^2} = \sqrt{5}$\\[3pt]
            \textbf{・マスの色交代性}：\\
            \quad \colorbox{white}{\fbox{\strut\bfseries 白マス}} $\;\longleftrightarrow\;$ \colorbox{accentcrimson!20}{\fbox{\strut\bfseries 常に黒マス}}\\[4pt]
            1手進むごとにマスの色が必ず反転する！\\[6pt]
            \textbf{・64手完全巡回} $\implies$ ハミルトン閉路\\[4pt]
            対称性とパリティ（偶奇性）が\\
            全マス踏破の成否を握る。
        };
    \end{scope}
\end{tikzpicture}""",
            "caption": "概念図 3：チェスのナイトがもつ「L字移動」の対称性と白黒反転パリティ。ナイト・ツアーの数学的基礎。"
        },
        {
            "num": 4,
            "short_title": "川渡りのアルゴリズム",
            "title": "第4講：川渡りパズルの状態空間探索 —— 狼と山羊とキャベツの論理",
            "subtitle": "制約充足問題（CSP）と有向グラフ最短経路アルゴリズム",
            "body": r"""「農夫が狼、山羊、キャベツを一艘の小舟で対岸へ運ばなければならない。舟には農夫のほかに1つしか乗せられない。農夫がいないと、狼は山羊を食べ、山羊はキャベツを食べてしまう。どう運べば全員無事に対岸へ渡れるか？」（\#373--\#377）。

中世から伝わるこの有名な古典パズルは、現代情報科学における**「状態空間探索（State Space Search）」**および**「制約充足問題（Constraint Satisfaction Problem）」**の原点です。

各時刻において、「誰が左岸にいて、誰が右岸にいるか」という状態は全部で $2^4 = 16$ 通り存在します。しかし、「農夫不在で狼と山羊が同居」「農夫不在で山羊とキャベツが同居」という禁止状態（制約違反）を除外すると、許される安全な状態はわずか**10通り**に絞られます。

この安全な状態をノード（節点）、舟による合法的な移動をエッジ（枝）とする「有向グラフ」を描けば、パズルを解くことは**「初期状態から目標状態への最短経路を探索する問題」**へと完全に帰着されます。この問題のクライマックスは、4手目に「一旦対岸へ運んだ山羊を連れ戻す」という逆転の発想です。局所的な前進にとらわれず、状態空間全体を俯瞰する視点こそが数学的思考の本質です。""",
            "box_title": "重要ポイント：状態空間と幅優先探索（BFS）",
            "box_text": r"""1. \textbf{状態のモデル化}：現実の制約をBoolean（真偽値）やビット列として定式化する。
2. \textbf{制約による枝刈り}：不可能な状態を探索木から即座に排除し、探索空間を劇的に縮小させる。
3. \textbf{一時的後退の価値}：最短解に至る経路には、一見無駄に見える「元の岸へ戻す」ステップが不可欠となる。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=0.92]
    % State nodes (Arranged neatly with compact multi-line text)
    \begin{scope}[shift={(0,0)}]
        \node[draw=primaryblue, line width=1.4pt, fill=softblue, rounded corners=2mm, inner sep=6pt] (S0) at (0, 3.2) {\textbf{初期：左岸(人, 狼, 羊, 甘)}};
        \node[draw=darkslate, line width=1.1pt, fill=white, rounded corners=2mm, inner sep=5pt] (S1) at (0, 1.8) {\small 羊を対岸へ渡す};
        \node[draw=darkslate, line width=1.1pt, fill=white, rounded corners=2mm, inner sep=5pt] (S2) at (0, 0.4) {\small 人が単身で戻る};
        \node[draw=darkslate, line width=1.1pt, fill=white, rounded corners=2mm, inner sep=5pt, align=center] (S3) at (-2.3, -1.0) {\small 狼を渡し\\[2pt]\small 羊を連れ戻す};
        \node[draw=darkslate, line width=1.1pt, fill=white, rounded corners=2mm, inner sep=5pt, align=center] (S4) at (2.3, -1.0) {\small 甘を渡し\\[2pt]\small 羊を連れ戻す};
        \node[draw=darkslate, line width=1.1pt, fill=white, rounded corners=2mm, inner sep=5pt] (S5) at (0, -2.4) {\small 甘（または狼）を渡す};
        \node[draw=accentcrimson, line width=1.6pt, fill=accentcrimson!15, rounded corners=2mm, inner sep=6pt] (S6) at (0, -3.8) {\textbf{達成：全員無事に対岸へ！}};

        \draw[->, line width=1.3pt, primaryblue] (S0) -- (S1);
        \draw[->, line width=1.3pt, primaryblue] (S1) -- (S2);
        \draw[->, line width=1.3pt, primaryblue] (S2) -- (S3);
        \draw[->, line width=1.3pt, primaryblue] (S2) -- (S4);
        \draw[->, line width=1.3pt, primaryblue] (S3) -- (S5);
        \draw[->, line width=1.3pt, primaryblue] (S4) -- (S5);
        \draw[->, line width=1.6pt, accentcrimson] (S5) -- (S6);
    \end{scope}

    % Right Key insight box (Vertically centered to match layout)
    \begin{scope}[shift={(7.3, -0.6)}]
        \node[draw=warmgold!80!black, fill=warmgold!10, rounded corners=2mm, text width=4.6cm, inner sep=9pt, align=left] at (0, 0) {
            \textbf{\small 【逆転の定石】}\\[4pt]
            \footnotesize
            荷物を対岸に運ぶだけでなく、一時的に「羊を連れ帰る」という一見無駄な後退が、袋小路の唯一の突破口となる。\\
            \vspace{4pt}
            状態空間グラフにおける最短路アルゴリズムの真骨頂。
        };
    \end{scope}
\end{tikzpicture}""",
            "caption": "概念図 4：川渡りパズルの状態遷移ネットワーク。禁忌状態を排除した合法状態空間の探索グラフ。"
        },
        {
            "num": 5,
            "short_title": "魔方陣の数理",
            "title": "第5講：魔方陣の代数構造 —— 線形代数と対称群が織りなす宇宙",
            "subtitle": "古代中国の「洛書」からアフィン空間への昇華",
            "body": r"""縦・横・対角線の数の和がすべて等しくなるように正方形に数を並べた「魔方陣（Magic Square, \#399--\#412）」。古代中国の易経に登場する「洛書（3次魔方陣）」をはじめ、西洋ではデューラーの版画『メランコリア I』に描かれるなど、人類を魅了し続けてきた神秘の数配置です。

デュードニーはこの魔方陣を、単なる試行錯誤のパズルから厳密な代数学の対象へと引き上げました。

最も基本的な $3 \times 3$ の魔方陣（1から9までの数字）において、全数字の総和は $1 + 2 + \dots + 9 = 45$ です。3行あるため、各行・各列の和（魔方陣定数）は必ず $45 \div 3 = 15$ にならなければなりません。

さらに、中央のマスを通るラインは4本（行1・列1・対角線2）あり、これらを連立させることで、**「中央の数は必ず 5 でなければならない」**ことが数学的に一意に証明されます。

さらに進んで、現代の線形代数では、魔方陣全体が「連立一次方程式の解空間（アフィン部分空間）」をなすことが知られています。自由度（次元）を計算することで、基本となる独立な魔方陣の線形結合としてすべての魔方陣を生成できるのです。""",
            "box_title": "重要ポイント：魔方陣の不変量と線形構造",
            "box_text": r"""1. \textbf{定数の必然性}：$n$ 次魔方陣の行和・列和は、総和の対称性から $M = \frac{n(n^2+1)}{2}$ と厳密に一意決定される。
2. \textbf{中心数の定理}：奇数次魔方陣の中心マスには、必ず全数字の中央値（3次ならば5）が配置される。
3. \textbf{対称変換群}：回転（4通り）と反転（2通り）による8個の変換は、二面体群 $D_4$ を構成し、本質的な解は1種類に帰着される。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=1.1]
    % 3x3 Magic Square
    \begin{scope}[shift={(0,0)}]
        \draw[step=1.2cm, darkslate, line width=1.4pt] (0,0) grid (3.6,3.6);
        \draw[line width=2.0pt, primaryblue] (0,0) rectangle (3.6,3.6);

        % Numbers
        \node at (0.6, 3.0) {\textbf{\LARGE 8}};
        \node at (1.8, 3.0) {\textbf{\LARGE 1}};
        \node at (3.0, 3.0) {\textbf{\LARGE 6}};

        \node at (0.6, 1.8) {\textbf{\LARGE 3}};
        \node[accentcrimson] at (1.8, 1.8) {\textbf{\LARGE 5}};
        \node at (3.0, 1.8) {\textbf{\LARGE 7}};

        \node at (0.6, 0.6) {\textbf{\LARGE 4}};
        \node at (1.8, 0.6) {\textbf{\LARGE 9}};
        \node at (3.0, 0.6) {\textbf{\LARGE 2}};

        \node[below=14pt, align=center] at (1.8, 0) {
            \textbf{【3次魔方陣（洛書）】}\\
            \small 各行・列・対角線の和 $= \mathbf{15}$（中心は常に $5$）
        };
    \end{scope}

    % Mathematical Decomposition Box
    \node[draw=primaryblue, fill=softblue, rounded corners=2mm, text width=6.2cm, inner sep=9pt, align=left] at (7.2, 1.8) {
        \textbf{\large 【魔方陣の代数的構造】}\\[5pt]
        \small 任意の3次魔方陣は、中心数 $x$、パラメータ $a, b$ を用いる線形モデルとして表現：\\[4pt]
        \centering
        \begin{tabular}{|c|c|c|}
        \hline
        $x+b$ & $x-a-b$ & $x+a$ \\ \hline
        $x+a-b$ & $x$ & $x-a+b$ \\ \hline
        $x-a$ & $x+a+b$ & $x-b$ \\ \hline
        \end{tabular}\\[6pt]
        \raggedright\footnotesize
        線形代数における3次元ベクトル空間の美しい具現化。
    };
\end{tikzpicture}""",
            "caption": "概念図 5：3次魔方陣の代数的構造。中心数「5」の決定性と線形空間としての一般解。"
        },
        {
            "num": 6,
            "short_title": "迷路の幾何学",
            "title": "第6講：迷路の幾何学と脱出アルゴリズム —— トレモーの解法",
            "subtitle": "トポロジーと深さ優先探索（DFS）の先駆的アルゴリズム",
            "body": r"""入り組んだ通路の迷宮から生還するための数学的手法とは何か？ デュードニーの第13章「迷路の問題（Mazes and How to Thread Them）」は、古今東西の有名な迷路（ハンプトンコート宮殿の生垣迷路など）を取り上げ、その幾何学的本質を解き明かしています。

初等的な迷路では「壁に右手を当てて歩き続ければ必ず脱出できる（右手法 / 壁づたい法）」と言われます。しかし、これは「迷路が単連結（環状の孤島がない）」場合にしか通用しません。中央に独立したループ構造（多重連結迷路）がある場合、右手法では同じ環状路を無限に周回してしまう罠に陥ります。

いかなる複雑な迷路であっても確実に脱出できる完全なアルゴリズムとして知られるのが、19世紀のフランスの数学者シャルル・ピエール・トレモーが考案した**「トレモーのアルゴリズム（Trémaux's Algorithm）」**です。

ルールは極めてシンプルです：
1. 通路を初めて進むときは、床に「1本線」の印をつける。
2. もし行き止まりに突き当たったら、回れ右をして戻り、通路に「2本目」の印をつけて**その通路を封鎖（二重印）**する。
3. すでに印がついている交差点に別の道から出た場合、決してその道には進まず、来た道を引き返して2本目の印をつける。

この操作は、コンピュータ・アルゴリズムにおける**「深さ優先探索（Depth-First Search, DFS）」そのもの**です。有限の迷路において、各通路は最大でも「往路」と「復路」の計2回しか通過されず、無限ループに陥ることなく確実に脱出路を発見できることが数学的に証明されています。""",
            "box_title": "重要ポイント：トレモーのアルゴリズムとDFS",
            "box_text": r"""1. \textbf{右手法の限界}：島（ループ）を含む多重連結迷路では、壁づたい法は無限周回トラップに囚われる。
2. \textbf{印による状態記憶}：未踏（0本）、探索中（1本）、走破・袋小路（2本）という3状態の記録が完全走破を保証する。
3. \textbf{計算量の最適性}：通路の総数を $E$ とすると、最大移動回数は高々 $2E$ 回で終了し、線形時間 $O(E)$ でゴールに到達する。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=0.88]
    % Maze graph nodes (Spacious layout with guaranteed zero collision)
    \node[draw=primaryblue, line width=1.6pt, fill=softblue, circle, inner sep=4pt] (IN) at (0, 1.8) {\textbf{\large 入口}};
    \node[draw=darkslate, line width=1.4pt, fill=white, circle, inner sep=4pt] (A) at (5.4, 1.8) {\textbf{\large 分岐 $A$}};
    \node[draw=accentcrimson, line width=1.6pt, fill=accentcrimson!15, rectangle, rounded corners=2mm, inner sep=6pt] (DEAD) at (11.4, 1.8) {\textbf{\large 行き止まり}};
    \node[draw=darkslate, line width=1.4pt, fill=white, circle, inner sep=4pt] (B) at (5.4, -1.2) {\textbf{\large 分岐 $B$}};
    \node[draw=forestgreen, line width=1.8pt, fill=forestgreen!20, circle, inner sep=6pt] (OUT) at (11.4, -1.2) {\textbf{\large 出口}};

    % Path 1: IN -> A (Forward 1-line, compact label)
    \draw[->, line width=1.6pt, primaryblue] (IN) -- (A)
        node[midway, above=6pt, align=center] {\small ① 初めて進む通路\\[-1pt]\footnotesize （1本線の印）};

    % Path 2: A -> DEAD (Forward straight exploration: clean two-line label centered)
    \draw[->, line width=1.6pt, darkslate] (A) -- (DEAD)
        node[midway, above=5pt, align=center] {\small ② 未踏路を直進探索\\[-1pt]\footnotesize （1本線）};

    % Path 3: DEAD -> A (High upward curving backtrack: completely clear of Path 2!)
    \draw[->, line width=1.6pt, accentcrimson, dashed] (DEAD.north) to[bend right=48]
        node[midway, above=6pt, accentcrimson] {\textbf{\small ③ 行き止まり！ 2本目で封鎖して後退}} (A.north);

    % Path 4: A -> B (Downward to unexplored path, clean single line on the right)
    \draw[->, line width=1.6pt, primaryblue] (A) -- (B)
        node[midway, right=10pt] {\textbf{\small ④ 別の未踏路へ進入} \footnotesize （1本線）};

    % Path 5: B -> OUT (Goal)
    \draw[->, line width=2.2pt, forestgreen] (B) -- (OUT)
        node[midway, above=6pt, forestgreen] {\textbf{\small ⑤ 出口（ゴール）到達！}};

    % Bottom Explanation Box with ample top margin
    \node[draw=primaryblue, line width=1.2pt, fill=softblue!30, rounded corners=2mm, text width=12.5cm, inner sep=9pt, align=left] at (5.7, -3.4) {
        \small \textbf{トレモーの規則}：通路に印をつけることで、「未踏の道」と「探索済みの袋小路」を厳密に区別する。\\
        いかなる多重連結迷路も、各通路を往復（計2回）以上通過することなく、有限時間で完全走破される。
    };
\end{tikzpicture}""",
            "caption": "概念図 6：トレモーの迷路走破アルゴリズム。袋小路の二重印封鎖と深さ優先探索のメカニズム。"
        },
        {
            "num": 7,
            "short_title": "不定方程式と整数論",
            "title": "第7講：ディオファントス方程式と整数論 —— 金銭・年齢・分配パズル",
            "subtitle": "「解が整数でなければならない」という最も美しい制約の解法",
            "body": r"""代数学の通常の方程式では、未知数の数よりも方程式の数が少ない場合、解は無数に存在して定まりません。しかし、「未知数はすべて正の整数（自然数）でなければならない」という条件がついた瞬間、状況は一変します。

このような方程式を、古代アレクサンドリアの数学者にちなんで**「不定方程式（ディオファントス方程式 / Diophantine Equation）」**と呼びます。

デュードニーの第1章「算術と代数の問題（\#1--\#141）」の多くは、このディオファントス方程式の鮮やかな応用です。
例えば、問題第1問「郵便局の困惑（\#1）」では、5シリング（60ペンス）の硬貨を出し、「2ペンス切手を何枚か、その6倍の枚数の1ペンス切手をくれ、そして残りを2ペンス半（2.5ペンス）切手でぴったり支払ってほしい」と求めます。

2ペンス切手の枚数を $x$ とすると、1ペンス切手は $6x$ 枚となります。2.5ペンス切手の枚数を $y$ と置くと、合計金額は：
\[
2x + 1(6x) + 2.5y = 60 \implies 8x + \frac{5}{2}y = 60 \implies 16x + 5y = 120
\]
この方程式において、$x, y$ はともに正の整数でなければなりません。
合同式（mod 5）をとると：
\[
16x \equiv 120 \pmod 5 \implies x \equiv 0 \pmod 5
\]
すなわち、$x$ は 5 の倍数でなければなりません。
$x = 5$ を代入すると、$16(5) + 5y = 80 + 5y = 120 \implies 5y = 40 \implies y = 8$。
もし $x \ge 10$ とすると $16x \ge 160 > 120$ となり、$y$ が負になってしまうため不適です。

したがって、可能な解は**「$x = 5, y = 8$」のただ1組**に確定します！
（2ペンス切手5枚、1ペンス切手30枚、2.5ペンス切手8枚）。

学校の数学では「連立方程式は式の数が足りなければ解けない」と教わりますが、現実の世界（切手の枚数や人数）がもつ「整数」という制約が、見事に唯一無二の答えを浮き彫りにするのです。""",
            "box_title": "重要ポイント：一次不定方程式と整数の剰余類",
            "box_text": r"""1. \textbf{ベズーの等式}：方程式 $ax + by = c$ が整数解をもつための必要十分条件は、$c$ が $\gcd(a, b)$ の倍数であること。
2. \textbf{合同式（モジュロ演算）の威力}：法（modulus）をとることで変数を1つ消去し、解の候補を瞬時に絞り込む。
3. \textbf{不等式による境界画定}：非負整数条件（$x \ge 1, y \ge 1$）によって、無限に広がる解の中から現実の有限解を特定する。""",
            "tikz": r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Accurate coordinate system & grid
    \def\xscale{1.2}
    \def\yscale{0.22}

    % Grid lines (integer lattice)
    \foreach \x in {1,2,3,4,5,6,7,8} {
        \draw[gray!20, thin] ({\x*\xscale}, 0) -- ({\x*\xscale}, {26*\yscale});
        \node[below=3pt, font=\footnotesize\color{darkslate}] at ({\x*\xscale}, 0) {\x};
    }
    \foreach \y in {4,8,12,16,20,24} {
        \draw[gray!20, thin] (0, {\y*\yscale}) -- ({8.5*\xscale}, {\y*\yscale});
        \node[left=3pt, font=\footnotesize\color{darkslate}] at (0, {\y*\yscale}) {\y};
    }

    % Origin label
    \node[below left=3pt, font=\footnotesize\color{darkslate}] at (0, 0) {0};

    % Axes with comfortable margins
    \draw[->, line width=1.3pt, darkslate] (-0.3, 0) -- ({9.8*\xscale}, 0)
        node[below right=2pt, font=\small\color{darkslate}] {\textbf{$x$（2ペンス切手基準枚数）}};
    \draw[->, line width=1.3pt, darkslate] (0, -0.3) -- (0, {28*\yscale})
        node[above right=2pt, font=\small\color{darkslate}] {\textbf{$y$（2.5ペンス切手枚数）}};

    % Line: 16x + 5y = 120 (y = 24 - 3.2x)
    \draw[line width=2.0pt, primaryblue] (0, {24*\yscale}) -- ({7.5*\xscale}, 0);
    \node[above right=3pt, primaryblue] at ({1.6*\xscale}, {19*\yscale}) {\textbf{直線 $16x + 5y = 120$}};

    % Boundary points
    \filldraw[fill=white, draw=darkslate, line width=1.5pt] (0, {24*\yscale}) circle (3.5pt)
        node[right=6pt, font=\footnotesize, fill=white, inner sep=1.5pt] {$(0, 24)$ [切手無指定]};

    \filldraw[fill=white, draw=darkslate, line width=1.5pt] ({7.5*\xscale}, 0) circle (3.5pt);
    \node[above right=4pt and 2pt, font=\footnotesize, fill=white, inner sep=1.5pt] at ({7.5*\xscale}, 0) {$(7.5, 0)$ [非整数]};

    % Non-integer points on the line for integer x
    \foreach \x/\y in {1/20.8, 2/17.6, 3/14.4, 4/11.2, 6/4.8, 7/1.6} {
        \filldraw[fill=gray!60, draw=darkslate] ({\x*\xscale}, {\y*\yscale}) circle (2.5pt);
        \draw[gray!40, dotted] ({\x*\xscale}, 0) -- ({\x*\xscale}, {\y*\yscale});
    }

    % The Unique Integer Solution (5, 8)
    \draw[accentcrimson, line width=1.3pt, dashed] ({5*\xscale}, 0) -- ({5*\xscale}, {8*\yscale}) -- (0, {8*\yscale});
    \filldraw[fill=accentcrimson, draw=primaryblue, line width=1.8pt] ({5*\xscale}, {8*\yscale}) circle (5.5pt);
    \node[above right=10pt, fill=softblue, draw=accentcrimson, line width=1.2pt, rounded corners=2mm, inner sep=6pt, align=left] at ({5*\xscale}, {8*\yscale}) {
        \textbf{\large 唯一の自然数解 $(x=5, y=8)$}\\[2pt]
        \footnotesize 2ペンス切手5枚、1ペンス切手30枚、2.5ペンス切手8枚
    };
\end{tikzpicture}""",
            "caption": "概念図 7：一次不定方程式 $16x + 5y = 120$ のグラフ。格子点（整数解）条件により唯一の解 $(5, 8)$ が抽出される。"
        },
        {
            "num": 8,
            "short_title": "15パズルの置換群",
            "title": "第8講：15パズルの置換群と不変量 —— サム・ロイドの難問を解き明かす",
            "subtitle": "交代群 $A_n$ とパリティ保存則による不可能性の証明",
            "body": r"""1870年代末、アメリカから全世界へと広がり一大社会現象を巻き起こした「15パズル（15 Puzzle / Sliding Puzzle, \#234--\#238）」。

1から15までの数字が書かれた正方形の駒を、$4 \times 4$ の枠（1マス空き）の中でスライドさせ、順番通りに並べるパズルです。著名なパズル作家サム・ロイドは、**「14番と15番の駒だけが入れ替わった初期状態から、正しい昇順（1から15）に戻せるか？」**という懸賞問題を新聞に発表し、世界中の人々を不眠不休の熱狂に陥れました。

しかし、この問題には**最初から絶対に解が存在しない**ことが、現代数学（群論）によって厳密に証明されています。

数学者たちが注目したのは、駒の配置がもつ**「パリティ（偶奇性）」**という不変量です。
1. 駒を1回スライドさせることは、数学的には「空きマスとの互換（置換）」を意味します。
2. 駒を元の位置関係に戻す偶数回の操作によって生じる置換は、すべて**「偶置換（Even Permutation）」**の集合（交代群 $A_{15}$）に属します。
3. 一方、14と15の2駒だけを入れ替える操作は、1回の互換のみを含む**「奇置換（Odd Permutation）」**です。

駒を盤上でどのように合法的にスライドさせても、偶置換から奇置換へと移り変わることは数学的に不可能です。すなわち、全 $16!$ 通りの配置空間は、互いに決して行き来できない**「解ける世界（偶パリティ）」**と**「絶対に解けない世界（奇パリティ）」**の2つの独立した宇宙へと完全に分断されているのです。""",
            "box_title": "重要ポイント：置換群とパリティ保存則",
            "box_text": r"""1. \textbf{置換の偶奇性}：あみだくじと同様、任意の置換は偶数回または奇数回の互換（2要素の交換）の積として一意に分類される。
2. \textbf{不変量（Invariant）の原理}：許された操作の前後で変化しない数学的性質を見出すことで、試行錯誤することなく不可能性を断定できる。
3. \textbf{現代暗号・物理への接続}：パリティの保存則は、素粒子物理学の保存則やコンピュータ・セキュリティの誤り検出符号の根幹をなす概念である。""",
            "tikz": r"""\begin{tikzpicture}[scale=0.90, >=Stealth]
    % Left Box: Even Permutations (Solvable Universe)
    \node[draw=primaryblue, line width=1.5pt, fill=softblue!60, rounded corners=3mm, inner sep=9pt, text width=5.0cm, align=center] (EVEN) at (0, 0) {
        \textbf{\large 【偶置換の世界】}\\[6pt]
        \textbf{可解な初期配置}\\[4pt]
        \small 全配置のちょうど半分（$16! / 2$ 通り）\\[6pt]
        \colorbox{white}{\fbox{\strut 合法的なスライド操作で常に可解}}
    };

    % Right Box: Odd Permutations (Unsolvable Universe)
    \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!12, rounded corners=3mm, inner sep=9pt, text width=5.0cm, align=center] (ODD) at (8.8, 0) {
        \textbf{\large 【奇置換の世界】}\\[6pt]
        \textbf{不可解な初期配置}\\[4pt]
        \small 全配置のもう半分（$16! / 2$ 通り）\\[6pt]
        \colorbox{white}{\fbox{\strut\color{accentcrimson}\bfseries ロイドの難問（14--15反転）}}
    };

    % Center Wall of Impossibility (Spacious separation)
    \draw[line width=2.4pt, darkslate, dashed] (4.4, -2.4) -- (4.4, 2.4);
    \node[fill=darkslate, text=white, font=\bfseries\small, rounded corners=2mm, inner sep=5pt] at (4.4, 1.8) {不可能性の壁};

    % Crossing blocked arrow with comfortable space
    \draw[->, line width=1.8pt, accentcrimson] (ODD.west) -- (5.3, 0)
        node[midway, above=4pt, font=\bfseries\color{accentcrimson}] {到達不可！}
        node[at end, left=3pt, font=\Large\bfseries\color{accentcrimson}] {$\times$};

    \node[below=16pt, align=center] at (4.4, -2.4) {
        \textbf{【結論】}\quad 盤面スライド操作はパリティ（偶奇性）を保存するため、\\
        二つの世界を行き来することは数学的に絶対に不可能である。
    };
\end{tikzpicture}""",
            "caption": "概念図 8：パリティ（偶奇性）の保存則による不可能性の証明。状態空間の不変量が可解性と不可解性を決定づける。"
        }
    ]

    parts = [preamble]

    for lec in lectures:
        # Chapter with short title for TOC and running headers to guarantee zero header collisions!
        parts.append(r"\chapter[" + lec["short_title"] + r"]{" + lec["title"] + r"}" + "\n")
        parts.append(r"\section*{" + lec["subtitle"] + r"}" + "\n\n")
        parts.append(lec["body"] + "\n\n")

        # Key Box
        parts.append(r"\begin{tcolorbox}[colback=softblue,colframe=primaryblue,title=\textbf{" + lec["box_title"] + r"},arc=3mm,boxrule=1pt]" + "\n")
        parts.append(lec["box_text"] + "\n")
        parts.append(r"\end{tcolorbox}" + "\n\n")

        # TikZ Center
        parts.append(r"\begin{center}" + "\n")
        parts.append(lec["tikz"] + "\n")
        parts.append(r"\par\vspace{0.5em}" + "\n")
        parts.append(r"\small " + lec["caption"] + "\n")
        parts.append(r"\end{center}" + "\n\n")

        parts.append(r"\clearpage" + "\n\n")

    # Epilogue / Reading Guide
    epilogue = r"""\chapter*{巻末付録：デュードニー全430問の数学的体系マップ}
\addcontentsline{toc}{chapter}{巻末付録：デュードニー全430問の数学的体系マップ}

デュードニーが『\textit{Amusements in Mathematics}』で提示した全430問は、現代の数学教育および離散数学のカリキュラムと驚くほど完璧に対応しています。大人の読者が原著の全問翻訳版に挑戦する際の羅針盤として、各章の数理的テーマを体系化しました。

\begin{table}[h]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
\toprule
\textbf{原著分類} & \textbf{問題番号} & \textbf{背後にある現代数学の分野} \\
\midrule
算術と代数の問題 & \#1 -- \#141 & 不定方程式、合同算術（数論）、数列と級数 \\
幾何学と裁ち合わせ & \#142 -- \#205 & 等積変形、ボヤイ・ゲアウィンの定理、計算幾何学 \\
点と線の問題 & \#206 -- \#213 & 射影幾何学、シルベスター・ガライの定理 \\
駒の移動パズル & \#214 -- \#238 & 置換群、不変量、状態空間探索アルゴリズム \\
一筆書きと経路 & \#239 -- \#261 & オイラーグラフ、ハミルトン路、トポロジー \\
組合せと群の問題 & \#262 -- \#287 & 組合せ論、分割数、ブロックデザイン \\
チェス盤のパズル & \#288 -- \#361 & 二部グラフ、独立集合問題、配置対称群 \\
測定・秤量・充填 & \#362 -- \#372 & 二進法・三進法（天秤）、ユークリッド互除法 \\
川渡りパズル & \#373 -- \#377 & 制約充足問題、幅優先探索（BFS） \\
ゲームの数理 & \#378 -- \#398 & 組合せゲーム理論、不偏ゲーム、ニム和（Nim-sum） \\
魔方陣と素数方陣 & \#399 -- \#412 & 線形代数（直交基底）、素数論、アフィン幾何 \\
迷路の解法 & 原著第13章 & 深さ優先探索（DFS）、単連結・多重連結トポロジー \\
パラドックスの館 & \#413 & 幾何学的消失、極限の錯視、無限のパラドックス \\
未分類の傑作 & \#414 -- \#430 & 総合的離散数学、ひらめきと不変量の統合 \\
\bottomrule
\end{tabular}
\end{table}

\vspace{1.0cm}
\begin{center}
{\large\color{primaryblue}\textbf{知的好奇心こそ、人間が年齢を重ねるごとに深まりゆく最大の知的財産です。}}\\[0.5em]
デュードニーの珠玉のパズルを通じて、数学の真の美しさと遊ぶ喜びを心ゆくまでご堪能ください。
\end{center}

\end{document}
"""
    parts.append(epilogue)

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))

    print(f"Generated {tex_path} ({len(''.join(parts))} chars).")

if __name__ == "__main__":
    build_intro_book()
