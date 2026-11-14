---
schema: 1
kind: incident
title: "Kodak confirms breach after ShinyHunters leak-site listing; June 18 deadline passed without publication"
headline: "Kodak confirms breach after ShinyHunters leak-site listing; June 18 deadline passed without publication"
summary: "Eastman Kodak acknowledged on 17 June 2026 that \"an unauthorized third party illegally gained access to a limited amount of company data,\" after ShinyHunters listed it on their dark-web leak site on 15 June claiming 2.2 million PII records and set an 18 June contact deadline (SecurityWeek, 2026-06-18 …"
discovered_at: "2026-06-20T05:12:13Z"
event_date: 2026-06-18
run_id: 2026-06-20-4cfd00ef
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
regions:
  - us
  - global
sectors:
  - manufacturing
  - technology
entities:
  - "incident:kodak-shinyhunters-breach"
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.securityweek.com/kodak-admits-data-breach-after-shinyhunters-hack-claims/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/kodak-confirms-data-breach-claimed-by-shinyhunters-extortion-gang/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.malwarebytes.com/blog/news/2026/06/kodak-confirms-breach-as-shinyhunters-leak-threat-reaches-deadline"
    publisher: Malwarebytes
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
migrated_from: briefs/2026-06-20.md
---

Eastman Kodak acknowledged on 17 June 2026 that "an unauthorized third party illegally gained access to a limited amount of company data," after ShinyHunters listed it on their dark-web leak site on 15 June claiming 2.2 million PII records and set an 18 June contact deadline ([SecurityWeek, 2026-06-18](https://www.securityweek.com/kodak-admits-data-breach-after-shinyhunters-hack-claims/); [BleepingComputer, 2026-06-17](https://www.bleepingcomputer.com/news/security/kodak-confirms-data-breach-claimed-by-shinyhunters-extortion-gang/)). As of the deadline ShinyHunters had not published samples — consistent with the group's pattern of withholding proof to maximise leverage. Kodak did not disclose the access vector; ShinyHunters' 2026 campaign has leaned on misconfigured Salesforce Experience/Aura guest-user access, Oracle PeopleSoft (CVE-2026-35273) and Snowflake credential stuffing across 100+ victims, with the group claiming a 1.5-billion-record Salesforce corpus ([BleepingComputer, 2026-06-17](https://www.bleepingcomputer.com/news/security/kodak-confirms-data-breach-claimed-by-shinyhunters-extortion-gang/)).

**Defender takeaway:** The Kodak claim is a leak-site listing with limited Kodak confirmation; treat the 2.2 M figure as unverified. The transferable action for CH/EU defenders is the ShinyHunters platform pattern — audit Salesforce Experience Cloud for `IsGuestEnabled=true` profiles with object-level access to sensitive tables, alert on high-volume SOQL from guest sessions, and enforce IP restriction on Salesforce orgs.
