# -*- coding: utf-8 -*-
"""
Execution Script for All Steps on Henri Poincare's Science and Hypothesis (#37157)
Pipeline:
- Step 1: Faithful Japanese Translation using qwen2.5-7b-instruct (LM Studio: http://192.168.128.16:1234/)
- Step 2: Mathematical / Physical Concept Verification using qwen2.5-math-7b-instruct (LM Studio: http://192.168.128.16:1234/)
- Step 3: High-school pedagogical explanation generation using gemma4:12b (Ollama: http://192.168.128.62:11434/)
"""

import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("scripts"))

from pipeline_utils import (
    translate_english_to_japanese,
    verify_and_check_math,
    generate_highschool_exposition
)

CHAPTERS_FILE = "books/37157_poincare_science_and_hypothesis/poincare_13_chapters.json"
CACHE_FILE = "books/37157_poincare_science_and_hypothesis/poincare_all_steps_cache.json"

CHAPTER_TOPICS = {
    "I": ("数学的推論の性質", "数学的帰納法、完全帰納法の論理、推論の創造性、ア・プリオリな総合判断と分析的推論の違い"),
    "II": ("数学的量と経験", "物理的連続体と数学的連続体、実数の切断、デデキントの連続性公理、測定と感覚の閾値"),
    "III": ("非ユークリッド幾何学", "ロバチェフスキー幾何学（双曲幾何）、リーマン幾何学（楕円幾何）、第五公準（平行線公準）、ポアンカレ円板モデル"),
    "IV": ("空間と幾何学", "幾何学的空間と視覚・触覚・運動空間の違い、同型変換群、リー群、規約主義（幾何学は規約である）"),
    "V": ("経験と幾何学", "剛体の運動と光の直進性、物理法則と幾何学的公理の不可分性、空間の次元の概念"),
    "VI": ("古典力学", "ニュートンの運動法則、質量と力の定義の循環性、慣性の法則、慣性質量と重力質量"),
    "VII": ("相対運動と絶対運動", "ニュートンのバケツ実験、マッハの原理、空間の相対性、エーテルと座標系"),
    "VIII": ("エネルギーと熱力学", "エネルギー保存則、熱力学第1・第2法則、不可逆性とエントロピー、ハミルトン形式と最小作用の原理"),
    "IX": ("物理学における仮説", "仮説の3分類（検証可能・無害・一般化）、オッカムの剃刀、単純性の仮定"),
    "X": ("現代物理学の理論", "原子論、マクスウェル方程式とエーテル、現象論的方程式と力学モデルの対応"),
    "XI": ("確率論の計算", "客観的偶然と主観的無知、微小原因と巨大結果（カオス）、ルーレットの回転と一様分布、大数の法則"),
    "XII": ("光学と電磁気学", "フレネルの波動論、マクスウェルの電磁場方程式、変位電流、光速度不変への胎動"),
    "XIII": ("電気力学とローレンツの理論", "電荷と電流の相互作用、ローレンツ力、相対性原理の先駆、質量と速度の依存関係")
}

def chunk_text(text, max_len=2200):
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
    if not os.path.exists(CHAPTERS_FILE):
        print(f"Error: {CHAPTERS_FILE} not found.", flush=True)
        return

    with open(CHAPTERS_FILE, "r", encoding="utf-8") as f:
        chapters = json.load(f)

    cached = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cached = json.load(f)
            print(f"Loaded existing cache: {len(cached)} chapters.", flush=True)
        except Exception as e:
            print(f"Failed to read cache: {e}", flush=True)

    print(f"Starting All Steps pipeline for {len(chapters)} chapters of Poincare...", flush=True)

    for i, ch in enumerate(chapters):
        num = ch["number"]
        title = ch["title"]
        key = f"Chapter_{num}"
        topic_info = CHAPTER_TOPICS.get(num, (title, title))
        
        print(f"\n==========================================", flush=True)
        print(f"[{i+1}/{len(chapters)}] Chapter {num}: {title} ({ch['length']} chars)", flush=True)
        print(f"Topic: {topic_info[0]} ({topic_info[1]})", flush=True)
        print(f"==========================================", flush=True)

        if key in cached and cached[key].get("highschool_lecture"):
            print(f"Chapter {num} is already fully completed. Skipping.", flush=True)
            continue

        text = ch["text"]
        chunks = chunk_text(text, max_len=2200)
        print(f"Divided into {len(chunks)} chunks.", flush=True)

        ch_trans_pieces = []
        ch_math_notes = []

        # Step 1 & Step 2 for each chunk
        for c_idx, chunk in enumerate(chunks):
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
            ch_trans_pieces.append(ja_trans)

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

        full_translation = "\n\n".join(ch_trans_pieces)

        # Step 3: High school exposition lecture generation using Ollama gemma4:12b
        print(f"  [Step 3] Generating High School Exposition Lecture with gemma4:12b (Ollama)...", flush=True)
        t4 = time.time()
        
        # Take key excerpt for pedagogical prompt
        excerpt_for_lecture = "\n\n".join(ch_trans_pieces[:4])
        lecture_prompt = (
            f"あなたは高校生に寄り添う親しみやすく明快な数学・物理の名講師です。\n"
            f"アンリ・ポアンカレの名著『科学と仮説』の【第{num}章：{topic_info[0]}】（主要テーマ：{topic_info[1]}）について、"
            f"高校生（数学I・II・B・IIIを学ぶ生徒）でも根本から感動的に理解できるよう、"
            f"丁寧で充実した解説講義を執筆してください。\n\n"
            f"【講義の構成ルール】\n"
            f"1. イントロダクション：なぜこの問題が重要なのか、ポアンカレの疑問（直観的な問いかけ）\n"
            f"2. 数学的・物理的アイデアの根本解説：具体的な日常の例えや図解のイメージを交えて数式（LaTeX形式）の意味を解き明かす\n"
            f"3. ポアンカレの深い洞察：従来の常識を覆した規約主義や数学的思考の発見\n"
            f"4. 高校生のための例題と詳しいステップ解説（数式付き）\n"
            f"5. 本章のまとめと哲学的メッセージ\n\n"
            f"【原著日本語訳の要約・参考抜粋】\n{excerpt_for_lecture[:3000]}"
        )
        
        try:
            lecture_text = generate_highschool_exposition(full_translation, f"{topic_info[0]} ({topic_info[1]})", model="gemma4:12b")
        except Exception as e:
            print(f"  [Step 3 Retry]: {e}", flush=True)
            time.sleep(3)
            lecture_text = generate_highschool_exposition(full_translation, f"{topic_info[0]} ({topic_info[1]})", model="gemma4:12b")
        t5 = time.time()
        print(f"  [Step 3 Done] ({t5-t4:.1f}s, {len(lecture_text)} chars)", flush=True)

        cached[key] = {
            "number": num,
            "title_en": title,
            "topic_ja": topic_info[0],
            "topic_details": topic_info[1],
            "length_en": ch["length"],
            "japanese_translation": full_translation,
            "math_verification_notes": ch_math_notes,
            "highschool_lecture": lecture_text
        }

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cached, f, ensure_ascii=False, indent=2)
        print(f"Saved Chapter {num} checkpoint to {CACHE_FILE}", flush=True)

    print("\nAll 13 chapters completed All Steps (Step 1, Step 2, Step 3) successfully!", flush=True)

if __name__ == "__main__":
    main()
