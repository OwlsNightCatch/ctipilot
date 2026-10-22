import sys, yaml
d = yaml.safe_load(open('work/2026-10-21T1148Z-audit/truth-3.yaml'))
key = sys.argv[1]
part = sys.argv[2] if len(sys.argv) > 2 else 'all'
for e in d['entries']:
    if key in e['entry']:
        if part == 'upgrade':
            print(yaml.safe_dump(e.get('upgrade'), allow_unicode=True, sort_keys=False, width=200))
            print('twin:', e.get('possible_twin_outside_batch'))
        else:
            print(yaml.safe_dump(e, allow_unicode=True, sort_keys=False, width=200))
