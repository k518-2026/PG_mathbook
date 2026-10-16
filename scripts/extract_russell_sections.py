# -*- coding: utf-8 -*-
"""
Extract all essays and preface from Bertrand Russell's pg25447.txt
"""

import json
import re

with open('books/25447_russell_mathematical_philosophy/pg25447.txt', 'r', encoding='utf-8') as f:
    text = f.read()

chapters_meta = [
    ('PREFACE', 'PREFACE', '序文（著者まえがき）', 5003, 8564),
    ('I', 'MYSTICISM AND LOGIC', '神秘主義と論理', 8564, 65245),
    ('II', 'THE PLACE OF SCIENCE IN A LIBERAL EDUCATION', '教養教育における科学の位置', 65245, 87295),
    ('III', "A FREE MAN'S WORSHIP", '自由人の祈祷', 87295, 107492),
    ('IV', 'THE STUDY OF MATHEMATICS', '数学の研究', 107492, 135432),
    ('V', 'MATHEMATICS AND THE METAPHYSICIANS', '数学と形而上学者たち', 135432, 177752),
    ('VI', 'ON SCIENTIFIC METHOD IN PHILOSOPHY', '哲学における科学的方法について', 177752, 227649),
    ('VII', 'THE ULTIMATE CONSTITUENTS OF MATTER', '物質の究極的構成要素', 227649, 265191),
    ('VIII', 'THE RELATION OF SENSE-DATA TO PHYSICS', 'センス・データと物理学との関係', 265191, 327783),
    ('IX', 'ON THE NOTION OF CAUSE', '原因の概念について', 327783, 379341),
    ('X', 'KNOWLEDGE BY ACQUAINTANCE AND KNOWLEDGE BY DESCRIPTION', '直接体験による知識と記述による知識', 379341, 426052)
]

sections = []
for num, title_en, title_ja, s, e in chapters_meta:
    raw = text[s:e].strip()
    fn_pos = raw.rfind('FOOTNOTES:')
    if fn_pos != -1:
        body = raw[:fn_pos].strip()
        footnotes_raw = raw[fn_pos:].strip()
    else:
        body = raw
        footnotes_raw = ''

    sections.append({
        'number': num,
        'title_en': title_en,
        'title_ja': title_ja,
        'length_raw': len(raw),
        'length_body': len(body),
        'length_fn': len(footnotes_raw),
        'text_en': raw,
        'body_en': body,
        'footnotes_en': footnotes_raw
    })
    print(f"{num:7} | Raw: {len(raw):6} chars | Body: {len(body):6} chars | FN: {len(footnotes_raw):5} chars | {title_en}")

out_path = 'books/25447_russell_mathematical_philosophy/russell_sections.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(sections, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(sections)} sections to {out_path}")
