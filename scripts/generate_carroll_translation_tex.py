# -*- coding: utf-8 -*-
"""
Generate LuaLaTeX document for Lewis Carroll #4763
"The Game of Logic" (原著全4章 完全翻訳・TikZ図版完全再現・数学校閲版)
"""

import json
import os
from carroll_chapters_ch1_ch2 import FRONTMATTER_TEX, CHAPTER_I_JA, CHAPTER_II_JA
from carroll_chapters_ch3_ch4 import CHAPTER_III_JA, CHAPTER_IV_JA

CACHE_FILE = "books/4763_carroll_game_of_logic/carroll_full_translation_math_verified.json"
OUTPUT_TEX = "books/4763_carroll_game_of_logic/carroll_game_of_logic_translation.tex"

TITLES = {
    "I": ("第1章", "古きを捨てて新しきを（New Lamps for Old）", "命題論・三段論法・誤謬論と正方形ダイアグラムによる論理表現"),
    "II": ("第2章", "問いかけの数々（Cross Questions）", "大小ダイアグラムへの命題配置・記号解釈と演習問題体系"),
    "III": ("第3章", "歪んだ答え（Crooked Answers）", "三段論法とダイアグラム配置の詳細解答と記号論理的解法"),
    "IV": ("第4章", "当たるも八卦当たらぬも八卦（Hit or Miss）", "総合論理パズル・誤謬の看破とゲームとしての記号論理")
}

CHAPTER_CONTENT = {
    "I": CHAPTER_I_JA,
    "II": CHAPTER_II_JA,
    "III": CHAPTER_III_JA,
    "IV": CHAPTER_IV_JA
}

