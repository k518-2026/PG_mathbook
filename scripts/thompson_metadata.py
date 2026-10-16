# -*- coding: utf-8 -*-
"""
Map of all 26 sections of Silvanus P. Thompson's Calculus Made Easy (#33283)
"""

SECTIONS_METADATA = [
    {
        "id": "preface",
        "number": "序文",
        "title_en": "Preface to the Second Edition",
        "title_ja": "第2版への序文",
        "subtitle_ja": "多くの初学者が微積分を克服した驚くべき成功の記録"
    },
    {
        "id": "prologue",
        "number": "プロローグ",
        "title_en": "Prologue",
        "title_ja": "プロローグ",
        "subtitle_ja": "「一人の人間にできることは、他の人間にもできる」"
    },
    {
        "id": "chap_01",
        "number": "第1章",
        "num_roman": "I",
        "title_en": "To deliver you from the Preliminary Terrors",
        "title_ja": "予備的恐怖からの解放",
        "subtitle_ja": "dx と dy という記号の真の意味・難解そうに見える数学記号の正体"
    },
    {
        "id": "chap_02",
        "number": "第2章",
        "num_roman": "II",
        "title_en": "On Different Degrees of Smallness",
        "title_ja": "小ささの異なる階級について",
        "subtitle_ja": "微小量と高次の微小量・無視してよい微小部分の幾何学的・代数的根拠"
    },
    {
        "id": "chap_03",
        "number": "第3章",
        "num_roman": "III",
        "title_en": "On Relative Growings",
        "title_ja": "相対的増大について",
        "subtitle_ja": "変化率・微分係数 dy/dx の直観的把握と相互関係"
    },
    {
        "id": "chap_04",
        "number": "第4章",
        "num_roman": "IV",
        "title_en": "Simplest Cases",
        "title_ja": "最も単純なケース",
        "subtitle_ja": "べき関数 y = x^n の微分の基本公式とその第一原理からの導出"
    },
    {
        "id": "chap_05",
        "number": "第5章",
        "num_roman": "V",
        "title_en": "Next Stage. What to do with Constants",
        "title_ja": "次の段階：定数の扱い方",
        "subtitle_ja": "加法定数と乗法定数・定数の微分がゼロになる理由"
    },
    {
        "id": "chap_06",
        "number": "第6章",
        "num_roman": "VI",
        "title_en": "Sums, Differences, Products and Quotients",
        "title_ja": "和・差・積および商の微分法",
        "subtitle_ja": "複合関数の基本微分則・積の微分法 (u·v) と商の微分法 (u/v)"
    },
    {
        "id": "chap_07",
        "number": "第7章",
        "num_roman": "VII",
        "title_en": "Successive Differentiation",
        "title_ja": "逐次微分法（高階微分）",
        "subtitle_ja": "2階微分・3階微分の意味と加速度の物理的導出"
    },
    {
        "id": "chap_08",
        "number": "第8章",
        "num_roman": "VIII",
        "title_en": "When Time Varies",
        "title_ja": "時間が変化するとき（時間変化率）",
        "subtitle_ja": "速度・加速度・物理現象における時間の導関数と連鎖律の直観"
    },
    {
        "id": "chap_09",
        "number": "第9章",
        "num_roman": "IX",
        "title_en": "Introducing a Useful Dodge",
        "title_ja": "便利な巧妙法（合成関数の微分法・連鎖律）",
        "subtitle_ja": "置換変数を用いた dy/dx = (dy/du)·(du/dx) の自在な計算技法"
    },
    {
        "id": "chap_10",
        "number": "第10章",
        "num_roman": "X",
        "title_en": "Geometrical Meaning of Differentiation",
        "title_ja": "微分の幾何学的意味",
        "subtitle_ja": "接線の傾き・dy/dx の図形的可視化・曲線の傾斜の決定"
    },
    {
        "id": "chap_11",
        "number": "第11章",
        "num_roman": "XI",
        "title_en": "Maxima and Minima",
        "title_ja": "極大値と極小値（最適化問題）",
        "subtitle_ja": "導関数が0となる点・2階微分の符号による極大極小判定と実用問題への応用"
    },
    {
        "id": "chap_12",
        "number": "第12章",
        "num_roman": "XII",
        "title_en": "Curvature of Curves",
        "title_ja": "曲線の曲率",
        "subtitle_ja": "曲線の曲がり具合・曲率半径の微分幾何学的定式化"
    },
    {
        "id": "chap_13",
        "number": "第13章",
        "num_roman": "XIII",
        "title_en": "Other Useful Dodges",
        "title_ja": "その他の便利な巧妙法（部分分数展開・逆関数）",
        "subtitle_ja": "複雑な有理関数の部分分数分解・逆関数微分法 dx/dy = 1/(dy/dx)"
    },
    {
        "id": "chap_14",
        "number": "第14章",
        "num_roman": "XIV",
        "title_en": "On true Compound Interest and the Law of Organic Growth",
        "title_ja": "真の複利計算と有機的成長の法則",
        "subtitle_ja": "自然対数の底 e・指数関数 e^x の微分・放射性崩壊と人口増加モデル"
    },
    {
        "id": "chap_15",
        "number": "第15章",
        "num_roman": "XV",
        "title_en": "How to deal with Sines and Cosines",
        "title_ja": "正弦（サイン）と余弦（コサイン）の微分法",
        "subtitle_ja": "三角関数の幾何学的増分・sin x と cos x の導関数と周期的現象"
    },
    {
        "id": "chap_16",
        "number": "第16章",
        "num_roman": "XVI",
        "title_en": "Partial Differentiation",
        "title_ja": "偏微分法",
        "subtitle_ja": "多変数関数・一方の変数を固定して微分する偏導関数の直観的理解"
    },
    {
        "id": "chap_17",
        "number": "第17章",
        "num_roman": "XVII",
        "title_en": "Integration",
        "title_ja": "積分法",
        "subtitle_ja": "微分の逆演算としての積分・不定積分と積分定数 C の正体"
    },
    {
        "id": "chap_18",
        "number": "第18章",
        "num_roman": "XVIII",
        "title_en": "Integrating as the Reverse of Differentiating",
        "title_ja": "微分の逆演算としての積分計算",
        "subtitle_ja": "基本関数の積分公式・多項式・分数式・べき関数の積分"
    },
    {
        "id": "chap_19",
        "number": "第19章",
        "num_roman": "XIX",
        "title_en": "On Finding Areas by Integrating",
        "title_ja": "積分による面積の求値法（定積分）",
        "subtitle_ja": "定積分・微小区間の無限和・曲線の下の面積の厳密計算"
    },
    {
        "id": "chap_20",
        "number": "第20章",
        "num_roman": "XX",
        "title_en": "Dodges, Pitfalls, and Triumphs",
        "title_ja": "積分の巧妙法・落とし穴・そして勝利",
        "subtitle_ja": "置換積分・部分積分・三角置換・微積分学の高度な実践技巧"
    },
    {
        "id": "chap_21",
        "number": "第21章",
        "num_roman": "XXI",
        "title_en": "Finding some Solutions",
        "title_ja": "微分方程式の解法",
        "subtitle_ja": "変数分離形微分方程式・物理現象や工学問題の数理モデルの完全解"
    },
    {
        "id": "epilogue",
        "number": "エピローグ",
        "title_en": "Epilogue and Apologue",
        "title_ja": "エピローグと寓話",
        "subtitle_ja": "読者への激励・数学の門をくぐり抜けた旅人へ"
    },
    {
        "id": "standard_forms",
        "number": "付録1",
        "title_en": "Table of Standard Forms",
        "title_ja": "標準公式一覧表",
        "subtitle_ja": "すべての微積分公式の体系的便覧"
    },
    {
        "id": "answers",
        "number": "付録2",
        "title_en": "Answers to Exercises",
        "title_ja": "全演習問題解答",
        "subtitle_ja": "原著全章の全問完全解答集"
    }
]

print(f"Loaded metadata for {len(SECTIONS_METADATA)} sections.")
