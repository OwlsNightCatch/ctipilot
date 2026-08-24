#!/usr/bin/env python3
"""HTML -> flattened visible text for literal quote verification.

Inline tags are removed WITHOUT inserting whitespace (so <code>/<strong>
inside a sentence do not break it). Block tags become a single space.
All whitespace runs -- including NBSP (U+00A0), narrow NBSP and newlines --
collapse to one ASCII space. Curly quotes/apostrophes are PRESERVED so a
quote check fails loudly if the analyst retyped them as ASCII.
"""
import re
import sys
import html

BLOCK = (
    r"p|div|br|hr|li|tr|h[1-6]|section|article|table|thead|tbody|tfoot|"
    r"blockquote|pre|ul|ol|dl|dd|dt|figure|figcaption|header|footer|nav|"
    r"td|th|main|aside|form|option"
)


def flatten(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        doc = fh.read()
    for tag in ("script", "style", "noscript", "svg", "template"):
        doc = re.sub(r"(?is)<%s\b.*?</%s>" % (tag, tag), " ", doc)
    doc = re.sub(r"(?is)<!--.*?-->", " ", doc)
    doc = re.sub(r"(?i)</?(%s)(\s[^>]*)?/?>" % BLOCK, " ", doc)
    doc = re.sub(r"(?s)<[^>]+>", "", doc)          # inline tags: no space
    doc = html.unescape(doc)
    doc = doc.replace(" ", " ").replace(" ", " ").replace(" ", " ")
    doc = re.sub(r"[ \t\r\n\f\v]+", " ", doc)
    return doc.strip()


if __name__ == "__main__":
    out = flatten(sys.argv[1])
    with open(sys.argv[2], "w", encoding="utf-8") as fh:
        fh.write(out + "\n")
    print(f"wrote {sys.argv[2]} ({len(out)} chars)")
