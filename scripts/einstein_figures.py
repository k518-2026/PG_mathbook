# -*- coding: utf-8 -*-
"""
TikZ Figures and Captions for 12 Chapters of Einstein Relativity Intro
Designed with extra-large vertical/horizontal clearance, perfectly balanced boxes,
and absolute zero overlap for all labels, badges, and illustrations.
"""

FIGS = {
    1: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Coordinate axes with ample margin
    \draw[->, very thick, gray!70] (-0.8, 0) -- (10.2, 0) node[right, black, font=\normalsize\bfseries] {$x$ (空間座標)};
    \draw[->, very thick, gray!70] (0, -0.6) -- (0, 5.2) node[above, black, font=\normalsize\bfseries] {$y$ (直交座標)};
    \draw[step=1.0, gray!20, very thin] (-0.5, -0.5) grid (9.8, 4.8);
    
    % Reference Frame Badge - placed clearly in upper left
    \node[draw=blue!80, fill=blue!12, rounded corners=4pt, line width=1.2pt, inner sep=6pt, font=\normalsize\bfseries, text=blue!90!black] 
        at (2.2, 4.4) {基準剛体座標系 $K$};
        
    % Concept Annotation Box - placed on upper right with plenty of room
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (6.8, 3.8) {\textbf{【アインシュタインの幾何学的洞察】}\\
        ・ユークリッド幾何学の命題は単なる抽象概念ではない\\
        ・2点間の「距離」とは、物理的な剛体定規を並べた実測値である\\
        ・座標系 $K$ は空間を満たす仮想の剛体格子として定義される};

    % Measuring Rod (L0) - placed at y = 1.3
    \draw[|-|, line width=2.5pt, red!85!black] (1.8, 1.3) -- (7.8, 1.3);
    \node[above=6pt, fill=white, inner sep=3pt, font=\normalsize\bfseries, text=red!85!black] 
        at (4.8, 1.3) {基準剛体定規（固有長 $L_0$）};
        
    % Measuring tick marks on the rod
    \foreach \x in {2.8, 3.8, 4.8, 5.8, 6.8} {
        \draw[thick, red!70!black] (\x, 1.15) -- (\x, 1.45);
    }
    
    % Event points A and B with generous clearance below
    \fill[red!90!black] (1.8, 1.3) circle (4pt);
    \node[below=10pt, fill=white, inner sep=2.5pt, font=\small\bfseries] at (1.8, 1.3) {基点 $A (x_1, y_1)$};
    
    \fill[red!90!black] (7.8, 1.3) circle (4pt);
    \node[below=10pt, fill=white, inner sep=2.5pt, font=\small\bfseries] at (7.8, 1.3) {終点 $B (x_2, y_2)$};
\end{tikzpicture}""",
    r"ユークリッド幾何学の命題を物理的な「剛体定規」による目盛り計測として捉え直す座標系 $K$ の構造。"),

    2: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Classical law vs question box at top
    \node[align=left, fill=white, draw=gray!60, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (5.0, 5.8) {\textbf{【ガリレイ変換と速度合成則の根本問題】}\\
        古典力学：堤防から見た歩行速度 $W = v + w$（単純な足し算）\\
        \textbf{核心の疑問}：もし歩行者ではなく「光（速度 $c$）」を放ったら、$W = v + c$ となるのか？\\
        $\implies$ マクスウェル電磁気学（光速普遍）と古典力学の真っ向対立！};

    % Train carriage (Moving Frame K') - made wider and taller
    \draw[very thick, fill=blue!12, draw=blue!75, rounded corners=6pt] (1.0, 2.0) rectangle (8.8, 4.3);
    \node[font=\normalsize\bfseries, text=blue!85!black] at (5.0, 3.8) {走行列車（運動系 $K'$）};
    
    % Observer M' inside train
    \node[draw=teal!80!black, circle, fill=cyan!35, inner sep=3pt, font=\small\bfseries] (obsMp) at (2.4, 2.9) {観測者 $M'$};
    
    % Walker walking inside train
    \fill[teal!80!black] (4.4, 2.9) circle (3pt);
    \draw[->, line width=2pt, teal!80!black] (4.4, 2.9) -- (7.2, 2.9) 
        node[midway, above=4pt, fill=white, inner sep=2.5pt, font=\small\bfseries, text=teal!90!black] {車内歩行 $w$};
        
    % Train velocity v arrow
    \draw[->, line width=2.5pt, red!85!black] (8.8, 3.15) -- (10.8, 3.15) 
        node[right, font=\normalsize\bfseries, text=red!85!black] {列車速度 $v$};

    % Embankment (Stationary Frame K)
    \draw[thick, fill=brown!25, draw=brown!60!black] (-0.8, -0.6) rectangle (10.2, 0.6);
    \node[font=\normalsize\bfseries, text=brown!60!black] at (5.5, 0.0) {堤防（静止基準系 $K$）};
    
    % Observer M on embankment
    \node[draw=orange!80!black, circle, fill=yellow!40, inner sep=3pt, font=\small\bfseries] (obsM) at (0.8, 1.4) {観測者 $M$};
    \draw[thick, gray!60, dashed] (0.8, 0.6) -- (obsM);
\end{tikzpicture}""",
    r"堤防の静止系 $K$ と一定速度 $v$ で走る列車系 $K'$ における運動の相対性と古典速度合成則。"),

    3: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Physical verdict box at top
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (4.0, 6.2) {\textbf{【同時性の相対性（Relativity of Simultaneity）の決定打】}\\
        ・堤防の観測者 $M$ にとって：光は両端から等距離を同速 $c$ で進むため「$A$ と $B$ は同時に起きた」\\
        ・車内の観測者 $M'$ にとって：列車が右へ走るため、$B$ からの光に先に出会い、$A$ からの光は後から来る\\
        $\implies$ \textbf{「同時に起きたかどうか」は観測者の運動状態によって異なる！時間は絶対ではない}};

    % Train body
    \draw[very thick, fill=blue!12, draw=blue!75, rounded corners=6pt] (0.0, 3.0) rectangle (8.0, 4.6);
    \node[font=\normalsize\bfseries, text=blue!85!black] at (4.0, 4.15) {高速列車（速度 $v$ で右方へ走行）};
    
    % Train velocity arrow
    \draw[->, line width=2.5pt, red!85!black] (8.0, 3.8) -- (9.6, 3.8) 
        node[right, font=\normalsize\bfseries, text=red!85!black] {$v$};
        
    % Observer M' inside train
    \node[draw=teal!80!black, circle, fill=cyan!35, inner sep=3pt, font=\small\bfseries] (obsMp) at (4.5, 3.5) {$M'$};
    \node[below=8pt, fill=white, inner sep=2pt, font=\footnotesize\bfseries] at (4.5, 3.0) {車内中点 $M'$（光 $B$ に突進し、光 $A$ から逃げる）};

    % Light waves in middle layer (y = 1.6) - well separated from train and embankment
    \draw[decorate, decoration={snake, amplitude=2.5pt, segment length=6pt}, line width=1.3pt, orange!90!black, ->] 
        (-0.8, 1.6) -- (3.3, 1.6) node[midway, above=3pt, fill=white, inner sep=1.5pt, font=\footnotesize\bfseries] {光速 $c \longrightarrow$};
    \draw[decorate, decoration={snake, amplitude=2.5pt, segment length=6pt}, line width=1.3pt, orange!90!black, ->] 
        (8.8, 1.6) -- (4.7, 1.6) node[midway, above=3pt, fill=white, inner sep=1.5pt, font=\footnotesize\bfseries] {$\longleftarrow$ 光速 $c$};

    % Embankment ground (y = -0.4 to 0.4)
    \draw[thick, fill=gray!20, draw=gray!60] (-2.2, -0.4) rectangle (10.2, 0.4);
    \node[font=\normalsize\bfseries, text=gray!80!black] at (6.5, 0.0) {堤防（静止系 $K$）};
    
    % Observer M on embankment
    \node[draw=orange!80!black, circle, fill=yellow!45, inner sep=3pt, font=\small\bfseries] (obsM) at (4.0, 0.4) {$M$};
    \node[above=4pt, fill=white, inner sep=2pt, font=\footnotesize\bfseries] at (4.0, 0.8) {堤防中点 $M$（$A, B$ からの光が「同時」に到達）};

    % Lightning strike points A and B
    \fill[red!90!black] (-1.0, 0.4) circle (4pt);
    \node[below=5pt, fill=white, inner sep=2pt, font=\small\bfseries, text=red!80!black] at (-1.0, -0.4) {落雷地点 $A$};
    \draw[line width=1.5pt, red!80!black, -{Latex[length=3mm]}] (-1.0, 2.2) -- (-1.0, 0.5) 
        node[midway, left=2pt, font=\scriptsize\bfseries, text=red!80!black] {雷撃};
        
    \fill[red!90!black] (9.0, 0.4) circle (4pt);
    \node[below=5pt, fill=white, inner sep=2pt, font=\small\bfseries, text=red!80!black] at (9.0, -0.4) {落雷地点 $B$};
    \draw[line width=1.5pt, red!80!black, -{Latex[length=3mm]}] (9.0, 2.2) -- (9.0, 0.5) 
        node[midway, right=2pt, font=\scriptsize\bfseries, text=red!80!black] {雷撃};
\end{tikzpicture}""",
    r"列車と堤防の思考実験。堤防の中点 $M$ で同時の2つの落雷は、前進する車内の中点 $M'$ には同時に届かない。"),

    4: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Subfigure 1: Rest Frame Clock
    \begin{scope}[xshift=0cm]
        \draw[thick, fill=blue!8, draw=blue!60, rounded corners=4pt] (0, 0) rectangle (2.8, 5.0);
        \node[font=\normalsize\bfseries, text=blue!85!black] at (1.4, 5.4) {【静止系 $S'$（固有時間 $\Delta t_0$）】};
        
        % Light source / detector
        \fill[black] (1.4, 0.7) circle (3.5pt);
        \node[below=4pt, fill=white, inner sep=2pt, font=\scriptsize\bfseries] at (1.4, 0.6) {発光部・検出器};
        
        % Ceiling mirror
        \draw[line width=3.5pt, blue!80!black] (0.4, 4.3) -- (2.4, 4.3);
        \node[above=3pt, font=\scriptsize\bfseries, text=blue!80!black] at (1.4, 4.3) {天井の鏡};
        
        % Light path up and down
        \draw[decorate, decoration={snake, amplitude=2pt, segment length=6pt}, line width=1.5pt, red!85!black, ->] 
            (1.25, 0.8) -- (1.25, 4.2) node[midway, left=2pt, font=\scriptsize\bfseries] {往路 $c$};
        \draw[decorate, decoration={snake, amplitude=2pt, segment length=6pt}, line width=1.5pt, orange!85!black, ->] 
            (1.55, 4.2) -- (1.55, 0.8) node[midway, right=2pt, font=\scriptsize\bfseries] {復路 $c$};
            
        % Height L dimension with offset
        \draw[|<->|, thick, gray!80!black] (0.25, 0.7) -- (0.25, 4.3) 
            node[midway, left=2pt, fill=white, inner sep=2pt, font=\small\bfseries] {$L$};
            
        \node[fill=white, draw=blue!40, rounded corners=3pt, inner sep=4pt, font=\footnotesize\bfseries] 
            at (1.4, -0.7) {$\Delta t_0 = \dfrac{2L}{c}$};
    \end{scope}

    % Subfigure 2: Moving Frame Clock - expanded height and width
    \begin{scope}[xshift=4.2cm]
        \draw[thick, fill=orange!8, draw=orange!60, rounded corners=4pt] (-0.3, 0) rectangle (7.5, 5.0);
        \node[font=\normalsize\bfseries, text=orange!90!black] at (3.6, 5.4) {【静止観察者 $S$ から見た移動系（時間 $\Delta t$）】};
        
        % Ground axis
        \draw[->, thick, gray!60] (-0.2, 0.7) -- (7.3, 0.7) node[right, black, font=\scriptsize] {$x$};
        
        % Positions of clock: start, top bounce, finish
        \fill[black] (0.5, 0.7) circle (3pt) node[below=5pt, font=\scriptsize] {発光 $t=0$};
        \draw[line width=2.5pt, blue!80!black] (2.4, 4.3) -- (4.8, 4.3);
        \fill[blue!80!black] (3.6, 4.3) circle (2.5pt) node[above=4pt, font=\scriptsize] {反射 $t=\frac{\Delta t}{2}$};
        \fill[black] (6.7, 0.7) circle (3pt) node[below=5pt, font=\scriptsize] {受光 $t=\Delta t$};
        
        % Triangle light path
        \draw[dashed, red!85!black, line width=1.8pt] (0.5, 0.7) -- (3.6, 4.3) -- (6.7, 0.7);
        \draw[->, line width=1.5pt, red!85!black] (0.5, 0.7) -- (2.05, 2.5);
        \draw[->, line width=1.5pt, red!85!black] (3.6, 4.3) -- (5.15, 2.5);
        
        % Diagonal label clearly placed outside the triangle to the left
        \node[left=3pt, fill=white, inner sep=2pt, font=\scriptsize\bfseries, text=red!85!black] 
            at (1.6, 2.7) {斜行距離 $\frac{c\Delta t}{2}$};
        
        % Vertical dashed line L
        \draw[dashed, thick, gray!70] (3.6, 0.7) -- (3.6, 4.3) 
            node[midway, right=2pt, fill=white, inner sep=1.5pt, font=\scriptsize] {高さ $L$};
            
        % Horizontal distances
        \draw[<->, thick, teal!80!black] (0.5, 0.2) -- (3.6, 0.2) 
            node[midway, fill=white, inner sep=1.5pt, font=\scriptsize\bfseries] {$\frac{v\Delta t}{2}$};
        \draw[<->, thick, teal!80!black] (0.5, -0.4) -- (6.7, -0.4) 
            node[midway, fill=white, inner sep=2pt, font=\scriptsize\bfseries] {全体移動距離 $v\Delta t$};
            
        % Pythagorean theorem box - comfortably placed in upper-middle
        \node[align=left, fill=white, draw=red!50, rounded corners=4pt, inner sep=4pt, font=\scriptsize] 
            at (3.6, 2.2) {\textbf{直角三角形に三平方の定理を適用：}\\
            $\left(\dfrac{c\Delta t}{2}\right)^2 = L^2 + \left(\dfrac{v\Delta t}{2}\right)^2$\\
            $\implies \Delta t = \dfrac{\Delta t_0}{\sqrt{1 - v^2/c^2}} > \Delta t_0$};
    \end{scope}
\end{tikzpicture}""",
    r"光時計の思考実験。三平方の定理から時間の遅れ $\Delta t = \Delta t_0 / \sqrt{1 - v^2/c^2}$ が導かれる幾何学的構造。"),

    5: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Stationary Rod (Intrinsic Length L0)
    \node[anchor=east, font=\normalsize\bfseries, text=blue!85!black] at (-0.8, 3.2) {静止時（固有長）：};
    \draw[fill=blue!15, draw=blue!75, line width=1.2pt, rounded corners=2pt] (0, 2.7) rectangle (6.5, 3.7);
    
    % Dimension L0
    \draw[|<->|, line width=1.2pt, blue!85!black] (0, 4.1) -- (6.5, 4.1) 
        node[midway, fill=white, inner sep=3pt, font=\normalsize\bfseries] {固有長 $L_0$（静止系で測定）};
    \draw[dashed, gray!60] (0, 2.7) -- (0, 4.3);
    \draw[dashed, gray!60] (6.5, 2.7) -- (6.5, 4.3);

    % Transverse thickness unchanged note (left of rod)
    \draw[<->, thick, teal!80!black] (-0.4, 2.7) -- (-0.4, 3.7) node[midway, left=2pt, font=\scriptsize] {幅 $D$};

    % Moving Rod (Lorentz Contracted Length L)
    \node[anchor=east, font=\normalsize\bfseries, text=red!85!black] at (-0.8, 1.0) {高速運動時（測定長）：};
    \draw[fill=red!20, draw=red!75, line width=1.2pt, rounded corners=2pt] (0, 0.5) rectangle (3.9, 1.5);
    
    % Dimension L
    \draw[|<->|, line width=1.2pt, red!85!black] (0, -0.1) -- (3.9, -0.1) 
        node[midway, fill=white, inner sep=3pt, font=\normalsize\bfseries] {$L = L_0 \sqrt{1 - v^2/c^2} < L_0$};
    \draw[dashed, gray!60] (0, 0.5) -- (0, -0.3);
    \draw[dashed, gray!60] (3.9, 0.5) -- (3.9, -0.3);
    
    % Transverse thickness unchanged note
    \draw[<->, thick, teal!80!black] (-0.4, 0.5) -- (-0.4, 1.5) node[midway, left=2pt, font=\scriptsize] {幅 $D$};

    % Velocity arrow
    \draw[->, line width=2.5pt, red!85!black] (4.1, 1.0) -- (5.6, 1.0) 
        node[right, font=\normalsize\bfseries, text=red!85!black] {速度 $v$};
        
    % Explanation Box placed well to the right
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (9.2, 2.1) {\textbf{【ローレンツ収縮の本質】}\\
        ・縮むのは「運動方向」の成分のみ\\
        ・運動に垂直な方向の寸法（幅や高さ）は全く変わらない\\
        ・物体が押し潰されるのではなく、\\
        　観測者の「同時性の定義」の違いによって\\
        　空間の間隔そのものが短縮して測られる};
\end{tikzpicture}""",
    r"進行方向に沿って剛体の長さが縮むローレンツ収縮の幾何学的イメージ。"),

    6: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Coordinate axes
    \draw[->, very thick, gray!70] (0, 0) -- (8.0, 0) node[right, black, font=\normalsize\bfseries] {速度 $v$};
    \draw[->, very thick, gray!70] (0, 0) -- (0, 5.2) node[above, black, font=\normalsize\bfseries] {質量 $m(v)$ / 全エネルギー $E$};
    
    % Light speed barrier
    \draw[dashed, line width=1.5pt, red!80!black] (6.2, 0) -- (6.2, 5.0);
    \node[above=3pt, font=\normalsize\bfseries, text=red!85!black] at (6.2, 5.0) {光速壁 $c$（宇宙の最高速度）};
    
    % Relativistic Curve plot
    \draw[domain=0:5.85, smooth, samples=120, line width=2.5pt, blue!80!black] 
        plot ({\x}, {1.0 / sqrt(1 - (\x/6.2)*(\x/6.2))});
        
    % Rest mass marker (v=0)
    \fill[blue!85!black] (0, 1.0) circle (4pt);
    \node[left=4pt, fill=white, inner sep=2pt, font=\normalsize\bfseries, text=blue!85!black] at (0, 1.0) {静止エネルギー $E_0 = m_0 c^2$};
    
    % Asymptotic divergence note
    \draw[->, line width=1.2pt, red!85!black] (5.4, 4.0) -- (6.0, 4.5);
    \node[left=6pt, fill=white, draw=red!40, rounded corners=3pt, inner sep=3pt, font=\footnotesize\bfseries, text=red!85!black] 
        at (5.3, 4.0) {$v \to c$ で無限大へ発散！};
        
    % Explanation badge
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (3.2, 3.4) {\textbf{【$E = mc^2$ と光速の壁】}\\
        ・運動エネルギーを加えるほど、物体は加速しにくくなり質量が増大する\\
        ・速度が光速 $c$ に達するには「無限のエネルギー」が必要\\
        $\implies$ 質量を持つ通常物体は絶対に光速を超えられない};
\end{tikzpicture}""",
    r"質量とエネルギーの等価性 $E = mc^2$ と、光速 $c$ へ近づくにつれて無限大へ発散する相対論的質量。"),

    7: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % 4D Spacetime coordinate axes
    \draw[->, very thick, gray!70] (-4.5, 0) -- (4.5, 0) node[right, black, font=\normalsize\bfseries] {空間 $x$};
    \draw[->, very thick, gray!70] (0, -0.6) -- (0, 5.0) node[above, black, font=\normalsize\bfseries] {時間 $ct$};
    
    % Light cone area (Future light cone)
    \fill[yellow!25, opacity=0.7] (0, 0) -- (4.2, 4.2) -- (-4.2, 4.2) -- cycle;
    
    % Light cone boundary rays
    \draw[line width=2pt, orange!90!black] (-4.2, 4.2) -- (0, 0) -- (4.2, 4.2);
    \node[above right=2pt, fill=white, inner sep=1.5pt, font=\footnotesize\bfseries, text=orange!90!black] 
        at (2.6, 2.6) {光の世界線 ($x = +ct$)};
    \node[above left=2pt, fill=white, inner sep=1.5pt, font=\footnotesize\bfseries, text=orange!90!black] 
        at (-2.6, 2.6) {光の世界線 ($x = -ct$)};
        
    % Worldline of massive particle
    \draw[line width=2.5pt, blue!80!black] (0, 0) .. controls (0.6, 1.5) and (-0.4, 2.8) .. (0.9, 4.6)
        node[above=2pt, fill=white, inner sep=2pt, font=\small\bfseries, text=blue!85!black] {物体の世界線 ($v < c$)};
        
    % Spacetime interval classification
    \node[font=\footnotesize\bfseries, text=teal!80!black] at (0, 3.6) {【時間的領域（因果律が成立）】};
    \node[font=\scriptsize, text=gray!80!black] at (3.3, 0.8) {【空間的領域（因果関係不能）】};
    \node[font=\scriptsize, text=gray!80!black] at (-3.3, 0.8) {【空間的領域（超光速が必要）】};
    
    % Invariant formula badge
    \node[align=center, fill=white, draw=gray!60, rounded corners=5pt, inner sep=5pt, font=\footnotesize, line width=0.8pt] 
        at (0, 1.5) {\textbf{ミンコフスキーの時空不変間隔：}\\
        $s^2 = c^2 t^2 - x^2 > 0$（光円錐内部）};
