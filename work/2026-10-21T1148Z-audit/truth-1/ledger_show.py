import yaml,sys
d=yaml.safe_load(open('work/2026-10-21T1148Z-audit/truth-1.ledger.yaml'))['claims']
e=sys.argv[1]
for c in d:
    if c['entry']==e:
        print(c['claim_id'],c['surface'],c['kind'],'|',c['text'][:140].replace('\n',' '), '|', c.get('urls',''))
