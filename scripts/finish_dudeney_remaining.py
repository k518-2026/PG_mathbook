# -*- coding: utf-8 -*-
"""
Sequential Robust Finisher for remaining problems of PG#16713
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

def call_llm(prompt, max_tokens=1000, temperature=0.1):
    payload = {
        "model": "qwen2.5-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "あなたは数学パズルおよび古典数学の専門翻訳者です。"
                    "英語のパズル問題文および解答解説を、自然で格調高い日本語に翻訳してください。\n"
                    "重要規則: 簡体字は一切使わず標準日本語のみを使用してください。"
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
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            time.sleep(2 + attempt * 2)
    return ""

def main():
    with open(PAIRED_FILE, "r", encoding="utf-8") as f:
        problems = json.load(f)

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    to_process = [p for p in problems if str(p["number"]) not in cache]
    print(f"Remaining: {len(to_process)}")

    for idx, p in enumerate(to_process, 1):
        num = p["number"]
        title = p.get("title", "")
        prob_text = p.get("problem", "")[:1200]
        sol_text = p.get("solution", "")[:1200]

        print(f"[{idx}/{len(to_process)}] Translating #{num} {title}...")

        prompt_prob = f"次の数学パズル問題（第{num}問『{title}』）を格調高い日本語に翻訳してください:\n\n{prob_text}"
        prob_ja = call_llm(prompt_prob, max_tokens=600)
        time.sleep(0.5)

        prompt_sol = f"次の数学パズル解答・解説（第{num}問『{title}』）を格調高い日本語に翻訳してください:\n\n{sol_text}"
        sol_ja = call_llm(prompt_sol, max_tokens=700)
        time.sleep(0.5)

        prompt_title = f"次の英語のパズルタイトルを自然な日本語に訳してください（タイトルのみ出力）: {title}"
        title_ja = call_llm(prompt_title, max_tokens=40)
        title_ja = re.sub(r'["\'「」]', '', title_ja).strip()

        cache[str(num)] = {
            "number": num,
            "title_ja": title_ja or title,
            "problem_ja": prob_ja or prob_text,
            "solution_ja": sol_ja or sol_text,
            "original_title": title
        }

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
        print(f"Saved #{num}. Total cached: {len(cache)}")

    print("All problems finished!")

if __name__ == "__main__":
    main()
