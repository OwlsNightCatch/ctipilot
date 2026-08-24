#!/usr/bin/env python3
"""Minimal HTML -> text extractor for on-disk quote checking (stdlib only)."""
import re
import sys
import html


def extract(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        doc = fh.read()
    doc = re.sub(r"(?is)<script.*?</script>", " ", doc)
    doc = re.sub(r"(?is)<style.*?</style>", " ", doc)
    doc = re.sub(r"(?is)<noscript.*?</noscript>", " ", doc)
    doc = re.sub(r"(?is)<svg.*?</svg>", " ", doc)
    doc = re.sub(r"(?is)<!--.*?-->", " ", doc)
    # block-level tags -> newline
    doc = re.sub(
        r"(?i)</?(p|div|br|li|tr|h[1-6]|section|article|table|thead|tbody|"
        r"blockquote|pre|ul|ol|figure|figcaption|header|footer|nav|td|th)[^>]*>",
        "\n",
        doc,
    )
    doc = re.sub(r"(?s)<[^>]+>", "", doc)
    doc = html.unescape(doc)
    lines = [ln.strip() for ln in doc.split("\n")]
    lines = [ln for ln in lines if ln]
    return "\n".join(lines)


if __name__ == "__main__":
    out = extract(sys.argv[1])
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"wrote {sys.argv[2]} ({len(out)} chars)")
    else:
        sys.stdout.write(out)
