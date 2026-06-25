#!/usr/bin/env python3
import json, hashlib
from datetime import datetime, timezone

RUN_ID = "2026-06-25-da7fbd23"
TODAY = "2026-06-25"
BRIEF = "briefs/2026-06-25.md"
STARTED = "2026-06-25T04:04:25Z"
COMPLETED = "2026-06-25T04:24:09Z"

def load(p):
    with open(p) as f: return json.load(f)
def save(p, d):
    with open(p, "w") as f: json.dump(d, f, indent=2, ensure_ascii=False); f.write("\n")

dur = int((datetime.fromisoformat(COMPLETED.replace("Z","+00:00")) -
           datetime.fromisoformat(STARTED.replace("Z","+00:00"))).total_seconds())

# ---------- cves_seen.json ----------
cs = load("state/cves_seen.json")
existing = {c["id"] for c in cs["cves"]}
new_cves = [
  ("CVE-2026-56447","MISP <2.5.42 — rdkafka plugin-load RCE (site-admin)","https://github.com/advisories/GHSA-834x-pvxg-xh58"),
  ("CVE-2026-56446","MISP <2.5.42 — NDJSON log-injection PHP RCE (site-admin)","https://www.misp-project.org/2026/06/22/misp.2.5.42.release.html/"),
  ("CVE-2026-56425","MISP <2.5.42 — Azure-AD OAuth state-reuse session hijack","https://www.misp-project.org/2026/06/22/misp.2.5.42.release.html/"),
  ("CVE-2026-56424","MISP <2.5.42 — broken access control, cross-org hard-delete","https://www.misp-project.org/2026/06/22/misp.2.5.42.release.html/"),
  ("CVE-2026-56423","MISP <2.5.42 — cross-org IDOR overwrite","https://www.misp-project.org/2026/06/22/misp.2.5.42.release.html/"),
  ("CVE-2026-56422","MISP <2.5.42 — broken access control","https://www.misp-project.org/2026/06/22/misp.2.5.42.release.html/"),
  ("CVE-2026-39893","Cacti <1.2.31 — pre-auth SQLi in graph_view.php (rfilter)","https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc"),
  ("CVE-2026-39938","Cacti <1.2.31 — unauthenticated LFI via graph_theme","https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc"),
  ("CVE-2026-39948","Cacti <1.2.31 — pre-auth SQLi","https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc"),
  ("CVE-2026-39955","Cacti <1.2.31 — pre-auth SQLi","https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc"),
  ("CVE-2026-39949","Cacti <1.2.31 — authenticated RCE via host-variable injection","https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc"),
]
added=[]
for cid,title,url in new_cves:
    if cid in existing:
        for c in cs["cves"]:
            if c["id"]==cid: c["last_seen"]=TODAY
    else:
        cs["cves"].append({"first_seen":TODAY,"id":cid,"last_seen":TODAY,
                           "primary_source_url":url,"title":title})
        added.append(cid)
cs["last_updated"]=TODAY
cs["cves"].sort(key=lambda c:c["id"])
save("state/cves_seen.json", cs)
print("cves added:", added)

# ---------- covered_items.json ----------
ci = load("state/covered_items.json")
def upsert(key,typ,title,section,url,delta):
    for it in ci["items"]:
        if it["key"]==key:
            it["last_covered"]=TODAY
            it["appearances"].append({"date":TODAY,"section":section,"brief_path":BRIEF,"delta_summary":delta})
            if url: it["primary_source_url"]=it.get("primary_source_url") or url
            return "updated"
    ci["items"].append({"key":key,"type":typ,"title":title,"first_covered":TODAY,
        "last_covered":TODAY,"primary_source_url":url,
        "appearances":[{"date":TODAY,"section":section,"brief_path":BRIEF,"delta_summary":delta}]})
    return "new"

