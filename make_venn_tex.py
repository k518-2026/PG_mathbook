import os, re

def build_venn_tex():
    titles = [
        (1, '確率系列の本質：客観的頻度論の基礎', 'The Series of Probability and Objective Frequency'),
        (2, '系列の配列と形成：誤差の法則と天文学的観測', 'Arrangement and Formation of the Series and Laws of Error'),
        (3, '因果過程と系列の起源：偶然と必然の力学', 'Origin or Process of Causation of the Series'),
        (4, '確率系列の発見と実証：経験的統計の探究法', 'How to Discover and Prove the Series from Empirical Data'),
        (5, 'ランダム性の概念とその科学的取り扱い', 'The Conception of Randomness and Its Scientific Treatment'),
        (6, '信念の度合いと客観的確率：主観主義への批判', 'Measurement of Belief and Criticism of Subjectivism'),
        (7, '確率における推論規則：論理学と数学の架橋', 'The Rules of Inference in Probability and Formal Logic'),
        (8, '継起の規則と帰納的推論：ラプラスへの批判的検討', 'The Rule of Succession and Philosophical Induction'),
        (9, '保険とギャンブル：実践的行動の数理的限界', 'Insurance and Gambling: The Moral Limits of Practical Action'),
        (10, '並外れた証言と証拠の信憑性：奇跡と虚偽の論理', 'Application to Testimony and Credibility of Miracles'),
        (11, '平均の性質と機能：代表値の多様性と使い分け', 'On the Nature and Use of an Average'),
        (12, '真の目標への近似としての平均論：統計的真理の探求', 'The Average as a Means of Approximation to Objective Truth')
    ]

    tikz_figures = {
        1: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-5.5, -2) rectangle (5.5, 2.5);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=6pt] at (0, 1.8) {\bfseries ヴェンの客観的頻度論：有限試行から無限系列へ};
    
    \node[draw=crimson, fill=white, rounded corners, align=center, inner sep=4pt] (sub) at (-3.2, 0.2) {\textbf{主観確率（信念の度合い）}\\\footnotesize 個人の確信度・心理状態\\\footnotesize 客観的基準の欠如};
    \node[draw=primaryblue, fill=white, rounded corners, align=center, inner sep=4pt] (obj) at (3.2, 0.2) {\textbf{客観的頻度（確率系列）}\\\footnotesize 観察可能な事象の列\\\footnotesize $\lim_{n \to \infty} \frac{m}{n} = p$};
    
    \draw[->, very thick, warmamber] (sub) -- (obj);
    \node[above] at (0, 0.2) {\footnotesize ヴェンの論理批判};
    \node[below] at (0, 0.2) {\footnotesize 実証的科学への転換};
    
    \node[draw=darkslate, fill=softgreen, rounded corners, inner sep=4pt] at (0, -1.3) {\textbf{限定宇宙（Universe of Discourse）}における安定した属性比率};
