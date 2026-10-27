import sys, os, json, re, urllib.request, time

TEX_PATH = r'E:\GoogleAntigravity\PG_mathbook\books\38769_hardy_pure_mathematics\hardy_pure_mathematics_translation.tex'
ENG_CLUSTERS_PATH = r'E:\GoogleAntigravity\PG_mathbook\books\38769_hardy_pure_mathematics\eng_clusters.json'
ENG_TRANSLATION_CACHE = r'E:\GoogleAntigravity\PG_mathbook\books\38769_hardy_pure_mathematics\eng_translations_cache.json'
CN_BLOCKS_PATH = r'E:\GoogleAntigravity\PG_mathbook\books\38769_hardy_pure_mathematics\cn_clusters.json'
CN_TRANSLATION_CACHE = r'E:\GoogleAntigravity\PG_mathbook\books\38769_hardy_pure_mathematics\cn_translations_cache.json'

URL = 'http://192.168.128.16:1234/v1/chat/completions'

def call_llm(prompt, max_tokens=2000):
    body = {
        'model': 'qwen2.5-7b-instruct',
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.1,
        'max_tokens': max_tokens
    }
    for attempt in range(4):
        try:
            req = urllib.request.Request(URL, data=json.dumps(body).encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=90) as res:
                data = json.loads(res.read().decode('utf-8'))
                ans = data['choices'][0]['message']['content'].strip()
                # Clean markdown quotes if model wraps in ```latex
                if ans.startswith('```latex'):
                    ans = ans[8:]
                elif ans.startswith('```'):
                    ans = ans[3:]
                if ans.endswith('```'):
                    ans = ans[:-3]
                return ans.strip()
        except Exception as e:
            print(f'Attempt {attempt+1} failed: {e}')
            time.sleep(5)
    raise RuntimeError('LLM failed after retries')

def translate_english_block(text):
    prompt = f'''あなたは純粋数学の名著 G. H. ハーディ『純粋数学教程』(A Course of Pure Mathematics) の日本語翻訳者です。
以下の英語の本文（LaTeX記法を含む）を、日本の標準的な大学高等数学の格調高く自然な日本語に翻訳してください。

【厳格な指示】
1. 中国語（簡体字や「如果」「我们」「我達」「并且」など）は絶対に混入させず、完全な現代日本語（「もし」「我々」「かつ」など）で記述してください。
2. 日本語環境で文字化けを起こす漢字は使わず、標準的なJIS漢字（常用漢字・人名用漢字）および現代日本語の数学用語（「稠密」「極限」「連続」「導関数」「積分」「級数」等）を使用してください。
3. 文頭に「Let us」や「Then」などの英語の断片を残さず、完全に日本語文として書き始めてください。
4. LaTeXの数式（$や\\(、\\[、マクロなど）は絶対に破壊せずそのまま維持してください。
5. 出力には説明や前置き、コードフェンス（```）は含めず、翻訳後のLaTeX本文のみを出力してください。

【翻訳対象】:
{text}'''
    return call_llm(prompt)

def rewrite_chinese_block(text):
    prompt = f'''あなたは純粋数学の名著 G. H. ハーディ『純粋数学教程』の日本語翻訳編集者です。
以下のテキストには中国語（簡体字や中国語表現：「如果」「我達」「并且」「称作」「线段」など）や日本語と中国語の混在が含まれています。
これを日本の標準的な大学高等数学の格調高く自然な完全な日本語に校閲・翻訳・書き直してください。

【厳格な指示】
1. 中国語（簡体字や「如果」「我们」「我達」「并且」「当〜时」「称作」等）を完全に排除し、標準的な現代日本語（「もし〜ならば」「我々は〜と呼ぶ」「かつ」「線分」「極大値」等）に修正してください。
2. 日本語環境で文字化け（□）の原因となる非日本語漢字（简、线、实、变、数、两、图、质、经、结、级など）はすべて正しい日本語文字（簡、線、実、変、数、2、図、質、経、結、級など）に置き換えてください。
3. LaTeXの数式（$や\\(、\\[、マクロなど）はそのまま維持してください。
4. 出力には前置きや解説、コードフェンスは含めず、修正後のLaTeX本文のみを出力してください。

【校閲対象テキスト】:
{text}'''
    return call_llm(prompt)

