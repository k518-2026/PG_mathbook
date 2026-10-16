# -*- coding: utf-8 -*-
with open('books/33283_thompson_calculus/thompson_calculus_translation.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 269
lines[268] = '\\noindent\\textbf{\\small 【章の論理とテーマ】べき関数 $y = x^n$ の微分の基本公式とその第一原理からの導出}\\\\[4mm]\n'

# Lines 437-438
lines[437] = '        \\text{($dx$ の高次の項)}\n'
lines[438] = '% blank removed\n'

with open('books/33283_thompson_calculus/thompson_calculus_translation.tex', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Lines written successfully from fix_lines.py!')\newcommand{\\TmpColA}{}
\\newcommand{\\TmpColB}{}
\\newcommand{\\PadTo}[3][]{#3}

