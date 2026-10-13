import os, subprocess

LATEX_TEMPLATE = r'''\documentclass[preview,border=10pt]{standalone}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,calc,patterns,backgrounds}
\definecolor{primaryblue}{RGB}{24, 76, 120}
\definecolor{softblue}{RGB}{235, 243, 250}
\definecolor{darkslate}{RGB}{44, 62, 80}
\definecolor{warmamber}{RGB}{217, 119, 6}
\definecolor{softamber}{RGB}{254, 243, 199}
\definecolor{crimson}{RGB}{185, 28, 28}
\definecolor{softrose}{RGB}{255, 228, 230}
\definecolor{accentgreen}{RGB}{16, 120, 70}
\definecolor{softgreen}{RGB}{236, 253, 245}

\begin{document}
{BODY}
\end{document}
'''

def render_tikz(tikz_code, output_prefix):
    tex_path = f"{output_prefix}.tex"
    pdf_path = f"{output_prefix}.pdf"
    png_path = f"{output_prefix}.png"
    
    # remove figure environment if present for standalone
    clean_code = tikz_code.replace(r'\begin{figure}[htbp]', '').replace(r'\end{figure}', '')
    clean_code = clean_code.replace(r'\centering', '')
    # remove \caption and \label
    import re
    clean_code = re.sub(r'\\caption\{.*?\}', '', clean_code)
    clean_code = re.sub(r'\\label\{.*?\}', '', clean_code)
    
    full_tex = LATEX_TEMPLATE.replace('{BODY}', clean_code)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(full_tex)
    
    cwd = os.path.dirname(tex_path) or '.'
    base_tex = os.path.basename(tex_path)
    res = subprocess.run(['lualatex', '-interaction=nonstopmode', base_tex], cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error compiling {tex_path}:\n{res.stdout[-500:]}")
        return False
    
    # render to png
    cmd = ['pdftoppm', '-png', '-r', '150', os.path.basename(pdf_path), os.path.splitext(os.path.basename(png_path))[0]]
    subprocess.run(cmd, cwd=cwd, check=True)
    return True

if __name__ == '__main__':
    print("Helper script ready.")
