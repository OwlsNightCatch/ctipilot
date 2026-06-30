import json
RUN_ID="2026-06-30-9aaa1114"; TODAY="2026-06-30"
def started(p):
    return open(f"work/{RUN_ID}/{p}").read().strip()
main_started=started("main.started_at"); main_ended=started("main.ended_at")
from datetime import datetime
def secs(a,b):
    fmt="%Y-%m-%dT%H:%M:%SZ"
    return int((datetime.strptime(b,fmt)-datetime.strptime(a,fmt)).total_seconds())

def slice_ids(s):
    return [x["id"] for x in json.load(open(f"work/{RUN_ID}/slice.{s}.json"))]

sub=lambda model,sa,ea,dur,att,used,items,tel:{
  "model":model,"model_id":"claude-sonnet-4-6","started_at":sa,"ended_at":ea,
  "duration_seconds":dur,"sources_attempted":att,"sources_used":used,
  "items_returned":items,"returned":True,"telemetry":tel}

M="Claude Sonnet 4.6"
sub_agents={
 "S1":sub(M,"2026-06-30T04:06:14Z","2026-06-30T04:11:18Z",304,slice_ids("S1"),
         ["horizon3-ai","bleepingcomputer","advisories-ncsc-nl","cisa-kev"],4,
         {"webfetch_calls":18,"websearch_calls":6,"bridge_fetches":12}),
 "S2":sub(M,"2026-06-30T04:06:23Z","2026-06-30T04:17:08Z",645,slice_ids("S2"),
         ["cert-pl","advisories-ncsc-nl"],4,
         {"webfetch_calls":8,"websearch_calls":10,"bridge_fetches":12}),
 "S3":sub(M,"2026-06-30T04:06:35Z","2026-06-30T04:17:01Z",626,slice_ids("S3"),
         ["dfirreport","kaspersky-securelist","watchtowr","vulncheck","zdi","msft-ti","hackernews","risky-biz-news"],11,
         {"webfetch_calls":16,"websearch_calls":5,"bridge_fetches":14}),
 "S4":sub(M,"2026-06-30T04:06:43Z","2026-06-30T04:09:48Z",185,slice_ids("S4"),
         ["databreaches-net","bleepingcomputer","securityweek"],3,
         {"webfetch_calls":5,"websearch_calls":5,"bridge_fetches":10}),
}

bridge_uses=[
 {"id":"dfirreport","method":"bridge:feed","outcome":"ok"},
 {"id":"hackernews","method":"bridge:feed","outcome":"ok"},
 {"id":"sophos-xops","method":"bridge:feed","outcome":"empty-feed"},
 {"id":"risky-biz-news","method":"bridge:feed","outcome":"ok"},
 {"id":"sans-isc","method":"bridge:feed","outcome":"ok"},
 {"id":"checkpoint-research","method":"bridge:feed","outcome":"ok"},
 {"id":"kaspersky-securelist","method":"bridge:feed","outcome":"ok"},
 {"id":"wiz-blog","method":"bridge:feed","outcome":"ok"},
 {"id":"watchtowr","method":"bridge:feed","outcome":"ok"},
 {"id":"vulncheck","method":"bridge:url","outcome":"ok"},
 {"id":"msft-ti","method":"bridge:msft-secblog","outcome":"ok"},
]

rec={
 "run_id":RUN_ID,"date":TODAY,"started":main_started,"completed":main_ended,
 "duration_seconds":secs(main_started,main_ended),
 "model":"Claude Opus 4.8 (1M context)","model_id":"claude-opus-4-8",
 "prompt_version":"v2.64","kind":"daily",
 "sub_agents":sub_agents,
 "fetch_failures":[],
 "bridge_uses":bridge_uses,
 "sources_changed":[],
 "items_published":13,
 "items_dropped_by_verification":0,
 "deep_dive":"bumblebee-adaptixc2-akira",
 "verification_iterations":0,
 "verification_residual_count":0,
 "verification":{"iterations":[]}
}

with open("state/run_log.json") as f: rl=json.load(f)
rl["runs"]=[r for r in rl["runs"] if r.get("run_id")!=RUN_ID]
rl["runs"].append(rec)
rl["runs"]=rl["runs"][-90:]
rl["last_updated"]=TODAY
with open("state/run_log.json","w") as f: json.dump(rl,f,indent=2,ensure_ascii=False); f.write("\n")
print("run_log appended; runs:",len(rl["runs"]),"duration:",rec["duration_seconds"],"s")
