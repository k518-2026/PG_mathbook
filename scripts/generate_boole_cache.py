import os
import sys
import json
import time
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

BOOK_DIR = 'e:/GoogleAntigravity/PG_mathbook/books/15114_boole_laws_of_thought'
CACHE_FILE = os.path.join(BOOK_DIR, 'ollama_generated_cache.json')
os.makedirs(BOOK_DIR, exist_ok=True)

OLLAMA_URL = "http://192.168.128.62:11434/api/chat"
MODEL_NAME = "qwen3.5:9b"

def query_ollama_stream(prompt, system_prompt=None, retries=3):
    headers = {"Content-Type": "application/json"}
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": True,
        "options": {
            "temperature": 0.7,
            "num_predict": 1200
        }
    }

    for attempt in range(retries):
        try:
            req = urllib.request.Request(OLLAMA_URL, data=json.dumps(payload).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=120) as res:
                full_text = ""
                for line in res:
                    if line:
                        chunk = json.loads(line.decode('utf-8'))
                        msg = chunk.get('message', {}).get('content', '')
                        full_text += msg
                        if chunk.get('done', False):
                            break
                return full_text.strip()
        except Exception as e:
            print(f"[Ollama] Attempt {attempt+1} failed: {e}", flush=True)
            time.sleep(3)
    return ""

SYSTEM_TEACHER = "あなたは教育情報分析研究会の専任数学講師です。高校生に向けて、ジョージ・ブールの『思考の法則』で論理と確率がどのように統一されたかを、深い数学的知見と親身でわかりやすい語り口で解説してください。"

