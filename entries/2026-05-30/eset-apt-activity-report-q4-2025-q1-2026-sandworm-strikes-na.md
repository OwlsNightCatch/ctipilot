---
schema: 1
kind: annual-report
horizon: operational
title: "ESET APT Activity Report Q4 2025–Q1 2026: Sandworm strikes NATO energy, Lazarus targets EU drone sector, UNC5221 pivots to Ivanti SPAWN toolset"
headline: "ESET APT Activity Report Q4 2025–Q1 2026: Sandworm strikes NATO energy, Lazarus targets EU drone sector, UNC5221 pivots to Ivanti SPAWN toolset"
summary: "ESET APT Activity Report Q4 2025–Q1 2026: Sandworm wiper targets Polish NATO energy company; Lazarus targets European drone manufacturers; UNC5221 deploys a new SPAWN toolset implant against Ivanti VPN appliances (ESET WeLiveSecurity, 2026-05-28)."
discovered_at: "2026-05-30T05:00:06Z"
event_date: 2026-05-28
run_id: 2026-05-30-aca445cc
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
  - russia-nexus
  - north-korea-nexus
  - china-nexus
regions:
  - europe
  - global
sectors:
  - energy
  - defense
  - technology
entities:
  - "report:eset-apt-activity-report-q4-2025-q1-2026-sandworm-lazarus"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q4-2025-q1-2026/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/chinese-hackers-exploit-iran-war/"
    publisher: Infosecurity Magazine
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-30.md
---

ESET published its APT Activity Report covering October 2025 through March 2026 on 28 May 2026 ([ESET WeLiveSecurity, 2026-05-28](https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q4-2025-q1-2026/)). EU- and NATO-relevant findings for public-sector defenders: Sandworm (Russia/GRU) intensified destructive winter operations against Ukrainian infrastructure and targeted a Polish energy company in December 2025 — a NATO member state critical-infrastructure attack attributed with medium confidence; this represents continued Sandworm willingness to conduct wiper operations beyond Ukraine's borders. Sednit/APT28 deployed Covenant and BeardShell implants against Ukrainian military, drone manufacturers, and logistics companies. Lazarus Group ran Operation DreamJob targeting European drone manufacturers — ESET assesses this as technology acquisition for North Korea's weapons programme. Operation DangerousPassword compromised the axios JavaScript library (100+ million weekly npm downloads), injecting trojanised code and demonstrating ongoing North Korea supply-chain interest in developer ecosystem targeting. UNC5221 (China-nexus) deployed a new implant assessed as part of the SPAWN toolset, specifically targeting Ivanti VPN appliances (Connect Secure, Policy Secure); organisations running unpatched Ivanti VPN should audit for SPAWN toolset artefacts including SPAWNANT installer, SPAWNMOLE tunneller, SPAWNSNAIL SSH backdoor, and SPAWNSLOTH log-tampering utility. The report PDF is available at `https://web-assets.esetstatic.com/wls/en/papers/threat-reports/eset-apt-activity-report-q4-2025-q1-2026.pdf`. Key defender actions: (a) confirm Sandworm wiper detection capability (file-destruction followed by MBR/VBR overwrite patterns, VSS deletion); (b) review Ivanti VPN logs for SPAWN footprints per [CISA AA24-060A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-060a) indicators; (c) audit npm dependency trees for axios versions <1.8.0 or 0.x released after the DangerousPassword campaign window.
