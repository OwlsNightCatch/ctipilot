import re,html,sys,json,os
P="work/2026-08-24T0410Z-intel/pages"
def strip(h):
    h=re.sub(r'<(script|style|head|noscript)[^>]*>.*?</\1>','',h,flags=re.S|re.I)
    h=re.sub(r'</(div|p|li|tr|td|th|h[1-6]|section|table|article|blockquote|ul|ol|br)\s*>','\n',h,flags=re.I)
    h=re.sub(r'<br\s*/?>','\n',h,flags=re.I)
    h=re.sub(r'<[^>]+>','',h)          # tags -> EMPTY STRING (no space!)
    return html.unescape(h)
bodies={}
for k in ["levelblue","expel","truffle","socradar","rapid7","bitdefender"]:
    f=f"{P}/raw.{k}.html"
    if not os.path.exists(f): continue
    b=strip(open(f,encoding="utf-8",errors="replace").read())
    bodies[k]=b
    open(f"{P}/body.{k}.txt","w",encoding="utf-8").write(b)
QUOTES=json.load(open("work/2026-08-24T0410Z-intel/quotes.json",encoding="utf-8"))
ok=bad=0
for q in QUOTES:
    b=bodies.get(q["src"],"")
    hit = q["quote"] in b
    if hit: ok+=1
    else: bad+=1
    print(("PASS " if hit else "FAIL ")+q["src"]+" :: "+q["quote"][:110].replace("\n"," "))
print(f"\n{ok} pass / {bad} fail")
