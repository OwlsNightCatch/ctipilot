#!/usr/bin/env python3
"""Literal-substring quote check against saved page bodies.

Tags are replaced with the EMPTY string (newline only for block-level closes),
per prompts/cti-run.md Phase 4 item 4 — replacing tags with a space corrupts the
text and produces false greens.
"""
import re, sys, html, os, json

BLOCK = re.compile(r'</(p|div|li|tr|h[1-6]|blockquote|section|article|pre|td|th|ul|ol|table)\s*>', re.I)
DROP  = re.compile(r'<(script|style|noscript)\b[^>]*>.*?</\1\s*>', re.I | re.S)
TAG   = re.compile(r'<[^>]+>')

_cache = {}

def load(name):
    if name in _cache:
        return _cache[name]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages", name + ".txt")
    t = open(p, encoding="utf-8", errors="replace").read()
    t = DROP.sub("", t)
    t = BLOCK.sub("\n", t)
    t = TAG.sub("", t)
    t = html.unescape(t)
    # collapse runs of whitespace to a single space so line wrapping in the
    # source HTML does not defeat a literal match; keep the source's own
    # characters otherwise (curly quotes, nbsp normalised to space only).
    t = t.replace(" ", " ")
    flat = re.sub(r"\s+", " ", t)
    _cache[name] = flat
    return flat

def norm(q):
    return re.sub(r"\s+", " ", q.replace(" ", " ")).strip()

def check(name, quote):
    body = load(name)
    q = norm(quote)
    if q in body:
        return True, None
    # try curly/straight apostrophe + quote variants
    for a, b in (("'", "’"), ("’", "'"), ('"', "“"), ('"', "”")):
        if norm(quote.replace(a, b)) in body:
            return True, f"matched with {a!r}->{b!r}"
    # locate longest matching prefix to help shorten
    lo, hi = 0, len(q)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if q[:mid] in body:
            lo = mid
        else:
            hi = mid - 1
    return False, f"longest prefix that matches ({lo} chars): {q[:lo]!r}"

if __name__ == "__main__":
    quotes = json.load(open(sys.argv[1]))
    bad = 0
    for name, q in quotes:
        ok, note = check(name, q)
        print(("PASS " if ok else "FAIL ") + name + " :: " + q[:90].replace("\n", " "))
        if note:
            print("      " + note)
        if not ok:
            bad += 1
    print(f"\n{len(quotes)-bad}/{len(quotes)} pass")
