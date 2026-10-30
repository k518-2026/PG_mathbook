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
\definecolor{darkslate}{RGB}{45, 55, 72}        % 濃灰
\definecolor{forestgreen}{RGB}{25, 115, 65}     % 深緑
\definecolor{warmgold}{RGB}{195, 140, 20}       % 琥珀金

% --- Headers & Footers ---
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{darkslate}\leftmark}
\fancyhead[R]{\small\color{darkslate}古典で学び直すデュードニー数学パズル入門}
\fancyfoot[C]{\color{darkslate}\thepage}
\renewcommand{\headrulewidth}{0.5pt}

% --- Hyperref ---
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=accentcrimson,
    urlcolor=primaryblue,
    pdftitle={古典で学び直すデュードニー数学パズル入門},
    pdfauthor={教育情報分析研究会}
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
{\large — — 珠玉の430問から読み解く近代数学の核心 — —\par}
\vspace{1.0cm}
{\color{accentcrimson}\rule{0.6\textwidth}{1.5pt}}\par
\vspace{2.0cm}

\begin{tcolorbox}[colback=softblue,colframe=primaryblue,width=0.85\textwidth,arc=3mm,boxrule=1.2pt]
\centering\large
\textbf{ヘンリー・アーネスト・デュードニー} 原著\\
\textit{Amusements in Mathematics} (1917)\\
\vspace{0.5em}
\normalsize
50代〜80代から始める、知的好奇心を満たす大人のための数学再入門
\end{tcolorbox}

\vfill
{\Large\textbf{教育情報分析研究会} 編著\par}
\vspace{0.3cm}
{\large 2026年 校閲決定版\par}
\vspace{1.0cm}
\end{titlepage}

% --- Preface ---
\frontmatter
\chapter*{発刊にあたって —— 遊びの中に潜む数学の深淵}

パズルとは、単なる暇つぶしの遊戯でしょうか？

19世紀末から20世紀初頭にかけて、イギリスの知性を熱狂させた稀代の数学パズル作家ヘンリー・アーネスト・デュードニー（Henry Ernest Dudeney, 1857--1930）は、その問いに対して生涯をかけて明確な「否」を突きつけました。

デュードニーが雑誌『ストランド・マガジン』等で発表し、1917年に集大成として上梓した不朽の金字塔『\textit{Amusements in Mathematics}（数学の愉しみ）』に収められた全430問は、一見すると親しみやすい日常の物語やユーモアに満ちた小品でありながら、その背後にはオイラー以来の**グラフ理論**、ガウスが拓いた**合同算術と数論**、トポロジー（位相幾何学）、そして現代の**離散数学や計算機科学の根幹**をなす驚くべき数理構造が潜んでいます。

大人になってから数学を学び直す醍醐味は、学生時代のような「試験のために解法パターンを暗記する苦痛」から完全に解放され、**「なぜそのように解けるのか」「その背景にどんな美しい数学の原理が息づいているのか」**を、豊かな人生経験とともにゆったりと味わえる点にあります。

本書は、デュードニーの遺した全430問の中から、近代数学の扉を開く**最重要の8つのテーマ（全8講）**を厳選し、美しいTikZ図版と丁寧な数理的解説によって、高校までの知識で直観的に理解できるよう書き下ろした本格的な大人向け入門書です。

どうぞ、知的好奇心の翼を広げ、数学という名の最も魅惑的な遊園地へ足を踏み入れてください。

\tableofcontents
\mainmatter
"""

    lectures = [
        {
            "num": 1,
            "title": "第1講：ハバダッシャーの奇跡 —— 正三角形から正方形への幾何学的変身",
            "subtitle": "ヒンジ結合による図形分割・裁ち合わせ（Dissection）の極致",
            "body": r"""幾何学において、ある多角形を有限個のピースに切り分け、並べ替えて別の多角形を隙間なく組み立て直す操作を「裁ち合わせ（Dissection / 等積変形）」と呼びます。

19世紀末、ハンガリーの数学者ボヤイ・ファルカシュとドイツのゲアヴィンは、「面積の等しい任意の二つの多角形は、有限回の直線切断と並べ替えによって互いに移り変わることができる」というボヤイ・ゲアウィンの定理を証明しました。しかし、実際に「何個のピースで、どのように切断すればよいか」を見つけ出すことは、極めて高度な直観と数学的構成力を要求する難問です。

この分野における歴史上最大の傑作と称えられるのが、デュードニーが1902年に発表した「ハバダッシャー（洋品店主）のパズル（The Haberdasher's Puzzle, \#144・\#147の発展）」です。

