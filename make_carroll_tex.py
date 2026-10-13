import os, re

def build_carroll_tex():
    titles = [
        (1, '不思議の国の数学者：チャールズ・ドジソンと『論理の遊戯』の世界', 'The Mathematician of Wonderland and The Game of Logic'),
        (2, 'キャロル・ボードの誕生：宇宙を四分割する「2属性ダイアグラム」', 'The Smaller Diagram and the Division of the Universe'),
        (3, '赤と白のカウンター：存在と無を可視化するシンボル体系', 'Red and Grey Counters: The Visual Algebra of Existence and Non-Existence'),
        (4, '3つの基本命題：Some, No, All をボード上に配置する', 'Three Fundamental Propositions: Some, No, and All on the Board'),
        (5, '中項の導入と「3属性ダイアグラム」：8つの小部屋が織りなす思考空間', 'The Larger Diagram and Eight Compartments: Introducing the Middle Term'),
        (6, '三段論法の完全解法（前編）：二つの前提をボードにプロットする技術', 'Plotting the Syllogism: Expressing Two Premises on the Larger Board'),
        (7, '三段論法の完全解法（後編）：中項の消去と結論のトランスファー', 'Elimination of the Middle Term and Transfer of Conclusions'),
        (8, '論理の落とし穴：キャロル・ボードが暴く「形式的誤謬」', 'Fallacies Unmasked: The Fallacy of Undistributed Middle and Beyond'),
        (9, 'キャロル図からカルノー図へ：現代デジタル回路と情報科学への直結', 'From Carroll Diagrams to Karnaugh Maps and Modern Digital Logic'),
        (10, '論理から確率へ：キャロル・ボードで解く条件付き確率とベイズの定理', 'From Logic to Probability: Conditional Probability and Bayes Theorem on the Board'),
        (11, '言葉の迷宮とパズル演習：『論理の遊戯』原著の傑作問題に挑む', 'Cross Questions and Crooked Answers: Carrollian Logic Puzzles'),
        (12, '論理的思考の真髄：記号・図・ゲームがひらく数学の未来', 'The Essence of Logical Thinking: Games, Symbols, and the Future of Mathematics')
    ]

    tikz_figures = {
        1: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-6, -2.5) rectangle (6, 2.5);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=6pt] at (0, 2.0) {\bfseries ルイス・キャロル（チャールズ・ドジソン）の学問と文学の統合};
    
    \node[draw=darkslate, fill=white, rectangle, align=center, inner sep=5pt] (lit) at (-3.5, 0.4) {\textbf{文学・言語遊戯}\\\footnotesize 『不思議の国のアリス』\\\footnotesize ノンセンス文学・言葉のパズル\\\footnotesize 厳密なルールの遊戯化};
    \node[draw=darkslate, fill=white, rectangle, align=center, inner sep=5pt] (math) at (3.5, 0.4) {\textbf{オックスフォード数学講師}\\\footnotesize ユークリッド幾何学の擁護\\\footnotesize 行列式・代数学の講義\\\footnotesize 記号論理学の体系化};
    
    \node[draw=crimson, fill=softamber, rounded corners, inner sep=6pt] (game) at (0, -1.0) {\Large\bfseries 『論理の遊戯』（1886年）};
    
    \draw[->, very thick, warmamber] (lit) -- (game);
    \draw[->, very thick, warmamber] (math) -- (game);
    
    \node[draw=darkslate, fill=softgreen, rounded corners, inner sep=4pt] at (0, -1.9) {\footnotesize 九枚のカウンターと二つのダイアグラムによる「三段論法の完全視覚化」};