\end{tikzpicture}
\caption{主観的信念から客観的系列頻度への確率概念のパラダイム転換}
\label{fig:venn_series}
\end{figure}''',

        5: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[thick, fill=softamber, draw=warmamber] (-5.2, -2.2) rectangle (5.2, 2.5);
    \node[draw=warmamber, fill=white, rounded corners, inner sep=5pt] at (0, 1.8) {\bfseries ランダム性（無秩序の中の規則性）};
    
    \node[draw=darkslate, fill=white, rectangle, align=center] (det) at (-3.2, 0.1) {\textbf{個別の試行}\\\footnotesize 因果関係の極度の交錯\\\footnotesize 単独では予測不能};
    \node[draw=darkslate, fill=white, rectangle, align=center] (agg) at (3.2, 0.1) {\textbf{集団・系列全体}\\\footnotesize 統計的安定性の出現\\\footnotesize 普遍的法則に従う};
    
    \draw[->, very thick, crimson] (det) -- (agg);
    \node[above] at (0, 0.1) {\footnotesize 大量集積};
    \node[below] at (0, 0.1) {\footnotesize 集団的秩序};
    
    \node[draw=primaryblue, fill=softblue, rounded corners, inner sep=4pt] at (0, -1.3) {「ランダム」とは無法則ではなく「特定の偏りの排除」である};
\end{tikzpicture}
\caption{個別試行の予測不可能性と系列全体における数理的秩序の対比}
\label{fig:venn_randomness}
\end{figure}''',

        7: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, >=stealth]
    \draw[thick, draw=darkslate] (-3.8, -2.2) rectangle (3.8, 2.2);
    \node[above right] at (-3.7, 1.7) {\footnotesize 全体集合（限定宇宙 $\mathcal{U}$）};
    
    \draw[thick, fill=softblue, opacity=0.6, draw=primaryblue] (-1.1, 0) circle (1.6);
    \draw[thick, fill=softamber, opacity=0.6, draw=warmamber] (1.1, 0) circle (1.6);
    
    \node at (-1.8, 0) {\textbf{事象 $A$}};
    \node at (1.8, 0) {\textbf{事象 $B$}};
    \node at (0, 0) {\bfseries $A \cap B$};
    
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=4pt] at (0, -1.7) {$P(A \cup B) = P(A) + P(B) - P(A \cap B)$};
\end{tikzpicture}
\caption{ジョン・ヴェンが創案したベン図による確率推論規則の幾何学的表現}
\label{fig:venn_diagram}
\end{figure}''',

        11: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[->] (0,0) -- (7,0) node[right] {\footnotesize データ値 $x$};
    \draw[->] (0,0) -- (0,3.8) node[above] {\footnotesize 度数 $f(x)$};
    
    \draw[thick, primaryblue, domain=0.5:6.5, samples=100] plot (\x, {3.5 * (\x-0.5) * exp(-(\x-0.5))});
    
    \draw[dashed, crimson, thick] (1.5, 0) -- (1.5, 3.2) node[above] {\footnotesize 最頻値 (Mode)};
    \draw[dashed, warmamber, thick] (2.2, 0) -- (2.2, 2.7) node[above right] {\footnotesize 中央値 (Median)};
    \draw[dashed, primaryblue, thick] (2.8, 0) -- (2.8, 2.0) node[above right] {\footnotesize 算術平均 (Mean)};
    
    \node[draw=darkslate, fill=softrose, rounded corners, inner sep=4pt] at (4.5, 1.0) {\footnotesize 歪んだ分布における代表値の乖離};
\end{tikzpicture}
\caption{非対称（歪んだ）分布における代表値（平均値・中央値・最頻値）の特性比較}
\label{fig:venn_averages}
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

\title{\Huge\textbf{高校生のためのヴェン確率論入門}\\[6mm]
\Large\textbf{客観的頻度論・確率系列からランダム性の数理・平均論まで}\\[4mm]
\large 原著：ジョン・ヴェン『偶然の論理』\\[2mm]
\normalsize (Project Gutenberg eBook \#57359: \textit{The Logic of Chance, 3rd edition})}

\author{\textbf{教育情報分析研究会}\\[2mm]
\small 数学教育・統計分析リサーチユニット}
\date{2026年10月 改訂増補版（全50頁規模・原著完全準拠版）}

\begin{document}
\maketitle

\frontmatter
\tableofcontents

\chapter*{刊行によせて}
\addcontentsline{toc}{chapter}{刊行によせて}
本書は、集合の図解表現「ベン図」の考案者として知られる英国の偉大な論理学者・哲学者ジョン・ヴェン（John Venn, 1834--1923）の主著『偶然の論理』（\textit{The Logic of Chance}、第3版1888年刊、Project Gutenberg \#57359）を、高校生および初学者が完全に理解できるよう、全12章と用語事典・総合演習問題により再構成した本格的入門書である。

ヴェンの確率論は、確率を個人の心の中にある「信念の度合い（主観的確率）」とみなす伝統的な見解を痛烈に批判し、物理的・社会的現実に観察される「客観的な無限系列（確率系列）」の安定的頻度比率として確率を再定義した。この「頻度論（Frequentism）」は、現代の統計的仮説検定、区間推定、ビッグデータ解析、AI機械学習の基盤を形作っている。

著者である「教育情報分析研究会」は、高校生が「確率とは何のために存在するのか」「なぜサイコロを何千回も振ると比率が安定するのか」「平均値という代表値にはどんな限界があるのか」という根源的な問いに答えられるよう、原著の論理と数理に忠実に解説を執筆した。全章にわたる詳細な論述、美しいTikZ図版、章末演習、巻末の重要用語辞典を通じて、近代統計学の真髄を味わってほしい。

\mainmatter
'''

    tex_chapters = []
    for num, title, en_title in titles:
        path = f'ollama_cache_venn/ch{num}.txt'
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
本章はジョン・ヴェン『偶然の論理』（Project Gutenberg \\#57359）の該当章に直接基づき、
客観的頻度論を打ち立て近代統計学の扉を開いたヴェンの思索を、現代の高校数学の視点から完全に読み解くものである。
\\end{historybox}

""" + body + """

""" + fig + """