彼は、一辺の長さが等しい正三角形を、わずか**「4つのピース」**に切り分け、それらがヒンジ（蝶番）で数珠つなぎになったまま回転させるだけで、完璧な「正方形」へと姿を変える驚異的な解法を発見しました。

正三角形の一辺を $a$ とすると面積は $S = \frac{\sqrt{3}}{4} a^2$ であり、これと等しい面積をもつ正方形の一辺は $x = \sqrt{S} = a \sqrt{\frac{\sqrt{3}}{4}} \approx 0.658 a$ となります。デュードニーは、正三角形の各辺の中点から垂線と平行線を巧みに組み合わせることで、無理数 $\sqrt[4]{3}$ を幾何学的に作図し、4片の連鎖変形を実現したのです。""",
            "box_title": "重要ポイント：裁ち合わせの数理とヒンジ連鎖",
            "box_text": r"""1. \textbf{ボヤイ・ゲアウィンの定理}：面積が等しい任意の2つの多角形は、有限個のピースへの分割によって必ず互いに変換可能である。
2. \textbf{最小ピース数の探求}：正三角形から正方形への変換は「4ピース」が理論的最小限界であることが証明されている。
3. \textbf{ヒンジ変形の幾何}：4つのピースは頂点でピン留めされており、裏返すことなく平面的にチェーン状に回すだけで三角形と正方形を往復する。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=1.1]
    % Left: Equilateral Triangle
    \begin{scope}[shift={(0,0)}]
        \coordinate (A) at (0, 3.464);
        \coordinate (B) at (-2, 0);
        \coordinate (C) at (2, 0);

        \draw[line width=1.5pt, primaryblue] (A) -- (B) -- (C) -- cycle;
        \node[above=3pt] at (A) {\textbf{\large $A$}};
        \node[below left=2pt] at (B) {\textbf{\large $B$}};
        \node[below right=2pt] at (C) {\textbf{\large $C$}};

        % Dissection lines
        \coordinate (D) at (-1, 1.732);
        \coordinate (E) at (1, 1.732);
        \coordinate (F) at (0, 0);

        \draw[line width=1.2pt, accentcrimson, dashed] (D) -- (E);
        \draw[line width=1.2pt, forestgreen] (D) -- (0.3, 0.7);
        \draw[line width=1.2pt, warmgold] (E) -- (-0.3, 0.7);

        \node[primaryblue] at (0, 2.3) {\textbf{\large 4ピース分割}};
        \node[below=12pt] at (0, 0) {\textbf{【正三角形】} 面積 $S = \frac{\sqrt{3}}{4} a^2$};
    \end{scope}

    % Center: Transformation arrow
    \draw[->, line width=2.0pt, accentcrimson] (3.0, 1.7) -- (5.2, 1.7)
        node[midway, above=4pt] {\small\textbf{ヒンジ回転変形}}
        node[midway, below=3pt] {\tiny （裏返さず連鎖回転）};

    % Right: Resulting Square
    \begin{scope}[shift={(6.4, 0.3)}]
        \coordinate (S1) at (0, 0);
        \coordinate (S2) at (2.6, 0);
        \coordinate (S3) at (2.6, 2.6);
        \coordinate (S4) at (0, 2.6);

        \draw[line width=1.5pt, accentcrimson, fill=softblue!40] (S1) -- (S2) -- (S3) -- (S4) -- cycle;
        \draw[line width=1.2pt, darkslate, dashed] (S1) -- (1.6, 2.6);
        \draw[line width=1.2pt, darkslate, dashed] (S2) -- (0.8, 1.8);

        \node at (1.3, 1.3) {\textbf{\large 完全な正方形}};
        \node[below=12pt] at (1.3, 0) {\textbf{【正方形】} 一辺 $x = a \sqrt{\frac{\sqrt{3}}{4}}$};
    \end{scope}
\end{tikzpicture}""",
            "caption": "概念図 1：デュードニーの最高傑作「ハバダッシャー・パズル」。正三角形から正方形への4分割ヒンジ連鎖変形。"
        },
        {
            "num": 2,
            "title": "第2講：オイラーの一筆書きとケーニヒスベルクの橋 —— 偶頂点と奇頂点",
            "subtitle": "トポロジーとグラフ理論の創始：なぜあの図形は描けないのか？",
            "body": r"""「鉛筆を紙から離さず、同じ線を二度通らずに描ききる」という一筆書き（Unicursal Problems, \#239--\#261）は、古くから人々の挑戦心をくすぐってきた定番パズルです。

この素朴な遊びに、現代数学の最重要分野である「位相幾何学（トポロジー）」および「グラフ理論」の礎を見出したのが、18世紀の大数学者レオンハルト・オイラー（1707--1783）でした。

