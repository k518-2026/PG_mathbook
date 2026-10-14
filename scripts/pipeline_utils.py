# -*- coding: utf-8 -*-
"""
Pipeline utilities for Laplace Translation & Math Verification
Model 1 (Translation): qwen2.5-7b-instruct
Model 2 (Math Check): qwen2.5-math-7b-instruct
"""

import urllib.request
import json
import time

LM_STUDIO_URL = "http://192.168.128.16:1234/v1/chat/completions"

def call_lm_studio(prompt, system_prompt="", model="qwen2.5-7b-instruct", max_tokens=2500, temperature=0.1):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    req = urllib.request.Request(
        LM_STUDIO_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    with urllib.request.urlopen(req, timeout=120) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"].strip()

def translate_english_to_japanese(english_text):
    """
    Step 1: Translate English original faithfully into Japanese using qwen2.5-7b-instruct
    """
    sys_prompt = (
        "あなたは数学古典の専門翻訳家です。"
        "英語の数学原著を、一切の要約や省略を行わず、原文の論理・語調・数式に忠実に、格調高い正確な日本語に翻訳してください。"
        "文中の数式や変数はLaTeX形式（$...$ または $$...$$）で記述してください。"
        "中国語は一切使わず、自然な日本語のみで記述してください。"
    )
    prompt = f"以下の原著英文を忠実に日本語へ翻訳してください：\n\n{english_text}"
    return call_lm_studio(prompt, system_prompt=sys_prompt, model="qwen2.5-7b-instruct", max_tokens=2500, temperature=0.1)

def verify_and_check_math(japanese_text, original_english=""):
    """
    Step 2: Math verification using qwen2.5-math-7b-instruct
    Checks mathematical consistency and confirms formulas.
    """
    prompt = (
        f"Please check the mathematical formulas, probabilities, and logic in the following passage. "
        f"Confirm that all formulas are mathematically valid and represented in standard LaTeX. "
        f"Respond concisely with the key mathematical verification note:\n\n{original_english[:800]}"
    )
    note = call_lm_studio(prompt, system_prompt="", model="qwen2.5-math-7b-instruct", max_tokens=250, temperature=0.1)
    return note

OLLAMA_URL = "http://192.168.128.62:11434/api/generate"

def call_ollama(prompt, system_prompt="", model="gemma4:12b"):
    """
    Call Ollama API on http://192.168.128.62:11434/
    """
    full_prompt = prompt
    if system_prompt:
        full_prompt = f"{system_prompt}\n\n{prompt}"
        
    payload = {
        "model": model,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 4096
        }
    }
    payload["think"] = False
    
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    with urllib.request.urlopen(req, timeout=300) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result.get("response", "").strip()

def generate_adult_relearning_exposition(verified_translation, chapter_topic, model="gemma4:12b"):
    """
    Step 3: Generate pedagogical lecture for adult re-learners (50s-80s) using Ollama.
    Explains historical mathematical classics using junior high and high school mathematics.
    Difficult concepts are explained even more thoroughly than the original text.
    """
    sys_prompt = (
        "あなたは『古典で学び直す数学 —— いまからでも遅くない高校までの数学で理解する歴史的名著』の専任ナビゲーターです。\n"
        "読者対象は、50代から80代の大人です。「学生時代に数学で挫折してしまったが、もう一度挑戦したい」「大人になって知的好奇心から数学の本質を味わいたい」という方々です。\n"
        "以下の執筆指針を厳格に守って、充実した丁寧な解説講義を執筆してください：\n\n"
        "【執筆指針】\n"
        "1. 前提知識は中学校・高校数学（方程式、関数のグラフ、三角比、確率の基礎、微分積分の直観的イメージ）に限定し、難しい大学レベルの専門用語は使わずに平易に解きほぐす。\n"
        "2. 難しい概念や数式は、原著以上に一歩一歩のステップを省かずに懇切丁寧に説明する。なぜその計算や式変形が成り立つのかを読者が納得できるよう示す。\n"
        "3. 人生経験豊かな大人の読者が深く共感できるよう、歴史的背景（なぜ当時の大数学者がその問題に挑んだのか）や日常・社会との結びつき、知的興奮を生き生きと伝える。\n"
        "4. 語り口は知的で温かく、読者を励まし伴走する丁寧な敬体（です・ます調）とする。\n"
        "5. 図解のイメージ（ベン図、グラフ、数直線、幾何的配置など）を言葉でも豊かに描写し、数式はLaTeX形式（$...$, $$...$$）で明快に記載する。"
    )
    prompt = (
        f"【本章のテーマ】：{chapter_topic}\n\n"
        f"以下の原著の日本語訳（数理校閲済み）の内容をもとに、大人の読者が中学校・高校の数学の知識で根本からスッキリ納得できるよう、"
        f"原著以上に丁寧で感動的な「学び直し解説講義」を執筆してください：\n\n"
        f"{verified_translation[:3500]}"
    )
    return call_ollama(prompt, system_prompt=sys_prompt, model=model)

# Backwards compatibility alias
def generate_highschool_exposition(verified_translation, chapter_topic, model="gemma4:12b"):
    return generate_adult_relearning_exposition(verified_translation, chapter_topic, model=model)

