# -*- coding: utf-8 -*-
"""
TikZ Figures and Captions for 12 Chapters of Russell Mathematical Philosophy Intro
"""

FIGS = {
    1: (r"""\begin{tikzpicture}[scale=1.0, >=Stealth]
    % Two impulses
    \draw[thick, fill=purple!10, rounded corners] (-3.5, 0.5) rectangle (-0.5, 3.5);
    \node[font=\bfseries\gtfamily, align=center] at (-2, 2.8) {神秘主義的衝動\\(Mysticism)};
    \node[font=\footnotesize, align=center] at (-2, 1.8) {直観・啓示\\時間の超越\\一者への帰入};
    \draw[thick, fill=blue!10, rounded corners] (0.5, 0.5) rectangle (3.5, 3.5);
    \node[font=\bfseries\gtfamily, align=center] at (2, 2.8) {科学的・論理的衝動\\(Science \& Logic)};
    \node[font=\footnotesize, align=center] at (2, 1.8) {分析・推論\\経験的検証\\多様性の探究};
    % Synthesis
    \draw[->, ultra thick, red!80!black] (-0.5, 2.0) -- (0.5, 2.0);
    \node[draw, thick, fill=yellow!20, rounded corners, align=center, font=\small\bfseries] at (0, -0.8) {ラッセルの理想：\\「情熱（感情）なき科学ではなく、\\批判的論理によって統御された崇高な思索」};
    \draw[->, thick, dashed] (-2, 0.5) |- (0, -0.2);
    \draw[->, thick, dashed] (2, 0.5) |- (0, -0.2);
\end{tikzpicture}""",
    r"ラッセルが説く哲学の二大源泉：「神秘主義的直観」の情熱と「科学的・論理的分析」の批判的精神の緊張と調和。"),

    2: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Logicism pyramid
    \draw[thick, fill=yellow!15] (0, 3.2) -- (2.5, 0) -- (-2.5, 0) -- cycle;
    \node[font=\small\bfseries] at (0, 0.5) {純粋論理学（命題論理・述語論理）};
    \node[font=\footnotesize] at (0, 1.3) {集合・関係・同一性の定義};
    \node[font=\small\bfseries] at (0, 2.1) {算術・自然数論（ペアノの公理）};
    \node[font=\small\bfseries, red!80!black] at (0, 2.8) {解析学・幾何学};
    % Logicism arrow
    \draw[->, ultra thick, blue!80!black] (3.2, 0.2) -- (3.2, 3.0) node[midway, right, font=\footnotesize, align=left] {すべて論理的公理から\\無矛盾に演繹可能\\（論理主義プログラム）};
    % Russell quotation box
    \node[draw, fill=white, rounded corners, font=\scriptsize, align=center] at (0, -1.2) {「数学とは、私たちが何について語っているのかも知らず、\\言っていることが真かどうかも知らない学問である」};
\end{tikzpicture}""",
    r"フレーゲ・ラッセルの「論理主義（Logicism）」の階層ピラミッド。全数学の論理学への還元構造。"),

    3: (r"""\begin{tikzpicture}[scale=1.0, >=Stealth]
    % Barber shop
    \draw[thick, fill=teal!10, rounded corners] (-3,-1) rectangle (3,2.5);
    \node[font=\bfseries\gtfamily] at (0, 2.1) {村の理髪師のパラドックス};
    \node[font=\small, align=center] at (0, 1.2) {「自分で自分の髭を剃らない村人全員の髭を剃り、\\それ以外の者の髭は決して剃らない理髪師」};
    % The question
    \node[draw, fill=red!15, thick, rounded corners, font=\small\bfseries, align=center] at (0, -0.2) {問い：この理髪師は自分の髭を剃るべきか？\\・剃る $\implies$ 剃ってはいけない！\\・剃らない $\implies$ 剃らねばならない！};
    % Conclusion
    \node[font=\footnotesize, red!80!black, align=center] at (0, -1.7) {自己言及による集合論の矛盾：$R = \{x \mid x \notin x\} \implies R \in R \iff R \notin R$};
\end{tikzpicture}""",
    r"ラッセルのパラドックス（理髪師のパラドックス）。素朴集合論の致命的な自己言及の矛盾の視覚化。"),

    4: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Type hierarchy
    \draw[thick, fill=blue!10, rounded corners] (-3, 2.2) rectangle (3, 3.2);
    \node at (0, 2.7) {\textbf{タイプ 2（集合の集合）}：$\{ \{a, b\}, \{c\} \}$};
    \draw[thick, fill=green!10, rounded corners] (-3, 1.0) rectangle (3, 2.0);
    \node at (0, 1.5) {\textbf{タイプ 1（個体の集合）}：$\{a, b, c, \dots\}$};
    \draw[thick, fill=orange!10, rounded corners] (-3, -0.2) rectangle (3, 0.8);
    \node at (0, 0.3) {\textbf{タイプ 0（個体・具体的な要素）}：リンゴ、人間、数字};
    % Arrows
    \draw[->, ultra thick, red] (0, 0.8) -- (0, 1.0) node[midway, right, font=\scriptsize] {元になれる};
    \draw[->, ultra thick, red] (0, 2.0) -- (0, 2.2) node[midway, right, font=\scriptsize] {元になれる};
    \draw[->, ultra thick, purple, dashed] (2.2, 1.7) arc (45:315:0.5) node[right, font=\scriptsize, red] {自己言及（$x \in x$）の絶対禁止！};
    \node[font=\footnotesize, align=center] at (0, -1.1) {型理論（Type Theory）：上位タイプの集合のみが下位タイプを要素に取れる};
\end{tikzpicture}""",
    r"ラッセルが提唱した「階型理論（型理論：Type Theory）」。自己言及を文法的に排除する階層構造。"),

    5: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Zeno's Race
    \draw[->, ultra thick] (0,0) -- (8,0) node[right] {空間（ゴール）};
    \fill[black] (0,0) circle (3pt) node[below=2pt] {アキレス (0)};
    \fill[black] (4,0) circle (3pt) node[below=2pt] {亀 ($x_0$)};
    % Steps
    \draw[->, thick, red] (0,0.5) .. controls (2,1.2) .. (4,0.5) node[midway, above, font=\scriptsize] {第1段階};
    \fill[red] (4,0) circle (2pt);
    \fill[blue] (6,0) circle (2pt) node[below=2pt, font=\scriptsize] {亀 ($x_1$)};
    \draw[->, thick, red] (4,0.5) .. controls (5,1.0) .. (6,0.5) node[midway, above, font=\scriptsize] {第2段階};
    \fill[blue] (7,0) circle (2pt) node[below=2pt, font=\scriptsize] {亀 ($x_2$)};
    % Modern resolution
    \node[align=left, fill=yellow!10, draw=gray!50, rounded corners, font=\footnotesize] at (4, 2.5) {ゼノンの誤謬：無限個の区間があっても、その和は有限時間に収束する！\\$\sum_{n=1}^\infty \left(\frac{1}{2}\right)^n = 1$ （カントール・ワイエルシュトラスによる連続体の解決）};
