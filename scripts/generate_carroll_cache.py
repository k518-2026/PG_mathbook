import os
import sys
import json
import time
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

CACHE_DIR = 'ollama_cache_carroll'
os.makedirs(CACHE_DIR, exist_ok=True)

OLLAMA_URL = "http://192.168.128.62:11434/api/chat"
MODEL_NAME = "gemma4:12b"

def query_ollama(prompt, system_prompt=None, retries=3):
    headers = {"Content-Type": "application/json"}
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 1500
        }
    }

    for attempt in range(retries):
        try:
            req = urllib.request.Request(OLLAMA_URL, data=json.dumps(payload).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=180) as res:
                data = json.loads(res.read().decode('utf-8'))
                return data.get('message', {}).get('content', '').strip()
        except Exception as e:
            print(f"[Ollama Error Attempt {attempt+1}]: {e}", flush=True)
            time.sleep(3)
    return ""

SYSTEM_PROMPT = """あなたは「教育情報分析研究会」の専任数学講師です。
高校生（数学A『論理と集合』『場合の数と確率』、情報I『論理演算と論理回路』）に向けて、
ルイス・キャロル（チャールズ・ドジソン）の歴史的著作『The Game of Logic（論理の遊戯）』(1886年) を、
極めて詳細かつ分かりやすく、学術的厳密性と親身な語り口で解説してください。
嘘や想像を排し、原著のテキストと数学的本質に完全に忠実に記述してください。"""