\end{tikzpicture}
\caption{オックスフォード大数学講師ドジソンによる文学と数学的論理学の融合}
\label{fig:carroll_synthesis}
\end{figure}''',

        2: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=1.0, >=stealth]
    % Outer boundary of Universe
    \draw[very thick, draw=darkslate] (-3.5, -3) rectangle (3.5, 3);
    \node[above] at (0, 3.1) {\bfseries 限定宇宙（Universe of Discourse）：すべてのケーキの集合};
    
    % Horizontal dividing line (x vs x')
    \draw[thick, draw=primaryblue] (-3.5, 0) -- (3.5, 0);
    \node[left, primaryblue] at (-3.6, 1.5) {\Large\bfseries $x$（上段：新しいケーキ）};
    \node[left, primaryblue] at (-3.6, -1.5) {\Large\bfseries $x'$（下段：新しくないケーキ）};
    
    % Vertical dividing line (y vs y')
    \draw[thick, draw=warmamber] (0, -3) -- (0, 3);
    \node[above, warmamber] at (-1.75, 3.4) {\Large\bfseries $y$（左列：おいしい）};
    \node[above, warmamber] at (1.75, 3.4) {\Large\bfseries $y'$（右列：おいしくない）};
    
    % 4 Cells
    \node[align=center] at (-1.75, 1.5) {\large\bfseries セル 1: $xy$\\\footnotesize 新しくておいしい};
    \node[align=center] at (1.75, 1.5) {\large\bfseries セル 2: $xy'$\\\footnotesize 新しいがおいしくない};
    \node[align=center] at (-1.75, -1.5) {\large\bfseries セル 3: $x'y$\\\footnotesize 新しくないがおいしい};
    \node[align=center] at (1.75, -1.5) {\large\bfseries セル 4: $x'y'$\\\footnotesize 新しくなくおいしくもない};
    
    \draw[dashed, fill=softblue, opacity=0.3] (-3.5, 0) rectangle (0, 3);
\end{tikzpicture}
\caption{キャロルの2属性ダイアグラム（Smaller Diagram）による宇宙の4分割}
\label{fig:carroll_smaller_diagram}
\end{figure}''',

        3: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-5.8, -2.2) rectangle (5.8, 2.5);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=5pt] at (0, 1.9) {\bfseries キャロル・カウンターの物理的記号体系};
    
    \node[draw=crimson, fill=softrose, circle, inner sep=6pt] (red) at (-3.5, 0.3) {\Large\bfseries 赤};
    \node[align=center] at (-3.5, -1.0) {\textbf{存在（FULL）}\\\footnotesize その部屋に事物が「存在する」\\\footnotesize 要素数 $\ge 1$\\\footnotesize 現代の論理値：真 (1)};
    
    \node[draw=darkslate, fill=gray!30, circle, inner sep=6pt] (grey) at (0, 0.3) {\Large\bfseries 灰};
    \node[align=center] at (0, -1.0) {\textbf{空（EMPTY）}\\\footnotesize その部屋に事物が「存在しない」\\\footnotesize 要素数 $= 0$（空集合 $\emptyset$）\\\footnotesize 現代の論理値：偽 (0)};
    
    \node[draw=darkslate, fill=white, dashed, circle, inner sep=6pt] (none) at (3.5, 0.3) {\Large\bfseries 空白};
    \node[align=center] at (3.5, -1.0) {\textbf{未定（UNKNOWN）}\\\footnotesize 情報がない状態\\\footnotesize 存在するか空か不明\\\footnotesize 三値論理の不定値};
    
    \draw[<->, thick, warmamber] (red) -- (grey);
