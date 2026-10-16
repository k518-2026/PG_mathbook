# -*- coding: utf-8 -*-
"""
TikZ Figures and Captions for 12 Chapters of Einstein Relativity Intro
"""

FIGS = {
    1: (r"""\begin{tikzpicture}[scale=1.0, >=Stealth]
    % Coordinates and grid
    \draw[->, thick, gray!60] (-0.5,0) -- (6,0) node[right, black] {$x$ (空間)};
    \draw[->, thick, gray!60] (0,-0.5) -- (0,4) node[above, black] {$y$};
    \draw[step=1.0, gray!20, very thin] (-0.5,-0.5) grid (5.5,3.5);
    % Rigid body / Reference frame
    \node[draw, rectangle, rounded corners, fill=blue!10, draw=blue!70, thick, inner sep=4pt] at (1.5,2.5) {基準座標系 $K$};
    % Measuring rod
    \draw[|-|, ultra thick, red!80!black] (1,0.5) -- (4,0.5) node[midway, above, font=\small\bfseries] {基準剛体定規 ($L_0$)};
    % Event points
    \fill[red] (1,0.5) circle (2.5pt) node[below=2pt, font=\small] {$A (x_1, y_1)$};
    \fill[red] (4,0.5) circle (2.5pt) node[below=2pt, font=\small] {$B (x_2, y_2)$};
    % Annotation
    \node[align=left, fill=white, draw=gray!40, rounded corners, font=\footnotesize, inner sep=3pt] at (3.5, 2.2) {幾何学の命題：\\「2点間の距離は定規の\\目盛り数として実測される」};
\end{tikzpicture}""",
    r"ユークリッド幾何学の命題を物理的な「剛体定規」による目盛り計測として捉え直す座標系 $K$ の構造。"),

    2: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Embankment
    \draw[thick, fill=brown!20] (-1,-0.5) rectangle (7,0.2);
    \node at (3,-0.15) {\textbf{堤防（静止座標系 $K$）}};
    \node[draw, circle, fill=yellow!40, inner sep=2pt] (obsK) at (0.5, 0.7) {観測者 $M$};
    % Train
    \draw[thick, fill=blue!15, rounded corners] (1.5,1.2) rectangle (6.5,2.6);
    \node at (4,2.2) {\textbf{走行列車（運動系 $K'$）}};
    \draw[->, ultra thick, red!80!black] (6.5, 1.9) -- (7.8, 1.9) node[right] {速度 $v$};
    \node[draw, circle, fill=cyan!40, inner sep=2pt] (obsKp) at (3.5, 1.7) {観測者 $M'$};
    % Walker inside train
    \draw[->, thick, teal] (4.5, 1.6) -- (5.5, 1.6) node[midway, above, font=\scriptsize] {歩行 $w$};
    % Classical addition
    \node[align=left, fill=white, draw=gray!50, rounded corners, font=\footnotesize] at (3, 3.4) {ガリレイ変換の古典則：$W = v + w$\\しかし「光速 $c$」に対してこの単純加算は通用するのか？};
\end{tikzpicture}""",
    r"堤防の静止系 $K$ と一定速度 $v$ で走る列車系 $K'$ における運動の相対性と古典速度合成則。"),

    3: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Track and Light pulses
    \draw[thick, fill=gray!20] (-2,-0.2) rectangle (8,0.2);
    \node[draw, rectangle, fill=blue!10, thick, rounded corners, minimum width=8cm, minimum height=1.6cm] at (3,1.6) {};
    \node at (3, 2.2) {\textbf{高速列車（速度 $v \to$）}};
    % Light sources at A and B
    \fill[red] (-0.8, 0) circle (3pt) node[below=3pt] {落雷地点 $A$};
    \fill[red] (6.8, 0) circle (3pt) node[below=3pt] {落雷地点 $B$};
    \draw[decorate, decoration={snake, amplitude=2pt, segment length=5pt}, thick, orange!90!black, ->] (-0.7,0.4) -- (2.5,0.4) node[midway, above, font=\scriptsize] {光波 $c$};
    \draw[decorate, decoration={snake, amplitude=2pt, segment length=5pt}, thick, orange!90!black, ->] (6.7,0.4) -- (3.5,0.4) node[midway, above, font=\scriptsize] {光波 $c$};
    % Observers
    \node[draw, circle, fill=yellow!50, inner sep=2pt] at (3, 0) {$M$};
    \node[below=2pt, font=\scriptsize] at (3,-0.3) {堤防の中点 $M$（同時到達）};
    \node[draw, circle, fill=cyan!50, inner sep=2pt] at (3.8, 1.6) {$M'$};
    \node[above=2pt, font=\scriptsize] at (3.8, 2.0) {車内の中点 $M'$（$B$ の光に突進）};
    \draw[->, ultra thick, red] (4.2, 1.6) -- (5.0, 1.6) node[right, font=\scriptsize] {$v$};
\end{tikzpicture}""",
    r"列車と堤防の思考実験。堤防の中点 $M$ で同時の2つの落雷は、前進する車内の中点 $M'$ には同時に届かない。"),

    4: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Rest frame clock
    \begin{scope}[xshift=0cm]
        \draw[thick, fill=gray!10] (0,0) rectangle (2,3);
        \node at (1,3.3) {\textbf{静止系（固有時間 $\Delta t_0$）}};
        \fill[black] (1,0.3) circle (3pt) node[right, font=\scriptsize] {光源/検出器};
        \draw[ultra thick, blue!80!black] (0.3,2.7) -- (1.7,2.7) node[midway, above, font=\scriptsize] {鏡};
        \draw[decorate, decoration={snake, amplitude=2pt, segment length=6pt}, thick, red, ->] (0.9,0.4) -- (0.9,2.6);
        \draw[decorate, decoration={snake, amplitude=2pt, segment length=6pt}, thick, red, ->] (1.1,2.6) -- (1.1,0.4);
        \draw[<->, thick] (0.1,0.3) -- (0.1,2.7) node[midway, left] {$L$};
        \node[below=4pt, font=\footnotesize] at (1,0) {$\Delta t_0 = \dfrac{2L}{c}$};
    \end{scope}
    % Moving frame clock
    \begin{scope}[xshift=4.5cm]
        \draw[->, thick, gray!60] (-0.5,0) -- (5,0) node[right, black] {$x$};
        \node at (2,3.3) {\textbf{移動系（光が斜めに進む $\Delta t$）}};
        \fill[black] (0,0.3) circle (2.5pt);
        \draw[ultra thick, blue!80!black] (1.2,2.7) -- (2.6,2.7);
        \fill[black] (3.8,0.3) circle (2.5pt);
        \draw[dashed, red, thick] (0,0.3) -- (1.9,2.7) -- (3.8,0.3);
        \draw[->, thick, red] (0,0.3) -- (0.95,1.5);
        \draw[->, thick, red] (1.9,2.7) -- (2.85,1.5);
        \draw[<->, blue, thick] (0,-0.4) -- (3.8,-0.4) node[midway, below, font=\scriptsize] {$v \Delta t$};
        \node[align=left, fill=white, draw=gray!40, rounded corners, font=\scriptsize] at (2, 1.2) {三平方の定理：\\$\left(\frac{c\Delta t}{2}\right)^2 = L^2 + \left(\frac{v\Delta t}{2}\right)^2$};
    \end{scope}
\end{tikzpicture}""",
    r"光時計の思考実験。三平方の定理から時間の遅れ $\Delta t = \Delta t_0 / \sqrt{1 - v^2/c^2}$ が導かれる幾何学的構造。"),

    5: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Rest rod
    \node[anchor=east, font=\bfseries] at (-0.5,2.5) {静止時 $L_0$：};
    \draw[fill=blue!20, draw=blue!80, thick] (0,2.1) rectangle (6,2.9);
    \draw[|<->|, thick] (0,3.2) -- (6,3.2) node[midway, above] {固有長 $L_0$};
    % Moving rod
    \node[anchor=east, font=\bfseries] at (-0.5,0.7) {高速運動時 $L$：};
    \draw[fill=red!20, draw=red!80, thick] (1,0.3) rectangle (4.6,1.1);
    \draw[|<->|, thick] (1,-0.2) -- (4.6,-0.2) node[midway, below] {$L = L_0 \sqrt{1 - v^2/c^2}$};
    \draw[->, ultra thick, red!80!black] (4.7,0.7) -- (6.2,0.7) node[right] {速度 $v$};
    % Contraction note
    \node[align=center, fill=yellow!10, draw=orange!60, rounded corners, font=\footnotesize] at (7.5, 2.0) {ローレンツ収縮：\\運動方向のみ縮み、\\垂直方向の幅は不変};
\end{tikzpicture}""",
    r"進行方向に沿って剛体の長さが縮むローレンツ収縮の幾何学的イメージ。"),

    6: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Mass increase curve
    \draw[->, thick] (0,0) -- (6.5,0) node[right] {速度 $v$};
    \draw[->, thick] (0,0) -- (0,4.2) node[above] {相対論的質量 $m(v)$ / エネルギー $E$};
    \draw[dashed, red, thick] (5.5,0) -- (5.5,4.0) node[above, font=\footnotesize] {光速壁 $c$};
    \draw[domain=0:5.2, smooth, variable=\x, ultra thick, blue!80!black] plot ({\x}, {1.0 / sqrt(1 - (\x/5.5)*(\x/5.5))});
    \fill[black] (0,1.0) circle (2.5pt) node[left, font=\footnotesize] {静止質量 $m_0$ ($E_0 = m_0 c^2$)};
    \node[align=left, fill=white, draw=gray!40, rounded corners, font=\footnotesize] at (2.8, 3.2) {速度が光速に近づくと\\質量・エネルギーは無限大に発散：\\物体は光速を超えられない};
\end{tikzpicture}""",
    r"質量とエネルギーの等価性 $E = mc^2$ と、光速 $c$ へ近づくにつれて無限大へ発散する相対論的質量。"),

    7: (r"""\begin{tikzpicture}[scale=1.0, >=Stealth]
    % Coordinate axes
    \draw[->, thick] (-3,0) -- (3,0) node[right] {$x$ (空間)};
    \draw[->, thick] (0,-0.5) -- (0,3.5) node[above] {$ct$ (時間)};
    % Light cone
    \fill[yellow!20, opacity=0.7] (0,0) -- (3,3) -- (-3,3) -- cycle;
    \draw[ultra thick, orange!90!black] (-3,3) -- (0,0) -- (3,3);
    \node[above, orange!90!black, font=\footnotesize] at (2.4, 2.5) {光世界線 ($x = ct$)};
    \node[above, orange!90!black, font=\footnotesize] at (-2.4, 2.5) {光世界線 ($x = -ct$)};
    % Worldline of particle
    \draw[ultra thick, blue!80!black] (0,0) .. controls (0.5,1.2) and (-0.3,2.0) .. (0.8,3.2) node[above, font=\footnotesize] {物質の世界線 ($v < c$)};
    % Spacetime invariant
    \node[align=center, fill=white, draw=gray!50, rounded corners, font=\footnotesize] at (0, 1.8) {絶対的不変間隔：\\$s^2 = c^2 t^2 - x^2 > 0$\\（未来光円錐の内部）};
\end{tikzpicture}""",
    r"ミンコフスキーの4次元時空と光円錐（Light Cone）。すべての因果律は光円錐の内部に制限される。"),

    8: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Earth gravitational field
    \begin{scope}[xshift=0cm]
        \draw[thick, fill=blue!10] (0,0) rectangle (2.5,3.2);
        \node at (1.25,3.5) {\textbf{重力場（地上）}};
        \fill[gray!40] (-0.3,-0.2) rectangle (2.8,0);
        \node at (1.25,-0.4) {地球表面};
        \fill[red] (1.25,1.8) circle (3pt) node[right, font=\footnotesize] {自由落下する球};
        \draw[->, ultra thick, red] (1.25,1.7) -- (1.25,0.7) node[midway, right, font=\footnotesize] {$g$};
        \node[font=\footnotesize] at (1.25, 0.4) {重力加速度};
    \end{scope}
    % Equal sign
    \node[font=\Huge\bfseries] at (3.5, 1.8) {$\equiv$};
    % Accelerating rocket
    \begin{scope}[xshift=4.5cm]
        \draw[thick, fill=yellow!10] (0,0) rectangle (2.5,3.2);
        \node at (1.25,3.5) {\textbf{無重力空間の加速ロケット}};
        \draw[->, ultra thick, purple] (1.25,3.2) -- (1.25,4.2) node[above, font=\footnotesize] {上向き加速 $\alpha = g$};
        \fill[red] (1.25,1.8) circle (3pt) node[right, font=\footnotesize] {静止する球};
        \draw[->, ultra thick, red] (1.25,1.7) -- (1.25,0.7) node[midway, right, font=\footnotesize] {見かけの落下 $g$};
        \node[font=\footnotesize] at (1.25, 0.4) {慣性力（擬似重力）};
    \end{scope}
\end{tikzpicture}""",
    r"アインシュタインの等価原理。一様な重力場と等加速度運動する乗り物の中の物理現象は完全に等価である。"),

    9: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Rotating disk
    \draw[thick, fill=cyan!10] (0,0) circle (2.5);
    \draw[->, ultra thick, red] (1.8, 1.8) arc (45:85:2.5) node[above, font=\footnotesize] {角速度 $\omega$};
    \fill[black] (0,0) circle (2pt) node[below=2pt, font=\footnotesize] {中心 $O$（静止）};
    % Radial rod (no contraction)
    \draw[|-|, thick, blue] (0,0) -- (0,2.3) node[midway, left, font=\scriptsize] {半径 $R$（収縮なし）};
    % Circumference rods (Lorentz contracted)
    \draw[ultra thick, red!80!black] (2.3, -0.4) arc (-10:30:2.3) node[midway, right, font=\scriptsize] {周長方向（速度 $v = R\omega$ で収縮）};
    % Non-euclidean conclusion
    \node[align=left, fill=white, draw=gray!50, rounded corners, font=\footnotesize] at (0, -3.2) {円周上の定規のみがローレンツ収縮するため：\\$\dfrac{\text{測定円周}}{\text{測定直径}} > \pi$ （ユークリッド幾何学の崩壊！）};
\end{tikzpicture}""",
    r"回転円盤の思考実験。円周方向の定規のみが収縮するため、円周率が $\pi$ より大きくなり非ユークリッド幾何学が現れる。"),

    10: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Massive star / Sun
    \shade[inner color=yellow!80!white, outer color=orange!90!black] (2,1) circle (0.9);
    \node at (2,1) {\textbf{太陽 $M$}};
    % Distant star real position
    \fill[blue] (-2,3) circle (2.5pt) node[above left, font=\footnotesize] {恒星の真の位置};
    % Deflected light path
    \draw[thick, blue, dashed] (-2,3) -- (5.5,1.9) node[right, font=\footnotesize] {見かけの位置};
    \draw[ultra thick, red, ->] (-2,3) .. controls (1.5,1.9) and (2.5,1.9) .. (5,0.5) node[right, black, font=\footnotesize] {地球の観測者};
    % Deflection angle theta
    \draw[<->, thick, purple] (4.5,1.0) arc (-10:20:1.5) node[midway, right, font=\footnotesize] {偏向角 $\theta = \dfrac{4GM}{c^2 R}$};
\end{tikzpicture}""",
    r"重力場による光線の湾曲（重力レンズ効果）。太陽の質量が周囲の時空を歪め、背後の恒星光が曲げられて地球に届く。"),

    11: (r"""\begin{tikzpicture}[scale=0.9, >=Stealth]
    % Flat vs Curved sheet
    \begin{scope}[yshift=2.5cm]
        \draw[thick, fill=blue!5] (0,0) -- (4,0) -- (5.5,1.5) -- (1.5,1.5) -- cycle;
        \draw[thick, red] (1.2,0.5) -- (3.8,0.5) -- (2.5,1.2) -- cycle;
        \node at (2.8, 1.8) {\textbf{平坦な空間（ユークリッド幾何学：内角の和 $= 180^\circ$）}};
    \end{scope}
    \begin{scope}[yshift=0cm]
        % Warped funnel
        \draw[thick, fill=orange!10] (0,0) .. controls (2,-1.5) and (3,-1.5) .. (5,0)
              -- (6,1.2) .. controls (3,0.2) and (2,0.2) .. (1,1.2) -- cycle;
        \shade[ball color=red!80!black] (2.7,-0.7) circle (0.4) node[below=8pt, font=\scriptsize] {大質量天体};
        \node at (3, -1.8) {\textbf{曲がった時空（リーマン幾何学：重力とは時空の歪みそのもの）}};
    \end{scope}
\end{tikzpicture}""",
    r"一般相対性理論の本質：物質とエネルギーが存在することで周囲の4次元時空連続体が歪み、重力として観測される。"),

    12: (r"""\begin{tikzpicture}[scale=0.95, >=Stealth]
    % Expanding balloon / universe
    \draw[thick, dashed, fill=blue!5] (0,0) circle (1.2);
    \fill[red] (0.5,0.5) circle (2pt) node[right, font=\scriptsize] {銀河A};
    \fill[red] (-0.4,-0.3) circle (2pt) node[left, font=\scriptsize] {銀河B};
    \draw[thick, fill=purple!5] (4.5,0) circle (2.2);
    \fill[red] (5.4,0.9) circle (2.5pt) node[right, font=\scriptsize] {銀河A};
    \fill[red] (3.8,-0.6) circle (2.5pt) node[left, font=\scriptsize] {銀河B};
    \draw[->, ultra thick, blue] (1.5,0) -- (2.0,0) node[midway, above, font=\scriptsize] {時間発展};
    % Annotation
    \node[align=left, fill=white, draw=gray!50, rounded corners, font=\footnotesize] at (2.5,-2.8) {宇宙膨張（ハッブルの法則）：\\銀河が空間を動くのではなく、\\「空間そのものが風船のように膨張している」};
\end{tikzpicture}""",
    r"宇宙論的帰結。アインシュタイン方程式が導く動的宇宙と空間自体の膨張モデル。")
}
