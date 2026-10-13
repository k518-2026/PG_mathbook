# -*- coding: utf-8 -*-
import os
import sys
import json
import time
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

CACHE_DIR = 'ollama_cache_thompson_calculus'
os.makedirs(CACHE_DIR, exist_ok=True)

OLLAMA_URL = "http://192.168.128.62:11434/api/chat"
MODEL_NAME = "gemma4:12b"

def query_ollama(prompt, system_prompt=None, max_tokens=600, retries=3):
    headers = {"Content-Type": "application/json"}
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "think": False,
        "options": {
            "temperature": 0.7,
            "num_predict": max_tokens
        }
    }

    for attempt in range(retries):
        try:
            t0 = time.time()
            req = urllib.request.Request(OLLAMA_URL, data=json.dumps(payload).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=90) as res:
                data = json.loads(res.read().decode('utf-8'))
                elapsed = time.time() - t0
                content = data.get('message', {}).get('content', '').strip()
                print(f"  [Ollama Response] {len(content)} chars in {elapsed:.1f}s", flush=True)
                return content
        except Exception as e:
            print(f"  [Ollama Attempt {attempt+1} Error]: {e}", flush=True)
            time.sleep(3)
    return ""

SYSTEM_PROMPT = """あなたは「教育情報分析研究会」の専任数学講師です。
高校生（数学II・数学III、物理基礎）に向けて、シルバヌス・P・トンプソンの歴史的名著『Calculus Made Easy（誰にもわかる微積分）』(1910年) の数学的本質を、
退屈な形式主義を排し、極めて分かりやすく熱意を込めて解説してください。
嘘や想像を排し、原著のテキストと数学的本質に完全に忠実に記述してください。"""

CHAPTER_PROMPTS = [
    (1, "予備的恐怖からの解放：微小量 dx と dy の正体と微積分の扉",
     """高校生に向けて、シルバヌス・P・トンプソン『Calculus Made Easy』第1章の思想（What one fool can do, another can）と、微小量 dx, dy、そして記号 d と ∫ の直観的正体について、熱意あふれる講義を500字程度で語ってください。"""),
    
    (2, "小ささの階級と無視の数理：1次微小量・2次微小量と近似の本質",
     """高校生に向けて、『Calculus Made Easy』第2章の「小ささの階級（Degrees of Smallness）」について語ってください。大富豪が落とした1ファージングの貨幣のたとえや、正方形の面積拡大 (x+dx)^2 = x^2 + 2x dx + (dx)^2 においてなぜ 2次微小量 (dx)^2 を極限で安全に無視できるのかを500字程度で明快に解説してください。"""),
    
    (3, "相対的な成長度：変化率としての導関数 dy/dx と曲線の傾き",
     """高校生に向けて、『Calculus Made Easy』第3章の「相対的な成長度（Relative Growings）」について語ってください。ロンドンの時計の針（長針と短針の速度比 12:1）のたとえや、グラフの割線から接線の傾き dy/dx への移行の意味を500字程度で解説してください。"""),
    
    (4, "ベキ関数の微分法：y = x^n の微分公式と直観的証明",
     """高校生に向けて、『Calculus Made Easy』第4章のベキ関数の微分公式 d/dx(x^n) = n x^(n-1) について語ってください。x^2 や x^3 の微小増分の展開から二項定理、そして負の指数 (1/x) や分数指数 (√x) への自然な拡張の美しさを500字程度で解説してください。"""),
    
    (5, "関数の結合と演算規則：和・差・積・商の微分公式のメカニズム",
     """高校生に向けて、『Calculus Made Easy』第5章の積の微分公式 (uv)' = u'v + uv' と商の微分公式について語ってください。長方形の縦と横を微小に伸ばしたときの面積モデルや、なぜ商の微分では分子にマイナス符号が現れるのかを500字程度で直観的に解説してください。"""),
    
    (6, "合成関数と連鎖律：「便利な裏技」チェイン・ルールの威力",
     """高校生に向けて、『Calculus Made Easy』第6章の「便利な裏技」である合成関数の連鎖律（チェイン・ルール）dy/dx = (dy/du) * (du/dx) について語ってください。中間変数 u を用いて複雑な関数の皮を一枚ずつ剥くように微分できる爽快感を500字程度で解説してください。"""),
    
    (7, "高階微分と運動の物理：第2次導関数 d^2y/dx^2、速度・加速度の数理",
     """高校生に向けて、『Calculus Made Easy』第7章の第2次導関数 d^2y/dx^2 と物理学における運動について語ってください。なぜ d に2がつき x に2がつくのかという記号の意味、位置・速度・加速度の関係、ガリレオの自由落下の数理を500字程度で解説してください。"""),
    
    (8, "極大・極小と最適化：導関数がゼロになる点と現実世界の最大化・最小化",
     """高校生に向けて、『Calculus Made Easy』第8章の極大・極小（最適化）について語ってください。山の頂上で足元が平ら（dy/dx = 0）になるフェルマーの原理、第2次導関数による山と谷の判定、そしてブリキ板の四隅を切り取って作る箱の容積最大化問題を500字程度で解説してください。"""),
    
    (9, "自然の成長と指数・対数：ネイピア数 e、真の複利法則と自然対数の微分",
     """高校生に向けて、『Calculus Made Easy』第9章の「真の複利法則」とネイピア数 e = 2.71828... について語ってください。連続複利の極限、微分しても形が変わらない唯一無二の関数 e^x の驚異、そして自然対数 ln x の微分が 1/x になる美しさを500字程度で解説してください。"""),
    
    (10, "振動と三角関数の微分：波と円運動を描く sin x と cos x の導関数",
     """高校生に向けて、『Calculus Made Easy』第10章の三角関数の微分について語ってください。なぜ度数法ではなく弧度法（ラジアン）を使うのか、単位円の幾何学による (sin x)' = cos x の導出、2回微分すると元の関数にマイナスがつく単振動の方程式を500字程度で解説してください。"""),
    
    (11, "微分の逆演算としての積分：不定積分の基礎と原始関数の探求",
     """高校生に向けて、『Calculus Made Easy』第11章の不定積分について語ってください。時計の針を巻き戻すように導関数から元の関数を探す推理の旅、長いS記号 ∫ の正体、そして消えた手がかりとしての積分定数 C の意味を500字程度で解説してください。"""),
    
    (12, "面積の求積と微積分学の基本定理：区分求積法から現代科学・AIへの架け橋",
     """高校生に向けて、『Calculus Made Easy』第12章の微積分学の基本定理と面積の求積について語ってください。アルキメデスの取り尽くし法から微小短冊の足し合わせ、面積の増加率が高さ f(x) に等しいという大発見、そして現代のAI（深層学習の勾配降下法）への繋がりを500字程度で力強く語ってください。""")
]

def main():
    print(f"=== Generating Ollama Lectures for all 12 Chapters ({OLLAMA_URL}, model: {MODEL_NAME}) ===")
    results = {}
    for num, title, prompt in CHAPTER_PROMPTS:
        print(f"[{num}/12] Generating: {title} ...", flush=True)
        text = query_ollama(prompt, system_prompt=SYSTEM_PROMPT, max_tokens=600)
        results[num] = text
        time.sleep(1)
    
    out_json = os.path.join(CACHE_DIR, 'ollama_lectures.json')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"=== Successfully saved all 12 Ollama lectures to {out_json} ===")

if __name__ == '__main__':
    main()