\end{tikzpicture}""",
    r"ミンコフスキーの4次元時空と光円錐（Light Cone）。すべての因果律は光円錐の内部に制限される。"),

    8: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Subfigure 1: Earth Gravity Field
    \begin{scope}[xshift=0cm]
        \draw[thick, fill=blue!8, draw=blue!60, rounded corners=5pt] (0, 0) rectangle (3.2, 4.4);
        \node[font=\normalsize\bfseries, text=blue!85!black] at (1.6, 4.8) {【静止系：地上重力場】};
        
        % Ground surface
        \fill[gray!40] (-0.2, -0.3) rectangle (3.4, 0);
        \node[font=\scriptsize\bfseries, text=gray!80!black] at (1.6, -0.5) {地球表面（重力源）};
        
        % Free-falling ball
        \fill[red!85!black] (1.6, 2.7) circle (4pt);
        \node[right=4pt, fill=white, inner sep=2pt, font=\scriptsize\bfseries] at (1.6, 2.7) {落下する球};
        \draw[->, line width=2.5pt, red!85!black] (1.6, 2.4) -- (1.6, 1.1) 
            node[midway, right=3pt, font=\normalsize\bfseries] {$g$};
        \node[below=2pt, fill=white, inner sep=2pt, font=\footnotesize\bfseries] at (1.6, 0.8) {本物の重力加速度};
    \end{scope}

    % Giant Equivalence Symbol
    \node[font=\fontsize{28}{32}\bfseries, text=red!80!black] at (4.5, 2.3) {$\equiv$};
    \node[above=2pt, font=\small\bfseries, text=red!80!black] at (4.5, 2.9) {完全等価};

    % Subfigure 2: Accelerating Rocket in Deep Space
    \begin{scope}[xshift=5.8cm]
        \draw[thick, fill=yellow!12, draw=orange!60, rounded corners=5pt] (0, 0) rectangle (3.2, 4.4);
        \node[font=\normalsize\bfseries, text=orange!90!black] at (1.6, 4.8) {【加速系：宇宙船内】};
        
        % Rocket upward acceleration
        \draw[->, line width=3pt, purple!85!black] (1.6, 4.4) -- (1.6, 5.7) 
            node[above, font=\normalsize\bfseries, text=purple!85!black] {上向き推力加速 $\alpha = g$};
            
        % Suspended ball appearing to fall
        \fill[red!85!black] (1.6, 2.7) circle (4pt);
        \node[right=4pt, fill=white, inner sep=2pt, font=\scriptsize\bfseries] at (1.6, 2.7) {浮遊する球};
        \draw[->, line width=2.5pt, red!85!black] (1.6, 2.4) -- (1.6, 1.1) 
            node[midway, right=3pt, font=\normalsize\bfseries] {$g$};
        \node[below=2pt, fill=white, inner sep=2pt, font=\footnotesize\bfseries] at (1.6, 0.8) {慣性力（擬似重力）};
        
        % Deep space note
        \node[font=\scriptsize, text=gray!70!black] at (1.6, -0.5) {重力のない深宇宙};
    \end{scope}
    
    % Conclusion badge
    \node[align=left, fill=white, draw=gray!60, rounded corners=5pt, inner sep=5pt, font=\footnotesize, line width=0.8pt] 
        at (4.5, -1.3) {\textbf{【等価原理（Principle of Equivalence）の物理的帰結】}\\
        密閉された小部屋の中にいる観測者は、どんな物理実験を行っても\\
        「地球の重力場にいるのか」それとも「宇宙船が加速しているのか」を判別できない！};
\end{tikzpicture}""",
    r"アインシュタインの等価原理。一様な重力場と等加速度運動する乗り物の中の物理現象は完全に等価である。"),

    9: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Rotating Disk
    \draw[line width=1.8pt, fill=cyan!8, draw=teal!75] (0, 0) circle (3.0);
    
    % Center of disk
    \fill[black] (0, 0) circle (3.5pt);
    \node[below right=3pt, fill=white, inner sep=1.5pt, font=\small\bfseries] at (0, 0) {回転中心 $O$（静止点）};
    
    % Rotation angular velocity omega arrow
    \draw[->, line width=2.5pt, red!85!black] (2.1, 2.1) arc (45:85:3.0) 
        node[above=4pt, font=\normalsize\bfseries, text=red!85!black] {回転角速度 $\omega$};
        
    % Radial measuring rod (Perpendicular to motion -> No contraction!)
    \draw[|-|, line width=2pt, blue!85!black] (0, 0) -- (0, 2.8) 
        node[midway, left=4pt, fill=white, inner sep=2pt, font=\small\bfseries, text=blue!85!black] 
        {半径 $R$（運動に直交 $\implies$ 収縮なし：$R = R_0$）};
        
    % Tangential measuring rod on circumference (Along motion -> Lorentz Contracted!)
    \draw[line width=3pt, red!85!black] (2.9, -0.6) arc (-11:25:2.9);
    \node[right=8pt, align=left, fill=white, draw=red!50, rounded corners=3pt, inner sep=3pt, font=\footnotesize\bfseries, text=red!85!black] 
        at (2.9, 0.4) {周長方向の定規：\\速度 $v = R\omega$ で走行 $\implies$ ローレンツ収縮！};
        
    % Non-Euclidean Conclusion Box
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (0, -4.1) {\textbf{【ユークリッド幾何学の必然的崩壊】}\\
        ・周上の定規が縮むため、円周を測るのに「より多くの定規」が必要となる\\
        ・実測円周 $C > 2\pi R \implies \dfrac{\text{実測円周}}{\text{実測直径}} > \pi$ （円周率が $3.14\dots$ より大きくなる！）\\
        $\implies$ \textbf{加速度系や重力場における空間は「曲がった非ユークリッド幾何学」に従う！}};