def main():
    # Update JSON cache so that it stores the verified translations
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    for num, content in CHAPTER_CONTENT.items():
        key = f"Chapter_{num}"
        if key not in data:
            data[key] = {"number": num, "title_en": f"CHAPTER {num}."}
        data[key]["japanese_translation"] = content.strip()

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated verified JSON cache: {CACHE_FILE}")

    preamble = r"""\documentclass[a4paper,11pt,openany]{ltjsbook}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{geometry}
\geometry{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{fancyhdr}

\definecolor{carrollred}{RGB}{185, 30, 45}
\definecolor{carrollgrey}{RGB}{90, 98, 110}
\definecolor{boardbg}{RGB}{252, 250, 245}
\definecolor{innerbg}{RGB}{244, 240, 230}
\definecolor{softpink}{RGB}{253, 246, 247}
\definecolor{darkslate}{RGB}{30, 35, 45}
\definecolor{boxframe}{RGB}{140, 50, 60}

\hypersetup{
    colorlinks=true,
    linkcolor=carrollred,
    citecolor=carrollgrey,
    urlcolor=carrollred
}

\pagestyle{fancy}
\setlength{\headheight}{32pt}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\headrulewidth}{0.4pt}

% ============================================================================
% Lewis Carroll 'The Game of Logic' TikZ Diagram Macros
% ============================================================================
% Counter tokens: Red ('1' = occupied) and Grey ('0' = empty)
\newcommand{\tokRed}[2]{%
  \filldraw[fill=carrollred, draw=white, double=carrollred!75!black, double distance=0.4pt, line width=0.5pt] (#1,#2) circle (0.20cm);
  \node[white, font=\sffamily\bfseries\footnotesize] at (#1,#2) {1};
}
\newcommand{\tokGrey}[2]{%
  \filldraw[fill=carrollgrey, draw=white, double=carrollgrey!75!black, double distance=0.4pt, line width=0.5pt] (#1,#2) circle (0.20cm);
  \node[white, font=\sffamily\bfseries\footnotesize] at (#1,#2) {0};
}
\newcommand{\carrollTok}[3]{%
  \ifx&#1&\else
    \ifnum#1=1\relax
      \tokRed{#2}{#3}%
    \else
      \tokGrey{#2}{#3}%
    \fi
  \fi
}

% Fence token helpers for Larger Diagram
\newcommand{\fN}{\tokRed{0}{0.42}}
\newcommand{\fS}{\tokRed{0}{-0.42}}
\newcommand{\fW}{\tokRed{-1.22}{0}}
\newcommand{\fE}{\tokRed{1.22}{0}}

% 1. Horizontal 2-compartment oblong: \carrollHorizTwo{left}{right}{fence}
\newcommand{\carrollHorizTwo}[3]{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.0]
    \fill[boardbg] (-1.1,-0.5) rectangle (1.1,0.5);
    \draw[line width=0.9pt, darkslate] (-1.1,-0.5) rectangle (1.1,0.5);
    \draw[line width=0.7pt, darkslate] (0,-0.5) -- (0,0.5);
    \carrollTok{#1}{-0.55}{0}
    \carrollTok{#2}{0.55}{0}
    \carrollTok{#3}{0}{0}
  \end{tikzpicture}%
}

% 2. Vertical 2-compartment oblong: \carrollVertTwo{top}{bottom}{fence}
\newcommand{\carrollVertTwo}[3]{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.0]
    \fill[boardbg] (-0.55,-1.0) rectangle (0.55,1.0);
    \draw[line width=0.9pt, darkslate] (-0.55,-1.0) rectangle (0.55,1.0);
    \draw[line width=0.7pt, darkslate] (-0.55,0) -- (0.55,0);
    \carrollTok{#1}{0}{0.5}
    \carrollTok{#2}{0}{-0.5}
    \carrollTok{#3}{0}{0}
  \end{tikzpicture}%
}

% 3. Smaller Diagram (2x2): \carrollSmall{c5}{c6}{c7}{c8}{fN}{fS}{fW}{fE}
\newcommand{\carrollSmall}[8]{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.0]
    \fill[boardbg] (-1.0,-1.0) rectangle (1.0,1.0);
    \draw[line width=0.9pt, darkslate] (-1.0,-1.0) rectangle (1.0,1.0);
    \draw[line width=0.7pt, darkslate] (-1.0,0) -- (1.0,0);
    \draw[line width=0.7pt, darkslate] (0,-1.0) -- (0,1.0);
    \carrollTok{#1}{-0.5}{0.5}
    \carrollTok{#2}{0.5}{0.5}
    \carrollTok{#3}{-0.5}{-0.5}
    \carrollTok{#4}{0.5}{-0.5}
    \carrollTok{#5}{0}{0.5}
    \carrollTok{#6}{0}{-0.5}
    \carrollTok{#7}{-0.5}{0}
    \carrollTok{#8}{0.5}{0}
  \end{tikzpicture}%
}

% 4. Partial Larger Diagrams (Chapter I)
% Upper half: \carrollLargeTop{c9}{c10}{c11}{c12}{fN_in}
\newcommand{\carrollLargeTop}[5]{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.0]
    \fill[boardbg] (-1.6,0) rectangle (1.6,1.6);
    \fill[innerbg] (-0.85,0) rectangle (0.85,0.85);
    \draw[line width=0.9pt, darkslate] (-1.6,0) rectangle (1.6,1.6);
    \draw[line width=0.7pt, darkslate] (-0.85,0) rectangle (0.85,0.85);
    \draw[line width=0.7pt, darkslate] (0,0) -- (0,1.6);
    \carrollTok{#1}{-1.22}{1.15}
    \carrollTok{#2}{1.22}{1.15}
    \carrollTok{#3}{-0.42}{0.42}
    \carrollTok{#4}{0.42}{0.42}
    \carrollTok{#5}{0}{0.42}
  \end{tikzpicture}%
}

% Lower half: \carrollLargeBottom{c13}{c14}{c15}{c16}{fS_in}
\newcommand{\carrollLargeBottom}[5]{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.0]
    \fill[boardbg] (-1.6,-1.6) rectangle (1.6,0);
    \fill[innerbg] (-0.85,-0.85) rectangle (0.85,0);
    \draw[line width=0.9pt, darkslate] (-1.6,-1.6) rectangle (1.6,0);
    \draw[line width=0.7pt, darkslate] (-0.85,-0.85) rectangle (0.85,0);
    \draw[line width=0.7pt, darkslate] (0,-1.6) -- (0,0);
    \carrollTok{#1}{-0.42}{-0.42}
    \carrollTok{#2}{0.42}{-0.42}
    \carrollTok{#3}{-1.22}{-1.15}
    \carrollTok{#4}{1.22}{-1.15}
    \carrollTok{#5}{0}{-0.42}
  \end{tikzpicture}%
}

% Right half: \carrollLargeRight{c10}{c12}{c14}{c16}{fE_out}
\newcommand{\carrollLargeRight}[5]{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.0]
    \fill[boardbg] (0,-1.6) rectangle (1.6,1.6);
    \fill[innerbg] (0,-0.85) rectangle (0.85,0.85);
    \draw[line width=0.9pt, darkslate] (0,-1.6) rectangle (1.6,1.6);
    \draw[line width=0.7pt, darkslate] (0,-0.85) rectangle (0.85,0.85);
    \draw[line width=0.7pt, darkslate] (0,0) -- (1.6,0);
    \carrollTok{#1}{1.22}{1.15}
    \carrollTok{#2}{0.42}{0.42}
    \carrollTok{#3}{0.42}{-0.42}
    \carrollTok{#4}{1.22}{-1.15}
    \carrollTok{#5}{1.22}{0}
  \end{tikzpicture}%
}

% 5. Full Larger Diagram (8 compartments): \carrollLarge{c9}{c10}{c11}{c12}{c13}{c14}{c15}{c16}{fences}
\newcommand{\carrollLarge}[9]{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=0.95]
    \fill[boardbg] (-1.6,-1.6) rectangle (1.6,1.6);
    \fill[innerbg] (-0.85,-0.85) rectangle (0.85,0.85);
    \draw[line width=0.9pt, darkslate] (-1.6,-1.6) rectangle (1.6,1.6);
    \draw[line width=0.8pt, darkslate] (-0.85,-0.85) rectangle (0.85,0.85);
    \draw[line width=0.7pt, darkslate] (-1.6,0) -- (1.6,0);
    \draw[line width=0.7pt, darkslate] (0,-1.6) -- (0,1.6);
    \carrollTok{#1}{-1.22}{1.22}
    \carrollTok{#2}{1.22}{1.22}
    \carrollTok{#3}{-0.42}{0.42}
    \carrollTok{#4}{0.42}{0.42}
    \carrollTok{#5}{-0.42}{-0.42}
    \carrollTok{#6}{0.42}{-0.42}
    \carrollTok{#7}{-1.22}{-1.22}
    \carrollTok{#8}{1.22}{-1.22}
    #9
  \end{tikzpicture}%
}

% 6. Labeled Reference Diagrams for Section Headers & Frontispiece
\newcommand{\carrollLabeledHorizX}{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.1]
    \fill[boardbg] (-1.2,-0.55) rectangle (1.2,0.55);
    \draw[line width=0.9pt, darkslate] (-1.2,-0.55) rectangle (1.2,0.55);
    \draw[line width=0.7pt, darkslate] (0,-0.55) -- (0,0.55);
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0,0) {$x$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (-0.6,-0.55) {$y$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0.6,-0.55) {$y'$};
  \end{tikzpicture}%
}

\newcommand{\carrollLabeledVertY}{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.1]
    \fill[boardbg] (-0.55,-1.1) rectangle (0.55,1.1);
    \draw[line width=0.9pt, darkslate] (-0.55,-1.1) rectangle (0.55,1.1);
    \draw[line width=0.7pt, darkslate] (-0.55,0) -- (0.55,0);
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0,0) {$y$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0.55,0.55) {$x$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0.55,-0.55) {$x'$};
  \end{tikzpicture}%
}

\newcommand{\carrollLabeledVertYPrime}{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.1]
    \fill[boardbg] (-0.55,-1.1) rectangle (0.55,1.1);
    \draw[line width=0.9pt, darkslate] (-0.55,-1.1) rectangle (0.55,1.1);
    \draw[line width=0.7pt, darkslate] (-0.55,0) -- (0.55,0);
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0,0) {$y'$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (-0.55,0.55) {$x$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (-0.55,-0.55) {$x'$};
  \end{tikzpicture}%
}

\newcommand{\carrollLabeledSmall}{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.15]
    \fill[boardbg] (-1.1,-1.1) rectangle (1.1,1.1);
    \draw[line width=0.9pt, darkslate] (-1.1,-1.1) rectangle (1.1,1.1);
    \draw[line width=0.7pt, darkslate] (-1.1,0) -- (1.1,0);
    \draw[line width=0.7pt, darkslate] (0,-1.1) -- (0,1.1);
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0,0.55) {$x$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0,-0.55) {$x'$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (-0.55,0) {$y$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0.55,0) {$y'$};
  \end{tikzpicture}%
}

\newcommand{\carrollLabeledLarge}{%
  \begin{tikzpicture}[baseline=-0.5ex, scale=1.1]
    \fill[boardbg] (-1.6,-1.6) rectangle (1.6,1.6);
    \fill[innerbg] (-0.85,-0.85) rectangle (0.85,0.85);
    \draw[line width=0.9pt, darkslate] (-1.6,-1.6) rectangle (1.6,1.6);
    \draw[line width=0.8pt, darkslate] (-0.85,-0.85) rectangle (0.85,0.85);
    \draw[line width=0.7pt, darkslate] (-1.6,0) -- (1.6,0);
    \draw[line width=0.7pt, darkslate] (0,-1.6) -- (0,1.6);
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0,0.85) {$x$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0,-0.85) {$x'$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (-0.85,0) {$y$};
    \node[fill=boardbg, inner sep=1.5pt, font=\normalsize] at (0.85,0) {$y'$};
    \node[fill=innerbg, inner sep=1.5pt, font=\normalsize] at (0,0) {$m$};
  \end{tikzpicture}%
}

\newcommand{\carrollLabeledBoth}{%
  \carrollLabeledLarge \hspace{10mm} \carrollLabeledSmall
}

% 7. Full Frontispiece Board
\newcommand{\carrollFrontispiece}{%
  \begin{tikzpicture}[scale=1.05]
    % Outer card frame
    \filldraw[fill=softpink!40, draw=boxframe, line width=1.2pt, rounded corners=4pt] (-5.2,-4.8) rectangle (5.2,4.6);
    \draw[draw=boxframe!60, line width=0.5pt, rounded corners=3pt] (-5.05,-4.65) rectangle (5.05,4.45);

    % Larger Diagram (Top Center)
    \begin{scope}[shift={(0, 1.45)}]
      \fill[boardbg] (-2.3,-2.2) rectangle (2.3,2.2);
      \fill[innerbg] (-1.2,-1.15) rectangle (1.2,1.15);
      \draw[line width=1.1pt, darkslate] (-2.3,-2.2) rectangle (2.3,2.2);
      \draw[line width=0.9pt, darkslate] (-1.2,-1.15) rectangle (1.2,1.15);
      \draw[line width=0.8pt, darkslate] (-2.3,0) -- (2.3,0);
      \draw[line width=0.8pt, darkslate] (0,-2.2) -- (0,2.2);

      % Attribute Labels
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (0,1.15) {$x$};
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (0,-1.15) {$x'$};
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (-1.2,0) {$y$};
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (1.2,0) {$y'$};
      \node[fill=innerbg, inner sep=2pt, font=\large\bfseries] at (0,0) {$m$};

      % Compartment Numbers 9..16
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (-1.95, 1.90) {9};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (1.95, 1.90) {10};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (-0.90, 0.88) {11};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (0.90, 0.88) {12};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (-0.90, -0.88) {13};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (0.90, -0.88) {14};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (-1.95, -1.90) {15};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (1.95, -1.90) {16};
    \end{scope}

    % Colours for Counters (Bottom Left)
    \begin{scope}[shift={(-2.3, -2.65)}]
      \node[font=\bfseries\small, align=center, darkslate] at (0, 1.35) {COLOURS FOR COUNTERS\\{\footnotesize カウンター（駒）の色}};
      \draw[line width=0.5pt, darkslate] (-0.8, 0.95) -- (0.8, 0.95);

      \tokRed{-1.85}{0.35}
      \node[font=\footnotesize, align=center] at (0.2, 0.35) {頭上に輝く太陽を見よ、\\私たちを照らす、\textbf{\textcolor{carrollred}{満ちて（1）赤い}}光を！};

      \tokGrey{-1.85}{-0.65}
      \node[font=\footnotesize, align=center] at (0.2, -0.65) {いまや太陽は去りゆきて、\\\textbf{\textcolor{carrollgrey}{空っぽの（0）}}空は\textbf{\textcolor{carrollgrey}{灰色}}なり！};

      \draw[line width=0.5pt, darkslate] (-0.8, -1.25) -- (0.8, -1.25);
    \end{scope}

    % Smaller Diagram (Bottom Right)
    \begin{scope}[shift={(2.3, -2.65)}]
      \fill[boardbg] (-1.45,-1.45) rectangle (1.45,1.45);
      \draw[line width=1.1pt, darkslate] (-1.45,-1.45) rectangle (1.45,1.45);
      \draw[line width=0.8pt, darkslate] (-1.45,0) -- (1.45,0);
      \draw[line width=0.8pt, darkslate] (0,-1.45) -- (0,1.45);

      % Attribute Labels
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (0,0.72) {$x$};
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (0,-0.72) {$x'$};
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (-0.72,0) {$y$};
      \node[fill=boardbg, inner sep=2pt, font=\large\bfseries] at (0.72,0) {$y'$};

      % Compartment Numbers 5..8
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (-1.18, 1.18) {5};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (1.18, 1.18) {6};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (-1.18, -1.18) {7};
      \node[font=\sffamily\footnotesize\bfseries, darkslate!80] at (1.18, -1.18) {8};
    \end{scope}
  \end{tikzpicture}%
}

\title{\Huge\textbf{論理の遊戯}\\[4mm]
\huge\textbf{ゲームとダイアグラムで楽しむ三段論法と記号論理}\\[6mm]
\Large\textbf{—— 原著全4章 完全翻訳・TikZ図版完全再現・数学校閲版 ——}\\[5mm]
\large 原著：ルイス・キャロル（Lewis Carroll / Charles L. Dodgson, 1887）\\[2mm]
\normalsize Project Gutenberg eBook \#4763: \textit{The Game of Logic}}

\author{\textbf{ルイス・キャロル} 著\\[2mm]
\textbf{教育情報分析研究会} 訳・数理校閲}
\date{2026年10月 校訂第2版（TikZ完全図版化）}

\begin{document}

\maketitle

\frontmatter

\chapter*{解題：ルイス・キャロル『論理の遊戯』の数学的・論理学的意義}
\addcontentsline{toc}{chapter}{解題：ルイス・キャロル『論理の遊戯』の数学的・論理学的意義}

『不思議の国のアリス』の著者として世界中で親しまれているルイス・キャロル（本名：チャールズ・ラトウィッジ・ドジソン, 1832--1898）は、オックスフォード大学クライスト・チャーチで26年間にわたり数学講読講師（Mathematical Lecturer）を務めた本物の数学者・論理学者であった。

彼が1887年に著した『論理の遊戯』（\textit{The Game of Logic}）は、アリストテレス以来の伝統的・形式的論理学（三段論法）が持つ形式的な退屈さと難解さを一掃し、正方形のダイアグラム（盤面）と赤・灰のカウンター（駒）を用いて誰でもパズルのように論理推論を楽しめるように設計された、驚くべき先駆的著作である。

本書でキャロルが考案した二重・三重の正方形ダイアグラムは、ベン図（ジョン・ヴェン）と並び、現代のコンピュータ工学における「カルノー図（Karnaugh Map）」の原型をなすものであり、視覚的に論理の真理値や属性の包含関係を決定する画期的な手法であった。

本書は全4章から構成され、
\begin{enumerate}[label=\textbf{第\arabic*章:}]
    \item \textbf{古きを捨てて新しきを（New Lamps for Old）}：命題の本質、三段論法（Syllogism）、誤謬（Fallacies）の分類、および正方形ダイアグラムを用いた推論の基礎。
    \item \textbf{問いかけの数々（Cross Questions）}：小ダイアグラム・大ダイアグラムを用いた命題の表現と記号解釈の徹底演習問題群。
    \item \textbf{歪んだ答え（Crooked Answers）}：第2章の演習に対する詳細な模範解答と、三段論法の具体的導出プロセス。
    \item \textbf{当たるも八卦当たらぬも八卦（Hit or Miss）}：日々の生活や言語の中に潜む論理的推論と誤謬を見抜く総合論理パズル。
\end{enumerate}
を収載している。

本全訳版は、Project Gutenberg eBook \#4763として公開されている1887年初版テキストを底本とし、原著に収載されている全92個の論理ダイアグラム（巻頭図版、横2区画図、縦2区画図、4区画小ダイアグラム、8区画大ダイアグラム、および大小連動図）をすべて高精細な\textbf{TikZベクター図版（赤・灰カウンター駒付き）}として完全再現した決定版である。

""" + FRONTMATTER_TEX + r"""

\tableofcontents

\mainmatter
"""

    body_chapters = []
    order = ["I", "II", "III", "IV"]

    for num in order:
        ch_meta = TITLES[num]
        ch_title = ch_meta[1]
        ch_subtitle = ch_meta[2]
        ja_text = CHAPTER_CONTENT[num].strip()

        chapter_tex = f"""\\chapter{{{ch_title}}}
\\label{{ch:{num.lower()}}}

\\begin{{center}}
\\large\\textit{{{ch_subtitle}}}
\\end{{center}}
\\vspace{{4mm}}

{ja_text}
"""
        body_chapters.append(chapter_tex)

    postamble = r"""
\backmatter
\chapter*{奥付・翻訳校閲記録}
\addcontentsline{toc}{chapter}{奥付・翻訳校閲記録}

\begin{tcolorbox}[colback=softpink, colframe=boxframe, title={\textbf{書誌情報・翻訳校閲メタデータ}}]
\begin{itemize}
    \item \textbf{原書タイトル}: \textit{The Game of Logic} (1887年初版)
    \item \textbf{原著者}: Lewis Carroll (Charles Lutwidge Dodgson, 1832--1898)
    \item \textbf{底本}: Project Gutenberg eBook \#4763
    \item \textbf{図版組版}: TikZによる大小論理ダイアグラム・赤灰カウンター駒完全ベクター再現（全92図版）
    \item \textbf{組版エンジン}: LuaLaTeX (\texttt{ltjsbook} クラス)
\end{itemize}
\end{tcolorbox}

\end{document}
"""

    full_tex = preamble + "\n\n".join(body_chapters) + postamble

    os.makedirs(os.path.dirname(OUTPUT_TEX), exist_ok=True)
    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_tex)

    print(f"Successfully generated {OUTPUT_TEX} ({len(full_tex)} chars)")

if __name__ == "__main__":
    main()
