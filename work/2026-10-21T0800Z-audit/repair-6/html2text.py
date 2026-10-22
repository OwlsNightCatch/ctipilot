#!/usr/bin/env python3
"""Strip a saved raw-HTML body to plain text (one paragraph per line) for grep -F checks.

usage: python3 -I html2text.py IN.html OUT.txt
"""
import html
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8", errors="replace").read()
t = re.sub(r"(?is)<(script|style|svg|noscript)[^>]*>.*?</\1>", " ", t)
t = re.sub(r"(?i)<br\s*/?>", "\n", t)
t = re.sub(r"(?i)</(p|div|li|h[1-6]|tr|section|article)>", "\n", t)
t = re.sub(r"(?s)<[^>]+>", " ", t)
t = html.unescape(t)
t = t.replace(" ", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r" *\n *", "\n", t)
t = re.sub(r"\n{2,}", "\n", t)
open(dst, "w", encoding="utf-8").write(t)
print(f"{dst}: {len(t)} chars")
