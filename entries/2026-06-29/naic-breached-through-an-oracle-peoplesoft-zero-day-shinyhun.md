---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "NAIC breached through an Oracle PeopleSoft zero-day; ShinyHunters dumps 3.1 TB and US rating-agency feeds stall"
headline: "NAIC breached through an Oracle PeopleSoft zero-day; ShinyHunters dumps 3.1 TB and US rating-agency feeds stall"
summary: "NAIC breached through an Oracle PeopleSoft zero-day (CVE-2026-35273); ShinyHunters dumps 3.1 TB and US rating-agency feeds stall — the same UNC6240 campaign GTIG has tracked against ~100 orgs (68% higher education) is still acquiring victims; treat internet-reachable PeopleSoft as assume-compromise. (daily 06-28, NAIC)"
discovered_at: "2026-06-29T00:20:53Z"
event_date: 2026-06-26
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - data-breach
  - zero-day
  - actively-exploited
  - organized-crime
regions:
  - us
  - europe
sectors:
  - finance
  - public-sector
entities:
  - "actor:shinyhunters"
cves:
  - id: CVE-2026-35273
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
sources:
  - url: "https://content.naic.org/about/security-update"
    publisher: NAIC security update
    role: primary
  - url: "https://www.insurancejournal.com/news/national/2026/06/25/875334.htm"
    publisher: Insurance Journal
    role: corroborating
  - url: "https://www.techradar.com/pro/security/naic-confirms-data-breach-with-shinyhunters-claiming-3-1tb-of-data-stolen-in-oracle-zero-day-attack"
    publisher: TechRadar
    role: corroborating
closed_sources: []
evidence:
  - quote: "Unauthorized access to a portion of the NAIC's environment was identified on June 11 via an Oracle PeopleSoft vulnerability. While in PeopleSoft, the unauthorized party was able to obtain information needed to gain temporary access to certain data storage areas."
    publisher: NAIC
  - quote: "Due to the incident, certain credit rating agencies have paused their data feeds and consequently, the NAIC has temporarily suspended assigning designations to insurer investments."
    publisher: NAIC
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
migrated_from: briefs/weekly/2026-W26.md
---

**If you did nothing this week:** any internet-reachable Oracle PeopleSoft instance is a live pre-auth foothold — the same zero-day path that put the US National Association of Insurance Commissioners into ShinyHunters' hands, and PeopleSoft is widely deployed across European public administration, higher education and HR/finance back offices. The W25 looking-ahead flagged that ShinyHunters PeopleSoft notifications were still landing and that EU universities were a probable next-named class; NAIC is the fresh high-profile confirmation that the campaign is still acquiring victims.

NAIC — the standard-setting body for all 50 US state insurance regulators — [confirmed on 2026-06-26](https://content.naic.org/about/security-update) that an unauthorised party reached its environment on June 11 via an Oracle PeopleSoft vulnerability, then pivoted from PeopleSoft to temporary access to data-storage areas. ShinyHunters claims 3.1 TB exfiltrated ([TechRadar](https://www.techradar.com/pro/security/naic-confirms-data-breach-with-shinyhunters-claiming-3-1tb-of-data-stolen-in-oracle-zero-day-attack), [Insurance Journal](https://www.insurancejournal.com/news/national/2026/06/25/875334.htm)). The operational tell is the downstream impact NAIC itself disclosed: credit-rating agencies paused their data feeds and NAIC suspended assigning designations to insurer investments — a regulatory-process outage, not just a data-confidentiality event. This is the same PeopleSoft exploitation wave (CVE-2026-35273, the unauthenticated RCE in PeopleTools Environment Management) Google GTIG attributes to UNC6240/ShinyHunters and has been tracking against the education sector — 68% of identified targets were higher-education institutions; Treat any externally-reachable PeopleSoft portal (`/PSEMHUB/`, `/PSIGW/HttpListeningConnector`) as a hunt target, not a patch-later item. ([daily 06-28](/briefs/2026-06-28/))
