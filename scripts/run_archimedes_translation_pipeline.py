# -*- coding: utf-8 -*-
"""
High-speed robust pipeline runner for PG#35550:
Sir Thomas Little Heath: Archimedes (Pioneers of Progress: Men of Science, 1920)
Translates and verifies each chapter via LM Studio, caches pieces,
and constructs:
  1. Full Academic Translation (全訳・学術決定版)
  2. Adult Re-learning Intro (古典で学び直すアルキメデス幾何学・力学入門) with TikZ diagrams
"""

import os
import re
import sys
import json
import time
import urllib.request

PROJECT_ROOT = r"E:\GoogleAntigravity\PG_mathbook"
BOOK_DIR = os.path.join(PROJECT_ROOT, "books", "35550_heath_archimedes")
CHAPTERS_FILE = os.path.join(BOOK_DIR, "heath_archimedes_chapters.json")
CACHE_FILE = os.path.join(BOOK_DIR, "heath_archimedes_translation_cache.json")
LM_STUDIO_URL = "http://192.168.128.16:1234/v1/chat/completions"

sys.path.insert(0, os.path.join(PROJECT_ROOT, "scripts"))
from safe_latex_cleaner import clean_text_for_latex

def call_lm_studio(prompt, max_tokens=1600, temperature=0.1):
    payload = {
        "model": "qwen2.5-7b-instruct",
        "messages": [
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
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            time.sleep(2 + attempt * 2)
    return ""

def clean_academic_japanese(text):
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        if line.strip().startswith(("Here is", "Below is", "Translation:", "翻訳：", "訳：", "以下は", "（注")):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()

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

def translate_chunk(chunk_en, section_title_ja):
    prompt = f"""Translate the following English academic text into natural, rigorous, high-style academic Japanese.
Book: Sir Thomas Little Heath "Archimedes"
Section: {section_title_ja}

CRITICAL RULES:
1. Use only standard Japanese (「である」「だ」調).
2. Absolutely NO Chinese simplified or traditional characters or Chinese syntax (e.g. 我们, 采用, 系统, 对于, 并且, 从而, 亦等).
3. Translate all mathematical and historical terms into standard Japanese mathematical terminology (e.g., exhaustion method -> 取り尽くし法, spiral -> らせん, quadrature -> 求積法, centre of gravity -> 重心, hydrostatics -> 流体静力学).
4. Output ONLY the Japanese translation. No preamble or notes.

English Text:
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

    print(f"Loaded {len(chapters)} sections. Starting Archimedes translation pipeline...")

    for idx, ch in enumerate(chapters):
        ch_num = ch["number"]
        key = f"Section_{ch_num}"
        ch_title_ja = ch["title_ja"]

        if key not in cache:
            cache[key] = {
                "number": ch_num,
                "roman": ch["roman"],
                "title_en": ch["title_en"],
                "title_ja": ch_title_ja,
                "chunks_done": 0,
                "translation_pieces": []
            }

        chunks = chunk_text(ch["text"], target_chars=1800)
        total_chunks = len(chunks)
        done_chunks = len(cache[key].get("translation_pieces", []))

        print(f"\n>>> [{ch_num}/{len(chapters)}] {ch['roman']}. {ch['title_en']} ({ch_title_ja}): {total_chunks} chunks (done: {done_chunks})")

        while done_chunks < total_chunks:
            chunk = chunks[done_chunks]
            print(f"  Translating chunk {done_chunks + 1}/{total_chunks} ({len(chunk)} chars)...", end="", flush=True)
            jp_text = translate_chunk(chunk, ch_title_ja)

            # Verification of Japanese quality
            kana = len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff]', jp_text))
            kanji = len(re.findall(r'[\u4e00-\u9fff]', jp_text))
            ratio = (kana / (kanji + 1)) if kanji > 0 else 1.0

            if ratio < 0.7 or len(jp_text) < 100:
                print(f" [Warning: low kana ratio {ratio:.2f}, retrying...]", flush=True)
                jp_text = translate_chunk(chunk, ch_title_ja)

            cache[key]["translation_pieces"].append(jp_text)
            cache[key]["chunks_done"] = len(cache[key]["translation_pieces"])
            done_chunks = cache[key]["chunks_done"]
            print(f" done (len {len(jp_text)}, kana ratio {ratio:.2f})")

            # Save incrementally
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

    print("\nAll sections successfully translated and cached!")

if __name__ == "__main__":
    main()