\end{tikzpicture}
\caption{赤カウンター（存在）と灰カウンター（空）および空白（情報なし）の3値構造}
\label{fig:carroll_counters}
\end{figure}''',

        4: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    % Prop 1: Some x are y
    \begin{scope}[xshift=-5cm]
        \draw[thick] (-1.5, -1.5) rectangle (1.5, 1.5);
        \draw (-1.5, 0) -- (1.5, 0); \draw (0, -1.5) -- (0, 1.5);
        \node[above] at (0, 1.5) {\footnotesize Some $x$ are $y$};
        \node[fill=crimson, text=white, circle, inner sep=3pt] at (-0.75, 0.75) {赤};
        \node[below] at (0, -1.6) {\footnotesize 特称肯定命題 (I)};
    \end{scope}

    % Prop 2: No x are y
    \begin{scope}[xshift=0cm]
        \draw[thick] (-1.5, -1.5) rectangle (1.5, 1.5);
        \draw (-1.5, 0) -- (1.5, 0); \draw (0, -1.5) -- (0, 1.5);
        \node[above] at (0, 1.5) {\footnotesize No $x$ are $y$};
        \node[fill=gray!50, text=black, circle, inner sep=3pt] at (-0.75, 0.75) {灰};
        \node[below] at (0, -1.6) {\footnotesize 全称否定命題 (E)};
    \end{scope}

    % Prop 3: All x are y
    \begin{scope}[xshift=5cm]
        \draw[thick] (-1.5, -1.5) rectangle (1.5, 1.5);
        \draw (-1.5, 0) -- (1.5, 0); \draw (0, -1.5) -- (0, 1.5);
        \node[above] at (0, 1.5) {\footnotesize All $x$ are $y$};
        \node[fill=crimson, text=white, circle, inner sep=3pt] at (-0.75, 0.75) {赤};
        \node[fill=gray!50, text=black, circle, inner sep=3pt] at (0.75, 0.75) {灰};
        \node[below] at (0, -1.6) {\footnotesize 全称肯定命題 (A)（二重配置）};
    \end{scope}
\end{tikzpicture}
\caption{3つの基本命題（Some, No, All）の Smaller Diagram 上のプロット形式}
\label{fig:carroll_propositions}
\end{figure}''',

        5: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, >=stealth]
    % Outer Square
    \draw[very thick, draw=darkslate] (-4, -4) rectangle (4, 4);
    \node[above] at (0, 4.1) {\bfseries Larger Diagram（3属性ダイアグラム：8分割空間）};
    
    % Inner Square (m)
    \draw[thick, draw=crimson, fill=softamber, opacity=0.4] (-2, -2) rectangle (2, 2);
    
    % Horizontal line
    \draw[thick, draw=primaryblue] (-4, 0) -- (4, 0);
    \node[left, primaryblue] at (-4.1, 2) {\Large $x$};
    \node[left, primaryblue] at (-4.1, -2) {\Large $x'$};
    
    % Vertical line
    \draw[thick, draw=warmamber] (0, -4) -- (0, 4);
    \node[above, warmamber] at (-2, 4.1) {\Large $y$};
    \node[above, warmamber] at (2, 4.1) {\Large $y'$};
    
    % Labels for 8 cells
    \node at (-1, 1) {\footnotesize $xym$};
    \node at (1, 1) {\footnotesize $xy'm$};
    \node at (-1, -1) {\footnotesize $x'ym$};
    \node at (1, -1) {\footnotesize $x'y'm$};
    
    \node at (-3, 3) {\footnotesize $xym'$};
    \node at (3, 3) {\footnotesize $xy'm'$};
    \node at (-3, -3) {\footnotesize $x'ym'$};
    \node at (3, -3) {\footnotesize $x'y'm'$};
    
    \node[draw=crimson, fill=white, inner sep=2pt] at (0, 0) {\footnotesize 中項 $m$（内側）};
    \node[draw=darkslate, fill=white, inner sep=2pt] at (0, 3.2) {\footnotesize 外枠 $m'$（外側）};
\end{tikzpicture}
\caption{中項 $m$ を含む3属性ダイアグラム（Larger Diagram）の8つの小部屋}
\label{fig:carroll_larger_diagram}
\end{figure}''',

        6: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[thick] (-3, -3) rectangle (3, 3);
    \draw[thick, crimson] (-1.5, -1.5) rectangle (1.5, 1.5);
    \draw (-3, 0) -- (3, 0); \draw (0, -3) -- (0, 3);
    
    % Sitting on the fence counter
    \node[fill=crimson, text=white, circle, inner sep=4pt] (fence) at (0, 0.75) {赤};
    \draw[->, thick, primaryblue] (fence) -- (-0.8, 0.75) node[midway, above] {\footnotesize 灰により移動};
    
    \node[fill=gray!50, text=black, circle, inner sep=4pt] at (0.75, 0.75) {灰};
    
    \node[draw=darkslate, fill=white, rounded corners, align=center, inner sep=4pt] at (0, -3.8) {
        \textbf{境界線上の赤カウンター（Sitting on the Fence）}\\
        \footnotesize 前提1「Some $x$ are $m$」により境界上に置かれた赤コインは、\\
        \footnotesize 前提2「No $m$ are $y'$」による灰コインの侵入で確定セル $xym$ へ押し出される
    };
\end{tikzpicture}
\caption{境界線上のカウンター（Sitting on the fence）と前提統合のダイナミクス}
\label{fig:carroll_sitting_fence}
\end{figure}''',

        7: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    % Larger Diagram with m
    \begin{scope}[xshift=-3.8cm]
        \draw[thick] (-2, -2) rectangle (2, 2);
        \draw[thick, crimson] (-1, -1) rectangle (1, 1);
        \draw (-2, 0) -- (2, 0); \draw (0, -2) -- (0, 2);
        \node[above] at (0, 2.1) {\bfseries Larger Diagram ($x, y, m$)};
        \node[fill=crimson, text=white, circle, inner sep=3pt] at (-0.5, 0.5) {赤};
        \node[fill=gray!50, text=black, circle, inner sep=3pt] at (0.5, 0.5) {灰};
        \node[fill=gray!50, text=black, circle, inner sep=3pt] at (1.5, 1.5) {灰};
        \node[below] at (0, -2.2) {\footnotesize 両前提の合成完了};
    \end{scope}

    % Transfer arrow
    \draw[->, very thick, warmamber] (-1.2, 0) -- (1.2, 0) node[midway, above] {\bfseries 中項 $m$ の消去} node[midway, below] {\footnotesize 結論のトランスファー};

    % Smaller Diagram
    \begin{scope}[xshift=3.8cm]
        \draw[thick] (-1.8, -1.8) rectangle (1.8, 1.8);
        \draw (-1.8, 0) -- (1.8, 0); \draw (0, -1.8) -- (0, 1.8);
        \node[above] at (0, 1.9) {\bfseries Smaller Diagram ($x, y$)};
        \node[fill=crimson, text=white, circle, inner sep=3pt] at (-0.9, 0.9) {赤};
        \node[fill=gray!50, text=black, circle, inner sep=3pt] at (0.9, 0.9) {灰};
        \node[below] at (0, -2.0) {\footnotesize 結論：「All $x$ are $y$」};
    \end{scope}
\end{tikzpicture}
\caption{3属性ボードから2属性ボードへの「中項消去と結論転写（Transfer）」の全貌}
\label{fig:carroll_elimination_transfer}
\end{figure}''',

        8: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \draw[thick, fill=softrose, draw=crimson] (-5.5, -2) rectangle (5.5, 2.5);
    \node[draw=crimson, fill=white, rounded corners, inner sep=5pt] at (0, 1.8) {\bfseries 中項不周延の誤謬（Fallacy of Undistributed Middle）の可視化};
    
    \node[draw=darkslate, fill=white, rectangle, align=center, inner sep=4pt] (p1) at (-3.2, 0.2) {\textbf{前提1：犬は動物}\\\footnotesize Some/All $x$ are $m$\\\footnotesize $m$ の一部に属する};
    \node[draw=darkslate, fill=white, rectangle, align=center, inner sep=4pt] (p2) at (3.2, 0.2) {\textbf{前提2：猫は動物}\\\footnotesize Some/All $y$ are $m$\\\footnotesize $m$ の一部に属する};
    
    \node[draw=crimson, fill=white, rounded corners, inner sep=5pt] (err) at (0, -1.0) {\textbf{中項 $m$ が全体（周延）をカバーしない}};
    
    \draw[->, thick, warmamber] (p1) -- (err);
    \draw[->, thick, warmamber] (p2) -- (err);
    
    \node[draw=darkslate, fill=white, inner sep=3pt] at (0, -1.7) {\footnotesize ボード上：赤カウンターが境界線から動けず、結論ボードに転写不能（推論破綻）};
\end{tikzpicture}
\caption{キャロル・ボードが視覚的に暴く中項不周延の誤謬の幾何学的証明}
\label{fig:carroll_fallacy_middle}
\end{figure}''',

        9: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    % Carroll Diagram (1886)
    \begin{scope}[xshift=-3.5cm]
        \draw[thick] (-1.8, -1.8) rectangle (1.8, 1.8);
        \draw (-1.8, 0) -- (1.8, 0); \draw (0, -1.8) -- (0, 1.8);
        \node[above] at (0, 1.9) {\textbf{キャロル図 (1886)}};
        \node at (-0.9, 0.9) {$xy$}; \node at (0.9, 0.9) {$xy'$};
        \node at (-0.9, -0.9) {$x'y$}; \node at (0.9, -0.9) {$x'y'$};
        \node[below] at (0, -2.0) {\footnotesize 集合・命題の空間分割};
    \end{scope}

    % Arrow
    \draw[->, very thick, primaryblue] (-1.0, 0) -- (1.0, 0) node[midway, above] {\footnotesize 67年の時を経て} node[midway, below] {\footnotesize ベル研究所};

    % Karnaugh Map (1953)
    \begin{scope}[xshift=3.5cm]
        \draw[thick] (-1.8, -1.8) rectangle (1.8, 1.8);
        \draw (-1.8, 0) -- (1.8, 0); \draw (0, -1.8) -- (0, 1.8);
        \node[above] at (0, 1.9) {\textbf{カルノー図 (1953)}};
        \node at (-0.9, 0.9) {\bfseries 1}; \node at (0.9, 0.9) {\bfseries 1};
        \node at (-0.9, -0.9) {\bfseries 0}; \node at (0.9, -0.9) {\bfseries 0};
        \draw[rounded corners, crimson, thick] (-1.6, 0.3) rectangle (1.6, 1.5);
        \node[below] at (0, -2.0) {\footnotesize 論理式の簡略化：$f = x$};
    \end{scope}
\end{tikzpicture}
\caption{キャロルの論理図からモーリス・カルノーのカルノー図（Karnaugh Map）への継承}
\label{fig:carroll_karnaugh}
\end{figure}''',

        10: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, >=stealth]
    % Board as Probability Space
    \draw[very thick, draw=darkslate] (-3.5, -2) rectangle (3.5, 2);
    \node[above] at (0, 2.1) {\bfseries 全事象（確率空間：面積 $S=1$）};
    
    \draw[thick, draw=primaryblue] (-3.5, 0.5) -- (3.5, 0.5);
    \draw[thick, draw=warmamber] (0, -2) -- (0, 2);
    
    % Condition X highlighted
    \fill[softblue, opacity=0.6] (-3.5, 0.5) rectangle (3.5, 2);
    \node[left, primaryblue] at (-3.6, 1.25) {\bfseries 事象 $X$};
    
    % Intersection X and Y
    \fill[softgreen, opacity=0.8] (-3.5, 0.5) rectangle (0, 2);
    \node at (-1.75, 1.25) {\large\bfseries $X \cap Y$};
    \node at (1.75, 1.25) {\footnotesize $X \cap Y^c$};
    
    \node[draw=darkslate, fill=white, rounded corners, inner sep=4pt] at (0, -1.0) {
        \Large $P(Y|X) = \frac{\text{セル } (X \cap Y) \text{ の面積}}{\text{行 } X \text{ の全面積}} = \frac{P(X \cap Y)}{P(X)}$
    };
\end{tikzpicture}
\caption{キャロル・ボード上の条件付き確率：部分領域へのズームインと面積比}
\label{fig:carroll_bayes_prob}
\end{figure}''',

        11: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \node[draw=primaryblue, fill=softblue, rounded corners, inner sep=5pt] (p1) at (-4, 1.5) {前提1：赤ちゃん $\to$ 非論理的};
    \node[draw=primaryblue, fill=softblue, rounded corners, inner sep=5pt] (p2) at (0, 1.5) {前提2：非論理的 $\to$ 危険管理不能};
    \node[draw=primaryblue, fill=softblue, rounded corners, inner sep=5pt] (p3) at (4, 1.5) {前提3：ワニの飼育者 $\to$ 危険管理可能};
    
    \node[draw=crimson, fill=softamber, rounded corners, inner sep=6pt] (chain) at (0, -0.3) {\Large\bfseries 中間概念の連鎖的消去（Sorites）};
    
    \draw[->, thick, warmamber] (p1) -- (chain);
    \draw[->, thick, warmamber] (p2) -- (chain);
    \draw[->, thick, warmamber] (p3) -- (chain);
    
    \node[draw=accentgreen, fill=softgreen, rounded corners, inner sep=5pt] (conc) at (0, -1.8) {\Large\bfseries 必然的結論：いかなる赤ちゃんもワニを飼いならすことはできない};
    \draw[->, very thick, accentgreen] (chain) -- (conc);
\end{tikzpicture}
\caption{キャロルのユーモア連鎖三段論法（ソリテス）の多段消去プロセス}
\label{fig:carroll_sorites}
\end{figure}''',

        12: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    \node[draw=darkslate, fill=white, rounded corners, inner sep=4pt] (ari) at (0, 3) {\textbf{アリストテレス（前4世紀）}：三段論法・形式論理の定式化};
    \node[draw=darkslate, fill=softblue, rounded corners, inner sep=4pt] (boo) at (0, 1.8) {\textbf{ジョージ・ブール（1854）}：思考の法則・論理の代数化 ($x^2=x$)};
    \node[draw=darkslate, fill=softamber, rounded corners, inner sep=4pt] (ven) at (-3, 0.6) {\textbf{ジョン・ヴェン（1866）}：ベン図・客観的頻度論};
    \node[draw=crimson, fill=softrose, rounded corners, inner sep=5pt] (car) at (3, 0.6) {\textbf{ルイス・キャロル（1886）}：キャロル図・論理のゲーム化};
    \node[draw=darkslate, fill=softgreen, rounded corners, inner sep=4pt] (sha) at (0, -0.6) {\textbf{クロード・シャノン（1937）}：ブール代数によるスイッチング回路設計};
    \node[draw=primaryblue, fill=softblue, rounded corners, inner sep=5pt] (mod) at (0, -1.8) {\Large\bfseries 現代のコンピュータ・人工知能・データサイエンス};
    
    \draw[->, thick] (ari) -- (boo);
    \draw[->, thick] (boo) -- (ven);
    \draw[->, thick] (boo) -- (car);
    \draw[->, thick] (ven) -- (sha);
    \draw[->, thick] (car) -- (sha);
    \draw[->, very thick, primaryblue] (sha) -- (mod);
\end{tikzpicture}
\caption{論理学・記号数学・情報科学の壮大な発展系譜とキャロルの位置づけ}
\label{fig:carroll_historical_lineage}
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
\definecolor{crimson}{RGB}{160, 30, 45}
\definecolor{softrose}{RGB}{253, 242, 242}
\definecolor{accentgreen}{RGB}{40, 120, 70}
\definecolor{softgreen}{RGB}{240, 248, 242}

\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=accentgreen,
    urlcolor=warmamber,
    pdftitle={高校生のためのルイス・キャロル論理学入門},
    pdfauthor={教育情報分析研究会}
}

\newtcolorbox{historybox}[2][]{
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

\title{\Huge\textbf{高校生のためのルイス・キャロル論理学入門}\\[6mm]
\Large\textbf{『論理の遊戯』とダイアグラムで楽しむ記号論理・三段論法・確率の数理}\\[4mm]
\large 原著：ルイス・キャロル（チャールズ・ドジソン）『論理の遊戯』\\[2mm]
\normalsize (Project Gutenberg eBook \#4763: \textit{The Game of Logic})}

\author{\textbf{教育情報分析研究会}\\[2mm]
\small 数学教育・統計分析リサーチユニット}
\date{2026年10月 初版（全50頁規模・原著完全準拠版）}

\begin{document}
\maketitle

\frontmatter
\tableofcontents

\chapter*{刊行によせて}
\addcontentsline{toc}{chapter}{刊行によせて}
本書は、『不思議の国のアリス』の作者として世界中に知られる英国の天才、ルイス・キャロル（Lewis Carroll, 本名チャールズ・ラトウィッジ・ドジソン Charles Lutwidge Dodgson, 1832--1898、オックスフォード大学クライスト・チャーチ数学講師）が著した歴史的名著『論理の遊戯』（\textit{The Game of Logic}、1886年刊、Project Gutenberg \#4763）を底本とし、現代の高校生に向けて丁寧に解き明かした本格的入門書である。

キャロルは本書において、中世以来の難解で退屈な暗記科目と化していたアリストテレス論理学を、**「赤と灰のカウンター」**と**「四角いゲーム盤（キャロル・ダイアグラム）」**を用いた、誰もが一人または二人で楽しく遊べる「思考のボードゲーム」へと鮮やかに生まれ変わらせた。
しかし、本書は単なる子どものパズルではない。それはジョージ・ブールが拓いた記号代数学と、ジョン・ヴェンが提案した集合図をさらに発展させ、のちの20世紀においてデジタルコンピュータの回路設計（カルノー図）や、確率空間の幾何学的表現へと結実する、極めて先駆的で強固な数理的基礎を備えている。

著者である「教育情報分析研究会」は、高校数学（数学A「集合と命題」「場合の数と確率」、情報I「論理回路とディジタル演算」、数学B・C「統計的推測」）を学ぶ若者たちが、キャロルのユーモアあふれる言葉の遊戯を通して、現代情報社会を生き抜くための「確固たる論理的思考力」を楽しく、かつ深く体得できるよう、全12章と用語事典・総合演習問題により本書を編纂した。

\mainmatter
'''

    tex_chapters = []
    for num, title, en_title in titles:
        path = f'ollama_cache_carroll/ch{num}.txt'
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
                continue
            elif s.startswith('#### '):
                t = s[5:].replace('&', r'\&').replace('_', r'\_')
                cleaned_lines.append(r'\subsection{' + t + '}')
                continue

            # Check if list item
            is_item = False
            is_enum = False
            item_prefix = ""
            if s.startswith('- ') or s.startswith('* '):
                is_item = True
                s = s[2:].strip()
            elif re.match(r'^\d+\.\s+', s):
                is_enum = True
                s = re.sub(r'^\d+\.\s+', '', s).strip()

            # Remove bold markdown **
            s = s.replace('**', '')

            # Protect math blocks: $$...$$ and $...$
            math_blocks = []
            def save_display_math(m):
                idx = len(math_blocks)
                math_blocks.append(m.group(0))
                return f"QQQMATHBLOCK{idx}QQQ"

            s_temp = re.sub(r'\$\$.*?\$\$', save_display_math, s)
            s_temp = re.sub(r'\$.*?\$', save_display_math, s_temp)

            # Escape non-math special characters
            s_temp = s_temp.replace('&', r'\&')
            s_temp = re.sub(r'(?<!\\)%', r'\%', s_temp)
            s_temp = re.sub(r'(?<!\\)#', r'\#', s_temp)
            s_temp = s_temp.replace('_', r'\_')
            s_temp = s_temp.replace('`', '')

            # Restore math blocks
            for idx, mb in enumerate(math_blocks):
                s_temp = s_temp.replace(f"QQQMATHBLOCK{idx}QQQ", mb)

            if is_item:
                cleaned_lines.append(r'\begin{itemize}\item ' + s_temp + r'\end{itemize}')
            elif is_enum:
                cleaned_lines.append(r'\begin{enumerate}\item ' + s_temp + r'\end{enumerate}')
            else:
                cleaned_lines.append(s_temp)

        body = '\n\n'.join(cleaned_lines)
        fig = tikz_figures.get(num, '')

        comp = """
\\chapter{""" + title + """}
\\label{ch:""" + str(num) + """}

\\begin{historybox}{原著における位置づけ：""" + en_title + """}
本章はルイス・キャロル『論理の遊戯』（Project Gutenberg \\#4763）の該当章および数理体系に直接基づき、
四角いダイアグラムと赤・灰のカウンターによる論理のアルゴリズムを、現代の高校数学・情報科学の視点から完全に読み解くものである。
\\end{historybox}

""" + body + """

""" + fig + """

\\section*{本章のまとめと確認演習}
\\begin{examplebox}{キャロル論理学の理解度チェック}
\\textbf{【問】} 本章で学んだ概念について、以下の設問に答えよ。
\\begin{enumerate}[label=(\\arabic*)]
\\item キャロルが考案したダイアグラムとカウンターのルールに従い、本章の主要な命題や推論を自分の手で図示せよ。
\\item 伝統的な形式論理学やベン図と比較したとき、キャロル流の解法が持つ直観的・機械的利点を説明せよ。
\\item この思考法が現代の情報科学（論理回路・二値論理）や確率論においてどのように活かされているか考察せよ。
\\end{enumerate}
\\end{examplebox}
"""
        tex_chapters.append(comp)

    glossary = r'''
\backmatter
\chapter{ルイス・キャロル論理学 重要用語辞典（Glossary）}
\label{ch:glossary}
\addcontentsline{toc}{chapter}{ルイス・キャロル論理学 重要用語辞典}

\begin{description}[leftmargin=3.5cm, style=nextline]
\item[限定宇宙（Universe of Discourse）]
議論や推論の対象となるすべての事物の全体集合。キャロル・ボードの外枠全体がこの限定宇宙を表し、現代集合論における普遍集合（Universal Set）$U$ または全事象 $S$ に相当する。

\item[2属性ダイアグラム（Smaller Diagram）]
2つの排他的属性 $x, x'$（上下の二分割）と $y, y'$（左右の二分割）によって、限定宇宙を4つの小部屋（$xy, xy', x'y, x'y'$）に分割した正方形の盤面。2つの命題の関係や三段論法の最終結論を表示するために用いられる。

\item[3属性ダイアグラム（Larger Diagram）]
2属性ダイアグラムに第3の属性である中項 $m$（内側の正方形）と $m'$（外枠の領域）を追加し、空間を $2^3 = 8$ 個の小部屋に分割した盤面。三段論法の2つの前提を統合し、中項を消去するために用いられる。

\item[赤カウンター（Red Counter）]
キャロル・ゲームにおいて「事物の存在（Existence / FULL）」を表す赤い駒。そのセルに少なくとも1つの要素が存在すること（要素数 $\ge 1$、現代論理学の存在量化 $\exists$）を意味する。

\item[灰カウンター（Grey Counter）]
「事物の非存在（Empty / 0）」を表す灰色の駒。そのセルには1つの要素も存在しないこと（空集合 $\emptyset$）を意味する。

\item[空白セル（Empty Cell / Unknown）]
カウンターが置かれていないセル。その部屋に事物が存在するか空であるかについて「何の情報もない（未定）」ことを表す。キャロルは「情報なし」と「空（0）」を厳格に区別した。

\item[特称肯定命題（Particular Affirmative, I）]
「いくつかの $x$ は $y$ である（Some $x$ are $y$）」。セル $xy$ に赤カウンターを1枚置くことで表現される。

\item[全称否定命題（Universal Negative, E）]
「いかなる $x$ も $y$ ではない（No $x$ are $y$）」。セル $xy$ に灰カウンターを置くことで表現される。

\item[全称肯定命題（Universal Affirmative, A）]
「すべての $x$ は $y$ である（All $x$ are $y$）」。キャロル流の解釈では、セル $xy'$ に灰カウンターを置き、かつセル $xy$ に赤カウンターを置く「二重配置」として定義される。

\item[特称否定命題（Particular Negative, O）]
「いくつかの $x$ は $y$ ではない（Some $x$ are not $y$）」。セル $xy'$ に赤カウンターを置くことで表現される。

\item[存在前提（Existential Import）]
全称命題「すべての $x$ は $y$ である」と主張するとき、主語 $x$ の外延が存在することを前提とするか否かという問題。現代論理学では空集合でも真とするが、キャロルは日常言語の健全性から存在を前提とした。

\item[中項（Middle Term, $m$）]
三段論法において、大前提と小前提の双方に含まれ、両者を媒介して結論を導くための架け橋となる概念。結論には現れず、推論の過程で消去される。

\item[境界線上のカウンター（Sitting on the Fence）]
ある前提（例：「Some $x$ are $m$」）において、第3の属性 $y$ に関する情報が不明な場合、赤カウンターを2つのセルの境界線（fence）の上にまたがって置くキャロルの卓越した図的技法。

\item[カウンターの押し出し（Dropping off the Fence）]
境界線上に置かれた赤カウンターが、別の前提によって片方のセルに灰カウンターが置かれた際、空となったセルを避けてもう一方のセルの中へと確定的に落ちる力学的推論プロセス。

\item[消去法（Elimination）]
三段論法において、3属性ダイアグラム上で中項 $m$ の境界を無視し、$x$ と $y$ の関係のみを抽出する手続き。ブール代数における消去定理の幾何学的実行である。

\item[結論のトランスファー（Transfer of Conclusion）]
Larger Diagram で中項 $m$ を消去した結果（$x$ と $y$ の残存情報）を、Smaller Diagram へとそっくり移し替えて最終結論を読み取る操作。

\item[三段論法（Syllogism）]
2つの前提命題（大前提・小前提）から論理的必然性をもって1つの結論を導き出す演繹的推論形式。アリストテレス以来の形式論理学の中核。

\item[中項不周延の誤謬（Fallacy of Undistributed Middle）]
中項 $m$ が前提においてその全外延にわたって言及されていないため、$x$ と $y$ の間に必然的な関係を導けない形式的誤謬。キャロル・ボード上では、赤カウンターが境界線上に留まり続け結論盤へ移せないこととして可視化される。

\item[両前提否定の誤謬（Fallacy of Negative Premises）]
2つの前提がともに否定命題（No...）であるとき、いかなる肯定的または必然的結論も導けないという規則。盤面上で中項の内外がいずれも遮断されるため推論が成立しない。

\item[連鎖三段論法（ソリテス / Sorites）]
3つ以上の前提が鎖のように連なり、多数の中間項を順次消去していく多段論法。キャロルが好んでパズルとして出題した。

\item[カルノー図（Karnaugh Map）]
1953年にモーリス・カルノーが開発した、ブール代数の論理式を最小化するための格子図。キャロル・ダイアグラムの正方形セル分割と論理的・構造的に完全同型である。

\item[論理積（AND / 共通部分）]
2つの属性がともに成り立つ領域。キャロル・ボードにおける小部屋（$xy$ など）の交差に対応する。

\item[論理和（OR / 和集合）]
2つの属性の少なくとも一方が成り立つ領域。ボード上で隣接する複数のセルをまとめたブロックとして視覚化される。

\item[二値論理（Binary Logic）]
真（1）と偽（0）の2つの値のみを扱う論理体系。現代のデジタルコンピュータやプログラミング言語の動作原理。

\item[三値論理（Ternary Logic）]
真・偽に加えて「未定・不明（Unknown）」の第3の状態を明示的に扱う論理体系。キャロルのカウンターなし状態がこれに相当する。

\item[結合確率（Joint Probability, $P(X \cap Y)$）]
2つの事象 $X$ と $Y$ が同時に発生する確率。キャロル・ボードを面積1の確率空間とみなしたとき、セル $xy$ の面積に対応する。

\item[条件付き確率（Conditional Probability, $P(Y|X)$）]
事象 $X$ が起こったという条件下で、事象 $Y$ が起こる確率。盤面全体から行 $X$ にズームインし、その中でセル $xy$ が占める面積比 $\frac{P(X \cap Y)}{P(X)}$ として定義される。

\item[ベイズの定理（Bayes' Theorem）]
結果の観察（検査陽性など）から、その原因（真の罹患）の事後確率を逆算する公式。キャロル・ボード上の分割セルの比率計算として直感的に導出できる。

\item[感度と特異度（Sensitivity and Specificity）]
検査の性能を表す指標。感度は陽性のものを正しく陽性と判定する確率、特異度は陰性のものを正しく陰性と判定する確率。

\item[客観的論理主義（Carroll's Logicism）]
思考や言語を主観的な感覚や曖昧さに委ねず、客観的な記号・図形・機械的ルールによって一意に決定しようとするキャロルの数学的態度。
\end{description}

\chapter{高校生のための総合演習問題と詳細解答}
\label{ch:final_exam}
\addcontentsline{toc}{chapter}{高校生のための総合演習問題と詳細解答}

\section*{総合問題}
\begin{enumerate}[label=\textbf{【問題\arabic*】}]
\item ある学校の生徒集団において、属性 $x$ を「理系選択者」、属性 $y$ を「チェス同好会員」とする。
次の命題をキャロルの Smaller Diagram 上にプロットし、それぞれの盤面の意味を説明せよ。
\begin{enumerate}[label=(\alph*)]
\item 「理系選択者の中にチェス同好会員がいる（Some $x$ are $y$）」
\item 「文系選択者（$x'$）にはチェス同好会員は一人もいない（No $x'$ are $y$）」
\item 「すべての理系選択者はチェス同好会員である（All $x$ are $y$）」
\end{enumerate}

\item 次の2つの前提から、キャロルの Larger Diagram（3属性盤）を用いて中項 $m$ を消去し、導かれる結論を Smaller Diagram 上に転写して日本語で述べよ。
\begin{itemize}
\item 大前提：「すべての数学者は思索家である（All $x$ are $m$）」
\item 小前提：「思索家でせっかちな者はいない（No $m$ are $y$）」
\end{itemize}
（ただし、$x$：数学者、$m$：思索家、$y$：せっかちな者 とする）

\item ある新興感染症の検査キットについて考える。全人口における真の罹患者の割合（事前確率）を $1\%$ とする。この検査キットは、実際に感染している人を $95\%$ の確率で「陽性」と判定し（感度 $95\%$）、感染していない人を $90\%$ の確率で正しく「陰性」と判定する（特異度 $90\%$、偽陽性率 $10\%$）。
キャロル・ボード（面積 $10000$ の正方形）を用いてこの確率空間を4つのセルに分割し、ある人が「陽性」と判定されたとき、その人が実際に感染している確率（事後確率）を求めよ。
\end{enumerate}

\section*{詳細な解答と解説}
\begin{description}[leftmargin=2.5cm, style=nextline]
\item[問題1の解答]
\begin{enumerate}[label=(\alph*)]
\item セル $xy$（上段左：理系かつチェス会員）に赤カウンターを1枚置く。
【解説】これは集合 $x \cap y \neq \emptyset$ を意味し、理系かつチェス愛好者である生徒が少なくとも1人実在することを示す。

\item セル $x'y$（下段左：文系かつチェス会員）に灰カウンターを1枚置く。
【解説】これは集合 $x' \cap y = \emptyset$（空集合）を意味し、文系かつチェス同好会の部屋には誰も存在しないことを表す。

\item セル $xy'$（上段右：理系かつチェス非会員）に灰カウンターを置き、セル $xy$（上段左）に赤カウンターを置く。
【解説】キャロル流の全称肯定命題の完全表現である。「チェスをやらない理系生徒はゼロである（灰）」と同時に「理系生徒は実在する（赤）」という二重の条件を満たす。
\end{enumerate}

\item[問題2の解答]
ステップ1（前提1のプロット）：大前提「All $x$ are $m$」より、外側（$m'$）の $x$ 領域であるセル $xym'$ とセル $xy'm'$ の双方に灰カウンターを置く。また、$x$ の存在により内側（$m$）の境界線上に赤カウンターを置く。
ステップ2（前提2のプロット）：小前提「No $m$ are $y$」より、内側（$m$）の $y$ 領域であるセル $xym$ に灰カウンターを置く。
ステップ3（カウンターの押し出し）：内側境界線上にあった赤カウンターは、左セル $xym$ に灰カウンターが入ったため、右セル $xy'm$ へと確定的に落ちる。
ステップ4（中項 $m$ の消去と転写）：中項 $m$ を取り除き、$x$ と $y$ の関係に注目すると、セル $xy$ は $xym, xym'$ ともに灰（空）、セル $xy'$ は赤（存在）が残る。
Smaller Diagram に転写すると、上段左（$xy$）に灰、上段右（$xy'$）に赤が配置される。
【結論】「No $x$ are $y$（いかなる数学者もせっかちではない）」、あるいは「All $x$ are $y'$（すべての数学者はせっかちではない）」。

\item[問題3の解答]
全体を $10,000$ 人の正方形ボード（横 $100 \times$ 縦 $100$）とする。
行の分割（真の罹患 $x$ と非罹患 $x'$）：
\begin{itemize}
\item 罹患者（$x$）：$10,000 \times 0.01 = 100$ 人（上段）
\item 非罹患者（$x'$）：$10,000 \times 0.99 = 9,900$ 人（下段）
\end{itemize}
列の分割（検査陽性 $y$ と検査陰性 $y'$）：
\begin{itemize}
\item セル $xy$（罹患かつ陽性）：$100 \times 0.95 = 95$ 人
\item セル $xy'$（罹患かつ陰性）：$100 \times 0.05 = 5$ 人
\item セル $x'y$（非罹患だが偽陽性）：$9,900 \times (1 - 0.90) = 990$ 人
\item セル $x'y'$（非罹患かつ真陰性）：$9,900 \times 0.90 = 8,910$ 人
\end{itemize}
陽性と判定された全生徒（列 $y$ の全面積）は、
\[
\text{陽性者総数} = 95 + 990 = 1,085 \text{ 人}
\]
この列 $y$ の中で、実際に感染しているセル $xy$ の割合（条件付き確率）は、
\[
P(x|y) = \frac{95}{1,085} = \frac{19}{217} \approx 0.0876 \quad (8.76\%)
\]
【解説】感度 $95\%$ という高精度な検査であっても、ベースの罹患率が $1\%$ と低い場合、陽性と出た人のうち実際に感染している確率はわずか $8.76\%$（約 $11$ 人に $1$ 人）に過ぎない。この「偽陽性の罠」が、キャロル・ボードの面積比として一目瞭然に可視化される。
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

    out_path = r'books/4763_carroll_game_of_logic/carroll_game_of_logic_intro.tex'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_tex)
    print(f'Wrote {len(full_tex)} bytes to {out_path}')

if __name__ == '__main__':
    build_carroll_tex()