\end{tikzpicture}""",
    r"回転円盤の思考実験。円周方向の定規のみが収縮するため、円周率が $\pi$ より大きくなり非ユークリッド幾何学が現れる。"),

    10: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Sun (Gravitational Lens)
    \shade[inner color=yellow!80!white, outer color=orange!95!black] (2.8, 1.2) circle (1.2);
    \node[font=\large\bfseries, text=black] at (2.8, 1.2) {太陽 $M$};
    \node[below=1.4cm, font=\scriptsize\bfseries, text=orange!90!black] at (2.8, 1.2) {質量による時空の窪み};
    
    % True Star Position
    \fill[blue!90!black] (-2.5, 3.8) circle (3.5pt);
    \node[above left=3pt, fill=white, inner sep=2pt, font=\small\bfseries, text=blue!90!black] 
        at (-2.5, 3.8) {恒星の真の位置 $S$};
        
    % Apparent Star Position
    \fill[purple!85!black] (-1.0, 4.6) circle (3pt);
    \node[above=3pt, fill=white, inner sep=2pt, font=\small\bfseries, text=purple!85!black] 
        at (-1.0, 4.6) {見かけの位置 $S'$（ズレて観測）};
        
    % Earth and Observer
    \draw[thick, fill=blue!30] (8.2, 0.4) circle (0.6);
    \node[font=\footnotesize\bfseries] at (8.2, 0.4) {地球};
    \fill[black] (7.7, 0.5) circle (2.5pt);
    \node[above=3pt, font=\scriptsize\bfseries] at (7.7, 0.5) {観測者};
    
    % Straight line of sight to apparent position (Dashed purple)
    \draw[thick, dashed, purple!80!black] (7.7, 0.5) -- (-1.0, 4.6);
    
    % Curved real ray of light (Solid red)
    \draw[line width=2.5pt, red!85!black, ->] (-2.5, 3.8) .. controls (2.3, 2.7) and (3.3, 2.7) .. (7.7, 0.5)
        node[midway, above=3pt, fill=white, inner sep=2pt, font=\footnotesize\bfseries, text=red!85!black] 
        {太陽の重力場で曲げられる光線};
        
    % Deflection angle theta annotation
    \draw[<->, line width=1.5pt, purple!85!black] (5.8, 1.3) arc (160:182:2.5);
    \node[right=4pt, fill=white, draw=purple!50, rounded corners=3pt, inner sep=3pt, font=\footnotesize\bfseries, text=purple!85!black] 
        at (6.0, 1.6) {偏向角 $\theta = \dfrac{4GM}{c^2 R} \approx 1.75''$};
        
    % Historical note
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=5pt, font=\footnotesize, line width=0.8pt] 
        at (2.8, -1.2) {\textbf{【1919年エディントン皆既日食観測による歴史的実証】}\\
        ニュートン力学の予言（$0.875''$）の正確に「2倍」曲がるというアインシュタインの予言が完全立証！};
\end{tikzpicture}""",
    r"重力場による光線の湾曲（重力レンズ効果）。太陽の質量が周囲の時空を歪め、背後の恒星光が曲げられて地球に届く。"),

    11: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Subfigure 1: Flat Euclidean Spacetime
    \begin{scope}[yshift=3.8cm]
        \draw[thick, fill=blue!6, draw=blue!50] (0, 0) -- (5.5, 0) -- (7.5, 2.0) -- (2.0, 2.0) -- cycle;
        % Euclidean Triangle
        \draw[line width=1.5pt, blue!85!black] (2.2, 0.4) -- (5.2, 0.4) -- (4.0, 1.6) -- cycle;
        \node[font=\footnotesize\bfseries, text=blue!85!black] at (3.8, 0.8) {内角の和 $= 180^\circ$};
        \node[above=4pt, font=\normalsize\bfseries, text=blue!90!black] at (3.7, 2.0) 
            {【物質のない平坦な時空（ユークリッド幾何学）】};
    \end{scope}

    % Subfigure 2: Warped Spacetime by Mass
    \begin{scope}[yshift=0cm]
        % Funnel gravity well
        \draw[thick, fill=orange!10, draw=orange!60] 
            (0, 0) .. controls (2.2, -1.8) and (3.3, -1.8) .. (5.5, 0)
            -- (7.5, 2.0) .. controls (5.3, 0.2) and (4.2, 0.2) .. (2.0, 2.0) -- cycle;
            
        % Grid lines representing curvature
        \draw[dashed, gray!60] (1.0, 0.5) .. controls (2.5, -1.0) and (3.5, -1.0) .. (5.0, 0.5);
        \draw[dashed, gray!60] (2.0, 1.2) .. controls (3.0, -0.4) and (4.0, -0.4) .. (6.0, 1.2);
        
        % Massive Star sinking into spacetime
        \shade[ball color=red!85!black] (3.6, -0.8) circle (0.6);
        \node[below=4pt, fill=white, inner sep=2pt, font=\small\bfseries, text=red!85!black] at (3.6, -1.5) {大質量天体 $M$};
        
        % Curved light geodesic
        \draw[line width=2pt, teal!85!black, ->] (0.5, 0.2) .. controls (2.5, -0.7) and (4.5, -0.7) .. (6.8, 1.5)
            node[midway, above=3pt, fill=white, inner sep=1.5pt, font=\scriptsize\bfseries] {測地線（最短軌道）};
            
        \node[above=4pt, font=\normalsize\bfseries, text=orange!90!black] at (3.7, 2.0) 
            {【質量が時空を歪めた湾曲時空（リーマン幾何学）】};
    \end{scope}

    % Wheeler's famous quote box
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (3.7, -2.6) {\textbf{【ジョン・ホイーラーによる一般相対論の要約】}\\
        「時空は物質にどのように動くかを命じ、物質は時空にどのように曲がるかを命じる」\\
        （Spacetime tells matter how to move; matter tells spacetime how to curve.）};
