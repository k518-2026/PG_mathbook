# -*- coding: utf-8 -*-
"""
Execution Script for Step 1 (Translation) and Step 2 (Math Check) on John Venn's The Logic of Chance (#57359)
LM Studio: http://192.168.128.16:1234/
Step 1: qwen2.5-7b-instruct (faithful Japanese translation)
Step 2: qwen2.5-math-7b-instruct (rigorous math checking & formula verification)
"""

import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("scripts"))
from pipeline_utils import translate_english_to_japanese, verify_and_check_math

CHAPTERS_FILE = "books/57359_venn_logic_of_chance/venn_19_chapters.json"
OUTPUT_CACHE_FILE = "books/57359_venn_logic_of_chance/venn_full_translation_math_verified.json"

def chunk_text(text, max_len=2200):
    """Split text into manageable chunks respecting paragraphs."""
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
            print(f"Loaded existing cache: {len(cached_results)} chapters already processed.", flush=True)
        except Exception as e:
            print(f"Failed to read existing cache: {e}", flush=True)

    print(f"Starting Step 1 & Step 2 for {len(chapters)} chapters of Venn...", flush=True)

    for i, ch in enumerate(chapters):
        num = ch["number"]
        title = ch["title"]
        key = f"Chapter_{num}"
        print(f"\n==========================================", flush=True)
        print(f"[{i+1}/{len(chapters)}] Processing Chapter {num}: {title} ({ch['length']} chars)", flush=True)
        print(f"==========================================", flush=True)

        if key in cached_results and cached_results[key].get("japanese_translation"):
            print(f"Chapter {num} is already fully in cache. Skipping.", flush=True)
            continue

        text = ch["text"]
        chunks = chunk_text(text, max_len=2200)
        print(f"Divided into {len(chunks)} chunks.", flush=True)

        if key not in cached_results:
            cached_results[key] = {
                "number": num,
                "title_en": title,
                "length_en": ch["length"],
                "chunks_done": 0,
                "translation_pieces": [],
                "math_notes": []
            }

        ch_state = cached_results[key]
        ch_translation_pieces = ch_state.get("translation_pieces", [])
        ch_math_notes = ch_state.get("math_notes", [])
        start_chunk_idx = len(ch_translation_pieces)

        if start_chunk_idx > 0:
            print(f"Resuming Chapter {num} from chunk {start_chunk_idx+1}/{len(chunks)}...", flush=True)

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
            ch_translation_pieces.append(ja_trans)

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
            ch_math_notes.append(math_note)

            # Update chunk-level state
            ch_state["translation_pieces"] = ch_translation_pieces
            ch_state["math_notes"] = ch_math_notes
            ch_state["chunks_done"] = len(ch_translation_pieces)

            # Save checkpoint every 3 chunks or at the end
            if (c_idx + 1) % 3 == 0 or (c_idx + 1) == len(chunks):
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

        full_translation = "\n\n".join(ch_translation_pieces)
        cached_results[key]["japanese_translation"] = full_translation
        cached_results[key]["math_verification_notes"] = ch_math_notes

        # Safe atomic write with retries for Windows
        temp_file = OUTPUT_CACHE_FILE + ".tmp"
        saved = False
        for attempt in range(5):
            try:
                with open(temp_file, "w", encoding="utf-8") as f:
                    json.dump(cached_results, f, ensure_ascii=False, indent=2)
                if os.path.exists(OUTPUT_CACHE_FILE):
                    os.replace(temp_file, OUTPUT_CACHE_FILE)
                else:
                    os.rename(temp_file, OUTPUT_CACHE_FILE)
                saved = True
                print(f"Saved Chapter {num} checkpoint to {OUTPUT_CACHE_FILE}", flush=True)
                break
            except Exception as e:
                print(f"Warning: Failed to save checkpoint (attempt {attempt+1}/5): {e}", flush=True)
                time.sleep(2)
        if not saved:
            print(f"Error: Could not save checkpoint for Chapter {num}", flush=True)

    print("\nAll 19 chapters of Venn completed Step 1 and Step 2 successfully!", flush=True)

if __name__ == "__main__":
    main()
