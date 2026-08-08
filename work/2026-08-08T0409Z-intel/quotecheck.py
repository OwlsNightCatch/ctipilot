import re,sys,html,json,os
RAW='work/2026-08-08T0409Z-intel/raw'
def norm(p):
    t=open(p,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>','',t)
    # close block-level tags to newline, everything else to EMPTY STRING (no inserted whitespace)
    t=re.sub(r'(?i)</(p|div|li|tr|h[1-6]|br|section|article)\s*>','\n',t)
    t=re.sub(r'(?i)<br\s*/?>','\n',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t)
    return t
BODIES={f[:-4]:norm(os.path.join(RAW,f)) for f in os.listdir(RAW) if f.endswith('.txt')}
def check(q, keys):
    variants={q, q.replace('’',"'").replace('“','"').replace('”','"').replace('—','--'),
              re.sub(r'\s+',' ',q)}
    for k in keys:
        b=BODIES.get(k,'')
        bn=re.sub(r'\s+',' ',b)
        for v in variants:
            if v in b or v in bn: return k
    return None
quotes=json.load(open(sys.argv[1]))
bad=0
for q in quotes:
    hit=check(q['q'], q['files'])
    print(("OK   %-16s"%hit if hit else "MISS %-16s"%"-"), q['id'], '|', q['q'][:95].replace('\n',' '))
    if not hit: bad+=1
print(f"\n{len(quotes)-bad}/{len(quotes)} verbatim; {bad} MISS")
