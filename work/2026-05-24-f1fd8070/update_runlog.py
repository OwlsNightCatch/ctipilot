#!/usr/bin/env python3
import json, datetime

TODAY="2026-05-24"; RUN_ID="2026-05-24-f1fd8070"
def load(p): return json.load(open(p))
def save(p,d): json.dump(d,open(p,"w"),indent=2,ensure_ascii=False); open(p,"a").write("\n")

started=open("work/%s/main.started_at"%RUN_ID).read().strip()
ended=open("work/%s/main.ended_at"%RUN_ID).read().strip()
def secs(a,b):
    f="%Y-%m-%dT%H:%M:%SZ"
    return int((datetime.datetime.strptime(b,f)-datetime.datetime.strptime(a,f)).total_seconds())

S1_attempt=["advisories-ncsc-nl","anssi-fr","apple-security","bsi-de","cert-eu","cert-pl","chrome-releases","cisa-advisories","cisa-directives","cisa-kev","cisco-psirt","greynoise","jpcert","mozilla-mfsa","ncsc-ch-incidents","ncsc-ch-security-hub","ncsc-uk","oracle-cpu","projectzero","rapid7-research","shadowserver","tenable-research","trustwave-spiderlabs","vulncheck","watchtowr","wiz-blog","zdi"]
S2_attempt=["advisories-ncsc-nl","anssi-fr","bsi-de","cert-at","cert-eu","cert-pl","cisa-advisories","cisa-news","citizen-lab","cnil-fr","compass-security","csirt-acn-it","edpb","enisa","govcert-at","heise-sec","ico-uk","infoguard-ch","inside-it-ch","kudelski-security","le-monde-info","ncsc-ch-focus","ncsc-ch-incidents","ncsc-ch-security-hub","ncsc-ie","ncsc-uk","oneconsult-ch","prodaft","safeonweb-be","scip-ch","sekoia","truesec","us-treasury-ofac"]
S3_attempt=["akamai-sirt","bleepingcomputer","checkpoint-research","cisa-news","cloudflare-cf1","crowdstrike","cyberscoop","darkreading","dfirreport","dragos","elastic-seclabs","eset","google-tag","hackernews","helpnetsecurity","huntress","intel471","kaspersky-securelist","krebs","malwarebytes","mandiant-gtig","msft-ti","push-security","redcanary","risky-biz-news","sans-ics","sans-isc","schneier","securityaffairs","securityweek","sentinellabs","socprime","sophos-xops","sygnia","talos","therecord","trellix","trendmicro-research","unit42","volexity"]
S4_attempt=["bleepingcomputer","cnil-fr","databreaches-net","edpb","ico-uk","sec-disclosures-edgar","troyhunt","cyberscoop","therecord","securityweek","securityaffairs","krebs","heise-sec","le-monde-info","inside-it-ch","risky-biz-news","hackernews"]

rl=load("state/run_log.json")
runs=rl["runs"]
record={
 "run_id": RUN_ID, "date": TODAY,
 "started": started, "completed": ended, "duration_seconds": secs(started,ended),
 "model": "Claude Opus 4.7", "model_id": "claude-opus-4-7",
 "prompt_version": "v2.59",
 "sub_agents": {
   "S1": {"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-05-24T04:09:46Z","ended_at":"2026-05-24T04:19:42Z","duration_seconds":596,"sources_attempted":S1_attempt,"sources_used":["ccb-belgium"],"items_returned":6,"returned":True,"telemetry":{"webfetch_calls":12,"websearch_calls":7,"bridge_fetches":14}},
   "S2": {"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-05-24T04:10:02Z","ended_at":"2026-05-24T04:22:08Z","duration_seconds":726,"sources_attempted":S2_attempt,"sources_used":["hackernews"],"items_returned":3,"returned":True,"telemetry":{"webfetch_calls":18,"websearch_calls":16,"bridge_fetches":12}},
   "S3": {"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-05-24T04:10:18Z","ended_at":"2026-05-24T04:20:53Z","duration_seconds":635,"sources_attempted":S3_attempt,"sources_used":["hackernews","helpnetsecurity"],"items_returned":5,"returned":True,"telemetry":{"webfetch_calls":24,"websearch_calls":4,"bridge_fetches":12}},
   "S4": {"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-05-24T04:10:28Z","ended_at":"2026-05-24T04:21:57Z","duration_seconds":689,"sources_attempted":S4_attempt,"sources_used":["therecord","heise-sec"],"items_returned":2,"returned":True,"telemetry":{"webfetch_calls":12,"websearch_calls":14,"bridge_fetches":18}},
 },
 "fetch_failures": [
   {"id":"sophos-xops","url_tried":"https://news.sophos.com/en-us/category/threat-research/feed/","fetch_method":"webfetch","status_code":503,"error_class":"transport-5xx","error_message":"HTTP 503 from Sophos blog feed (6th consecutive run)","attempted_methods":["webfetch"],"mitigation_applied":"none — no in-window story required this source","covered_anyway":False},
   {"id":"trendmicro-research","url_tried":"https://www.trendmicro.com/en_us/research.html","fetch_method":"webfetch","status_code":500,"error_class":"transport-5xx","error_message":"HTTP 500 from Trend Micro research landing (3rd consecutive run)","attempted_methods":["webfetch"],"mitigation_applied":"none — no in-window story required this source","covered_anyway":False},
   {"id":"databreaches-net","url_tried":"https://databreaches.net/category/breach-reports/","fetch_method":"bridge","status_code":403,"error_class":"transport-403","error_message":"Bridge HTTP 403; Wayback returned 24-byte availability placeholder only","attempted_methods":["bridge:url","webfetch"],"mitigation_applied":"WebSearch fallback — no uncovered in-window items","covered_anyway":False},
 ],
 "bridge_uses": [],
 "items_published": 7,
 "items_dropped_by_verification": 0,
 "deep_dive": "packagist-laravel-lang-supply-chain",
 "verification_iterations": 0,
 "verification_residual_count": 0,
 "verification": {"iterations": []},
}
# idempotent
runs=[r for r in runs if r.get("run_id")!=RUN_ID]
runs.append(record)
runs=runs[-90:]
rl["runs"]=runs
rl["last_updated"]=TODAY
save("state/run_log.json",rl)
print("run_log updated; runs:",len(runs),"duration_seconds:",record["duration_seconds"])
