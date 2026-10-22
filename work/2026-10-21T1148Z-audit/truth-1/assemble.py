import yaml,glob,os
os.chdir('/home/user/ctipilot/work/2026-10-21T1148Z-audit')
parts=sorted(glob.glob('truth-1/frag/[0-9][0-9].yaml'))
body='entries:\n'+''.join(open(p).read() for p in parts)
dg='truth-1/frag/dup.yaml'
body+= open(dg).read() if os.path.exists(dg) else 'duplicate_groups: []\n'
d=yaml.safe_load(body)
assert all('upgrade' in e and 'verdict' in e for e in d['entries'])
open('truth-1.yaml','w').write(body)
from collections import Counter
print(len(d['entries']),'entries',Counter(e['verdict'] for e in d['entries']),'dups',len(d['duplicate_groups']))
