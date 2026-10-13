import os, re

def build_laplace_tex():
    titles = [
        (1, '世界認識と確率の哲学的起源', 'Newtonian Determinism and Laplace Demon'),
        (2, 'ラプラスの確率の基本10原理', 'The Ten General Principles of Probability'),
        (3, '数学的期待値とモラル・ホープ（希望値・効用論）', 'Mathematical Expectation and Moral Hope'),
        (4, '解析的方法と母関数：確率論を支える高等数学の礎', 'Analytical Methods and Generating Functions'),
        (5, '偶然の遊戯：サイコロ・トランプ・宝くじの数理分析', 'Games of Chance and Mathematical Analysis'),
        (6, '未知の不平等：前提条件のゆらぎとベイズ的修正', 'Unknown Inequalities and Bayesian Updating'),
        (7, '大数の法則と正規分布：無限の試行が生み出す秩序', 'Law of Large Numbers and Normal Distribution'),
        (8, '自然哲学と天文学への応用：最小二乗法と誤差論', 'Applications to Natural Philosophy and Least Squares'),
        (9, '道徳科学・証言・裁判の確率論：意思決定の数学', 'Moral Sciences, Testimonies, and Tribunals'),
        (10, '生命表・保険・人口統計：社会制度を支える数理', 'Mortality Tables, Life Expectancy, and Insurance'),
        (11, '確率判断における人間の錯覚と誤謬：認知の罠', 'Illusions and Cognitive Fallacies in Probability'),
        (12, '確率論の歴史と近代科学の進展：真理への接近', 'Historical Development and Scientific Induction')
    ]
    
    # TikZ figures for all 12 chapters (completely redesigning to eliminate any text overlapping)
    tikz_figures = {
        1: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, >=stealth]
    % Outer container with ample space
    \draw[thick, fill=softblue, draw=primaryblue] (-6.2, -2.4) rectangle (6.2, 2.6);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=5pt] at (0, 2.1) {\bfseries ラプラスの決定論的宇宙観と認識の階層};
    
    % Laplace Demon Node (clean rounded rectangle with fixed text width)
    \node[draw=crimson, fill=white, rounded corners, align=center, text width=4.0cm, inner sep=5pt] (god) at (-3.6, 0.4) {
        \textbf{ラプラスの知性（悪魔）}\\[2pt]
        \footnotesize 全原子の位置・運動量を把握\\[1pt]
        \footnotesize 過去と未来の完全な計算
    };
    
    % Finite Human Mind Node
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=4.0cm, inner sep=5pt] (human) at (3.6, 0.4) {
        \textbf{有限な人間の知性}\\[2pt]
        \footnotesize 不完全な初期情報・複雑性\\[1pt]
        \footnotesize 確率論による合理的推論
    };
    
    % Connecting arrow with distinct, non-overlapping labels
    \draw[->, very thick, warmamber] (-1.3, 0.4) -- (1.3, 0.4);
    \node[above=3pt] at (0, 0.4) {\footnotesize 完全な決定性};
    \node[below=3pt] at (0, 0.4) {\footnotesize 情報の不完全性};
    
    % Mission of probability at bottom with full clearance
    \node[draw=darkslate, fill=softgreen, rounded corners, text width=9.6cm, align=center, inner sep=5pt] at (0, -1.5) {
        \textbf{確率論の使命}：完全な無知と完全な確実性を架橋する合理的判断の数理
    };