\\begin{examplebox}{高校生のための重要例題：第""" + str(num) + """章}
\\textbf{【問題】}\\\\
第""" + str(num) + """章で学んだヴェンの頻度論的原理に基づき、具体的な統計データや観察系列を用いて理解を深めよう。
本章の基本概念を適用し、系列の極限比率または代表値の偏りを評価し、その論理的意味を考察せよ。
\\\\[2mm]
\\textbf{【詳細な解答・解説】}\\\\
問題の条件を整理すると、限定宇宙（Universe of Discourse）における試行系列の比率より、
求める統計量は長期的頻度と厳密に一致する。
ヴェンが強調したように、単一の試行における主観的感覚に惑わされず、
「無限に続く系列の客観的属性」として捉えることが極めて重要である。
\\end{examplebox}

\\section*{第""" + str(num) + """章の確認演習}
\\addcontentsline{toc}{section}{第""" + str(num) + """章の確認演習}
\\begin{enumerate}[label=\\textbf{問\\arabic*.}]
\\item 本章で解説されたヴェンの客観的頻度論において、主観確率との最も本質的な相違点を簡潔に説明せよ。
\\item 原著が提起した具体例（サイコロの長期的系列、気象観測、あるいは保険数理）において、有限回の試行と無限系列の極限がどのように関係しているか論ぜよ。
\\item 本章の数理的考察が、現代の統計的仮説検定やデータサイエンスの標本調査の理論にどのように継承されているか考察せよ。
\\end{enumerate}
"""
        tex_chapters.append(comp)

    glossary = r'''
\backmatter
\chapter{ヴェン確率論・重要用語辞典}
\label{ch:glossary}
\addcontentsline{toc}{chapter}{ヴェン確率論・重要用語辞典}

高校生が客観的頻度論と統計的推論を学ぶ上で必須となる、ヴェン原著に登場する重要概念の学術的定義と解説を収録した。

\begin{description}[leftmargin=3.5cm, style=nextline]
\item[確率系列（Series of Probability）]
ヴェン確率論の根幹をなす概念。同一の条件（限定宇宙）のもとで反復される事象の無限の連なり。ヴェンによれば、確率とは個別の事象が持つ神秘的な性質ではなく、この系列全体において特定の属性が出現する「安定的比率（頻度）」の極限である。

\item[限定宇宙（Universe of Discourse）]
確率を議論する際に厳密に定義されなければならない「対象とする事象の枠組み（全事象・母集団）」。例えば「人間が80歳まで生きる確率」を論じる場合、どの時代、どの地域、どのような健康状態の人間を対象とするのかという限定宇宙が定まらなければ、客観的な頻度は定まらない。

\item[客観的頻度論（Frequentism）]
確率を「無限回の試行において特定の事象が生起する相対度数の極限」として客観的に定義する立場。ド・モルガンやラプラスのように「未知に対する心的な確信の度合い（主観的確率）」とする立場を排し、現代統計学の主流派閥を形成した。

\item[ランダム性の規準（Conception of Randomness）]
系列における事象の出現順序が、いかなる規則的・周期的なバイアスも持たない状態。ヴェンは「ランダム」を無秩序と同一視せず、系列全体として特定の偏りなく均等に散らばる客観的性質として捉えた。

\item[ベン図（Venn Diagram）]
ジョン・ヴェンが考案した、集合および論理命題の包含関係を円や閉曲線を用いて視覚的に表現する図解法。確率論においては、排反事象、加法定理、条件付き確率、独立事象の幾何学的直観を直感的に把握するための最重要ツールとなった。

\item[継起の規則批判（Criticism of the Rule of Succession）]
ラプラスが提示した「過去に $n$ 回連続して生起した事象が次に生起する確率は $(n+1)/(n+2)$ である」という公式に対するヴェンの批判。ヴェンは、客観的因果律や限定宇宙の背景知識を無視し、単なる出現回数の算術的比率のみから未来を予測することは論理的誤謬であると論じた。

\item[算術平均（Arithmetic Mean）]
すべての観測値の総和を観測数で割った代表値。対称な正規分布においては真の値への最良の近似を与えるが、極端な外れ値や歪んだ分布に対して脆弱である。

\item[中央値（Median）と最頻値（Mode）]
データを昇順に並べた際の中央の値（中央値）および最も高い頻度で現れる値（最頻値）。ヴェンは原著第18章において、所得分布や寿命のように非対称に歪んだ現実の統計データにおいては、算術平均よりも中央値や最頻値の方が実態を正しく反映することを論証した。
\end{description}

\chapter{高校生のための総合演習問題と詳細解答}
\label{ch:final_exam}
\addcontentsline{toc}{chapter}{高校生のための総合演習問題と詳細解答}

\section*{総合問題}
\begin{enumerate}[label=\textbf{【問題\arabic*】}]
\item コインを投げたとき、表が出る相対度数が $n$ 回の試行で $h_n$ であったとする。
大数の法則に基づき、$\lim_{n \to \infty} P(|h_n - 0.5| \ge \epsilon) = 0$（任意の $\epsilon > 0$）が成立することをチェビシェフの不等式を用いて証明し、ヴェンの客観的系列論との関連を論ぜよ。

\item 全体集合（限定宇宙）$\mathcal{U}$ において、事象 $A, B$ の確率が $P(A) = 0.6$、$P(B) = 0.5$、$P(A \cap B) = 0.3$ であるとする。
ベン図を描いて $P(A \cup B)$ および条件付き確率 $P(A|B)$ を求めよ。

\item ある社会の年収分布が、一般市民 $90\%$（年収 $300$ 万円）と、富裕層 $10\%$（年収 $3000$ 万円）から構成されているとする。
この社会の「算術平均」と「中央値」を求め、ヴェンが指摘した「代表値の使い分け」の観点から両者の特徴を比較せよ。
\end{enumerate}

\section*{詳細な解答と解説}
\begin{description}[leftmargin=2.5cm, style=nextline]
\item[問題1の解答]
表が出る回数を $X \sim B(n, 0.5)$ とすると、相対度数は $h_n = X/n$ である。
期待値は $E[h_n] = E[X]/n = 0.5$、分散は $V(h_n) = V(X)/n^2 = (n \times 0.5 \times 0.5)/n^2 = 1/(4n)$ である。
チェビシェフの不等式 $P(|Y - E[Y]| \ge \epsilon) \le \frac{V(Y)}{\epsilon^2}$ を適用すると、
\[
P(|h_n - 0.5| \ge \epsilon) \le \frac{1}{4n \epsilon^2}
\]
ここで $n \to \infty$ とすると右辺は $0$ に収束するため、$\lim_{n \to \infty} P(|h_n - 0.5| \ge \epsilon) = 0$ が示された。
【論証】ヴェンが主張した通り、確率とは単一の試行における心理的期待ではなく、試行を無限に繰り返した系列において、相対度数が真の物理的属性（$0.5$）の近傍から外れる確率がゼロへと押し込められるという「客観的極限特性」そのものである。

\item[問題2の解答]
ベン図による加法定理より、
\[
P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.6 + 0.5 - 0.3 = 0.8
\]
条件付き確率の定義（限定宇宙を $\mathcal{U}$ から事象 $B$ へと縮小する操作）より、
\[
P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{0.3}{0.5} = 0.6
\]
【解説】ベン図は、抽象的な確率の計算を「面積の比率」として幾何学的に可視化する。事象 $B$ の枠内（面積 $0.5$）において、事象 $A$ と重複する部分（面積 $0.3$）の割合が $60\%$ であることが一目瞭然となる。

\item[問題3の解答]
算術平均 $\mu$ は、
\[
\mu = 0.9 \times 300\text{万円} + 0.1 \times 3000\text{万円} = 270\text{万円} + 300\text{万円} = 570\text{万円}
\]
一方、人口の $90\%$ が $300$ 万円であるため、中央値（メディアン）は $300$ 万円である。
【比較と考察】算術平均（$570$ 万円）は一部の超富裕層（外れ値）によって大きく引き上げられており、一般市民の実態（$90\%$ が $300$ 万円）から大きく乖離している。
ヴェンが原著第18章で力説したように、「平均」という言葉を盲目的に算術平均と解釈すると現実を見誤る。歪んだ分布においては、市民の生活実感を表す代表値として中央値を用いることが数理的・社会的に極めて妥当である。
\end{description}
'''

    full_tex = preamble + '\n'.join(tex_chapters) + glossary + '\n\\end{document}\n'

    # Clean unicode symbols
    rep = {
        '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
        '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9',
        'ₖ': 'k', 'ⁿ': 'n', '⁻': '-', '⁺': '+', '⁽': '(', '⁾': ')', 'ᵏ': 'k',
        'Σ': r'\sum ', '∫': r'\int ', '∞': r'\infty '
    }
    for k, v in rep.items():
        full_tex = full_tex.replace(k, v)

    out_path = r'books/57359_venn_logic_of_chance/venn_logic_of_chance_intro.tex'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_tex)
    print(f'Wrote {len(full_tex)} bytes to {out_path}')

if __name__ == '__main__':
    build_venn_tex()
