import yaml,os,glob,re,sys
ROOT='/home/user/ctipilot/work/2026-10-21T1148Z-audit/'
D=ROOT+'truth-4/'
os.makedirs(D+'entries',exist_ok=True)
def _norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace(' ',' ')
    return re.sub(r'\s+',' ',s).strip().lower()
_bodies=None
def bodies():
    global _bodies
    out={}
    for f in glob.glob(D+'bodies/*'):
        if os.path.basename(f).startswith('.'): continue
        try: txt=open(f,errors='replace').read()
        except: continue
        first=txt.split('\n',1)[0].strip()
        out[f]=(first,_norm(txt))
    return out
def check_quotes(d):
    bs=bodies(); bad=[]
    for sect in ('exposure','detection','triage','takeaway'):
        for q in d.get('upgrade',{}).get(sect,[]) or []:
            nq=_norm(q['quote']); ok=False
            for f,(u,t) in bs.items():
                if (u==q['url'] or q['url'] in u or u in q['url']) and nq in t: ok=True;break
            if not ok:
                # try any body
                anyok=[os.path.basename(f) for f,(u,t) in bs.items() if nq in t]
                bad.append((sect,q['quote'][:70],q['url'],anyok))
    return bad
def save(d):
    slug=d['entry'].replace('/','__')
    # normalise to expected shape
    d.setdefault('defects',[]); d.setdefault('possible_twin_outside_batch',None)
    with open(D+'entries/'+slug+'.yaml','w') as f:
        yaml.safe_dump([d],f,sort_keys=False,allow_unicode=True,width=10000,default_flow_style=False)
    bad=check_quotes(d)
    for b in bad: print('QUOTE-NOT-FOUND',b)
    print('saved',slug,'defects',len(d['defects']),'verdict',d['verdict'])
def assemble():
    items=[]
    for f in sorted(glob.glob(D+'entries/*.yaml')):
        items+=yaml.safe_load(open(f))
    dg=[]; pd=[]
    p=D+'dupgroups.yaml'
    if os.path.exists(p):
        x=yaml.safe_load(open(p)) or {}
        dg=x.get('duplicate_groups',[]); pd=x.get('pair_decisions',[])
    out={'entries':items,'duplicate_groups':dg}
    if pd: out['pair_decisions']=pd
    with open(ROOT+'truth-4.yaml','w') as f:
        yaml.safe_dump(out,f,sort_keys=False,allow_unicode=True,width=10000,default_flow_style=False)
    print('assembled',len(items),'entries',len(dg),'dup groups',len(pd),'pair decisions')
if __name__=='__main__' and len(sys.argv)>1 and sys.argv[1]=='asm': assemble()
