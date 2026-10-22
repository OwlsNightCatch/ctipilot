import sys,yaml
d=yaml.safe_load(open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-4.ledger.yaml'))['claims']
sel=sys.argv[1]
n=int(sys.argv[2]) if len(sys.argv)>2 else 110
for c in d:
    if c['entry'].endswith(sel) or sel in c['entry']:
        print(c['claim_id'],'|',c['surface'],'|',c['kind'],'|',(c['text'] or '').replace('\n',' ')[:n],'|',','.join(c.get('urls') or [])[:80])
