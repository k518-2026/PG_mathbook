# -*- coding: utf-8 -*-
"""
Lewis Carroll 'The Game of Logic' (#4763)
Verified Japanese Translation & TikZ Diagrams: Chapter III, Chapter IV
"""

CHAPTER_III_JA = r"""
\begin{center}
\textit{「われは良きと思うままに彼へと答えけり、\\
『森のなかに燻製ニシンが実るのと同数なり』と。」}
\end{center}

\section{基礎問題の解答（Elementary）}

\begin{enumerate}[label=\textbf{\arabic*.}]
\item ある事物に「帰属させることができる」、すなわち「それに属すると言える」ものは何であれ、\textbf{「属性（Attribute）」}と呼ばれる。たとえば、「焼きたての（baked）」は（しばしば）「菓子パン（Buns）」に帰属させることができ、「美しい（beautiful）」は（めったにないことだが）「赤ん坊（Babies）」に帰属させることができる。
\item それらが2つの\textbf{事物}の名前である場合（たとえば「これらの豚は太った動物である」）、または2つの\textbf{属性}の名前である場合（たとえば「ピンクは淡い赤である」）。
\item 一方が事物の名前であり、他方が属性の名前である場合（たとえば「これらの豚はピンクである」）。なぜなら、事物は実際に属性そのものにはなりえないからである。
\item 文末に主語の名詞（実詞）が繰り返されているものと見なすという取り決め（たとえば「これらの豚はピンクの（豚）である」）。
\item \textbf{「命題（Proposition）」}とは、「主辞（Subject）」と呼ばれるある特定のクラスに属する事物のうち、いくつか（some）、または皆無（none）、またはすべて（all）が、「賓辞（Predicate）」と呼ばれる別の特定のクラスに属する事物でもあることを述べる文である。たとえば、「いくつかの新しいケーキは美味しくない」は、（省略せずに書けば）「いくつかの新しいケーキは美味しくないケーキである」であり、ここで「新しいケーキ」というクラスが主辞、「美味しくないケーキ」というクラスが賓辞である。
\item 主辞に属する事物のうち\textbf{いくつか（SOME）}がしかじかであると述べる命題は\textbf{「特称命題（Particular）」}と呼ばれる。たとえば、「いくつかの新しいケーキは美味しい」「いくつかの新しいケーキは美味しくない」。

主辞に属する事物のうち\textbf{皆無（NONE）}が、あるいは\textbf{すべて（ALL）}がしかじかであると述べる命題は\textbf{「全称命題（Universal）」}と呼ばれる。たとえば、「どの新しいケーキも美味しくない」「すべての新しいケーキは美味しくない」。
\item 各区画（compartment）の中の事物は\textbf{2つの}属性を持っており、それらの記号はその区画の2つの\textbf{辺（EDGES）}に書かれている。
\item 「1つ以上（One or more）」。
\item ダイアグラム全体が割り当てられる事物のクラスの名前として用いられる。
\item 2つの主張（陳述）を含んでいる命題。たとえば、「いくつかの新しいケーキは美味しく、かついくつかは美味しくない」。
\item 分割されたクラス全体が、分割後の各組のあいだで「余すところなく汲み尽くされて（exhausted）」おり、それらの組のどれにも属さないような要素が1つも存在しないとき。たとえば、新しいケーキはすべて「美味しい」か「美味しくない」のどちらか一方でなければならないから、「新しいケーキ」というクラスは「美味しい」と「美味しくない」とに「網羅的に」分割されている。
\item 人が2つの政党（派閥）のどちらに加わるか決心がつかないとき、どちら側へ飛び降りるか決められない状態にあることから、「柵の上に座っている（sitting on the fence）」と言われる。
\item 「いくつかの $x$ は $y$ である（Some $x$ are $y$）」と「どの $x$ も $y'$ ではない（No $x$ are $y'$）」。
\item 主辞が単一の事物である命題を\textbf{「単称命題（個別命題, Individual）」}と呼ぶ。たとえば、「私は幸福である」「ジョンは在宅していない」。これらは「存在するすべての『私』は幸福である」「私がいま考察しているすべての『ジョン』は在宅していない」と同じ意味であるため、全称命題の一種である。
\item 「いくつかの（some）」または「すべての（all）」で始まる命題。
\item 「いくつかの（some）」または「どの〜も…ない（no）」で始まる命題の場合。たとえば、「いくつかの $abc$ は $def$ である」は「いくつかの $bf$ は $acde$ である」と並び替えることができ、いずれも「いくつかの $abcdef$ が存在する」と等価である。
\item 「いくつかのトラは獰猛である（Some tigers are fierce）」、および「どのトラも獰猛でないことはない（No tigers are not-fierce）」。
\item 「いくつかの固ゆで卵は消化に悪い（Some hard-boiled eggs are unwholesome）」、および「どの固ゆで卵も消化に良くない（No hard-boiled eggs are wholesome）」。
\item 「いくつかの『私』は幸福である（Some I's are happy）」、および「どの『私』も不幸ではない（No I's are unhappy）」。
\item 「いくつかの『ジョン』は在宅していない（Some Johns are not at home）」、および「どの『ジョン』も在宅していない（No Johns are at home）」。
\item 大ダイアグラムの各区画にある事物は\textbf{3つの}属性を持っており、それらの記号はその区画の3つの\textbf{角（CORNERS）}に書かれている（ただし $m'$ の場合は例外で、実際にはダイアグラムに書き込まれていないが、外側の4つの角のそれぞれに立っているものと\textbf{見なされる}）。
\item 事物の対象領域（宇宙）が3つの異なる属性に関して分割されており、それら3つの属性の異なる2組を含む2つの命題が与えられ、さらにそれらから、まだ同時に現れていない残りの2つの属性を含む第3の命題を証明できるとき、与えられた2つの命題を\textbf{「前提（the Premisses）」}、第3の命題を\textbf{「結論（the Conclusion）」}、その一揃い全体を\textbf{「三段論法（a Syllogism）」}と呼ぶ。たとえば、前提が「どの $m$ も $x'$ ではない」と「すべての $m'$ は $y$ である」であり、それらから $x$ と $y$ を含む結論を証明できるような場合である。
\item ある属性が両方の前提に共通して現れる場合、それを含む名辞は\textbf{「中名辞（the Middle Term）」}と呼ばれる。たとえば、前提が「いくつかの $m$ は $x$ である」と「どの $m$ も $y'$ ではない」である場合、「$m$-事物」のクラスが「中名辞」である。

ある属性が一方の前提に現れ、その矛盾属性（否定形）がもう一方の前提に現れる場合、それらを含む2つの名辞は\textbf{「複数の媒名辞（中項群, the Middle Terms）」}と呼ぶことができる。たとえば、前提が「どの $m$ も $x'$ ではない」と「すべての $m'$ は $y$ である」である場合、「$m$-事物」と「$m'$-事物」の2つのクラスが「複数の媒名辞」と呼ばれる。
\item 否定命題は\textbf{確実に（with CERTAINTY）}印づけることができるのに対し、\textbf{肯定}命題（「いくつかの」または「すべての」で始まるもの）は、時に赤いカウンターを「柵の上に座らせる（境界線上に置く）」必要が生じるからである。
\item 私たちが関心を払う唯一の問いは、結論が前提から\textbf{論理的に導かれるかどうか}——すなわち、もし前提が真で\textbf{あったならば}、結論もまた真で\textbf{あるか}どうか——だけだからである。
\item 赤いカウンターを「この区画は占有\textbf{されうる（CAN be occupied）}」という意味に理解し、灰色のカウンターを「この区画は占有\textbf{されえない（CANNOT be occupied）}」すなわち「この区画は\textbf{必ず空でなければならない（MUST be empty）}」という意味に理解することによって解くことができる。
\item \textbf{「誤謬的な前提（Fallacious Premisses）」}と\textbf{「誤謬的な結論（Fallacious Conclusion）」}の2種類。
\item 大ダイアグラムから小ダイアグラムへ印を移し替えようとした際に、小ダイアグラムの4つの区画のどれに対しても「情報なし（no information）」であることを見出すことによって検出できる。
\item 正しい結論を求めたうえで、提示された結論がその正しい結論と同一でもなく、その一部でもないことを観察することによって検出できる。
\item 提示された結論が正しい結論の\textbf{一部（PART）}であるとき。この場合、私たちはそれを\textbf{「不完全な結論（欠陥のある結論, Defective Conclusion）」}と呼ぶことができる。
\end{enumerate}

\section{小ダイアグラムの半分：命題の表現の解答（Half of Smaller Diagram. Propositions represented.）}

\begin{center}
\begin{tabular}{cccc}
\textbf{1.}\;\carrollHorizTwo{}{1}{} & \hspace{8mm} & \textbf{2.}\;\carrollHorizTwo{0}{1}{} \\[6mm]
\textbf{3.}\;\carrollHorizTwo{1}{1}{} & \hspace{8mm} & \textbf{4.}\;\carrollHorizTwo{0}{0}{} \\[6mm]
\textbf{5.}\;\carrollHorizTwo{}{}{1} & \hspace{8mm} & \textbf{6.}\;\carrollHorizTwo{}{0}{}
\end{tabular}
\end{center}

\vspace{2mm}
\noindent\textbf{7.}\;\carrollHorizTwo{}{1}{}\quad
「いくつかの $x$ が存在する」を表現するために、正しいダイアグラムは \carrollHorizTwo{}{1}{1} になると思われるかもしれない。しかし、これは実際には「いくつかの $x$ は $y'$ である」の中にすでに含まれているのである。分割線（境界線）の上に赤いカウンターを置くことは、単に「区画の\textbf{どちらか一方}が占有されている」と教えてくれるにすぎないが、片方が占有されていることを知っている以上、それはすでに分かっていることなのである。

\begin{itemize}[label={}, leftmargin=0pt, itemsep=3mm]
\item \textbf{8.} どの $x$ も $y$ ではない。すなわち \carrollHorizTwo{0}{}{}
\item \textbf{9.} いくつかの $x$ は $y'$ である。すなわち \carrollHorizTwo{}{1}{}
\item \textbf{10.} すべての $x$ は $y$ である。すなわち \carrollHorizTwo{1}{0}{}
\item \textbf{11.} いくつかの $x$ は $y$ である。すなわち \carrollHorizTwo{1}{}{}
\item \textbf{12.} どの $x$ も $y$ ではない。すなわち \carrollHorizTwo{0}{}{}
\item \textbf{13.} いくつかの $x$ は $y$ であり、かついくつかは $y'$ である。すなわち \carrollHorizTwo{1}{1}{}
\item \textbf{14.} すべての $x$ は $y'$ である。すなわち \carrollHorizTwo{0}{1}{}
\item \textbf{15.} どの $y$ も $x'$ ではない。すなわち \carrollVertTwo{}{0}{}
\item \textbf{16.} すべての $y$ は $x$ である。すなわち \carrollVertTwo{1}{0}{}
\item \textbf{17.} $y$ は1つも存在しない。すなわち \carrollVertTwo{0}{0}{}
\item \textbf{18.} いくつかの $y$ は $x'$ である。すなわち \carrollVertTwo{}{1}{}
\item \textbf{19.} {\small（原著表記 15.）} いくつかの $y$ が存在する。すなわち \carrollVertTwo{}{}{1}
\end{itemize}

\section{小ダイアグラムの半分：記号の解釈の解答（Half of Smaller Diagram. Symbols interpreted.）}

\begin{enumerate}[label=\textbf{\arabic*.}]
\item どの $x$ も $y'$ ではない。（No $x$ are $y'$.）
\item $x$ は1つも存在しない。（No $x$ exist.）
\item いくつかの $x$ が存在する。（Some $x$ exist.）
\item すべての $x$ は $y'$ である。（All $x$ are $y'$.）
\item いくつかの $x$ は $y$ である。すなわち、いくつかの良いなぞなぞは難しい。
\item すべての $x$ は $y$ である。すなわち、すべての良いなぞなぞは難しい。
\item $x$ は1つも存在しない。すなわち、良いなぞなぞは1つもない。
\item どの $x$ も $y$ ではない。すなわち、どの良いなぞなぞも難しくない。
\item いくつかの $x$ は $y'$ である。すなわち、いくつかのロブスターは無欲（利他的）である。
\item どの $x$ も $y$ ではない。すなわち、どのロブスターも利己的ではない。
\item すべての $x$ は $y'$ である。すなわち、すべてのロブスターは無欲である。
\item いくつかの $x$ は $y$ であり、かついくつかは $y'$ である。すなわち、いくつかのロブスターは利己的であり、かついくつかは無欲である。
\item すべての $y'$ は $x'$ である。すなわち、すべての病弱な人（不健康な人, invalids）は不幸である。
\item いくつかの $y'$ が存在する。すなわち、いくつかの人々は不健康である。
\item いくつかの $y'$ は $x$ であり、かついくつかは $x'$ である。すなわち、いくつかの病弱な人は幸福であり、かついくつかは不幸である。
\item $y'$ は1人も存在しない。すなわち、不健康な人は誰ひとりいない。
\end{enumerate}

\section{小ダイアグラム：命題の表現の解答（Smaller Diagram. Propositions represented.）}

\begin{center}
\begin{tabular}{cccc}
\textbf{1.}\;\carrollSmall{1}{}{0}{}{}{}{}{} & \hspace{8mm} & \textbf{2.}\;\carrollSmall{}{}{1}{}{}{}{}{} \\[8mm]
\textbf{3.}\;\carrollSmall{}{}{}{0}{}{}{}{} & \hspace{8mm} & \textbf{4.}\;\carrollSmall{}{1}{}{}{}{}{}{} \\[8mm]
\textbf{5.}\;\carrollSmall{}{1}{}{}{}{}{}{} & \hspace{8mm} & \textbf{6.}\;\carrollSmall{}{}{0}{}{}{}{}{} \\[8mm]
\textbf{7.}\;\carrollSmall{}{}{}{1}{}{}{}{} & \hspace{8mm} & \textbf{8.}\;\carrollSmall{}{}{0}{1}{}{}{}{} \\[8mm]
\textbf{9.}\;\carrollSmall{}{}{}{}{}{}{}{1} & \hspace{8mm} & \textbf{10.}\;\carrollSmall{}{}{0}{0}{}{}{}{} \\[8mm]
\textbf{11.}\;\carrollSmall{1}{}{1}{}{}{}{}{} & \hspace{8mm} & \textbf{12.}\;\carrollSmall{1}{0}{}{1}{}{}{}{}
\end{tabular}
\end{center}

\begin{itemize}[label={}, leftmargin=0pt, itemsep=4mm]
\item \textbf{13.} どの $x'$ も $y$ ではない。すなわち \carrollSmall{}{}{0}{}{}{}{}{}
\item \textbf{14.} すべての $y'$ は $x'$ である。すなわち \carrollSmall{}{0}{}{1}{}{}{}{}
\item \textbf{15.} いくつかの $y'$ が存在する。すなわち \carrollSmall{}{}{}{}{}{}{}{1}
\item \textbf{16.} すべての $y$ は $x$ であり、かつすべての $x$ は $y$ である。すなわち \carrollSmall{1}{0}{0}{}{}{}{}{}
\item \textbf{17.} $x'$ は1つも存在しない。すなわち \carrollSmall{}{}{0}{0}{}{}{}{}
\item \textbf{18.} すべての $x$ は $y'$ である。すなわち \carrollSmall{0}{1}{}{}{}{}{}{}
\item \textbf{19.} どの $x$ も $y$ ではない。すなわち \carrollSmall{0}{}{}{}{}{}{}{}
\item \textbf{20.} いくつかの $x'$ は $y$ であり、かついくつかは $y'$ である。すなわち \carrollSmall{}{}{1}{1}{}{}{}{}
\item \textbf{21.} $y$ は1つも存在せず、かついくつかの $x$ が存在する。すなわち \carrollSmall{0}{1}{0}{}{}{}{}{}
\item \textbf{22.} すべての $x'$ は $y$ であり、かつすべての $y'$ は $x$ である。すなわち \carrollSmall{}{1}{1}{0}{}{}{}{}
\item \textbf{23.} {\small（原著表記 17.）} いくつかの $x$ は $y$ であり、かついくつかの $x'$ は $y'$ である。すなわち \carrollSmall{1}{}{}{1}{}{}{}{}
\end{itemize}

\section{小ダイアグラム：記号の解釈の解答（Smaller Diagram. Symbols interpreted.）}

\begin{enumerate}[label=\textbf{\arabic*.}]
\item いくつかの $y$ は非-$x$ である（または、いくつかの非-$x$ は $y$ である）。
\item どの非-$x$ も非-$y$ ではない（または、どの非-$y$ も非-$x$ ではない）。
\item どの非-$y$ も $x$ ではない。
\item 非-$x$ は1つも存在しない。すなわち、どの事物も非-$x$ ではない。
\item $y$ は1つも存在しない。すなわち、二階建ての家は1軒もない。
\item いくつかの $x'$ が存在する。すなわち、いくつかの家はレンガ造りではない。
\item どの $x$ も $y'$ ではない（または、どの $y'$ も $x$ ではない）。すなわち、レンガ造りの家で二階建て以外のものは1軒もない（または、二階建てでない家でレンガ造りのものは1軒もない）。
\item すべての $x'$ は $y'$ である。すなわち、レンガ造りでないすべての家は、二階建てではない。
\item いくつかの $x$ は $y$ であり、かついくつかは $y'$ である。すなわち、いくつかの太った少年は活発であり、かついくつかは活発ではない。
\item すべての $y'$ は $x'$ である。すなわち、すべての怠惰な（活発でない）少年は痩せている。
\item すべての $x$ は $y'$ であり、かつすべての $y'$ は $x$ である。すなわち、すべての太った少年は怠惰であり、かつすべての怠惰な少年は太っている。
\item すべての $y$ は $x$ であり、かつすべての $x'$ は $y'$ である。すなわち、すべての活発な少年は太っており、かつすべての痩せた少年は怠惰である。
\item $x$ は1匹も存在せず、かつ $y'$ も1匹も存在しない。すなわち、緑の目をした猫は1匹もおらず、気立ての悪い猫も1匹もいない。
\item いくつかの $x$ は $y'$ であり、かついくつかの $x'$ は $y$ である（または、いくつかの $y$ は $x'$ であり、かついくつかの $y'$ は $x$ である）。すなわち、いくつかの緑の目をした猫は気立てが悪く、かつ緑の目をしていないいくつかの猫は気立てがよい（または、いくつかの気立てのよい猫は緑の目をしておらず、かついくつかの気立ての悪い猫は緑の目をしている）。
\item いくつかの $x$ は $y$ であり、かつどの $x'$ も $y'$ ではない（または、いくつかの $y$ は $x$ であり、かつどの $y'$ も $x'$ ではない）。すなわち、いくつかの緑の目をした猫は気立てがよく、かつ緑の目をしていないどの猫も気立てが悪くない（または、いくつかの気立てのよい猫は緑の目をしており、かつ気立ての悪いどの猫も緑の目をしていないことはない）。
\item すべての $x$ は $y'$ であり、かつすべての $x'$ は $y$ である（または、すべての $y$ は $x'$ であり、かつすべての $y'$ は $x$ である）。すなわち、すべての緑の目をした猫は気立てが悪く、かつ緑の目をしていないすべての猫は気立てがよい（または、すべての気立てのよい猫は緑ではない目をしており、かつすべての気立ての悪い猫は緑の目をしている）。
\end{enumerate}

\section{大ダイアグラム：命題の表現の解答（Larger Diagram. Propositions represented.）}

\begin{center}
\begin{tabular}{cccc}
\textbf{1.}\;\carrollLarge{}{}{0}{0}{}{}{}{}{} & \hspace{8mm} & \textbf{2.}\;\carrollLarge{}{}{}{}{}{}{}{}{\fW} \\[10mm]
\textbf{3.}\;\carrollLarge{}{}{0}{0}{}{}{}{}{\fS} & \hspace{8mm} & \textbf{4.}\;\carrollLarge{}{0}{}{}{}{}{}{0}{} \\[10mm]
\textbf{5.}\;\carrollLarge{0}{}{0}{0}{1}{}{0}{}{} & \hspace{8mm} & \textbf{6.}\;\carrollLarge{}{}{0}{1}{0}{}{}{}{} \\[10mm]
\textbf{7.}\;\carrollLarge{}{}{0}{0}{0}{1}{}{}{} & \hspace{8mm} & \textbf{8.}\;\carrollLarge{}{0}{}{}{0}{0}{}{0}{}
\end{tabular}
\end{center}

\begin{itemize}[label={}, leftmargin=0pt, itemsep=5mm]
\item \textbf{9.} どの $x$ も $m$ ではない。すなわち \carrollLarge{}{}{0}{0}{}{}{}{}{}
\item \textbf{10.} いくつかの $m'$ は $y$ である。すなわち \carrollLarge{}{}{}{}{}{}{}{}{\fW}
\item \textbf{11.} すべての $y'$ は $m'$ である。すなわち \carrollLarge{}{}{}{0}{}{0}{}{}{\fE}
\item \textbf{12.} すべての $m$ は $x'$ である。すなわち \carrollLarge{}{}{0}{0}{}{}{}{}{\fS}
\item \textbf{13.} どの $x$ も $m$ ではない；すべての $y$ は $m$ である。すなわち \carrollLarge{0}{}{0}{0}{1}{}{0}{}{}
\item \textbf{14.} すべての $m'$ は $y$ である；どの $x$ も $m'$ ではない。すなわち \carrollLarge{0}{0}{}{}{}{}{1}{0}{}
\item \textbf{15.} すべての $x$ は $m$ である；どの $m$ も $y'$ ではない。すなわち \carrollLarge{0}{0}{1}{0}{}{0}{}{}{}
\item \textbf{16.} すべての $m'$ は $y'$ である；どの $x$ も $m'$ ではない。すなわち \carrollLarge{0}{0}{}{}{}{}{0}{1}{}
\item \textbf{17.} すべての $x$ は $m$ である；すべての $m$ は $y$ である。すなわち \carrollLarge{0}{0}{1}{0}{}{0}{}{}{} \quad {\small ［第2節 問7の注記参照］}
\item \textbf{18.} どの $x'$ も $m$ ではない；どの $m'$ も $y$ ではない。すなわち \carrollLarge{0}{}{}{}{0}{0}{0}{}{}
\item \textbf{19.} すべての $m$ は $x$ である；すべての $m$ は $y$ である。すなわち \carrollLarge{}{}{1}{0}{0}{0}{}{}{}
\item \textbf{20.} 「人（persons）」を対象領域（宇宙）にとるのがよいであろう。「私自身（myself）」を「中名辞」に選ぶこともでき、その場合の前提は次の形をとる：
\begin{quote}
私は、彼に子猫を連れてくるよう使いに出した人である；\\
私は、彼が間違えてやかんを持ってきた相手の人である。
\end{quote}
あるいは「彼（he）」を「中名辞」に選ぶこともでき、その場合の前提は次の形をとる：
\begin{quote}
彼は、私が子猫を連れてくるよう使いに出した人である；\\
彼は、間違えて私にやかんを持ってきた人である。
\end{quote}
この逸話の面白さは明らかに（私に何が起きたかではなく）\textbf{彼の}間抜けさにかかっているから、後者の形をとるのが最善であろう。そこで、$m=$「彼」；$x=$「私が子猫を連れてくるよう使いに出した人」；$y=$「間違えて私にやかんを持ってきた人」とおこう。

ゆえに、「すべての $m$ は $x$ である；すべての $m$ は $y$ である」となり、求めるダイアグラムは次のようになる：
\begin{center}
\carrollLarge{}{}{1}{0}{0}{0}{}{}{}
\end{center}
\end{itemize}

\section{両方のダイアグラムを用いる問題の解答（Both Diagrams employed.）}

\begin{itemize}[label={}, leftmargin=0pt, itemsep=4mm]
\item \textbf{1.}\;\carrollSmall{0}{}{1}{}{}{}{}{}\quad すなわち、すべての $y$ は $x'$ である。
\item \textbf{2.}\;\carrollSmall{}{1}{}{}{}{}{}{}\quad すなわち、いくつかの $x$ は $y'$ である（または、いくつかの $y'$ は $x$ である）。
\item \textbf{3.}\;\carrollSmall{}{}{1}{}{}{}{}{}\quad すなわち、いくつかの $y$ は $x'$ である（または、いくつかの $x'$ は $y$ である）。
\item \textbf{4.}\;\carrollSmall{}{}{}{0}{}{}{}{}\quad すなわち、どの $x'$ も $y'$ ではない（または、どの $y'$ も $x'$ ではない）。
\item \textbf{5.}\;\carrollSmall{0}{}{1}{}{}{}{}{}\quad すなわち、すべての $y$ は $x'$ である。すなわち、すべての黒いウサギは若い。
\item \textbf{6.}\;\carrollSmall{}{}{1}{}{}{}{}{}\quad すなわち、いくつかの $y$ は $x'$ である。すなわち、いくつかの黒いウサギは若い。
\item \textbf{7.}\;\carrollSmall{1}{0}{}{}{}{}{}{}\quad すなわち、すべての $x$ は $y$ である。すなわち、すべてのよく肥えた鳥は幸福である。
\item \textbf{8.}\;\carrollSmall{}{}{}{1}{}{}{}{}\quad すなわち、いくつかの $x'$ は $y'$ である。すなわち、よく肥えていないいくつかの鳥は不幸である（または、いくつかの不幸な鳥はよく肥えていない）。
\item \textbf{9.}\;\carrollSmall{1}{0}{}{}{}{}{}{}\quad すなわち、すべての $x$ は $y$ である。すなわち、ジョンは歯痛を患っている。
\item \textbf{10.}\;\carrollSmall{}{}{0}{}{}{}{}{}\quad すなわち、どの $x'$ も $y$ ではない。すなわち、ジョン以外の誰も歯痛を患っていない。
\item \textbf{11.}\;\carrollSmall{1}{}{}{}{}{}{}{}\quad すなわち、いくつかの $x$ は $y$ である。すなわち、散歩に出かけたある人は気分が良くなっている。
\item \textbf{12.}\;\carrollSmall{1}{}{}{}{}{}{}{}\quad すなわち、いくつかの $x$ は $y$ である。すなわち、私が子猫を連れてくるよう使いに出したある人が、間違えて私にやかんを持ってきた。
\end{itemize}

\vspace{4mm}
\begin{tcolorbox}[colback=white, colframe=boxframe!60, breakable, title={\textbf{問13〜32：大・小両ダイアグラムによる三段論法の完全導出}}]

\noindent\textbf{13.}\quad \carrollLarge{}{0}{0}{0}{}{}{}{0}{\fW} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{0}{}{}{}{}{}{}
\begin{quote}
「本（books）」を対象領域とし、$m=$「刺激的な（exciting）」、$x=$「熱のある患者に向く」、$y=$「人を眠くさせる」とする。\\
$\left.\begin{array}{l}\text{どの } m \text{ も } x \text{ ではない；}\\\text{すべての } m' \text{ は } y \text{ である。}\end{array}\right\} \;\therefore\;\text{どの } y' \text{ も } x \text{ ではない。}$\\
すなわち、\textbf{人を眠くさせるような本を除けば、熱のある患者に向く本は1冊もない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{14.}\quad \carrollLarge{}{}{1}{0}{}{0}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{1}{}{}{}{}{}{}{}
\begin{quote}
「人（persons）」を対象領域とし、$m=$「美人を得るに値する」、$x=$「相応の報いを得る」、$y=$「勇敢な」とする。\\
$\left.\begin{array}{l}\text{いくつかの } m \text{ は } x \text{ である；}\\\text{どの } y' \text{ も } m \text{ ではない。}\end{array}\right\} \;\therefore\;\text{いくつかの } y \text{ は } x \text{ である。}$\\
すなわち、\textbf{いくつかの勇敢な人は相応の報いを得る。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{15.}\quad \carrollLarge{0}{}{0}{0}{}{}{0}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{0}{}{}{}{}{}{}{}
\begin{quote}
「人（persons）」を対象領域とし、$m=$「忍耐強い」、$x=$「子供」、$y=$「じっと座っていられる」とする。\\
$\left.\begin{array}{l}\text{どの } x \text{ も } m \text{ ではない；}\\\text{どの } m' \text{ も } y \text{ ではない。}\end{array}\right\} \;\therefore\;\text{どの } x \text{ も } y \text{ ではない。}$\\
すなわち、\textbf{どの子供もじっと座っていられない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{16.}\quad \carrollLarge{0}{0}{0}{1}{0}{}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{0}{1}{}{}{}{}{}{}
\begin{quote}
「事物（things）」を対象領域とし、$m=$「太った」、$x=$「豚」、$y=$「骸骨」とする。\\
$\left.\begin{array}{l}\text{すべての } x \text{ は } m \text{ である；}\\\text{どの } y \text{ も } m \text{ ではない。}\end{array}\right\} \;\therefore\;\text{すべての } x \text{ は } y' \text{ である。}$\\
すなわち、\textbf{すべての豚は骸骨ではない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{17.}\quad \carrollLarge{}{}{0}{0}{1}{0}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{}{1}{}{}{}{}{}
\begin{quote}
「生き物（creatures）」を対象領域とし、$m=$「猿」、$x=$「兵士」、$y=$「いたずら好きな」とする。\\
$\left.\begin{array}{l}\text{どの } m \text{ も } x \text{ ではない；}\\\text{すべての } m \text{ は } y \text{ である。}\end{array}\right\} \;\therefore\;\text{いくつかの } y \text{ は } x' \text{ である。}$\\
すなわち、\textbf{いくつかのいたずら好きな生き物は兵士ではない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{18.}\quad \carrollLarge{0}{}{0}{0}{}{}{0}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{0}{}{}{}{}{}{}{}
\begin{quote}
「人（persons）」を対象領域とし、$m=$「公正な」、$x=$「私の従兄弟」、$y=$「裁判官」とする。\\
$\left.\begin{array}{l}\text{どの } x \text{ も } m \text{ ではない；}\\\text{どの } y \text{ も } m' \text{ ではない。}\end{array}\right\} \;\therefore\;\text{どの } x \text{ も } y \text{ ではない。}$\\
すなわち、\textbf{私の従兄弟は誰ひとり裁判官ではない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{19.}\quad \carrollLarge{}{}{1}{0}{}{}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{1}{}{}{}{}{}{}{}
\begin{quote}
「期間（periods）」を対象領域とし、$m=$「日（days）」、$x=$「雨降りの」、$y=$「うんざりする」とする。\\
$\left.\begin{array}{l}\text{いくつかの } m \text{ は } x \text{ である；}\\\text{すべての } xm \text{ は } y \text{ である。}\end{array}\right\} \;\therefore\;\text{いくつかの } x \text{ は } y \text{ である。}$\\
すなわち、\textbf{いくつかの雨降りの期間はうんざりする。}\\[2mm]
{\small \textbf{注意（N.B.）：} これらは正当な（まっとうな）前提ではない。なぜなら、結論が実際には第2前提の一部になっており、したがって第1前提が余分（冗長）だからである。このことは文字で次のように示される：「すべての $xm$ は $y$ である」は「いくつかの $xm$ は $y$ である」を含んでおり、それはさらに「いくつかの $x$ は $y$ である」を含んでいる。言葉で言えば、「すべての雨降りの日はうんざりする」は「いくつかの雨降りの日はうんざりする」を含んでおり、それは「いくつかの雨降りの期間はうんざりする」を含んでいる。さらに第1前提は、余分であるばかりでなく、実際には第2前提の中に含まれている（「いくつかの雨降りの日が存在する」と等価であり、それは「すべての雨降りの日はうんざりする」に含意されているからである）。総じて、実に不満足きわまりない一対の前提である！}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{20.}\quad \carrollLarge{0}{}{1}{}{0}{0}{0}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{1}{}{0}{}{}{}{}{}
\begin{quote}
「事物（things）」を対象領域とし、$m=$「薬」、$x=$「嫌な味がする（まずい）」、$y=$「センナ」とする。\\
$\left.\begin{array}{l}\text{すべての } m \text{ は } x \text{ である；}\\\text{すべての } y \text{ は } m \text{ である。}\end{array}\right\} \;\therefore\;\text{すべての } y \text{ は } x \text{ である。}$\\
すなわち、\textbf{センナは嫌な味がする。} {\small ［第2節 問7の注記参照］}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{21.}\quad \carrollLarge{}{}{0}{1}{0}{}{}{}{\fW} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{1}{}{}{}{}{}{}
\begin{quote}
「人（persons）」を対象領域とし、$m=$「ユダヤ人」、$x=$「裕福な」、$y=$「パタゴニア人」とする。\\
$\left.\begin{array}{l}\text{いくつかの } m \text{ は } x \text{ である；}\\\text{すべての } y \text{ は } m' \text{ である。}\end{array}\right\} \;\therefore\;\text{いくつかの } x \text{ は } y' \text{ である。}$\\
すなわち、\textbf{いくつかの裕福な人はパタゴニア人ではない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{22.}\quad \carrollLarge{0}{}{}{}{0}{0}{0}{}{\fN} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{}{0}{}{}{}{}{}
\begin{quote}
「生き物（creatures）」を対象領域とし、$m=$「絶対禁酒主義者」、$x=$「砂糖を好む」、$y=$「ナイチンゲール」とする。\\
$\left.\begin{array}{l}\text{すべての } m \text{ は } x \text{ である；}\\\text{どの } y \text{ も } m' \text{ ではない。}\end{array}\right\} \;\therefore\;\text{どの } y \text{ も } x' \text{ ではない。}$\\
すなわち、\textbf{どのナイチンゲールも砂糖を嫌わない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{23.}\quad \carrollLarge{}{}{0}{0}{0}{}{}{}{\fW} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{}{}{}{}{}{}{}
\begin{quote}
「食物（food）」を対象領域とし、$m=$「体に良い」、$x=$「マフィン」、$y=$「菓子パン（buns）」とする。\\
$\begin{array}{l}\text{どの } x \text{ も } m \text{ ではない；}\\\text{すべての } y \text{ は } m' \text{ である。}\end{array}$\\
小ダイアグラムに対する\textbf{「情報がない（no information）」}ため、\textbf{いかなる結論も導き出すことができない（誤謬的な前提）。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{24.}\quad \carrollLarge{}{}{0}{0}{1}{}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{}{1}{}{}{}{}{}
\begin{quote}
「生き物（creatures）」を対象領域とし、$m=$「うまく走る」、$x=$「太った」、$y=$「グレイハウンド」とする。\\
$\left.\begin{array}{l}\text{どの } x \text{ も } m \text{ ではない；}\\\text{いくつかの } y \text{ は } m \text{ である。}\end{array}\right\} \;\therefore\;\text{いくつかの } y \text{ は } x' \text{ である。}$\\
すなわち、\textbf{いくつかのグレイハウンドは太っていない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{25.}\quad \carrollLarge{}{}{}{}{0}{0}{}{}{\fN\fW} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{}{}{}{}{}{}{}
\begin{quote}
「人（persons）」を対象領域とし、$m=$「兵士」、$x=$「行進する」、$y=$「若者」とする。\\
$\begin{array}{l}\text{すべての } m \text{ は } x \text{ である；}\\\text{いくつかの } y \text{ は } m' \text{ である。}\end{array}$\\
小ダイアグラムに対する\textbf{「情報がない」}ため、\textbf{いかなる結論も導き出すことができない（誤謬的な前提）。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{26.}\quad \carrollLarge{0}{0}{0}{1}{0}{}{1}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{0}{1}{1}{}{}{}{}{}
\begin{quote}
「食物（food）」を対象領域とし、$m=$「甘い」、$x=$「砂糖」、$y=$「塩」とする。\\
$\left.\begin{array}{l}\text{すべての } x \text{ は } m \text{ である；}\\\text{すべての } y \text{ は } m' \text{ である。}\end{array}\right\} \;\therefore\;\left\{\begin{array}{l}\text{すべての } x \text{ は } y' \text{ である。}\\\text{すべての } y \text{ は } x' \text{ である。}\end{array}\right.$\\
すなわち、\textbf{砂糖は塩ではない。塩は砂糖ではない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{27.}\quad \carrollLarge{}{}{1}{0}{}{0}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{1}{}{}{}{}{}{}{}
\begin{quote}
「事物（Things）」を対象領域とし、$m=$「卵」、$x=$「固ゆでの」、$y=$「割れる」とする。\\
$\left.\begin{array}{l}\text{いくつかの } m \text{ は } x \text{ である；}\\\text{どの } m \text{ も } y' \text{ ではない。}\end{array}\right\} \;\therefore\;\text{いくつかの } x \text{ は } y \text{ である。}$\\
すなわち、\textbf{いくつかの固ゆでのものは割ることができる。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{28.}\quad \carrollLarge{0}{}{0}{0}{}{}{0}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{0}{}{}{}{}{}{}{}
\begin{quote}
「人（persons）」を対象領域とし、$m=$「ユダヤ人」、$x=$「家の中にいる」、$y=$「庭にいる」とする。\\
$\left.\begin{array}{l}\text{どの } m \text{ も } x \text{ ではない；}\\\text{どの } m' \text{ も } y \text{ ではない。}\end{array}\right\} \;\therefore\;\text{どの } x \text{ も } y \text{ ではない。}$\\
すなわち、\textbf{家の中にいる人で、同時に庭にもいる人は誰ひとりいない。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{29.}\quad \carrollLarge{0}{0}{}{}{}{}{1}{0}{\fN} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{}{1}{}{}{}{}{}
\begin{quote}
「事物（Things）」を対象領域とし、$m=$「騒々しい」、$x=$「戦闘」、$y=$「見過ごされうる」とする。\\
$\left.\begin{array}{l}\text{すべての } x \text{ は } m \text{ である；}\\\text{すべての } m' \text{ は } y \text{ である。}\end{array}\right\} \;\therefore\;\text{いくつかの } x' \text{ は } y \text{ である。}$\\
すなわち、\textbf{戦闘でないいくつかの事物は、見過ごされる（気づかれずに済む）ことがある。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{30.}\quad \carrollLarge{0}{}{0}{0}{1}{}{0}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{0}{}{1}{}{}{}{}{}
\begin{quote}
「人（persons）」を対象領域とし、$m=$「ユダヤ人」、$x=$「狂っている（mad）」、$y=$「ラビ」とする。\\
$\left.\begin{array}{l}\text{どの } m \text{ も } x \text{ ではない；}\\\text{すべての } y \text{ は } m \text{ である。}\end{array}\right\} \;\therefore\;\text{すべての } y \text{ は } x' \text{ である。}$\\
すなわち、\textbf{すべてのラビは正気（sane）である。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{31.}\quad \carrollLarge{}{}{1}{}{0}{0}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{1}{}{}{}{}{}{}{}
\begin{quote}
「事物（Things）」を対象領域とし、$m=$「魚」、$x=$「泳げる」、$y=$「ガンギエイ（skates）」とする。\\
$\left.\begin{array}{l}\text{どの } m \text{ も } x' \text{ ではない；}\\\text{いくつかの } y \text{ は } m \text{ である。}\end{array}\right\} \;\therefore\;\text{いくつかの } y \text{ は } x \text{ である。}$\\
すなわち、\textbf{いくつかのガンギエイは泳ぐことができる。}
\end{quote}
\hrule\vspace{4mm}

\noindent\textbf{32.}\quad \carrollLarge{}{}{0}{0}{1}{}{}{}{} \hspace{6mm} $\Longrightarrow$ \hspace{6mm} \carrollSmall{}{}{1}{}{}{}{}{}
\begin{quote}
「人々（people）」を対象領域とし、$m=$「激情的な」、$x=$「合理的な」、$y=$「雄弁家（演説家）」とする。\\
$\left.\begin{array}{l}\text{すべての } m \text{ は } x' \text{ である；}\\\text{いくつかの } y \text{ は } m \text{ である。}\end{array}\right\} \;\therefore\;\text{いくつかの } y \text{ は } x' \text{ である。}$\\
すなわち、\textbf{いくつかの雄弁家は非合理的である。} {\small ［第2節 問7の注記参照］}
\end{quote}

\end{tcolorbox}
"""

