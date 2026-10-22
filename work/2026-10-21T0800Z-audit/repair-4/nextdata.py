import json, re, sys, html
raw = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', raw, re.S)
d = json.loads(m.group(1))["props"]["pageProps"]["data"]
for k in ("title", "dateCreated", "lastModified"):
    print(k, ":", d.get(k))
for k in ("symptoms", "solution"):
    v = d.get(k) or ""
    v = " ".join(map(str, v)) if isinstance(v, list) else str(v)
    v = re.sub(r"<[^>]+>", " ", v)
    print("==", k, "==", re.sub(r"\s+", " ", html.unescape(v)))
