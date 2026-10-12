import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath('e:/GoogleAntigravity/PG_mathbook/scripts'))
import gemma_client

BOOK_DIR = 'e:/GoogleAntigravity/PG_mathbook/books/57359_venn_logic_of_chance'
CACHE_FILE = os.path.join(BOOK_DIR, 'gemma_generated_cache.json')
os.makedirs(BOOK_DIR, exist_ok=True)

PROMPTS = {
    "foreword": """高校生に向けて、「集合の『ヴェン図』で超有名なジョン・ヴェンの名著『偶然の論理（The Logic of Chance）』で学ぶ確率と統計」のまえがきを、熱心な高校数学の先生の語り口で書いてください。
誰もが知るヴェン図の生みの親が、実は近代統計学の「頻度主義（客観的なデータ重視）」の扉を開いた大哲学者・数学者であった驚きと、前作のラプラスとの対比、高校数学（数Aの集合・確率、数B・数Cの統計）に直結する面白さを、ワクワクする文体で300字程度で伝えてください。""",

    "ch1_intro": """高校生に向けて、「確率は心の主観か、それとも客観的な事実か？」というテーマを説明してください。
ラプラスが『同様に確からしいという私たちの信念』に重きを置いたのに対し、ジョン・ヴェンは『そんな主観ではなく、何千回も実際に繰り返したときの客観的なデータの割合（頻度）こそが確率だ！』と真っ向から挑みました。
サイコロやコイン、スマートフォンのガチャを例にして、この歴史的な大論争の面白さを高校生に語りかける口調で350字程度で解説してください。""",

    "ch1_column": """高校生向けの探究コラムとして、「ヴェン図はなぜ生まれたのか？：複雑な論理と確率を一目で解き明かすグラフィック革命」について、ヴェン図が生まれた歴史的背景と視覚的思考の威力を250字程度で書いてください。""",

    "ch2_intro": """高校生に向けて、ジョン・ヴェンの核となるアイデア「確率の系列（Probability Series）と相対度数の安定」を解説してください。
1回や2回のコイン投げでは表が出るか裏が出るかはまったく予測できない。しかし、100回、1000回、10000回と系列を伸ばしていくと、相対度数（表の出た割合）が不思議なほど一定の数値（1/2）にピタリと落ち着いていく「統計的規則性」の感動を、高校生に親身に語りかける口調で350字程度で語ってください。""",

    "ch2_column": """高校生向けの探究コラムとして、「コンピュータの乱数は本当にランダムか？：疑似乱数とヴェンの系列論」について、ゲームやプログラミングで使われる乱数が実は計算によって作られていることの面白さを250字程度で書いてください。""",

    "ch3_intro": """高校生に向けて、「ランダム（偶然）とは何か？：幾何学的確率と一様性の罠」を解説してください。
円の中にランダムに点を打つ、あるいは針を落とす（ビュフォンの針）。面積や長さの比率で確率を計算する「幾何学的確率」の美しさと、実は『ランダムに選ぶ』という言葉には慎重な定義が必要だというヴェンの鋭い警告を、高校生向けに350字程度で分かりやすく教えてください。""",

    "ch3_column": """高校生向けの探究コラムとして、「ビュフォンの針実験：針を落とすだけで円周率πが求まる奇跡の数学」について、偶然の試行から幾何学の定数πが浮かび上がる驚きを250字程度で解説してください。""",

    "ch4_intro": """高校生に向けて、「ヴェン図でマスターする条件付き確率：全体集合の『ズームイン』」を解説してください。
公式 P(B|A) = P(AかつB) / P(A) を丸暗記するのではなく、ヴェン図を使うと「全体の舞台（全事象S）から、事象Aという円の中にズームインして新しい世界を作ったとき、その中でBが占める面積比」として直感的に一瞬で理解できる魔法を、高校生に語りかける口調で350字程度で解説してください。""",

    "ch4_column": """高校生向けの探究コラムとして、「論理回路と現代のコンピュータ：ヴェン図・ブール代数が作ったスマホの頭脳」について、集合演算（AND, OR, NOT）がCPUの基礎になっているつながりを250字程度で書いてください。""",

    "ch5_intro": """高校生に向けて、「現実のデータは綺麗な正規分布ばかりではない！：ヴェンの警告と非対称データの現実」を解説してください。
数学の理論では綺麗な左右対称のベルカーブ（正規分布）を仮定しがちですが、ヴェンは『現実の社会データや人間の能力・所得などは、左右非対称に歪んでいたり外れ値がある！』と看破しました。
テストの点数やYouTuberの再生数、現代のデータサイエンスを例に、現実を見る大切さを350字程度で熱く語ってください。""",

    "ch5_column": """高校生向けの探究コラムとして、「平均値の罠：年収や再生数は『中央値』で見ないと騙される理由」について、外れ値に引っ張られる平均値と頑健な中央値の違いを身近な例で250字程度で解説してください。""",

    "ch6_intro": """高校生に向けて、「データから法則を導く『帰納法（Induction）』と現代の統計的推測」を解説してください。
演繹法（前提から結論を導く）だけでなく、バラバラな観察データから背後にある真実を推理する『帰納法』こそが近代科学と統計学のエンジンです。
偶然起きたことなのか、それとも意味のある差（有意差）なのかを見極める知恵を、高校生にエールを送る口調で350字程度で語ってください。""",

    "ch6_column": """高校生向けの探究コラムとして、「仮説検定の第一歩：『偶然とは考えにくい』を数学にする方法」について、高校生にもわかるコインのイカサマ見破り法（P値の基本直感）を250字程度で書いてください。""",

    "afterword": """高校生に向けて、本書のまとめとして「ラプラスの直感とヴェンのデータ主義、両方の眼を持って未知の世界に漕ぎ出そう」というメッセージを情熱的に250字程度で書いてください。"""
}

def run():
    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except Exception:
            cache = {}

    print(f"Starting Venn text generation. Already cached: {len(cache)}/{len(PROMPTS)}", flush=True)

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

    print("All Venn sections completed!", flush=True)

if __name__ == '__main__':
    run()
