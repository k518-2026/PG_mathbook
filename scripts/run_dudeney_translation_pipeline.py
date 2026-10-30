# -*- coding: utf-8 -*-
"""
Full Translation Pipeline for PG#16713 (Resilient & Cleaned)
"""

import os
import sys
import json
import time
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

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
                    "英語のパズル問題文および解答解説を、自然で親しみやすく格調高い日本語に翻訳してください。\n"
                    "重要規則:\n"
                    "1. 簡体字や不自然な中国語漢字は一切使わず、標準的な日本語の漢字・仮名・句読点のみを用いてください。\n"
                    "2. 出力は必ず指定されたJSONフォーマットのみを出力してください。"
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
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            time.sleep(2 + attempt * 2)
    return ""

def clean_json_response(raw_text):
    text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        text = match.group(1)
    else:
        m2 = re.search(r"(\{.*\})", text, re.DOTALL)
        if m2:
            text = m2.group(1)
    try:
        return json.loads(text)
    except Exception:
        return None

def translate_single_problem(item):
    p_num = item["number"]
    p_title = item.get("title", "")
    p_text = item.get("problem", "")[:2000] # safety truncate to prevent model context blowup
    s_text = item.get("solution", "")[:2000]

    prompt = (
        f"以下のデュードニーの数学パズル（第{p_num}問「{p_title}」）の問題文と解答を日本語に翻訳してください。\n\n"
        f"【原題】: {p_title}\n"
        f"【問題文】:\n{p_text}\n\n"
        f"【解答・解説文】:\n{s_text}\n\n"
        "以下のJSON形式で出力してください:\n"
        "{\n"
        f'  "number": {p_num},\n'
        '  "title_ja": "日本語のタイトル",\n'
        '  "problem_ja": "問題文の日本語訳",\n'
        '  "solution_ja": "解答・解説文の日本語訳"\n'
        "}"
    )

    raw = call_llm(prompt, max_tokens=1400)
    parsed = clean_json_response(raw)

    if parsed and "problem_ja" in parsed and "solution_ja" in parsed:
        return {
            "number": p_num,
            "title_ja": parsed.get("title_ja", p_title),
            "problem_ja": parsed["problem_ja"],
            "solution_ja": parsed["solution_ja"],
            "original_title": p_title
        }
    else:
        # Fallback if json parse fails: do problem and solution separately
        fallback_prompt_prob = f"次の英語の数学パズル問題文を自然で格調高い日本語に翻訳してください:\n\n{p_text}"
        prob_ja = call_llm(fallback_prompt_prob, max_tokens=900)
        fallback_prompt_sol = f"次の数学パズルの解答・解説を自然で格調高い日本語に翻訳してください:\n\n{s_text}"
        sol_ja = call_llm(fallback_prompt_sol, max_tokens=900)
        return {
            "number": p_num,
            "title_ja": p_title,
            "problem_ja": prob_ja or p_text,
            "solution_ja": sol_ja or s_text,
            "original_title": p_title
        }

def main():
    with open(PAIRED_FILE, "r", encoding="utf-8") as f:
        problems = json.load(f)

    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache = json.load(f)
            print(f"Loaded {len(cache)} cached items.")
        except Exception:
            cache = {}

    to_process = [p for p in problems if str(p["number"]) not in cache]
    print(f"Total problems: {len(problems)}, remaining: {len(to_process)}")

    if not to_process:
        print("All problems already translated!")
        return

    max_workers = 2
    count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_num = {executor.submit(translate_single_problem, item): item["number"] for item in to_process}
        for future in as_completed(future_to_num):
            num = future_to_num[future]
            try:
                res = future.result()
                cache[str(num)] = res
                count += 1
                if count % 5 == 0 or count == len(to_process):
                    with open(CACHE_FILE, "w", encoding="utf-8") as f:
                        json.dump(cache, f, ensure_ascii=False, indent=2)
                    print(f"[{count}/{len(to_process)}] Completed problem #{num}. Total cached: {len(cache)}")
            except Exception as e:
                print(f"Error on problem #{num}: {e}")

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print("Translation pipeline finished.")

if __name__ == "__main__":
    main()
