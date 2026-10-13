# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from thompson_ch01_03 import CHAPTERS_1_3
from thompson_ch04_06 import CHAPTERS_4_6
from thompson_ch07_09 import CHAPTERS_7_9
from thompson_ch10_12 import CHAPTERS_10_12

CACHE_DIR = 'ollama_cache_thompson_calculus'
os.makedirs(CACHE_DIR, exist_ok=True)

ALL_CHAPTERS = {}
ALL_CHAPTERS.update(CHAPTERS_1_3)
ALL_CHAPTERS.update(CHAPTERS_4_6)
ALL_CHAPTERS.update(CHAPTERS_7_9)
ALL_CHAPTERS.update(CHAPTERS_10_12)

def main():
    print(f"=== Writing Thompson Calculus Cache for all {len(ALL_CHAPTERS)} chapters ===")
    total_chars = 0
    for num in sorted(ALL_CHAPTERS.keys()):
        title, content = ALL_CHAPTERS[num]
        fname = f"chap_{num:02d}.txt"
        fpath = os.path.join(CACHE_DIR, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        chars = len(content)
        total_chars += chars
        print(f"Chapter {num:02d}: {title} -> {chars:,} chars written to {fpath}")
    print(f"=== Done! Total characters: {total_chars:,} ===")

if __name__ == '__main__':
    main()
