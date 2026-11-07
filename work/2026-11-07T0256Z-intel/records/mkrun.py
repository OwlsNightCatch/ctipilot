import json, yaml, subprocess, re, glob, os
RUN='work/2026-11-07T0256Z-intel'; RID='2026-11-07T0256Z-intel'; TODAY='2026-11-07'
def head(path):
    return subprocess.check_output(['git','show','HEAD:'+path],text=True)
# ledgers
led={}; per={}
for dm in ['S1','S2','S3','S4']:
    f=yaml.safe_load(open(f'{RUN}/findings.{dm}.yaml'))
    per[dm]=f
    for r in f['source_ledger']: led[r['id']]=(dm,r)
def sa(dm): return [r['id'] for r in per[dm]['source_ledger'] if r.get('attempted')]
src_new=json.load(open('sources/sources.json'))['sources']; src_old=json.loads(head('sources/sources.json'))['sources']
N={x['id']:x for x in src_new}; O={x['id']:x for x in src_old}
def used(dm): 
    ids=[r['id'] for r in per[dm]['source_ledger'] if (r.get('returned') or 0)>0]
    return ids
sub={}
tel={'S1':(8,11,190,9),'S2':(1,21,100,7),'S3':(0,10,100,8),'S4':(1,30,75,5)}
times={'S1':('2026-11-07T02:58:32Z','2026-11-07T03:30:08Z',1896),'S2':('2026-11-07T02:58:32Z','2026-11-07T03:18:26Z',1194),'S3':('2026-11-07T02:58:33Z','2026-11-07T03:17:27Z',1134),'S4':('2026-11-07T02:58:33Z','2026-11-07T03:18:35Z',1202)}
for dm in ['S1','S2','S3','S4']:
    w,s,b,n=tel[dm]
    sub[dm]=dict(model='Sonnet 5.5',model_id='claude-sonnet-5-5',started_at=times[dm][0],ended_at=times[dm][1],duration_seconds=times[dm][2],
      sources_attempted=sa(dm),sources_used=used(dm),items_returned=n,returned=True,telemetry=dict(webfetch_calls=w,websearch_calls=s,bridge_fetches=b))
fu={'FU1':('2026-11-07T03:33:36Z','2026-11-07T03:49:18Z',942,(2,0,50),4),'FU2':('2026-11-07T03:33:36Z','2026-11-07T03:46:18Z',762,(0,1,30),4),'FU3':('2026-11-07T03:33:36Z','2026-11-07T03:48:41Z',905,(0,3,37),5)}
for k,(a,b_,dur,(w,s,br),n) in fu.items():
    sub[k]=dict(model='Sonnet 5.5',model_id='claude-sonnet-5-5',started_at=a,ended_at=b_,duration_seconds=dur,sources_attempted=[],sources_used=[],items_returned=n,returned=True,telemetry=dict(webfetch_calls=w,websearch_calls=s,bridge_fetches=br))
def ff(i,url,fm,code,cls,msg,att,mit):
    return dict(id=i,url_tried=url,fetch_method=fm,status_code=code,error_class=cls,error_message=msg,attempted_methods=att,mitigation_applied=mit,covered_anyway=False)
