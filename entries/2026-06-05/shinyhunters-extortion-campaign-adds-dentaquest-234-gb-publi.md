---
schema: 1
kind: incident
horizon: operational
title: "ShinyHunters extortion campaign adds DentaQuest — 234 GB published after refusal to pay, 2.6 M dental-benefit records exposed"
headline: "ShinyHunters extortion campaign adds DentaQuest — 234 GB published after refusal to pay, 2.6 M dental-benefit records exposed"
summary: "UPDATE (originally covered 2026-06-02): DentaQuest, a Sun Life subsidiary administering dental and vision benefits for ~35 M US Medicaid, Medicare and employer-plan members, is the latest confirmed named victim of the ShinyHunters data-extortion campaign last covered here on the Charter Communications listing."
discovered_at: "2026-06-05T05:00:07Z"
event_date: 2026-06-04
run_id: 2026-06-05-2c6574c4
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
regions:
  - us
sectors:
  - healthcare
entities:
  - "actor:shinyhunters"
  - "incident:dentaquest-shinyhunters-2026"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/dentaquest-data-breach-exposed-info-of-26-million-accounts/"
    publisher: "BleepingComputer, 2026-06-04"
    role: primary
  - url: "https://www.bankinfosecurity.com/shinyhunters-leaks-234gb-dentaquest-data-trove-a-31883"
    publisher: "BankInfoSecurity, 2026-06-04"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-02/shinyhunters-publishes-the-charter-communications-dataset-af
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-05.md
---

**UPDATE (originally covered 2026-06-02):** DentaQuest, a Sun Life subsidiary administering dental and vision benefits for ~35 M US Medicaid, Medicare and employer-plan members, is the latest confirmed named victim of the ShinyHunters data-extortion campaign last covered here on the Charter Communications listing. ShinyHunters listed DentaQuest on 23 May with a 27 May ransom deadline and **published 234 GB after the deadline passed unpaid**; in a 1 June statement DentaQuest confirmed unauthorised access to "a limited portion of its network" ([BleepingComputer, 2026-06-04](https://www.bleepingcomputer.com/news/security/dentaquest-data-breach-exposed-info-of-26-million-accounts/)).

The dataset is HIPAA-format ASC X12 claims interchange — names, postal and email addresses, dates of birth, phone numbers, health-insurance details and **Medicaid IDs** across 2.6 M unique email addresses ([BankInfoSecurity, 2026-06-04](https://www.bankinfosecurity.com/shinyhunters-leaks-234gb-dentaquest-data-trove-a-31883)). DentaQuest's specific attack vector is not publicly confirmed, but the extortion pattern (extortion-without-encryption, a hard deadline, publish-on-refusal) matches the broader ShinyHunters campaign — several of whose other victims this year were reached through compromised cloud-SaaS (Salesforce) access. The operational reminder for defenders is unchanged: this actor monetises pure exfiltration, so backups do not blunt the leverage — detection has to land at the bulk-export stage (large outbound archive transfers from claims systems; and, where cloud-SaaS access has been the entry point for other victims, off-hours SaaS API token generation and anomalous bulk-export API calls).
