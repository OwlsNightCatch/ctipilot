---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "The Gentlemen — EDR-killer framework documented, OT-adjacent victim claimed, operator named"
headline: "The Gentlemen — EDR-killer framework documented, OT-adjacent victim claimed, operator named"
summary: "The Gentlemen RaaS grew +315% in Q1 and impacted OT — ESET exposed its centrally-built GentleKiller EDR-killer; the gang halted milling at Mackay Sugar. (daily 06-19, ESET)"
discovered_at: "2026-06-22T00:14:35Z"
event_date: 2026-06-19
run_id: 2026-W25-0aacfe65
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - russia-nexus
  - ot-ics
regions:
  - global
sectors:
  - manufacturing
entities:
  - "actor:gentlemen-raas-gentlekiller"
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://therecord.media/mackay-sugar-cyberattack-claimed-gentlemen"
    publisher: The Record
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
migrated_from: briefs/weekly/2026-W25.md
---

The Gentlemen RaaS operation moved from tooling disclosure to victim impact to attribution across three days. On 2026-06-18 ESET published a months-long investigation showing the gang **centrally builds and maintains its affiliates' GentleKiller EDR-killer framework** — a structural departure from the affiliate norm in which each affiliate sources its own evasion tooling ([ESET, 2026-06-19](https://www.welivesecurity.com/en/eset-research/killing-me-gently-inside-gentlemens-edr-killer-framework/); [daily 06-19](/briefs/2026-06-19/)). On 2026-06-18 Mackay Sugar — Australia's second-largest sugar producer — confirmed an intrusion around 10 June that halted milling at two of three mills, an OT-adjacent impact the group later claimed ([The Record, 2026-06-18](https://therecord.media/mackay-sugar-cyberattack-claimed-gentlemen); [daily 06-20](/briefs/2026-06-20/)). Separately, KrebsOnSecurity published OSINT attribution identifying the group's administrator ("Hastalamuerte" / "Zeta88") as a 36-year-old from Izhevsk, Russia, who reportedly uses AI tooling to develop ransomware and assist post-exploitation ([KrebsOnSecurity, 2026-06-10](https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/)).

The defender signal is the centralised EDR-killer model: because the BYOVD evasion tooling is built once and pushed to all affiliates, detection content that catches GentleKiller's driver-load and EDR-tamper behaviour generalises across every affiliate intrusion rather than needing per-affiliate tuning. The Krebs attribution is an analytical claim, not an indictment — treat it as context, not actionable IOC.
