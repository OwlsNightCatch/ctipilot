import json,re,html,sys,subprocess,os
D='/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-4/bodies/'
for cve in sys.argv[1:]:
    c=cve.upper(); jp=D+'msrc-'+c.lower()+'.json'
    if not os.path.exists(jp):
        r=subprocess.run(['python3','/home/user/ctipilot/tools/fetch_source.py','msrc','cve',c],capture_output=True,text=True,cwd='/home/user/ctipilot')
        open(jp,'w').write(r.stdout)
    d=json.load(open(jp))
    url='https://msrc.microsoft.com/update-guide/en-US/vulnerability/'+c
    out=[url,'# MSRC SUG OData record (msrc cve recipe) flattened to text']
    for k in ['cveNumber','cveTitle','releaseDate','latestRevisionDate','publiclyDisclosed','exploited','latestSoftwareRelease','severity','impact','baseScore','temporalScore','vectorString','cweList','tag','customerActionRequired']:
        out.append(f'{k}: {d.get(k)}')
    out.append('description: '+re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',d.get('description') or d.get('unformattedDescription') or ''))))
    for a in d.get('articles',[]):
        t=re.sub(r'<[^>]+>',' ',a['description']); out.append('ARTICLE '+str(a['articleType'])+': '+re.sub(r'\s+',' ',html.unescape(t)))
    for r in d.get('revisions',[]):
        out.append(f"REVISION {r['version']} {r['revisionDate']}: {r['unformattedDescription']}")
    open(D+'msrc-'+c.lower()+'.txt','w').write('\n'.join(out)+'\n')
    open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/url-liveness.tsv','a').write(f"{url}\tmsrc-recipe-ok\t{__import__('datetime').datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
    print('wrote',c)
