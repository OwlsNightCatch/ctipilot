# usage: python3 vr.py < rows ; rows: claim_id|verdict|source_url|passage   (one per line)
import sys,json
out=open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-4.claims.yaml','a')
if out.tell()==0: out.write('claims:\n')
n=0
for line in sys.stdin:
    line=line.rstrip('\n')
    if not line.strip(): continue
    p=line.split('|',3)
    cid,v,url,passage=[x.strip() for x in p]
    passage=passage[:200]
    out.write('  - {claim_id: %s, verdict: %s, source_url: %s, passage: %s}\n'%(json.dumps(cid),v,json.dumps(url) if url and url!='null' else 'null',json.dumps(passage)))
    n+=1
print('wrote',n)