オイラーは1736年、「ケーニヒスベルクの7つの橋をすべて一度だけ渡って元の場所に戻れるか」という問題に取り組み、橋の長さや陸地の形状といった幾何学的寸法をすべて捨て去り、「陸地を点（頂点 / Vertex）」、「橋を線（辺 / Edge）」とするネットワーク構造へと抽象化しました。

オイラーが確立した「一筆書き可能性の定理」は驚くほど明快です：
各頂点に接続する線の数が偶数本である頂点を**「偶頂点」**、奇数本である頂点を**「奇頂点」**と呼びます。線を描き進める際、ある頂点に「入って出る」ためには2本の線が必要となるため、始点と終点以外のすべての頂点は必ず偶数本の接続を持たなければなりません。

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

        \draw[line width=1.3pt, primaryblue] (A1) -- (B1) -- (D1) -- (C1) -- (A1);
        \draw[line width=1.3pt, primaryblue] (A1) -- (D1);
        \draw[line width=1.3pt, primaryblue] (-1.8,0) to[bend left=30] (1.8,0);

        \node[below=14pt, align=center] at (0, -1.2) {
            \textbf{【奇頂点 0個】}\\
            \small 全頂点が偶数次 $\to$ 出発点に戻る一筆書き可能
        };
    \end{scope}

    % Case B: Non-Eulerian (4 Odd Vertices)
    \begin{scope}[shift={(7.5, 0)}]
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (A2) at (-1.5, 2.0) {\textbf{3}};
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (B2) at (1.5, 2.0) {\textbf{3}};
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (C2) at (-1.5, -0.6) {\textbf{3}};
        \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, circle, inner sep=4pt] (D2) at (1.5, -0.6) {\textbf{3}};

        \draw[line width=1.3pt, darkslate] (A2) -- (B2) -- (D2) -- (C2) -- (A2);
        \draw[line width=1.3pt, darkslate] (A2) -- (D2);
        \draw[line width=1.3pt, darkslate] (B2) -- (C2);

        \node[below=14pt, align=center] at (0, -0.6) {
            \textbf{【奇頂点 4個】}\\
            \small 完全グラフ $K_4$ $\to$ \textbf{一筆書きは数学的に不可能}
        };
    \end{scope}
\end{tikzpicture}""",
            "caption": "概念図 2：オイラーの一筆書き判定原理。各頂点に集まる線の本数（偶数・奇数）が運命を完全に決定する。"
        },
        {
            "num": 3,
            "title": "第3講：チェス盤の数学 —— ナイト・ツアーと8クイーン問題",
            "subtitle": "二次元格子上の探索・対称群・ハミルトン路の数理",
            "body": r"""64個の白黒マスからなるチェス盤は、それ自体が豊かな離散数学の実験場です（\#288--\#361）。デュードニーはチェス盤を用いた数学パズルの第一人者でもありました。

代表的な古典問題の一つが「ナイト・ツアー（Knight's Tour, \#339--\#340）」です。チェスのナイト（八方に「2マス進んで1マス曲がる」L字型に跳ぶ駒）を盤上に置き、64マスすべてのマスを重複することなくちょうど1度ずつ訪問して元の位置に戻る（または終わる）ことができるか、という問題です。

グラフ理論の言葉で言えば、これは「ナイトの移動可能なマス同士を結んだグラフにおいて**ハミルトン閉路（Hamiltonian Cycle）**が存在するか」という問題に他なりません。

ナイト・ツアーには、チェス盤の市松模様（白黒）に由来する美しい数論的制約が存在します。ナイトは1回移動するごとに、必ず「白マスから黒マスへ」、あるいは「黒マスから白マスへ」と色を変えます。したがって、奇数回目の移動では出発点と異なる色のマスにあり、偶数回目で同じ色に戻ります。64マスを完全に巡回して元のマスに戻るためには、ちょうど64回の移動が必要となり、白32マスと黒32マスが交互に訪れられなければなりません。

