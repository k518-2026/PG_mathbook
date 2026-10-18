# -*- coding: utf-8 -*-
"""
Robust text cleaning for Einstein translation.
Applies official Gutenberg formula mappings and fixes LaTeX formatting.
"""

import re
import sys
import os

sys.path.insert(0, os.path.abspath("scripts"))
from einstein_image_math_map import IMAGE_MAP

def clean_text_for_latex(text):
    t = text

    # Remove prompt artifacts
    t = re.sub(r'以下の文章を忠実に日本語へ翻訳しました：?\s*', '', t)
    t = re.sub(r'以下が翻訳です：?\s*', '', t)
    t = re.sub(r'翻訳文：?\s*', '', t)

    # Clean any remaining image markers
    t = re.sub(r'\[\s*\d+\s*\]', '', t)

    # Normalize backslash underscores
    t = t.replace(r'\_', '_')

    math_tokens = []
    def add_token(math_str):
        math_tokens.append(math_str)
        return "ZZZMATHTOKEN" + str(len(math_tokens)-1) + "ZZZ"

    # Stash all standard math and equation/array environments first!
    t = re.sub(r'\\begin\{(align\*?|gather\*?|multline\*?|equation\*?|array|Syllogism)\}.*?\\end\{\1\}', lambda m: add_token(m.group(0)), t, flags=re.DOTALL)
    t = re.sub(r'\$\$.*?\$\$', lambda m: add_token(m.group(0)), t, flags=re.DOTALL)
    t = re.sub(r'\\\[.*?\\\]', lambda m: add_token(m.group(0)), t, flags=re.DOTALL)
    t = re.sub(r'\\\(.*?\\\)', lambda m: add_token(m.group(0)), t, flags=re.DOTALL)
    t = re.sub(r'(?<!\\)\$[^$\n]+(?<!\\)\$', lambda m: add_token(m.group(0)), t)

    # Insert image map as protected tokens
    for img_token, math_rep in IMAGE_MAP.items():
        if img_token in t:
            token_key = add_token(math_rep)
            t = t.replace(img_token, "\n\n" + token_key + "\n\n")

    t = re.sub(r'image\d+', '', t)

    # Clean specific remaining formula patterns in plain text
    t = t.replace('_ds_2 = _g_11_du_2 + 2_g_12_du dv_ + _g_22_dv_2,', add_token(r'\[ ds^2 = g_{11} du^2 + 2 g_{12} du\, dv + g_{22} dv^2 \]'))
    t = t.replace('_ds_2 = _du_2 + _dv_2', add_token(r'\[ ds^2 = du^2 + dv^2 \]'))
    t = t.replace('_ds^2 = _g_{11}_dx_1^2 + 2_g_{12}_dx_1__dx_2 ... + _g_{44}_dx_4^2,', add_token(r'\[ ds^2 = g_{11} dx_1^2 + 2 g_{12} dx_1 dx_2 + \dots + g_{44} dx_4^2 \]'))
    t = t.replace('_ds^2 = _dx_1^2 + _dx_2^2 + _dx_3^2 + _dx_4^2.', add_token(r'\[ ds^2 = dx_1^2 + dx_2^2 + dx_3^2 + dx_4^2 \]'))
    t = t.replace('_ds^2', add_token(r'$ds^2$'))
    t = t.replace('_u_', add_token(r'$u$')).replace('_v_', add_token(r'$v$'))
    t = t.replace('_x_1, _x_2, _x_3, _x_4', add_token(r'$x_1, x_2, x_3, x_4$'))
    t = t.replace('_x_1..._x_4', add_token(r'$x_1, \dots, x_4$'))
    t = t.replace('_g_{11}', add_token(r'$g_{11}$'))
    t = t.replace('_P_', add_token(r'$P$')).replace('_P′_', add_token(r"$P'$"))
    t = t.replace('_t_ = 0', add_token(r'$t = 0$'))
    t = t.replace('_g_11, _g_12, _g_22', add_token(r'$g_{11}, g_{12}, g_{22}$'))
    t = t.replace('_g_11', add_token(r'$g_{11}$'))
    t = t.replace('_g_12', add_token(r'$g_{12}$'))
    t = t.replace('_g_22', add_token(r'$g_{22}$'))

    t = t.replace('_mc^2_', add_token(r'$mc^2$'))
    t = re.sub(r'(?<![A-Za-z0-9\$\\_])E\s*=\s*mc\^2(?![A-Za-z0-9\$_])', lambda m: add_token(r'$E = mc^2$'), t)
    t = re.sub(r'(?<![A-Za-z0-9\$\\_])mc\^2(?![A-Za-z0-9\$_])', lambda m: add_token(r'$mc^2$'), t)

    # Subscripts like _x_1, _x_2, _x_3, _x_4, _E_0, _g_11 in remaining text
    t = re.sub(r'_([a-zA-Z]+)_([0-9a-zA-Z]+)', lambda m: add_token(f"${m.group(1)}_{{{m.group(2)}}}$"), t)

    # Single-letter variables and primed variables like _x_, _y_, _z_, _t_, _v_, _c_, _K_, _K'_, _K′_
    t = re.sub(r'_([A-Za-z0-9\'’]+)_', lambda m: add_token(f"${m.group(1)}$"), t)

    # Variables with comma separation like _x, y, z, t_
    t = re.sub(r'_([a-zA-Z0-9,\s\'’]+)_', lambda m: add_token(f"${m.group(1)}$"), t)

    # Any remaining pairs of underscores
    t = re.sub(r'_([^_]+)_', lambda m: add_token(f"${m.group(1)}$") if len(m.group(1)) <= 10 and not any(c in m.group(1) for c in 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん一-龯') else r'\\textit{' + m.group(1) + '}', t)

    # Lone underscores, & % #
    t = re.sub(r'(?<!\\)_', r'\\_', t)
    t = re.sub(r'(?<!\\)&', r'\\&', t)
    t = re.sub(r'(?<!\\)%', r'\\%', t)
    t = re.sub(r'(?<!\\)#', r'\\#', t)

    # Restore all tokens
    for i, token in enumerate(math_tokens):
        cleaned = token
        if cleaned.startswith('$$') and cleaned.endswith('$$'):
            inner = cleaned[2:-2].strip()
            cleaned = "\\[\n" + inner + "\n\\]"
        t = t.replace("ZZZMATHTOKEN" + str(i) + "ZZZ", cleaned)

    # Terminology and Chinese cleanup
    replacements = {
        '坐标': '座標', '欧几里得': 'ユークリッド', '欧几': 'ユークリッド',
        'カート游戏': 'デカルト座標の規則', 'Marble': '大理石',
        '不 penetrability': '不入性', 'simultaneity': '同時性',
        '二维坐标': '二次元座標', '三维坐标': '三次元座標', '四维坐标': '四次元座標',
        '显然，': '明らかに、', '显然': '明らかに', '我们必须': 'ここで私たちは',
        '给出': '与える', '对于': 'に対して', '满足': '満たす', '通过': 'を通じて',
        '方程组': '方程式系', '方程式式': '方程式', '方程': '方程式', '这一': 'この', '这': 'これ',
        '们': '達', '对': '対', '刚': '剛', '显': '顕', '借用了': '借用した',
        '借用': '借用', '方程式式系': '方程式系'
    }
    for k, v in replacements.items():
        t = t.replace(k, v)

    t = t.replace('方程式式', '方程式')

    return t
