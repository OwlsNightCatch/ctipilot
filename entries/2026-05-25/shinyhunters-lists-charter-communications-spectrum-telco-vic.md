---
schema: 1
kind: incident
horizon: operational
title: ShinyHunters lists Charter Communications (Spectrum) — telco victim in the Salesforce-credential campaign
headline: ShinyHunters lists Charter Communications (Spectrum) — telco victim in the Salesforce-credential campaign
summary: "ShinyHunters listed Charter Communications (Spectrum), claiming 42M records with a 27 May deadline — a fresh victim in the Salesforce-credential campaign tracked here via 7-Eleven (2026-05-19), and by our own tracking its first telco/ISP victim to respond publicly. Charter denies any \"sensitive PI or CPNI\" exfiltration, a denial calibrated to FCC categories; the 42M figure is the actor's unverified claim (CyberInsider, 2026-05-23)."
discovered_at: "2026-05-25T05:00:03Z"
event_date: 2026-05-24
run_id: 2026-05-25-d675ef38
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
  - cloud
regions:
  - us
  - global
sectors:
  - telco
entities:
  - "actor:shinyhunters"
  - "incident:medtronic-shinyhunters-corporate-it-breach"
cves: []
sources:
  - url: "https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/"
    publisher: "CyberInsider, 2026-05-23"
    role: primary
  - url: "https://www.troyhunt.com/weekly-update-505/"
    publisher: "Troy Hunt — Weekly Update 505, 2026-05-24"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-25.md
---

**UPDATE (Salesforce-credential extortion campaign, originally covered 2026-05-19 via the 7-Eleven breach):** ShinyHunters listed Charter Communications — operating consumer services under the Spectrum brand — on its leak site around 22–23 May, claiming over 42 million PII records and setting a 27 May negotiation deadline before threatened release ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)). The 42M figure is the actor's own unverified leak-site claim. Charter issued a narrowly-worded statement confirming it is "following security protocols" and "alerting appropriate authorities" while explicitly denying that "sensitive personal information (PI) or customer proprietary network information (CPNI)" was exfiltrated — language calibrated to FCC-protected categories. The exclusion of *non*-CPNI PII (billing name, address, email) from that denial is conspicuous and leaves room for lower-sensitivity data exposure even if the denial holds.

By our own campaign tracking Charter is the first telco/ISP victim of this wave to respond publicly — an inference from the prior named victims (Instructure, Vimeo, Wynn, Vercel, Medtronic, 7-Eleven), none of them telcos, rather than a claim made by the cited sources. The pattern is consistent with the broader ShinyHunters wave against enterprise Salesforce tenants — abuse of exposed OAuth tokens and misconfigured connected-app / Experience Cloud integrations, not a vulnerability in Salesforce itself — the same vector behind the confirmed 7-Eleven breach (600k records, covered 2026-05-19). The fresh Charter listing is independently corroborated by [Troy Hunt's Weekly Update 505, 2026-05-24](https://www.troyhunt.com/weekly-update-505/), which records ShinyHunters' new claimed victims. For CH/EU public bodies running Salesforce: audit connected-app OAuth scopes, rotate long-lived connected-app credentials, restrict Experience/Community Cloud guest-user access, and baseline bulk-object query volumes via Shield Event Monitoring — an anomalous large `SELECT` against Account/Contact objects is the data-exfiltration signature to alert on.
