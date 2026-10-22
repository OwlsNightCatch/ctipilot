#!/usr/bin/env python3
# usage: v.py <<'X' ... lines: claim_id<TAB>verdict<TAB>url<TAB>passage  (use ||| as separator)
import sys,json
out='work/2026-10-21T1148Z-audit/truth-1.claims.yaml'
import os
os.chdir('/home/user/ctipilot')
new=not os.path.exists(out)
with open(out,'a') as f:
    if new: f.write('claims:\n')
    for line in sys.stdin:
        line=line.rstrip('\n')
        if not line.strip(): continue
        p=line.split('|||')
        if len(p)!=4: print('BAD',line[:80]); continue
        cid,v,u,ps=[x.strip() for x in p]
        ps=ps[:200]
        f.write('  - {claim_id: %s, verdict: %s, source_url: %s, passage: %s}\n'%(cid,v,'null' if u in('','null') else json.dumps(u),json.dumps(ps,ensure_ascii=False)))
