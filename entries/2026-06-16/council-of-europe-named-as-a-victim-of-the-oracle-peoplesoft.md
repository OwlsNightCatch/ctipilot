---
schema: 1
kind: vulnerability
horizon: operational
title: Council of Europe named as a victim of the Oracle PeopleSoft (CVE-2026-35273) campaign
headline: Council of Europe named as a victim of the Oracle PeopleSoft (CVE-2026-35273) campaign
summary: "Council of Europe breached via the Oracle PeopleSoft zero-day (CVE-2026-35273) — ShinyHunters claims 297 GB / ~429,000 files and set a 16 June leak deadline; the first European intergovernmental victim named in the 100+-organisation PeopleSoft campaign (§ 4 update). (SecurityWeek, 2026-06-15)"
discovered_at: "2026-06-16T05:09:02Z"
event_date: 2026-06-15
run_id: 2026-06-16-38d638e1
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
regions:
  - europe
sectors:
  - public-sector
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757"
    publisher: The Register
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2026-35273)"
confidence: high
update_of: 2026-06-12/shinyhunters-peoplesoft-campaign-oracle-confirms-cve-2026-35
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "**Block perimeter access to `/PSEMHUB/*` on Oracle PeopleSoft** and treat any externally-reachable Environment Management Hub as compromised pending forensic review (CVE-2026-35273)."
migrated_from: briefs/2026-06-16.md
---

**UPDATE (originally covered 2026-06-12/2026-06-13):** ShinyHunters listed the **Council of Europe** — the 46-member Strasbourg human-rights body, of which Switzerland is a member — claiming **297 GB across ~429,000 files** taken via the Oracle PeopleSoft Environment Management Hub zero-day **CVE-2026-35273**, and set a **16 June leak deadline** ([SecurityWeek, 2026-06-15](https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/)). This is the first European intergovernmental institution named in the 100+-organisation PeopleSoft campaign previously covered as an education-sector wave.

The claimed dataset spans payroll for 10,000+ current and former staff (2011–2026), 14,000+ CVs, and HR records with names, dates of birth, addresses, bank-account, tax/social-security and medical data. The Council of Europe confirmed it "is currently investigating the matter and assessing the situation" and has not confirmed exfiltration ([The Register, 2026-06-15](https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757); [BleepingComputer, 2026-06-15](https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/)). The vector — unauthenticated HTTP to the `/PSEMHUB/hub` servlet (`T1190`) — is unchanged; treat any externally-reachable PeopleSoft Environment Management Hub as compromised pending forensic review and block perimeter access to `/PSEMHUB/*`. Confidence on the victim claim is MEDIUM pending Council of Europe confirmation (extortion-site claim).
