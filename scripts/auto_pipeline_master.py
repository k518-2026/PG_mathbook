# -*- coding: utf-8 -*-
"""
Autonomous Master Pipeline for Project Gutenberg Math Classical Books (PG_mathbook).
Uses ONLY LM Studio API at http://192.168.128.16:1234/ (or http://localhost:1234/ when running directly on sff7020).
Automatically:
1. Verifies Python, Git, TeX Live (LuaLaTeX), and LM Studio models (qwen2.5-7b-instruct, qwen2.5-math-7b-instruct).
2. Pulls latest changes from GitHub.
3. Checks existing books and compiles any missing PDFs without overwriting curated TeX files.
4. Picks the next classic math book from book_queue.json, downloads Gutenberg text, runs:
   - Step 1 & 2: Full Original Translation + Math Verification -> LuaLaTeX -> PDF -> Git push
   - Step 3: Adult Re-learning Intro Book (12 chapters + TikZ + Glossary + Exercises) -> LuaLaTeX -> PDF -> Git push
5. Updates catalog.json, README.md, index.html, docs/index.html, and pushes to GitHub.
"""

import os
import re
import sys
import json
import time
import socket
import shutil
import argparse
import subprocess
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "scripts"))

from pipeline_utils import (
    resolve_lm_studio_base_url,
    call_lm_studio,
    translate_english_to_japanese,
    verify_and_check_math,
    generate_adult_relearning_exposition,
)
from safe_latex_cleaner import clean_text_for_latex
import manage_catalog

LOG_FILE = os.path.join(PROJECT_ROOT, "auto_pipeline.log")
ENV_STATUS_FILE = os.path.join(PROJECT_ROOT, "environment_status.json")
QUEUE_FILE = os.path.join(PROJECT_ROOT, "book_queue.json")
LOCK_FILE = os.path.join(PROJECT_ROOT, ".pipeline.lock")


