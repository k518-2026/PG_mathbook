# -*- coding: utf-8 -*-
"""
Fix Section V, XXXII, and App_IV in Einstein translation cache.
"""

import json

CACHE_FILE = "books/30155_einstein_relativity/einstein_full_translation_cache.json"

with open(CACHE_FILE, "r", encoding="utf-8") as f:
    cache = json.load(f)

# Fix Section V
sec_v = cache["Sec_V"]["japanese_translation"]
sec_v = sec_v.replace(
    "我達现在進行第二個論證，並且稍後還會回到這個論點。",
    "我々は今や第二の論点へと進もう。これについては後に再び立ち返ることになる。"
)
cache["Sec_V"]["japanese_translation"] = sec_v

# Fix Section XXXII (10²⁷ -> 10^{27})
sec_xxxii = cache["Sec_XXXII"]["japanese_translation"]
sec_xxxii = sec_xxxii.replace("10²⁷", "$10^{27}$").replace("10²", "$10^2$").replace("⁷", "")
cache["Sec_XXXII"]["japanese_translation"] = sec_xxxii

# Fix Section App_IV (二维座标 -> 二次元座標, 三维座标 -> 三次元座標, 四维座标 -> 四次元座標)
sec_app_iv = cache["Sec_App_IV"]["japanese_translation"]
sec_app_iv = sec_app_iv.replace("二维座标", "二次元座標")
sec_app_iv = sec_app_iv.replace("三维座标", "三次元座標")
sec_app_iv = sec_app_iv.replace("四维座标", "四次元座標")
sec_app_iv = sec_app_iv.replace("座标", "座標")
sec_app_iv = sec_app_iv.replace("维", "次元")
cache["Sec_App_IV"]["japanese_translation"] = sec_app_iv

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print("Fixed Section V, XXXII, App_IV successfully!")
