import json,datetime
p='sources/sources.json'
s=json.load(open(p,encoding='utf-8'))
recs={r['id']:r for r in s['sources']}
TODAY='2026-10-28'
changes=[]
def note(i,who,text):
    r=recs[i]; old=r.get('notes') or ''
    add=f" | {TODAY} ({who}): {text}"
    r['notes']=old+add
    changes.append({'id':i,'change':'notes','from':None,'to':'recipe note appended','reason':f'{TODAY} ({who}): recipe note from the sub-agent source ledger, text in sources.json'})
used=['cisa-kev','cisa-advisories','paloalto-psirt','hpe-networking-psirt','mysites-guru','tenable-research','inside-it-ch','iverify-blog','report-uri-blog']
for i in used:
    r=recs[i]; old=r.get('last_successful_fetch')
    if old!=TODAY:
        r['last_successful_fetch']=TODAY
        r['consecutive_quiet_periods']=0
        changes.append({'id':i,'change':'last_successful_fetch','from':old,'to':TODAY,'reason':'fetched and used'})
# failures that never demote
for i,reason in [('connectwise-trust-center','403 on direct, extract, url, the reader and WebFetch again; a 403 never demotes'),
                 ('ec-digital-strategy-newsroom','403 (CloudFront) on every transport for the third run; a 403 never demotes')]:
    r=recs[i]; old=r.get('consecutive_fetch_failures',0)
    r['consecutive_fetch_failures']=old+1
    changes.append({'id':i,'change':'consecutive_fetch_failures','from':old,'to':old+1,'reason':reason})
note('hpe-networking-psirt','S1','https://csaf.arubanetworking.hpe.com/changes.csv (read with `url --direct`) lists every CSAF file with its release timestamp, so new bulletins can be enumerated without guessing ids.')
note('cisco-psirt','S1','`feed https://sec.cloudapps.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml 25` returns dated items including Interim revisions; the advisory page reads with extract (prose) and `url --direct` (vulnerable-products table, revision history).')
note('paloalto-psirt','S1','https://security.paloaltonetworks.com/json/CVE-<id> returns the advisory as CVE JSON with `exploits`, CVSS 4.0 metrics and a timestamped timeline; extract of the HTML page drops the Timeline.')
note('inside-it-ch','S2','extract may return the raw page; the full article body is in the __NEXT_DATA__ JSON at props.pageProps.post.post.managed.published.elements[0].data.rawState.blocks[*].text.')
note('apa-ots','S2','the feed https://www.ots.at/rss/index works but holds only the 15 newest releases (about 3 h), so a 168 h lookback sweep is impossible through it.')
note('ransomware-live','S4','the API v2 (api.ransomware.live/v2/groupvictims/<group>) works; the per-victim id pages time out (>100 s) through extract and url.')
note('databreaches-net','S4','the feed timed out twice on 2026-10-28; `extract https://databreaches.net/` reads the front page.')
# promotion
r=recs['karimi-honeypot-data']
if r['status']!='active':
    r['status']='active'
    changes.append({'id':'karimi-honeypot-data','change':'status','from':'candidate','to':'active','reason':'sources.promotion_due: cited by published entries from at least three distinct runs'})
# new candidates
def add_cand(rec,reason):
    assert rec['id'] not in recs
    s['sources'].append(rec); recs[rec['id']]=rec
    changes.append({'id':rec['id'],'change':'added','from':None,'to':'candidate','reason':reason})
base=dict(consecutive_failures=0,consecutive_fetch_failures=0,consecutive_quiet_periods=0,status='candidate',tier='standard',language=['en'])
add_cand({**base,'id':'ellio-threat-research','publisher':'ELLIO Threat Research Lab','category':['research','vulns'],'fetch_method':'bridge','reliability':'B','url':'https://ellio.tech/en/blog/','last_successful_fetch':TODAY,
  'notes':'Added 2026-10-28 (S1): first-hand internet-scale sensor telemetry on mass exploitation; its post of 2026-10-26 recorded the first exploit traffic for CVE-2026-111497 and is cited by the Node2Shell entry. No RSS (feed and sitemap paths 404); `extract https://ellio.tech/en/blog/` reads titles and teasers without hrefs, WebFetch of the listing returns the hrefs, and `extract <post URL>` reads a post. Candidate: promote to active after 3 contributing runs.',
  'health_cmd':['extract','https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/']},'first-hand exploitation telemetry cited by a published entry')
add_cand({**base,'id':'jfrog-security-research','publisher':'JFrog Security Research','category':['research','vulns'],'fetch_method':'rss','reliability':'B','url':'https://research.jfrog.com/','rss_url':'https://research.jfrog.com/rss.xml','last_successful_fetch':TODAY,
  'notes':'Added 2026-10-28 (S3): original vulnerability research with reproductions (Brotli2Shell reach into FFmpeg and ClickHouse, cited by the Node2Shell entry); the feed https://research.jfrog.com/rss.xml carries dated posts and article bodies read with `extract`. Candidate: promote to active after 3 contributing runs.'},'original research cited by a published entry')
s['last_updated']=TODAY
open(p,'w',encoding='utf-8').write(json.dumps(s,indent=1)+'\n')
open('work/2026-10-28T0256Z-intel/sources_changed.json','w').write(json.dumps(changes,indent=1,ensure_ascii=False))
print(len(changes),'changes')
