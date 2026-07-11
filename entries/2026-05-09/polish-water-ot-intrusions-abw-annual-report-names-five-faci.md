---
schema: 1
kind: threat
horizon: operational
title: "Polish water OT intrusions — ABW annual report names five facilities; APT28 / APT29 / UNC1151 formally attributed; NIS2 enforcement context"
headline: "Polish water OT intrusions — ABW annual report names five facilities; APT28 / APT29 / UNC1151 formally attributed; NIS2 enforcement context"
summary: "UPDATE (originally covered 2026-05-08):"
discovered_at: "2026-05-09T05:00:14Z"
event_date: null
run_id: 2026-05-09-migrated
priority: notable
immediate_action: null
tags:
  - nation-state
  - ot-ics
  - russia-nexus
  - actively-exploited
regions:
  - europe
sectors:
  - water
  - public-sector
entities:
  - "campaign:frostyneighbor-2026-05-campaign"
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-207a"
    publisher: CISA AA24-207A — Russian GRU targeting critical infrastructure (background reference)
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: 2026-05-08/pro-russian-hacktivists-modify-ot-pump-settings-at-five-poli
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-09.md
---

**UPDATE (originally covered 2026-05-08):**

Poland's Internal Security Agency (ABW) published its 2025 Annual Report on 2026-05-07, providing materially expanded detail beyond the initial reporting. The report names five municipal water facilities targeted in intrusion attempts during H2 2025 and Q1 2026: **Jabłonna Lacka**, **Szczytno**, **Małdyty**, **Tolkmicko**, and **Sierakowo**. All are smaller municipalities (populations 1,500–26,000) with limited IT security staff, consistent with the observed targeting pattern. ABW formally attributes the intrusion campaign to **APT28** (Russian GRU) for the initial-access and persistence phase, **APT29** (Russian SVR) for the intelligence-collection overlay observed at Jabłonna Lacka, and **UNC1151** (Belarusian GRU-affiliated, historically associated with Ghostwriter information operations) for a disinformation component: fabricated leak documents purporting to show contamination data. This represents more granular tri-attribution than the "pro-Russian hacktivist" framing used in initial reporting.

NIS2 Directive context: Poland transposed NIS2 into national law effective 2026-02-01 (Ustawa z dnia 28 listopada 2025 r. o krajowym systemie cyberbezpieczeństwa). Water distribution operators above the 50-employee threshold are now classified as Essential Entities under NIS2, subject to mandatory incident notification to CSIRT GOV (ABW) within 24/72 hours. ABW's annual report explicitly notes that the five named facilities fell below the NIS2 threshold at the time of intrusion, highlighting the coverage gap for small municipal operators. ABW is recommending legislative action to extend NIS2 obligations to critical-function entities regardless of headcount.
