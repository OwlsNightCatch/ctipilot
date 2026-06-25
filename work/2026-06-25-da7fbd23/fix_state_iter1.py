#!/usr/bin/env python3
import json
RUN_ID="2026-06-25-da7fbd23"; TODAY="2026-06-25"; BRIEF="briefs/2026-06-25.md"
def load(p):
    with open(p) as f: return json.load(f)
def save(p,d):
    with open(p,"w") as f: json.dump(d,f,indent=2,ensure_ascii=False); f.write("\n")

# ---- covered_items: drop Cacti record; convert Arista to CVE-2026-7473 UPDATE appearance ----
ci=load("state/covered_items.json")
items=ci["items"]
# remove the Cacti record added today (key CVE-2026-39893)
items=[it for it in items if it["key"]!="CVE-2026-39893"]
# remove my mistaken vulnerability-trend Arista record
items=[it for it in items if it["key"]!="vulnerability-trend:arista-eos-tunnel-decapsulation"]
# append UPDATE appearance to existing CVE-2026-7473
found=False
for it in items:
    if it["key"]=="CVE-2026-7473":
        it["last_covered"]=TODAY
        it["appearances"].append({"date":TODAY,"section":"updates","brief_path":BRIEF,
            "delta_summary":"UPDATE: Eclypsium technical analysis; Arista confirms no code fix planned for EOS 4.x (mitigation-only); prior 06-10 coverage listed patch-available. KEV/exploited status retained."})
        found=True
ci["items"]=items
ci["last_updated"]=TODAY
save("state/covered_items.json",ci)
print("covered_items: Cacti+vuln-trend removed; CVE-2026-7473 update appended:",found)

# ---- cves_seen: remove Cacti CVEs added today (dropped); bump CVE-2026-7473 last_seen ----
cs=load("state/cves_seen.json")
drop={"CVE-2026-39893","CVE-2026-39938","CVE-2026-39948","CVE-2026-39955","CVE-2026-39949"}
before=len(cs["cves"])
cs["cves"]=[c for c in cs["cves"] if c["id"] not in drop]
for c in cs["cves"]:
    if c["id"]=="CVE-2026-7473": c["last_seen"]=TODAY
cs["last_updated"]=TODAY
save("state/cves_seen.json",cs)
print("cves_seen: removed",before-len(cs["cves"]),"Cacti CVEs; CVE-2026-7473 bumped")

# ---- run_log: counts + verification iteration 1 ----
rl=load("state/run_log.json")
for r in rl["runs"]:
    if r.get("run_id")==RUN_ID:
        r["items_published"]=8
        r["items_dropped_by_verification"]=1
        r["verification_iterations"]=1
        r["verification_residual_count"]=0  # provisional; updated after final iteration
        r["verification"]={"iterations":[{
            "n":1,"model":"Claude Opus 4.8 (1M context)","model_id":"claude-opus-4-8[1m]",
            "started_at":"2026-06-25T04:28:17Z","ended_at":"2026-06-25T04:32:07Z","duration_seconds":230,
            "verdict":"NEEDS_FIXES","truth":6,"editorial":1,"advisory":1,
            "findings":[
              {"code":"F3","category":"claim-not-supported","section":"active-threats","item":"Arista EOS tunnel-decapsulation — 'no CVE published'","url_or_quote":"CVE-2026-7473 named by both sources; repo covered it 2026-06-10","summary":"'no CVE published' is false; CVE-2026-7473 is KEV-listed","remediation_applied":"Reframed as § 4 UPDATE naming CVE-2026-7473 (CVSS 6.9), KEV/exploited retained, new no-patch-for-4.x delta surfaced","remediation_outcome":"fixed-clean"},
              {"code":"F3","category":"claim-not-supported","section":"verification-notes","item":"Arista exploitation reduced-confidence hedge","url_or_quote":"KEV added 2026-06-09","summary":"exploitation is KEV-confirmed; remove hedge","remediation_applied":"Removed the reduced-confidence hedge; status set exploited, cisa-kev","remediation_outcome":"fixed-clean"},
              {"code":"F3","category":"claim-not-supported","section":"active-threats","item":"Operation Endgame StealC C2 directory-traversal","url_or_quote":"exploit used by global law enforcement","summary":"operational exploitation belongs to LE, not Proofpoint/IBM","remediation_applied":"Reworded: researchers documented the flaw; an exploit built on it was used by law enforcement","remediation_outcome":"fixed-clean"},
              {"code":"F4","category":"hallucinated-fact","section":"trending-vulnerabilities","item":"Cacti 1.2.31 multi-CVE","url_or_quote":"GHSA-69gg covers only CVE-2026-39893","summary":"over-attribution of 3 extra CVEs/LFI/40-vulns/EUVD to one GHSA","remediation_applied":"Item dropped to § 7 (also out-of-window: GHSA dated 06-19)","remediation_outcome":"dropped-item"},
              {"code":"F4","category":"hallucinated-fact","section":"trending-vulnerabilities","item":"MISP 2.5.42 CVSS scores","url_or_quote":"CVSS 8.7/9.3/9.4/7.1 unsourced","summary":"release notes carry no CVSS; only GHSA-834x gives CVE-2026-56447=9.3","remediation_applied":"Removed unsourced CVSS; kept only 9.3 (CVE-2026-56447); generalised other-CVE descriptions to release-page wording","remediation_outcome":"fixed-clean"},
              {"code":"F4","category":"hallucinated-fact","section":"active-threats","item":"Mistic BOF capability","url_or_quote":"'headline capability is in-memory execution of Beacon Object Files'","summary":"BOF not in readable cited sources","remediation_applied":"Removed BOF framing + BOF evidence quote; kept signed-Defender sideloading (CSO) + affiliate list (SecurityWeek)","remediation_outcome":"fixed-degraded"},
              {"code":"F7","category":"drop","section":"active-threats","item":"Arista EOS recycled 06-10 coverage","url_or_quote":"briefs/2026-06-10.md CVE-2026-7473","summary":"recycled prior coverage presented as fresh","remediation_applied":"Reframed as § 4 UPDATE with the new no-patch delta","remediation_outcome":"fixed-clean"},
              {"code":"F11","category":"editorial-advisory","section":"deep-dive","item":"Edgecution CloudFront C2 quote","url_or_quote":"Zscaler SPA-unreadable quote","summary":"verbatim quote from SPA-unreadable page","remediation_applied":"Softened to 'Zscaler reports'; rebound Evidence to a corroborated BleepingComputer quote","remediation_outcome":"fixed-clean"}
            ],
            "telemetry":{"webfetch_calls":16,"websearch_calls":0,"bridge_fetches":2,"urls_checked":18}
        }]}
rl["last_updated"]=TODAY
save("state/run_log.json",rl)
print("run_log: items_published=8, dropped=1, verification iter1 recorded")
