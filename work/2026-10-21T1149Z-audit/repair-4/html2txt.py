"""Strip an HTML file to visible text (stdlib only). Usage: html2txt.py IN OUT"""
import sys
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "svg", "template", "head"}
BLOCK = {"p", "div", "li", "tr", "br", "h1", "h2", "h3", "h4", "h5", "h6",
         "section", "article", "table", "pre", "dd", "dt", "td", "th", "relative-time"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag in BLOCK:
            self.out.append("\n")
        if tag == "relative-time":
            for k, v in attrs:
                if k == "datetime":
                    self.out.append(f"[datetime {v}] ")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8", errors="replace") as f:
        html = f.read()
    p = P()
    p.feed(html)
    text = "".join(p.out)
    lines = [" ".join(l.split()) for l in text.splitlines()]
    cleaned = []
    for l in lines:
        if l or (cleaned and cleaned[-1]):
            cleaned.append(l)
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned))


if __name__ == "__main__":
    main()
