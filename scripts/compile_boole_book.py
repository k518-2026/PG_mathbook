import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

BOOK_DIR = 'e:/GoogleAntigravity/PG_mathbook/books/15114_boole_laws_of_thought'
TEX_NAME = 'boole_laws_of_thought_intro.tex'
PDF_NAME = 'boole_laws_of_thought_intro.pdf'

def compile_pdf():
    print(f"Compiling {TEX_NAME} with LuaLaTeX (Pass 1)...")
    res1 = subprocess.run(
        ['lualatex', '--interaction=nonstopmode', TEX_NAME],
        cwd=BOOK_DIR,
        capture_output=True,
        encoding='utf-8',
        errors='ignore'
    )
    print("Pass 1 returncode:", res1.returncode)
    if res1.returncode != 0:
        print("Pass 1 errors (last 30 lines):")
        print('\n'.join(res1.stdout.splitlines()[-30:]))
        return False
        
    print(f"Compiling {TEX_NAME} with LuaLaTeX (Pass 2 for TOC/Hyperref)...")
    res2 = subprocess.run(
        ['lualatex', '--interaction=nonstopmode', TEX_NAME],
        cwd=BOOK_DIR,
        capture_output=True,
        encoding='utf-8',
        errors='ignore'
    )
    print("Pass 2 returncode:", res2.returncode)
    
    pdf_path = os.path.join(BOOK_DIR, PDF_NAME)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"Successfully generated PDF: {pdf_path} ({size_kb:.1f} KB)")
        return True
    else:
        print("Error: PDF not found!")
        return False

if __name__ == '__main__':
    compile_pdf()
