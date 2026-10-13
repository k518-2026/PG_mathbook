import os, re
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from scripts.new_tikz_figures import NEW_TIKZ

def build_thompson_tex():
    titles = [
        (1, r'予備的恐怖からの解放：微小量 $dx$ と $dy$ の正体と微積分の扉', 'To Deliver You From the Preliminary Terrors', '予備的恐怖からの解放'),
        (2, r'小ささの階級と無視の数理：1次微小量・2次微小量と近似の本質', 'On Different Degrees of Smallness', '小ささの階級と無視の数理'),
        (3, r'相対的な成長度：変化率としての導関数 $\frac{dy}{dx}$ と曲線の傾き', 'On Relative Growings and Geometrical Slopes', '相対的な成長度'),
        (4, r'ベキ関数の微分法：$y = x^n$ の微分公式と直観的証明', 'Simplest Cases: Powers of x and Constants', 'ベキ関数の微分法'),
        (5, r'関数の結合と演算規則：和・差・積・商の微分公式のメカニズム', 'Sums, Differences, Products, and Quotients', '関数の結合と演算規則'),
        (6, r'合成関数と連鎖律：「便利な裏技」チェイン・ルールの威力', 'Introducing a Useful Dodge: The Chain Rule', '合成関数と連鎖律'),
        (7, r'高階微分と運動の物理：第2次導関数 $\frac{d^2y}{dx^2}$、速度・加速度の数理', 'Successive Differentiation and When Time Varies', '高階微分と運動の物理'),
        (8, r'極大・極小と最適化：導関数がゼロになる点と現実世界の最大化・最小化', 'Maxima and Minima: The Art of Optimization', '極大・極小と最適化'),
        (9, r'自然の成長と指数・対数：ネイピア数 $e$、真の複利法則と自然対数の微分', 'On True Compound Interest and the Exponential Magic', '自然の成長と指数・対数'),
        (10, r'振動と三角関数の微分：波と円運動を描く $\sin x$ と $\cos x$ の導関数', 'How to Deal with Sines and Cosines', '振動と三角関数の微分'),
        (11, r'微分の逆演算としての積分：不定積分の基礎と原始関数の探求', 'Integration: Reversing the Process and Finding Solutions', '微分の逆演算としての積分'),
        (12, r'面積の求積と微積分学の基本定理：区分求積法から現代科学・AIへの架け橋', 'On Finding Areas by Integrating and the Fundamental Theorem', '面積の求積と基本定理')
    ]
    tikz_figures = NEW_TIKZ

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
\definecolor{softblue}{RGB}{235, 243, 250}
\definecolor{darkslate}{RGB}{44, 62, 80}
\definecolor{warmamber}{RGB}{217, 119, 6}
\definecolor{softamber}{RGB}{254, 243, 199}
\definecolor{crimson}{RGB}{185, 28, 28}
\definecolor{softrose}{RGB}{255, 228, 230}
\definecolor{accentgreen}{RGB}{16, 120, 70}
\definecolor{softgreen}{RGB}{236, 253, 245}

\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    urlcolor=primaryblue,
    citecolor=accentgreen,
    pdftitle={高校生のための微積分入門 —— 『Calculus Made Easy』で直観的にわかる微分・積分・極限から物理・曲線の数理まで},
    pdfauthor={教育情報分析研究会}
}

\newtcolorbox{examplebox}[1]{
    colback=softgreen,
    colframe=accentgreen,
    coltitle=white,
    fonttitle=\bfseries,
    title=#1,
    arc=3mm,
    boxrule=1pt,
    left=4mm,right=4mm,top=3mm,bottom=3mm,
    breakable
}

