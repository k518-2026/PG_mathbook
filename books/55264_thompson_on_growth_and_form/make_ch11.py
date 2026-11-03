# -*- coding: utf-8 -*-
"""
Build Chapter 11 (The Logarithmic Spiral) translation
"""

ch11_content = r"""\chapter{対数螺旋 (The Logarithmic Spiral)}

\section{成長の幾何学と螺旋の分類}

自然界において、有機的成長が描き出す最も普遍的かつ魅力的な幾何学曲線が**螺旋（Spiral）**である。螺旋はアメーバの仮足の旋回から、ヒマワリの種子の配列、巻き貝やオウムガイの殻、さらには雄羊の角や銀河の腕に至るまで、あらゆるスケールにおいて観察される。

しかし、幾何学において「螺旋」と呼ばれる曲線には、本質的に異なる力学的・幾何学的性質を持つ二大分類が存在する：

\subsection{1. アルキメデス螺旋 (Archimedean Spiral)}
アルキメデス螺旋の方程式は、極座標 $(r, \theta)$ において、
\begin{equation}
    r = a + b\theta
\end{equation}
で表される。動径 $r$ は回転角 $\theta$ に正比例して一様に増加するため、隣り合う渦のピッチ（間隔）は常に一定（$2\pi b$）である。これは、一様な厚みのロープや絨毯を一定速度で巻き取ったときの断面に現れる曲線である。
アルキメデス螺旋は「一様な蓄積」を反映するが、全体としての相似比は渦を巻くごとに変化し、自己相似性は持たない。

\subsection{2. 対数螺旋 (Logarithmic Spiral / Equiangular Spiral)}
対数螺旋の方程式は、
\begin{equation}
    r = a e^{b\theta} \quad \text{あるいは} \quad \log\left(\frac{r}{a}\right) = b\theta
\end{equation}
で表される。この曲線において、動径ベクトルと各点における接線とのなす角 $\alpha$（挟角）は、$\cot \alpha = b$ により、**曲線のいかなる点においても完全に一定**である。このためルネ・デカルトやヤコブ・ベルヌーイはこの曲線を**「等角螺旋（Spira mirabilis / 驚異の螺旋）」**と呼んだ。

\section{殻の幾何学的相似成長 --- グノモン的成長の原理}

なぜ軟体動物の殻（オウムガイやアンモナイト、巻き貝）は、例外なく対数螺旋を形成するのか？

動物の軟組織（筋肉や内臓）は三次元的に等方的に拡大成長することができるが、炭酸カルシウムを主成分とする硬い殻（貝殻）は、一度分泌されて固化すると、内部から自律的に変形したり膨張したりすることができない。成長は常に**「開口部の外縁に新たな分泌物を付加（Accretionary Growth）すること」**によってのみ行われる。

古い殻を脱ぎ捨てることなく、開口部の一端に新しい部屋（房）を次々と付け足しながら、全体として**「まったく同一の幾何学的プロポーション（相似形）を永遠に保ち続ける」**ための幾何学的必要十分条件は、その成長軌跡が対数螺旋を描くことである。

古代ギリシャの幾何学者ヘロンは、ある図形に付加したとき、元の図形と全く相似な図形を生み出す図形を**「グノモン（Gnomon）」**と呼んだ。対数螺旋における成長とは、まさに連続的なグノモンの付加（Gnomonic Growth）そのものなのである。

\begin{figure}[htbp]
    \centering
    \ifdefined\figplaceholder
    \else
    \includegraphics[width=0.65\textwidth]{images/i500.png}
    \fi
    \caption{オウムガイ（\textit{Nautilus pompilius}）の隔壁切断面と等角螺旋}
    \label{fig:nautilus}
\end{figure}

オウムガイの殻を二等分した断面を観察すると、内部は湾曲した美しい隔壁（Septa）によって多数の気室に仕切られている（図\ref{fig:nautilus}）。動物体本体は常に最新の最も広い外室に居住し、過去に生活していた古い部屋は気体で満たされ、海中での浮力調整タンクとして機能する。各気室の体積比、隔壁の曲率半径、開口部の角度比は、殻のどの成長段階においても完璧な幾何学的等比数列を成している。
"""

with open(r"E:\GoogleAntigravity\PG_mathbook\books\55264_thompson_on_growth_and_form\ch11_logarithmic_spiral.tex", "w", encoding="utf-8") as f:
    f.write(ch11_content)

print("Chapter 11 TeX written successfully.")
