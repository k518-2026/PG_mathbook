import json
import os
import re

cat = json.load(open(r"E:\GoogleAntigravity\PG_mathbook\catalog.json", encoding="utf-8"))

def convert_markdown_stars(text):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        stripped = line.strip()
        # skip TeX comments
        if stripped.startswith("%"):
            new_lines.append(line)
            continue
        
        # Replace **word** with \textbf{word}
        # Be careful not to cross lines or break math
        # Pattern: \*\*(.*?)\*\*
        line_mod = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', line)
        new_lines.append(line_mod)
    return "\n".join(new_lines)

modified_files = set()

# Process all .tex files registered in catalog or in recent books
for b in cat["books"]:
    tfile = b.get("tex_file")
    if not tfile:
        continue
    fpath = os.path.join(r"E:\GoogleAntigravity\PG_mathbook", tfile)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    
    # check if non-comment ** exists
    has_stars = False
    for l in content.split("\n"):
        if not l.strip().startswith("%") and "**" in l:
            has_stars = True
            break
            
    if has_stars:
        new_content = convert_markdown_stars(content)
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        modified_files.add(fpath)
        print(f"Fixed markdown stars in: {tfile}")

# Also check any sub-tex files like in 55264
for root, dirs, files in os.walk(r"E:\GoogleAntigravity\PG_mathbook\books"):
    # skip raw gutenberg extraction folders like 13702-t
    if "-t" in root or "raw" in root:
        continue
    for f in files:
        if f.endswith(".tex") and not f.startswith("pg") and not "-t" in f:
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
            has_stars = False
            for l in content.split("\n"):
                if not l.strip().startswith("%") and "**" in l:
                    has_stars = True
                    break
            if has_stars and fpath not in modified_files:
                new_content = convert_markdown_stars(content)
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                modified_files.add(fpath)
                print(f"Fixed markdown stars in subfile: {os.path.relpath(fpath, r'E:\GoogleAntigravity\PG_mathbook')}")

print(f"Total files updated: {len(modified_files)}")