さらにデュードニーは、各マスを訪れた順序の番号（1〜64）を書き込んだとき、縦・横・対角線の和がすべて等しくなるという「魔方陣ナイト・ツアー（Magic Knight's Tour, \#412）」という極限の芸術作品をも完成させました。""",
            "box_title": "重要ポイント：チェス盤上のグラフ探索と不変量",
            "box_text": r"""1. \textbf{白黒二部グラフ性}：ナイトの移動は「白 $\leftrightarrow$ 黒」の完全な二部グラフを形成し、同色マスへの直接移動は不可能である。
2. \textbf{ハミルトン路と閉路}：すべての頂点をちょうど1回ずつ訪れる巡回ルート。閉路ツアーと開路ツアーの2種類が存在する。
3. \textbf{8クイーン問題の独立性}：互いに利き筋（縦・横・斜め）に入らないよう8個のクイーンを配置する問題。解は基本12通り（回転・鏡像を含め全92通り）。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=0.85]
    % 8x8 Chessboard fragment (center 5x5 for clarity)
    \draw[step=1.2cm, darkslate!40, very thin] (-2.4, -2.4) grid (2.4, 2.4);
    \draw[line width=1.5pt, darkslate] (-2.4, -2.4) rectangle (2.4, 2.4);

    % Center Knight
    \filldraw[fill=primaryblue!20, draw=primaryblue, line width=1.4pt] (0, 0) circle (0.45);
    \node[primaryblue] at (0, 0) {\textbf{\large N}};

    % 8 Legal Knight moves
    \foreach \x/\y in {1.2/2.4, -1.2/2.4, 1.2/-2.4, -1.2/-2.4, 2.4/1.2, -2.4/1.2, 2.4/-1.2, -2.4/-1.2} {
        \filldraw[fill=accentcrimson!20, draw=accentcrimson, line width=1.2pt] (\x, \y) circle (0.35);
        \draw[->, line width=1.2pt, accentcrimson, dashed] (0, 0) -- (\x, \y);
    }

    % Side Explanation Box
    \node[draw=primaryblue, fill=softblue, rounded corners=2mm, text width=6.2cm, inner sep=8pt, align=left] at (6.8, 0) {
        \textbf{\large 【ナイト移動の不変量】}\\[4pt]
        \small
        $\bullet$ 移動ベクトル：$(\pm 1, \pm 2)$ または $(\pm 2, \pm 1)$\\[3pt]
        $\bullet$ 格子点間距離：$\sqrt{1^2 + 2^2} = \sqrt{5}$\\[3pt]
        $\bullet$ 色の交代性：白 $\leftrightarrow$ 黒（常に反転）\\[3pt]
        $\bullet$ 64手完全巡回 $\implies$ ハミルトン閉路\\
        \vspace{4pt}
        \footnotesize 対称性とパリティ（偶奇性）が全マス踏破の成否を握る。
    };
\end{tikzpicture}""",
            "caption": "概念図 3：チェスのナイトがもつ「L字移動」の対称性と白黒反転パリティ。ナイト・ツアーの数学的基礎。"
        },
        {
            "num": 4,
            "title": "第4講：川渡りパズルと状態遷移図 —— 制約充足問題の数理",
            "subtitle": "「狼・羊・キャベツ」から宣教師と人喰い人種へ：二進法とグラフ探索",
            "body": r"""「1艘の小さな舟があり、船頭のほかに1つしか乗せられない。狼と羊を二人きりにすると羊が食べられ、羊とキャベツを残すとキャベツが食べられてしまう。すべてを対岸へ無事に渡すにはどうすればよいか？」

この著名な川渡り問題（Crossing River Problems, \#373--\#377）の歴史は古く、8世紀の学者アルクィンがカール大帝のために編纂した『青年の精神を鍛えるための問題集』にまで遡ります。デュードニーはこれを発展させ、船の定員、乗客の家族構成や嫉妬深い夫たちなど、複雑な制約を加えた数々の名作を考案しました。

現代の数学・情報科学の視点から見ると、川渡り問題は**「状態空間のグラフ探索問題（State Space Search）」**に他なりません。

左岸にいるメンバーの組み合わせを状態ベクトル $(W, S, C, B)$（狼・羊・キャベツ・舟の各位置：0または1）として表すと、可能な状態は全 $2^4 = 16$ 通り存在します。このうち、「狼と羊が同居」「羊とキャベツが同居」（船頭が不在のとき）という禁止条件を除外すると、安全な状態はわずか数個に絞り込まれます。

安全な状態をノード（点）とし、舟による合法的な往復移動をエッジ（線）で結ぶと、**「始点 $(1,1,1,1)$ から終点 $(0,0,0,0)$ への最短経路探索」**という幾何学的な迷路問題へと完全に帰着されるのです。""",
            "box_title": "重要ポイント：状態空間と最短経路探索",
            "box_text": r"""1. \textbf{状態の二進数符号化}：各要素が「こちら側（1）」か「対岸（0）」かのブール値ベクトルで表現。
2. \textbf{安全制約フィルター}：禁止される状態（捕食・違反条件）を排除し、有効状態空間を特定する。
3. \textbf{グラフ上の最短経路}：幅優先探索（BFS）により、手戻りのない最小手数（7回移動）が機械的・論理的に導出される。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=0.95]
    % State nodes
    \node[draw=primaryblue, line width=1.3pt, fill=softblue, rounded corners=2mm, inner sep=6pt] (S0) at (0, 3.2) {\textbf{初期：(人, 狼, 羊, 菜)}};
    \node[draw=darkslate, line width=1.0pt, fill=white, rounded corners=2mm, inner sep=5pt] (S1) at (0, 1.8) {\small 羊を対岸へ渡す};
    \node[draw=darkslate, line width=1.0pt, fill=white, rounded corners=2mm, inner sep=5pt] (S2) at (0, 0.4) {\small 人が単独で戻る};
    \node[draw=darkslate, line width=1.0pt, fill=white, rounded corners=2mm, inner sep=5pt] (S3) at (-2.4, -1.0) {\small 狼を渡して羊を連れ戻す};
    \node[draw=darkslate, line width=1.0pt, fill=white, rounded corners=2mm, inner sep=5pt] (S4) at (2.4, -1.0) {\small 菜を渡して羊を連れ戻す};
    \node[draw=darkslate, line width=1.0pt, fill=white, rounded corners=2mm, inner sep=5pt] (S5) at (0, -2.4) {\small 菜（または狼）を渡す};
    \node[draw=accentcrimson, line width=1.5pt, fill=accentcrimson!15, rounded corners=2mm, inner sep=6pt] (S6) at (0, -3.8) {\textbf{完了：全員が無事に対岸へ！}};

    \draw[->, line width=1.2pt, primaryblue] (S0) -- (S1);
    \draw[->, line width=1.2pt, primaryblue] (S1) -- (S2);
    \draw[->, line width=1.2pt, primaryblue] (S2) -- (S3);
    \draw[->, line width=1.2pt, primaryblue] (S2) -- (S4);
    \draw[->, line width=1.2pt, primaryblue] (S3) -- (S5);
    \draw[->, line width=1.2pt, primaryblue] (S4) -- (S5);
    \draw[->, line width=1.5pt, accentcrimson] (S5) -- (S6);

    % Right Key insight box
    \node[draw=warmgold!80!black, fill=warmgold!10, rounded corners=2mm, text width=5.0cm, inner sep=7pt, align=left] at (6.2, -0.4) {
        \textbf{\small 【逆転の着眼点】}\\[3pt]
        \footnotesize
        荷物を対岸に運ぶだけでなく、一時的に「羊を連れ戻す」という一見後退に見える手が、制約充足の唯一の突破口となる。
    };
\end{tikzpicture}""",
            "caption": "概念図 4：川渡りパズルの状態遷移ネットワーク。後退手を含むグラフ探索が最適解（7手）を導く。"
        },
        {
            "num": 5,
            "title": "第5講：魔方陣の美学 —— 対称群・素数方陣・二重複合方陣",
            "subtitle": "縦・横・斜めの和が一致する数論の結晶：デューラーからデュードニーへ",
            "body": r"""$1$ から $n^2$ までの自然数を正方形のマス目に重複なく並べ、縦・横・対角線のすべての和が等しくなるように配置したものを「$n$次魔方陣（Magic Squares, \#399--\#412）」と呼びます。

その行や列の一定の和を**「魔方陣定数（Magic Constant）」**と呼び、数学的には初項から末項までの総和 $\frac{n^2(n^2+1)}{2}$ を $n$ 等分することで次のように一意に定まります：
\[
M(n) = \frac{n(n^2+1)}{2}
\]
3次魔方陣なら $M(3) = 15$、4次魔方陣なら $M(4) = 34$、8次魔方陣なら $M(8) = 260$ となります。

3次魔方陣（中国古代の「洛書」）は、回転や鏡像を除くと本質的に**1種類**しか存在しません。中心の数は必ず平均値である「5」となり、四隅には偶数（2, 4, 6, 8）、十字の辺中央には奇数（1, 3, 7, 9）が配置されるという厳格な代数構造を持っています。

デュードニーはこの古典魔方陣の地平をさらに押し広げました：
1. **素数魔方陣（Magic Squares of Primes）**：すべての構成要素が「素数」だけで作られた魔方陣。
2. **二階魔方陣（Magic Squares of Two Degrees, \#408）**：元の数の配置で魔方陣であるだけでなく、すべてのマスを「2乗（平方）」してもなお魔方陣であり続けるという驚異の方陣。

整数の合同算術（モジュロ演算）とアフィン変換の理論が、この神秘的な数の配列の背後で完璧に調和しています。""",
            "box_title": "重要ポイント：魔方陣の代数構造と対称性",
            "box_text": r"""1. \textbf{不変定数の公式}：$n$次通常魔方陣の各行・各列・対角線の和は常に $M = \frac{n(n^2+1)}{2}$ に固定される。
2. \textbf{中心核の性質}：奇数次魔方陣の中心マスには、必ず全要素の中央値（3次なら $\frac{1+9}{2}=5$）が鎮座する。
3. \textbf{高階魔方陣の奇跡}：数の和だけでなく平方和（$\sum x^2$）まで一定になる方陣は、ディオファントス方程式の精緻な解である。""",
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
            \small 各列・行・対角線の和 $= \mathbf{15}$（中心は常に $5$）
        };
    \end{scope}

    % Mathematical Decomposition Box
    \node[draw=primaryblue, fill=softblue, rounded corners=2mm, text width=6.2cm, inner sep=9pt, align=left] at (7.2, 1.8) {
        \textbf{\large 【魔方陣の数学的分解】}\\[5pt]
        \small 任意の3次魔方陣は、中心を $x$、公差を $a, b$ とする直交基底の線形結合として表される：\\[4pt]
        \centering
        \begin{tabular}{|c|c|c|}
        \hline
        $x+b$ & $x-a-b$ & $x+a$ \\ \hline
        $x+a-b$ & $x$ & $x-a+b$ \\ \hline
        $x-a$ & $x+a+b$ & $x-b$ \\ \hline
        \end{tabular}\\[6pt]
        \raggedright\footnotesize
        線形代数における3次元ベクトル空間の美しい直交基底をなしている。
    };