\end{tikzpicture}""",
    r"一般相対性理論の本質：物質とエネルギーが存在することで周囲の4次元時空連続体が歪み、重力として観測される。"),

    12: (r"""\begin{tikzpicture}[scale=1.05, >=Stealth, every node/.style={font=\small}]
    % Past Universe (Small sphere)
    \begin{scope}[xshift=0cm]
        \draw[line width=1.5pt, dashed, fill=blue!8, draw=blue!70] (0, 0) circle (1.5);
        \node[above=4pt, font=\normalsize\bfseries, text=blue!85!black] at (0, 1.6) {【過去の宇宙（狭い空間）】};
        
        \fill[red!85!black] (0.6, 0.5) circle (3pt);
        \node[above right=1pt, fill=white, inner sep=1.5pt, font=\scriptsize\bfseries] at (0.6, 0.5) {銀河 $A$};
        
        \fill[teal!85!black] (-0.5, -0.4) circle (3pt);
        \node[below left=1pt, fill=white, inner sep=1.5pt, font=\scriptsize\bfseries] at (-0.5, -0.4) {銀河 $B$};
        
        \draw[<->, thick, purple!80!black] (-0.35, -0.25) -- (0.45, 0.35) 
            node[midway, fill=white, inner sep=1.5pt, font=\scriptsize\bfseries] {距離 $d_0$};
    \end{scope}

    % Time Evolution Arrow
    \draw[->, line width=3pt, blue!75!black] (2.0, 0) -- (3.6, 0) 
        node[midway, above=3pt, font=\small\bfseries, text=blue!85!black] {宇宙膨張};
    \node[below=3pt, font=\scriptsize, text=gray!70!black] at (2.8, 0) {数十億年};

    % Present / Future Universe (Expanded sphere)
    \begin{scope}[xshift=6.5cm]
        \draw[line width=1.8pt, fill=purple!8, draw=purple!70] (0, 0) circle (2.8);
        \node[above=4pt, font=\normalsize\bfseries, text=purple!85!black] at (0, 2.9) {【現在の宇宙（膨張した空間）】};
        
        \fill[red!85!black] (1.3, 1.0) circle (3.5pt);
        \node[above right=1pt, fill=white, inner sep=1.5pt, font=\scriptsize\bfseries] at (1.3, 1.0) {銀河 $A$};
        
        \fill[teal!85!black] (-1.1, -0.9) circle (3.5pt);
        \node[below left=1pt, fill=white, inner sep=1.5pt, font=\scriptsize\bfseries] at (-1.1, -0.9) {銀河 $B$};
        
        \draw[<->, line width=1.2pt, purple!80!black] (-0.8, -0.65) -- (1.0, 0.75) 
            node[midway, fill=white, inner sep=2pt, font=\small\bfseries] {距離 $d = a(t) d_0 \gg d_0$};
    \end{scope}
    
    % Expansion Insight Box
    \node[align=left, fill=yellow!15, draw=orange!70, rounded corners=5pt, inner sep=6pt, font=\footnotesize, line width=0.8pt] 
        at (3.6, -3.8) {\textbf{【ハッブル＝ルメートルの法則と空間の膨張】}\\
        ・銀河が既存の空間の中を猛スピードで飛んで遠ざかっているのではない\\
        ・\textbf{銀河と銀河の間の「空間そのもの」が風船のように引き伸ばされている}\\
        ・アインシュタイン方程式が予測した「動的な膨張宇宙」は現代宇宙論の標準モデルとなった};
\end{tikzpicture}""",
    r"宇宙論的帰結。アインシュタイン方程式が導く動的宇宙と空間自体の膨張モデル。")
}
