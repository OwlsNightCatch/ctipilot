import yaml,json,sys
RUN='2026-11-19T0355Z-intel'
sa=json.load(open(f'work/{RUN}/derived.sub_agents.json'))
fix={'S1':('2026-11-19T03:57:36Z','2026-11-19T04:35:37Z'),'S2':('2026-11-19T03:57:36Z','2026-11-19T04:20:29Z'),'S3':('2026-11-19T03:57:35Z','2026-11-19T04:23:34Z'),'S4':('2026-11-19T03:57:36Z','2026-11-19T04:22:06Z')}
for s,(a,b) in fix.items(): sa[s]['started_at']=a; sa[s]['ended_at']=b
upd=['2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16','2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce','2026-09-22/cve-2026-13684-synology-dsm-unauth-file-read-write','2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i','2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce','2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router','2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap','2026-10-23/hpesbnw05162-hpe-aruba-aos-8-aos-10-72-cves-19-unauth']
def ff(id,url,m,code,cls,msg,att,mit):
    return dict(id=id,url_tried=url,fetch_method=m,status_code=code,error_class=cls,error_message=msg,attempted_methods=att,mitigation_applied=mit,covered_anyway=False)
fails=[ff('lab52','https://lab52.io/blog/','bridge:feed','n/a','connection-reset','every direct transport reset the connection, WebFetch returned 503, the reader pool is dead, Wayback TLS/429',['bridge:feed','bridge:extract','webfetch','bridge:jina'],'a WebSearch cache shows the newest post is 2026-10-05, so nothing inside the lookback is known to be missed'),
 ff('belden-psirt','https://www.belden.com/security','bridge:extract',403,'transport-403','HTML listing 403 on every transport, reader pool dead (402)',['bridge:extract','webfetch','bridge:jina'],'advisory PDFs on assets.belden.com read with fetch_source.py pdf and discovery by WebSearch; newest advisory PSIRT-6 of 2026-09-09'),
 ff('f5-k-articles','https://my.f5.com/manage/s/article/K000163925','bridge:extract',200,'js-shell','myF5 Salesforce single-page application: extract, WebFetch and the reader return an empty shell',['bridge:extract','webfetch','bridge:jina'],'F5 text read through the CNA record, nginx.org advisories, Rapid7, Wiz and CERT.at'),
 ff('baselland-ch','https://www.baselland.ch/politik-und-behorden/regierungsrat/medienmitteilungen','bridge:extract',403,'transport-403','canton site answers 403 on every transport',['bridge:extract','webfetch','bridge:url'],'communiques read verbatim through the Polizeiticker relay and four regional outlets; the incident is held on the backlog'),
 ff('airlock-advisory','https://www.airlock.com/security-advisories','bridge:extract',400,'js-shell','cookie-check 400 shell; WebFetch shows a disclosure policy with no advisory entries; Techzone needs a login',['bridge:extract','bridge:url-direct','webfetch'],'Airlock CNA text read through the ENISA EUVD record and the vendor documentation changelogs')]
fm={'schema':1,'run_id':RUN,'kind':'intel','date':'2026-11-19','started':'2026-11-19T03:55:51Z','completed':'2026-11-19T07:00:00Z','duration_seconds':11049,
 'model':'Sonnet 5.5','model_id':'claude-sonnet-5-5','prompt_version':'v4.25','window_hours':26,'gap_hours':24.0,
 'entries_published':6,'entries_updated':8,'updated_entry_ids':upd,'deep_dive':None,'sub_agents':sa,'fetch_failures':fails,
 'bridge_uses':[dict(id='cisa-kev',method='tools/fetch_source.py cisa-kev and tools/kev_window_diff.py',outcome='success: catalog 2026.11.18, four additions inside the window, all four now covered by an entry or a changelog record; no KEV ransomware-flag row'),
   dict(id='extract',method='tools/fetch_source.py extract',outcome='success on vendor, CERT, research and news pages and on the deep reads; drupal.org SA-018 answered a client challenge'),
   dict(id='url-direct',method='tools/fetch_source.py url --direct',outcome='success: ENISA EUVD, raw GitHub files, CNA records, listings'),
   dict(id='ncsc-csh',method='tools/fetch_source.py ncsc-csh post',outcome='success: Security Hub posts 13196, 13198 and 13203'),
   dict(id='pdf',method='tools/fetch_source.py pdf',outcome='success: Belden advisory PDFs'),
   dict(id='webfetch',method='WebFetch with the outbound-links template',outcome='success: CISA alert pages, sygnia.co listing, Drupal SA-018 cross-check'),
   dict(id='jina-reader',method='tools/fetch_source.py jina (last rung)',outcome='dead: HTTP 402 on every pooled key')],
 'sources_changed':[dict(change='added candidate',id='nginx-security-advisories',reason='project primary with per-CVE ranges, the only readable F5 or nginx source for the nginx2root entry'),
   dict(change='added candidate',id='unit42-timely-threat-intel',reason='dated plain-text exploitation notes; its REDCap note predated the CISA listing by six weeks'),
   dict(change='added candidate',id='polizeiticker-ch',reason='RSS relay of cantonal police communiques that carried the Basel-Landschaft incident while baselland.ch refused every transport'),
   dict(change='promoted to active',id='mitel-security-advisories',reason='three contributing runs (sources.promotion_due)'),
   {'change':'fetch_method','id':'sygnia','from':'blocked','to':'webfetch','reason':'WebFetch with the outbound-links template now reads the listing; failure counter reset'},
   dict(change='health_cmd',id='typo3-security-advisories, cnil-fr',reason='source_health UNSOLVED list: the landing page carries no security vocabulary (typo3, recipe is the feed) and the 503 origin fell through to the metered reader (cnil, now url --direct); not re-probed, source_health has no single-source mode'),
   dict(change='notes',id='lab52, belden-psirt',reason='no transport reads lab52; Belden advisories read as PDFs on assets.belden.com'),
   dict(change='last_successful_fetch',id='cisa-kev, enisa-euvd, fortinet-psirt, advisories-ncsc-nl, cert-at, cert-eu, ncsc-ch-security-hub, zscaler-threatlabz, cyderes-howler-cell',reason='fetched and used by an entry or a changelog record published this run'),
   dict(change='consecutive_quiet_periods',id='(64 slice records)',reason='200 but nothing publishable in the horizon: counters incremented by one; the 9 sources used were reset to 0')],
 'entities_added':['actor:tcherber','malware:enigma-locker','incident:cyberpower-powerpanel-dc-intrusion-2026-11','product:airlock-gateway','product:cisco-catalyst-center','product:cisco-secure-network-analytics','product:cisco-secure-workload','product:cyberpower-powerpanel-business','product:idunno-anticsrf','product:redcap','product:trend-micro-deep-discovery-analyzer'],
 'entries_dropped_by_verification':0,'publish_status':'pending','publish_checked_at':None,'publish_note':None,
 'verification_iterations':0,'verification_residual_count':0,'verification':{'confirmation_waived':None,'iterations':[]}}
body=open(f'work/{RUN}/rec/run_body.md',encoding='utf-8').read() if len(sys.argv)>1 else '\n## Verification & coverage notes\n\nPLACEHOLDER\n'
class D(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)
txt='---\n'+yaml.dump(fm,Dumper=D,sort_keys=False,allow_unicode=True,width=10000)+'---\n'+body
open(f'runs/2026-11-19/{RUN}.md','w',encoding='utf-8').write(txt)
print(len(txt))
