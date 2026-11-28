import sys,re,json,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',t,re.S)
if not m:
    print('no next data', len(t)); sys.exit()
d=json.loads(m.group(1))
def walk(o,out):
    if isinstance(o,dict):
        for k,v in o.items():
            if k in('body','lead','title','text','teaser','content') and isinstance(v,str): out.append((k,v))
            else: walk(v,out)
    elif isinstance(o,list):
        for v in o: walk(v,out)
out=[]; walk(d,out)
seen=set()
for k,v in out:
    v=re.sub(r'<[^>]+>',' ',html.unescape(v)); v=re.sub(r'\s+',' ',v).strip()
    if len(v)>40 and v not in seen:
        seen.add(v); print(f'[{k}]',v[:1800])