fetch_failures=[
 ff('connectwise-trust-center','https://www.connectwise.com/company/trust/advisories','blocked',403,'transport-403','advisories page answers 403 on every transport again',['bridge:extract','bridge:url --direct'],'no substitute read; listed as a coverage gap; 403 never demotes'),
 ff('sygnia','https://www.sygnia.co/blog/','blocked',403,'transport-403','blog answers 403 on url --direct; reader pool exhausted (HTTP 402 on every key)',['bridge:url --direct','bridge:extract'],'no substitute read; listed as a coverage gap; 403 never demotes'),
 ff('ico-uk','https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/','blocked',403,'transport-403','403 on every rung including WebFetch, fourth run in a row',['bridge:extract','bridge:url --direct','webfetch','websearch'],'two WebSearch queries found no ICO notice dated in the window; 403 never demotes'),
 ff('prodaft','https://www.prodaft.com/blog','blocked',None,'no-dated-listing','no dated listing readable on any transport',['bridge:extract','bridge:url'],'no substitute read; listed as a coverage gap'),
]
bridge_uses=[
 dict(id='kev-window-diff',method='tools/kev_window_diff.py',outcome='success: one KEV addition in the 26 h window (CVE-2026-19868), NOT COVERED, published as a new entry'),
 dict(id='cisa-kev',method='tools/fetch_source.py cisa-kev',outcome='success (S1; catalogue 2026.11.06)'),
 dict(id='ncsc-ch-security-hub',method='tools/fetch_source.py ncsc-csh recent / post',outcome='success (S1, S2, FU2; post 13054 read with its edit history)'),
 dict(id='sonicwall-psirt-api',method='tools/fetch_source.py url --direct psirtapi.global.sonicwall.com vulndetail JSON',outcome='success (FU1: the affected and fixed tables the SPA page and extract drop)'),
 dict(id='ag-ch-sitemap',method='tools/fetch_source.py url --direct ag.ch/sitemap.xml + extract',outcome='success (FU3: the canton\'s own communiqué for the Aargau ordinance)'),
 dict(id='deep-read',method='FU1 to FU3 scoped cti-research deep reads (extract, url --direct, WebFetch, cisa-kev) with saved bodies under work/<run-id>/bodies/',outcome='success: 18 primaries read in full; the will-publish set exceeded eight items, so the deep read was delegated'),
 dict(id='jina-reader',method='tools/fetch_source.py jina (last rung)',outcome='unavailable: every key in the pool answered HTTP 402; no read needed it (feed, extract, url --direct and WebFetch sufficed)'),
]
# sources_changed from diff
sc=[]
for i,x in N.items():
    o=O.get(i)
    if o is None:
        sc.append(dict(id=i,change='added',to='candidate',reason=(x.get('notes') or '')[:240])); continue
    if x.get('last_successful_fetch')!=o.get('last_successful_fetch'):
        sc.append(dict(id=i,change='last_successful_fetch',to=x['last_successful_fetch'],reason='fetched and used'))
    for f in ('status','fetch_method','rss_url'):
        if x.get(f)!=o.get(f):
            reason={'status':'promotion_due: cited by published entries from 3 or more distinct runs'}.get(f,'recipe fix, see the notes appended to the record')
            sc.append(dict(id=i,change=f,to=x.get(f),reason=reason))
    if (x.get('notes') or '')!=(o.get('notes') or ''):
        add=(x['notes'][len(o.get('notes') or ''):]).strip(' |')
        sc.append(dict(id=i,change='notes',to='recipe note appended',reason=add[:240]))
# entities added
def keys(t): return re.findall(r'^  - key: "([^"]+)"',t,flags=re.M)
ek_new=set(keys(open('entities/registry.yaml',encoding='utf-8').read())); ek_old=set(keys(head('entities/registry.yaml')))
ents=sorted(ek_new-ek_old)
upd=['2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack','2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole','2026-10-30/wordpress-core-7-1-4-unauthenticated-upgrade-window-rce-race','2026-09-15/cve-2026-76461-cisco-secure-email-gateway-sqli-root-rce','2026-08-13/cve-2026-58115-simatic-iot2050-node-red-unauth-root','2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse']
fm=dict(schema=1,run_id=RID,kind='intel',date=TODAY,started='2026-11-07T02:56:04Z',completed='2026-11-07T04:30:00Z',duration_seconds=5636,
 model='Sonnet 5.5',model_id='claude-sonnet-5-5',prompt_version='v4.24',window_hours=26,gap_hours=24.0,
 entries_published=7,entries_updated=6,updated_entry_ids=upd,deep_dive=None,sub_agents=sub,fetch_failures=fetch_failures,bridge_uses=bridge_uses,
 sources_changed=sc,entities_added=ents,entries_dropped_by_verification=0,publish_status='pending',publish_checked_at=None,publish_note=None)
open(f'{RUN}/runfm.json','w').write(json.dumps(fm,indent=1,ensure_ascii=False))
print(len(sc),len(ents)); print(ents)