CHAPTERS = [
    (1, "不思議の国の数学者 —— チャールズ・ドジソンと『論理の遊戯』の世界",
     "The Mathematician of Wonderland and The Game of Logic",
     """【講義内容：第1章 前半】
ルイス・キャロルことチャールズ・ラトウィッジ・ドジソン（オックスフォード大学クライスト・チャーチ数学講師）の生涯と二面性について語ってください。
彼がなぜ世界的な児童文学『不思議の国のアリス』を生み出す一方で、このような本格的記号論理学の入門書『The Game of Logic』を著したのか。
当時のヴィクトリア朝における伝統的アリストテレス論理学の堅苦しさと限界、そして「論理を退屈な暗記ではなく、赤と白のカウンターとゲーム盤を使った心躍る知的遊戯にする」というキャロルの革命的着想を、高校生に向けて約2000字で熱く語ってください。""",
     """【講義内容：第1章 後半】
原著の冒頭にある子ども読者への詩（To my Child-friend）や、ゲームの用具（9枚のカウンター：赤4枚、灰5枚、そして2つのダイアグラム）の数学的意図を解説してください。
クリケットに22人必要なのに対し、このゲームは「たった1人（できれば2人で間違いを正し合いながら）」でプレイできるというキャロルのユーモア。
そして、このゲームが現代の数学（高校数学Aの集合と命題、高校数学B/Cの統計的推測）や情報科学（ブール論理・プログラミングの条件分岐）といかに直結しているのかを、高校生向けに約2000字で詳細に解説してください。"""
    ),

    (2, "キャロル・ボードの誕生 —— 宇宙を四分割する「2属性ダイアグラム」",
     "The Smaller Diagram and the Division of the Universe",
     """【講義内容：第2章 前半】
キャロルの論理図の基本となる「Smaller Diagram（2属性ダイアグラム）」の幾何学的構造について徹底解説してください。
議論の領域である万有集合（Universe of Discourse）とは何か。
属性 x（例えば「新しいケーキ」）とその否定 x'（「新しくないケーキ」）による上下の二分割（North and South）。
属性 y（例えば「おいしい」）とその否定 y'（「おいしくない」）による左右の二分割（West and East）。
これによって宇宙が4つの小部屋（Cells: xy, xy', x'y, x'y'）に完全に排他的かつ網羅的に分割される論理の幾何学を、高校数学の集合（共通部分、補集合）と対比させながら約2000字で解説してください。""",
     """【講義内容：第2章 後半】
4つのセル（xy, xy', x'y, x'y'）それぞれに属する事物とは何か、具体的なキャロル流の例（ケーキ、林檎、学生など）を用いて丁寧に分析してください。
境界線（Boundaries）の意味、属性の有無がどのように空間内の位置として定まるのか。
オイラー図やベン図（円の重なり）と比較したとき、なぜキャロルの四角形分割ダイアグラムが直観的であり、誤りを防ぐ上で極めて優れているのかを、数理的視点から約2000字で解説してください。"""
    ),

    (3, "赤と白のカウンター —— 存在と無を可視化するシンボル体系",
     "Red and Grey Counters: The Visual Algebra of Existence and Non-Existence",
     """【講義内容：第3章 前半】
キャロルが考案したカウンターの色のルールを徹底的に掘り下げてください。
「赤カウンター（Red Counter）」＝ 存在（Exist, FULL, 1以上）。その部屋に少なくとも1つの事物が存在する。
「灰（白）カウンター（Grey Counter）」＝ 空（Empty, 0）。その部屋には1つの事物も存在しない（空集合）。
そして「カウンターが置かれていない状態」＝ 情報なし（Unknown / 未定）。
この「3つの状態（存在・空・未定）」の区別が、形式論理学においてどれほど画期的であったかを、高校生向けに約2000字で論じてください。""",
     """【講義内容：第3章 後半】
情報科学におけるビット（0と1）および三値論理（True, False, Unknown）との深い関連を解説してください。
ブール代数における 0 と 1 の代数演算が、キャロルの盤上では物理的なカウンターの配置としていかに直感的に操作できるか。
高校数学の「空集合 $\emptyset$」と「要素の存在 $\exists$」の記号が、赤と灰のコインでどのように完璧に可視化されるのかを、高校生が手を動かして実感できるよう約2000字で解説してください。"""
    ),

    (4, "3つの基本命題 —— Some, No, All をボード上に配置する",
     "Three Fundamental Propositions: Some, No, and All on the Board",
     """【講義内容：第4章 前半】
キャロルが『論理の遊戯』で用いる3つの基本命題について詳しく解説してください。
1. 特称肯定命題（Some x are y）：いくつかの新しいケーキはおいしい。
2. 全称否定命題（No x are y）：いかなる新しいケーキもおいしくない。
3. 全称肯定命題（All x are y）：すべての新しいケーキはおいしい。
それぞれの命題が、Smaller Diagram 上のどのセルに赤カウンターや灰カウンターを置くことによって表現されるのか、その精密なプロット規則を約2000字で解説してください。""",
     """【講義内容：第4章 後半】
論理学史上の大論争である「存在前提（Existential Import）」に対するキャロルの独自の見解を解説してください。
現代論理学では「All x are y」は $x \to y$（xが空集合でも真）と解釈されますが、キャロルは「All x are y」を「No x are y'（新しくておいしくないものはない）」かつ「Some x are y（新しいケーキは実際に存在する）」という2つの命題の合成として定義しました。
なぜキャロルはこの立場をとったのか、日常言語の直感と数理の厳密性の狭間で彼が下した決断を、高校生向けに約2000字で明快に解き明かしてください。"""
    ),

    (5, "中項の導入と「3属性ダイアグラム」 —— 8つの小部屋が織りなす思考空間",
     "The Larger Diagram and Eight Compartments: Introducing the Middle Term",
     """【講義内容：第5章 前半】
三段論法を解くための決定的な武器である「Larger Diagram（3属性ダイアグラム）」の幾何学構造を解説してください。
2つの前提をつなぐ媒介項である「中項（Middle Term $m$）」の役割。
キャロルは外側の正方形の中に内側の正方形を配置し、内側を $m$、外側の枠を $m'$ と定義しました。
上下（$x, x'$）、左右（$y, y'$）、内外（$m, m'$）という3つの二項対立が組み合わさることで、空間全体が $2^3 = 8$ 個の小部屋に分割される美しい幾何学的シンメトリーを約2000字で解説してください。""",
     """【講義内容：第5章 後半】
8つの小部屋（xym, xym', xy'm, xy'm', x'ym, x'ym', x'y'm, x'y'm'）のそれぞれの意味と、事物の分類を解説してください。
ジョン・ヴェンの3円ダイアグラム（ヴェン図）とキャロルの3属性長方形ダイアグラムを比較し、なぜキャロル図の方が対称性に優れ、境界の認識が容易であるのか。
高校数学の3事象のベン図 $A \cap B \cap C$ とキャロル図の完全な同型性を、高校生向けに約2000字で解説してください。"""
    ),

    (6, "三段論法の完全解法（前編） —— 二つの前提をボードにプロットする技術",
     "Plotting the Syllogism: Expressing Two Premises on the Larger Board",
     """【講義内容：第6章 前半】
大前提（Premise 1: $x$ と $m$ の関係）と小前提（Premise 2: $y$ と $m$ の関係）を、3属性ダイアグラム上にプロットする具体的な手順を解説してください。
キャロル独特の卓越した発明である「境界線上に座るカウンター（Sitting on the fence）」の技法。
例えば「Some $x$ are $m$」と言われたとき、それが $y$ なのか $y'$ なのか分からないため、カウンターを $xym$ と $xy'm$ の間の境界線（fence）の上に置くという視覚的表現のルールを約2000字で詳細に解説してください。""",
     """【講義内容：第6章 後半】
キャロルの名作パズルを用いた具体例のステップ・バイ・ステップ解説。
例題：「すべてのケーキは甘い（All $x$ are $m$）」「甘いものは健康的ではない（No $m$ are $y$）」。
第1前提から灰カウンターを置き、境界線上の赤カウンターがどのように内側のセルへと押し出される（落とされる）のか。
2つの前提が合わさることで情報が確定していくダイナミックな思考のプロセスを、約2000字で生き生きと解説してください。"""
    ),

    (7, "三段論法の完全解法（後編） —— 中項の消去と結論のトランスファー",
     "Elimination of the Middle Term and Transfer of Conclusions",
     """【講義内容：第7章 前半】
三段論法の核心である「中項の消去（Elimination of the Middle Term $m$）」のアルゴリズムを徹底解説してください。
中項 $m$ は前提をつなぐ足場に過ぎず、最終的な結論（Conclusion）には現れてはなりません。
3属性ダイアグラム上で $m$ と $m'$ を統合し、残された $x$ と $y$ の関係だけを抽出して「Smaller Diagram（2属性ボード）」へと転写（Transfer）する幾何学的ルールを約2000字で解き明かしてください。""",
     """【講義内容：第7章 後半】
アリストテレス以来、中世の学者たちが呪文のように暗記した伝統的三段論法の格と式（Barbara, Celarent, Darii, Ferio など全19形式）。
キャロルのゲーム盤を使えば、暗記など一切不要で、すべて同一のシンプルな機械的ルール（プロット $\to$ 整理 $\to$ 転写）で自動的に正しい結論が導き出せるという知的快感を、高校生向けに約2000字で解説してください。"""
    ),

    (8, "論理の落とし穴 —— キャロル・ボードが暴く「形式的誤謬」",
     "Fallacies Unmasked: The Fallacy of Undistributed Middle and Beyond",
     """【講義内容：第8章 前半】
誤った推論である「誤謬（Fallacies）」が、キャロル・ボード上でどのように視覚的に暴かれるかを解説してください。
論理学で最も頻出する「中項不周延の誤謬（Fallacy of Undistributed Middle）」。
例えば「犬は動物である」「猫は動物である」ゆえに「犬は猫である」という誤謬。
キャロル・ボード上では、カウンターが境界線（fence）上に留まったままどちらのセルにも落ちず、結論の Smaller Diagram に転写できないこととして完璧に可視化されるメカニズムを約2000字で解説してください。""",
     """【講義内容：第8章 後半】
「両前提否定の誤謬（Fallacy of Negative Premises）」や「不当全称の誤謬（Illicit Major/Minor）」の解明。
日常会話やSNS、メディアの議論でしばしば見られる詭弁・誤謬のパターン。
キャロルのボードを手にした高校生が、世の中の怪しい議論の前提の破綻を一瞬で見破れるようになる論理的リテラシーの武器としての価値を、約2000字で力強く語ってください。"""
    ),

    (9, "キャロル図からカルノー図へ —— 現代デジタル回路と情報科学への直結",
     "From Carroll Diagrams to Karnaugh Maps and Modern Digital Logic",
     """【講義内容：第9章 前半】
19世紀のキャロル図が、20世紀半ばにベル研究所のモーリス・カルノーによって再発見され、「カルノー図（Karnaugh Map）」としてデジタル回路設計の標準手法となった歴史的奇跡を解説してください。
隣接するセル同士が1ビットだけ変化するグレイコード配置と、キャロルの正方形分割の一致。
ブール代数の論理式（論理積 AND、論理和 OR、排他的論理和 XOR）が、キャロル・ボード上でどのように視覚的に単純化・圧縮されるかを約2000字で解説してください。""",
     """【講義内容：第9章 後半】
高校「情報I」で学ぶ真理値表、論理ゲート（AND回路、OR回路、NOT回路、NAND回路）、半加算器（Half Adder）の仕組みとの接続。
コンピュータがなぜキャロルと同じ「2つの状態（0と1）」の配置だけであらゆる計算、画像処理、AIのニューラルネットワークまで実行できるのか。
論理の遊戯が現代の情報化社会の物理的基盤である驚きを約2000字で解説してください。"""
    ),

    (10, "論理から確率へ —— キャロル・ボードで解く条件付き確率とベイズの定理",
     "From Logic to Probability: Conditional Probability and Bayes' Theorem on the Board",
     """【講義内容：第10章 前半】
論理学のボードを「確率空間」として再解釈する数理的飛躍を解説してください。
ボード全体の面積を全確率 1 とし、各セルの面積を結合確率 $P(x, y)$ とみなす。
赤カウンターを「生起確率の重み（Probability Mass）」として解釈したとき、高校数学Aで学ぶ「条件付き確率 $P(Y|X) = \frac{P(X \cap Y)}{P(X)}$」が、ボード上の特定の領域（行や列）への「ズームインと面積比」として直感的に理解できることを約2000字で解説してください。""",
     """【講義内容：第10章 後半】
現代のデータサイエンスとAIの根幹である「ベイズの定理（逆確率の計算）」のキャロル・ボード解法。
感染症のPCR検査（有病率、感度、特異度）を例に、陽性と判定されたときに本当に感染している確率を、ボード上のセルの面積比から一発で導く鮮やかな解法。
事前確率から事後確率への更新が、キャロルのカウンターの移動としていかに直感的に理解できるかを約2000字で詳細に解説してください。"""
    ),

    (11, "言葉の迷宮とパズル演習 —— 『論理の遊戯』原著の傑作問題に挑む",
     "Cross Questions and Crooked Answers: Carrollian Logic Puzzles",
     """【講義内容：第11章 前半】
原著『The Game of Logic』の第2章（Cross Questions）と第3章（Crooked Answers）に収録された、キャロルならではのユーモラスなパズルを厳選して解説してください。
「すべての赤ちゃんは非論理的である」「ワニを軽蔑する者はいない」「非論理的な人間はワニを飼いならすことができない」などの奇想天外な命題。
言葉の綾に惑わされず、主語・述語・中項を正確に記号化し、ボード上にプロットして解く快感を約2000字で解説してください。""",
     """【講義内容：第11章 後半】
多段の前提が連なる「連鎖三段論法（ソリテス / Sorites）」の解法テクニック。
3つ以上の属性（4属性、5属性）へと拡張されるキャロルの論理図のアイデア。
日常言語の曖昧さを排し、厳密な数学的命題へと翻訳する「論理的読解力」の重要性を、大学入試現代文や小論文、数学の証明問題への応用と絡めて約2000字で解説してください。"""
    ),

    (12, "論理的思考の真髄 —— 記号・図・ゲームがひらく数学の未来",
     "The Essence of Logical Thinking: Games, Symbols, and the Future of Mathematics",
     """【講義内容：第12章 前半】
アリストテレスから始まり、ブール、ヴェン、キャロル、フレーゲ、ラッセル、ゲーデル、チューリングへと至る数理論理学の壮大な歴史的潮流の総括。
「推論を計算にし、計算をゲームにする」というキャロルの哲学が、いかにして20世紀の計算可能性理論やプログラミング言語の誕生を予告していたかを約2000字で振り返ってください。""",
     """【講義内容：第12章 後半】
高校生読者への熱いエールと結びのメッセージ。
AIが急速に普及する現代社会において、人間が「論理的に正しく考えること」「前提の正しさを批判的に吟味すること」がなぜかつてなく重要になっているのか。
本書で学んだキャロルの思考の遊戯盤を胸に、自分の頭で考え、真理を探求していく未来の科学者・市民としての姿勢を約2000字で力強く語ってください。"""
    )
]

