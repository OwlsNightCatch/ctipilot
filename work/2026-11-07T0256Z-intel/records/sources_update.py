import json, yaml, re, glob, sys
from urllib.parse import urlparse
RUN='work/2026-11-07T0256Z-intel'; TODAY='2026-11-07'
APPLY = len(sys.argv)>1 and sys.argv[1]=='apply'
raw=open('sources/sources.json',encoding='utf-8').read()
d=json.loads(raw)
S={x['id']:x for x in d['sources']}
host=lambda u: (urlparse(u).netloc or '').lower().replace('www.','') if u else ''
led={}
for dm in ['S1','S2','S3','S4']:
    f=yaml.safe_load(open(f'{RUN}/findings.{dm}.yaml'))
    for r in f['source_ledger']: led[r['id']]=r
# cited hosts in entries touched by this run
import subprocess
files=subprocess.check_output("git status --porcelain entries | awk '{print $2}'",shell=True,text=True).split()
files=[x for x in files if x.endswith('.md')]
import os
cited=set()
def urls(t):
    fm=t.split('---\n',2)[1]
    return set(re.findall(r'url: "(https?://[^"]+)"',fm))
for p_ in subprocess.check_output("git ls-files -m -o --exclude-standard entries",shell=True,text=True).split():
    t=open(p_,encoding='utf-8').read()
    try: old=subprocess.check_output(['git','show','HEAD:'+p_],text=True,stderr=subprocess.DEVNULL)
    except Exception: old=''
    base=urls(old) if old else set()
    for u in urls(t)-base: cited.add(host(u))
used=set(i for i,r in led.items() if (r.get('returned') or 0)>0)
bymhost={}
for i,x in S.items():
    for u in (x.get('url'),x.get('rss_url')):
        if u: bymhost.setdefault(host(u),set()).add(i)
for h in cited:
    ids=bymhost.get(h,set())
    if len(ids)==1: used|=ids
    else: used|={i for i in ids if i in led}
plan=[]
for i,r in led.items():
    x=S.get(i)
    if not x: plan.append((i,'NOT IN sources.json')); continue
    if i in used:
        x['last_successful_fetch']=TODAY; x['consecutive_quiet_periods']=0; x['consecutive_fetch_failures']=0; plan.append((i,'used'))
    elif r.get('attempted'):
        note=(r.get('note') or '')+' '+(r.get('transport') or '')
        if re.search(r'\b403\b|HTTP 4\d\d|unreachable|failed|blocked',note) and (r.get('in_horizon_items') or 0)==0 and re.search(r'403',note):
            x['consecutive_fetch_failures']=(x.get('consecutive_fetch_failures') or 0)+1; plan.append((i,'fetch-failure+1'))
        else:
            x['consecutive_quiet_periods']=(x.get('consecutive_quiet_periods') or 0)+1; plan.append((i,'quiet+1'))
for i,a in plan: print(a,i)
print('used-by-host extras:',sorted(used-{i for i,r in led.items() if (r.get('returned') or 0)>0}))
if APPLY:
    open('sources/sources.json','w',encoding='utf-8').write(json.dumps(d,indent=1,ensure_ascii=True)+'\n')
    print('written')
