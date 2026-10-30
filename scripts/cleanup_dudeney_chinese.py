# -*- coding: utf-8 -*-
"""
Fix Chinese artifacts and re-translate flagged problems using strict Japanese prompts.
"""

import os
import sys
import json
import time
import re
import urllib.request

PROJECT_ROOT = r"E:\GoogleAntigravity\PG_mathbook"
BOOK_DIR = os.path.join(PROJECT_ROOT, "books", "16713_dudeney_amusements_in_mathematics")
PAIRED_FILE = os.path.join(BOOK_DIR, "dudeney_paired_problems.json")
CACHE_FILE = os.path.join(BOOK_DIR, "dudeney_full_japanese_cache.json")
LM_STUDIO_URL = "http://192.168.128.16:1234/v1/chat/completions"

SIMPLIFIED_CHARS = [
    '为', '这', '们', '并', '样', '说', '对', '会', '发', '经',
    '买', '卖', '从', '么', '动', '见', '问', '书', '长', '门', '关', '开',
    '给', '进', '还', '过', '带', '没', '两', '将', '总',
    '便士', '先令', '香蕉'
]

def call_llm(prompt, max_tokens=1000, temperature=0.1):
    payload = {
        "model": "qwen2.5-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "あなたは優秀な日本の数学者・翻訳家です。"
                    "英語または中国語混じりの文章を、完全な美しい日本語（標準的な現代日本語）に翻訳・修正してください。\n"
                    "重要規則:\n"
                    "1. 中国語（簡体字や中国語独特の単語：便士→ペンス、先令→シリング、香蕉→バナナ、这、为、们等）は絶対に排除し、標準日本語のみにしてください。\n"
                    "2. 翻訳文のみを出力してください。"
                )
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    req = urllib.request.Request(
        LM_STUDIO_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            time.sleep(1 + attempt)
    return ""

def main():
    with open(PAIRED_FILE, "r", encoding="utf-8") as f:
        problems = json.load(f)
    prob_map = {p["number"]: p for p in problems}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    flagged_keys = []
    for k, v in cache.items():
        text = v.get("problem_ja", "") + " " + v.get("solution_ja", "")
        if any(c in text for c in SIMPLIFIED_CHARS):
            flagged_keys.append(int(k))

    flagged_keys.sort()
    print(f"Total problems needing Japanese cleanup: {len(flagged_keys)}")

    for idx, num in enumerate(flagged_keys, 1):
        orig_item = prob_map.get(num, {})
        title = orig_item.get("title", f"Problem {num}")
        orig_p = orig_item.get("problem", "")[:1200]
        orig_s = orig_item.get("solution", "")[:1200]

        print(f"[{idx}/{len(flagged_keys)}] Cleaning #{num}: {title}...")

        prompt_p = (
            f"次の英語のパズル問題（第{num}問『{title}』）を、中国語を一切含めず完全な美しい現代日本語に翻訳してください:\n\n"
            f"{orig_p}"
        )
        p_ja = call_llm(prompt_p, max_tokens=600)

        prompt_s = (
            f"次の英語のパズル解答（第{num}問『{title}』）を、中国語を一切含めず完全な美しい現代日本語に翻訳してください:\n\n"
            f"{orig_s}"
        )
        s_ja = call_llm(prompt_s, max_tokens=600)

        prompt_t = f"次のパズルタイトルの日本語訳（タイトルのみ）: {title}"
        t_ja = call_llm(prompt_t, max_tokens=30)
        t_ja = re.sub(r'["\'「」]', '', t_ja).strip()

        cache[str(num)]["title_ja"] = t_ja or cache[str(num)].get("title_ja", title)
        if p_ja:
            cache[str(num)]["problem_ja"] = p_ja
        if s_ja:
            cache[str(num)]["solution_ja"] = s_ja

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)

    print("Cleanup completed!")

if __name__ == "__main__":
    main()