PROMPTS = {
    "foreword": """高校生に向けて、「ジョージ・ブール『思考の法則（An Investigation of the Laws of Thought）』で学ぶ論理と確率の数学」のまえがきを、熱意あふれる指導者の語り口で書いてください。
ブール代数がすべてのコンピュータ・スマホ・AIの基礎であること、そして本書が論理だけでなく確率論を方程式として解く大革命であったこと、ラプラスやヴェンとの違いを交え、高校数学を学ぶ君たちに一生ものの武器になることを、充実した分量（600字程度）で力強く伝えてください。""",

    "ch1_intro": """高校生に向けて、「第1章：思考を計算する —— ブール代数の夜明け」の導入講義を書いてください。
言葉の論理を数学の記号で表すとはどういうことか？
べき等律 x^2 = x がなぜ「真（1）と偽（0）」の2値の世界を決定づけるのか。
AND（論理積）、OR（論理和）、NOT（否定）の演算規則が、高校数学の「集合の共通部分・和集合・補集合」と完全に一致する感動を、具体例を交えて詳しく（600字程度）解説してください。""",

    "ch1_column": """高校生向け探究コラムとして、「ブール代数とデジタル回路：0と1のスイッチがスマホの頭脳になるまで」について、クロード・シャノンの修士論文の快挙や論理ゲート（AND/OR/NOT/NAND）の仕組みを詳しく（400字程度）書いてください。""",

    "ch2_intro": """高校生に向けて、「第2章：真理値から確率へ —— 必然の論理から不確実性の論理へ」の導入講義を書いてください。
論理では「1か0か（真か偽か）」の白黒だった世界が、確率論では「0から1の間の実数値」というグラデーションになること。
指示変数（Indicator Variable）を使うと、事象の生起期待値がそのまま確率 P(A) になるというブールの洞察を、サイコロや天気の例を用いて詳しく（600字程度）解説してください。""",

    "ch2_column": """高校生向け探究コラムとして、「ブールの展開定理（Expansion Theorem）：あらゆる論理式を直交する基本構成要素に分解する数学の魔術」について、高校生にもわかるように詳しく（400字程度）解説してください。""",

    "ch3_intro": """高校生に向けて、「第3章：ブールの一般解法 —— 確率問題を代数方程式で解く」の講義を書いてください。
ラプラスや従来の確率論が個別の問題ごとに頭をひねって解いていたのに対し、ブールは『すべての確率問題は連立方程式を機械的に解くだけで答えが出る』という普遍的な代数的解法を打ち立てました。
このアイデアがどれほど革命的だったかを、具体的に連立方程式を解くイメージを交えて詳しく（600字程度）語ってください。""",

    "ch3_column": """高校生向け探究コラムとして、「完全な情報がない世界で生きる：未知の確率を代数的に消去（Elimination）する技術」について詳しく（400字程度）書いてください。""",

    "ch4_intro": """高校生に向けて、「第4章：統計的条件と不等式 —— ブールの不等式（Bonferroniの不等式）」の講義を書いてください。
情報が足りなくて正確な確率値が1つに決まらないときでも、『少なくともこの範囲（上限と下限）には収まる』と数学的に保証するブールの不等式 P(A∪B) <= P(A) + P(B) の絶大な威力。
これが現代のビッグデータ解析や統計学の多重比較補正（ボンフェローニ補正）で必須の技術になっている理由を詳しく（600字程度）教えてください。""",

    "ch4_column": """高校生向け探究コラムとして、「多重検定の落とし穴：サイコロを20回振れば1回は『偶然の奇跡』が起きる？ ボンフェローニ補正の知恵」について詳しく（400字程度）解説してください。""",

    "ch5_intro": """高校生に向けて、「第5章：原因と結果の結合 —— ベイズ逆確率の代数的拡張」の講義を書いてください。
ラプラスのベイズの定理を、ブールは複数の証言や条件が複雑に絡み合った状況へと代数的に拡張しました。
法廷で『2人の証言者がそれぞれ矛盾したことを言っているとき、被告人が有罪である真の確率はいくらか？』という難問をブールがどう定式化したかを、高校生向けに詳しく（600字程度）解説してください。""",

    "ch5_column": """高校生向け探究コラムとして、「法廷の確率論：コリンズ事件（1968年）に見る確率計算の誤用と冤罪の危機」について詳しく（400字程度）解説してください。""",

    "ch6_intro": """高校生に向けて、「第6章：論理回路から現代AIへ —— ブール代数が生んだ情報社会」の講義を書いてください。
ブール代数は単なる机上の数学ではなく、現代のコンピュータのCPU、半導体チップ、そしてニューラルネットワーク（AI）の根底を支えています。
0と1の論理ゲートがどのように確率的な推論マシン（確率的AI・生成AI）へと進化していったのか、その壮大な歴史の架け橋を熱く詳しく（600字程度）語ってください。""",

    "ch6_column": """高校生向け探究コラムとして、「量子コンピュータとブール代数の彼方：0と1の重ね合わせが拓く新世界」について詳しく（400字程度）解説してください。""",

    "ch7_intro": """高校生に向けて、「第7章：ラプラス・ヴェン・ブール —— 確率論を築いた3大巨人の対話」の講義を書いてください。
第1弾ラプラス（主観的信念と原因の確率）、第2弾ヴェン（客観的データと無限系列の頻度）、そして第3弾ブール（論理代数と確率方程式の統一）。
この3者の確率観を比較対照し、高校数学の「場合の数・確率・統計的な推測」がどのように美しく1つの全体像に統合されるかを、感動的に詳しく（600字程度）総括してください。""",

    "ch7_column": """高校生向け探究コラムとして、「数学は発見か、それとも人間の発明か？：『思考の法則』が問いかける究極の哲学」について詳しく（400字程度）解説してください。""",

    "afterword": """高校生に向けて、本書のあとがきを書いてください。
論理の厳密さと、不確実性に立ち向かう確率の柔軟性。この2つを兼ね備えた思考力を手に入れた高校生が、これからのAI時代・情報社会を堂々と歩んでいくための力強いエールを、教育情報分析研究会として情熱的に（500字程度）届けてください。"""
}

def run():
    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except Exception:
            cache = {}

    print(f"Starting Boole text generation on Ollama ({MODEL_NAME}). Already cached: {len(cache)}/{len(PROMPTS)}", flush=True)

    for i, (key, prompt) in enumerate(PROMPTS.items(), 1):
        if key in cache and len(cache[key]) > 200:
            print(f"[{i}/{len(PROMPTS)}] {key} is already cached ({len(cache[key])} chars).", flush=True)
            continue

        print(f"[{i}/{len(PROMPTS)}] Generating {key} via Ollama...", flush=True)
        start_t = time.time()
        reply = query_ollama_stream(prompt, system_prompt=SYSTEM_TEACHER)
        elapsed = time.time() - start_t

        if reply:
            cache[key] = reply
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)
            print(f"  -> Generated {key} in {elapsed:.2f}s ({len(reply)} chars)", flush=True)
        else:
            print(f"  -> FAILED {key}", flush=True)

    print("All Boole sections generated successfully!", flush=True)

if __name__ == '__main__':
    run()
