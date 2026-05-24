#!/usr/bin/env python3
"""Phase 4 state update for weekly 2026-W21. Idempotent."""
import json, re, datetime

RUN_ID = "2026-W21-473d6fa5"
TODAY = "2026-05-24"
ISO_WEEK = "2026-W21"
BRIEF = "briefs/weekly/2026-W21.md"

# ---- covered_items.json ----
ci = json.load(open("state/covered_items.json"))
items = ci["items"]

EXCLUDE = {
 'item:b1ack-stash-46m-card-dump-may-2026-third-free-release-wave',
 'item:ico-poca-confiscation-rizwan-manjra-markerstudy-off-hours-bu',
 'item:fast16-symantec-carbon-black-contemporaneous-stuxnet-nuclea',
 'item:cisco-talos-badiis-demo-pdb-maas-isapi-backdoor-lwxat-dragon',
 'item:pintheft-linux-kernel-rds-zerocopy-iouring-lpe-no-cve-arch-d',
 'item:google-cloud-api-key-deletion-delay-2026',
 'item:atos-byovd-hardware-gate-bypass-2026',
 'item:fbi-psa260521-kali365-phaas-oauth-device-code-m365-mfa-bypass',
 'incident:skoda-shop-breach-2026',
 'item:storm-2949-sspr-to-key-vault-azure-cloud-wide-kill-chain',
 'actor:storm-2949',
 'item:kimsuky-pebbledash-hellodoor-trycloudflare-tunnel-c2-evolution',
 'item:tycoon2fa-oauth-device-authorization-grant-microsoft-365-post-takedown',
 'policy:enisa-cve-root-2026',
 'policy:eu-cybersecurity-package-2026',
 'policy:germany-kritis-dachg-2026',
 'policy:eu-cyber-sanctions-2027-renewal',
 'policy:europol-anti-scam-platform-2026',
 'annual-report:five-eyes-agentic-ai-guidance-2026',
 'policy:germany-nis2-umsu-registration-2026',
 'CVE-2026-20182',
 'UAT-8616',
 'incident:foxconn-nitrogen-2026',
 'incident:bwh-hotels-breach-2026',
 'incident:clinical-diagnostics-nmdl-igj-2026',
}

appearance = {
    "date": TODAY,
    "section": "weekly_summary",
    "brief_path": BRIEF,
    "delta_summary": "Consolidated in weekly summary for week 2026-W21",
}

appended = 0
for it in items:
    if it["key"] in EXCLUDE:
        continue
    if it.get("last_covered", "") < "2026-05-18":
        continue
    apps = it.setdefault("appearances", [])
    # idempotent: skip if this exact weekly appearance already present
    if any(a.get("section") == "weekly_summary" and a.get("brief_path") == BRIEF for a in apps):
        continue
    apps.append(dict(appearance))
    if it.get("last_covered", "") < TODAY:
        it["last_covered"] = TODAY
    appended += 1

# New top-level record for the W2-surfaced EU 20th-package MSS prohibition (genuinely new)
NEW_KEY = "policy:eu-20th-russia-sanctions-mss-prohibition-2026"
if not any(i["key"] == NEW_KEY for i in items):
    items.append({
        "key": NEW_KEY,
        "type": "policy",
        "title": "EU 20th Russia sanctions package — Article 5n managed-security-services prohibition (eff. 25 May 2026); Switzerland adopted most measures 22 May",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://www.gtlaw.com/en/insights/2026/5/eus-20th-russia-sanctions-package-key-changes-and-compliance-implications",
        "appearances": [{
            "date": TODAY,
            "section": "weekly_summary",
            "brief_path": BRIEF,
            "delta_summary": "First coverage (W2 horizon). Art. 5n MSS prohibition effective 25 May; CH adopted 22 May; SECO confirmation of MSS scope pending.",
        }],
    })
    print("covered_items: added new record", NEW_KEY)

ci["last_updated"] = TODAY
json.dump(ci, open("state/covered_items.json", "w"), indent=2, ensure_ascii=False)
open("state/covered_items.json", "a").write("\n")
print(f"covered_items: appended {appended} weekly_summary appearances")

# ---- cves_seen.json: bump last_seen for every CVE referenced in the brief ----
brief_text = open(BRIEF).read()
cve_ids = set(re.findall(r"CVE-\d{4}-\d{4,7}", brief_text))
cs = json.load(open("state/cves_seen.json"))
cves = cs["cves"]
by_id = {c["id"]: c for c in cves}
bumped = 0
missing = []
for cid in sorted(cve_ids):
    if cid in by_id:
        if by_id[cid].get("last_seen", "") < TODAY:
            by_id[cid]["last_seen"] = TODAY
            bumped += 1
    else:
        missing.append(cid)
cs["last_updated"] = TODAY
json.dump(cs, open("state/cves_seen.json", "w"), indent=2, ensure_ascii=False)
open("state/cves_seen.json", "a").write("\n")
print(f"cves_seen: brief references {len(cve_ids)} CVEs; bumped {bumped}; MISSING (not in cves_seen): {missing}")

# ---- sources.json: bump last_successful_fetch for contributing sources; add CSA candidate ----
sj = json.load(open("sources/sources.json"))
srcs = sj["sources"]
by_sid = {s["id"]: s for s in srcs}
USED = ["securityweek","hackernews","therecord","unit42","talos","eset","mandiant-gtig",
        "msft-ti","checkpoint-research","cisco-psirt","anssi-fr","cert-pl","rapid7-research",
        "bsi-de","krebs","bleepingcomputer","heise-sec","helpnetsecurity","vulncheck"]
sbumped = 0
for sid in USED:
    if sid in by_sid:
        by_sid[sid]["last_successful_fetch"] = TODAY
        by_sid[sid]["consecutive_failures"] = 0
        sbumped += 1

CSA_ID = "csa-labs"
if not any(s["id"] == CSA_ID or "cloudsecurityalliance" in (s.get("url") or "") for s in srcs):
    srcs.append({
        "id": CSA_ID,
        "publisher": "Cloud Security Alliance — Lab Space (Research Notes)",
        "url": "https://labs.cloudsecurityalliance.org/research/",
        "category": ["research"],
        "reliability": "MEDIUM",
        "language": ["en"],
        "status": "candidate",
        "fetch_method": "webfetch",
        "last_successful_fetch": TODAY,
        "consecutive_failures": 0,
        "notes": "Surfaced by W1 (2026-W21) — published a strong two-wave consolidated research note on the Shai-Hulud/Megalodon supply-chain cascade (CVE-2026-45321, SLSA BL3 invalidation analysis). Candidate — promote to active after 3 successful runs.",
    })
    print("sources: added candidate", CSA_ID)
sj["last_updated"] = TODAY
json.dump(sj, open("sources/sources.json", "w"), indent=2, ensure_ascii=False)
open("sources/sources.json", "a").write("\n")
print(f"sources: bumped last_successful_fetch on {sbumped} sources")

print("STATE UPDATE COMPLETE")
