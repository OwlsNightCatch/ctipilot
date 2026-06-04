#!/usr/bin/env python3
import json

RUN_ID="2026-06-04-51b23ffa"
TODAY="2026-06-04"
STARTED="2026-06-04T04:07:53Z"
COMPLETED="2026-06-04T04:33:16Z"
DUR=1523

def load(p):
    with open(p) as f: return json.load(f)
def save(p,d):
    with open(p,"w") as f:
        json.dump(d,f,indent=2,ensure_ascii=False); f.write("\n")

slices={}
for k in ["S1","S2","S3","S4"]:
    slices[k]=[s["id"] for s in load(f"work/{RUN_ID}/sources.{k}.json")]

sub={
 "S1":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-04T04:11:11Z","ended_at":"2026-06-04T04:14:32Z","duration_seconds":201,
   "sources_attempted":slices["S1"],"sources_used":["cisa-kev","cisco-psirt","bsi-de"],"items_returned":4,"returned":True,
   "telemetry":{"webfetch_calls":8,"websearch_calls":6,"bridge_fetches":8}},
 "S2":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-04T04:11:19Z","ended_at":"2026-06-04T04:17:47Z","duration_seconds":388,
   "sources_attempted":slices["S2"],"sources_used":["ncsc-ch-security-hub","ncsc-ch-focus","heise-sec","bsi-de"],"items_returned":6,"returned":True,
   "telemetry":{"webfetch_calls":8,"websearch_calls":16,"bridge_fetches":12}},
 "S3":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-04T04:11:28Z","ended_at":"2026-06-04T04:16:36Z","duration_seconds":308,
   "sources_attempted":slices["S3"],"sources_used":["hackernews","huntress","securityweek","bleepingcomputer"],"items_returned":7,"returned":True,
   "telemetry":{"webfetch_calls":18,"websearch_calls":8,"bridge_fetches":12}},
 "S4":{"model":"Claude Sonnet 4.6","model_id":"claude-sonnet-4-6","started_at":"2026-06-04T04:11:35Z","ended_at":"2026-06-04T04:17:22Z","duration_seconds":347,
   "sources_attempted":slices["S4"],"sources_used":["us-treasury-ofac","securityweek","risky-biz-news","bleepingcomputer"],"items_returned":5,"returned":True,
   "telemetry":{"webfetch_calls":14,"websearch_calls":7,"bridge_fetches":8}},
}

fetch_failures=[
 {"id":"databreaches-net","url_tried":"https://databreaches.net/2026/06/02/data-of-600000-gaza-households-exposed-in-world-food-programme-cyberattack/","fetch_method":"bridge:url","status_code":403,"error_class":"transport-403","error_message":"fetch_source: upstream HTTP 403; bridge + Wayback both failed","attempted_methods":["bridge:url","bridge:wayback"],"mitigation_applied":"WFP/Dutch-hotel stories covered via UpGuard / DutchNews / Techzine","covered_anyway":False},
 {"id":"inside-it-ch","url_tried":"https://www.inside-it.ch/","fetch_method":"bridge:url","status_code":403,"error_class":"transport-403","error_message":"persistent 403 (4th consecutive run); bridge returned HTML shell without article content","attempted_methods":["webfetch","bridge:url","bridge:wayback"],"mitigation_applied":"CH/EU coverage via heise-sec and NCSC.ch","covered_anyway":False},
 {"id":"sophos-xops","url_tried":"https://news.sophos.com/en-us/category/threat-research/","fetch_method":"webfetch","status_code":503,"error_class":"transport-5xx","error_message":"feed URLs returned empty/503 (4th consecutive run); no in-window alternate","attempted_methods":["webfetch","rss"],"mitigation_applied":"none — no new in-window Sophos items","covered_anyway":False},
]

bridge_uses=[
 {"id":"cisa-kev","method":"bridge:cisa-kev","outcome":"ok"},
 {"id":"bsi-de","method":"bridge:bsi-rss","outcome":"ok"},
 {"id":"ncsc-ch-security-hub","method":"bridge:url","outcome":"ok"},
 {"id":"databreaches-net","method":"bridge:url","outcome":"item-not-found"},
]

rec={
 "run_id":RUN_ID,"date":TODAY,"started":STARTED,"completed":COMPLETED,"duration_seconds":DUR,
 "model":"Claude Opus 4.8","model_id":"claude-opus-4-8","prompt_version":"v2.60",
 "sub_agents":sub,
 "fetch_failures":fetch_failures,
 "bridge_uses":bridge_uses,
 "items_published":15,
 "items_dropped_by_verification":0,
 "deep_dive":"http2-bomb-cve-2026-49975",
 "verification_iterations":0,
 "verification_residual_count":0,
 "verification":{"iterations":[]},
}

rl=load("state/run_log.json")
ids=[r.get("run_id") for r in rl["runs"]]
if RUN_ID in ids:
    rl["runs"][ids.index(RUN_ID)]=rec
    print("run_log: updated existing record")
else:
    rl["runs"].append(rec)
    print("run_log: appended new record")
rl["runs"]=rl["runs"][-90:]
rl["last_updated"]=TODAY
save("state/run_log.json",rl)
print(f"run_log: total {len(rl['runs'])} runs")
