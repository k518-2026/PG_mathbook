# -*- coding: utf-8 -*-
"""
Robust text cleaning for Einstein translation.
Normalizes backslash underscores before processing.
"""

import re

def clean_text_for_latex(text):
    t = text
    # Clean image markers
    t = re.sub(r'image\d+', '', t)
    # Remove literal footnotes markers [6]
    t = re.sub(r'\[\s*\d+\s*\]', '', t)

    # Normalize any escaped underscores from LLM back to raw underscore:
    t = t.replace(r'\_', '_')

    math_tokens = []
    
    def add_token(math_str):
        math_tokens.append(math_str)
        return "ZZZMATHTOKEN" + str(len(math_tokens)-1) + "ZZZ"

    # Specific replacements into tokens directly:
    # Sec_XXV:
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

    # Sec_XXVI:
    t = t.replace('dx^2 + dy^2 + dz^2 - c^2 dt^2 = dx\'^2 + dy\'^2 + dz\'^2 - c^2 dt\'^2.', add_token(r'\[ dx^2 + dy^2 + dz^2 - c^2 dt^2 = dx\'^2 + dy\'^2 + dz\'^2 - c^2 dt\'^2 \]'))
    t = t.replace('ds^2 = dx^2 + dy^2 + dz^2 - c^2 dt^2,', add_token(r'\[ ds^2 = dx^2 + dy^2 + dz^2 - c^2 dt^2 \]'))
    t = t.replace('ds^2 = dx_1^2 + dx_2^2 + dx_3^2 + dx_4^2.', add_token(r'\[ ds^2 = dx_1^2 + dx_2^2 + dx_3^2 + dx_4^2 \]'))

    # Sec_XV:
    t = re.sub(r'(?<![A-Za-z0-9\$\\])E\s*=\s*mc\^2(?![A-Za-z0-9\$])', lambda m: add_token(r'$E = mc^2$'), t)
    t = re.sub(r'(?<![A-Za-z0-9\$\\])mc\^2(?![A-Za-z0-9\$])', lambda m: add_token(r'$mc^2$'), t)
    t = t.replace(r'\frac{1}{2}mv^2', add_token(r'$\frac{1}{2}mv^2$'))
    t = t.replace(r'mc^2 \left( 1 - \frac{v^2}{c^2} \right)^{-\frac{1}{2}}', add_token(r'\[ mc^2 \left( 1 - \frac{v^2}{c^2} \right)^{-\frac{1}{2}} \]'))
    t = t.replace(r'mc^2 \left( 1 + \frac{v^2}{2c^2} + \frac{3v^4}{8c^4} + \cdots \right)', add_token(r'\[ mc^2 \left( 1 + \frac{v^2}{2c^2} + \frac{3v^4}{8c^4} + \cdots \right) \]'))
    t = t.replace(r'\frac{v^2}{c^2}', add_token(r'$\frac{v^2}{c^2}$'))
    t = t.replace('E = E_0 + \\frac{1}{2}mv^2', add_token(r'\[ E = E_0 + \frac{1}{2}mv^2 \]'))
    t = t.replace('m\' = \\frac{E_0}{c^2}', add_token(r'\[ m\' = \frac{E_0}{c^2} \]'))
    t = t.replace('m = \\frac{E_0}{c^2}', add_token(r'\[ m = \frac{E_0}{c^2} \]'))
    t = t.replace(r'\Delta m = \frac{\Delta E}{c^2}', add_token(r'\[ \Delta m = \frac{\Delta E}{c^2} \]'))
    t = t.replace(r'E = mc^2 + \text{その他の項}', add_token(r'\[ E = mc^2 + \text{その他の項} \]'))
    t = t.replace('_mc^2_', add_token(r'$mc^2$'))

    # Sec_App_I:
    t = t.replace(r'x^2 - c^2 t^2 = x\'^2 - c^2 t\'^2', add_token(r'\[ x^2 - c^2 t^2 = x\'^2 - c^2 t\'^2 \]'))
    t = t.replace(r'x\'^2 - c^2 t\'^2 = x^2 - c^2 t^2', add_token(r'\[ x\'^2 - c^2 t\'^2 = x^2 - c^2 t^2 \]'))
    t = t.replace(r't\' &= \gamma \left(t - \frac{vx}{c^2}\right)', add_token(r'\[ t\' = \gamma \left(t - \frac{vx}{c^2}\right) \]'))
    t = t.replace(r'x^2 + y^2 + z^2 - c^2 t^2 = 0', add_token(r'\[ x^2 + y^2 + z^2 - c^2 t^2 = 0 \]'))
    t = t.replace(r'_x_^2 + _y_^2 + _z_^2 – _c_^2_t_^2 = 0', add_token(r'\[ x^2 + y^2 + z^2 - c^2 t^2 = 0 \]'))
    t = re.sub(r'x′?\^?2\s*\+\s*y′?\^?2\s*\+\s*z′?\^?2\s*[–\-]\s*c\^?2\s*t′?\^?2\s*=\s*0', lambda m: add_token(r'\[ x^2 + y^2 + z^2 - c^2 t^2 = 0 \]'), t)

    # Stash all standard math environments
    t = re.sub(r'\$\$.*?\$\$', lambda m: add_token(m.group(0)), t, flags=re.DOTALL)
    t = re.sub(r'\\\[.*?\\\]', lambda m: add_token(m.group(0)), t, flags=re.DOTALL)
    t = re.sub(r'\\\(.*?\\\)', lambda m: add_token(m.group(0)), t, flags=re.DOTALL)
    t = re.sub(r'(?<!\\)\$[^$\n]+(?<!\\)\$', lambda m: add_token(m.group(0)), t)

    # Subscripts like _x_1, _x_2, _x_3, _x_4 in remaining text
    t = re.sub(r'_([a-zA-Z]+)_([0-9a-zA-Z]+)', lambda m: add_token(f"${m.group(1)}_{{{m.group(2)}}}$"), t)

    # Single-letter variables _x_, _y_, _z_, _t_, _v_, _c_, _K_
    t = re.sub(r'_([A-Za-z0-9\'’]+)_', lambda m: add_token(f"${m.group(1)}$"), t)

    # Markdown italic words like _word_
    t = re.sub(r'_([^_\n]+)_', r'\\textit{\1}', t)

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

    return t
