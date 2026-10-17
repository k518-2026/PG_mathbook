# -*- coding: utf-8 -*-
"""
Map of Gutenberg image tokens (image001 - image060) to LaTeX expressions and figures.
"""

IMAGE_MAP = {
    # Sec IX
    "image001": r"""\begin{center}
\begin{tikzpicture}[scale=0.9, thick]
  \draw[->] (-4,0) -- (4,0) node[right] {線路（基準系 $K$）};
  \filldraw (-3,0) circle (2pt) node[below] {$A$};
  \filldraw (3,0) circle (2pt) node[below] {$B$};
  \filldraw (0,0) circle (2pt) node[below] {$M$};
  \draw[rounded corners, fill=gray!15] (-3, 0.8) rectangle (3, 1.6);
  \node at (0, 1.2) {列車（基準系 $K'$） $\longrightarrow v$};
  \filldraw (0, 0.8) circle (2pt) node[above] {$M'$};
\end{tikzpicture}
\end{center}""",

    # Sec XI (Fig. 2 and Lorentz equations)
    "image002": r"""\begin{center}
\begin{tikzpicture}[scale=0.8, >=stealth, thick]
  % System K
  \draw[->] (0,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,0) -- (0,3) node[above] {$y$};
  \draw[->] (0,0) -- (-1.5,-1.5) node[below left] {$z$};
  \node at (-0.3,0.3) {$K$};
  % System K'
  \draw[->, shift={(4.5,0)}] (0,0) -- (3,0) node[right] {$x'$};
  \draw[->, shift={(4.5,0)}] (0,0) -- (0,3) node[above] {$y'$};
  \draw[->, shift={(4.5,0)}] (0,0) -- (-1.5,-1.5) node[below left] {$z'$};
  \draw[->, very thick, blue] (5.2, 1.5) -- (6.5, 1.5) node[right] {$v$};
  \node at (4.2,0.3) {$K'$};
\end{tikzpicture}\\[1mm]
{\small 図 2：互いに平行な空間配置を持つ二つの慣性座標系 $K$ と $K'$}
\end{center}""",

    "image003": r"\[ x' = \frac{x - vt}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image004": r"\[ t' = \frac{t - \frac{v}{c^2}x}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image005": r"\[ x' = ct \sqrt{\frac{1 - \frac{v}{c}}{1 + \frac{v}{c}}}, \quad t' = t \sqrt{\frac{1 - \frac{v}{c}}{1 + \frac{v}{c}}} \]",

    # Sec XII
    "image006": r"\[ x = 0 \quad \text{および} \quad x = \sqrt{1 - \frac{v^2}{c^2}} \]",
    "image007": r"\[ \sqrt{1 - \frac{v^2}{c^2}} \]",
    "image008": r"\[ \sqrt{1 - \frac{v^2}{c^2}} \]",
    "image009": r"\[ \sqrt{1 - 1} = 0 \]",
    "image010": r"\[ \sqrt{1 - \frac{v^2}{c^2}} \]",
    "image011": r"\[ t = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image012": r"\[ \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} \]",

    # Sec XIII
    "image013": r"\[ w = \frac{v + w'}{1 + \frac{v w'}{c^2}} \]",
    "image014": r"""\begin{center}
\begin{tikzpicture}[scale=0.9, thick]
  \draw[fill=cyan!15] (-3, -0.4) rectangle (3, 0.4);
  \node at (0,0) {管 $T$ 内を流れる液体（速度 $v \longrightarrow$）};
  \draw[->, red, very thick] (-4, 0) -- (-3, 0) node[midway, above] {光信号};
\end{tikzpicture}\\[1mm]
{\small 図 3：フィゾーの実験の概念図}
\end{center}""",
    "image015": r"\[ w = \frac{c}{n} + v\left(1 - \frac{1}{n^2}\right) \]",
    "image016": r"\[ n = \frac{c}{w'} \]",
    "image017": r"\[ \frac{v w'}{c^2} \]",
    "image018": r"\[ w = (w' + v)\left(1 - \frac{v w'}{c^2}\right) \]",
    "image019": r"\[ w = w' + v\left(1 - \frac{w'^2}{c^2}\right) \]",

    # Sec XV
    "image020": r"\[ \frac{1}{2} m v^2 \]",
    "image021": r"\[ \frac{m c^2}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image022": r"\[ m c^2 + \frac{1}{2} m v^2 + \frac{3}{8} m \frac{v^4}{c^2} + \dots \]",
    "image023": r"\[ \frac{v}{c} \]",
    "image024": r"\[ \frac{E_0}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image025": r"\[ \frac{(m + \frac{E_0}{c^2}) c^2}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image026": r"\[ m + \frac{E_0}{c^2} \]",
    "image027": r"\[ \frac{E_0}{c^2} \]",
    "image028": r"\[ (m + \frac{E}{c^2}) c^2 \]",

    # Sec XVI
    "image029": r"\[ \sqrt{1 - \frac{v^2}{c^2}} \]",

    # Sec XVII
    "image030": r"\[ \Delta t' = \frac{- \frac{v}{c^2} \Delta x}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image031": r"\[ x_4 = i c t \quad (i = \sqrt{-1}) \]",

    # Sec XIX
    "image032": r"\[ (\text{重力質量}) = (\text{慣性質量}) \]",

    # Sec XXV
    "image033": r"\[ ds^2 = g_{11} du^2 + 2 g_{12} du\, dv + g_{22} dv^2 \]",

    # Sec XXVI
    "image034": r"\[ ds^2 = dx_1^2 + dx_2^2 + dx_3^2 + dx_4^2 \]",
    "image035": r"\[ x_4 = i c t \]",

    # Sec XXXI
    "image036": r"\[ 2\pi R \sin\left(\frac{r}{R}\right) \]",

    # Sec XXXII
    "image037": r"\[ R^2 = \frac{2}{\kappa \rho} \]",

    # App I
    "image038": r"\[ a = \frac{\lambda + \mu}{2}, \quad b = \frac{\lambda - \mu}{2} \]",
    "image039": r"\[ x' = ax - bct, \quad ct' = act - bx \]",
    "image040": r"\[ x = \frac{bc}{a} t \]",
    "image041": r"\[ v = \frac{bc}{a} \]",
    "image042": r"\[ a^2 - b^2 = 1 \]",
    "image043": r"\[ \Delta x = \frac{1}{a} \]",
    "image044": r"\[ \Delta x' = a \left(1 - \frac{v^2}{c^2}\right) \]",
    "image045": r"\[ a = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image046": r"\[ b = \frac{\frac{v}{c}}{\sqrt{1 - \frac{v^2}{c^2}}} \]",
    "image047": r"\[ x'^2 - c^2 t'^2 = x^2 - c^2 t^2 \]",
    "image048": r"\[ y' = y, \quad z' = z \]",
    "image049": r"\[ x^2 + y^2 + z^2 - c^2 t^2 = 0 \]",

    # App II
    "image050": r"\[ x_1'^2 + x_2'^2 + x_3'^2 + x_4'^2 = x_1^2 + x_2^2 + x_3^2 + x_4^2 \]",

    # App III
    "image051": r"\[ \Delta \sigma = \frac{24\pi^3 a^2}{T^2 c^2 (1 - e^2)} \]",
    "image052": r"\[ \alpha = \frac{4 G M}{c^2 \Delta} = \frac{1.75''}{\Delta} \]",
    "image053": r"\[ \alpha = \frac{4 K M}{c^2 \Delta} \]",
    "image054": r"""\begin{center}
\begin{tabular}{lrr}
\toprule
星の番号 & 観測された偏角（秒） & 計算された偏角（秒） \\
\midrule
Star 5  & $-0.19$ & $-0.22$ \\
Star 4  & $+0.29$ & $+0.31$ \\
Star 3  & $+0.11$ & $+0.10$ \\
Star 6  & $+0.20$ & $+0.12$ \\
Star 10 & $+0.10$ & $+0.04$ \\
Star 2  & $-0.08$ & $+0.09$ \\
\bottomrule
\end{tabular}
\end{center}""",
    "image055": r"\[ \nu = \nu_0 \sqrt{1 - \frac{v^2}{c^2}} \]",
    "image056": r"\[ \nu = \nu_0 \left(1 - \frac{v^2}{2c^2}\right) \]",
    "image057": r"\[ \nu = \nu_0 \left(1 + \frac{\phi}{c^2}\right) \]",
    "image058": r"\[ \phi = -\frac{v^2}{2} = -\frac{r^2 \omega^2}{2} \]",
    "image059": r"\[ \frac{\nu_1 - \nu_2}{\nu_0} = \frac{\phi_1 - \phi_2}{c^2} \]",
    "image060": r"\[ \frac{\Delta \nu}{\nu_0} = -\frac{G M}{c^2 R} \]"
}
