import sys, yaml
d = yaml.safe_load(open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-3.ledger.yaml'))['claims']
ents = []
for c in d:
    if c['entry'] not in ents: ents.append(c['entry'])
key = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 160
for c in d:
    if key in c['entry']:
        print(c['claim_id'], c['surface'], c['kind'], '|', c['text'][:n].replace('\n',' '), '|', ','.join(c.get('urls',[]))[:200] if c.get('urls') else '')
