import yaml,sys
d=yaml.safe_load(open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-2.ledger.yaml'))['claims']
pre=sys.argv[1]
w=int(sys.argv[2]) if len(sys.argv)>2 else 600
for x in d:
    if x['entry'].startswith(pre):
        print(x['claim_id'],'|',x['surface'],'|',x['kind'],'|',(x['text'] or '')[:w].replace('\n',' '),'|',x.get('urls',''))
