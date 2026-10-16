import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = 'e:/GoogleAntigravity/PG_mathbook'
CATALOG_PATH = os.path.join(ROOT_DIR, 'catalog.json')

def load_catalog():
    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_html():
    cat = load_catalog()
    books = cat.get("books", [])

    # Group books by base Gutenberg ID
    groups = {}
    order = []
    for b in books:
        gid = b.get("gutenberg_id", "")
        base_id = gid.split("-")[0]
        if base_id not in groups:
            groups[base_id] = {
                "base_id": base_id,
                "original_title": b.get("original_title", ""),
                "original_author": b.get("original_author", ""),
                "gutenberg_url": b.get("gutenberg_url", f"https://www.gutenberg.org/ebooks/{base_id}"),
                "books": []
            }
            order.append(base_id)
        if b.get("original_title"):
            groups[base_id]["original_title"] = b.get("original_title")
        if b.get("original_author"):
            groups[base_id]["original_author"] = b.get("original_author")
        groups[base_id]["books"].append(b)

    cards_html = ""
    for base_id in order:
        group = groups[base_id]
        orig_title = group["original_title"]
        orig_author = group["original_author"]
        gutenberg_url = group["gutenberg_url"]
        b_list = group["books"]

        # Aggregate searchable text
        search_terms = [base_id, orig_title, orig_author]
        for b in b_list:
            search_terms.extend([
                b.get("japanese_title", ""),
                b.get("author", ""),
                b.get("description", ""),
                b.get("model_used", "")
            ])
        search_attr = " ".join(search_terms).replace('"', '&quot;')

        sections_html = ""

        if len(b_list) >= 2:
            full_trans = next((b for b in b_list if "-intro" not in b.get("gutenberg_id", "")), b_list[0])
            intro_book = next((b for b in b_list if "-intro" in b.get("gutenberg_id", "")), b_list[1])

            sections_html = f"""
        <div class="edition-grid">
          <!-- 原著日本語訳・数学校閲版 -->
          <div class="edition-panel edition-academic">
            <div class="edition-badge-bar">
              <span class="badge badge-academic">原著日本語全訳・数学校閲版</span>
              <span class="badge badge-pages">{full_trans.get("chapters_count", "-")}章 / {full_trans.get("pages", "-")}頁</span>
            </div>
            <h3 class="edition-title">{full_trans.get("japanese_title", "")}</h3>
            <div class="edition-author"><span class="label">訳・校閲：</span>{full_trans.get("author", "")}</div>
            <p class="edition-desc">{full_trans.get("description", "")}</p>
            <div class="engine-info">
              <span class="engine-tag">⚡ {full_trans.get("model_used", "")}</span>
            </div>
            <div class="card-actions">
              <a href="{full_trans.get("pdf_file", "")}" class="btn btn-pdf" target="_blank">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                PDF全訳版を読む ({full_trans.get("pages", "-")}P)
              </a>
              <a href="{full_trans.get("tex_file", "")}" class="btn btn-tex" target="_blank">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                TeX原稿ソース
              </a>
            </div>
          </div>

          <!-- 古典で学び直す大人のための入門書 -->
          <div class="edition-panel edition-highschool">
            <div class="edition-badge-bar">
              <span class="badge badge-highschool">大人のための学び直し入門書</span>
              <span class="badge badge-pages">{intro_book.get("chapters_count", "-")}章 / {intro_book.get("pages", "-")}頁</span>
            </div>
            <h3 class="edition-title">{intro_book.get("japanese_title", "")}</h3>
            <div class="edition-author"><span class="label">編著・解説：</span>{intro_book.get("author", "")}</div>
            <p class="edition-desc">{intro_book.get("description", "")}</p>
            <div class="engine-info">
              <span class="engine-tag">⚡ {intro_book.get("model_used", "")}</span>
            </div>
            <div class="card-actions">
              <a href="{intro_book.get("pdf_file", "")}" class="btn btn-pdf btn-hs" target="_blank">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                PDF学び直し版を読む ({intro_book.get("pages", "-")}P)
              </a>
              <a href="{intro_book.get("tex_file", "")}" class="btn btn-tex" target="_blank">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                TeX原稿ソース
              </a>
            </div>
          </div>
        </div>
"""
        else:
            # Single book in this group (e.g. Poincare, Venn, Boole, Carroll, Thompson)
            b = b_list[0]
            is_combined = ("解説付" in b.get("japanese_title", "") or "全Steps" in b.get("description", "") or "Step 3" in b.get("description", ""))
            
            badge_type_html = ""
            if is_combined:
                badge_type_html = '<span class="badge badge-combined">原著全訳 ＋ 数学校閲 ＋ 大人のための丁寧な解説講義（合本集成版）</span>'
            else:
                badge_type_html = '<span class="badge badge-highschool">古典で学び直す数学入門書</span>'

            sections_html = f"""
        <div class="edition-single">
          <div class="edition-panel {'edition-combined' if is_combined else 'edition-highschool'}">
            <div class="edition-badge-bar">
              {badge_type_html}
              <span class="badge badge-pages">{b.get("chapters_count", "-")}章 / {b.get("pages", "-")}頁</span>
              <span class="badge badge-author">{b.get("author", "")}</span>
            </div>
            <h3 class="edition-title">{b.get("japanese_title", "")}</h3>
            <p class="edition-desc">{b.get("description", "")}</p>
            <div class="engine-info">
              <span class="engine-tag">⚡ {b.get("model_used", "")}</span>
            </div>
            <div class="card-actions">
              <a href="{b.get("pdf_file", "")}" class="btn btn-pdf" target="_blank">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                PDF製本版を読む ({b.get("pages", "-")}P)
              </a>
              <a href="{b.get("tex_file", "")}" class="btn btn-tex" target="_blank">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                TeX原稿ソース
              </a>
            </div>
          </div>
        </div>
"""

        cards_html += f"""
      <article class="work-box" data-search="{search_attr}">
        <!-- 原著マスターヘッダー（同じ枠の最上部） -->
        <header class="work-header">
          <div class="work-header-top">
            <span class="work-id-badge">Project Gutenberg #{base_id}</span>
            <span class="work-editions-count">収録エディション: {len(b_list)} 版</span>
          </div>
          <div class="work-original-hero">
            <div class="hero-left">
              <span class="hero-label">原著（一次資料）：</span>
              <a href="{gutenberg_url}" target="_blank" rel="noopener noreferrer" class="orig-hero-link" title="Project Gutenberg で原著テキストを直接閲覧">
                <strong class="orig-hero-title">{orig_title}</strong>
                <span class="orig-hero-author">({orig_author})</span>
                <svg class="icon-ext" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              </a>
            </div>
            <a href="{gutenberg_url}" target="_blank" rel="noopener noreferrer" class="btn-gutenberg-pill">
              Gutenberg原著を開く ↗
            </a>
          </div>
        </header>

        <!-- 原著と大人の学び直し本を統合収容するボディ -->
        <div class="work-body">
{sections_html}
        </div>
      </article>
"""

    html = f"""<!DOCTYPE html>
<html lang="ja" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>古典で学び直す数学 | いまからでも遅くない高校までの数学で理解する歴史的名著</title>
  <meta name="description" content="50代から80代の大人へ贈る数学学び直しライブラリ。昔数学で挫折してしまった方や知的好奇心に燃える大人のために、Project Gutenbergの古典原典を中学校・高校数学で原著以上に丁寧に解き明かします。" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <div class="site-badge">REDISCOVERING MATHEMATICS THROUGH CLASSICS</div>
      <h1 class="site-title">古典で学び直す数学</h1>
      <p class="site-subtitle">
        —— <strong>いまからでも遅くない、高校までの数学で理解する歴史的名著</strong> ——<br>
        「学生のころ数学に挫折してしまった」「大人になった今だからこそ、数学の奥深い美しさを味わいたい」<br>
        50代〜80代の読者に向けて、人類の知的至宝（ラプラス、ポアンカレ、ヴェン、ブール、キャロル、トンプソン）を
        <strong>中学校・高校で習う数学だけを使って、原著以上に一歩一歩丁寧に解き明かす</strong>大人のためのオープン数学ライブラリです。<br>
        各枠の最上部にある<strong>「Gutenberg原著を開く」</strong>から、いつでも英語・仏語の一次資料へ立ち返ることができます。
      </p>
      <div class="meta-strip">
        <span class="strip-pill">対象読者：<strong>50代〜80代・大人の学び直し</strong></span>
        <span class="strip-pill">前提知識：<strong>中学校・高校までの数学</strong></span>
        <span class="strip-pill">収録古典：<strong>{len(groups)}</strong> 作品（全 <strong>{len(books)}</strong> 冊）</span>
        <span class="strip-pill">組版：<strong>LuaLaTeX (TeX Live 2026 / TikZ図版多数)</strong></span>
        <span class="strip-pill">重複管理：<strong>catalog.json 連携済み</strong></span>
      </div>
    </div>
  </header>

  <main class="container">
    <section class="toolbar">
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="search" id="searchInput" placeholder="古典原著名・タイトル・著者・数学テーマで検索..." oninput="filterBooks()" />
      </div>
      <div class="toolbar-actions">
        <span id="matchCount" class="match-badge">全 {len(groups)} 作品表示中</span>
        <button class="theme-toggle-btn" onclick="toggleTheme()" id="themeBtn" aria-label="テーマ切替">🌙 ダーク表示</button>
      </div>
    </section>

    <!-- 原著と学び直し本が同じ枠に入る統合グリッド -->
    <section class="works-container" id="worksContainer">
{cards_html}
    </section>

    <section class="info-section">
      <h2>📚 『古典で学び直す数学』の基本理念</h2>
      <p>
        数学は、若い学生だけの試験勉強の道具ではありません。むしろ、人生経験を積んだ大人だからこそ、
        「なぜ確率という不確実なものを人間は計算しようとしたのか」「記号論理はなぜコンピュータを生み出したのか」「無限小とは一体何なのか」という
        問いの深さと、それを乗り越えた先人たちの思考の美しさに心から感動できるはずです。
      </p>
      <p>
        本ライブラリでは、大学レベルの難解な専門用語を振りかざすのではなく、
        <strong>「中学校や高校で誰もが一度は目にしたことのある数式やグラフ（1次・2次関数、方程式、確率、図形）」</strong>だけを道具として用います。
        難解な概念ほどステップを省略せず、原著以上に懇切丁寧に図解（TikZ）と例題を交えて解説しています。
      </p>
      <p>
        書籍の追加・更新は <code>catalog.json</code> を通じて厳格に重複判定され、同一 Gutenberg ID の二重登録を防止しています。
        すべての作品枠に Project Gutenberg の原典への直リンクを備え、学び直しの旅をどこまでも深く楽しんでいただけます。
      </p>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <p>&copy; 2026 <strong>教育情報分析研究会</strong> (Educational Information Analysis Study Group)</p>
      <p>古典で学び直す数学シリーズ —— Project Gutenberg パブリックドメイン数学古典集成</p>
      <p>Source Repository: <a href="https://github.com/k518-2026/PG_mathbook" target="_blank" rel="noopener noreferrer">https://github.com/k518-2026/PG_mathbook</a></p>
    </div>
  </footer>

  <script>
    function filterBooks() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const boxes = document.querySelectorAll('.work-box');
      let count = 0;
      boxes.forEach(box => {{
        const searchData = box.getAttribute('data-search').toLowerCase();
        if (!query || searchData.includes(query)) {{
          box.style.display = '';
          count++;
        }} else {{
          box.style.display = 'none';
        }}
      }});
      document.getElementById('matchCount').textContent = `全 ${{boxes.length}} 作品中 ${{count}} 作品表示中`;
    }}

    function toggleTheme() {{
      const html = document.documentElement;
      const current = html.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      const btn = document.getElementById('themeBtn');
      btn.textContent = next === 'dark' ? '☀️ ライト表示' : '🌙 ダーク表示';
      localStorage.setItem('theme', next);
    }}

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {{
      document.documentElement.setAttribute('data-theme', savedTheme);
      document.getElementById('themeBtn').textContent = savedTheme === 'dark' ? '☀️ ライト表示' : '🌙 ダーク表示';
    }}
  </script>
</body>
</html>
"""

    # Write to root index.html
    root_index = os.path.join(ROOT_DIR, 'index.html')
    with open(root_index, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {root_index}")

    # Write to docs/index.html (for GitHub Pages)
    docs_dir = os.path.join(ROOT_DIR, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    docs_index = os.path.join(docs_dir, 'index.html')
    # in docs/, adjust relative paths to books/
    docs_html = html.replace('href="books/', 'href="../books/').replace('href="style.css"', 'href="../style.css"')
    with open(docs_index, 'w', encoding='utf-8') as f:
        f.write(docs_html)
    print(f"Generated {docs_index}")

if __name__ == '__main__':
    generate_html()
