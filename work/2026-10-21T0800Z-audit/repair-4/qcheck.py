#!/usr/bin/env python3
"""qcheck.py BODY_FILE 'quote' ['quote' ...]

For each quote: report LITERAL (grep -F on the tag-stripped, entity-decoded,
whitespace-collapsed text), SKELETON (check_run.py letters-and-digits match) or MISS.
Also: qcheck.py --text BODY_FILE  prints the stripped text."""
import html
import re
import sys
import unicodedata


def text_of(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    return re.sub(r"\s+", " ", raw)


def skel(t: str) -> str:
    t = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), t)
    t = re.sub(r"\\[ntr]", " ", t)
    t = unicodedata.normalize("NFKC", t).casefold()
    return "".join(c for c in t if c.isalnum())


def main() -> None:
    if sys.argv[1] == "--text":
        print(text_of(open(sys.argv[2], encoding="utf-8", errors="replace").read()))
        return
    raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    txt = text_of(raw)
    sk = skel(raw) + "|" + skel(txt)
    for q in sys.argv[2:]:
        qn = re.sub(r"\s+", " ", q)
        if qn in txt or qn in raw:
            v = "LITERAL"
        elif skel(q) in sk:
            v = "SKELETON"
        else:
            v = "MISS"
        print(f"{v}: {q[:110]}")


if __name__ == "__main__":
    main()
