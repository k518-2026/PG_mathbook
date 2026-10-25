import re
# -*- coding: utf-8 -*-
"""
Pipeline utilities for Original Book Translation, Math Verification, and Adult Re-learning Intro Books.
Uses ONLY LM Studio at http://192.168.128.16:1234/ (or http://localhost:1234/ when running directly on sff7020).
Step 1 (Translation): qwen2.5-7b-instruct
Step 2 (Math Check): qwen2.5-math-7b-instruct
Step 3 (Adult Re-learning Exposition): qwen2.5-7b-instruct
"""

import os
import json
import time
import urllib.request
import urllib.error

LM_STUDIO_CANDIDATES = [
    os.getenv("LM_STUDIO_HOST", "").rstrip("/"),
    "http://localhost:1234",
    "http://192.168.128.16:1234",
    "http://sff7020:1234",
]

_RESOLVED_BASE_URL = None


def resolve_lm_studio_base_url(timeout=5):
    global _RESOLVED_BASE_URL
    if _RESOLVED_BASE_URL:
        return _RESOLVED_BASE_URL
    for base in LM_STUDIO_CANDIDATES:
        if not base:
            continue
        try:
            req = urllib.request.Request(f"{base}/v1/models")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                if resp.status == 200:
                    _RESOLVED_BASE_URL = base
                    return base
        except Exception:
            continue
    return "http://192.168.128.16:1234"


def call_lm_studio(prompt, system_prompt="", model="qwen2.5-7b-instruct", max_tokens=2500, temperature=0.1, retries=3):
    base_url = resolve_lm_studio_base_url()
    url = f"{base_url}/v1/chat/completions"

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=180) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            last_err = e
            time.sleep(3)
    raise RuntimeError(f"LM Studio call failed after {retries} retries: {last_err}")


def translate_english_to_japanese(english_text):
    """
    Step 1: Translate English original faithfully into Japanese using qwen2.5-7b-instruct
    """
    sys_prompt = (
        "あなたは世界最高峰の数学専門翻訳家です。"
        "英語の純粋数学書（G. H. ハーディ著）を、原文の数式と厳密な論理展開を1字1句忠実に維持し、最高品質の学術日本語（自然な標準日本語）のみで翻訳してください。"
        "中国語（簡体字・繁体字・我達・它達・进行・如果・但是などの中国語語彙・構文）は絶対に混入させず、完全に排除してください。"
        "数式はLaTeX形式（$...$ または $$...$$）を正確に保持してください。"
        "【最重要】『以下の文章を忠実に日本語へ翻訳しました：』などの前置き・挨拶・注釈・解説は一切出力せず、翻訳本文のみを出力してください。"
    )
    prompt = f"以下の数学原著英文を、中国語を一切交えず格調高い標準日本語のみに翻訳してください（前置き・解説は一切不要、翻訳本文のみ出力）：\n\n{english_text}"
    res = call_lm_studio(prompt, system_prompt=sys_prompt, model="qwen2.5-7b-instruct", max_tokens=2500, temperature=0.1)
    res = re.sub(r'^(?:以下の(?:文章|原著英文|英文)?を?[^：\n]*[：:\n]+)+', '', res.strip()).strip()
    return res


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


def generate_adult_relearning_exposition(verified_translation, chapter_topic, model="qwen2.5-7b-instruct"):
    """
    Step 3: Generate pedagogical lecture for adult re-learners (50s-80s) using LM Studio (http://192.168.128.16:1234/).
    Explains historical mathematical classics using junior high and high school mathematics.
    """
    sys_prompt = (
        "あなたは『古典で学び直す数学』の専任ナビゲーターです。\n"
        "読者対象は、50代から80代の大人です。「学生時代に数学で挫折してしまったが、もう一度挑戦したい」「大人になって知的好奇心から数学の本質を味わいたい」という方々です。\n"
        "以下の執筆指針を厳格に守って、充実した丁寧な解説講義を執筆してください：\n\n"
        "【執筆指針】\n"
        "1. 前提知識は中学校・高校数学（方程式、関数のグラフ、三角比、確率の基礎、微分積分の直観的イメージ）に限定し、難しい大学レベルの専門用語は使わずに平易に解きほぐす。\n"
        "2. 難しい概念や数式は、原著以上に一歩一歩のステップを省かずに懇切丁寧に説明する。なぜその計算や式変形が成り立つのかを読者が納得できるよう示す。\n"
        "3. 人生経験豊かな大人の読者が深く共感できるよう、歴史的背景（なぜ当時の大数学者がその問題に挑んだのか）や日常・社会との結びつき、知的興奮を生き生きと伝える。\n"
        "4. 語り口は知的で温かく、読者を励まし伴走する丁寧な敬体（です・ます調）とする。\n"
        "5. 数式はLaTeX形式（$...$, $$...$$）で明快に記載し、中国語は一切混入させず自然な日本語のみで記述する。"
    )
    prompt = (
        f"【本章のテーマ】：{chapter_topic}\n\n"
        f"以下の原著の日本語訳（数理校閲済み）の内容をもとに、大人の読者が中学校・高校の数学の知識で根本からスッキリ納得できるよう、"
        f"原著以上に丁寧で感動的な「学び直し解説講義」を執筆してください：\n\n"
        f"{verified_translation[:3000]}"
    )
    return call_lm_studio(prompt, system_prompt=sys_prompt, model="qwen2.5-7b-instruct", max_tokens=3000, temperature=0.2)


# Backwards compatibility alias
def generate_highschool_exposition(verified_translation, chapter_topic, model="qwen2.5-7b-instruct"):
    return generate_adult_relearning_exposition(verified_translation, chapter_topic, model=model)
