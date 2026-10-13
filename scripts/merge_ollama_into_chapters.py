# -*- coding: utf-8 -*-
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

CACHE_DIR = 'ollama_cache_thompson_calculus'
LECTURES_FILE = os.path.join(CACHE_DIR, 'ollama_lectures.json')

def merge_lectures():
    if not os.path.exists(LECTURES_FILE):
        print(f"Error: {LECTURES_FILE} not found!")
        return

    with open(LECTURES_FILE, 'r', encoding='utf-8') as f:
        lectures = json.load(f)

    for num_str, lecture_text in lectures.items():
        num = int(num_str)
        fname = f"chap_{num:02d}.txt"
        fpath = os.path.join(CACHE_DIR, fname)
        if not os.path.exists(fpath):
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already merged
        if "【Ollama専任講師講義】" in content:
            continue

        header_marker = "**教育情報分析研究会　数学教育・物理解析リサーチユニット**\n\n"
        ollama_block = f"""### 【Ollama専任講師特別講義】トンプソン流直観的微積分の扉

{lecture_text}

"""
        if header_marker in content:
            new_content = content.replace(header_marker, header_marker + ollama_block, 1)
        else:
            lines = content.split('\n\n')
            new_content = lines[0] + '\n\n' + ollama_block + '\n\n'.join(lines[1:])

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Merged Ollama lecture into Chapter {num:02d} ({len(new_content):,} chars)")

if __name__ == '__main__':
    merge_lectures()