records = [
  ("campaign:ncsc-ch-m365-voicemail-phishing-week25","campaign","NCSC-CH Week 25 M365 voicemail phishing wave (CH)","active_threats","https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_25.html","First coverage. Dual-path ZIP-infostealer / fake-login M365 credential theft in CH; downstream BEC + chain phishing."),
  ("campaign:operation-endgame-amadey-stealc","campaign","Operation Endgame — Amadey/StealC MaaS takedown","active_threats","https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/","First coverage of the Amadey/StealC phase (distinct from 06-19 SocGholish/TA569). 326 servers, 142 domains, ~27M creds, EUR41M frozen; StealC C2 panel directory-traversal used by IBM X-Force/Proofpoint."),
  ("tool:mistic-mltbackdoor","tool","Mistic / MLTBackdoor backdoor (Woodgnat/KongTuke IAB)","active_threats","https://www.broadcom.com/support/security-center/protection-bulletin/backdoor-mistic-new-backdoor-may-be-linked-to-ransomware-access-broker","First coverage. Signed-Defender (MpExtMs.exe) sideload of EndpointDlp.dll; in-memory BOF execution; sells to Qilin/Interlock/Rhysida/Akira/8Base/Black Basta."),
  ("vulnerability-trend:arista-eos-tunnel-decapsulation","vulnerability-trend","Arista EOS tunnel-decapsulation flaw (exploited, no patch)","active_threats","https://eclypsium.com/blog/arista-eos-tunnel-decapsulation-no-patch/","First coverage. Eclypsium reports ITW exploitation; no patch for EOS 4.x; config mitigation (disable IP-in-IP/GRE, drop IPPROTO 4/47). No CVE published."),
  ("tool:edgecution-payouts-kings","tool","Edgecution — Edge extension Native Messaging sandbox-to-host bridge (Payouts Kings)","deep_dive","https://www.zscaler.com/blogs/security-research/payouts-king-ransomware-initial-access-broker-deploys-new-edgecution","First coverage. Deep dive. Headless Edge extension relays C2 to host Python backdoor via Native Messaging API; Teams IT-helpdesk lure; CloudFront C2."),
  ("CVE-2026-56447","cve","MISP 2.5.42 security release (6 CVEs incl. 2 RCE)","trending_vulns","https://www.misp-project.org/2026/06/22/misp.2.5.42.release.html/","First coverage. Site-admin RCE (rdkafka plugin-load + ndjson PHP injection), Azure-AD OAuth state-reuse, broken access control. EU CERT/CSIRT TIP."),
  ("CVE-2026-39893","cve","Cacti 1.2.31 — pre-auth SQLi cluster + unauth LFI","trending_vulns","https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc","First coverage. Pre-auth SQLi in graph_view.php (rfilter) reachable via default guest viewing; ENISA EUVD indexed 06-24."),
  ("campaign:cordyceps-github-actions-pwn-request","campaign","Cordyceps — GitHub Actions pull_request_target pwn-request class","research","https://novee.security/blog/cordyceps/","First coverage. 300+/30,000 repos fully exploitable from one unauth PR (Azure Sentinel, Google ADK, Apache Doris, Cloudflare, PSF Black); actions/checkout v7 mitigation."),
  ("campaign:klue-icarus-salesforce-oauth-breach","campaign","Klue/Icarus Salesforce OAuth-token breach","updates","https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/","UPDATE: BeyondTrust and LastPass added to named-victim list (now 14+); BeyondTrust is a PAM vendor. LastPass vaults unaffected."),
]
res={}
for r in records: res[r[0]]=upsert(*r)
ci["last_updated"]=TODAY
save("state/covered_items.json", ci)
print("covered_items:", res)

# ---------- deep_dive_history.json ----------
dd = load("state/deep_dive_history.json")
dd["entries"].append({"date":TODAY,"category":"endpoint-rce",
  "title":"Edgecution — abusing the Chrome/Edge Native Messaging API as a browser-sandbox-to-host bridge (Payouts Kings IAB)",
  "primary_cve":None,"brief_path":BRIEF})
dd["entries"]=dd["entries"][-30:]
dd["last_updated"]=TODAY
save("state/deep_dive_history.json", dd)
print("deep_dive appended: endpoint-rce / Edgecution")

# ---------- run_log.json ----------
rl = load("state/run_log.json")
def sub(model,mid,sa,ea,dsec,att,used,items,tele):
    return {"model":model,"model_id":mid,"started_at":sa,"ended_at":ea,
            "duration_seconds":dsec,"sources_attempted":att,"sources_used":used,
            "items_returned":items,"returned":True,"telemetry":tele}
