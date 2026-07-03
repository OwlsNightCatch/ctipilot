---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "ShinyHunters extortion brand — Council of Europe named, Kodak and One Medical added to the leak-site pressure"
headline: "ShinyHunters extortion brand — Council of Europe named, Kodak and One Medical added to the leak-site pressure"
summary: "ShinyHunters named the Council of Europe in the Oracle PeopleSoft campaign — a European institution of which Switzerland is a member — while adding Kodak and One Medical to its leak-site pressure. (daily 06-16, SecurityWeek)"
discovered_at: "2026-06-22T00:14:34Z"
event_date: 2026-06-20
run_id: 2026-W25-0aacfe65
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - espionage
regions:
  - global
  - europe
sectors:
  - public-sector
  - technology
  - healthcare
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit"
    publisher: Google GTIG
    role: primary
  - url: "https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/"
    publisher: SecurityWeek — Council of Europe
    role: corroborating
  - url: "https://www.securityweek.com/kodak-admits-data-breach-after-shinyhunters-hack-claims/"
    publisher: SecurityWeek — Kodak
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2026-35273)"
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

The ShinyHunters extortion brand (the data-theft cluster Google tracks as UNC6240) ran on two fronts this week. The technical core remains the Oracle PeopleSoft zero-day campaign (CVE-2026-35273) consolidated in the W24 weekly, and Google's Threat Intelligence Group sharpened it this week: GTIG's analysis confirms UNC6240 exploited the flaw between 27 May and 9 June as a zero-day, has notified 100+ organisations (68% in higher education), and documented the TTPs — JSP shell implant, a customised MeshCentral agent masquerading as Azure cloud endpoints, `[victim]_fanout.sh` SSH credential-spraying and `zstd`-compressed exfiltration ([Google GTIG](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit)). On 2026-06-16 ShinyHunters listed the **Council of Europe** — the 46-member Strasbourg human-rights body of which Switzerland is a member — claiming roughly 297 GB exfiltrated; per W1's assessment it is the only named European-institution victim in the campaign to date ([SecurityWeek, 2026-06-16](https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/); [daily 06-16](/briefs/2026-06-16/)). In parallel the brand expanded its leak-site extortion pressure beyond PeopleSoft: Eastman Kodak confirmed on 2026-06-17 that "an unauthorized third party illegally gained access to a limited amount of company data" after a ShinyHunters listing ([SecurityWeek, 2026-06-19](https://www.securityweek.com/kodak-admits-data-breach-after-shinyhunters-hack-claims/); [daily 06-20](/briefs/2026-06-20/)), and Amazon's One Medical confirmed a legacy third-party file-storage breach while ShinyHunters' unverified 8.8 TB claim ran a deadline that expired 2026-06-21 ([BankInfoSecurity, 2026-06-20](https://www.bankinfosecurity.com/shinyhunters-threatens-to-leak-amazon-one-medical-records-a-32027); [daily 06-21](/briefs/2026-06-21/)).

The cross-day pattern for a CH/EU SOC: the same brand is simultaneously running a confirmed enterprise-SaaS zero-day (PeopleSoft, vendor-confirmed) and a higher-noise leak-site operation where claims (Kodak data volume, the One Medical 8.8 TB figure) are attacker-asserted and partly unverified. Triage the two differently — the PeopleSoft exposure is a patch-and-hunt emergency for internet-reachable instances; the leak-site listings warrant victim-notification monitoring but the headline data volumes should be treated as unconfirmed until the victim corroborates.
