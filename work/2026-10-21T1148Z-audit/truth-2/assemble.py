import yaml,glob,sys
frs=sorted(glob.glob('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-2/frag/e*.yaml'))
entries=[]
for f in frs:
    entries+=yaml.safe_load(open(f))
dup=[]
try: dup=yaml.safe_load(open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-2/frag/dups.yaml')) or []
except FileNotFoundError: pass
out={'entries':entries,'duplicate_groups':dup}
yaml.safe_dump(out,open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-2.yaml','w'),sort_keys=False,allow_unicode=True,width=10000)
print('entries',len(entries))
