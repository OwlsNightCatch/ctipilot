#!/usr/bin/env python3
"""Check each evidence quote of an entry verbatim against saved bodies (first line = URL)."""
import sys, glob, re
sys.path.insert(0, '/home/user/ctipilot/site')
import content_model as cm
from pathlib import Path
root = Path('/home/user/ctipilot')
dirs = [root/'work/2026-10-21T1148Z-audit/truth-4/bodies', root/'work/2026-10-21T1148Z-audit/repair-4/src']
bodies = {}
for d in dirs:
    for f in d.glob('*'):
        if f.is_file():
            try:
                t = f.read_text(encoding='utf-8', errors='replace')
            except Exception:
                continue
            first = t.split('\n', 1)[0].strip()
            bodies.setdefault(first.rstrip('/'), []).append((f, t))
def norm(s):
    return re.sub(r'\s+', ' ', s)
for eid in sys.argv[1:]:
    p = root/'entries'/(eid + '.md')
    e = cm.load_entry(p) if hasattr(cm, 'load_entry') else None
    if e is None:
        import yaml
    for ev in (e.get('evidence') or []):
        q = ev.get('original') or ev.get('quote')
        u = (ev.get('source_url') or '').rstrip('/')
        cands = bodies.get(u, [])
        hit = [str(f.name) for f, t in cands if q in t or norm(q) in norm(t)]
        anyhit = [] if hit else [str(f.name) for k, v in bodies.items() for f, t in v if q in t or norm(q) in norm(t)]
        print(('OK  ' if hit else ('ELSEWHERE ' + ','.join(anyhit[:2]) + ' ' if anyhit else 'MISS ')) + (u[:70] or '(no url)') + ' :: ' + q[:80])