def run():
    # 1. Translate all English clusters
    with open(ENG_CLUSTERS_PATH, encoding='utf-8') as f:
        eng_clusters = json.load(f)
    
    eng_cache = {}
    if os.path.exists(ENG_TRANSLATION_CACHE):
        with open(ENG_TRANSLATION_CACHE, encoding='utf-8') as f:
            eng_cache = json.load(f)
    
    print(f'Processing {len(eng_clusters)} English clusters...')
    for c in eng_clusters:
        cid = str(c['id'])
        if cid in eng_cache:
            continue
        s_line = c['start_line']
        e_line = c['end_line']
        print(f'Translating EN cluster {cid}/{len(eng_clusters)} (lines {s_line}-{e_line})...')
        tr = translate_english_block(c['text'])
        # clean any accidental English starter like 'Let us then suppose that'
        if tr.startswith('Let us') or tr.startswith('Let '):
            tr = re.sub(r'^Let (us )?[a-zA-Z\s,]+(?:that )?', '', tr)
        eng_cache[cid] = tr
        with open(ENG_TRANSLATION_CACHE, 'w', encoding='utf-8') as f:
            json.dump(eng_cache, f, ensure_ascii=False, indent=2)
        print(f'  Saved EN cluster {cid}')
    
    # 2. Extract Chinese clusters from main text
    with open(TEX_PATH, encoding='utf-8') as f:
        lines = f.readlines()[:17818]
    
    non_cp_set = {'业', '两', '为', '么', '义', '书', '产', '仅', '你', '侧', '值', '偿', '关', '则', '创', '别', '剑', '协', '单', '卡', '历', '发', '变', '哪', '图', '圆', '处', '复', '实', '导', '尔', '带', '幂', '应', '开', '异', '张', '总', '您', '执', '报', '择', '换', '敛', '时', '权', '极', '构', '查', '标', '样', '桥', '检', '椭', '步', '每', '汇', '测', '涉', '现', '电', '确', '离', '种', '积', '穷', '简', '类', '紧', '级', '纯', '纸', '线', '组', '经', '结', '绘', '给', '统', '续', '联', '节', '虑', '规', '计', '认', '讨', '议', '记', '许', '论', '设', '访', '证', '识', '词', '试', '话', '该', '误', '说', '请', '读', '负', '质', '费', '赖', '趋', '轭', '载', '较', '边', '达', '过', '进', '连', '选', '释', '长', '问', '间', '顶', '项', '须', '领', '驱', '验', '骤'}
    
    cn_lines = []
    for idx, line in enumerate(lines):
        clean = re.sub(r'\\[a-zA-Z]+', '', line)
        has_non_cp = any(c in non_cp_set for c in line)
        has_cn_word = any(w in clean for w in ['我達', '如果', '并且', '称作', '线段', '极大值', '极小值', '换句话说', '在区间', '实部', '虚部', '共轭', '等价于', '两根', '单值', '量级', '读者はまた', '这', '显然'])
        if has_non_cp or has_cn_word:
            cn_lines.append(idx)
    
    cn_clusters = []
    curr = []
    for idx in cn_lines:
        if not curr or idx <= curr[-1] + 2:
            curr.append(idx)
        else:
            cn_clusters.append((curr[0], curr[-1]))
            curr = [idx]
    if curr:
        cn_clusters.append((curr[0], curr[-1]))
    
    cn_items = []
    for cid, (s, e) in enumerate(cn_clusters):
        cn_items.append({'id': cid+1, 'start_line': s+1, 'end_line': e+1, 'text': ''.join(lines[s:e+1])})
    
    with open(CN_BLOCKS_PATH, 'w', encoding='utf-8') as f:
        json.dump(cn_items, f, ensure_ascii=False, indent=2)
    print(f'Identified {len(cn_items)} Chinese clusters.')
    
    cn_cache = {}
    if os.path.exists(CN_TRANSLATION_CACHE):
        with open(CN_TRANSLATION_CACHE, encoding='utf-8') as f:
            cn_cache = json.load(f)
            
    for c in cn_items:
        cid = str(c['id'])
        if cid in cn_cache:
            continue
        s_line = c['start_line']
        e_line = c['end_line']
        print(f'Rewriting CN cluster {cid}/{len(cn_items)} (lines {s_line}-{e_line})...')
        tr = rewrite_chinese_block(c['text'])
        cn_cache[cid] = tr
        with open(CN_TRANSLATION_CACHE, 'w', encoding='utf-8') as f:
            json.dump(cn_cache, f, ensure_ascii=False, indent=2)
        print(f'  Saved CN cluster {cid}')

    print('All English and Chinese clusters processed!')

if __name__ == '__main__':
    run()
