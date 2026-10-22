import json,sys
d=json.load(open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-1/kev-2026.10.20.json'))
print('catalog',d['catalogVersion'],d['dateReleased'])
v={x['cveID']:x for x in d['vulnerabilities']}
for c in sys.argv[1:]:
    x=v.get(c)
    if x: print(c,'IN KEV added',x['dateAdded'],x['vendorProject'],x['product'],'ransomware:',x.get('knownRansomwareCampaignUse'),'due',x['dueDate'])
    else: print(c,'not in KEV')
