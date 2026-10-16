# -*- coding: utf-8 -*-
with open('books/33283_thompson_calculus/thompson_calculus_translation.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix \end{gather*}} -> \end{gather*}
content = content.replace(r'\end{gather*}}', r'\end{gather*}')

# Add missing macros to preamble
macro_defs = r'''\newcommand{\TmpColA}{}
\newcommand{\TmpColB}{}
\newcommand{\PadTo}[3][]{#3}
'''
if r'\newcommand{\TmpColA}' not in content:
    content = content.replace(r'\begin{document}', macro_defs + '\n\\begin{document}')

with open('books/33283_thompson_calculus/thompson_calculus_translation.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print('Preamble and gather braces successfully fixed!')
