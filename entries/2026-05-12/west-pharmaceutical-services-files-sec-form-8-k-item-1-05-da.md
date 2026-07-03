---
schema: 1
kind: incident
horizon: operational
title: "West Pharmaceutical Services files SEC Form 8-K Item 1.05 — data exfiltrated, systems encrypted, global operations partially restarted"
headline: "West Pharmaceutical Services files SEC Form 8-K Item 1.05 — data exfiltrated, systems encrypted, global operations partially restarted"
summary: "West Pharmaceutical Services Inc. (NYSE: WST), a US-headquartered global manufacturer of drug-delivery and packaging components, filed a Form 8-K on 2026-05-11 disclosing a material cybersecurity incident under Item 1.05 (SEC EDGAR — WST 8-K, 2026-05-11)."
discovered_at: "2026-05-12T05:00:02Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - supply-chain
regions:
  - us
  - global
sectors:
  - healthcare
  - manufacturing
entities: []
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm"
    publisher: "SEC EDGAR — West Pharmaceutical Services Inc. Form 8-K, 2026-05-11"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
---

West Pharmaceutical Services Inc. (NYSE: WST), a US-headquartered global manufacturer of drug-delivery and packaging components, filed a Form 8-K on **2026-05-11** disclosing a material cybersecurity incident under Item 1.05 ([SEC EDGAR — WST 8-K, 2026-05-11](https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm)). The filing states that detection occurred on **May 4 2026**, materiality was determined **May 7**, and that "certain data was exfiltrated by an unauthorized party and certain systems were encrypted" — terminology consistent with a [T1486 Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486/) plus [T1041 Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041/) double-extortion ransomware pattern. The company took global systems offline, activated incident response, notified law enforcement and engaged external forensics; core enterprise systems are restored, shipping/receiving/manufacturing are partially restarted at some facilities, and full restoration timeline and material financial impact remain undetermined. No threat actor has claimed responsibility publicly at time of filing.

**Defender takeaway:** A double-extortion event against an OT-adjacent pharmaceutical packaging manufacturer is a high-supply-chain-risk template — West Pharma's elastomeric closures, vials and drug-delivery devices feed European biopharma packaging lines including those of national-formulary suppliers. EU public-sector procurement teams handling pharmaceutical resilience plans should validate continuity-of-supply with downstream vendors that source closures or delivery devices from West. Detection pivot for analogous targets: large-volume SMB enumeration, VSSAdmin / WBEM shadow-copy deletion ([T1490 Inhibit System Recovery](https://attack.mitre.org/techniques/T1490/)), and abnormal DLP egress volume in the days preceding encryption — the encryption event is rarely the first indicator if logs are retained.
