---
schema: 1
kind: incident
title: >
  ShinyHunters Salesforce campaign — Charter and 7-Eleven both confirm; 7-Eleven count put at
  ~185,000 affected
headline: >
  ShinyHunters Salesforce campaign — Charter and 7-Eleven both confirm; 7-Eleven count put at
  ~185,000 affected
summary: >
  ShinyHunters Salesforce extortion — two fresh victim confirmations. Charter Communications
  (Spectrum) confirmed a breach but disputes that sensitive PI or CPNI was taken
  (BleepingComputer, 2026-05-26), while 7-Eleven confirmed a breach affecting roughly 185,000
  individuals — CyberInsider reports Social Security and driver's-licence numbers in the exposed
  set (CyberInsider, 2026-05-26); both trace to the vishing → Entra → Salesforce-Aura pattern.
discovered_at: "2026-05-27T05:00:03Z"
updated_at: "2026-06-05T05:00:07Z"
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
  - healthcare
entities:
  - "actor:shinyhunters"
  - "incident:dentaquest-shinyhunters-2026"
techniques: []
affected_products: []
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
  - url: "https://securityaffairs.com/192907/uncategorized/shinyhunters-leaks-charter-communications-data-potentially-impacting-5-million-customers.html"
    publisher: Security Affairs
    role: primary
  - url: "https://haveibeenpwned.com/Breach/Charter"
    publisher: Have I Been Pwned
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/dentaquest-data-breach-exposed-info-of-26-million-accounts/"
    publisher: "BleepingComputer, 2026-06-04"
    role: primary
  - url: "https://www.bankinfosecurity.com/shinyhunters-leaks-234gb-dentaquest-data-trove-a-31883"
    publisher: "BankInfoSecurity, 2026-06-04"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-05-24)"
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-02T05:00:10Z"
    run_id: 2026-06-02-8af85d01
    type: update
    summary: >
      UPDATE (originally covered 2026-05-27): After Charter Communications declined to pay,
      ShinyHunters published the stolen dataset on 30 May. Have I Been Pwned ingested it as 4.9
      million unique email addresses, alongside names, phone numbers and physical addresses (Security
      Affairs, 2026-05-30 · Have I Been Pwned).
    fields:
      - sources
      - body
    merged_from: 2026-06-02/shinyhunters-publishes-the-charter-communications-dataset-af
  - at: "2026-06-05T05:00:07Z"
    run_id: 2026-06-05-2c6574c4
    type: update
    summary: >
      UPDATE (originally covered 2026-06-02): DentaQuest, a Sun Life subsidiary administering dental
      and vision benefits for ~35 M US Medicaid, Medicare and employer-plan members, is the latest
      confirmed named victim of the ShinyHunters data-extortion campaign last covered here on the
      Charter Communications listing.
    fields:
      - entities
      - sectors
      - sources
      - body
    merged_from: 2026-06-05/shinyhunters-extortion-campaign-adds-dentaquest-234-gb-publi
migrated_from: briefs/2026-05-27.md
---

**UPDATE (originally covered 2026-05-24 / 2026-05-25):** Charter Communications (Spectrum) has confirmed it was breached after ShinyHunters listed it and threatened to leak data; Charter notified law enforcement but states that no sensitive personal information or customer proprietary network information (CPNI) was exfiltrated — disputing the actor's claim of 42 million records ([BleepingComputer, 2026-05-26](https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/); [CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)). ShinyHunters claims initial access on 1 April 2026 via vishing that compromised an employee Entra account, then bulk-exported customer records from Charter's Salesforce CRM.

Separately, 7-Eleven confirmed its ShinyHunters incident affects roughly 185,000 individuals; BleepingComputer reports the exposed fields as names, dates of birth, email addresses, phone numbers and physical addresses (describing the affected as franchisee-document holders) ([BleepingComputer, 2026-05-26](https://www.bleepingcomputer.com/news/security/7-eleven-data-breach-exposes-personal-information-of-185-000-people/)), while CyberInsider additionally reports Social Security numbers and driver's licence numbers in the set ([CyberInsider, 2026-05-26](https://cyberinsider.com/7-eleven-data-breach-exposes-personal-information-of-185000-applicants/)). The 185,000 figure is not contradictory with the earlier unconfirmed 600,000-record CRM claim. Both intrusions follow the campaign's Salesforce-Aura pattern (vishing → Entra account → CRM export, or unauthenticated `/s/sfsites/aura` guest-profile queries): audit guest-user object permissions on Experience Cloud, enable Secure Guest User Record Access, restrict SSN/ID fields to named users, and enforce phishing-resistant MFA (FIDO2/passkeys) on SaaS admin accounts.

## Update — 2026-06-02T05:00:10Z

After Charter Communications declined to pay, ShinyHunters published the stolen dataset on 30 May. Have I Been Pwned ingested it as 4.9 million unique email addresses, alongside names, phone numbers and physical addresses ([Security Affairs, 2026-05-30](https://securityaffairs.com/192907/uncategorized/shinyhunters-leaks-charter-communications-data-potentially-impacting-5-million-customers.html) · [Have I Been Pwned](https://haveibeenpwned.com/Breach/Charter)).

A subset of roughly 85,000 records originated from an internal employee directory and included job titles. ShinyHunters had originally claimed 42 million records and customer proprietary network information (CPNI); Charter confirmed the incident but stated no sensitive personal information or CPNI was exfiltrated. As established in prior coverage of the broader ShinyHunters Salesforce campaign, the access pattern is vishing-driven compromise of an employee Microsoft Entra account followed by a Salesforce export. The data is now public.

## Update — 2026-06-05T05:00:07Z

DentaQuest, a Sun Life subsidiary administering dental and vision benefits for ~35 M US Medicaid, Medicare and employer-plan members, is the latest confirmed named victim of the ShinyHunters data-extortion campaign last covered here on the Charter Communications listing. ShinyHunters listed DentaQuest on 23 May with a 27 May ransom deadline and **published 234 GB after the deadline passed unpaid**; in a 1 June statement DentaQuest confirmed unauthorised access to "a limited portion of its network" ([BleepingComputer, 2026-06-04](https://www.bleepingcomputer.com/news/security/dentaquest-data-breach-exposed-info-of-26-million-accounts/)).

The dataset is HIPAA-format ASC X12 claims interchange — names, postal and email addresses, dates of birth, phone numbers, health-insurance details and **Medicaid IDs** across 2.6 M unique email addresses ([BankInfoSecurity, 2026-06-04](https://www.bankinfosecurity.com/shinyhunters-leaks-234gb-dentaquest-data-trove-a-31883)). DentaQuest's specific attack vector is not publicly confirmed, but the extortion pattern (extortion-without-encryption, a hard deadline, publish-on-refusal) matches the broader ShinyHunters campaign — several of whose other victims this year were reached through compromised cloud-SaaS (Salesforce) access. The operational reminder for defenders is unchanged: this actor monetises pure exfiltration, so backups do not blunt the leverage — detection has to land at the bulk-export stage (large outbound archive transfers from claims systems; and, where cloud-SaaS access has been the entry point for other victims, off-hours SaaS API token generation and anomalous bulk-export API calls).
