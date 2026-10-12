import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('e:/GoogleAntigravity/PG_mathbook/scripts'))
import gemma_client

BOOK_DIR = 'e:/GoogleAntigravity/PG_mathbook/books/58881_laplace_probability'
CACHE_FILE = os.path.join(BOOK_DIR, 'gemma_generated_cache.json')
os.makedirs(BOOK_DIR, exist_ok=True)

PROMPTS = {
    "foreword": """高校生に向けて、「ピエール＝シモン・ラプラス『確率の哲学的試論』を通して確率と統計を学ぶ意義」について、熱心な高校数学の先生の語り口で前書き（まえがき）を書いてください。
なぜ高校生が今この古典を読むべきなのか、スマホやAIや進路決定といった現代社会との繋がり、確率を学ぶと世界がどう見えてくるかを、親しみやすくワクワクする文体で300字程度で伝えてください。""",

    "ch1_intro": """高校生に向けて、ラプラスの「決定論」と「確率の役割」を説明してください。
もし宇宙のすべての原子の位置と速度を知る「ラプラスの悪魔」がいたら未来はすべて計算できるはずなのに、なぜ私たちは「確率」という考え方を必要とするのか？
天気予報やサイコロを例にして、私たちの「無知」を補うための知恵としての確率の魅力を、高校生に語りかける口調で350字程度で解説してください。""",

    "ch1_column": """高校生向けの探究コラムとして、「もしラプラスの悪魔が本当にいたら、私たちの自由意志はどうなるのか？」というテーマで、知的好奇心を刺激する文章を250字程度で書いてください。現代の量子力学の不確定性にも触れてください。""",

    "ch2_intro": """高校生に向けて、「期待値（数学的期待値）」と「精神的期待値（効用）」の違いについて解説してください。
宝くじを買う時やゲームのガチャを引く時、数学的な期待値はマイナスでも、なぜ人は挑戦するのか？
「1000円の価値は人によって違う」というダニエル・ベルヌーイやラプラスの考え方を交え、高校生に親しみやすく350字程度で解説してください。""",

    "ch2_column": """高校生向けの探究コラムとして、「高校生のお小遣いと期待値のリアル：ギャンブルの胴元はなぜ必ず勝つのか？」について、控除率と大数の法則の観点から分かりやすく250字程度で書いてください。""",

    "ch3_intro": """高校生に向けて、ラプラスの確率論の真骨頂である「逆確率（ベイズの定理）」の面白さを解説してください。
「原因から結果を計算する」通常の確率に対して、「すでに起こった結果から、背後にある原因の確率を推測する」とはどういうことか？
医療検査の陽性反応や迷惑メールフィルターを例にして、高校生が納得するわかりやすい例えで350字程度で語ってください。""",

    "ch3_column": """高校生向けの探究コラムとして、「裁判員裁判と確率：ラプラスが考えた『無実の罪を防ぐ数学』」について、目撃証言の誤りや状況証拠をベイズ的にどう考えるべきかを高校生向けに250字程度で解説してください。""",

    "ch4_intro": """高校生に向けて、「大数の法則」と「正規分布（ガウス分布）」の感動的な美しさを解説してください。
コインを投げると、表か裏かはまったくの偶然。しかし、それを何千回と繰り返すと、美しいベル型の曲線（正規分布）が忽然と現れる。
バラバラな偶然が集まると確固たる必然（法則）が生まれる不思議さを、高校生に向けて熱く350字程度で語ってください。""",

    "ch4_column": """高校生向けの探究コラムとして、「テストの偏差値の正体：なぜみんな正規分布を信じるのか？」について、模試の偏差値（平均50、標準偏差10）が正規分布とどう結びついているかを250字程度で解説してください。""",

    "ch5_intro": """高校生に向けて、「天体観測のズレから生まれた統計学（最小二乗法）」と「現代のAI・データサイエンス」のつながりを解説してください。
惑星の軌道を観測する時の「測定誤差」をどうやって乗り越えたのか？
散布図に直線を引く最小二乗法が、現代のAIの基本原理になっていることを、高校生にワクワクする口調で350字程度で教えてください。""",

    "ch5_column": """高校生向けの探究コラムとして、「データに騙されないための統計リテラシー：相関関係と因果関係の違い」について、「アイスが売れると水難事故が増える」などの例を使って250字程度で解説してください。""",

    "ch6_intro": """高校生に向けて、「ギャンブラーの誤謬（ごびゅう）」と確率の直感の罠について解説してください。
コイン投げで裏が連続したとき、「次は表が出るはずだ」と感じる錯覚。
ラプラスが警告した「人間の直感は確率においていかに騙されやすいか」を、高校生に親しみやすく350字程度で語ってください。""",

    "ch6_column": """高校生向けの探究コラムとして、「モンティ・ホール問題：直感と数学が激突する3つの扉」について、なぜ扉を変えると当たる確率が2倍（2/3）になるのか、直感を覆すポイントを250字程度で書いてください。""",

    "afterword": """高校生に向けて、本書のまとめとして「確率的思考を身につけて、不確実な未来を楽しもう」というメッセージを情熱的に250字程度で書いてください。"""
}

def run():
    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except Exception:
            cache = {}

    print(f"Starting generation. Already cached: {len(cache)}/{len(PROMPTS)}", flush=True)

    for i, (key, prompt) in enumerate(PROMPTS.items(), 1):
        if key in cache and cache[key]:
            print(f"[{i}/{len(PROMPTS)}] {key} is already cached.", flush=True)
            continue

        print(f"[{i}/{len(PROMPTS)}] Generating {key}...", flush=True)
        start_t = time.time()
        reply = gemma_client.query_gemma(prompt, max_tokens=500, temperature=0.7)
        elapsed = time.time() - start_t

        if reply:
            cache[key] = reply
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)
            print(f"  -> Generated {key} in {elapsed:.2f}s ({len(reply)} chars)", flush=True)
        else:
            print(f"  -> FAILED {key}", flush=True)

    print("All sections completed!", flush=True)

if __name__ == '__main__':
    run()
