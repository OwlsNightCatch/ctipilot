import yaml,json,re,sys
RUN='2026-11-19T0355Z-intel'
rp=f'runs/2026-11-19/{RUN}.md'
class D(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)
def load():
    t=open(rp,encoding='utf-8').read()
    parts=t.split('\n---\n',1)
    fm=yaml.safe_load(parts[0].lstrip('-\n')); body=parts[1]
    return fm,body
def save(fm,body):
    open(rp,'w',encoding='utf-8').write('---\n'+yaml.dump(fm,Dumper=D,sort_keys=False,allow_unicode=True,width=10000)+'---\n'+body)
def entry_of(sec,item):
    m=re.search(r'entries/([^ ]+?)\.md',str(sec))
    if m: return m.group(1)
    it=str(item).lower()
    for k,v in [('nginx','2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws'),('basel','run-record')]:
        if k in it or k in str(sec).lower(): return v
    return 'run-record'
if __name__=='__main__':
    spec=json.load(open(sys.argv[1]))
    fm,body=load()
    f=yaml.safe_load(open(f'work/{RUN}/verification.iter{spec["n"]}.findings.yaml')); f=f['findings'] if isinstance(f,dict) else f
    rem=spec['remediation']
    assert len(rem)==len(f),(len(rem),len(f))
    fl=[]
    for x,r in zip(f,rem):
        s=re.sub(r'\s+',' ',str(x['summary'])).strip()
        fl.append({'code':x['code'],'entry':entry_of(x.get('section'),x.get('item')),'summary':s[:230]+('...' if len(s)>230 else ''),'remediation_applied':r})
    it={'n':spec['n'],'model':'Sonnet 5.5','model_id':'claude-sonnet-5-5','subagent_type':'cti-verification','started_at':spec['started'],'ended_at':spec['ended'],'duration_seconds':spec['dur'],'verdict':spec['verdict'],'truth':spec['truth'],'editorial':spec['editorial'],'advisory':spec['advisory'],'claims_in_scope':spec['claims'],'claims_checked':spec['claims'],'findings':fl}
    its=[i for i in fm['verification']['iterations'] if i['n']!=spec['n']]+[it]
    fm['verification']['iterations']=sorted(its,key=lambda i:i['n'])
    fm['verification_iterations']=len(fm['verification']['iterations'])
    fm['verification_residual_count']=spec.get('residual',0)
    save(fm,body); print('recorded iteration',spec['n'],len(fl),'findings')