\end{tikzpicture}""",
    r"ゼノンのパラドックス（アキレスと亀）と、現代解析学・実数連続体による無限和の有限収束の解決。"),

    6: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Two infinite sets
    \draw[thick, fill=blue!5] (-3.5,-0.5) rectangle (3.5, 2.5);
    \node[font=\bfseries\gtfamily] at (0, 2.1) {カントールの濃度の世界（自然数 vs 偶数）};
    % Sets
    \node[anchor=west] at (-3, 1.4) {自然数 $\mathbb{N}$：$1, \quad 2, \quad 3, \quad 4, \quad \dots \quad n$};
    \node[anchor=west] at (-3, 0.4) {偶数 $2\mathbb{N}$：$2, \quad 4, \quad 6, \quad 8, \quad \dots \quad 2n$};
    % 1-to-1 correspondences
    \draw[<->, thick, red] (-2.5, 1.1) -- (-2.5, 0.7) node[midway, left, font=\tiny] {$1:1$};
    \draw[<->, thick, red] (-1.3, 1.1) -- (-1.3, 0.7);
    \draw[<->, thick, red] (-0.1, 1.1) -- (-0.1, 0.7);
    \draw[<->, thick, red] (1.1, 1.1) -- (1.1, 0.7);
    % Conclusion
    \node[font=\footnotesize, align=center] at (0, -1.2) {「無限集合とは、自らの真部分集合と1対1対応がつく集合である」（デデキント・カントール）\\自然数全体の個数と偶数全体の個数は「等しい（可算無限 $\aleph_0$）」！};
\end{tikzpicture}""",
    r"無限集合の本質：全体と部分が対等（1対1対応）となる無限濃度 $\aleph_0$ の数理。"),

    7: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Description theory box
    \draw[thick, fill=orange!10, rounded corners] (-3.5, 0) rectangle (3.5, 3.2);
    \node[font=\bfseries\gtfamily] at (0, 2.7) {「現在のフランス国王は禿頭である」};
    \node[font=\footnotesize, red!80!black] at (0, 2.0) {日常言語の錯覚：主語があるからといって、実在するとは限らない！};
    % Russell's 3 logical propositions
    \draw[thick, fill=white, rounded corners] (-3.2, 0.2) rectangle (3.2, 1.6);
    \node[font=\scriptsize, align=left] at (0, 0.9) {
        ラッセルの論理的分解：\\
        1. 存在：少なくとも1人の $x$ がフランス国王である。\\
        2. 唯一性：高々1人の $x$ がフランス国王である。\\
        3. 属性：その $x$ は禿頭である。 $\implies$ 1が偽なので、文全体は「偽」！
    };