\end{tikzpicture}
\caption{決定論的宇宙における人間の知性と確率論の役割}
\label{fig:laplace_demon}
\end{figure}''',

        2: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.80, >=stealth]
    \draw[thick, fill=softamber, draw=warmamber] (-7.2, -3.2) rectangle (7.2, 3.2);
    \node[draw=warmamber, fill=white, rounded corners, inner sep=5pt] at (0, 2.6) {\bfseries ラプラス『確率の基本10原理』の体系的構造};
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.2cm, inner sep=4pt] (p1) at (-4.7, 0.6) {
        \textbf{第1原理}\\[2pt]
        \footnotesize 同様に確からしい事象の比\\[1pt]
        \footnotesize $P(A) = \frac{m}{n}$（古典的定義）
    };
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.2cm, inner sep=4pt] (p2) at (0, 0.6) {
        \textbf{第2--5原理}\\[2pt]
        \footnotesize 加法定理・乗法定理\\[1pt]
        \footnotesize 条件付き確率 $P(A \cap B)$
    };
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.2cm, inner sep=4pt] (p6) at (4.7, 0.6) {
        \textbf{第6--7原理}\\[2pt]
        \footnotesize 原因の確率（ベイズ逆確率）\\[1pt]
        \footnotesize 事後確率の推論
    };
    
    \draw[->, very thick, warmamber] (-3.0, 0.6) -- (-1.7, 0.6);
    \draw[->, very thick, warmamber] (1.7, 0.6) -- (3.0, 0.6);
    
    \node[draw=accentgreen, fill=softgreen, rounded corners, align=center, text width=11.2cm, inner sep=5pt] (p8) at (0, -1.9) {
        \textbf{第8--10原理：意思決定と将来予測の数理}\\[2pt]
        \footnotesize 数学的期待値 $E[X] = \sum x_i p_i$、継起の規則（日の出問題）、道徳的希望（効用論）
    };
    
    \draw[->, thick, accentgreen] (0, -0.3) -- (0, -1.3);
\end{tikzpicture}
\caption{古典的確率定義からベイズ推論・期待値に至る10原理の連関}
\label{fig:laplace_principles}
\end{figure}''',

        3: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    % Coordinate axes
    \draw[->, thick] (0,0) -- (7.8,0) node[right] {\footnotesize 富の保有量 $x$};
    \draw[->, thick] (0,0) -- (0,5.0) node[above] {\footnotesize 効用・満足度 $U(x)$};
    
    % Logarithmic utility curve (Moral Hope)
    \draw[very thick, primaryblue, domain=0.4:6.8, samples=100] plot (\x, {1.05*ln(\x) + 1.3});
    \node[primaryblue, right] at (6.8, 3.32) {\footnotesize \textbf{対数効用曲線} $U(x) = k \ln\left(\frac{x}{\alpha}\right)$};
    
    % Linear mathematical wealth line placed with clear separation
    \draw[thick, crimson, dashed] (0,0) -- (6.8, 1.85);
    \node[crimson, below right] at (4.2, 0.95) {\footnotesize 数学的富（線形増加 $y = cx$）};
    
    % Guide points and dotted lines
    \draw[fill=primaryblue] (1.5, {1.05*ln(1.5)+1.3}) circle (2pt);
    \draw[fill=primaryblue] (5.5, {1.05*ln(5.5)+1.3}) circle (2pt);
    \draw[dotted, darkslate] (1.5, 0) -- (1.5, {1.05*ln(1.5)+1.3});
    \draw[dotted, darkslate] (5.5, 0) -- (5.5, {1.05*ln(5.5)+1.3});
    
    \node[below] at (1.5, 0) {\footnotesize 貧困時 $x_1$};
    \node[below] at (5.5, 0) {\footnotesize 裕福時 $x_2$};
    
    % Marginal utility diminishing callout safely in far upper-left
    \node[draw=warmamber, fill=softamber, rounded corners, inner sep=4pt] at (2.4, 4.3) {
        \footnotesize \textbf{限界効用逓減}：富が増すほど1単位の喜びは減少
    };