def log(msg):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{timestamp} [{socket.gethostname()}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def acquire_lock(max_age_sec=7200):
    if os.path.exists(LOCK_FILE):
        try:
            age = time.time() - os.path.getmtime(LOCK_FILE)
            if age < max_age_sec:
                log(f"Another pipeline instance is already running (lock age: {int(age)}s). Exiting.")
                return False
        except Exception:
            pass
    try:
        with open(LOCK_FILE, "w", encoding="utf-8") as f:
            f.write(f"pid={os.getpid()} host={socket.gethostname()} time={time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    except Exception:
        pass
    return True


def release_lock():
    try:
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
    except Exception:
        pass


def ensure_tex_in_path():
    """Ensure TeX Live / LuaLaTeX and Git are in PATH even in minimal startup environments."""
    extra_paths = [
        r"C:\texlive\2026\bin\windows",
        r"C:\texlive\2025\bin\windows",
        r"C:\texlive\2024\bin\windows",
        r"C:\Program Files\Git\cmd",
        r"C:\Python314",
        r"C:\Python313",
        r"C:\Python312",
        os.path.expanduser(r"~\.lmstudio\bin"),
    ]
    current_path = os.environ.get("PATH", "")
    for p in extra_paths:
        if os.path.isdir(p) and p.lower() not in current_path.lower():
            current_path = p + os.pathsep + current_path
    os.environ["PATH"] = current_path


def run_cmd(cmd, cwd=PROJECT_ROOT, timeout=1800):
    log(f"Running: {cmd}")
    try:
        res = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        if res.returncode == 0:
            return True, res.stdout.strip()
        else:
            log(f"Command failed (code {res.returncode}): {res.stderr[:400]}")
            return False, res.stderr.strip()
    except Exception as e:
        log(f"Exception executing command: {e}")
        return False, str(e)


def try_start_local_lm_studio():
    """If running on the LM Studio host machine and server is not up yet, start LM Studio app and server via lms CLI."""
    lm_app_candidates = [
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\LM Studio\LM Studio.exe"),
        r"C:\Program Files\LM Studio\LM Studio.exe",
    ]
    for app_path in lm_app_candidates:
        if os.path.exists(app_path):
            ok_tl, out_tl = run_cmd('tasklist /FI "IMAGENAME eq LM Studio.exe"', timeout=10)
            if "LM Studio.exe" not in out_tl:
                log(f"Launching LM Studio application ({app_path})...")
                subprocess.Popen([app_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(12)
            break

    lms_exe = os.path.expanduser(r"~\.lmstudio\bin\lms.exe")
    if os.path.exists(lms_exe):
        log(f"Found local LM Studio CLI ({lms_exe}). Starting API server on 0.0.0.0:1234...")
        run_cmd(f'"{lms_exe}" server start --bind 0.0.0.0 --port 1234 --cors', timeout=30)


def wait_for_lm_studio(timeout_seconds=300, check_interval=10):
    candidates = [
        os.getenv("LM_STUDIO_HOST", "").rstrip("/"),
        "http://localhost:1234",
        "http://192.168.128.16:1234",
        "http://sff7020:1234",
    ]
    candidates = [c for c in candidates if c]
    log(f"Waiting for LM Studio API server ({candidates})...")
    start_time = time.time()
    tried_local_start = False

    while time.time() - start_time < timeout_seconds:
        for base in candidates:
            try:
                req = urllib.request.Request(f"{base}/v1/models")
                with urllib.request.urlopen(req, timeout=5) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode("utf-8"))
                        models = [m.get("id") for m in data.get("data", [])]
                        log(f"LM Studio is UP at {base}! Available models: {models}")
                        return base, models
            except Exception:
                continue

        if not tried_local_start:
            tried_local_start = True
            try_start_local_lm_studio()

        log(f"LM Studio not ready yet. Retrying in {check_interval}s...")
        time.sleep(check_interval)

    log(f"Timeout ({timeout_seconds}s) waiting for LM Studio.")
    return None, []


def verify_environment():
    ensure_tex_in_path()
    status = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "python": None,
        "git": None,
        "lualatex": None,
        "lm_studio_url": None,
        "lm_studio_models": [],
        "ready": False,
    }

    ok_py, out_py = run_cmd("python --version", timeout=15)
    status["python"] = out_py if ok_py else None

    ok_git, out_git = run_cmd("git --version", timeout=15)
    status["git"] = out_git if ok_git else None

    ok_tex, out_tex = run_cmd("lualatex --version", timeout=15)
    status["lualatex"] = out_tex.splitlines()[0] if (ok_tex and out_tex) else None

    base_url, models = wait_for_lm_studio(timeout_seconds=180, check_interval=8)
    status["lm_studio_url"] = base_url
    status["lm_studio_models"] = models
    status["ready"] = bool(status["python"] and status["git"] and status["lualatex"] and status["lm_studio_url"])

    try:
        with open(ENV_STATUS_FILE, "w", encoding="utf-8") as f:
            json.dump(status, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    log(f"Environment Verification: Python={status['python']} | Git={status['git']} | LuaLaTeX={status['lualatex']} | LM_Studio={status['lm_studio_url']}")
    return status


def git_sync_pull():
    log("Syncing latest repository from GitHub (git pull --rebase --autostash origin main)...")
    ok, _ = run_cmd("git pull --rebase --autostash origin main", timeout=120)
    if not ok:
        run_cmd("git rebase --abort", timeout=30)


def git_commit_and_push(message):
    log("Updating HTML Dashboard & README before commit...")
    run_cmd("python scripts/generate_html_dashboard.py", timeout=120)
    ok, st = run_cmd("git status --porcelain", timeout=60)
    if not ok or not st.strip():
        log("No changes to commit.")
        return True
    run_cmd("git add -A", timeout=60)
    run_cmd(f'git commit -m "{message}"', timeout=60)
    git_sync_pull()
    push_ok, _ = run_cmd("git push origin main", timeout=180)
    if push_ok:
        log(f"Successfully pushed to GitHub: {message}")
    else:
        log("WARNING: git push failed.")
    return push_ok


def compile_latex_book(book_dir, tex_name, force=False):
    abs_dir = os.path.join(PROJECT_ROOT, book_dir)
    tex_path = os.path.join(abs_dir, tex_name)
    pdf_name = os.path.splitext(tex_name)[0] + ".pdf"
    pdf_path = os.path.join(abs_dir, pdf_name)

    if not os.path.exists(tex_path):
        log(f"TeX file not found: {tex_path}")
        return False, 0

    if not force and os.path.exists(pdf_path):
        if os.path.getmtime(pdf_path) >= os.path.getmtime(tex_path) and os.path.getsize(pdf_path) > 50000:
            return True, get_pdf_pages(pdf_path)

    log(f"Compiling {tex_name} in {book_dir} with LuaLaTeX (2 passes)...")
    cmd = f"lualatex -interaction=nonstopmode -halt-on-error {tex_name}"
    ok1, _ = run_cmd(cmd, cwd=abs_dir, timeout=600)
    if not ok1:
        log(f"First pass failed for {tex_name}")
        return False, 0
    ok2, _ = run_cmd(cmd, cwd=abs_dir, timeout=600)
    if not ok2:
        log(f"Second pass failed for {tex_name}")
        return False, 0

    # Clean auxiliary files
    for ext in (".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"):
        aux_p = os.path.join(abs_dir, os.path.splitext(tex_name)[0] + ext)
        if os.path.exists(aux_p):
            try:
                os.remove(aux_p)
            except Exception:
                pass

    pages = get_pdf_pages(pdf_path)
    log(f"Compilation successful for {tex_name} ({pages} pages)")
    return True, pages


def get_pdf_pages(pdf_path):
    if not os.path.exists(pdf_path):
        return 0
    try:
        with open(pdf_path, "rb") as f:
            data = f.read()
        matches = re.findall(rb"/Type\s*/Page\b", data)
        return len(matches) if matches else 60
    except Exception:
        return 60


def strip_gutenberg_boilerplate(raw_text):
    start_markers = [
        "*** START OF THE PROJECT GUTENBERG EBOOK",
        "*** START OF THIS PROJECT GUTENBERG EBOOK",
        "***START OF THE PROJECT GUTENBERG EBOOK",
    ]
    end_markers = [
        "*** END OF THE PROJECT GUTENBERG EBOOK",
        "*** END OF THIS PROJECT GUTENBERG EBOOK",
        "***END OF THE PROJECT GUTENBERG EBOOK",
        "End of the Project Gutenberg EBook",
        "End of Project Gutenberg's",
    ]
    text = raw_text.replace("\r\n", "\n")
    for m in start_markers:
        idx = text.find(m)
        if idx != -1:
            nl = text.find("\n", idx)
            if nl != -1:
                text = text[nl + 1 :]
            break
    for m in end_markers:
        idx = text.find(m)
        if idx != -1:
            text = text[:idx]
            break
    return text.strip()


def extract_chapters_generic(clean_text):
    """Splits a Gutenberg math book into chapters/sections reliably."""
    # Remove LaTeX preamble if the Gutenberg txt is a TeX-derived plain text
    lines = clean_text.split("\n")
    chapters = []
    pattern = re.compile(
        r"^(?:CHAPTER|Chapter|SECTION|Section|PART|Part|ESSAY|Essay)\s+([IVXLCDM]+|\d+)(?:[\.\:\s—\-]+(.*))?$"
    )

    matches = []
    for idx, line in enumerate(lines):
        s = line.strip()
        m = pattern.match(s)
        if m:
            # Skip TOC lines that end with page numbers or leader dots
            if re.search(r"\.\.\.|\s+\d+$", s):
                continue
            matches.append((idx, m.group(1), (m.group(2) or "").strip()))

    # Filter out TOC duplicates: keep matches that have substantial text (>600 chars) before next match
    valid_matches = []
    for i, (line_idx, ch_num, ch_sub) in enumerate(matches):
        next_idx = matches[i + 1][0] if i + 1 < len(matches) else len(lines)
        body = "\n".join(lines[line_idx + 1 : next_idx]).strip()
        if len(body) >= 600:
            title = f"Chapter {ch_num}"
            if ch_sub:
                title += f": {ch_sub}"
            else:
                # Check next non-empty line for title
                for lookahead in range(line_idx + 1, min(line_idx + 5, next_idx)):
                    cand = lines[lookahead].strip()
                    if cand and len(cand) < 90:
                        title += f": {cand}"
                        break
            valid_matches.append((line_idx, title, body))

    if len(valid_matches) >= 3:
        for i, (_, title, body) in enumerate(valid_matches, start=1):
            chapters.append({"number": i, "title": title, "text": body, "length": len(body)})
        return chapters

    # Fallback: split into ~12000-character logical parts by double newline
    chunks = chunk_text(clean_text, max_len=12000)
    for i, ch_text in enumerate(chunks, start=1):
        chapters.append({
            "number": i,
            "title": f"Section {i}",
            "text": ch_text,
            "length": len(ch_text),
        })
    return chapters


def chunk_text(text, max_len=2000):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = []
    current_len = 0
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        p_len = len(p)
        if current_len + p_len > max_len and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = [p]
            current_len = p_len
        else:
            current_chunk.append(p)
            current_len += p_len
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    return chunks


def build_translation_tex(item, chapters, cache_data, tex_path):
    title_ja = item["translation_title_ja"]
    author_ja = item["author_ja"]
    orig_title = item["original_title"]
    gid = item["gutenberg_id"]

    preamble = rf"""\documentclass[a4paper,11pt,openany]{{ltjsbook}}
\usepackage{{luatexja}}
\usepackage{{luatexja-fontspec}}
\usepackage{{amsmath,amssymb,amsfonts,amsthm}}
\usepackage{{geometry}}
\geometry{{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}}
\usepackage{{tcolorbox}}
\tcbuselibrary{{skins,breakable}}
\usepackage{{hyperref}}
\usepackage{{fancyhdr}}

\definecolor{{primaryblue}}{{RGB}}{{20, 60, 110}}
\definecolor{{darkslate}}{{RGB}}{{35, 45, 60}}
\definecolor{{accentcrimson}}{{RGB}}{{160, 30, 45}}

\hypersetup{{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=darkslate,
    urlcolor=accentcrimson,
    pdftitle={{{title_ja}}},
    pdfauthor={{{author_ja}}}
}}

\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[LE,RO]{{\thepage}}
\fancyhead[RE]{{\leftmark}}
\fancyhead[LO]{{\rightmark}}
\setlength{{\headheight}}{{14pt}}
\renewcommand{{\headrulewidth}}{{0.4pt}}

\title{{
    {{\huge\bfseries\gtfamily {title_ja}}}\\[14pt]
    {{\large 原題：\textit{{{orig_title}}}}}\\[6pt]
    {{\normalsize Project Gutenberg eBook \#{gid}}}
}}
\author{{\textbf{{{author_ja}}} 著\\[4pt]教育情報分析研究会 訳・数学校閲}}
\date{{2026年10月 完全決定版}}

\begin{{document}}
\maketitle
\frontmatter
\tableofcontents
\clearpage
\mainmatter
"""
    body_parts = [preamble]
    for ch in chapters:
        num = ch["number"]
        key = f"Chapter_{num}"
        ch_entry = cache_data.get(key, {})
        ch_title_en = clean_text_for_latex(ch["title"])
        ja_text = ch_entry.get("japanese_translation", "")
        cleaned_ja = clean_text_for_latex(ja_text)
        body_parts.append(f"\n\\chapter{{第{num}章：{ch_title_en}}}\n\n{cleaned_ja}\n")

    body_parts.append("\n\\end{document}\n")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write("".join(body_parts))


def build_intro_book_via_lm_studio(item, chapters, cache_data, abs_book_dir, intro_tex_name):
    """Generates the Adult Re-learning Intro Book using ONLY LM Studio (http://192.168.128.16:1234/)."""
    intro_cache_path = os.path.join(abs_book_dir, f"{item['slug']}_intro_cache.json")
    intro_cache = {}
    if os.path.exists(intro_cache_path):
        try:
            with open(intro_cache_path, "r", encoding="utf-8") as f:
                intro_cache = json.load(f)
        except Exception:
            intro_cache = {}

    target_chapters = chapters[:12] if len(chapters) >= 12 else chapters
    for idx, ch in enumerate(target_chapters, start=1):
        key = f"Intro_{idx}"
        if key in intro_cache and intro_cache[key].get("lecture"):
            continue
        ch_key = f"Chapter_{ch['number']}"
        ja_source = cache_data.get(ch_key, {}).get("japanese_translation", ch["text"][:3000])
        log(f"[Intro Book #{item['gutenberg_id']}] Generating adult re-learning lecture {idx}/{len(target_chapters)}: {ch['title']}")
        lecture = generate_adult_relearning_exposition(ja_source, ch["title"])
        intro_cache[key] = {
            "number": idx,
            "title": ch["title"],
            "lecture": lecture,
        }
        with open(intro_cache_path, "w", encoding="utf-8") as f:
            json.dump(intro_cache, f, ensure_ascii=False, indent=2)

    title_ja = item["intro_title_ja"]
    orig_title = item["original_title"]
    gid = item["gutenberg_id"]
    intro_tex_path = os.path.join(abs_book_dir, intro_tex_name)

    preamble = rf"""\documentclass[a4paper,11pt,openany]{{ltjsbook}}
\usepackage{{luatexja}}
\usepackage{{luatexja-fontspec}}
\usepackage{{amsmath,amssymb,amsfonts,amsthm}}
\usepackage{{geometry}}
\geometry{{top=24mm,bottom=24mm,left=24mm,right=24mm,footskip=10mm}}
\usepackage{{tikz}}
\usepackage{{tcolorbox}}
\tcbuselibrary{{skins,breakable}}
\usepackage{{hyperref}}
\usepackage{{fancyhdr}}

\definecolor{{primaryblue}}{{RGB}}{{20, 60, 110}}
\definecolor{{softblue}}{{RGB}}{{238, 244, 252}}
\definecolor{{darkslate}}{{RGB}}{{35, 45, 60}}

\hypersetup{{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=darkslate,
    pdftitle={{{title_ja}}},
    pdfauthor={{教育情報分析研究会}}
}}

\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[LE,RO]{{\thepage}}
\fancyhead[RE]{{\leftmark}}
\fancyhead[LO]{{\rightmark}}
\setlength{{\headheight}}{{14pt}}
\renewcommand{{\headrulewidth}}{{0.4pt}}

\title{{
    {{\huge\bfseries\gtfamily {title_ja}}}\\[14pt]
    {{\large 底本：\textit{{{orig_title}}} (Project Gutenberg eBook \#{gid})}}
}}
\author{{\textbf{{教育情報分析研究会}} 編著}}
\date{{2026年10月}}

\begin{{document}}
\maketitle
\frontmatter
\tableofcontents
\clearpage
\mainmatter
"""
    parts = [preamble]
    for idx in range(1, len(target_chapters) + 1):
        entry = intro_cache.get(f"Intro_{idx}", {})
        ch_title = clean_text_for_latex(entry.get("title", f"第{idx}講"))
        lecture_clean = clean_text_for_latex(entry.get("lecture", ""))
        parts.append(f"\n\\chapter{{{ch_title}}}\n\n{lecture_clean}\n")

    parts.append("\n\\end{document}\n")
    with open(intro_tex_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))


def process_queued_book(item):
    gid = str(item["gutenberg_id"])
    slug = item["slug"]
    book_dir = item["book_dir"]
    abs_book_dir = os.path.join(PROJECT_ROOT, book_dir)
    os.makedirs(abs_book_dir, exist_ok=True)

    raw_txt_path = os.path.join(abs_book_dir, f"pg{gid}.txt")
    if not os.path.exists(raw_txt_path):
        url = item["gutenberg_txt_url"]
        log(f"Downloading Gutenberg eBook #{gid} from {url}...")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw_bytes = resp.read()
        with open(raw_txt_path, "wb") as f:
            f.write(raw_bytes)
        log(f"Downloaded {len(raw_bytes)} bytes to {raw_txt_path}")

    with open(raw_txt_path, "r", encoding="utf-8", errors="replace") as f:
        raw_text = f.read()

    chapters_json_path = os.path.join(abs_book_dir, f"{slug}_chapters.json")
    if os.path.exists(chapters_json_path):
        with open(chapters_json_path, "r", encoding="utf-8") as f:
            chapters = json.load(f)
    else:
        clean_txt = strip_gutenberg_boilerplate(raw_text)
        chapters = extract_chapters_generic(clean_txt)
        with open(chapters_json_path, "w", encoding="utf-8") as f:
            json.dump(chapters, f, ensure_ascii=False, indent=2)
        log(f"Extracted {len(chapters)} chapters for #{gid} ({item['original_title']}).")

    cache_path = os.path.join(abs_book_dir, f"{slug}_translation_cache.json")
    cache_data = {}
    if os.path.exists(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cache_data = json.load(f)
        except Exception:
            cache_data = {}

    chunks_translated_this_session = 0
    for i, ch in enumerate(chapters, start=1):
        num = ch["number"]
        key = f"Chapter_{num}"
        if key in cache_data and cache_data[key].get("japanese_translation"):
            continue

        chunks = chunk_text(ch["text"], max_len=2000)
        if key not in cache_data:
            cache_data[key] = {
                "number": num,
                "title_en": ch["title"],
                "length_en": ch["length"],
                "chunks_done": 0,
                "translation_pieces": [],
                "math_notes": [],
            }

        ch_state = cache_data[key]
        pieces = ch_state.get("translation_pieces", [])
        notes = ch_state.get("math_notes", [])
        start_idx = len(pieces)

        log(f"[#{gid} {item['original_title']}] Chapter {num}/{len(chapters)}: {ch['title']} (chunk {start_idx + 1}/{len(chunks)})")
        for c_idx in range(start_idx, len(chunks)):
            chunk = chunks[c_idx]
            log(f"  -> [Step 1: qwen2.5-7b-instruct] Translating Ch.{num} chunk {c_idx + 1}/{len(chunks)} ({len(chunk)} chars)...")
            ja_piece = translate_english_to_japanese(chunk)
            log(f"  -> [Step 2: qwen2.5-math-7b-instruct] Math review Ch.{num} chunk {c_idx + 1}/{len(chunks)}...")
            math_note = verify_and_check_math(ja_piece, chunk)

            pieces.append(ja_piece)
            notes.append(math_note)
            ch_state["translation_pieces"] = pieces
            ch_state["math_notes"] = notes
            ch_state["chunks_done"] = len(pieces)

            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)

            chunks_translated_this_session += 1

        ch_state["japanese_translation"] = "\n\n".join(pieces)
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)

        # Commit checkpoint after each completed chapter
        git_commit_and_push(f"chore(auto-pipeline): Checkpoint #{gid} Chapter {num}/{len(chapters)} translation")

    # Build and compile Original Translation PDF
    trans_tex_name = f"{slug}_translation.tex"
    trans_pdf_name = f"{slug}_translation.pdf"
    trans_tex_path = os.path.join(abs_book_dir, trans_tex_name)
    build_translation_tex(item, chapters, cache_data, trans_tex_path)
    ok_trans, trans_pages = compile_latex_book(book_dir, trans_tex_name, force=True)

    if ok_trans:
        manage_catalog.register_book({
            "gutenberg_id": gid,
            "original_title": item["original_title"],
            "original_author": item["original_author"],
            "japanese_title": item["translation_title_ja"],
            "author": f"{item['author_ja']} 著 / 教育情報分析研究会 訳・数学校閲",
            "category": item["category"],
            "language": "ja",
            "chapters_count": len(chapters),
            "pages": trans_pages,
            "status": "完成",
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%S+09:00"),
            "book_dir": book_dir,
            "tex_file": f"{book_dir}/{trans_tex_name}",
            "pdf_file": f"{book_dir}/{trans_pdf_name}",
            "model_used": "qwen2.5-7b-instruct (翻訳) & qwen2.5-math-7b-instruct (数理校閲) @ http://192.168.128.16:1234/",
            "compiler": "LuaLaTeX (LuaHBTeX / TeX Live 2026)",
            "description": f"Project Gutenberg eBook #{gid}収載の{item['author_ja']}『{item['original_title']}』全{len(chapters)}章を、qwen2.5-7b-instructによる原著直訳とqwen2.5-math-7b-instructによる数理校閲で完全製本した全訳学術書。",
            "gutenberg_url": item["gutenberg_url"],
        })
        git_commit_and_push(f"feat(auto-pipeline): Complete translation PDF for #{gid} ({item['original_title']})")

    # Build and compile Adult Re-learning Intro Book PDF
    intro_tex_name = f"{slug}_intro.tex"
    intro_pdf_name = f"{slug}_intro.pdf"
    build_intro_book_via_lm_studio(item, chapters, cache_data, abs_book_dir, intro_tex_name)
    ok_intro, intro_pages = compile_latex_book(book_dir, intro_tex_name, force=True)

    if ok_intro:
        manage_catalog.register_book({
            "gutenberg_id": f"{gid}-intro",
            "original_title": item["original_title"],
            "original_author": item["original_author"],
            "japanese_title": item["intro_title_ja"],
            "author": "教育情報分析研究会",
            "category": item["category"],
            "language": "ja",
            "chapters_count": min(12, len(chapters)),
            "pages": intro_pages,
            "status": "完成",
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%S+09:00"),
            "book_dir": book_dir,
            "tex_file": f"{book_dir}/{intro_tex_name}",
            "pdf_file": f"{book_dir}/{intro_pdf_name}",
            "model_used": "qwen2.5-7b-instruct & qwen2.5-math-7b-instruct @ http://192.168.128.16:1234/",
            "compiler": "LuaLaTeX (LuaHBTeX / TeX Live 2026)",
            "description": f"Project Gutenberg eBook #{gid}収載の{item['author_ja']}『{item['original_title']}』を底本に、大人の学び直しの読者に向けて高校数学の範囲で原著以上に懇切丁寧に解き明かす入門書。",
            "gutenberg_url": item["gutenberg_url"],
        })
        git_commit_and_push(f"feat(auto-pipeline): Complete intro book PDF for #{gid}-intro ({item['intro_title_ja']})")

    return ok_trans and ok_intro


def run_all_pipelines(check_only=False):
    log("=== STARTING MATH CLASSICAL BOOKS AUTO-PIPELINE ===")

    env = verify_environment()
    if check_only:
        log("Check-only mode completed.")
        return env["ready"]

    if not env["ready"]:
        log("Environment not fully ready (missing LM Studio or TeX/Python/Git). Exiting.")
        return False

    git_sync_pull()

    # 1. Ensure all already-cataloged books have compiled PDFs (without overwriting curated .tex files)
    catalog = manage_catalog.load_catalog()
    for b in catalog.get("books", []):
        bdir = b.get("book_dir")
        tfile = b.get("tex_file")
        if bdir and tfile:
            tex_name = os.path.basename(tfile)
            compile_latex_book(bdir, tex_name, force=False)

    # 2. Check autonomous book_queue.json for pending books
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            qdata = json.load(f)
        for item in qdata.get("queue", []):
            gid = str(item["gutenberg_id"])
            if manage_catalog.is_duplicate(gid) and manage_catalog.is_duplicate(f"{gid}-intro"):
                item["status"] = "completed"
                continue

            log(f"=== Starting Autonomous Processing for Queued Book #{gid}: {item['original_title']} ===")
            item["status"] = "in_progress"
            with open(QUEUE_FILE, "w", encoding="utf-8") as f:
                json.dump(qdata, f, ensure_ascii=False, indent=2)
            git_commit_and_push(f"chore(startup): Auto-pipeline started on {socket.gethostname()} for eBook #{gid}")

            done = process_queued_book(item)
            if done:
                item["status"] = "completed"
                with open(QUEUE_FILE, "w", encoding="utf-8") as f:
                    json.dump(qdata, f, ensure_ascii=False, indent=2)
                git_commit_and_push(f"chore(queue): Mark eBook #{gid} as completed in book_queue.json")
            # Process 1 full queued book pair per boot cycle
            break

    git_commit_and_push(f"Auto-pipeline sync: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    log("=== AUTO-PIPELINE COMPLETED SUCCESSFULLY ===")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true", help="Only verify environment and exit")
    args = parser.parse_args()

    if args.check_only:
        run_all_pipelines(check_only=True)
    else:
        if acquire_lock():
            try:
                run_all_pipelines(check_only=False)
            finally:
                release_lock()
