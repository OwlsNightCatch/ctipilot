import glob, yaml, os, sys
B = '/home/user/ctipilot/work/2026-10-21T1148Z-audit/'
frags = sorted(glob.glob(B + 'truth-3/frag/*.py'))
entries, claims, groups = [], [], []
for f in frags:
    ns = {}
    exec(open(f, encoding='utf-8').read(), ns)
    e = ns['ENTRY']
    entries.append(e)
    for line in ns['CLAIMS'].strip().splitlines():
        line = line.strip()
        if not line: continue
        p = [x.strip() for x in line.split('¦')]
        assert len(p) == 4, (f, line)
        cid, v, url, passage = p
        claims.append({'claim_id': cid, 'verdict': v, 'source_url': (None if url in ('', 'null') else url), 'passage': passage[:200]})
    groups.extend(ns.get('DUP', []))
class D(yaml.SafeDumper): pass
def rep(dumper, data):
    if '\n' in data: return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)
D.add_representer(str, rep)
open(B + 'truth-3.yaml', 'w', encoding='utf-8').write(yaml.dump({'entries': entries, 'duplicate_groups': groups}, Dumper=D, sort_keys=False, allow_unicode=True, width=1000))
open(B + 'truth-3.claims.yaml', 'w', encoding='utf-8').write(yaml.dump({'claims': claims}, Dumper=D, sort_keys=False, allow_unicode=True, width=1000))
# coverage check against ledger
led = yaml.safe_load(open(B + 'truth-3.ledger.yaml'))['claims']
have = {c['claim_id'] for c in claims}
missing = [str(c['claim_id']) for c in led if str(c['claim_id']) not in have]
extra = [c for c in have if c not in {str(x['claim_id']) for x in led}]
print('entries', len(entries), 'claims', len(claims), 'ledger', len(led), 'missing', len(missing), 'extra', extra)
