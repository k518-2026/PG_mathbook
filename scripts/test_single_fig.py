import os, subprocess

TEMPLATE = r'''\documentclass[preview]{standalone}
\usepackage{luatexja}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,calc,patterns,backgrounds}

\definecolor{primaryblue}{RGB}{24, 76, 120}
\definecolor{softblue}{RGB}{235, 243, 250}
\definecolor{darkslate}{RGB}{44, 62, 80}
\definecolor{warmamber}{RGB}{217, 119, 6}
\definecolor{softamber}{RGB}{254, 243, 199}
\definecolor{accentgreen}{RGB}{13, 148, 136}
\definecolor{softgreen}{RGB}{240, 253, 244}
\definecolor{crimson}{RGB}{190, 24, 93}
\definecolor{softrose}{RGB}{255, 241, 242}

\begin{document}
__TIKZ__
\end{document}
'''

def test_fig(fig_num, tikz_code):
    os.makedirs('test_figs', exist_ok=True)
    tex_path = f'test_figs/fig_{fig_num}.tex'
    pdf_path = f'test_figs/fig_{fig_num}.pdf'
    png_prefix = f'test_figs/fig_{fig_num}'
    
    # Extract tikzpicture only if wrapped in figure
    if r'\begin{tikzpicture}' in tikz_code:
        start = tikz_code.find(r'\begin{tikzpicture}')
        end = tikz_code.find(r'\end{tikzpicture}') + len(r'\end{tikzpicture}')
        inner_tikz = tikz_code[start:end]
    else:
        inner_tikz = tikz_code

    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(TEMPLATE.replace('__TIKZ__', inner_tikz))
        
    res = subprocess.run(['lualatex', '-interaction=nonstopmode', f'fig_{fig_num}.tex'], cwd='test_figs', capture_output=True, encoding='utf-8', errors='ignore')
    if res.returncode != 0:
        print(f"Error compiling fig {fig_num}:")
        if res.stdout:
            print(res.stdout[-1000:])
        return False
        
    subprocess.run(['pdftoppm', '-png', '-r', '150', f'fig_{fig_num}.pdf', f'fig_{fig_num}'], cwd='test_figs', capture_output=True)
    print(f"Fig {fig_num} compiled successfully to test_figs/fig_{fig_num}-1.png")
    return True
