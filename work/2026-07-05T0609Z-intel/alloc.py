import json
d=json.load(open('sources/sources.json'))
srcs = d['sources'] if isinstance(d,dict) else d
gaps = {"cisa-advisories","cisa-directives","cisa-news","industrialcyber-co"}

DOMAINS = {
 "S1": {"active-breaking","vulns","vendor-psirt"},
 "S2": {"ch-eu","gov","sanctions"},
 "S3": {"research","news","discovery","ot-ics"},
 "S4": {"breaches","news","ransomware"},
}
def cats(s):
    c=s.get('category',[]); return set([c] if isinstance(c,str) else c)

def slot(s):
    return {k:s.get(k) for k in ('id','publisher','url','tier','fetch_method','reliability','language','notes','last_successful_fetch')}

for dom, filt in DOMAINS.items():
    matching=[s for s in srcs if s.get('status')=='active' and (cats(s)&filt)]
    essential=[s for s in matching if s.get('tier')=='essential']
    standard=[s for s in matching if s.get('tier')!='essential']
    # rank standard oldest last_successful_fetch first, promote gaps
    def key(s):
        g = 0 if s['id'] in gaps else 1
        lsf = s.get('last_successful_fetch') or '0000-00-00'
        return (g, lsf)
    standard.sort(key=key)
    take = standard[:13]
    slice_ = [slot(s) for s in essential] + [slot(s) for s in take]
    json.dump({"domain":dom,"essential_ids":[s['id'] for s in essential],
               "standard_ids":[s['id'] for s in take],"sources":slice_},
              open(f'work/{__import__("os").environ["RUN_ID"]}/alloc.{dom}.json','w'), indent=1)
    print(f"{dom}: essential={len(essential)} standard_taken={len(take)} total={len(slice_)}")
