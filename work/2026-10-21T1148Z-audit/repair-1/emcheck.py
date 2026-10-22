import sys, yaml, re
for path in sys.argv[1:]:
    t = open(path, encoding='utf-8').read()
    head, body = t.split('\n---\n', 1)
    fm = yaml.safe_load(head.lstrip('-\n'))
    issues = []
    for k in ('title', 'headline', 'summary', 'sourcing_note'):
        if fm.get(k) and '—' in str(fm[k]): issues.append(k)
    for i, a in enumerate(fm.get('actions') or []):
        if '—' in str(a): issues.append(f'actions[{i}]')
    for c in fm.get('cves') or []:
        for k, v in c.items():
            if isinstance(v, str) and '—' in v: issues.append(f"cves[{c.get('id')}].{k}")
    if fm.get('immediate_action') and '—' in str(fm['immediate_action']): issues.append('immediate_action')
    for n, line in enumerate(body.split('\n'), 1):
        if re.match(r'^## (Update|Correction|Improvement) — \d{4}-', line): continue
        if '—' in line: issues.append(f'body line {n}: ' + line[:60])
    for m in re.findall(r'\b(T1\d{3}(?:\.\d{3})?)\b', body): issues.append('T-id in body: ' + m)
    for pat in ('UPDATE (', 'this brief', 'tracked here', '(migrated)', 'this run', 'in this series', '§'):
        if pat in body or pat in str(fm.get('summary')) or pat in str(fm.get('headline')): issues.append('selfref: ' + pat)
    print(path.split('/')[-1][:60], 'OK' if not issues else issues)