\end{tikzpicture}""",
    r"ラッセルの記述理論（Theory of Descriptions）。日常言語の文法構造を論理記号で厳密に解剖する手法。"),

    8: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Triangle of Knowledge
    \draw[thick, fill=cyan!10] (0, 2.8) -- (-3, 0) -- (3, 0) -- cycle;
    \node[font=\bfseries\gtfamily] at (0, 3.1) {客観的物理世界（太陽・原子・他者の心）};
    \node[font=\small, align=center] at (-2.5, -0.6) {直接親知による知識\\(Acquaintance)\\感覚与格・痛覚・直観};
    \node[font=\small, align=center] at (2.5, -0.6) {記述による知識\\(Description)\\理論的構成・推論・物理法則};
    % Logic bridge
    \draw[<->, ultra thick, red!80!black] (-1.5, 0.8) -- (1.5, 0.8) node[midway, above, font=\scriptsize] {論理的構成（オッカムの剃刀）};
    \node[font=\footnotesize, align=center] at (0, -1.6) {「推論された未知の実体よりも、知覚された経験からの論理的構成物を好め」};
\end{tikzpicture}""",
    r"直接親知（Acquaintance）と記述（Description）の架橋。感覚与格から客観的物理世界を論理的に構成する認識論。"),

    9: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Cause vs Functional relation
    \begin{scope}[xshift=-3.5cm]
        \draw[thick, fill=red!10, rounded corners] (0,0) rectangle (3.2, 2.5);
        \node[font=\bfseries\gtfamily] at (1.6, 2.1) {旧来の「因果律」};
        \node[font=\scriptsize, align=left] at (1.6, 1.0) {・原因 $A$ が結果 $B$ を生む\\・擬人的な強制力（引力等）\\・ア・プリオリな絶対法則\\$\to$ ラッセル「王制の遺物」};
    \end{scope}
    \begin{scope}[xshift=0.5cm]
        \draw[thick, fill=blue!10, rounded corners] (0,0) rectangle (3.2, 2.5);
        \node[font=\bfseries\gtfamily] at (1.6, 2.1) {先進物理学の「微分方程式」};
        \node[font=\scriptsize, align=left] at (1.6, 1.0) {・関数関係 $\dfrac{d^2 x}{dt^2} = f(x, t)$\\・物理量どうしの相関と恒常性\\・過去と未来の数学的対称性\\$\to$ 純粋な数理的関数関係};
    \end{scope}
