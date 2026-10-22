#!/usr/bin/env python3
"""Check every evidence quote (and original) of an entry against saved bodies (exact substring)."""
import sys, glob, re
sys.path.insert(0, '/home/user/ctipilot/site')
import content_model as cm
root='/home/user/ctipilot'
files=glob.glob(root+'/work/2026-10-21T1148Z-audit/truth-2/bodies/*')+glob.glob(root+'/work/2026-10-21T1148Z-audit/repair-2/src/*')
texts={f:open(f,errors='replace').read() for f in files}
import unicodedata
sk=lambda t:''.join(c for c in unicodedata.normalize('NFKC',t).casefold() if c.isalnum())
sktexts={f:sk(t) for f,t in texts.items()}
for eid in sys.argv[1:]:
    e=cm.load_entry(__import__('pathlib').Path(f'{root}/entries/{eid}.md'), root=__import__('pathlib').Path(root))
    for ev in e.get('evidence') or []:
        for key in ('quote','original'):
            q=ev.get(key)
            if not q: continue
            hits=[f.rsplit('/',1)[1] for f,t in texts.items() if q in t]
            sh=[] if hits else [f.rsplit('/',1)[1] for f,t in sktexts.items() if sk(q) in t]
            print(('OK  ' if hits else ('SKEL' if sh else 'MISS')), key, repr(q[:80]), (hits or sh)[:4])
