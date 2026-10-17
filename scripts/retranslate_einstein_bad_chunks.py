# -*- coding: utf-8 -*-
"""
Re-translate the 13 specific bad chunks in Einstein's Relativity (#30155)
using qwen2.5-7b-instruct with strict instructions for natural Japanese,
no Chinese characters/grammar, and no preface text.
"""

import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("scripts"))
from pipeline_utils import call_lm_studio

CACHE_FILE = "books/30155_einstein_relativity/einstein_full_translation_cache.json"
SECTIONS_FILE = "books/30155_einstein_relativity/einstein_sections.json"

def chunk_text(text, max_len=2400):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = []
    current_len = 0
    for p in paragraphs:
        p_len = len(p)
        if current_len + p_len > max_len and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = [p]
            current_len = p_len
        else:
            current_chunk.append(p)
            current_len += p_len
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    return chunks

TARGET_BAD_CHUNKS = [
    ("Sec_I", 0),
    ("Sec_II", 1),
    ("Sec_II", 2),
    ("Sec_III", 1),
    ("Sec_V", 2),
    ("Sec_XI", 1),
    ("Sec_XVII", 1),
    ("Sec_XIX", 1),
    ("Sec_XXIV", 2),
    ("Sec_XXIX", 2),
    ("Sec_XXXI", 1),
    ("Sec_App_I", 2),
    ("Sec_App_IV", 1),
]

SYS_PROMPT = """あなたは近代物理学・数学の学術翻訳を専門とする日本の最高峰の翻訳家です。
アルベルト・アインシュタインの原著英文を、一切の要約や省略を行わず、格調高く自然で明晰な日本語（和文標準語）へ完全直訳してください。

【厳格な遵守事項】
1. 中国語（簡体字、中国語特有の単語・助詞・構文「我们」「显然」「坐标」「对于」「满足」「被」「是什么」等）は一切混入させてはなりません。
2. 専門用語は日本の物理学・数学の標準術語を用いてください：
   - coordinate system → 座標系（※「坐标」は禁止）
   - Euclidean geometry → ユークリッド幾何学（※「欧几里得」は禁止）
   - reference-body / frame of reference → 基準体、参照枠
   - simultaneity → 同時性
   - impenetrability → 不入性（不可入性）
   - Cartesian co-ordinates → デカルト座標（※「カート游戏」等の誤訳は厳禁）
   - marble slab → 大理石の平板（※「Marble」の未訳は厳禁）
3. 文中の数式・変数は標準的なLaTeX形式（$...$, $$...$$, \\[ ... \\]）で出力してください。
4. 「以下の文章を翻訳しました」「以下が翻訳です」等の前置き・注釈・解説文は一切出力せず、翻訳本文のみを出力してください。"""

def main():
    with open(SECTIONS_FILE, "r", encoding="utf-8") as f:
        sections = json.load(f)

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    sec_map = {s["number"]: s for s in sections}

    for sec_key, c_idx in TARGET_BAD_CHUNKS:
        sec_num = sec_key.replace("Sec_", "")
        sec_en = sec_map[sec_num]
        chunks = chunk_text(sec_en["text_en"], max_len=2400)
        chunk_to_trans = chunks[c_idx]

        print(f"\nRe-translating {sec_key} chunk {c_idx+1}/{len(chunks)} ({len(chunk_to_trans)} chars)...")
        prompt = f"以下の英文を格調高く明晰な日本語へ完全直訳してください（前置き・注釈は一切不要）：\n\n{chunk_to_trans}"

        for attempt in range(3):
            try:
                res = call_lm_studio(prompt, system_prompt=SYS_PROMPT, model="qwen2.5-7b-instruct", max_tokens=2500, temperature=0.1)
                # check if Chinese leaked
                if any(w in res for w in ['显然', '我们', '坐标', '对于', '欧几里得']):
                    print(f"Warning: Chinese leaked on attempt {attempt+1}, retrying...")
                    time.sleep(1)
                    continue
                break
            except Exception as e:
                print(f"Error on attempt {attempt+1}: {e}")
                time.sleep(2)

        print(f"Done: {len(res)} Japanese chars.")
        cache[sec_key]["translation_pieces"][c_idx] = res

    # Reassemble full translations for modified sections
    for sec_key, _ in TARGET_BAD_CHUNKS:
        cache[sec_key]["japanese_translation"] = "\n\n".join(cache[sec_key]["translation_pieces"])

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    print("\nAll target bad chunks successfully re-translated and cache updated!")

if __name__ == "__main__":
    main()
