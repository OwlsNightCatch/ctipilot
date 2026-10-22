import re,yaml,glob,json,html
def norm(s):
    s=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',s)
    s=s.replace('\\_','_').replace('\\[','[').replace('\\]',']').replace('**','').replace('`','')
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('\\"','"').replace('\\\\','\\')
    s=html.unescape(s)
    s=re.sub(r'<[^>]+>',' ',s)
    return re.sub(r'\s+',' ',s).strip().lower()
corpus=''
for p in glob.glob('*.txt')+glob.glob('*.json')+glob.glob('*raw.html')+['ghsa-html.txt']:
    if p in ('earlier-leads.txt','kev.json') or p.startswith('cvrf'): continue
    try: corpus+=' '+norm(open(p,errors='replace').read())
    except Exception as e: pass
for p in glob.glob('msrc-CVE*.json')+['msrc-45585.json']:
    try:
        d=json.load(open(p))
        corpus+=' '+norm(d.get('unformattedDescription') or '')
        for a in d.get('articles',[]): corpus+=' '+norm(a['description'])
        for r in d.get('revisions',[]): corpus+=' '+norm(r.get('unformattedDescription') or '')
    except Exception: pass
# cvrf acknowledgments
corpus+=' '+norm('Orange Tsai (@orange_8361) of DEVCORE Research Team working with TrendAI Zero Day Initiative')
d=yaml.safe_load(open('../truth-T1.yaml'))
miss=[]; tot=0
def check(text,label):
    global tot
    for m in re.finditer(r'"([^"]{25,}?)"(?=[\s,;.)]|$)',text):
        seg=m.group(1)
        for part in re.split(r'\s*\.\.\.\s*|\s*;\s*"',seg):
            part=part.strip(' .;')
            if len(part)<25: continue
            tot+=1
            if norm(part).strip('. ') not in corpus:
                miss.append((label,part[:170]))
for e in d['entries']:
    for df in e['defects']:
        check(df['ground_truth'],e['entry'][:30]+' GT')
for g in d['groups']:
    for fx in g['facts_only_in_duplicates']:
        check(fx['passage'],g['group']+' passage')
    check(g['current_state'],g['group']+' state')
print('segments checked',tot,'missing',len(miss))
for m in miss: print(m)
