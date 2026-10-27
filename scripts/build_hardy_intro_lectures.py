import sys, os, json, time
sys.path.insert(0, 'E:/GoogleAntigravity/PG_mathbook/scripts')
from pipeline_utils import call_lm_studio

cache_path = 'E:/GoogleAntigravity/PG_mathbook/books/38769_hardy_pure_mathematics/hardy_pure_mathematics_intro_cache.json'
with open('E:/GoogleAntigravity/PG_mathbook/books/38769_hardy_pure_mathematics/hardy_pure_mathematics_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

intro_cache = {}
if os.path.exists(cache_path):
    with open(cache_path, 'r', encoding='utf-8') as f:
        intro_cache = json.load(f)

with open('E:/GoogleAntigravity/PG_mathbook/books/38769_hardy_pure_mathematics/hardy_pure_mathematics_translation_cache.json', 'r', encoding='utf-8') as f:
    trans_cache = json.load(f)

sys_prompt = (
    "あなたは『古典数学学び直し講座』の専任ナビゲーターです。\n"
    "読者対象は、50代から80代の大人です。「学生時代に数学でつまずいてしまったが、もう一度学びたい」「大人になって知的好奇心から数学の本質を味わいたい」という方々です。\n"
    "以下の執筆方針に厳密に従って、充実した講義原稿を作成してください：\n\n"
    "【執筆方針】\n"
    "1. 前提知識は中学校・高校数学（方程式、関数のグラフ、三角比、極限の基礎、微積分の直観的イメージ）に限定し、大学レベルの専門用語は使わずに平易に解説する。\n"
    "2. 難しい概念や数式は、一足飛びに結論にいかず一段階ずつ丁寧に論理を追う。なぜその計算や式変形が成り立つのかを読者が納得できるようにする。\n"
    "3. 歴史的背景（なぜ当時の数学者たちがその問題に挑んだのか）や、現代社会・科学とのつながりも交え、知的好奇心を刺激する。\n"
    "4. 語り口は知性的で温かみがあり、読者を励ます丁寧な敬体（です・ます調）とする。\n"
    "5. 数式はLaTeX形式（$...$, $$...$$）で適切に記載し、文章は自然な日本語のみで記述する。"
)

for idx, ch in enumerate(chapters[:10], start=1):
    key = f'Intro_{idx}'
    if key in intro_cache and intro_cache[key].get('lecture'):
        print(f'{key} already done.')
        continue
    ch_num = ch['number']
    ch_key = f'Chapter_{ch_num}'
    ja_source = trans_cache.get(ch_key, {}).get('japanese_translation', ch['text'][:2000])
    print(f'Generating {key}: {ch["title"]}...')
    
    prompt = (
        f"【本章のテーマ】：{ch['title']}\n\n"
        f"以下の原著日本語訳（校閲済み）の内容をもとに、大人の読者が中学・高校の数学の知識で根本からスッキリ理解できるよう、"
        f"一段階ずつ丁寧で直観的な「学び直し講義」を作成してください：\n\n"
        f"{ja_source[:1200]}"
    )
    
    lecture = call_lm_studio(prompt, system_prompt=sys_prompt, model="qwen2.5-7b-instruct", max_tokens=1800, temperature=0.2)
    intro_cache[key] = {
        'number': idx,
        'title': ch['title'],
        'lecture': lecture
    }
    with open(cache_path, 'w', encoding='utf-8') as f:
        json.dump(intro_cache, f, ensure_ascii=False, indent=2)
    print(f'Saved {key} (length: {len(lecture)})')
    time.sleep(3)

print('All 10 intro lectures generated successfully!')
