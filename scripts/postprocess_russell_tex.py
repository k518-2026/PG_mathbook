# -*- coding: utf-8 -*-
"""
Post-process and clean TeX file:
1. Normalize simplified Chinese characters that occasionally leak into Japanese text.
2. Fix fancyhdr headheight.
"""

import sys

TEX_PATH = "books/25447_russell_mathematical_philosophy/russell_mysticism_and_logic_translation.tex"

simp2trad = {
    '经': '経', '调': '調', '题': '題', '们': '達', '这': 'これ', '实': '実',
    '释': '釈', '视': '視', '为': '為', '则': '則', '误': '誤', '导': '導',
    '观': '観', '议': '議', '认': '認', '专': '専', '词': '詞', '赋': '賦',
    '对': '対', '质': '質', '仅': '僅', '语': '語', '现': '現', '说': '説',
    '发': '発', '应': '応', '关': '関', '与': 'と', '并': '並', '样': '様',
    '两': '両', '时': '時', '间': '間', '动': '動', '见': '見', '线': '線',
    '变': '変', '种': '種', '规': '規', '统': '統', '计': '計', '义': '義',
    '类': '類', '设': '設', '极': '極', '无': '無', '确': '確', '结': '結',
    '构': '構', '断': '断', '处': '処', '选': '選', '择': '択', '联': '連',
    '系': '係', '显': '顕', '进': '進', '运': '運', '转': '転', '换': '換',
    '证': '証', '论': '論', '述': '述', '简': '簡', '单': '単', '复': '複',
    '杂': '雑', '键': '鍵', '问': '問'
}

def main():
    with open(TEX_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    count = 0
    for s, j in simp2trad.items():
        if s in text:
            c = text.count(s)
            count += c
            text = text.replace(s, j)

    print(f"Replaced {count} simplified Chinese characters.")

    # Fix fancyhdr headheight
    if "\\setlength{\\headheight}" not in text:
        text = text.replace(r"\usepackage{fancyhdr}", "\\usepackage{fancyhdr}\n\\setlength{\\headheight}{25pt}\n\\addtolength{\\topmargin}{-13pt}")

    with open(TEX_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print("Post-processing complete.")

if __name__ == "__main__":
    main()
