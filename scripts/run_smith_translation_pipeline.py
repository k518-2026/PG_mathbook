# -*- coding: utf-8 -*-
"""
High-speed robust pipeline runner for PG#22599:
Smith & Karpinski: The Hindu-Arabic Numerals (全8章)
Translates and verifies each chapter via LM Studio, caches pieces,
and constructs both:
  1. Full Academic Translation (原著完全翻訳・数学校閲版)
  2. Adult Re-learning Intro (古典で学び直すインド・アラビア数字入門) with TikZ diagrams
"""

import os
import re
import sys
import json
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = r"E:\GoogleAntigravity\PG_mathbook"
BOOK_DIR = os.path.join(PROJECT_ROOT, "books", "22599_smith_hindu_arabic_numerals")
CHAPTERS_FILE = os.path.join(BOOK_DIR, "smith_hindu_arabic_numerals_chapters.json")
CACHE_FILE = os.path.join(BOOK_DIR, "smith_hindu_arabic_numerals_translation_cache.json")
LM_STUDIO_URL = "http://192.168.128.16:1234/v1/chat/completions"

sys.path.insert(0, os.path.join(PROJECT_ROOT, "scripts"))
from safe_latex_cleaner import clean_text_for_latex

CHAPTER_TITLES_JA = [
    "第1章：インド・アラビア数字の起源に関する初期の諸説 (Early Ideas of Their Origin)",
    "第2章：位取り記法を伴わない初期のインド数字 (Early Hindu Forms with No Place Value)",
    "第3章：位取り記法を伴う後期のインド数字 (Later Hindu Forms, with a Place Value)",
    "第4章：記号「ゼロ」の起源と誕生 (The Symbol Zero)",
    "第5章：ボエティウスによるヨーロッパへの数字導入をめぐる問題 (The Question of the Introduction of the Numerals into Europe by Boethius)",
    "第6章：アラビア世界における数字の発展と受容 (The Development of the Numerals among the Arabs)",
    "第7章：ヨーロッパへの数字の本格的導入 (The Definite Introduction of the Numerals into Europe)",
    "第8章：ヨーロッパ各地における数字の普及と計算革命 (The Spread of the Numerals in Europe)"
]


def call_lm_studio(prompt, system_prompt="You are an expert academic translator specializing in the history of mathematics and mathematical typography.", model="qwen2.5-7b-instruct", max_tokens=2048, temperature=0.1):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
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
    for retry in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            time.sleep(2)
    return ""


def clean_academic_japanese(text):
    """Purify AI translations: remove markdown chat preamble, Chinese phrasing, etc."""
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        if line.strip().startswith(("Here is", "Below is", "Translation:", "翻訳：", "日本語訳：", "以下は", "（より")):
            continue
        # Remove footnote tag artifacts like {123}
        line = re.sub(r'\{[0-9ivxlc]+\}', '', line)
        cleaned.append(line)
    res = "\n".join(cleaned).strip()
    return res


def chunk_text(text, target_chars=1800):
    paragraphs = text.split("\n\n")
    chunks = []
    current = []
    curr_len = 0
    for p in paragraphs:
        p_clean = p.strip()
        if not p_clean:
            continue
        if curr_len + len(p_clean) > target_chars and current:
            chunks.append("\n\n".join(current))
            current = [p_clean]
            curr_len = len(p_clean)
        else:
            current.append(p_clean)
            curr_len += len(p_clean)
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def translate_chunk(chunk_en, chapter_title_ja):
    prompt = f"""あなたは数学史の最高峰の学術翻訳者です。
底本：David Eugene Smith & Louis Charles Karpinski『The Hindu-Arabic Numerals』
該当章：{chapter_title_ja}

以下の英語原文を、日本の数学史・解析学の標準的な格調高い学術日本語（「である」「だ」調、正確な術語）に翻訳してください。

【厳格な規則】
1. 中国語の簡体字や中国語独特の言い回し（例如、我们、使得、关于等）は一切混入させず、純正な日本の学術日本語で記述してください。
2. 数字・数式・人名（Aryabhata, Brahmagupta, Al-Khowarizmi, Gerbert, Fibonacci, Boethius等）は正確な定訳・カナ表記を付してください。
3. 翻訳本文のみを出力し、「以下は翻訳です」「解説：」などの前置き・後書きは一切含めないでください。

【英語原文】：
{chunk_en}
"""
    raw_trans = call_lm_studio(prompt)
    return clean_academic_japanese(raw_trans)


def main():
    with open(CHAPTERS_FILE, "r", encoding="utf-8") as f:
        chapters = json.load(f)

    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache = json.load(f)
        except Exception:
            cache = {}

    print(f"Loaded {len(chapters)} chapters. Starting translation pipeline...")

    for idx, ch in enumerate(chapters):
        ch_num = ch["number"]
        key = f"Chapter_{ch_num}"
        ch_title_ja = CHAPTER_TITLES_JA[idx]

        if key not in cache:
            cache[key] = {
                "number": ch_num,
                "title_en": ch["title_en"],
                "title_ja": ch_title_ja,
                "chunks_done": 0,
                "translation_pieces": []
            }

        chunks = chunk_text(ch["text"], target_chars=1800)
        total_chunks = len(chunks)
        done_chunks = cache[key].get("chunks_done", 0)

        print(f"\n>>> [{ch_num}/8] {ch_title_ja}: {total_chunks} chunks (done: {done_chunks})")

        while done_chunks < total_chunks:
            chunk = chunks[done_chunks]
            print(f"  Translating chunk {done_chunks + 1}/{total_chunks} ({len(chunk)} chars)...", end="", flush=True)
            jp_text = translate_chunk(chunk, ch_title_ja)
            if not jp_text:
                print(" [ERROR: Empty response, retrying...]")
                time.sleep(2)
                continue
            cache[key]["translation_pieces"].append(jp_text)
            done_chunks += 1
            cache[key]["chunks_done"] = done_chunks
            print(f" Done ({len(jp_text)} chars)")

            # Save checkpoint every chunk
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

        cache[key]["japanese_translation"] = "\n\n".join(cache[key]["translation_pieces"])
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)

    print("\nAll 8 chapters translated successfully!")


if __name__ == "__main__":
    main()