\end{tikzpicture}""",
            "caption": "概念図 5：3次魔方陣の構造と、線形代数学によるパラメータ分解表示。"
        },
        {
            "num": 6,
            "title": "第6講：迷路の幾何学と脱出アルゴリズム —— トレモーの解法",
            "subtitle": "トポロジー的連結性・壁づたい法・深さ優先探索（DFS）の起源",
            "body": r"""迷路（Mazes and How to Thread Them, 原著第13章）は、古来より神話（クノッソスの迷宮とミノタウロス）や造園芸術として親しまれてきましたが、数学者にとっては**「未知の連結グラフを有限時間で完全走破するアルゴリズム」**の研究対象です。

デュードニーは、迷路の構造を幾何学的に分類し、どのような迷路であっても確実に脱出できる数学的手法を解説しました。

最も素朴な手法は「右手（または左手）を常に壁につけたまま歩き続ける」という**「壁づたい法（Wall Follower）」**です。この方法は、迷路のスタートとゴールが外周の壁に連結している「単連結（Simply Connected）」な迷路においては、必ずゴールに到達できることがトポロジー的に保証されています。

しかし、迷路の内部に「浮島（ループ状の壁の塊）」が存在し、ゴールがその島の中にあるような「多重連結（Multiply Connected）」の迷路では、壁づたい法を行うと同じループを無限に旋回してしまい、脱出に失敗します。