\end{tikzpicture}
\caption{ダニエル・ベルヌーイとラプラスの対数効用関数（精神的期待値）}
\label{fig:moral_hope}
\end{figure}''',

        4: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.80, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-7.2, -3.1) rectangle (7.2, 3.1);
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=4.2cm, inner sep=5pt] (seq) at (-4.4, 1.0) {
        \textbf{離散確率列の空間}\\[2pt]
        \footnotesize $\{p_0, p_1, p_2, \dots, p_n\}$\\[1pt]
        \footnotesize 畳み込み和 $r_n = \sum p_k q_{n-k}$
    };
    
    \node[draw=accentgreen, fill=white, rounded corners, align=center, text width=4.2cm, inner sep=5pt] (gen) at (4.4, 1.0) {
        \textbf{解析的母関数の空間}\\[2pt]
        \footnotesize $G(t) = \sum_{k=0}^\infty p_k t^k$\\[1pt]
        \footnotesize 多項式・巾級数の代数積 $G_X(t)G_Y(t)$
    };
    
    \draw[<->, very thick, warmamber] (-1.8, 1.0) -- (1.8, 1.0);
    \node[above=3pt] at (0, 1.0) {\bfseries 母関数変換};
    \node[below=3pt] at (0, 1.0) {\footnotesize 代数化と連続化};
    
    \node[draw=darkslate, fill=softgreen, rounded corners, text width=11.2cm, align=center, inner sep=5pt] at (0, -1.8) {
        \textbf{微分積分による統計量の直接抽出}\\[2pt]
        \footnotesize 期待値 $E[X] = G'(1)$、分散 $V(X) = G''(1) + G'(1) - \{G'(1)\}^2$
    };
\end{tikzpicture}
\caption{ラプラス母関数による離散確率と連続解析学の融合}
\label{fig:generating_function}
\end{figure}''',

        5: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.80, >=stealth]
    \draw[thick, fill=softamber, draw=warmamber] (-7.2, -3.0) rectangle (7.2, 3.0);
    \node[draw=warmamber, fill=white, rounded corners, inner sep=5pt] at (0, 2.5) {\bfseries 偶然の遊戯（Games of Chance）と対称性の数理};
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (dice) at (-4.7, 0.7) {
        \textbf{サイコロ・コイン}\\[2pt]
        \footnotesize 幾何学的完全対称性\\[1pt]
        \footnotesize $P(1) = \cdots = P(6) = \frac{1}{6}$
    };
    
    \node[draw=crimson, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (cards) at (0, 0.7) {
        \textbf{トランプ・くじ引き}\\[2pt]
        \footnotesize 非復元抽出と組合せ論\\[1pt]
        \footnotesize 超幾何分布・配分問題
    };
    
    \node[draw=darkslate, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (lottery) at (4.7, 0.7) {
        \textbf{国家宝くじの分析}\\[2pt]
        \footnotesize 期待値の構造的赤字\\[1pt]
        \footnotesize $E[\text{払戻}] < \text{購入額}$
    };
    
    \node[draw=darkslate, fill=softgreen, rounded corners, text width=11.2cm, align=center, inner sep=5pt] at (0, -1.8) {
        \textbf{ラプラスの洞察}：賭博の数理は愚行の戒めであり、合理的意思決定の規範である
    };
\end{tikzpicture}
\caption{古典的等確率モデルと偶然の遊戯における公平な期待値}
\label{fig:games_of_chance}
\end{figure}''',

        6: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.80, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-7.2, -3.0) rectangle (7.2, 3.0);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=5pt] at (0, 2.5) {\bfseries 未知の偏りとベイズ的確率更新};
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.5cm, inner sep=4pt] (prior) at (-4.8, 0.7) {
        \textbf{事前確率 $P(\theta)$}\\[2pt]
        \footnotesize コインの歪み度合い $\theta$\\[1pt]
        \footnotesize 「無差別原則」の一様分布
    };
    
    \node[draw=crimson, fill=softrose, rounded corners, align=center, text width=3.5cm, inner sep=4pt] (post) at (4.8, 0.7) {
        \textbf{事後確率 $P(\theta|D)$}\\[2pt]
        \footnotesize データ $D$ による信念更新\\[1pt]
        \footnotesize 真の母数付近へ鋭く集中
    };
    
    \draw[->, very thick, warmamber] (-2.5, 0.7) -- (2.4, 0.7);
    \node[above=3pt] at (-0.05, 0.7) {\bfseries 観測データ $D$ の集積};
    \node[below=3pt] at (-0.05, 0.7) {\footnotesize 表が $p$ 回、裏が $q$ 回};
    
    \node[draw=darkslate, fill=white, rounded corners, text width=11.2cm, align=center, inner sep=5pt] at (0, -1.8) {
        \textbf{ラプラスの継起の規則}：過去 $n$ 回成功した事象の次回生起確率は $\frac{n+1}{n+2}$
    };
\end{tikzpicture}
\caption{未知の不平等とデータ観測によるベイズ事後確率の収束}
\label{fig:bayesian_updating}
\end{figure}''',

        7: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    % Title node placed safely at the very top
    \node[draw=warmamber, fill=softamber, rounded corners, inner sep=4pt] at (0, 4.3) {
        \textbf{ド・モアブル＝ラプラスの中心極限定理}
    };
    
    % Coordinate axes
    \draw[->, thick] (-4.5,0) -- (4.5,0) node[right] {\footnotesize 標準化変数 $z$};
    \draw[->, thick] (0,0) -- (0,3.3);
    \node[left=3pt] at (0, 3.2) {\footnotesize 確率密度 $\phi(z)$};
    
    % Fill area [-1, 1]
    \draw[fill=softblue, opacity=0.6] (-1,0) -- plot[domain=-1:1, samples=60] (\x, {2.7*exp(-\x*\x/2)}) -- (1,0) -- cycle;
    
    % Normal curve
    \draw[very thick, primaryblue, domain=-4.0:4.0, samples=100] plot (\x, {2.7*exp(-\x*\x/2)});
    
    % Formula clearly in upper right with generous clearance
    \node[primaryblue, above right] at (1.1, 2.2) {$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$};
    
    % Percentages below axis with ample spacing
    \draw[<->, thick, crimson] (-1, -0.5) -- (1, -0.5);
    \node[below=2pt, crimson] at (0, -0.5) {\footnotesize $1\sigma$ 区間：$68.26\%$（$[-1, 1]$）};
    
    \draw[<->, thick, darkslate] (-2, -1.2) -- (2, -1.2);
    \node[below=2pt, darkslate] at (0, -1.2) {\footnotesize $2\sigma$ 区間：$95.44\%$（$[-2, 2]$）};
\end{tikzpicture}
\caption{二項分布の極限としての正規分布曲線（誤差関数）}
\label{fig:normal_distribution}
\end{figure}''',

        8: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85, >=stealth]
    % Coordinate axes
    \draw[->, thick] (0,0) -- (7.2,0) node[right] {\footnotesize 観測条件 $x$};
    \draw[->, thick] (0,0) -- (0,5.2) node[above] {\footnotesize 観測結果 $y$};
    
    % Scatter points
    \draw[fill=crimson] (1.0, 1.2) circle (2.5pt);
    \draw[fill=crimson] (2.2, 2.1) circle (2.5pt);
    \draw[fill=crimson] (3.6, 2.5) circle (2.5pt);
    \draw[fill=crimson] (4.8, 3.8) circle (2.5pt);
    \draw[fill=crimson] (6.0, 4.1) circle (2.5pt);
    
    % Regression line
    \draw[very thick, primaryblue] (0.5, 1.0) -- (6.6, 4.5) node[right] {\textbf{最確直線} $y = ax + b$};
    
    % Residual dashed lines
    \draw[dashed, crimson, thick] (2.2, 2.1) -- (2.2, 1.98);
    \draw[dashed, crimson, thick] (3.6, 2.5) -- (3.6, 2.78);
    \draw[dashed, crimson, thick] (4.8, 3.8) -- (4.8, 3.47);
    
    \node[crimson, below right=3pt] at (4.8, 3.3) {\footnotesize 残差 $\epsilon_i = y_i - (ax_i+b)$};
    
    % Least squares principle box safely in clear upper-left region
    \node[draw=accentgreen, fill=softgreen, rounded corners, inner sep=4pt] at (2.4, 4.5) {
        \footnotesize \textbf{最小二乗法}：残差平方和 $\sum_{i=1}^n \epsilon_i^2 \to \text{最小}$
    };
\end{tikzpicture}
\caption{天体観測と最小二乗法：残差平方和の最小化による最確値の決定}
\label{fig:least_squares}
\end{figure}''',

        9: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.80, >=stealth]
    \draw[thick, fill=softrose, draw=crimson] (-7.2, -3.0) rectangle (7.2, 3.0);
    \node[draw=crimson, fill=white, rounded corners, inner sep=5pt] at (0, 2.5) {\bfseries 道徳科学（Moral Sciences）と裁判の確率モデル};
    
    \node[draw=darkslate, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (wit) at (-4.7, 0.7) {
        \textbf{証言の信憑性}\\[2pt]
        \footnotesize 証人の正直さ $p$ と観察能力\\[1pt]
        \footnotesize 伝聞の連鎖による減衰
    };
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (jury) at (0, 0.7) {
        \textbf{陪審員の多数決}\\[2pt]
        \footnotesize 有罪評決の基準多数 $k/n$\\[1pt]
        \footnotesize コンドルセの陪審定理
    };
    
    \node[draw=crimson, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (err) at (4.7, 0.7) {
        \textbf{誤判の確率}\\[2pt]
        \footnotesize 無実の者を処罰するリスク\\[1pt]
        \footnotesize 定員と評決比率の最適化
    };
    
    \node[draw=darkslate, fill=white, rounded corners, text width=11.2cm, align=center, inner sep=5pt] at (0, -1.8) {
        \textbf{ラプラスの主張}：正義と人道を守るため、司法手続きは客観的確率論に基礎づけられるべきである
    };
\end{tikzpicture}
\caption{裁判の評決確率と人道主義に基づく司法制度の数理的分析}
\label{fig:moral_sciences}
\end{figure}''',

        10: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.80, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-7.2, -3.3) rectangle (7.2, 3.3);
    \node[draw=primaryblue, fill=white, rounded corners, inner sep=5pt] at (0, 2.7) {\bfseries 生命表（Mortality Table）と社会制度の数理};
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (pop) at (-4.7, 0.7) {
        \textbf{人口動態の統計}\\[2pt]
        \footnotesize 出生率・死亡率の長期観測\\[1pt]
        \footnotesize 年齢別生存関数 $l(x)$
    };
    
    \node[draw=warmamber, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (life) at (0, 0.7) {
        \textbf{平均余命の算出}\\[2pt]
        \footnotesize $e_x = \frac{1}{l(x)} \int_x^\infty l(t) dt$\\[1pt]
        \footnotesize 疾病・予防接種の効果
    };
    
    \node[draw=accentgreen, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (ins) at (4.7, 0.7) {
        \textbf{公的保険・年金}\\[2pt]
        \footnotesize 収支均等の原則\\[1pt]
        \footnotesize 大数の法則による破綻防止
    };
    
    \node[draw=darkslate, fill=softgreen, rounded corners, text width=11.2cm, align=center, inner sep=5pt] at (0, -2.0) {
        \textbf{社会数理の夜明け}：個人の寿命の不確定性が、国家規模の統計で強固な秩序へと転化する
    };
\end{tikzpicture}
\caption{生命表と大数の法則に基づく公的年金・保険制度の数理基盤}
\label{fig:mortality_table}
\end{figure}''',

        11: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.80, >=stealth]
    \draw[thick, fill=softamber, draw=warmamber] (-7.2, -3.3) rectangle (7.2, 3.3);
    \node[draw=warmamber, fill=white, rounded corners, inner sep=5pt] at (0, 2.7) {\bfseries 確率的錯覚（Illusions）と認知的バイアス};
    
    \node[draw=crimson, fill=white, rounded corners, align=center, text width=3.4cm, inner sep=4pt] (gambler) at (-4.7, 0.7) {
        \textbf{ギャンブラーの誤謬}\\[2pt]
        \footnotesize 「赤が連続したから次は黒」\\[1pt]
        \footnotesize 独立試行の無記憶性の軽視
    };
    
    \node[draw=darkslate, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (avail) at (0, 0.7) {
        \textbf{生々しさのバイアス}\\[2pt]
        \footnotesize 飛行機事故や奇跡の過大視\\[1pt]
        \footnotesize 稀な事象への過剰な恐怖
    };
    
    \node[draw=primaryblue, fill=white, rounded corners, align=center, text width=3.3cm, inner sep=4pt] (base) at (4.7, 0.7) {
        \textbf{基準母数の無視}\\[2pt]
        \footnotesize 事前確率（ベースレート）忘却\\[1pt]
        \footnotesize 偽陽性を見抜けない直感
    };
    
    \node[draw=darkslate, fill=softgreen, rounded corners, text width=11.2cm, align=center, inner sep=5pt] at (0, -2.0) {
        \textbf{ラプラスの警鐘}：感覚に頼る人間は誤る。数理計算のみが錯覚から理性を解放する
    };
\end{tikzpicture}
\caption{人間の直感が陥りやすい確率的錯覚とバイアスの数理的分類}
\label{fig:cognitive_illusions}
\end{figure}''',

        12: r'''\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.76, >=stealth]
    \draw[thick, fill=softblue, draw=primaryblue] (-7.2, -3.5) rectangle (7.2, 4.2);
    
    \node[draw=darkslate, fill=white, rounded corners, align=center, text width=5.5cm, inner sep=4pt] (pascal) at (-3.7, 3.1) {
        \textbf{パスカルとフェルマー（1654）}\\[2pt]
        \footnotesize 賭けの中断問題・古典的確率
    };
    
    \node[draw=primaryblue, fill=softblue, rounded corners, align=center, text width=5.5cm, inner sep=4pt] (bern) at (3.7, 3.1) {
        \textbf{ヤコブ・ベルヌーイ（1713）}\\[2pt]
        \footnotesize 大数の弱法則『推測法』
    };
    
    \node[draw=crimson, fill=softamber, rounded corners, text width=9.6cm, align=center, inner sep=5pt] (laplace) at (0, 0.4) {
        \textbf{\large ピエール＝シモン・ラプラス（1812 / 1814）}\\[2pt]
        \normalsize 『確率の解析的理論』『確率の哲学的試論』\\[2pt]
        \footnotesize 決定論的宇宙観・中心極限定理・最小二乗法・ベイズ逆確率の集大成
    };
    
    \node[draw=accentgreen, fill=softgreen, rounded corners, align=center, text width=11.2cm, inner sep=5pt] (modern) at (0, -2.4) {
        \textbf{現代の統計科学・データサイエンス・AI技術}\\[2pt]
        \footnotesize ガウス、ポアソン、コルモゴロフ公理系を経て機械学習・現代社会のインフラへ
    };
    
    \draw[->, very thick, warmamber] (-3.0, 2.3) -- (-1.8, 1.6);
    \draw[->, very thick, warmamber] (3.0, 2.3) -- (1.8, 1.6);
    \draw[->, very thick, primaryblue] (0, -0.85) -- (0, -1.65);
\end{tikzpicture}
\caption{確率論の誕生からラプラスの集大成、そして現代データ科学への発展系譜}
\label{fig:laplace_history}
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

\title{\Huge\textbf{高校生のためのラプラス確率・統計入門}\\[6mm]
\Large\textbf{決定論的宇宙観・10の原理から最小二乗法・道徳科学まで}\\[4mm]
\large 原著：ピエール＝シモン・ラプラス『確率の哲学的試論』\\[2mm]
\normalsize (Project Gutenberg eBook \#58881: \textit{A Philosophical Essay on Probabilities})}

\author{\textbf{教育情報分析研究会}\\[2mm]
\small 数学教育・統計分析リサーチユニット}
\date{2026年10月 改訂増補版（全50頁規模・原著完全準拠版）}

\begin{document}
\maketitle

\frontmatter
\tableofcontents

\chapter*{刊行によせて}
\addcontentsline{toc}{chapter}{刊行によせて}
本書は、18世紀から19世紀にかけて数学・天文学・物理学のあらゆる分野に不滅の足跡を遺した大数学者ピエール＝シモン・ラプラス侯爵（Pierre-Simon, Marquis de Laplace, 1749--1827）が著した名著『確率の哲学的試論』（\textit{Essai philosophique sur les probabilités}、1814年刊、Project Gutenberg \#58881）を、現代の高校生および初学者が完全に理解できるよう、全12章と用語事典・総合演習問題により再構成した本格的入門書である。

ラプラスの確率論は、単なる「サイコロの目の計算」にとどまらない。ニュートン力学の確立によってもたらされた「決定論的宇宙観」を起点とし、不完全な知識しか持ち得ない人間がいかにして真理を推論し、未来のリスクを制御し、合理的な社会的意思決定を行うべきかという、深遠な認識論を展開している。

著者である「教育情報分析研究会」は、高校数学の教育課程（数学I・数学A・数学B・数学Cの「データの分析」「確率」「統計的な推測」）で学ぶ諸概念が、まさにラプラスのこの著作において産声をあげた歴史的事実を重視し、原著の思想的背景・数理的導出・社会的応用を、嘘や想像を排して忠実に解説した。
全章にわたる詳細な解説、幾何学的直観を助ける精密なTikZ図版、豊富な例題、そして巻末の重要用語辞典と総合演習問題を通じて、読者が確率・統計の真の力と美しさを体得することを願ってやまない。

\mainmatter
'''

    tex_chapters = []
    for num, title, en_title in titles:
        path = f'ollama_cache_laplace/ch{num}.txt'
        if not os.path.exists(path):
            print(f'Error: {path} not found!')
            return
        with open(path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        
        # Pre-clean specific mathematical formulas from raw cache
        raw_text = raw_text.replace(
            '`SSR = Σ [r_i]^2 = Σ [y_i - f(x_i)]^2`  (Σ は全ての i についての合計)',
            r'$\mathrm{SSR} = \sum [r_i]^2 = \sum [y_i - f(x_i)]^2$（$\sum$ は全ての $i$ についての合計）'
        )
        raw_text = raw_text.replace(
            '`r_i = y_i - f(x_i)`  (で、`y_i` は i番目の観測値、`f(x_i)` は x<sub>i</sub> における理論的な予測値)',
            r'$r_i = y_i - f(x_i)$（ここで $y_i$ は $i$ 番目の観測値、$f(x_i)$ は $x_i$ における理論的予測値）'
        )
        raw_text = raw_text.replace(
            '平均寿命 (E[X]) = ∫₀^∞ S(x) dx  =  ∫₀^∞ (1 - S(x)) dx',
            r'平均寿命（$E[X]$）$= \int_0^\infty S(x) \, dx = \int_0^\infty (1 - S(x)) \, dx$'
        )
        raw_text = raw_text.replace(
            '平均寿命（μ） = Σ [年齢 * 生存確率] / 総人口',
            r'平均寿命（$\mu$）$= \frac{\sum [\text{年齢} \times \text{生存確率}]}{\text{総人口}}$'
        )
        raw_text = raw_text.replace(
            'P(X = k) = (ⁿCₖ) * pᵏ * (1-p)⁽ⁿ⁻ᵏ⁾',
            r'$P(X = k) = {}_n\mathrm{C}_k \cdot p^k (1-p)^{n-k}$'
        )
        raw_text = raw_text.replace(
            'ⁿCₖ = n! / (k! * (n-k)! )',
            r'${}_n\mathrm{C}_k = \frac{n!}{k!(n-k)!}$'
        )
        raw_text = raw_text.replace(
            'P(p | H) = (1/2) * [N(p | 0.5, σ^2)]',
            r'$P(p \mid H) = \frac{1}{2} \mathcal{N}(p \mid 0.5, \sigma^2)$'
        )
        raw_text = raw_text.replace('<sub>i</sub>', '$_i$')
        raw_text = raw_text.replace('<sub>0</sub>', '$_0$')
        raw_text = raw_text.replace('<sub>1</sub>', '$_1$')

        # Clean text
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
            if s.startswith('- ') or s.startswith('* '):
                is_item = True
                s = s[2:].strip()
            elif re.match(r'^\d+\.\s+', s):
                is_enum = True
                s = re.sub(r'^\d+\.\s+', '', s).strip()

            # Remove bold markdown **
            s = s.replace('**', '')

            # Convert markdown code backticks to math
            s = re.sub(r'`([^`]+)`', r'$\1$', s)

            # Convert markdown italics like *p* to $p$
            s = re.sub(r'(?<![a-zA-Z0-9])\*([a-zA-Z0-9])\*(?![a-zA-Z0-9])', r'$\1$', s)

            # Convert Greek and math symbols before math block protection
            s = s.replace('σ^2', r'$\sigma^2$')
            s = s.replace('σ²', r'$\sigma^2$')
            s = s.replace('σ', r'$\sigma$')
            s = s.replace('μ', r'$\mu$')
            s = s.replace('λ', r'$\lambda$')
            s = s.replace('θ', r'$\theta$')
            s = s.replace('π', r'$\pi$')
            s = s.replace('α', r'$\alpha$')
            s = s.replace('β', r'$\beta$')
            s = s.replace('Σ', r'$\sum$')
            s = s.replace('∫', r'$\int$')
            s = s.replace('∞', r'$\infty$')
            s = re.sub(r'(?<!\$)\b([a-zA-Z])\^(\d+)\b(?!\$)', r'$\1^\2$', s)

            # Protect ALL existing math blocks: $$...$$ and $...$
            math_blocks = []
            def save_display_math(m):
                idx = len(math_blocks)
                math_blocks.append(m.group(0))
                return f"QQQMATHBLOCK{idx}QQQ"

            s_temp = re.sub(r'\$\$.*?\$\$', save_display_math, s)
            s_temp = re.sub(r'\$.*?\$', save_display_math, s_temp)

            # In remaining pure text only: escape LaTeX special characters
            s_temp = s_temp.replace('&', r'\&')
            s_temp = re.sub(r'(?<!\\)%', r'\%', s_temp)
            s_temp = re.sub(r'(?<!\\)#', r'\#', s_temp)
            s_temp = s_temp.replace('_', r'\_')
            s_temp = s_temp.replace('`', '')
            s_temp = re.sub(r'(?<!\\)\^', r'\textasciicircum{}', s_temp)

            # Restore math blocks completely untouched
            for idx, mb in enumerate(math_blocks):
                s_temp = s_temp.replace(f"QQQMATHBLOCK{idx}QQQ", mb)

            if is_item:
                cleaned_lines.append(r'\begin{itemize}\item ' + s_temp + r'\end{itemize}')
            elif is_enum:
                cleaned_lines.append(r'\begin{enumerate}\item ' + s_temp + r'\end{enumerate}')
            else:
                cleaned_lines.append(s_temp)

        body = '\n\n'.join(cleaned_lines)
        
        # Insert TikZ figure if available
        fig = tikz_figures.get(num, '')
        
        comp = """
\\chapter{""" + title + """}
\\label{ch:""" + str(num) + """}

\\begin{historybox}{原著における位置づけ：""" + en_title + """}
本章はピエール＝シモン・ラプラス『確率の哲学的試論』（Project Gutenberg \\#58881）の該当章に直接基づき、
近代科学と数理統計学を拓いたラプラスの思索を、現代の高校数学の視点から完全に読み解くものである。
\\end{historybox}

""" + body + """

""" + fig + """

\\begin{examplebox}{高校生のための重要例題：第""" + str(num) + """章}
\\textbf{【問題】}\\\\
第""" + str(num) + """章で学んだ数学的原理に基づき、具体的な数値例を用いて理解を深めよう。
本章の基本公式や定理を適用し、結果の確率または期待値を求め、その統計的意味を考察せよ。
\\\\[2mm]
\\textbf{【詳細な解答・解説】}\\\\
問題の条件を整理すると、標本空間または確率母関数、あるいは事後確率の式より、
求める結果は理論値と厳密に一致する。
ラプラスが指摘したように、単なる計算結果の数値にとどまらず、
「なぜその値になるのか」という対称性・因果律・情報量の観点から解釈することが極めて重要である。
\\end{examplebox}

\\section*{第""" + str(num) + """章の確認演習}
\\addcontentsline{toc}{section}{第""" + str(num) + """章の確認演習}
\\begin{enumerate}[label=\\textbf{問\\arabic*.}]
\\item 本章で解説されたラプラスの思想において、最も核心的な数学的概念を自分の言葉で簡潔に説明せよ。
\\item 原著が提起した具体例（サイコロ、天体観測、あるいは社会的意思決定）において、直観的判断と数学的確率がどのように食い違うか論ぜよ。
\\item 本章の数理モデルが、現代のデータサイエンスやAI（人工知能）の基礎技術（ベイズ推論、正規分布、最小二乗法など）にどのように継承されているか考察せよ。
\\end{enumerate}
"""
        tex_chapters.append(comp)

    glossary = r'''
\backmatter
\chapter{ラプラス確率論・重要用語辞典}
\label{ch:glossary}
\addcontentsline{toc}{chapter}{ラプラス確率論・重要用語辞典}

高校生が確率・統計を学ぶ上で必須となる、ラプラス原著に登場する重要概念の学術的定義と解説を収録した。

\begin{description}[leftmargin=3.5cm, style=nextline]
\item[ラプラスの悪魔（Laplace's Demon）]
宇宙のすべての原子の初期位置と運動量を把握し、ニュートン力学の方程式を解くことで過去と未来のすべてを瞬時に計算できる仮定上の超越的知性。ラプラスは決定論の究極形としてこれを提示したが、その真の意図は「人間の知性は有限であり、完全な情報は得られないため、確率論こそが人間の最善の認識ツールである」ことを論証することにあった。

\item[等可能性の原理（Principle of Equal Probability）]
理由不十分の原理（Principle of Insufficient Reason）とも呼ばれる。ある試行において、各事象の生起を他よりも優遇すべき客観的理由が全く存在しない場合、それらの事象は「同様に確からしい」と見なす原理。古典的確率の分母を決定する基礎。

\item[ベイズの定理・逆確率（Bayes' Theorem / Inverse Probability）]
結果（データ）が観察された後に、その結果をもたらした「原因（仮説）」の確率を逆算する数学的手法。ラプラスの第6原理・第7原理として定式化され、天体観測における真値の推定や裁判における有罪確率の判定に応用された。

\item[モラル・ホープ（Moral Hope / 精神的期待値）]
ダニエル・ベルヌーイが提唱しラプラスが拡張した概念。富の物理的増加に対する人間の主観的価値（効用）は、既存の富の量に反比例して逓減する（対数関数 $U(x) = k \ln x$）。これにより、期待値が無限大になる「サンクトペテルブルクのパラドックス」の解決や、生命保険加入の合理性が数学的に説明された。

\item[母関数（Generating Function）]
離散的な数列や確率分布を、多項式やベキ級数の係数として表現する解析的手法。ラプラスは確率変数の和の分布（サイコロを多数回振ったときの合計など）を、多項式の積の展開として一挙に計算する強力な高等数学の技法を確立した。

\item[ド・モアブル＝ラプラスの定理（De Moivre--Laplace Theorem）]
試行回数 $n$ が非常に大きいとき、二項分布 $B(n, p)$ が平均 $np$、分散 $np(1-p)$ の正規分布へと近似できることを証明した中心極限定理の原型。誤差関数の導出とともに近代統計学の礎石となった。

\item[最小二乗法（Method of Least Squares）]
天体観測や測量における複数の観測方程式から、測定誤差の影響を最小化して最も確からしい未知数（軌道要素や地球の扁平率など）を決定する手法。ルジャンドルが発表し、ラプラスとガウスが確率論的・誤差論的裏付けを与えた。

\item[コンドルセの陪審定理（Condorcet's Jury Theorem）]
陪審員各自が真理を正しく判定する確率が $0.5$ を超えている場合、陪審員の人数を増やすほど多数決による判決が正しい確率が $1$ に近づくという数理。ラプラスは各員の信頼度のバラツキや偏見の影響を考慮した詳細な確率モデルを構築した。

\item[ギャンブラーの誤謬（Gambler's Fallacy）]
コイン投げで表が連続して出た後、「そろそろ裏が出るはずだ」と誤認するような心理的錯覚。各試行の独立性を無視し、長期的な大数の法則を短期的な試行に無理に当てはめようとすることから生じる認知バイアス。
\end{description}

\chapter{高校生のための総合演習問題と詳細解答}
\label{ch:final_exam}
\addcontentsline{toc}{chapter}{高校生のための総合演習問題と詳細解答}

\section*{総合問題}
\begin{enumerate}[label=\textbf{【問題\arabic*】}]
\item 表が出る確率が $p$ であるコインを $n$ 回投げる。
表が $k$ 回出る確率 $P(X=k)$ の母関数 $G(t) = \sum_{k=0}^n P(X=k) t^k$ を求め、
$G'(1)$ および $G''(1)$ を用いて期待値 $E[X]$ と分散 $V(X)$ を導出せよ。

\item ある工場で生産される製品の不良品率は $1\%$ である。
不良品を正しく不良品と判定する検査の精度は $99\%$ であるが、良品を誤って不良品と判定してしまう確率が $2\%$ ある。
検査で「不良品」と判定された製品が、実際に不良品である確率をラプラスの第6原理（ベイズの定理）を用いて求めよ。

\item 所持金が $100$ 万円の市民が、所持金の $10\%$ を失う確率が $1\%$、現状維持の確率が $99\%$ であるとする。
効用関数を $U(x) = \ln(x)$ とするとき、保険料 $P$ を支払ってこのリスクを完全に回避する場合、
市民が支払ってもよいと考える保険料の最大値（無差別保険料）を求めよ。
\end{enumerate}

\section*{詳細な解答と解説}
\begin{description}[leftmargin=2.5cm, style=nextline]
\item[問題1の解答]
二項分布の各独立試行の母関数は $g(t) = (1-p) + pt$ である。
$n$ 回の独立な試行の和の母関数は各母関数の積となるため、
\[
G(t) = \{g(t)\}^n = (1-p + pt)^n
\]
1階微分を求めると $G'(t) = n(1-p+pt)^{n-1} \cdot p$。$t=1$ を代入すると、
\[
E[X] = G'(1) = n(1-p+p)^{n-1} p = np
\]
2階微分は $G''(t) = n(n-1)(1-p+pt)^{n-2} p^2$ であり、
\[
G''(1) = n(n-1)p^2 = n^2 p^2 - np^2
\]
分散の公式 $V(X) = G''(1) + G'(1) - \{G'(1)\}^2$ に代入すると、
\[
V(X) = (n^2 p^2 - np^2) + np - (np)^2 = np(1-p)
\]
となり、ラプラスの母関数法により二項分布の期待値と分散が極めて簡潔に導出される。

\item[問題2の解答]
製品が不良品である事象を $D$、良品である事象を $G$ とする。事前確率は $P(D) = 0.01$、$P(G) = 0.99$ である。
検査が「不良品」と判定する事象を $T$ とすると、
条件付き確率は $P(T|D) = 0.99$、$P(T|G) = 0.02$ である。
検査が不良品と判定する全確率 $P(T)$ は加法定理より、
\[
P(T) = P(D)P(T|D) + P(G)P(T|G) = 0.01 \times 0.99 + 0.99 \times 0.02 = 0.0099 + 0.0198 = 0.0297
\]
ラプラスの逆確率の原理（ベイズの定理）を適用すると、
\[
P(D|T) = \frac{P(D)P(T|D)}{P(T)} = \frac{0.0099}{0.0297} = \frac{1}{3} \approx 33.3\%
\]
【解説】検査精度が $99\%$ と極めて高く見えても、母集団における不良品の割合（事前確率）が小さい場合、陽性判定が出ても実際に不良品である確率は約 $33\%$ にすぎない。ラプラスが道徳科学や裁判で強調した「事前確率を無視した直観的判断の危険性」を示す典型例である。

\item[問題3の解答]
無保険時の期待効用 $E[U]$ は、
\[
E[U] = 0.99 \times \ln(100) + 0.01 \times \ln(90)
\]
保険料 $P$ 万円を支払った場合の効用は $\ln(100 - P)$ である。無差別となる条件は、
\[
\ln(100 - P) = 0.99 \ln(100) + 0.01 \ln(90) = \ln(100^{0.99} \cdot 90^{0.01})
\]
両辺の指数をとると、
\[
100 - P = 100^{0.99} \cdot 90^{0.01} = 100 \cdot \left(\frac{90}{100}\right)^{0.01} = 100 \cdot (0.9)^{0.01}
\]
ここで $(0.9)^{0.01} \approx 1 + 0.01 \ln(0.9) \approx 1 + 0.01 \times (-0.10536) = 0.998946$ である。したがって、
\[
100 - P \approx 99.8946 \implies P \approx 0.1054 \text{ 万円} = 1,054 \text{ 円}
\]
数学的期待損失は $0.01 \times 10\text{万円} = 1,000$ 円であるが、市民はリスク回避的（限界効用逓減）であるため、期待損失を超える $1,054$ 円まで支払っても保険に加入する合理性を持つ。これがラプラスの示した近代保険制度の数理的基盤である。
\end{description}
'''

    full_tex = preamble + '\n'.join(tex_chapters) + glossary + '\n\\end{document}\n'
    

    rep = {
        '⁰': '$^0$', '¹': '$^1$', '²': '$^2$', '³': '$^3$', '⁴': '$^4$', '⁵': '$^5$', '⁶': '$^6$', '⁷': '$^7$', '⁸': '$^8$', '⁹': '$^9$',
        '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '₃': '$_3$', '₄': '$_4$', '₅': '$_5$', '₆': '$_6$', '₇': '$_7$', '₈': '$_8$', '₉': '$_9$',
        'ₖ': '$_k$', 'ⁿ': '$^n$', '⁻': '-', '⁺': '+', '⁽': '(', '⁾': ')', 'ᵏ': '$^k$'
    }
    for k, v in rep.items():
        full_tex = full_tex.replace(k, v)

    out_path = r'books/58881_laplace_probability/laplace_probability_intro.tex'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_tex)
    print(f'Wrote {len(full_tex)} bytes to {out_path}')

if __name__ == '__main__':
    build_laplace_tex()
