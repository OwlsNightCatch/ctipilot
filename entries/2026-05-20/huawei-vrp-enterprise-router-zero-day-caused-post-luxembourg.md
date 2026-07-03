---
schema: 1
kind: threat
horizon: operational
title: Huawei VRP enterprise-router zero-day caused POST Luxembourg nationwide telecom outage (July 2025) — no CVE filed 10 months later
headline: Huawei VRP enterprise-router zero-day caused POST Luxembourg nationwide telecom outage (July 2025) — no CVE filed 10 months later
summary: "Recorded Future News disclosed on 2026-05-19 that a zero-day vulnerability in Huawei VRP (Versatile Routing Platform) operating-system software on enterprise routers was the root cause of the POST Luxembourg nationwide telecom outage of 23 July 2025 — disruption of landline, 4G, and 5G networks for more than …"
discovered_at: "2026-05-20T05:00:05Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - no-patch
  - zero-day
  - nation-state
regions:
  - europe
sectors:
  - telco
  - public-sector
entities: []
cves: []
sources:
  - url: "https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage"
    publisher: "The Record, 2026-05-19"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-20.md
---

Recorded Future News disclosed on [2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage) that a zero-day vulnerability in **Huawei VRP** (Versatile Routing Platform) operating-system software on enterprise routers was the root cause of the **POST Luxembourg** nationwide telecom outage of 23 July 2025 — disruption of landline, 4G, and 5G networks for more than three hours that triggered hundreds of calls to emergency services when service returned. POST Luxembourg head of communications Paul Rausch is quoted on record: the incident "exploited a non-public, non-documented behaviour, for which no patch was available at the time" and "was not related to the exploitation of any known or previously documented vulnerabilities." The attack mechanism was specially crafted network traffic that sent Huawei enterprise routers into a continuous restart loop; Luxembourg prosecutors stated they found "no evidence that an attack was specifically directed at POST Luxembourg" — the traffic appears to have transited the network rather than being targeted. Luxembourg cybersecurity authorities alerted partner IR teams across Europe through government channels at the time.

**Why it matters to us:** Ten months on, **no CVE has been assigned** in any public database, Huawei has not publicly acknowledged the vulnerability, and Huawei enterprise security advisories continue to be published through a restricted customer portal rather than as public CVEs. Whether the flaw is patched, how many operators are exposed, and whether similar Huawei enterprise routers in Swiss / German / EU telco fleets remain vulnerable is unknown. Operators running Huawei enterprise routers should escalate this with their Huawei account team and demand explicit status on the Luxembourg advisory. The 10-month disclosure gap is itself the structural lesson — vendor-restricted advisory portals leave critical-infrastructure operators outside the standard vuln-mgmt pipeline. [SINGLE-SOURCE — Recorded Future News, named institutional sources].