record = {
  "run_id":RUN_ID,"date":TODAY,"started":STARTED,"completed":COMPLETED,
  "duration_seconds":dur,
  "model":"Claude Opus 4.8 (1M context)","model_id":"claude-opus-4-8[1m]",
  "prompt_version":"v2.64",
  "sub_agents":{
    "S1":sub("Claude Sonnet 4.6","claude-sonnet-4-6","2026-06-25T04:05:34Z","2026-06-25T04:16:43Z",669,
        ["cisa-kev","cert-eu","ncsc-ch-security-hub","ncsc-nl","msrc-blog","broadcom-symantec","zscaler-threatlabz","elastic-seclabs","eclypsium","novee-security","zafran","socket-dev-blog","enisa"],
        ["broadcom-symantec","zscaler-threatlabz","eclypsium","novee-security","elastic-seclabs"],9,
        {"webfetch_calls":12,"websearch_calls":14,"bridge_fetches":18}),
    "S2":sub("Claude Sonnet 4.6","claude-sonnet-4-6","2026-06-25T04:05:50Z","2026-06-25T04:14:07Z",497,
        ["ncsc-ch-security-hub","enisa","cert-eu","cert-fr-avis","inside-it-ch","ccb-belgium","bsi-de","infoguard-labs","github-advisory"],
        ["ncsc-ch-security-hub","enisa","github-advisory","infoguard-labs"],4,
        {"webfetch_calls":9,"websearch_calls":13,"bridge_fetches":8}),
    "S3":sub("Claude Sonnet 4.6","claude-sonnet-4-6","2026-06-25T04:06:05Z","2026-06-25T04:13:03Z",418,
        ["msft-ti","eset","bleepingcomputer","helpnetsecurity","novee-security","securityweek","zafran","socket-dev-blog","schneier","elastic-seclabs","huntress","mandiant-gtig","sophos-xops"],
        ["msft-ti","eset","bleepingcomputer","novee-security","securityweek","zafran","socket-dev-blog","elastic-seclabs"],5,
        {"webfetch_calls":16,"websearch_calls":6,"bridge_fetches":6}),
    "S4":sub("Claude Sonnet 4.6","claude-sonnet-4-6","2026-06-25T04:06:15Z","2026-06-25T04:15:36Z",561,
        ["hackernews","securityweek","therecord","cyberscoop","helpnetsecurity","databreaches-net","ico-uk","cnil-fr","sec-disclosures-edgar"],
        ["securityweek","therecord","cyberscoop","helpnetsecurity"],3,
        {"webfetch_calls":10,"websearch_calls":10,"bridge_fetches":9}),
  },
  "fetch_failures":[
    {"id":"databreaches-net","url_tried":"https://databreaches.net/","fetch_method":"bridge:url",
     "status_code":403,"error_class":"transport-403",
     "error_message":"HTTP 403 on bridge fetch (third consecutive run)",
     "attempted_methods":["bridge:url","websearch"],
     "mitigation_applied":"WebSearch fallback; no in-window qualifying disclosures not already covered by primary sources",
     "covered_anyway":False}
  ],
  "sources_changed":[],
  "items_published":9,
  "items_dropped_by_verification":0,
  "deep_dive":"edgecution-native-messaging-bridge",
  "verification_iterations":0,
  "verification_residual_count":0,
  "verification":{"iterations":[]},
  "bridge_uses":[]
}
# idempotent
rl["runs"]=[r for r in rl["runs"] if r.get("run_id")!=RUN_ID]
rl["runs"].append(record)
rl["runs"]=rl["runs"][-90:]
rl["last_updated"]=TODAY
save("state/run_log.json", rl)
print("run_log appended:", RUN_ID, "duration_seconds", dur)

# ---------- sources/sources.json bookkeeping ----------
srcs = load("sources/sources.json")
# ids that contributed content this run (must exist in sources.json to bump)
contributed = {"ncsc-ch-security-hub","enisa","github-advisory","infoguard-labs",
               "msft-ti","eset","bleepingcomputer","securityweek","helpnetsecurity",
               "therecord","cyberscoop","elastic-seclabs","novee-security","zafran",
               "eclypsium","csa-labs"}
bumped=[]
present_ids={s["id"] for s in srcs["sources"]}
for s in srcs["sources"]:
    if s["id"] in contributed and s.get("status")=="active":
        s["last_successful_fetch"]=TODAY
        s["consecutive_fetch_failures"]=0
        s["consecutive_quiet_periods"]=0
        s["last_covered_in_brief"]=TODAY
        bumped.append(s["id"])
srcs["last_updated"]=TODAY
save("sources/sources.json", srcs)
print("sources bumped:", bumped)
print("contributed-not-in-sources:", sorted(contributed - present_ids))

