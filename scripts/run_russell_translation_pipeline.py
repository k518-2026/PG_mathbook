# -*- coding: utf-8 -*-
"""
Execution Script for Translation and Math Verification on Russell's Mysticism and Logic (#25447)
底本: Bertrand Russell, "Mysticism and Logic and Other Essays"
全10篇のエッセイ + 序文（計11セクション）
Step 1: qwen2.5-7b-instruct (原著直訳・完全翻訳、一切の省略・要約なし)
Step 2: qwen2.5-math-7b-instruct (数理・論理・記号論理・数哲学の検証)
"""

import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("scripts"))
from pipeline_utils import translate_english_to_japanese, verify_and_check_math

SECTIONS_FILE = "books/25447_russell_mathematical_philosophy/russell_sections.json"
OUTPUT_CACHE_FILE = "books/25447_russell_mathematical_philosophy/russell_full_translation_cache.json"

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
    print(f"Opening {SECTIONS_FILE}...", flush=True)
    if not os.path.exists(SECTIONS_FILE):
        print(f"Error: {SECTIONS_FILE} not found.", flush=True)
        return

    with open(SECTIONS_FILE, "r", encoding="utf-8") as f:
        sections = json.load(f)

    cached_results = {}
    if os.path.exists(OUTPUT_CACHE_FILE):
        try:
            with open(OUTPUT_CACHE_FILE, "r", encoding="utf-8") as f:
                cached_results = json.load(f)
            print(f"Loaded existing cache: {len(cached_results)} sections in cache.", flush=True)
        except Exception as e:
            print(f"Failed to read existing cache: {e}", flush=True)

    print(f"Starting Step 1 & Step 2 for {len(sections)} sections of Russell #25447...", flush=True)

    total_chunks = 0
    for sec in sections:
        total_chunks += len(chunk_text(sec["text_en"], max_len=2400))
    print(f"Total workload: {len(sections)} sections, {total_chunks} chunks.", flush=True)

    completed_chunks_count = 0

    for i, sec in enumerate(sections):
        num = sec["number"]
        title = sec["title_en"]
        title_ja = sec.get("title_ja", "")
        key = f"Sec_{num}"
        print(f"\n==========================================", flush=True)
        print(f"[{i+1}/{len(sections)}] Processing Section {num}: {title} ({sec['length_raw']} chars)", flush=True)
        print(f"==========================================", flush=True)

        if key in cached_results and cached_results[key].get("japanese_translation"):
            print(f"Section {num} is already fully in cache. Skipping.", flush=True)
            completed_chunks_count += cached_results[key].get("chunks_done", 0)
            continue

        text = sec["text_en"]
        chunks = chunk_text(text, max_len=2400)
        print(f"Divided into {len(chunks)} chunks.", flush=True)

        if key not in cached_results:
            cached_results[key] = {
                "number": num,
                "title_en": title,
                "title_ja": title_ja,
                "length_en": sec["length_raw"],
                "chunks_done": 0,
                "translation_pieces": [],
                "math_notes": []
            }

        sec_state = cached_results[key]
        sec_translation_pieces = sec_state.get("translation_pieces", [])
        sec_math_notes = sec_state.get("math_notes", [])
        start_chunk_idx = len(sec_translation_pieces)

        if start_chunk_idx > 0:
            print(f"Resuming Section {num} from chunk {start_chunk_idx+1}/{len(chunks)}...", flush=True)

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
            sec_translation_pieces.append(ja_trans)

            # Step 2: Math/Logic Verification with qwen2.5-math-7b-instruct
            print("  [Step 2] Logic & Math checking with qwen2.5-math-7b-instruct...", flush=True)
            t2 = time.time()
            try:
                math_note = verify_and_check_math(ja_trans, original_english=chunk)
            except Exception as e:
                print(f"  [Step 2 Retry]: {e}", flush=True)
                time.sleep(2)
                math_note = verify_and_check_math(ja_trans, original_english=chunk)
            t3 = time.time()
            print(f"  [Step 2 Done] ({t3-t2:.1f}s, {len(math_note)} chars)", flush=True)
            sec_math_notes.append(math_note)

            sec_state["translation_pieces"] = sec_translation_pieces
            sec_state["math_notes"] = sec_math_notes
            sec_state["chunks_done"] = len(sec_translation_pieces)

            # Atomic checkpoint save
            temp_file = OUTPUT_CACHE_FILE + ".tmp"
            for attempt in range(5):
                try:
                    with open(temp_file, "w", encoding="utf-8") as f:
                        json.dump(cached_results, f, ensure_ascii=False, indent=2)
                    if os.path.exists(OUTPUT_CACHE_FILE):
                        os.replace(temp_file, OUTPUT_CACHE_FILE)
                    else:
                        os.rename(temp_file, OUTPUT_CACHE_FILE)
                    break
                except Exception:
                    time.sleep(1)

        full_translation = "\n\n".join(sec_translation_pieces)
        cached_results[key]["japanese_translation"] = full_translation
        cached_results[key]["math_verification_notes"] = sec_math_notes

        temp_file = OUTPUT_CACHE_FILE + ".tmp"
        for attempt in range(5):
            try:
                with open(temp_file, "w", encoding="utf-8") as f:
                    json.dump(cached_results, f, ensure_ascii=False, indent=2)
                if os.path.exists(OUTPUT_CACHE_FILE):
                    os.replace(temp_file, OUTPUT_CACHE_FILE)
                else:
                    os.rename(temp_file, OUTPUT_CACHE_FILE)
                break
            except Exception:
                time.sleep(1)

        print(f"Section {num} completed and saved. ({len(full_translation)} Japanese chars)", flush=True)

    print("\nALL SECTIONS SUCCESSFULLY TRANSLATED AND VERIFIED!", flush=True)

if __name__ == "__main__":
    main()