この難問を完全に解決したのが、19世紀のフランスの数学者シャルル・ピエール・トレモーが考案した**「トレモーのアルゴリズム（Trémaux's Algorithm）」**です。
- 初めて通る通路には印を1つつける。
- 行き止まりに当たったら引き返し、その通路に2つ目の印をつける（二度と入らない）。
- 交差点（分岐点）に来たとき、未探索の通路があればそれを優先し、既知の通路なら引き返す。

このルールに従うことで、人間はどんな複雑怪奇な多重連結迷路であっても、**すべての通路を最大でも「往復（2回）」通るだけで必ず脱出できる**のです。これはまさに、現代のコンピュータが巨大なネットワークを探索する「深さ優先探索（DFS）」の原型そのものです。""",
            "box_title": "重要ポイント：迷路探索のトポロジーと計算量",
            "box_text": r"""1. \textbf{単連結と多重連結}：壁が一本につながっているか、独立したループ状の島壁を含むかによる分類。
2. \textbf{壁づたい法の限界}：外周壁に属さない浮島上のゴールには到達できない（無限ループの発生）。
3. \textbf{トレモーの完全性}：分岐点でのマーキング操作により、全辺を高々2回辿るだけで有限時間内に確実に脱出を保証する。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=1.0]
    % Maze graph abstraction
    \node[draw=primaryblue, line width=1.5pt, fill=softblue, circle, inner sep=4pt] (IN) at (0, 0) {\textbf{入口}};
    \node[draw=darkslate, line width=1.2pt, fill=white, circle, inner sep=4pt] (A) at (2.2, 1.2) {\textbf{分岐 $A$}};
    \node[draw=darkslate, line width=1.2pt, fill=white, circle, inner sep=4pt] (B) at (2.2, -1.2) {\textbf{分岐 $B$}};
    \node[draw=accentcrimson, line width=1.2pt, fill=accentcrimson!15, rectangle, rounded corners, inner sep=4pt] (DEAD) at (4.6, 1.2) {\textbf{行き止まり}};
    \node[draw=forestgreen, line width=1.5pt, fill=forestgreen!20, circle, inner sep=5pt] (OUT) at (5.2, -1.2) {\textbf{出口}};

    % Paths
    \draw[->, line width=1.5pt, primaryblue] (IN) -- (A) node[midway, above] {\small 1本線 (進行)};
    \draw[->, line width=1.5pt, darkslate] (A) -- (DEAD) node[midway, above] {\small 初進入};
    \draw[->, line width=1.5pt, accentcrimson, dashed] (DEAD) to[bend left=25] node[midway, below] {\small 2本線 (封鎖)} (A);
    \draw[->, line width=1.5pt, primaryblue] (A) -- (B) node[midway, right] {\small 未探索へ};
    \draw[->, line width=1.8pt, forestgreen] (B) -- (OUT) node[midway, above] {\textbf{\small ゴール到達！}};

    % Explanation Box
    \node[draw=primaryblue, fill=white, rounded corners=2mm, text width=12cm, inner sep=7pt, align=left] at (2.6, -2.8) {
        \small \textbf{トレモーの規則}：通路に印をつけることで、「未踏の道」と「探索済みの袋小路」を厳密に区別する。\\
        いかなる多重連結迷路も、各通路を往復（計2回）以上通過することなく、有限時間で完全走破される。
    };