def generate_all():
    print(f"=== Starting Carroll The Game of Logic text generation ===", flush=True)
    total_chapters = len(CHAPTERS)
    
    for num, title, en_title, prompt1, prompt2 in CHAPTERS:
        out_file = os.path.join(CACHE_DIR, f"ch{num}.txt")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 5000:
            print(f"[Chapter {num}/{total_chapters}] Already cached ({os.path.getsize(out_file)} bytes). Skipping.", flush=True)
            continue
            
        print(f"\n[Chapter {num}/{total_chapters}] Generating {title}...", flush=True)
        
        t0 = time.time()
        print(f"  -> Part 1 querying...", flush=True)
        part1 = query_ollama(prompt1, SYSTEM_PROMPT)
        t1 = time.time()
        print(f"  -> Part 1 finished in {t1-t0:.2f}s ({len(part1)} chars)", flush=True)
        
        print(f"  -> Part 2 querying...", flush=True)
        part2 = query_ollama(prompt2, SYSTEM_PROMPT)
        t2 = time.time()
        print(f"  -> Part 2 finished in {t2-t1:.2f}s ({len(part2)} chars)", flush=True)
        
        full_content = f"## 第{num}章：{title}\n\n{part1}\n\n### 講義の深化と応用展開\n\n{part2}\n"
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"[Chapter {num}] Saved {len(full_content)} chars to {out_file} (Total: {t2-t0:.2f}s)", flush=True)

if __name__ == '__main__':
    generate_all()
