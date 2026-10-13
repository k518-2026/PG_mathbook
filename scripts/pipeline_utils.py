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
