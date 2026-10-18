# -*- coding: utf-8 -*-
import sys, json, time, os

sys.path.insert(0, 'scripts')
import manage_catalog

item = {
    'gutenberg_id': '41568',
    'slug': 'whitehead_intro_mathematics',
    'book_dir': 'books/41568_whitehead_intro_mathematics',
    'original_title': 'An Introduction to Mathematics',
    'original_author': 'Alfred North Whitehead',
    'author_ja': 'アルフレッド・ノース・ホワイトヘッド',
    'translation_title_ja': '数学入門 —— 抽象の力と数理的思考の体系（原著全17章 完全翻訳・数学校閲版）',
    'intro_title_ja': '古典で学び直すホワイトヘッド数学入門',
    'category': 'Mathematics & Philosophy of Science (Project Gutenberg eBook #41568)',
    'gutenberg_url': 'https://www.gutenberg.org/ebooks/41568'
}

manage_catalog.register_book({
    'gutenberg_id': '41568',
    'original_title': item['original_title'],
    'original_author': item['original_author'],
    'japanese_title': item['translation_title_ja'],
    'author': f"{item['author_ja']} 著 / 教育情報分析研究会 訳・数学校閲",
    'category': item['category'],
    'language': 'ja',
    'chapters_count': 17,
    'pages': 60,
    'status': '完成',
    'created_at': time.strftime('%Y-%m-%dT%H:%M:%S+09:00'),
    'book_dir': item['book_dir'],
    'tex_file': f"{item['book_dir']}/whitehead_intro_mathematics_translation.tex",
    'pdf_file': f"{item['book_dir']}/whitehead_intro_mathematics_translation.pdf",
    'model_used': 'qwen2.5-7b-instruct (翻訳) & qwen2.5-math-7b-instruct (数理校閲) @ http://192.168.128.16:1234/',
    'compiler': 'LuaLaTeX (LuaHBTeX / TeX Live 2026)',
    'description': 'Project Gutenberg eBook #41568収載のアルフレッド・ノース・ホワイトヘッド『An Introduction to Mathematics』全17章を、qwen2.5-7b-instructによる原著直訳とqwen2.5-math-7b-instructによる数理校閲で完全製本した全訳学術書。',
    'gutenberg_url': item['gutenberg_url']
})

with open('book_queue.json', 'r', encoding='utf-8') as f:
    qdata = json.load(f)
for it in qdata.get('queue', []):
    if str(it.get('gutenberg_id')) == '41568':
        it['status'] = 'completed'
with open('book_queue.json', 'w', encoding='utf-8') as f:
    json.dump(qdata, f, ensure_ascii=False, indent=2)

print('Registered 41568 translation and marked queue completed.')
