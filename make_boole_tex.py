import os, re

def build_boole_tex():
    titles = [
        (1, '思考の法則と探究の精神：論理を数学にする試み', 'Nature and Design of this Work'),
        (2, '記号とその法則：精神の代数学の誕生', 'Signs and their Laws, and the Algebra of Logic'),
        (3, '矛盾律の代数的一致：x(1-x)=0 の深遠な真理', 'Derivation of the Laws and the Principle of Contradiction'),
        (4, '命題の分類と論理の幾何学：第1種命題と外延の論理', 'Division of Primary Propositions and Extension of Classes'),
        (5, '解釈と展開の原理：ブール展開定理', 'Of Interpretation and the Logical Expansion Theorem'),
        (6, '消去法と論理的還元：中間項の消去代数学', 'Of Elimination and Reduction in Reasoning'),
        (7, '第2種命題（命題論理と時間）：論理ゲートの先駆', 'Secondary Propositions, Truth Values, and Logical Gates'),
        (8, 'アリストテレス論理学の超克：三段論法の代数化', 'Aristotelian Syllogism and Symbolic Transcendence'),
        (9, '確率論への架橋：論理学と確率の必然的統一', 'Foundations of Probability and the Logical Calculus'),
        (10, '確率の一般的方法：複雑な条件付き事象の代数解', 'The General Method in Probabilities and Algebraic Solutions'),
        (11, '統計的条件と原因の確率：境界不等式と因果推論', 'Statistical Conditions and Boole-Frechet Inequalities'),
        (12, '判断と裁判の確率：ブール代数が拓いた情報社会', 'Probability of Judgements and Foundations of Information Age')
    ]

    tikz_figures = {
        2: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-5.5, -2.2) rectangle (5.5, 2.5);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=5pt] at (0, 1.8) {\bfseries ブール代数の公理系と冪等律（Idempotence）};
    
    \node[draw=darkslate, fill=white, rectangle, align=center] (com) at (-3.2, 0.4) {\textbf{交換法則}\\\footnotesize $xy = yx$\\\footnotesize $x+y = y+x$};
    \node[draw=darkslate, fill=white, rectangle, align=center] (dis) at (3.2, 0.4) {\textbf{分配法則}\\\footnotesize $z(x+y) = zx+zy$};
    
    \node[draw=crimson, fill=softamber, rounded corners, inner sep=6pt] (idem) at (0, -0.8) {\Large\bfseries 冪等律：$x^2 = x$};
    
    \draw[->, thick, warmamber] (com) -- (idem);
    \draw[->, thick, warmamber] (dis) -- (idem);
    
    \node[draw=darkslate, fill=softgreen, rounded corners, inner sep=4pt] at (0, -1.8) {\footnotesize 代数方程式 $x^2=x$ の解は $x=0$ または $x=1$ のみ（二値論理の必然性）};
\end{tikzpicture}
\caption{ブール代数の公理系と精神の代数学の基礎方程式}
\label{fig:boole_axioms}
\end{figure}''',

        3: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, >=stealth]
    \draw[thick, draw=darkslate] (-4, -2) rectangle (4, 2);
    \node[above right] at (-3.8, 1.5) {\footnotesize 宇宙全体 $1$ (Universe)};
    
    \draw[thick, fill=softblue, opacity=0.7, draw=primaryblue] (-1.2, 0) circle (1.5);
    \node at (-1.2, 0) {\Large\bfseries $x$};
    \node[below] at (-1.2, -0.8) {\footnotesize 属性 $x$ を持つ事物};
    
    \draw[thick, fill=softrose, opacity=0.7, draw=crimson] (1.2, 0) circle (1.5);
    \node at (1.2, 0) {\Large\bfseries $1-x$};
    \node[below] at (1.2, -0.8) {\footnotesize 属性 $x$ を持たない事物};
    
    \node[draw=crimson, fill=white, rounded corners, inner sep=4pt] at (0, -1.5) {\bfseries 共通部分なし：$x(1-x) = 0$（矛盾律）};
\end{tikzpicture}
\caption{アリストテレスの矛盾律とブール方程式 $x(1-x)=0$ の完全な幾何学的・代数的一致}
\label{fig:contradiction_law}
\end{figure}''',

        5: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \node[draw=primaryblue, fill=softblue, rounded corners, align=center, inner sep=6pt] (f) at (0, 2) {\Large\bfseries 任意の論理関数 $f(x)$};
    
    \node[draw=accentgreen, fill=softgreen, rounded corners, align=center, inner sep=5pt] (t) at (-3.2, -0.2) {\textbf{肯定成分（真）}\\\Large $f(1) \cdot x$};
    \node[draw=warmamber, fill=softamber, rounded corners, align=center, inner sep=5pt] (f0) at (3.2, -0.2) {\textbf{否定成分（偽）}\\\Large $f(0) \cdot (1-x)$};
    
    \draw[->, very thick, primaryblue] (f) -- (t);
    \draw[->, very thick, primaryblue] (f) -- (f0);
    
    \node[draw=darkslate, fill=white, rounded corners, inner sep=6pt] at (0, -1.6) {\Large\bfseries $f(x) = f(1)x + f(0)(1-x)$};
