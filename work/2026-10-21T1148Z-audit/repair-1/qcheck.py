import sys, glob, yaml, re
bodies = {}
for p in glob.glob('work/2026-10-21T1148Z-audit/truth-1/bodies/*') + glob.glob('work/2026-10-21T1148Z-audit/repair-1/src/*'):
    try:
        txt = open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        continue
    first = txt.split('\n', 1)[0].strip()
    bodies.setdefault(first, []).append((p, txt))
def norm(s): return re.sub(r'\s+', ' ', s)
for path in sys.argv[1:]:
    t = open(path, encoding='utf-8').read()
    fm = yaml.safe_load(t.split('\n---\n', 1)[0].lstrip('-\n'))
    for ev in fm.get('evidence') or []:
        s = ev.get('original') or ev.get('quote')
        url = ev.get('source_url')
        cands = bodies.get(url, []) if url else [b for v in bodies.values() for b in v]
        hit = [p for p, txt in cands if s in txt or norm(s) in norm(txt)]
        print(('OK  ' if hit else 'MISS'), (url or '-')[:70], '|', s[:80], '|', (hit[0].split('/')[-1] if hit else ('no body for url' if not cands else '')))