CHAPTER_IV_JA = r"""
\begin{center}
\textit{「汝には当てられまい、当てられまい、当てられまい、\\
汝には到底当てられまい、わが良き人よ。」}\\
\small（``Thou canst not hit it, hit it, hit it, / Thou canst not hit it, my good man.'' —— シェイクスピア『恋の骨折り損』第4幕第1場）
\end{center}

\section*{総合演習：前提ペアからの推論と誤謬判定（問1〜91）}

\begin{enumerate}[label=\textbf{\arabic*.}]
\item 苦痛は人を疲れさせる；いかなる苦痛も熱烈に望まれることはない。（Pain is wearisome; No pain is eagerly wished for.）
\item 禿頭（はげ）の人は誰ひとりヘアブラシを必要としない；どのトカゲにも毛髪はない。（No bald person needs a hair-brush; No lizards have hair.）
\item すべての思慮のない人々は害悪をなす；思慮深い人は誰ひとり約束を忘れない。（All thoughtless people do mischief; No thoughtful person forgets a promise.）
\item 私はジョンが好きではない；私の友人の何人かはジョンが好きである。（I do not like John; Some of my friends like John.）
\item どのジャガイモもパイナップルではない；すべてのパイナップルは美味しい。（No potatoes are pine-apples; All pine-apples are nice.）
\item どのピン（留め針）も野心的ではない；どの縫い針もピンではない。（No pins are ambitious; No needles are pins.）
\item 私の友人は皆風邪をひいている；風邪をひいている人は誰も歌えない。（All my friends have colds; No one can sing who has a cold.）
\item これらすべての料理はよく調理されている；いくつかの料理は、よく調理されていなければ体に良くない。（All these dishes are well-cooked; Some dishes are unwholesome if not well-cooked.）
\item どの薬も美味しくない；センナは薬である。（No medicine is nice; Senna is a medicine.）
\item いくつかの牡蠣（カキ）は無口（静か）である；無口な生き物はどれも面白くない。（Some oysters are silent; No silent creatures are amusing.）
\item すべての賢明な人は足で歩く；すべての愚かな人は逆立ちして（手で）歩く。（All wise men walk on their feet; All unwise men walk on their hands.）
\item 「自分の仕事にだけ構いなさい；この喧嘩はあなたの関知すべき仕事ではない。」（"Mind your own business; This quarrel is no business of yours."）
\item どの橋も砂糖では作られていない；いくつかの橋は絵のように美しい。（No bridges are made of sugar; Some bridges are picturesque.）
\item 解けるようななぞなぞはどれも私の興味を引かない；これらすべてのなぞなぞは解くことができない。（No riddles interest me that can be solved; All these riddles are insoluble.）
\item ジョンは勤勉である；すべての勤勉な人々は幸福である。（John is industrious; All industrious people are happy.）
\item どのカエルも本を書かない；何人かの人々は本を書くのにインクを使う。（No frogs write books; Some people use ink in writing books.）
\item どの火かき棒（pokers）も柔らかくない；すべての枕は柔らかい。（No pokers are soft; All pillows are soft.）
\item どのレイヨウ（アンテロープ）も不格好ではない；優美な動物は目を楽しませる。（No antelope is ungraceful; Graceful animals delight the eye.）
\item いくつかの叔父は気前がよくない；すべての商人は気前がよい。（Some uncles are ungenerous; All merchants are generous.）
\item 不幸な人は誰ひとりほくそ笑まない；幸福な人は誰ひとりうめき声を上げない。（No unhappy people chuckle; No happy people groan.）
\item 耳に聞こえる音楽は空気中に振動を引き起こす；耳に聞こえない音楽はお金を払う価値がない。（Audible music causes vibration in the air; Inaudible music is not worth paying for.）
\item 彼は私に5ポンドくれた；私は大喜びした。（He gave me five pounds; I was delighted.）
\item どの年老いたユダヤ人も太った粉屋ではない；私の友人は皆、年老いた粉屋である。（No old Jews are fat millers; All my friends are old millers.）
\item 小麦粉（穀粉）は食用に適している；オートミールは穀粉の一種である。（Flour is good for food; Oatmeal is a kind of flour.）
\item いくつかの夢は恐ろしい；どの子羊も恐ろしくない。（Some dreams are terrible; No lambs are terrible.）
\item 裕福な人は誰ひとり街頭で物乞いをしない；裕福でない人は皆、家計簿をつけるべきである。（No rich man begs in the street; All who are not rich should keep accounts.）
\item どの泥棒も正直ではない；いくつかの不正直な人々は悪事が露見する。（No thieves are honest; Some dishonest people are found out.）
\item すべてのスズメバチ（wasps）は不愛想（敵対的）である；すべての子犬は愛想がよい（友好的である）。（All wasps are unfriendly; All puppies are friendly.）
\item すべてのありそうもない話は疑われる；これらの話のどれひとつとしてありそうなものはない。（All improbable stories are doubted; None of these stories are probable.）
\item 「彼は私に、あなたが立ち去ってしまったと言った。」「彼は真実の言葉をひとことも言わない。」（"He told me you had gone away." "He never says one word of truth."）
\item 彼の歌は決して1時間も続かない；1時間続く歌は退屈である。（His songs never last an hour; A song, that lasts an hour, is tedious.）
\item どのウェディングケーキ（bride-cakes）も体に良くない；体に良くない食物は避けるべきである。（No bride-cakes are wholesome; Unwholesome food should be avoided.）
\item どの年老いた守銭奴も快活ではない；いくつかの年老いた守銭奴は痩せている。（No old misers are cheerful; Some old misers are thin.）
\item すべてのアヒルはよちよち歩く；よちよち歩くものは何ひとつ優美ではない。（All ducks waddle; Nothing that waddles is graceful.）
\item どの教授も無知ではない；いくつかの無知な人々はうぬぼれ屋である。（No Professors are ignorant; Some ignorant people are conceited.）
\item 歯痛は決して心地よいものではない；暖かさは決して不快なものではない。（Toothache is never pleasant; Warmth is never unpleasant.）
\item 退屈な人間（うんざりさせるおしゃべり, Bores）は恐ろしい；あなたは退屈な人間である。（Bores are terrible; You are a bore.）
\item いくつかの山は登頂不可能である；すべての牧場の柵越え段（stiles）は乗り越えることができる。（Some mountains are insurmountable; All stiles can be surmounted.）
\item どのフランス人もプラムプディングを好まない；すべてのイギリス人はプラムプディングを好む。（No Frenchmen like plumpudding; All Englishmen like plumpudding.）
\item どの怠け者も名声を勝ち取らない；いくつかの画家は怠け者ではない。（No idlers win fame; Some painters are not idle.）
\item どのロブスターも非合理的ではない；合理的な生き物はどれも不可能なことを期待しない。（No lobsters are unreasonable; No reasonable creatures expect impossibilities.）
\item いかなる善行も違法ではない；合法的なことは恐れることなく行ってよい。（No kind deed is unlawful; What is lawful may be done without fear.）
\item どの化石も失恋する（恋に破れる）ことはない；いかなる牡蠣も失恋することがありうる。（No fossils can be crossed in love; Any oyster may be crossed in love.）
\item 「これは我慢の限界を超えている！」「ふむ、私の身には我慢の限界を超えることなど一度も起きたためしがないよ。」（"This is beyond endurance!" "Well, nothing beyond endurance has ever happened to me."）
\item すべての教育を受けていない人間は浅薄である；これらすべての学生は教育を受けている。（All uneducated men are shallow; All these students are educated.）
\item 私の従兄弟は皆、不公正である；どの裁判官も不公正ではない。（All my cousins are unjust; No judges are unjust.）
\item 探検されたいかなる国にもドラゴンははびこっていない；未探検の国々は魅力的である。（No country, that has been explored, is infested by dragons; Unexplored countries are fascinating.）
\item どの守銭奴も気前がよくない；いくつかの老人は気前がよくない。（No misers are generous; Some old men are not generous.）
\item 思慮分別のある人間はハイエナを避ける；どの銀行家も無分別ではない。（A prudent man shuns hyaenas; No banker is imprudent.）
\item いくつかの詩は独創的である；いかなる独創的な作品も意のままに量産することはできない。（Some poetry is original; No original work is producible at will.）
\item どの守銭奴も無欲ではない；守銭奴以外に卵の殻をため込む者はいない。（No misers are unselfish; None but misers save egg-shells.）
\item すべての顔色の青白い人々は粘液質（冷静沈着）である；顔色が青白くない人は誰も詩人には見えない。（All pale people are phlegmatic; No one, who is not pale, looks poetical.）
\item すべてのクモは巣を張る；巣を張らないいくつかの生き物は獰猛である。（All spiders spin webs; Some creatures, that do not spin webs, are savage.）
\item 私の従兄弟は誰ひとり公正ではない；すべての裁判官は公正である。（None of my cousins are just; All judges are just.）
\item ジョンは勤勉である；どの勤勉な人々も不幸ではない。（John is industrious; No industrious people are unhappy.）
\item 傘は旅行において役に立つ；旅行において役に立たないものは置いていくべきである。（Umbrellas are useful on a journey; What is useless on a journey should be left behind.）
\item いくつかの枕は柔らかい；どの火かき棒も柔らかくない。（Some pillows are soft; No pokers are soft.）
\item 私は年老いており、かつ足が不自由である；どの年老いた商人も足の不自由な賭博師ではない。（I am old and lame; No old merchant is a lame gambler.）
\item 波乱万丈な旅は決して忘れられない；波乱のない平凡な旅は本に書く価値がない。（No eventful journey is ever forgotten; Uneventful journeys are not worth writing a book about.）
\item 砂糖は甘い；いくつかの甘いものは子供たちに好かれる。（Sugar is sweet; Some sweet things are liked by children.）
\item リチャードは機嫌を損ねている；リチャード以外の誰もあの馬には乗れない。（Richard is out of temper; No one but Richard can ride that horse.）
\item すべての冗談は楽しませることを意図している；いかなる議会制定法（Act of Parliament）も冗談ではない。（All jokes are meant to amuse; No Act of Parliament is a joke.）
\item 「私はそれを新聞で見たのだ。」「すべての新聞は嘘をつく。」（"I saw it in a newspaper." "All newspapers tell lies."）
\item いかなる悪夢も心地よくない；不快な経験は切望されない。（No nightmare is pleasant; Unpleasant experiences are not anxiously desired.）
\item 用心深い旅行者はたくさんの小銭を持ち歩く；不用心な旅行者は荷物を紛失する。（Prudent travellers carry plenty of small change; Imprudent travellers lose their luggage.）
\item すべてのスズメバチは不愛想である；どの子犬も不愛想ではない。（All wasps are unfriendly; No puppies are unfriendly.）
\item 彼は昨日ここを訪ねてきた；彼は私の友人ではない。（He called here yesterday; He is no friend of mine.）
\item どの四足動物も口笛を吹けない；いくつかの猫は四足動物である。（No quadrupeds can whistle; Some cats are quadrupeds.）
\item 調理された肉は肉屋では売られていない；調理されていない生の肉は夕食には出されない。（No cooked meat is sold by butchers; No uncooked meat is served at dinner.）
\item 金（ゴールド）は重い；金以外の何ものも彼を黙らせることはできない。（Gold is heavy; Nothing but gold will silence him.）
\item いくつかの豚は野生である；太っていない豚は1匹もいない。（Some pigs are wild; There are no pigs that are not fat.）
\item どの皇帝も歯科医ではない；すべての歯科医は子供たちに恐れられている。（No emperors are dentists; All dentists are dreaded by children.）
\item 年老いていない人は皆、散歩を好む；あなたも私も年老いていない。（All, who are not old, like walking; Neither you nor I are old.）
\item すべての刃（blades）は鋭い；いくつかの草は葉身（blades）である。（All blades are sharp; Some grasses are blades.）
\item 尊大な（独裁的な）人は誰ひとり人気がない；彼女は尊大である。（No dictatorial person is popular; She is dictatorial.）
\item いくつかの甘いものは体に良くない；どのマフィンも甘くない。（Some sweet things are unwholesome; No muffins are sweet.）
\item どの軍人も詩を書かない；どの将軍も民間人（文民）ではない。（No military men write poetry; No generals are civilians.）
\item 退屈な人間は恐れられる；退屈な人間が滞在を延ばすよう懇願されることは決してない。（Bores are dreaded; A bore is never begged to prolong his visit.）
\item すべてのフクロウは申し分ない；いくつかの言い訳は不十分（申し分なくない）である。（All owls are satisfactory; Some excuses are unsatisfactory.）
\item 私の従兄弟は皆、不公正である；すべての裁判官は公正である。（All my cousins are unjust; All judges are just.）
\item いくつかの菓子パンはこってりしている（rich）；すべての菓子パンは美味しい。（Some buns are rich; All buns are nice.）
\item どの薬も美味しくない；どの丸薬（ピル）も薬効がないことはない。（No medicine is nice; No pills are unmedicinal.）
\item いくつかの授業（日課）は難しい；難しいものには注意が必要である。（Some lessons are difficult; What is difficult needs attention.）
\item 予期せぬ喜びはどれも私を苛立たせない；あなたの訪問は予期せぬ喜びである。（No unexpected pleasure annoys me; Your visit is an unexpected pleasure.）
\item 毛虫（イモムシ）は雄弁ではない；ジョーンズは雄弁である。（Caterpillars are not eloquent; Jones is eloquent.）
\item いくつかの禿頭の人はかつらをかぶる；あなたの子供たちは皆、毛髪がある。（Some bald people wear wigs; All your children have hair.）
\item すべてのスズメバチは不愛想である；不愛想な生き物は常に歓迎されない。（All wasps are unfriendly; Unfriendly creatures are always unwelcome.）
\item どの破産者も裕福ではない；いくつかの商人は破産者ではない。（No bankrupts are rich; Some merchants are not bankrupts.）
\item イタチはときどき眠る；すべての動物はときどき眠る。（Weasels sometimes sleep; All animals sometimes sleep.）
\item 経営状態の悪い事業は利益を生まない；鉄道が経営不良になることは決してない。（Ill-managed concerns are unprofitable; Railways are never ill-managed.）
\item 誰もが豚を見たことがある；誰も豚に感嘆しない。（Everybody has seen a pig; Nobody admires a pig.）
\end{enumerate}

\vspace{4mm}
\section*{対話からの前提抽出と結論の導出（問92〜95）}
\noindent\textbf{以下のそれぞれの対話から一対の前提を抽出し、もし結論が存在するならばそれを演繹せよ：}

\begin{enumerate}[label=\textbf{\arabic*.}, start=92]
\item 「ライオンというやつは——私ほど何度も連中に追いかけられた経験のある者なら誰でも請け合うことだが——実に獰猛きわまりない動物なのだ。そして連中のなかには、一般的な法則として保証するつもりはないけれども、コーヒーを飲まない個体が確かにいくつか存在するのだよ。」
\item 「あんなものを勧めるなんて、君も実に馬鹿げたことをしたものだ！ 少しでも分別があれば、年老いた船乗りでオートミール粥（gruel）を好む者など1人もいないことくらい知っていそうなものなのに！」

「でも、あの方は君の叔父さんだと思ったものだから——」

「私の叔父だなんて、まさか！ くだらない（たわごとだ）！」

「たわごとと呼びたければ呼ぶがいいさ。ただ私が知っているのは、\textbf{私の}叔父たちは皆老人で、しかもどいつもこいつもオートミール粥に目がないということだけだよ！」

「ほう、それなら\textbf{君の}叔父たちは——」
\item 「さあ、ここから出よう！ これ以上こんな押し合いへし合いには我慢できないよ。混雑した店が快適でないことくらい、君だってよく知っているだろう。」

「おや、買い物に出て快適さを期待する人なんてどこにいるのかしら？」

「なんだと、もちろん私は期待するとも！ それに、通りのもう少し先へ行けば、混雑していない店がいくつかあるに違いない。だから——」
\item 「医者で形而上学的なオルガン奏者である者は1人もいないそうだよ。そしてそのことから、\textbf{あなた}に関するちょっとした事実が私には分かってしまうのさ。」

「おや、どうして\textbf{そんなこと}が分かるんだい？ 私がオルガンを弾くのを聞いたことなど一度もないだろうに。」

「ええ、先生、でもあなたがブラウニングの詩について語っておられるのを聞いたことがありますからね。それで少なくともあなたが\textbf{形而上学的}であることだけは分かりましたよ。ということは——」
\end{enumerate}

\vspace{4mm}
\section*{対話からの三段論法の抽出と妥当性検証（問96〜100）}
\noindent\textbf{以下のそれぞれの対話から三段論法を抽出し、その正しさを検証せよ：}

\begin{enumerate}[label=\textbf{\arabic*.}, start=96]
\item 「私に口答えしないでくれ！ 私は君よりずっと多くの裕福な商人を知っているがね、天地開闢このかた、彼らのなかに年老いた守銭奴だった者など\textbf{ただの1人も}いなかったと断言できるよ！」

「それで、それが年老いたブラウン氏と何の関係があるんです？」

「なんだと、彼は大層な金持ちじゃないか？」

「ええ、もちろん金持ちですよ。それがどうしました？」

「おいおい、彼を『守銭奴の商人』と呼ぶのが馬鹿げていることが分からないのかい？ 彼は商人ではないか、さもなければ守銭奴ではないかのどちらかだよ！」
\item 「お見舞いに来てくださるなんて、本当にご親切さまですこと！ おかげさまで今日は本当にずいぶん気分がよろしいのですよ。」

「それは重畳。ところで、この喜ばしい回復の手柄は、『自然』と『医術』のどちらに帰せられるべきなのでしょうか？」

「医術だと思いますわ。先生があの特製の特許薬を少し分けてくださったものですから。」

「ほう、それならあの医者をヤブ医者（山師）呼ばわりするのはもう二度とやめることにしよう。少なくともここに\textbf{誰か1人は}、彼の薬を飲んで気分が良くなった人がいるわけだからね！」
\item 「いやよ、私、あなたなんかちっとも好きじゃないわ。もう行って私のお人形と遊ぶことにするわ。\textbf{お人形}は決して不親切にしないもの。」

「へえ、じゃあ従兄弟よりもお人形のほうが好きだっていうのかい？ やれやれ、なんてお馬鹿なちびさんだ！」

「ええ、もちろんそうよ！ \textbf{従兄弟}なんてちっとも親切じゃないわ——少なくとも私がこれまで見たことのある従兄弟はみんなそうよ。」

「ふん、それでいったい\textbf{何が}証明できるっていうんだい！ もし従兄弟はお人形じゃないって言いたいのなら、いったい誰が従兄弟はお人形だなんて言ったよ？」
\item 「いったい何だってゼラニウムの話なんかしているんだい？ この距離じゃ、どの花か見分けなんかつけられるはずがないだろう！ もちろん、あそこにあるのが全部\textbf{赤い}花だということは認めるよ——\textbf{それ}を知るのに望遠鏡はいらないからね。」

「でも、いくつかのゼラニウムは赤いわよね、そうじゃなくて？」

「それは否定しないさ。だが、それがどうしたっていうんだ？ まさか君は、あの花のうちのいくつかがゼラニウムだなんて言うつもりじゃあるまいね！」

「もちろん、あなたに論理の筋道をたどるだけの分別がおありなら、そう教えてあげるところよ！ でも、\textbf{あなた}みたいな人に何かを証明してあげたところで、いったい何の役に立つのかしらね？」
\item 「諸君、あらゆる点を考慮すれば、今回の試験はまずまず立派な成績で合格したと言える。さて、私が去る前に一言助言を与えておこう。『本当に学びたいと切望している者は皆、\textbf{一生懸命に努力する（勉強する）}』ということを心に留めておきなさい。」

「生徒たちを代表いたしまして、厚く御礼申し上げます、先生！ そして、生徒たちのうち少なくとも\textbf{何人かは}、本当に学びたいと\textbf{切望して}いるのだと考えますと、私も鼻が高い思いでございます。」

「ほう、それは実に喜ばしいことだ。ところで、どうしてそうだとお分かりになるのですかな？」

「いやはや先生、彼らが——つまり彼らのうちの何人かが、どれほど一生懸命に努力しているかを私はよく知っておりますからね。私以上にそれをよく知る者がおりましょうか？」
\end{enumerate}

\vspace{4mm}
\section*{総合長文問題：溺愛する母親の演説（問101）}
\noindent\textbf{次の演説から、一連の三段論法（または三段論法の形式をとった議論）を抽出し、それらの正しさを検証せよ。}

\noindent{\small （これは、ある友人が「お子さんたちの教育（お稽古事や勉強）に関して、もしかすると\textbf{ほんの少しばかり}やり過ぎていらっしゃるのではないでしょうか」と控えめに忠告したのに対して、子供を溺愛する母親がまくし立てた言葉であると想定されている。）}

\begin{enumerate}[label=\textbf{\arabic*.}, start=101]
\item 「いいえね、あの子たちは将来、世の中に出て自分たちの力で生きていかなければならないのですよ。\textbf{私たち}には、あの子たち一人ひとりに財産を残してやることなどできませんからね。そしてご存じの通り、お金というものはそれ相応の対価（価値）なしには手に入らないものです——生きていきたいなら、あの子たちは\textbf{働か}なければなりません。でも、もし何も知らなかったら、いったいどうやって働けるというのです？ 私の言うことをお聞きなさい、\textbf{今の}ご時世には、無知な人間の居場所などどこにもありませんよ！ そして、ものを学ぶべき時期は若いうちだということでは、すべての専門家の意見が一致しています。年をとってからでは、取り立てて言うほどの記憶力など残っていませんからね。子供は1時間で、大人が5時間かけるよりも多くのことを学ぶものです。ですから、学ばなければならない者は、いやしくも学ぶつもりがあるなら、若いうちに学ばなければならないのです。もちろん、子供たちが\textbf{健康}でなければそんなことはできません——\textbf{それ}については私もまったく同感ですよ。ところで、お医者様がおっしゃるには、頬に血色のよい赤みがさしていないような子供は誰ひとり健康ではないそうです。さあ、うちの可愛い子たちをちょっと見てごらんなさいな！ まあ、あの子たちの頬ときたら、まるで芍薬（シャクヤク）の花のように見事に咲き誇っているじゃありませんか！ それからまた、世間で言われていますことには、子供たちの健康を保つためには、1日の勉強時間は合計で決して6時間を超えてはならず、週に少なくとも2回は半ドン（午後休み）を与えなければならないそうですね。そして\textbf{それ}こそ、まさに私たちが実行している計画そのものだと請け合いますよ！ 私たちは決して6時間を超えることはありませんし、毎週水曜日と土曜日にはいつも決まって、午後1時の昼食のあとには勉強など一文字たりともさせてはおりません！ ですから、うちの大切な宝物たちの教育において私が何か危険を冒しているなどと、いったい全体どうしてあなたが想像できるのか、私には到底理解できませんわ、ええ、本当に！」
\end{enumerate}

\begin{center}
\vspace{6mm}
\textbf{—— 大尾（THE END） ——}
\end{center}
"""