\end{tikzpicture}""",
            "caption": "概念図 6：トレモーの迷路走破アルゴリズム。袋小路の二重印封鎖と深さ優先探索のメカニズム。"
        },
        {
            "num": 7,
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
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=0.9]
    % Coordinate axes
    \draw[->, thick, darkslate] (-0.5, 0) -- (8.5, 0) node[right] {\textbf{$x$（2ペンス切手基準）}};
    \draw[->, thick, darkslate] (0, -0.5) -- (0, 6.0) node[above] {\textbf{$y$（2.5ペンス切手枚数）}};

    % Line: 16x + 5y = 120 -> y = 24 - 3.2x
    % at x=0, y=24 (off screen), at x=5, y=8. Let's scale y by 0.2
    \draw[line width=1.5pt, primaryblue] (0, 4.8) -- (7.5, 0) node[midway, above right] {\small 直線 $16x + 5y = 120$};

    % Integer grid points
    \foreach \px in {1,2,3,4,5,6,7} {
        \foreach \py in {1,2,3,4,5} {
            \fill[gray!40] (\px, \py) circle (1.5pt);
        }
    }

    % The Unique Integer Solution (x=5, y=1.6 in scaled coords -> y=8 in reality)
    \filldraw[fill=accentcrimson, draw=accentcrimson, line width=1.5pt] (5, 1.6) circle (4pt);
    \node[above right=4pt, accentcrimson] at (5, 1.6) {\textbf{\large 唯一の自然数解 $(x=5, y=8)$}};

    % Inadmissible point x=0, y=24
    \filldraw[fill=darkslate!40, draw=darkslate] (0, 4.8) circle (3pt);
    \node[left=3pt] at (0, 4.8) {\footnotesize $(0, 24)$ [切手無指定]};

    % Inadmissible point x=7.5, y=0
    \node[below=3pt] at (7.5, 0) {\footnotesize $(7.5, 0)$ [非整数]};
\end{tikzpicture}""",
            "caption": "概念図 7：一次不定方程式 $16x + 5y = 120$ のグラフ。格子点（整数解）条件により唯一の解 $(5, 8)$ が抽出される。"
        },
        {
            "num": 8,
            "title": "第8講：不変量とパリティ —— パズルが暴く「不可能性」の証明",
            "subtitle": "15パズル・盤面の反転・市松模様：なぜその配置には到達できないのか？",
            "body": r"""数学パズルの真髄は、「解けたときの喜び」だけにあるのではありません。それ以上に深い知的な感動を与えてくれるのが、**「ある操作をいくら繰り返しても、その状態には絶対に到達できない」という不可能性の証明**です。

その最強の思考の武器が**「不変量（Invariant）」**と**「パリティ（偶奇性 / Parity）」**です。

有名な「15パズル（15 Puzzle, \#214--\#238の駒移動パズルと同型）」を考えてみましょう。1から15までの数字が書かれた正方形の駒を4×4の枠の中でスライドさせ、順番を揃えるゲームです。1870年代、サミュエル・ロイドは「14」と「15」の駒だけが入れ替わった初期配置を提示し、これを正しく整列させることができた者に巨額の賞金を懸けました。

世界中の人々が何日も駒を動かし続けましたが、誰一人として賞金を獲得することはできませんでした。なぜなら、それは**数学的に「絶対に解けない配置」**だったからです。

ある駒の並び順において、大きな数が小さな数より前にあるペアの個数を「転倒数（Inversion Number）」と呼びます。駒を左右に1マススライドさせても並び順は変わらないため転倒数は不変です。駒を上下にスライドさせると、ちょうど3つの駒を飛び越えるため、転倒数の増減は必ず奇数（$\pm 1$ または $\pm 3$）となります。同時に空マスの行数も1行変化します。

ここで、「転倒数」と「空マスの行数」の和の偶奇性（パリティ）を計算すると、**どのような合法的なスライド操作を行っても、このパリティは常に「一定（不変）」に保たれる**ことが厳密に証明されます。

14と15が入れ替わった配置は、目標の配置とパリティが正反対（奇数と偶数）であるため、宇宙の寿命が尽きるまで駒を動かし続けても、目標配置には絶対に到達できないのです。

デュードニーは、カウンターパズルやチェス盤パズルにおいて、この不変量と市松模様のパリティを鮮やかに使いこなし、見かけの複雑さに惑わされない「数学的真実の透視法」を世に示しました。""",
            "box_title": "重要ポイント：不変量と対称性の論理",
            "box_text": r"""1. \textbf{不変量（インバリアント）}：状態が遷移しても変化しない数学的性質。物理学の保存則（エネルギー・運動量）と完全に同義。
2. \textbf{パリティの保存}：偶奇性の不変により、状態空間は互いに交わらない2つの独立した宇宙（可到達領域と不可到達領域）に二分される。
3. \textbf{不可能性の証明の価値}：「できないこと」を論理的に証明することは、無駄な努力を永久に断ち切る人間知性の最高峰の業績である。""",
            "tikz": r"""\begin{tikzpicture}[>=Stealth, scale=1.0]
    % State space division
    \draw[line width=1.5pt, primaryblue, fill=softblue!30, rounded corners=3mm] (-5.5, -2.2) rectangle (-0.5, 2.2);
    \node[primaryblue] at (-3.0, 1.7) {\textbf{\large 【偶パリティの世界】}};
    \node[draw=forestgreen, line width=1.3pt, fill=white, rounded corners, inner sep=6pt] (START) at (-3.0, 0.6) {\textbf{初期配置 (正順)}};
    \node[draw=forestgreen, line width=1.3pt, fill=white, rounded corners, inner sep=6pt] (TARGET) at (-3.0, -0.8) {\textbf{目標完成形 $(1 \sim 15)$}};
    \draw[<->, line width=1.5pt, forestgreen] (START) -- (TARGET) node[midway, right] {\small 相互移動可能};

    % Wall of impossibility
    \draw[line width=3.0pt, accentcrimson, dashed] (0, -2.5) -- (0, 2.5) node[midway, fill=white, inner sep=4pt] {\textbf{\large 不可能の壁}};

    % Impossible state space
    \draw[line width=1.5pt, accentcrimson, fill=accentcrimson!10, rounded corners=3mm] (0.5, -2.2) rectangle (5.5, 2.2);
    \node[accentcrimson] at (3.0, 1.7) {\textbf{\large 【奇パリティの世界】}};
    \node[draw=accentcrimson, line width=1.3pt, fill=white, rounded corners, inner sep=6pt, align=center] (LOYD) at (3.0, -0.1) {
        \textbf{ロイドの難問}\\
        \small （14と15が反転した配置）
    };

    % Barrier arrow
    \draw[->, line width=2.0pt, darkslate] (LOYD) -- (0.2, -0.1) node[above=4pt] {\Large $\times$};
    \node[below=14pt] at (0, -2.5) {
        \small \textbf{結論}：スライド操作はパリティを保存するため、二つの世界を行き来することは数学的に絶対に不可能である。
    };
\end{tikzpicture}""",
            "caption": "概念図 8：パリティ（偶奇性）の保存則による不可能性の証明。状態空間の不変量が可解性と不可解性を決定づける。"
        }
    ]

    parts = [preamble]

    for lec in lectures:
        num = lec["num"]
        parts.append(r"\chapter{" + lec["title"] + r"}" + "\n")
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
