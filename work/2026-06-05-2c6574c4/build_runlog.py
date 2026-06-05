import json
RUN_ID="2026-06-05-2c6574c4"
started=open(f"work/{RUN_ID}/main.started_at").read().strip()
ended=open(f"work/{RUN_ID}/main.ended_at").read().strip()
def secs(a,b):
    from datetime import datetime
    f="%Y-%m-%dT%H:%M:%SZ"
    return int((datetime.strptime(b,f)-datetime.strptime(a,f)).total_seconds())
sub={
 "S1":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-05T04:12:04Z","ended_at":"2026-06-05T04:22:14Z","duration_seconds":610,
   "sources_attempted":["advisories-ncsc-nl","anssi-fr","apple-security","bsi-de","cert-eu","cert-pl","chrome-releases","cisa-advisories","cisa-directives","cisa-kev","cisco-psirt","greynoise","jpcert","mozilla-mfsa","ncsc-ch-incidents","ncsc-ch-security-hub","ncsc-uk","oracle-cpu","projectzero","rapid7-research","shadowserver","tenable-research","trustwave-spiderlabs","vulncheck","watchtowr","wiz-blog","zdi"],
   "sources_used":["hackernews","securityweek","wiz-blog"],"items_returned":4,"returned":True,
   "telemetry":{"webfetch_calls":18,"websearch_calls":14,"bridge_fetches":10}},
 "S2":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-05T04:12:05Z","ended_at":"2026-06-05T04:18:07Z","duration_seconds":362,
   "sources_attempted":["advisories-ncsc-nl","anssi-fr","bsi-de","cert-at","cert-eu","cert-pl","cisa-advisories","cisa-directives","cisa-news","citizen-lab","cnil-fr","compass-security","crowdstrike","csirt-acn-it","edpb","enisa","google-tag","govcert-at","heise-sec","ibm-xforce","ico-uk","infoguard-ch","inside-it-ch","jpcert","kudelski-security","le-monde-info","mandiant-gtig","msft-ti","ncc-research","ncsc-ch-focus","ncsc-ch-incidents","ncsc-ch-security-hub","ncsc-ie","ncsc-uk","oneconsult-ch","prodaft","recordedfuture-insikt","safeonweb-be","scip-ch","sekoia","truesec","us-treasury-ofac","withsecure-labs"],
   "sources_used":["cert-pl","heise-sec"],"items_returned":5,"returned":True,
   "telemetry":{"webfetch_calls":9,"websearch_calls":15,"bridge_fetches":7}},
 "S3":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-05T04:12:14Z","ended_at":"2026-06-05T04:20:55Z","duration_seconds":521,
   "sources_attempted":["akamai-sirt","bleepingcomputer","checkpoint-research","dfirreport","dragos","elastic-seclabs","eset","hackernews","huntress","kaspersky-securelist","mandiant-gtig","prodaft","proofpoint-blog","redcanary","sans-isc","securityaffairs","securityweek","sentinellabs","sophos-xops","talos","trendmicro-research","unit42","volexity","wiz-blog","zdi"],
   "sources_used":["volexity","unit42","wiz-blog","hackernews","bleepingcomputer","securityweek"],"items_returned":5,"returned":True,
   "telemetry":{"webfetch_calls":0,"websearch_calls":4,"bridge_fetches":28}},
 "S4":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-05T04:12:24Z","ended_at":"2026-06-05T04:22:18Z","duration_seconds":594,
   "sources_attempted":["bleepingcomputer","cnil-fr","databreaches-net","edpb","hackernews","ico-uk","krebs","risky-biz-news","sans-isc","sec-disclosures-edgar","securityaffairs","securityweek","therecord"],
   "sources_used":["bleepingcomputer","risky-biz-news","hackernews"],"items_returned":6,"returned":True,
   "telemetry":{"webfetch_calls":14,"websearch_calls":9,"bridge_fetches":8}},
}
rec={
 "run_id":RUN_ID,"date":"2026-06-05","started":started,"completed":ended,"duration_seconds":secs(started,ended),
 "model":"Claude Opus 4.8","model_id":"claude-opus-4-8","prompt_version":"v2.60",
 "sub_agents":sub,
 "fetch_failures":[
   {"id":"inside-it-ch","url_tried":"https://www.inside-it.ch/","fetch_method":"bridge:url","status_code":403,"error_class":"transport-403","error_message":"Bridge 403; Wayback returned no usable snapshot >=5000 bytes in last 180 days","attempted_methods":["webfetch","bridge:url","bridge:wayback"],"mitigation_applied":"none — coverage gap (6+ consecutive runs)","covered_anyway":False},
   {"id":"databreaches-net","url_tried":"https://databreaches.net/","fetch_method":"bridge:url","status_code":403,"error_class":"transport-403","error_message":"Bridge 403; Wayback fallback found 0 usable snapshots in last 180 days","attempted_methods":["bridge:url","bridge:wayback"],"mitigation_applied":"WebSearch story-awareness fallback; no unique databreaches-only items","covered_anyway":False},
   {"id":"sophos-xops","url_tried":"https://www.sophos.com/en-us/blog/feed?id=blt6f15f4f7deaf4242","fetch_method":"bridge:feed","status_code":503,"error_class":"transport-5xx","error_message":"upstream HTTP 503 on Sophos blog feed","attempted_methods":["bridge:feed","bridge:url"],"mitigation_applied":"none — coverage gap (5+ runs)","covered_anyway":False},
   {"id":"sec-disclosures-edgar","url_tried":"sec-edgar 8k 2026-06-03 2026-06-05 1.05","fetch_method":"bridge:sec-edgar","status_code":500,"error_class":"transport-5xx","error_message":"sec-edgar bridge HTTP 500; EDGAR full-text fallback returned 0 Item 1.05 filings in window","attempted_methods":["bridge:sec-edgar","bridge:url"],"mitigation_applied":"EDGAR full-text search fallback — 0 cyber 8-K filings in window","covered_anyway":False}
 ],
 "bridge_uses":[
   {"id":"cisa-kev","method":"bridge:cisa-kev","outcome":"ok"},
   {"id":"cert-pl","method":"bridge:url","outcome":"ok"},
   {"id":"volexity","method":"bridge:url","outcome":"ok"},
   {"id":"unit42","method":"bridge:url","outcome":"ok"},
   {"id":"wiz-blog","method":"bridge:url","outcome":"ok"}
 ],
 "items_published":13,
 "items_dropped_by_verification":0,
 "deep_dive":"redis-cve-2026-23479",
 "verification_iterations":0,
 "verification_residual_count":0,
 "verification":{"iterations":[]}
}
p="state/run_log.json"
d=json.load(open(p))
runs=d.get("runs",[])
runs=[r for r in runs if r.get("run_id")!=RUN_ID]
runs.append(rec)
runs=runs[-90:]
d["runs"]=runs
json.dump(d,open(p,"w"),indent=2)
print("run_log updated; runs:",len(runs),"items_published:",rec["items_published"])
