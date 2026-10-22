import yaml, os, datetime, sys
W='/home/user/ctipilot/work/2026-10-21T1149Z-audit/'
OUT=W+'truth-T1.yaml'
PROG=W+'truth-T1.progress'
class Lit(str): pass
def lit_rep(d,v): return d.represent_scalar('tag:yaml.org,2002:str',str(v),style='|' if '\n' in v else None)
yaml.SafeDumper.add_representer(Lit,lit_rep)
def load():
    if os.path.exists(OUT):
        return yaml.safe_load(open(OUT)) or {}
    return {}
def save(d):
    with open(OUT,'w') as f:
        yaml.safe_dump(d,f,width=200,allow_unicode=True,sort_keys=False,default_flow_style=False)
def add_entry(e):
    d=load(); d.setdefault('entries',[])
    d['entries']=[x for x in d['entries'] if x['entry']!=e['entry']]+[e]
    save(d)
    ts=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    prev=open(PROG).read() if os.path.exists(PROG) else ''
    if e['entry'] not in prev:
        open(PROG,'a').write(f"{ts} {e['entry']} {e['verdict']}\n")
def set_groups(g):
    d=load(); d['groups']=g; save(d)
def df(where,claim,defect,gt,url,fix,cls):
    return dict(where=where,claim=claim,defect=defect,ground_truth=gt,ground_truth_url=url,fix=fix,**{'class':cls})
