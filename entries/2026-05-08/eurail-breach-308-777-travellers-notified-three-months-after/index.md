---
schema: 1
kind: incident
title: "Eurail breach: 308,777 travellers notified three months after a December 2025 data theft exposed names and passport numbers, and DiscoverEU participants' IBANs and health data may also be involved"
headline: "Eurail sent breach letters to 308,777 travellers on 2026-03-27, three months after attackers copied its customer files"
summary: >
  Attackers copied files from Eurail's network on 2025-12-26, and the rail-pass operator sent
  breach letters on 2026-03-27 to 308,777 people whose names and passport numbers were exposed.
  The European Commission warned DiscoverEU participants that passport or ID copies, IBANs and
  health data may also be involved, and says it notified the European Data Protection
  Supervisor.
discovered_at: "2026-05-08T05:00:05Z"
event_date: 2026-04-09
run_id: 2026-05-08-migrated
priority: routine
immediate_action: null
tags:
  - data-breach
regions:
  - europe
sectors: []
entities:
  - "incident:eurail-breach-2026"
techniques: [T1005]
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/eurail-says-december-data-breach-impacts-300-000-individuals/"
    publisher: "BleepingComputer"
    date: "2026-04-09"
    role: primary
  - url: "https://youth.europa.eu/news/updated-data-security-incident-affecting-discovereu-travellers_en"
    publisher: "European Commission, European Youth Portal"
    date: "2026-01-13"
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
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-08.md
updates:
  - at: "2026-09-30T07:13:14Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The earlier text dated the breach letters to late April 2026, said the Dutch data protection
      authority and the European Data Protection Supervisor had opened reviews, said the breach
      exposed passport numbers, IBANs and DiscoverEU pass details, and advised IBAN replacement.
      Eurail sent the letters on 2026-03-27 and lists names and passport numbers as exposed, and the
      Commission says IBANs and health data may be involved and that it notified the EDPS. A
      sentence saying Swiss applicants may be affected had no source and is removed. The priority
      moves from high to routine.
    fields: [title, headline, summary, event_date, priority, sources, verification, classification, body, techniques]
---

Eurail, the Netherlands-based seller of Interrail and Eurail passes and supplier of the EU's DiscoverEU programme, says an unauthorized actor transferred files from its network on 2025-12-26 and sent letters on 2026-03-27 to 308,777 people whose names and passport numbers were exposed ([BleepingComputer, 2026-04-09](https://www.bleepingcomputer.com/news/security/eurail-says-december-data-breach-impacts-300-000-individuals/)), and the European Commission told DiscoverEU participants that passport or ID copies, IBANs and health data may also be involved ([European Commission, 2026-01-13](https://youth.europa.eu/news/updated-data-security-incident-affecting-discovereu-travellers_en)).

**Defender takeaway:** there is no access vector or actor to hunt, and Eurail, which warned in February that a sample of the stolen data had been published on Telegram, advises affected customers to watch for phishing and scams and to change their Rail Planner app password wherever it is reused ([BleepingComputer, 2026-04-09](https://www.bleepingcomputer.com/news/security/eurail-says-december-data-breach-impacts-300-000-individuals/)).

## Correction — 2026-09-30T07:13:14Z

The earlier text said Eurail began sending notifications in late April 2026 and that the Dutch data protection authority and the EDPS had opened reviews of the delay. Eurail sent its letters on 2026-03-27 ([BleepingComputer, 2026-04-09](https://www.bleepingcomputer.com/news/security/eurail-says-december-data-breach-impacts-300-000-individuals/)), and the Commission states only that the EDPS was notified of the breach ([European Commission, 2026-01-13](https://youth.europa.eu/news/updated-data-security-incident-affecting-discovereu-travellers_en)). The earlier text also said the breach exposed passport numbers, IBANs and DiscoverEU pass details, and advised affected people to consider replacing their IBAN. Eurail's letters list names and passport numbers, and Eurail says it stored no financial information on the compromised systems, although its February disclosure listed IBANs and health information ([BleepingComputer, 2026-04-09](https://www.bleepingcomputer.com/news/security/eurail-says-december-data-breach-impacts-300-000-individuals/)). The Commission says DiscoverEU participants' IBANs and health data may be involved ([European Commission, 2026-01-13](https://youth.europa.eu/news/updated-data-security-incident-affecting-discovereu-travellers_en)). The earlier text also said Swiss nationals who applied through a bilateral arrangement may be affected, which no source supports.
