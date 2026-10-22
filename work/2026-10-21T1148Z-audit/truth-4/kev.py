import json,sys
D='/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-4/bodies/'
k=json.load(open(D+'cisa-kev.json'))
idx={v['cveID']:v for v in k['vulnerabilities']}
for c in sys.argv[1:]:
    c=c.upper(); v=idx.get(c)
    if v: print(c,'KEV dateAdded',v['dateAdded'],'|',v['vendorProject'],v['product'],'|',v['shortDescription'][:140],'| ransomware:',v['knownRansomwareCampaignUse'],'| due',v['dueDate'])
    else: print(c,'NOT in KEV (catalog',k['catalogVersion'],')')
