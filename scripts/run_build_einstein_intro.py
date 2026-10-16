# -*- coding: utf-8 -*-
"""
Main Builder for Einstein Relativity Intro
(古典で学び直すアインシュタイン相対性理論入門)
Combines Preamble, 12 Chapters (TikZ Fig, OrigBox, LectureBox, ExampleBox), Glossary, Exercises, Postamble
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from scripts.make_einstein_intro_tex import PREAMBLE, POSTAMBLE
from scripts.einstein_figures import FIGS
from scripts.einstein_examples import EXAMPLES
from scripts.einstein_chapters import CHAPTERS

OUTPUT_TEX = "books/30155_einstein_relativity/einstein_relativity_intro.tex"

def build_tex():
    tex_parts = [PREAMBLE]
    
    for ch_num in range(1, 13):
        ch = CHAPTERS[ch_num]
        fig_tikz, fig_caption = FIGS[ch_num]
        example_tex = EXAMPLES[ch_num]
        
        part_name = ""
        if ch_num == 1:
            part_name = "\\part{特殊相対性理論（時間と空間の革命）}\n\n"
        elif ch_num == 8:
            part_name = "\\part{一般相対性理論（重力と曲がった時空）}\n\n"
        elif ch_num == 12:
            part_name = "\\part{現代宇宙論とアインシュタインの遺産}\n\n"

        ch_tex = f"""{part_name}\\chapter{{{ch['title']}}}
\\begin{{center}}
{{\\Large\\bfseries\\gtfamily {ch['subtitle']}}}
\\end{{center}}
\\vspace*{{2mm}}

\\section*{{本章の視覚的見取り図}}
\\begin{{center}}
{fig_tikz}

\\small\\textbf{{図版解説：}}{fig_caption}
\\end{{center}}
\\vspace*{{2mm}}

\\section*{{アインシュタインの原典思索}}
\\begin{{origbox}}[原著第{ch_num}章：アルベルト・アインシュタインの肉声]
{ch['orig']}
\\end{{origbox}}

\\section*{{大人のための徹底解説講義}}
\\begin{{lecturebox}}[徹底講義：高校数学で追体験する物理学革命]
{ch['lecture']}
\\end{{lecturebox}}

\\vspace*{{3mm}}
{example_tex}
"""
        tex_parts.append(ch_tex)
    
    tex_parts.append(POSTAMBLE)
    
    full_content = "\n\n\\clearpage\n".join(tex_parts)
    
    os.makedirs(os.path.dirname(OUTPUT_TEX), exist_ok=True)
    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    print(f"Successfully generated {OUTPUT_TEX} ({len(full_content)} chars)")

if __name__ == "__main__":
    build_tex()
