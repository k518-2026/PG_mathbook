# -*- coding: utf-8 -*-
"""
Execution Script for Step 1 (Translation) and Step 2 (Math Check) on
Silvanus P. Thompson's Calculus Made Easy (#33283)
LM Studio: http://192.168.128.16:1234/
Step 1: qwen2.5-7b-instruct (faithful Japanese translation, no preamble)
Step 2: qwen2.5-math-7b-instruct (rigorous math checking & formula verification)
"""

import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("scripts"))
from pipeline_utils import translate_english_to_japanese, verify_and_check_math
from thompson_metadata import SECTIONS_METADATA

CHAPTERS_FILE = "books/33283_thompson_calculus/thompson_chapters.json"
OUTPUT_CACHE_FILE = "books/33283_thompson_calculus/thompson_full_translation_math_verified.json"

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

def main():
    print(f"Opening {CHAPTERS_FILE}...", flush=True)
    if not os.path.exists(CHAPTERS_FILE):
        print(f"Error: {CHAPTERS_FILE} not found.", flush=True)
        return

    with open(CHAPTERS_FILE, "r", encoding="utf-8") as f:
        chapters = json.load(f)

    cached_results = {}
    if os.path.exists(OUTPUT_CACHE_FILE):
        try:
            with open(OUTPUT_CACHE_FILE, "r", encoding="utf-8") as f:
                cached_results = json.load(f)
            print(f"Loaded existing cache: {len(cached_results)} sections already in cache.", flush=True)
        except Exception as e:
            print(f"Failed to read existing cache: {e}", flush=True)

    print(f"Starting Step 1 & Step 2 for {len(chapters)} sections of Thompson #33283...", flush=True)

    for i, ch in enumerate(chapters):
        meta = SECTIONS_METADATA[i]
        sec_id = meta["id"]
        sec_num = meta["number"]
        sec_title = meta["title_ja"]
        title_en = meta["title_en"]
        
        print(f"\n==========================================", flush=True)
        print(f"[{i+1}/{len(chapters)}] Processing {sec_num}: {sec_title} ({title_en})", flush=True)
        print(f"==========================================", flush=True)

        if sec_id in cached_results and cached_results[sec_id].get("japanese_translation"):
            print(f"Section {sec_id} is already fully translated in cache. Skipping.", flush=True)
            continue

        raw_text = ch["text"]
        chunks = chunk_text(raw_text, max_len=2400)
        print(f"Divided into {len(chunks)} chunks.", flush=True)

        if sec_id not in cached_results:
            cached_results[sec_id] = {
                "id": sec_id,
                "number": sec_num,
                "title_en": title_en,
                "title_ja": sec_title,
                "subtitle_ja": meta.get("subtitle_ja", ""),
                "length_en": ch["length"],
                "chunks_done": 0,
                "translation_pieces": [],
                "math_notes": []
            }

        sec_state = cached_results[sec_id]
        translation_pieces = sec_state.get("translation_pieces", [])
        math_notes = sec_state.get("math_notes", [])
        start_chunk_idx = len(translation_pieces)

        if start_chunk_idx > 0:
            print(f"Resuming {sec_id} from chunk {start_chunk_idx+1}/{len(chunks)}...", flush=True)

        for c_idx in range(start_chunk_idx, len(chunks)):
            chunk = chunks[c_idx]
            print(f"  --- Chunk {c_idx+1}/{len(chunks)} ({len(chunk)} chars) ---", flush=True)

            # Step 1: Translation with qwen2.5-7b-instruct
            print("  [Step 1] Translating with qwen2.5-7b-instruct...", flush=True)
            t0 = time.time()
            try:
                ja_trans = translate_english_to_japanese(chunk)
            except Exception as e:
                print(f"  [Step 1 Retry]: {e}", flush=True)
                time.sleep(2)
                ja_trans = translate_english_to_japanese(chunk)
            t1 = time.time()
            print(f"  [Step 1 Done] ({t1-t0:.1f}s, {len(ja_trans)} chars)", flush=True)
            translation_pieces.append(ja_trans)

            # Step 2: Math Verification with qwen2.5-math-7b-instruct
            print("  [Step 2] Math checking with qwen2.5-math-7b-instruct...", flush=True)
            t2 = time.time()
            try:
                math_note = verify_and_check_math(ja_trans, original_english=chunk)
            except Exception as e:
                print(f"  [Step 2 Retry]: {e}", flush=True)
                time.sleep(2)
                math_note = verify_and_check_math(ja_trans, original_english=chunk)
            t3 = time.time()
            print(f"  [Step 2 Done] ({t3-t2:.1f}s)", flush=True)
            math_notes.append(math_note)

            sec_state["chunks_done"] = len(translation_pieces)
            sec_state["translation_pieces"] = translation_pieces
            sec_state["math_notes"] = math_notes

            # Incremental save
            with open(OUTPUT_CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(cached_results, f, ensure_ascii=False, indent=2)

        # Merge full translation for this section
        sec_state["japanese_translation"] = "\n\n".join(translation_pieces)
        sec_state["math_verification_notes"] = "\n\n".join(math_notes)
        with open(OUTPUT_CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cached_results, f, ensure_ascii=False, indent=2)
        print(f"Section {sec_id} completely finished and saved! ({len(sec_state['japanese_translation'])} chars)", flush=True)

    print("\n==========================================", flush=True)
    print("ALL 26 SECTIONS OF THOMPSON CALCULUS PROCESSED!", flush=True)
    print("==========================================", flush=True)

if __name__ == "__main__":
    main()