\newtcolorbox{pointbox}[1]{
    colback=softamber,
    colframe=warmamber,
    coltitle=darkslate,
    fonttitle=\bfseries,
    title=#1,
    arc=2mm,
    boxrule=1pt,
    left=3mm,right=3mm,top=2mm,bottom=2mm,
    breakable
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

\begin{document}

\begin{titlepage}
\begin{center}
\vspace*{1.5cm}
{\Large\bfseries プロジェクト・グーテンベルク古典数学入門シリーズ 第5弾}\\[0.8cm]
\rule{\textwidth}{1.5pt}\\[0.4cm]
{\huge\bfseries 高校生のための微積分入門}\\[0.4cm]
{\Large\bfseries —— 『Calculus Made Easy』で直観的にわかる\\微分・積分・極限から物理・曲線の数理まで ——}\\[0.4cm]
\rule{\textwidth}{1.5pt}\\[1.5cm]

{\large 原著：シルバヌス・P・トンプソン（\textit{Silvanus P. Thompson}）\\
\textit{Calculus Made Easy}（1910年）}\\[2.0cm]

{\Large\bfseries 著：教育情報分析研究会}\\[2.5cm]

\vfill
{\large 2026年10月 最新版}\\[0.5cm]
{\footnotesize 本書は Project Gutenberg のパブリックドメイン数学古典（eBook \#33283）を底本とし、\\
現代の高校数学（数学II・数学III、物理基礎）に完全対応した50ページ以上の本格的入門書です。}
\end{center}
\end{titlepage}

\frontmatter
\tableofcontents

\mainmatter
'''

    cache_dir = 'ollama_cache_thompson_calculus'
    tex_chapters = []

    for num, title_ja, title_en, short_title in titles:
        fname = f"chap_{num:02d}.txt"
        path = os.path.join(cache_dir, fname)
        if not os.path.exists(path):
            print(f"Warning: {path} not found! Skipping.")
            continue
        
        with open(path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        
        # Pre-clean raw text
        raw_text = raw_text.replace('<sub>i</sub>', '$_i$')
        raw_text = raw_text.replace('<sub>0</sub>', '$_0$')
        raw_text = raw_text.replace('<sub>1</sub>', '$_1$')
        raw_text = raw_text.replace('<sub>2</sub>', '$_2$')
        raw_text = raw_text.replace('<sup>2</sup>', '$^2$')
        raw_text = raw_text.replace('<sup>3</sup>', '$^3$')
        raw_text = raw_text.replace('<sup>n</sup>', '$^n$')

        lines = raw_text.split('\n')
        cleaned_lines = []
        for line in lines:
            s = line.strip()
            if not s:
                continue
            if s.startswith('# ') or s.startswith('## '):
                continue
            if s.startswith('### '):
                raw_t = s[4:].strip()
                m_blocks = []
                def save_m(m):
                    idx = len(m_blocks)
                    m_blocks.append(m.group(0))
                    return f"QQQSECTIONMATH{idx}QQQ"
                t = re.sub(r'\$.*?\$', save_m, raw_t)
                t = t.replace('&', r'\&').replace('_', r'\_')
                for idx, mb in enumerate(m_blocks):
                    t = t.replace(f"QQQSECTIONMATH{idx}QQQ", mb)
                cleaned_lines.append(r'\section{' + t + '}')
                continue
            elif s.startswith('#### '):
                raw_t = s[5:].strip()
                m_blocks = []
                def save_m(m):
                    idx = len(m_blocks)
                    m_blocks.append(m.group(0))
                    return f"QQQSECTIONMATH{idx}QQQ"
                t = re.sub(r'\$.*?\$', save_m, raw_t)
                t = t.replace('&', r'\&').replace('_', r'\_')
                for idx, mb in enumerate(m_blocks):
                    t = t.replace(f"QQQSECTIONMATH{idx}QQQ", mb)
                cleaned_lines.append(r'\subsection{' + t + '}')
                continue

            is_item = False
            is_enum = False
            if s.startswith('- ') or s.startswith('* '):
                is_item = True
                s = s[2:].strip()
            elif re.match(r'^\d+\.\s+', s):
                is_enum = True
                s = re.sub(r'^\d+\.\s+', '', s).strip()

            # First, preserve math blocks: $$...$$ and $...$
            math_blocks = []
            def save_math(m):
                idx = len(math_blocks)
                math_blocks.append(m.group(0))
                return f"QQQMATHBLOCK{idx}QQQ"

            s_temp = re.sub(r'\$\$.*?\$\$', save_math, s)
            s_temp = re.sub(r'\$.*?\$', save_math, s_temp)

            # In text outside math:
            s_temp = s_temp.replace('**', '')
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

        # Example and Exercises for each chapter
        example_content = get_example_for_chapter(num)
        exercises_content = get_exercises_for_chapter(num)

        ch_tex = f"""\\chapter{{{title_ja}}}
\\chaptermark{{{short_title}}}

\\begin{{flushright}}
\\small\\textit{{{title_en}}}
\\end{{flushright}}

{fig}

{body}

{example_content}

{exercises_content}
"""
        tex_chapters.append(ch_tex)

    glossary = get_glossary_and_final_exercises()
    full_tex = preamble + '\n'.join(tex_chapters) + glossary + '\n\\end{document}\n'

    rep = {
        '⁰': '$^0$', '¹': '$^1$', '²': '$^2$', '³': '$^3$', '⁴': '$^4$', '⁵': '$^5$', '⁶': '$^6$', '⁷': '$^7$', '⁸': '$^8$', '⁹': '$^9$',
        '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '₃': '$_3$', '₄': '$_4$', '₅': '$_5$', '₆': '$_6$', '₇': '$_7$', '₈': '$_8$', '₉': '$_9$',
        'ₖ': '$_k$', 'ⁿ': '$^n$', '⁻': '-', '⁺': '+', '⁽': '(', '⁾': ')', 'ᵏ': '$^k$'
    }
    for k, v in rep.items():
        full_tex = full_tex.replace(k, v)

    out_path = r'books/33283_thompson_calculus/thompson_calculus_intro.tex'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_tex)
    print(f"Wrote {len(full_tex)} bytes to {out_path}")

def get_example_for_chapter(num):
    examples = {
        1: (
            "微小量 $dx$ と $dy$ の直観的把握",
            r"時速 $60\,\mathrm{km}$ で等速直線運動している自動車がある。走行時間 $t$（時間）と走行距離 $s$（$\mathrm{km}$）の関係は $s = 60t$ である。いま、微小時間 $dt = 1\,\text{秒} = \frac{1}{3600}\,\text{時間}$ が経過したとき、走行距離の微小増分 $ds$ を求め、比 $\frac{ds}{dt}$ の物理的意味を答えよ。",
            r"関数 $s(t) = 60t$ において、時間 $t$ が $t + dt$ に変化したとき、走行距離は $s + ds = 60(t + dt) = 60t + 60dt$ となる。両辺から $s = 60t$ を引くと、微小増分 $ds = 60dt$ が得られる。$dt = \frac{1}{3600}\,\text{時間}$ を代入すると、$ds = 60 \times \frac{1}{3600} = \frac{1}{60}\,\mathrm{km} \approx 16.67\,\mathrm{m}$ である。このとき、比 $\frac{ds}{dt}$ は $\frac{60dt}{dt} = 60\,\mathrm{km/h}$ となり、微小時間の極限においても一定の「瞬間の速度（スピードメーターの指示値）」を表す。微小量 $ds$ と $dt$ はともに極小であるが、その比 $\frac{ds}{dt}$ は有限で確固たる物理的実在（速度）を示す。"
        ),
        2: (
            "小ささの階級と高次微小量の無視",
            r"一辺の長さが $x = 10\,\mathrm{cm}$ の正方形の金属板がある。温度上昇により各辺が $dx = 0.01\,\mathrm{cm}$（$0.1\,\mathrm{mm}$）だけ熱膨張した。全体の面積の正確な増加分 $\Delta S$ を求め、1次微小量 $2x dx$ と2次微小量 $(dx)^2$ の数値を比較せよ。",
            r"正方形の面積 $S = x^2$ に対し、膨張後の面積は $(x+dx)^2 = x^2 + 2x dx + (dx)^2$ である。面積の増分は $\Delta S = 2x dx + (dx)^2$ である。数値を代入すると、$2x dx = 2 \times 10 \times 0.01 = 0.2\,\mathrm{cm}^2$ であり、$(dx)^2 = (0.01)^2 = 0.0001\,\mathrm{cm}^2$ である。全体増分 $\Delta S = 0.2001\,\mathrm{cm}^2$ のうち、$(dx)^2$ が占める割合はわずか $\frac{0.0001}{0.2} = 0.05\%$ に過ぎない。$dx \to 0$ の極限では、この割合は完全にゼロへ収束する。したがって、高次の微小量 $(dx)^2$ を消去し、$dS = 2x dx$、すなわち $\frac{dS}{dx} = 2x$ と近似・極限計算を行うことは、完全に合理的かつ数学的に厳密である。"
        ),
        3: (
            "曲線の接線の傾きと瞬間変化率",
            r"放物線 $y = x^2 - 4x + 5$ 上の点 $P(3, 2)$ における接線の傾きを導関数の定義に基づき求め、その点における接線の方程式を求めよ。",
            r"関数 $f(x) = x^2 - 4x + 5$ に対し、$x$ が $x + dx$ に変化したときの変化量は、\\$f(x+dx) = (x+dx)^2 - 4(x+dx) + 5 = x^2 + 2x dx + (dx)^2 - 4x - 4dx + 5$\\となる。$dy = f(x+dx) - f(x) = (2x - 4)dx + (dx)^2$。両辺を $dx$ で割り、$dx \to 0$ とすると、導関数 $\frac{dy}{dx} = 2x - 4$ が得られる。点 $P(3, 2)$ における接線の傾きは $m = 2(3) - 4 = 2$ である。したがって、求める接線の方程式は $y - 2 = 2(x - 3)$、すなわち $y = 2x - 4$ である。"
        ),
        4: (
            "ベキ関数の微分公式の応用",
            r"次の各関数の導関数を求めよ。\\(1) $y = 5x^4 - 2x^3 + 7x - 9$ \quad (2) $y = \frac{3}{x^2}$ \quad (3) $y = 4\sqrt{x}$",
            r"(1) ベキ関数の基本公式 $\frac{d}{dx}(x^n) = n x^{n-1}$ および定数項の微分はゼロである規則より、\\$\frac{dy}{dx} = 5(4x^3) - 2(3x^2) + 7(1) - 0 = 20x^3 - 6x^2 + 7$。\\(2) 負の指数表示 $y = 3x^{-2}$ に直す。公式を適用して、\\$\frac{dy}{dx} = 3(-2x^{-3}) = -6x^{-3} = -\frac{6}{x^3}$。\\(3) 分数指数表示 $y = 4x^{1/2}$ に直す。公式より、\\$\frac{dy}{dx} = 4\left(\frac{1}{2}x^{-1/2}\right) = 2x^{-1/2} = \frac{2}{\sqrt{x}}$。"
        ),
        5: (
            "積の微分法と商の微分法の実践",
            r"次の各関数を微分せよ。\\(1) $y = (x^2 + 3)(2x - 1)$ \quad (2) $y = \frac{x^2 - 1}{x^2 + 1}$",
            r"(1) 積の微分公式 $(uv)' = u'v + uv'$ を用いる。$u = x^2 + 3$, $v = 2x - 1$ とおくと、$u' = 2x$, $v' = 2$。\\$\frac{dy}{dx} = (2x)(2x - 1) + (x^2 + 3)(2) = 4x^2 - 2x + 2x^2 + 6 = 6x^2 - 2x + 6$。\\（※展開してから微分した $y = 2x^3 - x^2 + 6x - 3 \implies y' = 6x^2 - 2x + 6$ と完全に一致する）。\\(2) 商の微分公式 $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ を用いる。$u = x^2 - 1$, $v = x^2 + 1$ より $u' = 2x$, $v' = 2x$。\\$\frac{dy}{dx} = \frac{2x(x^2 + 1) - (x^2 - 1)(2x)}{(x^2 + 1)^2} = \frac{(2x^3 + 2x) - (2x^3 - 2x)}{(x^2 + 1)^2} = \frac{4x}{(x^2 + 1)^2}$。"
        ),
        6: (
            "連鎖律（チェイン・ルール）による合成関数の微分",
            r"関数 $y = (3x^2 - 5)^4$ の導関数 $\frac{dy}{dx}$ を、中間変数 $u$ を用いた連鎖律によって求めよ。",
            r"中間変数として括弧の中身 $u = 3x^2 - 5$ を設定する。これにより、$y = u^4$ と表される。\\それぞれの微分を計算すると、\\$\frac{dy}{du} = 4u^3, \quad \frac{du}{dx} = 6x$\\連鎖律 $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$ を適用すると、\\$\frac{dy}{dx} = 4u^3 \cdot 6x = 24x u^3$\\最後に $u = 3x^2 - 5$ を代入して戻すと、\\$\frac{dy}{dx} = 24x(3x^2 - 5)^3$\\展開することなく、合成関数の微分公式によって極めて簡潔に導出できる。"
        ),
        7: (
            "高階微分と自由落下運動の解析",
            r"地上から初速度 $v_0 = 19.6\,\mathrm{m/s}$ で鉛直上向きに投げ上げられた小球の時刻 $t$（秒）における高さが $h(t) = 19.6t - 4.9t^2$（$\mathrm{m}$）で与えられている。\\(1) 時刻 $t$ における小球の速度 $v(t) = \frac{dh}{dt}$ と加速度 $a(t) = \frac{d^2h}{dt^2}$ を求めよ。\\(2) 小球が最高点に達する時刻と、その高さを求めよ。",
            r"(1) 速度は高さの1次導関数である：\\$v(t) = \frac{dh}{dt} = 19.6 - 9.8t\,\mathrm{[m/s]}$\\加速度は速度の1次導関数（高さの2次導関数）である：\\$a(t) = \frac{d^2h}{dt^2} = -9.8\,\mathrm{[m/s^2]}$\\これは下向きの一定な重力加速度 $g = 9.8\,\mathrm{m/s^2}$ を示す。\\(2) 最高点では瞬間の速度がゼロになるため、$v(t) = 19.6 - 9.8t = 0$ より $t = 2.0\,\text{秒}$。\\そのときの高さは $h(2) = 19.6(2) - 4.9(4) = 39.2 - 19.6 = 19.6\,\mathrm{m}$ である。"
        ),
        8: (
            "容積最大化問題（トンプソンの名作古典問）",
            r"一辺の長さが $12\,\mathrm{cm}$ の正方形のブリキ板がある。四隅から合同な正方形（一辺 $x\,\mathrm{cm}$）を切り取り、折り曲げて蓋のない直方体の箱を作る。箱の容積 $V$ が最大となるときの切り取り幅 $x$ と、その最大容積 $V_{\text{max}}$ を求めよ。",
            r"箱の底面は一辺 $(12 - 2x)\,\mathrm{cm}$ の正方形、高さは $x\,\mathrm{cm}$ である。ただし $0 < x < 6$。\\容積関数は $V(x) = x(12 - 2x)^2 = x(144 - 48x + 4x^2) = 4x^3 - 48x^2 + 144x$。\\極値を求めるため導関数を計算する：\\$\frac{dV}{dx} = 12x^2 - 96x + 144 = 12(x^2 - 8x + 12) = 12(x - 2)(x - 6)$\\$0 < x < 6$ において停留点は $x = 2$ のみ。\\第2次導関数を調べると、$\frac{d^2V}{dx^2} = 24x - 96$ より、$x = 2$ で $\frac{d^2V}{dx^2} = 48 - 96 = -48 < 0$（上に凸、極大）。\\したがって $x = 2\,\mathrm{cm}$ のとき容積は最大となり、最大容積は $V(2) = 2(12 - 4)^2 = 2 \times 64 = 128\,\mathrm{cm}^3$ である。"
        ),
        9: (
            "自己増殖する指数関数と自然対数の微分",
            r"関数 $y = x^2 e^x$ および $y = \ln(x^2 + 1)$ の導関数を求めよ。",
            r"(1) 積の微分公式 $(uv)' = u'v + uv'$ を適用する。$u = x^2, v = e^x$ とおくと、$u' = 2x, v' = e^x$（$e^x$ の微分は自分自身のまま）。\\$\frac{dy}{dx} = 2x e^x + x^2 e^x = (x^2 + 2x)e^x = x(x+2)e^x$。\\(2) 自然対数の合成関数である。連鎖律を用いる。$u = x^2 + 1$ とおくと $y = \ln(u)$。\\$\frac{dy}{du} = \frac{1}{u}, \quad \frac{du}{dx} = 2x$\\したがって $\frac{dy}{dx} = \frac{1}{u} \cdot 2x = \frac{2x}{x^2 + 1}$。"
        ),
        10: (
            "三角関数の微分と合成関数",
            r"次の各関数を微分せよ。\\(1) $y = \sin(3x)$ \quad (2) $y = \cos^2(x)$ \quad (3) $y = x \sin(x)$",
            r"(1) 連鎖律：$u = 3x$ とおくと $y = \sin(u)$。$\frac{dy}{dx} = \cos(u) \cdot 3 = 3\cos(3x)$。\\(2) 連鎖律：$u = \cos(x)$ とおくと $y = u^2$。$\frac{dy}{dx} = 2u \cdot (-\sin x) = -2\sin(x)\cos(x) = -\sin(2x)$。\\(3) 積の微分：$u = x, v = \sin(x)$。$\frac{dy}{dx} = 1 \cdot \sin(x) + x \cdot \cos(x) = \sin(x) + x\cos(x)$。"
        ),
        11: (
            "不定積分の計算と原始関数の決定",
            r"次の不定積分を求めよ。\\(1) $\int (6x^2 - 4x + 5)\,dx$ \quad (2) $\int \left(\frac{1}{x} + \frac{2}{\sqrt{x}}\right)dx$ \quad (3) $\int 3e^x dx$",
            r"(1) ベキ関数の基本積分公式 $\int x^n dx = \frac{1}{n+1}x^{n+1} + C$ より、\\$\int (6x^2 - 4x + 5)\,dx = 6\left(\frac{x^3}{3}\right) - 4\left(\frac{x^2}{2}\right) + 5x + C = 2x^3 - 2x^2 + 5x + C$。\\(2) 指数表記で整理すると $\int (x^{-1} + 2x^{-1/2})dx$。\\$x^{-1}$ の積分は自然対数 $\ln|x|$ となり、$x^{-1/2}$ の積分は $\frac{x^{1/2}}{1/2} = 2\sqrt{x}$ であるから、\\$\int \left(\frac{1}{x} + \frac{2}{\sqrt{x}}\right)dx = \ln|x| + 4\sqrt{x} + C$。\\(3) 指数関数の積分は自分自身のままであるから、$\int 3e^x dx = 3e^x + C$。（すべて $C$ は積分定数）。"
        ),
        12: (
            "定積分による放物線下の面積求積",
            r"放物線 $y = 3x^2$ と $x$ 軸、および2直線 $x = 1, x = 3$ で囲まれた図形の面積 $S$ を、定積分の定義（微積分学の基本定理）に基づき求めよ。",
            r"求める面積 $S$ は、微小短冊 $y \cdot dx = 3x^2 dx$ を $x = 1$ から $x = 3$ まで連続的に足し合わせた定積分として表される：\\$S = \int_1^3 3x^2 \, dx$\\被積分関数 $f(x) = 3x^2$ の原始関数の一つは $F(x) = x^3$ である（実際、$F'(x) = 3x^2$）。\\微積分学の基本定理 $\int_a^b f(x)dx = [F(x)]_a^b = F(b) - F(a)$ を適用すると、\\$S = [x^3]_1^3 = 3^3 - 1^3 = 27 - 1 = 26$\\アルキメデスが古代に膨大な取り尽くし法で求めた放物線下の面積が、微積分学の基本定理によってわずか2行で厳密に計算できる。"
        )
    }
    title, q, sol = examples.get(num, ("例題", "問題文", "解答解説"))
    return f"""\\begin{{examplebox}}{{高校生のための重要例題：第{num}章 —— {title}}}
\\textbf{{【問題】}}\\\\
{q}
\\\\[2mm]
\\textbf{{【詳細な解答・解説】}}\\\\
{sol}
\\end{{examplebox}}
"""

def get_exercises_for_chapter(num):
    exercises = {
        1: [
            "記号 $dx$ と $\\Delta x$ の概念的相違を、直観的微小量と有限な増分の観点から説明せよ。",
            "トンプソンの箴言「What one fool can do, another can」が示す、微積分学習において直観が形式主義に先行すべき理由を論ぜよ。",
            "積分記号 $\\int$ がなぜ文字「S」の引き伸ばしとして考案されたか、その歴史的背景を述べよ。"
        ],
        2: [
            "一辺 $x$ の立方体の体積 $(x+dx)^3$ を展開し、なぜ2次および3次の微小量が極限で消去されるか説明せよ。",
            "100万ポンドに対する1ペニーの比率を計算し、微小量の無視が近似としてどれほど高精度か考察せよ。",
            "物理学における「1次近似（微小振動の線形化）」の重要性を述べよ。"
        ],
        3: [
            "平均変化率 $\\frac{\\Delta y}{\\Delta x}$ と瞬間変化率 $\\frac{dy}{dx}$ の違いを、速度計の動作に例えて説明せよ。",
            "放物線 $y = x^2$ の $x = 2$ における接線の方程式を導関数の定義から導け。",
            "関数が「滑らかである（微分可能である）」とは、幾何学的に何を意味するか述べよ。"
        ],
        4: [
            "二項定理を用いて、自然数 $n$ に対する公式 $\\frac{d}{dx}(x^n) = n x^{n-1}$ を証明せよ。",
            "関数 $y = \\frac{1}{x^3}$ および $y = \\sqrt[3]{x}$ の導関数を求めよ。",
            "定数関数の微分がゼロになる理由を、幾何学的傾きの観点から説明せよ。"
        ],
        5: [
            "長方形の面積モデルを用いて、積の微分公式 $(uv)' = u'v + uv'$ を幾何学的に図解・説明せよ。",
            "商の微分公式を用いて、関数 $y = \\frac{2x+1}{x-3}$ を微分せよ。",
            "3つの関数の積 $(uvw)'$ の公式を導出せよ。"
        ],
        6: [
            "連鎖律 $\\frac{dy}{dx} = \\frac{dy}{du}\\frac{du}{dx}$ を、ギア比（歯車の連動）のアナロジーを用いて説明せよ。",
            "関数 $y = (2x^3 - 1)^5$ および $y = \\sqrt{4 - x^2}$ を微分せよ。",
            "逆関数の微分公式 $\\frac{dx}{dy} = \\frac{1}{dy/dx}$ の幾何学的意味を論ぜよ。"
        ],
        7: [
            "第2次導関数 $\\frac{d^2y}{dx^2}$ が、曲線の「凹凸（曲がり具合）」を示す理由を説明せよ。",
            "物体の位置が $s(t) = t^3 - 6t^2 + 9t$ で表されるとき、速度がゼロになる時刻と、そのときの加速度を求めよ。",
            "ニュートンの運動方程式 $F = m\\frac{d^2x}{dt^2}$ がなぜ「第2階微分方程式」であるか述べよ。"
        ],
        8: [
            "極大点と極小点において、なぜ必ず1次導関数がゼロ（$\\frac{dy}{dx} = 0$）になるかフェルマーの原理から説明せよ。",
            "関数 $y = x^3 - 3x$ の増減表を作成し、極大値・極小値を求めよ。",
            "2次導関数を用いた極値の判別法（$\\frac{d^2y}{dx^2} \\gtrless 0$）の有効性と限界を論ぜよ。"
        ],
        9: [
            "連続複利の極限 $\\lim_{n\\to\\infty}\\left(1 + \\frac{1}{n}\\right)^n$ からネイピア数 $e$ が定義される過程を説明せよ。",
            "関数 $y = e^x$ の微分がなぜ自分自身になるのか、その直観的証明を述べよ。",
            "自然対数 $y = \\ln x$ の導関数が $\\frac{1}{x}$ となることを、逆関数の微分法から示せ。"
        ],
        10: [
            "度数法ではなく弧度法（ラジアン）を用いたときにのみ $\\lim_{\\theta\\to 0}\\frac{\\sin\\theta}{\\theta} = 1$ が成立する理由を説明せよ。",
            "等速円運動の射影から、$\\frac{d}{dx}(\\sin x) = \\cos x$ と $\\frac{d}{dx}(\\cos x) = -\\sin x$ を導け。",
            "単振動の方程式 $\\frac{d^2y}{dx^2} = -\\omega^2 y$ の解が三角関数となる理由を考察せよ。"
        ],
        11: [
            "「積分とは過程の逆行である」というトンプソンの思想と、積分定数 $C$ の必然性を論ぜよ。",
            "なぜ $\\int x^{-1} dx$ においてベキ関数の積分公式が使えず、自然対数が出現するのか説明せよ。",
            "置換積分法と部分積分法の公式を、微分の合成関数・積の微分公式から導出せよ。"
        ],
        12: [
            "区分求積法（リーマン和）において、短冊の幅をゼロに近づけたとき定積分へと収束するメカニズムを解説せよ。",
            "微積分学の基本定理 $\\frac{d}{dx}\\left(\\int_a^x f(t)dt\\right) = f(x)$ を幾何学的に証明せよ。",
            "現代の人工知能（ニューラルネットワークの勾配降下法）において導関数がどのように活用されているか論ぜよ。"
        ]
    }
    items = exercises.get(num, ["問題1", "問題2", "問題3"])
    return f"""\\section*{{第{num}章の確認演習}}
\\addcontentsline{{toc}}{{section}}{{第{num}章の確認演習}}
\\begin{{enumerate}}[label=\\textbf{{問\\arabic*.}}]
\\item {items[0]}
\\item {items[1]}
\\item {items[2]}
\\end{{enumerate}}
"""

def get_glossary_and_final_exercises():
    return r'''\chapter*{付録：高校生のための微積分重要用語辞典}
\addcontentsline{toc}{chapter}{付録：高校生のための微積分重要用語辞典}
\markboth{付録：微積分重要用語辞典}{付録：微積分重要用語辞典}

本書で登場した極めて重要かつ本質的な数学・物理の用語を、トンプソンの直観的視点から整理した解説集である。

\begin{description}[leftmargin=3.5cm, style=nextline]
\item[微小量（Differential, $dx, dy$）]
ゼロではないが、あらゆる通常の測定可能な有限量と比べて極めて微小な増分。トンプソンはこれを「ほんの少しのかけら（a little bit of）」と表現した。

\item[小ささの階級（Degrees of Smallness）]
1次微小量 $dx$ に対し、2次微小量 $(dx)^2$ や $dx \cdot dy$ は桁違いに小さく、極限操作において正当に無視できるという近代微積分の近似原理。

\item[導関数（Derivative, $\frac{dy}{dx}$）]
変数 $x$ の微小な成長に対する変数 $y$ の微小な成長の比率（相対的成長度）。グラフ上ではその点における接線の傾きを表す。

\item[平均変化率（Average Rate of Change）]
区間 $[x, x + \Delta x]$ における関数の平均的な変化の傾き $\frac{\Delta y}{\Delta x} = \frac{f(x+\Delta x) - f(x)}{\Delta x}$。

\item[瞬間変化率（Instantaneous Rate of Change）]
平均変化率の区間幅 $\Delta x$ を限りなくゼロに近づけた極限値。スピードメーターが指すその瞬間の速度。

\item[接線（Tangent Line）]
曲線上の点において、曲線の局所的な進行方向と完全に一致する直線。傾きは導関数 $f'(x)$ に等しい。

\item[ベキ関数の微分公式]
自然数、負数、分数を含む任意の実数指数 $n$ に対し、$\frac{d}{dx}(x^n) = n x^{n-1}$ が成立するという微積分の基本定理。

\item[積の微分公式（Product Rule）]
2つの関数 $u, v$ の積の導関数は $(uv)' = u'v + uv'$ となる。長方形の面積拡大モデルにより直観的に証明される。

\item[商の微分公式（Quotient Rule）]
分数の導関数は $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ となる。分母の増大が商を減少させるため分子にマイナス符号が現れる。

\item[連鎖律（Chain Rule）]
合成関数 $y = f(g(x))$ に対し、中間変数 $u = g(x)$ を介して $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$ と分解・計算する強力な技法（トンプソンの「便利な裏技」）。

\item[第2次導関数（Second Derivative, $\frac{d^2y}{dx^2}$）]
導関数をさらに微分したもの。曲線の曲がり具合（凹凸）や、物理における加速度（速度の変化率）を表す。

\item[極大値・極小値（Maxima and Minima）]
関数が局所的に最大または最小となる値。その地点では接線が水平（$\frac{dy}{dx} = 0$）となり、2次導関数の符号によって山（$< 0$）か谷（$> 0$）かが判定される。

\item[変曲点（Inflection Point）]
曲線の凹凸（上に凸と下に凸）が入れ替わる境界点。第2次導関数がゼロ（$\frac{d^2y}{dx^2} = 0$）となる。

\item[ネイピア数（Napier's Constant, $e$）]
連続複利の極限 $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = 2.71828\dots$ で定義される超越数。関数 $y = e^x$ は微分しても自分自身のままである唯一無二の性質を持つ。

\item[自然対数（Natural Logarithm, $\ln x$）]
ネイピア数 $e$ を底とする対数。その導関数は $\frac{d}{dx}(\ln x) = \frac{1}{x}$ となり、反比例関数の原始関数を与える。

\item[弧度法（Radian）]
半径と弧長の比によって角度を定義する単位系。三角関数の極限 $\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$ を保証し、微積分を美しく成立させる。

\item[不定積分（Indefinite Integral, $\int f(x) dx$）]
微分の逆演算として、導関数 $f(x)$ から元の関数（原始関数）$F(x) + C$ を復元する操作。

\item[積分定数（Constant of Integration, $C$）]
定数は微分するとゼロになるため、積分によって復元する際に生じる任意定数。初期条件によって特定される。

\item[定積分（Definite Integral, $\int_a^b f(x) dx$）]
区間 $[a, b]$ における微小短冊 $f(x)dx$ の無限和。曲線と $x$ 軸で囲まれた符号付き面積を表す。

\item[微積分学の基本定理（Fundamental Theorem of Calculus）]
微分と積分が表裏一体の逆演算であり、面積関数 $S(x)$ の導関数が元の関数の高さ $f(x)$ に等しいという大定理：$\int_a^b f(x)dx = F(b) - F(a)$。
\end{description}

\chapter*{付録：高校数学総合演習問題と詳細解説}
\addcontentsline{toc}{chapter}{付録：高校数学総合演習問題と詳細解説}
\markboth{付録：高校数学総合演習問題}{付録：高校数学総合演習問題}

全12章で学んだトンプソン流微積分の理論を総合的に活用する、大学入試・実践レベルの演習問題である。

\section*{【総合演習問題】}

\begin{enumerate}[label=\textbf{第\arabic*問.}]
\item 関数 $f(x) = x^3 - 6x^2 + 9x + 2$ について、次の問いに答えよ。
\begin{enumerate}
\item 導関数 $f'(x)$ および第2次導関数 $f''(x)$ を求めよ。
\item 増減表を作成し、極大値・極小値および変曲点の座標を求めよ。
\item $x \ge 0$ における曲線 $y = f(x)$ の概形を描け。
\end{enumerate}

\item 半径 $R$ の球に内接する直円柱を考える。
\begin{enumerate}
\item 円柱の底面の半径を $r$、高さを $2h$ とするとき、$r, h, R$ の関係式を求めよ。
\item 円柱の体積 $V$ を $h$ の関数として表せ。
\item 円柱の体積 $V$ が最大となるときの高さ $2h$ および最大体積 $V_{\text{max}}$ を $R$ を用いて表せ。
\end{enumerate}

\item 次の不定積分および定積分を計算せよ。
\begin{enumerate}
\item $\int (3x^2 - 4x + 1)\,dx$
\item $\int \left(e^{2x} + \frac{1}{x}\right)dx \quad (x > 0)$
\item $\int_0^{\pi} \sin(x)\,dx$
\item $\int_1^2 \left(x + \frac{1}{x^2}\right)dx$
\end{enumerate}

\item 放物線 $y = 4 - x^2$ と直線 $y = x + 2$ について、次の問いに答えよ。
\begin{enumerate}
\item 放物線と直線の交点の $x$ 座標を求めよ。
\item 放物線と直線で囲まれた図形の面積 $S$ を定積分を用いて求めよ。
\end{enumerate}

\item 地上から初速度 $v_0$、仰角 $\theta$ で打ち出された物体の運動を考える（空気抵抗は無視し、重力加速度を $g$ とする）。
\begin{enumerate}
\item 水平方向の位置 $x(t)$ および鉛直方向の位置 $y(t)$ を時間の関数として表せ。
\item 軌道方程式 $y = f(x)$ を求めよ。
\item 水平到達距離 $X$ が最大となる仰角 $\theta$ を、微分の考え方を用いて導け。
\end{enumerate}
\end{enumerate}

\newpage
\section*{【総合演習問題の解答・解説】}

\subsection*{第1問の解答}
(a) $f(x) = x^3 - 6x^2 + 9x + 2$ に対し、\\
$f'(x) = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x - 1)(x - 3)$。\\
$f''(x) = 6x - 12 = 6(x - 2)$。\\
(b) $f'(x) = 0$ となるのは $x = 1, 3$。\\
$x = 1$ のとき、$f(1) = 1 - 6 + 9 + 2 = 6$。$f''(1) = -6 < 0$ より極大値 $6$。\\
$x = 3$ のとき、$f(3) = 27 - 54 + 27 + 2 = 2$。$f''(3) = 6 > 0$ より極小値 $2$。\\
変曲点は $f''(x) = 0$ となる $x = 2$ であり、座標は $(2, f(2)) = (2, 4)$ である。\\
(c) 曲線は $(0, 2)$ から出発し、$(1, 6)$ で極大となり、$(2, 4)$ で凹凸が反転し、$(3, 2)$ で極小となった後、右肩上がりに急上昇する三次曲線となる。

\subsection*{第2問の解答}
(a) 球の中心を原点にとると、円柱の上底面の縁は球面上にあるため、三平方の定理より $r^2 + h^2 = R^2$、すなわち $r^2 = R^2 - h^2$（ただし $0 < h < R$）。\\
(b) 円柱の底面積は $\pi r^2 = \pi(R^2 - h^2)$、高さは $2h$ であるから、体積は\\
$V(h) = \pi(R^2 - h^2)(2h) = 2\pi(R^2 h - h^3)$。\\
(c) $V(h)$ を $h$ で微分して極大値を求める：\\
$\frac{dV}{dh} = 2\pi(R^2 - 3h^2)$。\\
$\frac{dV}{dh} = 0$ とおくと、$h > 0$ より $h = \frac{R}{\sqrt{3}} = \frac{\sqrt{3}}{3}R$。\\
$\frac{d^2V}{dh^2} = -12\pi h < 0$ より、このとき体積は最大となる。\\
求める高さは $2h = \frac{2\sqrt{3}}{3}R$。\\
最大体積は $V_{\text{max}} = 2\pi\left(R^2 \cdot \frac{R}{\sqrt{3}} - \frac{R^3}{3\sqrt{3}}\right) = 2\pi \cdot \frac{2R^3}{3\sqrt{3}} = \frac{4\sqrt{3}\pi}{9}R^3$ である。

\subsection*{第3問の解答}
(a) $\int (3x^2 - 4x + 1)dx = x^3 - 2x^2 + x + C$。\\
(b) 連鎖律の逆より $\int e^{2x}dx = \frac{1}{2}e^{2x}$。したがって $\frac{1}{2}e^{2x} + \ln|x| + C$。\\
(c) $[-\cos(x)]_0^{\pi} = (-\cos\pi) - (-\cos 0) = -(-1) - (-1) = 1 + 1 = 2$。\\
(d) $\left[\frac{x^2}{2} - \frac{1}{x}\right]_1^2 = \left(2 - \frac{1}{2}\right) - \left(\frac{1}{2} - 1\right) = \frac{3}{2} - \left(-\frac{1}{2}\right) = 2$。

\subsection*{第4問の解答}
(a) 交点の方程式は $4 - x^2 = x + 2 \iff x^2 + x - 2 = 0 \iff (x + 2)(x - 1) = 0$。\\
交点の $x$ 座標は $x = -2, 1$。\\
(b) 区間 $[-2, 1]$ において放物線が直線の上側にある（$4 - x^2 \ge x + 2$）。\\
面積 $S = \int_{-2}^1 \{(4 - x^2) - (x + 2)\}dx = \int_{-2}^1 (-x^2 - x + 2)dx$。\\
これは有名な $\frac{1}{6}$ 公式 $S = \frac{1}{6}(\beta - \alpha)^3$ の形である：\\
$S = \frac{1}{6}(1 - (-2))^3 = \frac{1}{6}(3)^3 = \frac{27}{6} = \frac{9}{2} = 4.5$。

\subsection*{第5問の解答}
(a) 水平方向は等速直線運動：$x(t) = (v_0 \cos\theta)t$。\\
鉛直方向は等加速度運動：$y(t) = (v_0 \sin\theta)t - \frac{1}{2}gt^2$。\\
(b) $t = \frac{x}{v_0 \cos\theta}$ を $y(t)$ に代入すると、軌道方程式は\\
$y = (\tan\theta)x - \frac{g}{2v_0^2 \cos^2\theta}x^2$。\\
(c) 再び地面（$y = 0$）に落下する時刻は $t = \frac{2v_0 \sin\theta}{g}$。\\
このときの水平到達距離は\\
$X(\theta) = (v_0 \cos\theta) \cdot \frac{2v_0 \sin\theta}{g} = \frac{v_0^2}{g}(2\sin\theta\cos\theta) = \frac{v_0^2}{g}\sin(2\theta)$。\\
$X(\theta)$ を $\theta$ で微分すると $\frac{dX}{d\theta} = \frac{2v_0^2}{g}\cos(2\theta)$。\\
$\frac{dX}{d\theta} = 0$ とおくと $2\theta = 90^\circ \implies \theta = 45^\circ$。\\
$\theta = 45^\circ$ のとき水平到達距離は最大値 $X_{\text{max}} = \frac{v_0^2}{g}$ となる。
'''

if __name__ == '__main__':
    build_thompson_tex()
