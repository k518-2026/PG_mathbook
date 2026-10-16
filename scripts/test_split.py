# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

line = chr(36) + 'amn\\theta^{n-1} \\tan^{m-1}\\left(\\theta^n\\right)\\sec^2 \\theta^n' + chr(36)
print('Line:', repr(line))

pattern = r'(\$\$[\s\S]*?\$\$|\$[^\$\n]+?\$|\\\(.*?\\\)|\\\[[\s\S]*?\\\])'
parts = re.split(pattern, line)
print('Parts count:', len(parts))
for idx, p in enumerate(parts):
    print(f'Part {idx}:', repr(p))