\end{tikzpicture}""",
    r"ラッセルによる「因果概念の追放」。擬人的な原因・結果の因果律から微分方程式の関数関係への純化。"),

    10: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Mathematical Beauty
    \draw[thick, fill=purple!5, rounded corners] (-3.5,-0.5) rectangle (3.5, 2.5);
    \node[font=\bfseries\gtfamily, purple!80!black] at (0, 2.1) {冷徹で厳格なる数学の美（The Cold Beauty of Mathematics）};
    \node[font=\small, align=center] at (0, 1.0) {「正しく見つめられた数学は、真理だけでなく至高の美を備えている。\\それは彫刻のように冷徹で厳格であり、人間の弱さに迎合せず、\\絵画や音楽のような華麗な罠を持たず、純粋なる崇高さを宿している」};
    \draw[thick, dashed] (-3, 0.1) -- (3, 0.1);
    \node[font=\footnotesize, align=center] at (0, -1.0) {知性の解放：有限な人間の感情を超え、永遠にして普遍なる真理の宮殿へ遊戯する精神};
\end{tikzpicture}""",
    r"ラッセルが讃える「数学の冷徹な美」。感情や世俗の利害を離れた純粋論理の崇高な美学。"),

    11: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Scientific Philosophy vs Dogmatism
    \draw[thick, fill=yellow!10] (-3.5, 0) rectangle (-0.5, 3);
    \node[font=\bfseries\gtfamily, align=center] at (-2, 2.5) {伝統的形而上学\\（独断論）};
    \node[font=\scriptsize, align=left] at (-2, 1.3) {・宇宙全体の包括的一括説明\\・人間の道徳的願望の投影\\・曖昧な日常言語の言いくるめ};
    \draw[thick, fill=cyan!10] (0.5, 0) rectangle (3.5, 3);
    \node[font=\bfseries\gtfamily, align=center] at (2, 2.5) {科学的哲学\\（論理分析哲学）};
    \node[font=\scriptsize, align=left] at (2, 1.3) {・問題を個別・微細に分割\\・数理論理学による精密化\\・仮説の検証可能性と修正};
    \draw[->, ultra thick, red!80!black] (-0.5, 1.5) -- (0.5, 1.5) node[midway, above, font=\scriptsize] {方法論的転換};
\end{tikzpicture}""",
    r"哲学における科学的方法。宇宙全体を一挙に語る大風呂敷の形而上学から、問題を個別に切り分ける論理分析へ。"),

    12: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Modern computer architecture derived from logic
    \draw[thick, fill=green!10, rounded corners] (-3.5, 1.5) rectangle (3.5, 3.0);
    \node[font=\bfseries\gtfamily] at (0, 2.6) {論理主義の遺産：現代の計算機科学と人工知能};
    \node[font=\footnotesize, align=center] at (0, 1.9) {ブール代数 $\to$ フレーゲ・ラッセルの論理式 $\to$ チューリング機械 $\to$ デジタルCPU};
    % Modern AI logic
    \draw[thick, fill=blue!10, rounded corners] (-3.5, -0.5) rectangle (3.5, 1.0);
    \node[font=\bfseries\gtfamily] at (0, 0.6) {型付きプログラミング言語・自動定理証明系};
    \node[font=\footnotesize, align=center] at (0, -0.1) {Haskell, Rust, Lean 4, Coq $\dots$ すべてラッセルの型理論（Type Theory）が直系の祖！};
    \draw[->, ultra thick, red] (0, 1.5) -- (0, 1.0);
\end{tikzpicture}""",
    r"ラッセルの論理哲学から現代のコンピュータ、Rust/Haskell等の型システム、AI自動定理証明（Lean）への系譜。")
}
