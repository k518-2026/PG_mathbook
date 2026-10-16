# -*- coding: utf-8 -*-
"""
Execution Script for Translation and Math Verification on Einstein's Relativity (#30155)
底本: Albert Einstein, "Relativity: The Special and the General Theory"
Part I (1-17), Part II (18-29), Part III (30-32), and Appendices I-IV
Step 1: qwen2.5-7b-instruct (Faithful, non-summarizing translation to Japanese)
Step 2: qwen2.5-math-7b-instruct (Mathematical & Formula consistency check)
"""

import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("scripts"))
from pipeline_utils import translate_english_to_japanese, verify_and_check_math

SECTIONS_FILE = "books/30155_einstein_relativity/einstein_sections.json"
OUTPUT_CACHE_FILE = "books/30155_einstein_relativity/einstein_full_translation_cache.json"

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

    print(f"Starting Step 1 & Step 2 for {len(sections)} sections/appendices of Einstein #30155...", flush=True)

    for i, sec in enumerate(sections):
        num = sec["number"]
        title = sec["title_en"]
        part = sec.get("part", "")
        key = f"Sec_{num}"
        print(f"\n==========================================", flush=True)
        print(f"[{i+1}/{len(sections)}] Processing {part} - Section {num}: {title} ({sec['length']} chars)", flush=True)
        print(f"==========================================", flush=True)

        if key in cached_results and cached_results[key].get("japanese_translation"):
            print(f"Section {num} is already fully in cache. Skipping.", flush=True)
            continue

        text = sec["text_en"]
        chunks = chunk_text(text, max_len=2400)
        print(f"Divided into {len(chunks)} chunks.", flush=True)

        if key not in cached_results:
            cached_results[key] = {
                "number": num,
                "part": part,
                "title_en": title,
                "length_en": sec["length"],
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
                print(f"Saved Section {num} checkpoint to {OUTPUT_CACHE_FILE}", flush=True)
                break
            except Exception as e:
                print(f"Warning: Failed to save checkpoint (attempt {attempt+1}/5): {e}", flush=True)
                time.sleep(2)

    print("\nAll 37 sections/appendices of Einstein #30155 completed Step 1 and Step 2 successfully!", flush=True)

if __name__ == "__main__":
    main()
