import yaml,json,datetime
R='2026-10-28T0256Z-intel'
import datetime as _dt
_n=_dt.datetime.strptime(open('work/2026-10-28T0256Z-intel/main.ended_at').read().strip(),'%Y-%m-%dT%H:%M:%SZ')
NOW=_n.strftime('%Y-%m-%dT%H:%M:%SZ')
DUR=int((_n-_dt.datetime(2026,10,28,2,56,12)).total_seconds())
W=f'work/{R}'
def att(dm):
    d=yaml.safe_load(open(f'{W}/findings.{dm}.yaml'))
    return [r['id'] for r in d['source_ledger'] if r.get('attempted')]
used={'S1':['cisa-kev','cisa-advisories','paloalto-psirt','hpe-networking-psirt','mysites-guru','tenable-research'],'S2':['inside-it-ch'],'S3':['iverify-blog','report-uri-blog'],'S4':[]}
tele={'S1':(11,19,120,8,'2026-10-28T02:58:29Z','2026-10-28T03:29:30Z',1861),'S2':(2,37,95,6,'2026-10-28T02:58:29Z','2026-10-28T03:26:39Z',1690),'S3':(3,18,150,11,'2026-10-28T02:58:29Z','2026-10-28T03:22:50Z',1461),'S4':(2,41,95,9,'2026-10-28T02:58:29Z','2026-10-28T03:32:59Z',2070)}
subs={}
for dm,(wf,ws,bf,items,s,e,dur) in tele.items():
    subs[dm]={'model':'Sonnet 5.5','model_id':'claude-sonnet-5-5','started_at':s,'ended_at':e,'duration_seconds':dur,'sources_attempted':att(dm),'sources_used':used[dm],'items_returned':items,'returned':True,'telemetry':{'webfetch_calls':wf,'websearch_calls':ws,'bridge_fetches':bf}}
fm={
 'schema':1,'run_id':R,'kind':'intel','date':'2026-10-28','started':'2026-10-28T02:56:12Z','completed':NOW,'duration_seconds':DUR,
 'model':'Sonnet 5.5','model_id':'claude-sonnet-5-5','prompt_version':'v4.24','window_hours':26,'gap_hours':24.0,
 'entries_published':5,'entries_updated':9,
 'updated_entry_ids':['2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave','2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619','2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release','2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27','2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi','2026-10-26/cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix','2026-09-30/manno-ti-commune-ransomware-safepay-claim','2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud','2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups'],
 'deep_dive':None,'sub_agents':subs,
 'fetch_failures':[
  {'id':'connectwise-trust-center','url_tried':'https://www.connectwise.com/company/trust/advisories','fetch_method':'bridge:url','status_code':403,'error_class':'transport-403','error_message':'403 on direct, extract, url, the reader and WebFetch; no readable body (failing on every run since 2026-10-19)','attempted_methods':['bridge:url','bridge:extract','jina','webfetch'],'mitigation_applied':'status.connectwise.com read with extract (only the covered 2026-10-16 incident) and a WebSearch for October 2026 advisories found nothing new','covered_anyway':False},
  {'id':'ec-digital-strategy-newsroom','url_tried':'https://digital-strategy.ec.europa.eu/en/news','fetch_method':'bridge:extract','status_code':403,'error_class':'transport-403','error_message':'403 (CloudFront) on extract, the reader fallback, url and WebFetch','attempted_methods':['bridge:extract','bridge:url','jina','webfetch'],'mitigation_applied':'Commission policy items probed by WebSearch; nothing dated in the window surfaced','covered_anyway':False},
  {'id':'resecurity','url_tried':'https://www.resecurity.com/blog','fetch_method':'bridge:extract','status_code':200,'error_class':'js-shell','error_message':'extract returns an empty JavaScript shell; no in-container reader for the listing','attempted_methods':['bridge:extract','webfetch','websearch'],'mitigation_applied':'WebSearch restricted to resecurity.com lists dated article pages; the newest post is 2026-10-14, outside the horizon','covered_anyway':False},
  {'id':'golem-security','url_tried':'https://www.golem.de/specials/security/','fetch_method':'bridge:extract','status_code':200,'error_class':'cookie-wall','error_message':'listing sits behind a cookie wall for every in-container transport','attempted_methods':['bridge:extract','bridge:url'],'mitigation_applied':'heise-sec and Inside IT cover the same DACH news','covered_anyway':False},
 ],
 'bridge_uses':[
  {'id':'kev-window-diff','method':'tools/kev_window_diff.py','outcome':'success (2 KEV additions of 2026-10-27: CVE-2026-111497 COVERED-STALE on two store entries, CVE-2026-48356 NOT COVERED; dispositions in the notes)'},
  {'id':'cisa-kev','method':'tools/fetch_source.py cisa-kev','outcome':'success (S1 and the main agent: catalogVersion 2026.10.27 lists the PHP flaws from 2026-10-26)'},
  {'id':'deep-read-primaries','method':'tools/fetch_source.py extract / url --direct','outcome':'success (CISA alert, ELLIO, Tenable, JFrog, Akamai, Cisco node.js and PHP advisories, Palo Alto advisory HTML and JSON, Citrix CTX697263, CERT-FR, HPE CSAF, Balbooa, mySites.guru, Inside IT __NEXT_DATA__, DeXpose, Hüttenberg, Netzwoche, IDC Frontier reports 6 and 7, Report URI, iVerify saved under work/<run-id>/bodies)'},
 ],
 'sources_changed':[],'entities_added':[],
 'entries_dropped_by_verification':0,
 'publish_status':'pending','publish_checked_at':None,'publish_note':None,
 'verification_iterations':0,'verification_residual_count':0,
 'verification':{'confirmation_waived':None,'iterations':[]},
}
for c in json.load(open(f'{W}/sources_changed.json')):
    fm['sources_changed'].append({'id':c['id'],'change':c['change'],'from':c['from'],'to':c['to'],'reason':c['reason']})
_it=json.load(open(f'{W}/verification_iters.json'))
fm['verification']['iterations']=_it
fm['verification_iterations']=len(_it)
fm['verification']['confirmation_waived']='the first CLEAN verdict landed at the 8-iteration cap (iteration 8), so no confirmation pass was possible; iterations 1 to 7 each returned NEEDS_FIXES and iteration 8 walked all 339 ledger claims with none unsupported'
_last=_it[-1]
fm['verification_residual_count']=(_last['truth']+_last['editorial']) if _last['verdict']=='NEEDS_FIXES' else 0
fm['entities_added']=['incident:ara-region-lyss-limpachtal-ransomware-2026-09','campaign:deadtag','tool:coruna','tool:darksword','product:cisco-expressway-select-series','product:cisco-identity-services-engine-portal-builder','product:cisco-ultra-reliable-wireless-backhaul','product:cisco-unified-industrial-wireless-software','product:hpe-networking-clearpass-policy-manager','product:bun','product:istio']
body=open(f'{W}/records/run_notes.md').read()
class D(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)
out='---\n'+yaml.dump(fm,Dumper=D,sort_keys=False,width=1000,allow_unicode=True,default_flow_style=None)+'---\n\n'+body
import os
os.makedirs('runs/2026-10-28',exist_ok=True)
open(f'runs/2026-10-28/{R}.md','w',encoding='utf-8').write(out)
print('written',len(out))
