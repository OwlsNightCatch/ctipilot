import json
TODAY="2026-06-30"
with open("sources/sources.json") as f: s=json.load(f)
src={x["id"]:x for x in s["sources"]}

contributed=["advisories-ncsc-nl","bleepingcomputer","cert-pl","dfirreport","hackernews",
             "kaspersky-securelist","msft-ti","securityweek","vulncheck","watchtowr","zdi",
             "horizon3-ai","risky-biz-news","databreaches-net"]
for sid in contributed:
    if sid in src:
        x=src[sid]
        x["last_successful_fetch"]=TODAY
        x["consecutive_failures"]=0
        x["consecutive_fetch_failures"]=0
        x["consecutive_quiet_periods"]=0
        x["last_covered_in_brief"]=TODAY
    else:
        print("MISSING:",sid)

# anssi-fr / cert-fr feed stale (returns only pre-window entries) — quiet, not transport-dead; note it.
if "anssi-fr" in src:
    x=src["anssi-fr"]
    x["consecutive_quiet_periods"]=x.get("consecutive_quiet_periods",0)+1
    x["notes"]=x.get("notes","")+" | 2026-06-30: CERT-FR actu feed returned only entries up to 2026-06-19 (S2 reports feed appears stale since Nov 2025 via bridge actu-recent). No in-window items; quiet-period++. National CERT — not demoted (transport 200, content stale); flag feed-staleness for investigation."

# rapid7-research: S1 used wrong feed URL (/blog/feed/ 404). Documented recipe is rss.xml and is healthy. Reinforce note; no counter change.
if "rapid7-research" in src:
    x=src["rapid7-research"]
    x["notes"]=x.get("notes","")+" | 2026-06-30: a sub-agent hit HTTP 404 on https://www.rapid7.com/blog/feed/ — that is the WRONG endpoint. Correct feed is https://www.rapid7.com/rss.xml (already documented above). Source healthy; no demotion."

s["last_updated"]=TODAY
with open("sources/sources.json","w") as f: json.dump(s,f,indent=2,ensure_ascii=False); f.write("\n")
print("sources updated; active total:", sum(1 for x in s["sources"] if x.get("status")=="active"))
