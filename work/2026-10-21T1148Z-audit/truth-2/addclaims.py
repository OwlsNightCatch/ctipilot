import sys,yaml,json
# usage: addclaims.py <file.yaml containing list of {claim_id,verdict,source_url,passage}>
out='/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-2.claims.yaml'
rows=yaml.safe_load(open(sys.argv[1]))
import os
existing=set()
if os.path.exists(out):
    cur=yaml.safe_load(open(out)) or {}
    existing={r['claim_id'] for r in cur.get('claims',[])}
else:
    cur={'claims':[]}
n=0
for r in rows:
    if r['claim_id'] in existing: continue
    cur['claims'].append({'claim_id':r['claim_id'],'verdict':r['verdict'],'source_url':r.get('source_url'),'passage':(r.get('passage') or '')[:200]})
    n+=1
yaml.safe_dump(cur,open(out,'w'),sort_keys=False,allow_unicode=True,width=10000)
print('added',n,'total',len(cur['claims']))
