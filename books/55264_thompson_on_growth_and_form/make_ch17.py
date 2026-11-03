# -*- coding: utf-8 -*-
"""
Build Chapter 17 (On the Theory of Transformations) translation
"""

ch17_content = r"""\chapter{変形の理論、あるいは近縁形態の比較 (On the Theory of Transformations)}

\section{比較解剖学と幾何学的変換}

比較解剖学において、生物学者たちは無数の生物種の骨格や形態を比較し、共通の祖先からの進化や適応放散を論じてきた。しかし、彼らが用いる比較の手法は、個々の骨や突起の名称を対応づける「部位ごとの相同性（Homology）」の記述にとどまり、有機体全体の輪郭がいかにして包括的に変化したかという**形態の幾何学的連続性**を定量的に扱うことは極めて稀であった。

これに対し、アルブレヒト・デューラーが1528年の『人身均衡四書（Vier Bücher von menschlicher Proportion）』において試みたように、格子（グリッド）を伸縮・剪断・歪曲させることによって人体の多様なプロポーションを体系的に変形描画した先駆的手法が存在する。

われわれはこのデューラーの直観を近代幾何学の厳密な数学的枠組みへと拡張する。すなわち、ある生物の標準的な形態を二次元（あるいは三次元）のデカルト直交座標系 $(x, y)$ の上に描き、近縁な別の生物種の形態を、その座標格子全体を連続的に歪めた新しい座標系 $(x', y')$ への**幾何学的写像（Transformation / Mapping）**として表現するのである：
\begin{align}
    x' &= f(x, y) \\
    y' &= g(x, y)
\end{align}

\section{魚類の形態変換}

この座標変換理論の最も鮮やかな実例は、海洋魚類の骨格および外形の比較において観察される。

\begin{figure}[htbp]
    \centering
    \ifdefined\figplaceholder
    \else
    \begin{minipage}{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{images/i729a.png}
        \caption{直交座標系における \textit{Diodon}（ハリセンボン科）}
        \label{fig:diodon}
    \end{minipage}
    \hfill
    \begin{minipage}{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{images/i729b.png}
        \caption{同心円・放射状変形座標における \textit{Orthagoriscus}（マンボウ）}
        \label{fig:orthagoriscus}
    \end{minipage}
    \fi
\end{figure}

図\ref{fig:diodon}に示すように、ハリセンボン科の魚（\textit{Diodon}）の輪郭と骨格を正方形の直交等間隔グリッドの上に描く。ここで水平軸を後方に向かって急速に短縮・湾曲させ、垂直軸を同心円弧状に変形させた新しい格子（図\ref{fig:orthagoriscus}）に元の魚の各点を写像すると、驚くべきことに、形態が極端に特異なマンボウ（\textit{Orthagoriscus mola} / \textit{Mola mola}）の骨格と外形が、背鰭や臀鰭の配置に至るまで寸分の狂いもなく現出する。

同様に、淡水魚のブリーム（\textit{Abramis}）の直交格子を斜めに剪断（Shearing Transformation）させると、別の近縁種である \textit{Polyprion} や \textit{Pseudopriacanthus} の形態へと連続的に移行する。

\begin{figure}[htbp]
    \centering
    \ifdefined\figplaceholder
    \else
    \includegraphics[width=0.85\textwidth]{images/i735.png}
    \fi
    \caption{頭足類・甲殻類における連続的座標変換の展開}
    \label{fig:carapace_transform}
\end{figure}

\section{形態形成における力場と進化の連続性}

この幾何学的写像の成功は、進化生物学に対して極めて重大な哲学的含意を持つ。

もし生物の進化が、ダーウィニズムの極端な解釈が主張するように「無数の独立した微小変異（遺伝子の偶発的変異）が各器官において個別に生じ、それぞれが独立に自然淘汰された結果」であるならば、魚の口、眼、背鰭、脊椎、尾鰭の各部が示す変化はバラバラで無秩序なものになるはずである。

しかし実際には、生物の全身のすべての器官が、**「個体全体を包摂する単一の滑らかな力学的歪み関数」**に従って調和的に協調して変形している。これは、成長の過程において生物組織に作用する物理的な力場（機械的張力、成長因子の濃度勾配、流動場の勾配テンソル）が、有機体全体を一括して統括・再編成していることを雄弁に物語っている。

変形の理論は、形態の多様性が無秩序な偶然の産物ではなく、幾何学と物理法則の拘束条件のもとで秩序正しく調和した**「連続的力学系の固有モードの遷移」**であることを示しているのである。
"""

with open(r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\ch17_transformations.tex", "w", encoding="utf-8") as f:
    f.write(ch17_content)

print("Chapter 17 TeX written successfully.")
