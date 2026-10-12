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

    cards_html = ""
    for b in books:
        b_id = b.get("gutenberg_id", "")
        orig_title = b.get("original_title", "")
        orig_author = b.get("original_author", "")
        jp_title = b.get("japanese_title", "")
        author = b.get("author", "教育情報分析研究会")
        gutenberg_url = b.get("gutenberg_url", f"https://www.gutenberg.org/ebooks/{b_id}")
        pages = b.get("pages", "-")
        chapters = b.get("chapters_count", "-")
        model = b.get("model_used", "")
        desc = b.get("description", "")
        tex_path = b.get("tex_file", "")
        pdf_path = b.get("pdf_file", "")

        cards_html += f"""
      <div class="book-card" data-search="{jp_title} {orig_title} {orig_author} {author} {b_id} {desc}">
        <div class="card-header">
          <span class="badge badge-id">Gutenberg #{b_id}</span>
          <span class="badge badge-pages">{chapters}章 / {pages}頁</span>
          <span class="badge badge-author">{author}</span>
        </div>
        <h2 class="book-title">{jp_title}</h2>
        <div class="original-meta">
          <span class="label">原著：</span>
          <a href="{gutenberg_url}" target="_blank" rel="noopener noreferrer" class="orig-link" title="Project Gutenbergで原著を見る">
            <strong>{orig_title}</strong> <span>({orig_author})</span>
            <svg class="icon-ext" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
        </div>
        <p class="book-desc">{desc}</p>
        <div class="engine-info">
          <span class="engine-tag">⚡ 生成エンジン: {model}</span>
        </div>
        <div class="card-actions">
          <a href="{pdf_path}" class="btn btn-pdf" target="_blank">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            PDF製本版を読む ({pages}P)
          </a>
          <a href="{tex_path}" class="btn btn-tex" target="_blank">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            TeX原稿ソース
          </a>
        </div>
      </div>
"""

    html = f"""<!DOCTYPE html>
<html lang="ja" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PG_mathbook | 高校生のための古典数学入門ライブラリ</title>
  <meta name="description" content="Project Gutenberg の数学古典から高校生向けの本格的な確率・統計・論理入門書を編纂・製本するプロジェクト。原著リンク付き目録。" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <div class="site-badge">PROJECT GUTENBERG CLASSIC MATH SERIES</div>
      <h1 class="site-title">高校生のための古典数学入門ライブラリ</h1>
      <p class="site-subtitle">
        Project Gutenberg（Bookshelf 672）収載の歴史的名著をもとに、高校生に向けて執筆・製本された数学入門書コレクション。<br>
        すべての書籍の「原著名」をクリックすると、<strong>Project Gutenbergの原著ページ</strong>を直接閲覧・検証できます。
      </p>
      <div class="meta-strip">
        <span class="strip-pill">編著者：<strong>教育情報分析研究会</strong></span>
        <span class="strip-pill">収録作品：<strong>{len(books)}</strong> 冊</span>
        <span class="strip-pill">組版：<strong>LuaLaTeX (LuaHBTeX / TeX Live 2026)</strong></span>
        <span class="strip-pill">重複管理：<strong>catalog.json 連携済み</strong></span>
      </div>
    </div>
  </header>

  <main class="container">
    <section class="toolbar">
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="search" id="searchInput" placeholder="タイトル・原著名・著者・キーワードで検索..." oninput="filterBooks()" />
      </div>
      <div class="toolbar-actions">
        <span id="matchCount" class="match-badge">全 {len(books)} 件表示中</span>
        <button class="theme-toggle-btn" onclick="toggleTheme()" id="themeBtn" aria-label="テーマ切替">🌙 ダーク表示</button>
      </div>
    </section>

    <section class="books-grid" id="booksGrid">
{cards_html}
    </section>

    <section class="info-section">
      <h2>📚 プロジェクトの理念と重複管理について</h2>
      <p>
        本ライブラリは、18〜19世紀の偉大な数学者たち（ラプラス、ジョン・ヴェン、ジョージ・ブール）が著したパブリックドメインの原典を底本とし、現代の高校生が「論理・確率・統計」の本質を直感と数式の両面から深く学べるよう、教育情報分析研究会が編纂・組版したものです。
      </p>
      <p>
        書籍の追加・更新は <code>catalog.json</code> を通じて厳格に重複判定され、同一 Gutenberg ID の二重登録を防止しています。また、すべての原著名には原著（Project Gutenberg EBook）への直リンクを配備し、いつでも一次資料へと立ち返ることができるオープンな数学教育環境を提供しています。
      </p>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <p>&copy; 2026 <strong>教育情報分析研究会</strong> (Educational Information Analysis Study Group)</p>
      <p>Source Repository: <a href="https://github.com/k518-2026/PG_mathbook" target="_blank" rel="noopener noreferrer">https://github.com/k518-2026/PG_mathbook</a></p>
    </div>
  </footer>

  <script>
    function filterBooks() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.book-card');
      let count = 0;
      cards.forEach(card => {{
        const searchData = card.getAttribute('data-search').toLowerCase();
        if (!query || searchData.includes(query)) {{
          card.style.display = '';
          count++;
        }} else {{
          card.style.display = 'none';
        }}
      }});
      document.getElementById('matchCount').textContent = `全 ${{cards.length}} 件中 ${{count}} 件表示中`;
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