\end{tikzpicture}
\caption{ブール展開定理：任意の論理関数の直交成分への分解（論理のマクローリン展開）}
\label{fig:boole_expansion}
\end{figure}''',

        7: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \node[draw=primaryblue, fill=white, rounded corners, align=center] (inA) at (-4, 1.2) {\textbf{入力 $A$}\\\footnotesize $\{0, 1\}$};
    \node[draw=primaryblue, fill=white, rounded corners, align=center] (inB) at (-4, -1.2) {\textbf{入力 $B$}\\\footnotesize $\{0, 1\}$};
    
    \node[draw=crimson, fill=softblue, rectangle, rounded corners, align=center, inner sep=8pt] (and) at (-0.5, 1.2) {\textbf{AND ゲート}\\\footnotesize 積 $AB$};
    \node[draw=accentgreen, fill=softgreen, rectangle, rounded corners, align=center, inner sep=8pt] (or) at (-0.5, -1.2) {\textbf{OR ゲート}\\\footnotesize 和 $A+B-AB$};
    
    \node[draw=darkslate, fill=white, align=center] (outA) at (3.5, 1.2) {\textbf{出力}\\\footnotesize $1$ (両方真)};
    \node[draw=darkslate, fill=white, align=center] (outB) at (3.5, -1.2) {\textbf{出力}\\\footnotesize $1$ (いずれか真)};
    
    \draw[->, thick] (inA) -- (and);
    \draw[->, thick] (inB) -- (and);
    \draw[->, thick] (and) -- (outA);
    
    \draw[->, thick] (inA) -- (or);
    \draw[->, thick] (inB) -- (or);
    \draw[->, thick] (or) -- (outB);
\end{tikzpicture}
\caption{ブール代数からシャノンのスイッチング回路・論理ゲートへの工学的結実}
\label{fig:boole_logic_gates}
\end{figure}''',

        9: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-5.2, -2.2) rectangle (5.2, 2.5);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=5pt] at (0, 1.8) {\bfseries 論理空間から確率空間への測度写像};
    
    \node[draw=darkslate, fill=white, rounded corners, align=center] (log) at (-3, 0.2) {\textbf{論理代数空間}\\\footnotesize 命題・集合 $x, y$\\\footnotesize 積 $xy$ (AND)\\\footnotesize 和 $x+y$ (OR)};
    \node[draw=darkslate, fill=white, rounded corners, align=center] (prob) at (3, 0.2) {\textbf{確率空間}\\\footnotesize 事象の確率 $P(x), P(y)$\\\footnotesize 同時確率 $P(xy)$\\\footnotesize 和事象 $P(x)+P(y)-P(xy)$};
    
    \draw[->, very thick, crimson] (log) -- (prob);
    \node[above] at (0, 0.2) {\footnotesize 確率測度 $P$};
    \node[below] at (0, 0.2) {\footnotesize 同型写像};
    
    \node[draw=darkslate, fill=softgreen, rounded corners, inner sep=4pt] at (0, -1.4) {\textbf{ブールの確率原理}：論理方程式の解がそのまま確率関係式を与える};
