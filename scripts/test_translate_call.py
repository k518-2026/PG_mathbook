import urllib.request
import json
import time
import sys

q = "In every business of life we are occasionally perplexed by some chance question that for the moment staggers us. A gentleman entered a post-office and requested: Please give me some twopenny stamps, six times as many penny stamps, and the rest in twopence-halfpenny stamps for my 5 shillings."
a = "5 shillings = 60 pence. 2x + 6x + 2.5y = 60 pence, so 16x + 5y = 120. Solution gives 5 twopenny stamps, 30 penny stamps, and 8 twopence-halfpenny stamps."

prompt = (
    "Translate the following math puzzle into natural, scholarly Japanese.\n"
    "Output strict JSON with keys 'problem_ja' and 'solution_ja'.\n\n"
    f"[Problem]\n{q}\n\n[Solution]\n{a}\n"
)

payload = {
    "model": "qwen2.5-7b-instruct",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 600,
    "temperature": 0.1
}

t0 = time.time()
req = urllib.request.Request(
    "http://192.168.128.16:1234/v1/chat/completions",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req, timeout=60) as res:
    data = json.loads(res.read().decode("utf-8"))
    elapsed = time.time() - t0
    sys.stdout.buffer.write(f"Time: {elapsed:.2f}s\n".encode("utf-8"))
    sys.stdout.buffer.write(data["choices"][0]["message"]["content"].encode("utf-8"))
    sys.stdout.buffer.write(b"\n")
