"""Wave statistics over the run's updated entries, base vs now."""
import subprocess, yaml, collections, sys
RUN = '2026-10-21T1148Z-audit'
base = open(f'work/{RUN}/base.sha').read().strip()
ids = [l.strip() for l in open(f'work/{RUN}/main/done-ids.txt') if l.strip()]
def split(t):
    i = t.index('\n---\n', 4)
    return yaml.safe_load(t[4:i]), t[i + 5:]
mv = collections.Counter(); kinds = collections.Counter(); tech = []; types = collections.Counter(); lines = collections.Counter()
for i in ids:
    c, body = split(open(f'entries/{i}.md').read())
    o, _ = split(subprocess.run(['git', 'show', f'{base}:entries/{i}.md'], capture_output=True, text=True).stdout)
    if o['priority'] != c['priority']: mv[f"{o['priority']}->{c['priority']}"] += 1
    if o['kind'] != c['kind'] or o.get('deep_dive') != c.get('deep_dive'): kinds[f"{o['kind']}{'(dd)' if o.get('deep_dive') else ''}->{c['kind']}"] += 1
    tech += c.get('techniques') or []
    r = [u for u in c['updates'] if u['run_id'] == RUN]
    assert len(r) == 1, i
    types[r[0]['type'] + ('/internal' if r[0].get('internal') else '')] += 1
    for k in ['Exposure', 'Detection', 'Triage', 'Defender takeaway']:
        if f'**{k}:**' in body: lines[k] += 1
print(len(ids), dict(mv), sum(mv.values()), dict(kinds), len(tech), len(set(tech)), dict(types), dict(lines))
