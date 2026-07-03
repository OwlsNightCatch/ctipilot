---
schema: 1
kind: incident
horizon: operational
title: "ShinyHunters Salesforce campaign — Charter and 7-Eleven both confirm; 7-Eleven count put at ~185,000 affected"
headline: "ShinyHunters Salesforce campaign — Charter and 7-Eleven both confirm; 7-Eleven count put at ~185,000 affected"
summary: "ShinyHunters Salesforce extortion — two fresh victim confirmations. Charter Communications (Spectrum) confirmed a breach but disputes that sensitive PI or CPNI was taken (BleepingComputer, 2026-05-26), while 7-Eleven confirmed a breach affecting roughly 185,000 individuals — CyberInsider reports Social Security and driver's-licence numbers in the exposed set (CyberInsider, 2026-05-26); both trace to the vishing → Entra → Salesforce-Aura pattern."
discovered_at: "2026-05-27T05:00:03Z"
event_date: 2026-05-26
run_id: 2026-05-27-0b6f12dd
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
  - cloud
  - phishing
regions:
  - us
  - global
sectors:
  - telco
  - retail
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/"
    publisher: "BleepingComputer, 2026-05-26"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/7-eleven-data-breach-exposes-personal-information-of-185-000-people/"
    publisher: "BleepingComputer, 2026-05-26"
    role: corroborating
  - url: "https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/"
    publisher: "CyberInsider, 2026-05-23"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-05-24)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-27.md
---

**UPDATE (originally covered 2026-05-24 / 2026-05-25):** Charter Communications (Spectrum) has confirmed it was breached after ShinyHunters listed it and threatened to leak data; Charter notified law enforcement but states that no sensitive personal information or customer proprietary network information (CPNI) was exfiltrated — disputing the actor's claim of 42 million records ([BleepingComputer, 2026-05-26](https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/); [CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)). ShinyHunters claims initial access on 1 April 2026 via vishing that compromised an employee Entra account, then bulk-exported customer records from Charter's Salesforce CRM.

Separately, 7-Eleven confirmed its ShinyHunters incident affects roughly 185,000 individuals; BleepingComputer reports the exposed fields as names, dates of birth, email addresses, phone numbers and physical addresses (describing the affected as franchisee-document holders) ([BleepingComputer, 2026-05-26](https://www.bleepingcomputer.com/news/security/7-eleven-data-breach-exposes-personal-information-of-185-000-people/)), while CyberInsider additionally reports Social Security numbers and driver's licence numbers in the set ([CyberInsider, 2026-05-26](https://cyberinsider.com/7-eleven-data-breach-exposes-personal-information-of-185000-applicants/)). The 185,000 figure is not contradictory with the earlier unconfirmed 600,000-record CRM claim. Both intrusions follow the campaign's Salesforce-Aura pattern (vishing → Entra account → CRM export, or unauthenticated `/s/sfsites/aura` guest-profile queries): audit guest-user object permissions on Experience Cloud, enable Secure Guest User Record Access, restrict SSN/ID fields to named users, and enforce phishing-resistant MFA (FIDO2/passkeys) on SaaS admin accounts.