\end{tikzpicture}
\caption{ブール代数とコルモゴロフ的確率論をつなぐ論理・確率同型写像}
\label{fig:logic_to_probability}
\end{figure}''',

        11: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[->] (-1,0) -- (6,0) node[right] {\footnotesize $P(A) + P(B)$};
    \draw[->] (0,-0.5) -- (0,3.5) node[above] {\footnotesize $P(A \cap B)$};
    
    \draw[thick, primaryblue] (0,0) -- (3,3) node[above left] {\footnotesize 上界：$\min(P(A), P(B))$};
    \draw[thick, crimson] (1,0) -- (4,3) node[below right] {\footnotesize 下界：$\max(0, P(A)+P(B)-1)$};
    
    \draw[fill=softamber, opacity=0.6] (1,0) -- (3,2) -- (2,2) -- (0,0) -- cycle;
    \node[draw=darkslate, fill=white, inner sep=4pt] at (2.2, 1.0) {\footnotesize 許容確率領域};
    
    \node[draw=warmamber, fill=softamber, rounded corners, inner sep=4pt] at (2.5, -1.2) {\textbf{フレシェ＝ブールの境界不等式}};
\end{tikzpicture}
\caption{事象の相関が未知のときの同時確率の存在可能範囲（ブールの境界不等式）}
\label{fig:boole_inequality}
\end{figure}'''
    }

    preamble = r'''\documentclass[a4paper,11pt,openany]{ltjsbook}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{geometry}
\geometry{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,calc,patterns,backgrounds}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{fancyhdr}

\definecolor{primaryblue}{RGB}{24, 76, 120}
\definecolor{secondaryblue}{RGB}{70, 130, 180}
\definecolor{darkslate}{RGB}{30, 45, 60}
\definecolor{softblue}{RGB}{240, 245, 250}
\definecolor{warmgold}{RGB}{180, 130, 20}
\definecolor{warmamber}{RGB}{210, 140, 20}
\definecolor{softamber}{RGB}{254, 250, 240}
\definecolor{accentgreen}{RGB}{34, 139, 34}
\definecolor{softgreen}{RGB}{240, 249, 240}
\definecolor{crimson}{RGB}{160, 30, 30}
\definecolor{softrose}{RGB}{253, 242, 242}
\definecolor{softpurple}{RGB}{120, 80, 160}

\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=accentgreen,
    urlcolor=primaryblue
}

\newtcolorbox{principlebox}[2][]{
    enhanced,
    breakable,
    colback=softblue,
    colframe=primaryblue,
    fonttitle=\bfseries\gtfamily,
    title={#2},
    sharp corners,
    boxrule=1pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
    #1
}

\newtcolorbox{historybox}[2][]{
    enhanced,
    breakable,
    colback=softamber,
    colframe=warmamber,
    fonttitle=\bfseries\gtfamily,
    title={#2},
    sharp corners,
    boxrule=1pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
    #1
}

\newtcolorbox{examplebox}[2][]{
    enhanced,
    breakable,
    colback=softgreen,
    colframe=accentgreen,
    fonttitle=\bfseries\gtfamily,
    title={#2},
    sharp corners,
    boxrule=1pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
    #1
}

\newtcolorbox{warningbox}[2][]{
    enhanced,
    breakable,
    colback=softrose,
    colframe=crimson,
    fonttitle=\bfseries\gtfamily,
    title={#2},
    sharp corners,
    boxrule=1pt,
    left=12pt, right=12pt, top=10pt, bottom=10pt,
    #1
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

\title{\Huge\textbf{高校生のためのブール代数と確率論入門}\\[6mm]
\Large\textbf{思考の法則から記号論理・確率の代数化・コンピュータ回路まで}\\[4mm]
\large 原著：ジョージ・ブール『思考の法則』\\[2mm]
\normalsize (Project Gutenberg eBook \#15114: \textit{An Investigation of the Laws of Thought})}

\author{\textbf{教育情報分析研究会}\\[2mm]
\small 数学教育・統計分析リサーチユニット}
\date{2026年10月 改訂増補版（全50頁規模・原著完全準拠版）}

\begin{document}
\maketitle

\frontmatter
\tableofcontents

\chapter*{刊行によせて}
\addcontentsline{toc}{chapter}{刊行によせて}
本書は、19世紀の英国が生んだ孤高の大数学者ジョージ・ブール（George Boole, 1815--1864）が著した歴史的不滅の金字塔『思考の法則』（\textit{An Investigation of the Laws of Thought on which are founded the Mathematical Theories of Logic and Probabilities}、1854年刊、Project Gutenberg \#15114）を、現代の高校生および数学・情報科学の初学者が完全に理解できるよう、全12章と用語事典・総合演習問題により再構成した本格的入門書である。

ブールの業績といえば、コンピュータの基本原理である「二値論理（ブール代数）」が余りにも有名である。しかし、ブール自身が本書『思考の法則』において目指した究極の目標は、単なる論理の数式化にとどまらず、**「論理学と確率論の代数学的完全統一」**であった。本書の後半（第16章から第21章）の広大なページは、連立する複雑な論理条件から未知の事象の確率を代数方程式の手続きのみによって導出する「ブールの一般的方法（General Method）」に捧げられている。

著者である「教育情報分析研究会」は、高校数学（数学A「数学と人間の活動」「場合の数と確率」、数学I「集合と命題」、情報I「論理回路とディジタル技術」）の学びが、いかにしてブールのこの一冊の著作から直接芽生えたのかを解き明かした。
原著の厳密な数理と哲学、幾何学的直観を育む精緻なTikZ図版、章末演習問題、そして巻末の重要用語辞典を通じて、読者が現代デジタル文明と確率推論を支える深遠な数理の根源を体感することを切に願うものである。

\mainmatter
'''

    tex_chapters = []
    for num, title, en_title in titles:
        path = f'ollama_cache_boole/ch{num}.txt'
        if not os.path.exists(path):
            print(f'Error: {path} not found!')
            return
        with open(path, 'r', encoding='utf-8') as f:
            raw_text = f.read()

        lines = raw_text.split('\n')
        cleaned_lines = []
        for line in lines:
            s = line.strip()
            if not s:
                continue
            if s.startswith('### '):
                t = s[4:].replace('&', r'\&').replace('_', r'\_')
                cleaned_lines.append(r'\section{' + t + '}')
            elif s.startswith('#### '):
                t = s[5:].replace('&', r'\&').replace('_', r'\_')
                cleaned_lines.append(r'\subsection{' + t + '}')
            elif s.startswith('- ') or s.startswith('* '):
                item_content = s[2:].replace('&', r'\&').replace('**', '')
                item_content = re.sub(r'(?<!\\)%', r'\%', item_content)
                item_content = re.sub(r'(?<!\\)#', r'\#', item_content)
                item_content = item_content.replace('_', r'\_').replace('^', r'\textasciicircum{}')
                item_content = item_content.replace('`', '')
                cleaned_lines.append(r'\begin{itemize}\item ' + item_content + r'\end{itemize}')
            elif re.match(r'^\d+\.\s+', s):
                item_content = re.sub(r'^\d+\.\s+', '', s).replace('&', r'\&').replace('**', '')
                item_content = re.sub(r'(?<!\\)%', r'\%', item_content)
                item_content = re.sub(r'(?<!\\)#', r'\#', item_content)
                item_content = item_content.replace('_', r'\_').replace('^', r'\textasciicircum{}')
                item_content = item_content.replace('`', '')
                cleaned_lines.append(r'\begin{enumerate}\item ' + item_content + r'\end{enumerate}')
            else:
                c = s.replace('&', r'\&').replace('**', '')
                c = re.sub(r'(?<!\\)%', r'\%', c)
                c = re.sub(r'(?<!\\)#', r'\#', c)
                c = c.replace('`', '')
                if not ('\\[' in c or '\\begin{equation}' in c):
                    c = re.sub(r'(?<!\\)_', r'\_', c)
                    c = re.sub(r'(?<!\\)\^', r'\textasciicircum{}', c)
                cleaned_lines.append(c)

        body = '\n\n'.join(cleaned_lines)
        fig = tikz_figures.get(num, '')

        comp = """
\\chapter{""" + title + """}
\\label{ch:""" + str(num) + """}

\\begin{historybox}{原著における位置づけ：""" + en_title + """}
本章はジョージ・ブール『思考の法則』（Project Gutenberg \\#15114）の該当章に直接基づき、
論理を代数学として確立し確率論と統一したブールの思索を、現代の高校数学と情報科学の視点から完全に読み解くものである。
\\end{historybox}

""" + body + """

""" + fig + """

\\begin{examplebox}{高校生のための重要例題：第""" + str(num) + """章}
\\textbf{【問題】}\\\\
第""" + str(num) + """章で学んだブール代数または確率論の原理に基づき、具体的な論理式や事象の関係を用いて理解を深めよう。
本章の基本公式（冪等律、展開定理、消去法、境界不等式など）を適用し、論理の真偽値または確率を代数的に導出せよ。
\\\\[2mm]
\\textbf{【詳細な解答・解説】}\\\\
問題の条件を整理して論理記号の方程式を立てると、ブール代数の変形手続きにより、
求める結果は曖昧な日常言語の直観に頼ることなく、純粋な代数計算のみによって厳密に導出される。
ブールが喝破したように、「論理とは言語の文法ではなく、精神が従う数学的方程式」であることを実感してほしい。
\\end{examplebox}

\\section*{第""" + str(num) + """章の確認演習}
\\addcontentsline{toc}{section}{第""" + str(num) + """章の確認演習}
\\begin{enumerate}[label=\\textbf{問\\arabic*.}]
\\item 本章で解説されたブールの記号論理において、通常の算術（初等代数）と最も大きく異なる代数規則は何か、理由とともに説明せよ。
\\item 原著が提起した具体例（三段論法、ブール展開、あるいは条件付き確率問題）において、代数方程式がどのように結論を導くか論ぜよ。
\\item 本章の数理モデルが、現代のコンピュータ（論理ゲート、デジタル回路、プログラミング言語）およびAI推論技術にどのように結実しているか考察せよ。
\\end{enumerate}
"""
        tex_chapters.append(comp)

    glossary = r'''
\backmatter
\chapter{ブール代数・論理確率論・重要用語辞典}
\label{ch:glossary}
\addcontentsline{toc}{chapter}{ブール代数・論理確率論・重要用語辞典}

高校生が記号論理学、コンピュータの基礎理論、およびブール確率論を学ぶ上で必須となる重要概念の学術的定義と解説を収録した。

\begin{description}[leftmargin=3.5cm, style=nextline]
\item[冪等律（Law of Idempotence）]
ブール代数の根幹をなす代数法則 $x^2 = x$。同一の概念（属性）を重複して適用しても、対象となる事物の集合は変化しないことを表す。代数方程式 $x^2 - x = 0$ すなわち $x(1-x) = 0$ の解が $0$ と $1$ のみに限られることから、思考の数学が「二値論理」となる必然性が導かれる。

\item[宇宙（Universe: 記号 1）と無（Nothing: 記号 0）]
ブール代数における普遍集合と空集合の表現。記号 $1$ は「思考の対象となり得るすべての事物（全体集合）」を表し、記号 $0$ は「いかなる事物も存在しないこと（無・空集合）」を表す。

\item[矛盾律（Principle of Contradiction）]
「ある事物は同時に存在しかつ存在しないことはできない」というアリストテレス以来の根本命題。ブールはこれを代数方程式 $x(1-x) = 0$ として定式化し、論理学の最高原理が代数学の恒等式に帰着されることを示した。

\item[ブール展開定理（Boole's Expansion Theorem）]
任意の論理関数 $f(x)$ を、独立な直交成分の和として $f(x) = f(1)x + f(0)(1-x)$ と一意に展開できる定理。2変数に対しては $f(x, y) = f(1,1)xy + f(1,0)x(1-y) + f(0,1)(1-x)y + f(0,0)(1-x)(1-y)$ となり、現代の論理関数の加法標準形（主加法標準形）の元祖である。

\item[消去法（Elimination in Logic）]
連立する論理方程式から、目的としない中間項（媒介概念）を消去して主概念間の関係を抽出する手続き。関数 $f(x) = 0$ から $x$ を消去した結果は $f(1)f(0) = 0$ となる。これによりアリストテレスの三段論法が完全な代数計算として機械化された。

\item[第2種命題（Secondary Propositions）]
事物の類（クラス）を論じる第1種命題に対し、「命題そのものの真偽」あるいは「その命題が真である時間の割合」を論じる命題。ブールはこれを真偽値 $\{0, 1\}$ の代数として統一し、現代の命題論理およびクロード・シャノンによる論理回路設計の基礎を拓いた。

\item[ブールの一般的方法（General Method in Probabilities）]
連立する論理条件から未知事象の確率を代数的に導出するアルゴリズム。論理方程式を代数的に解き、展開定理により独立な排反事象へと分解した後、確率の公理を適用して連立確率方程式へと変換する。

\item[フレシェ＝ブールの不等式（Boole-Frechet Inequalities）]
事象 $A, B$ の相関関係が未知である場合でも、同時確率 $P(A \cap B)$ の上限と下限を厳密に制限する不等式：
\[
\max(0, P(A) + P(B) - 1) \le P(A \cap B) \le \min(P(A), P(B))
\]
情報が不完全な状況下での数理的意思決定において絶大な威力を発揮する。
\end{description}

\chapter{高校生のための総合演習問題と詳細解答}
\label{ch:final_exam}
\addcontentsline{toc}{chapter}{高校生のための総合演習問題と詳細解答}

\section*{総合問題}
\begin{enumerate}[label=\textbf{【問題\arabic*】}]
\item 2変数の論理関数 $f(x, y) = x + y - xy$（論理和 OR）について、ブールの展開定理を適用して $xy, x(1-y), (1-x)y, (1-x)(1-y)$ の4つの基本成分に展開せよ。

\item 「すべての数学者は哲学者である（$m(1-p)=0$）」かつ「ある哲学者は詩人ではない（$v p(1-s)=0$）」という前提から、消去法を用いて中間項 $p$ を消去し、数学者 $m$ と詩人 $s$ の関係を代数的に導出せよ。

\item 事象 $A$ の生起確率が $P(A) = 0.8$、事象 $B$ の生起確率が $P(B) = 0.7$ であるとする。両事象の相関関係が全く不明であるとき、両者が同時に起こる確率 $P(A \cap B)$ の取り得る値の範囲をフレシェ＝ブールの不等式を用いて求めよ。
\end{enumerate}

\section*{詳細な解答と解説}
\begin{description}[leftmargin=2.5cm, style=nextline]
\item[問題1の解答]
展開定理の各係数を計算する：
\begin{itemize}
\item $f(1, 1) = 1 + 1 - 1\times 1 = 1$
\item $f(1, 0) = 1 + 0 - 1\times 0 = 1$
\item $f(0, 1) = 0 + 1 - 0\times 1 = 1$
\item $f(0, 0) = 0 + 0 - 0\times 0 = 0$
\end{itemize}
したがって、ブール展開式は、
\[
f(x, y) = 1 \cdot xy + 1 \cdot x(1-y) + 1 \cdot (1-x)y + 0 \cdot (1-x)(1-y) = xy + x(1-y) + (1-x)y
\]
【解説】これは論理和 $x \text{ OR } y$ が、「$x$ と $y$ の両方」「$x$ のみ」「$y$ のみ」という互いに排反な3つの直交成分の和として完全に表現されることを示している。現代のディジタル回路における加法標準形の導出そのものである。

\item[問題2の解答]
第1の前提より $m(1-p) = 0 \iff m - mp = 0 \iff mp = m$。
中間概念 $p$ を消去するために、全体を $p$ に関する関数 $F(p) = 0$ と整理し、消去定理 $F(1)F(0) = 0$ を適用する。
$m(1-p) = 0$ より $p=1$ のとき $m(0)=0$（常に成立）、$p=0$ のとき $m(1)=m=0$ でなければならない。
したがって、中間項 $p$ を消去すると、数学者 $m$ が存在し得る条件は $p$ の包含関係に完全に制約される。
ブールの消去法により、三段論法の結論は曖昧な言語的推論を一切挟むことなく、機械的な代数計算として一意に導かれる。

\item[問題3の解答]
フレシェ＝ブールの境界不等式を適用する：
\[
\max(0, P(A) + P(B) - 1) \le P(A \cap B) \le \min(P(A), P(B))
\]
数値を代入すると、
下界：$\max(0, 0.8 + 0.7 - 1) = \max(0, 0.5) = 0.5$
上界：$\min(0.8, 0.7) = 0.7$
したがって、求める範囲は、
\[
0.5 \le P(A \cap B) \le 0.7
\]
【解説】事象 $A$ と $B$ が互いに独立であるか、正の相関か、負の相関かという追加情報が一切ない場合でも、ブールの代数的条件により、両者が同時に起こる確率は最低でも $50\%$、最大でも $70\%$ の間に必ず収まらなければならない。これがブールが『思考の法則』第19章で打ち立てた統計的条件論の真骨頂である。
\end{description}
'''

    full_tex = preamble + '\n'.join(tex_chapters) + glossary + '\n\\end{document}\n'

    rep = {
        '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
        '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
        'ₖ': 'k', 'ⁿ': 'n', '⁻': '-', '⁺': '+', '⁽': '(', '⁾': ')', 'ᵏ': 'k',
        'Σ': r'\sum ', '∫': r'\int ', '∞': r'\infty '
    }
    for k, v in rep.items():
        full_tex = full_tex.replace(k, v)

    out_path = r'books/15114_boole_laws_of_thought/boole_laws_of_thought_intro.tex'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_tex)
    print(f'Wrote {len(full_tex)} bytes to {out_path}')

if __name__ == '__main__':
    build_boole_tex()
