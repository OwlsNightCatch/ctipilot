---
schema: 1
kind: threat
title: "INTERPOL Operation Ramz — 13-country MENA cybercrime sweep: 201 arrests, 53 servers seized, Algerian PhaaS server takedown"
headline: "INTERPOL Operation Ramz — 13-country MENA cybercrime sweep: 201 arrests, 53 servers seized, Algerian PhaaS server takedown"
summary: "INTERPOL announced on 2026-05-18 the completion of Operation Ramz — described as the first cyber operation of its scale coordinated by INTERPOL specifically targeting the MENA region — running October 2025 through 2026-02-28 across 13 countries (Algeria, Bahrain, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Oman …"
discovered_at: "2026-05-19T05:00:04Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - phishing
  - eu-nexus
regions:
  - middle-east
  - africa
  - europe
sectors:
  - finance
  - public-sector
entities:
  - "campaign:interpol-operation-ramz-mena-cybercrime-13-country-201-arre"
cves: []
sources:
  - url: "https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region"
    publisher: INTERPOL
    role: primary
  - url: "https://thehackernews.com/2026/05/interpol-operation-ramz-disrupts-mena.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/18/interpol-mena-cybercrime-operation-ramz-201-arrests/"
    publisher: Help Net Security
    role: corroborating
closed_sources: []
evidence:
  - quote: "A first-of-its-kind cybercrime operation in the MENA region has led to the arrest of 201 individuals, with a further 382 suspects identified"
    publisher: INTERPOL
  - quote: "In Algeria, a website offering phishing as a service was identified and dismantled as part of Operation Ramz"
    publisher: INTERPOL
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
migrated_from: briefs/2026-05-19.md
---

INTERPOL announced on 2026-05-18 the completion of Operation Ramz — described as the first cyber operation of its scale coordinated by INTERPOL specifically targeting the MENA region — running October 2025 through 2026-02-28 across 13 countries (Algeria, Bahrain, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Oman, Palestine, Qatar, Tunisia, UAE) ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region); [The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/interpol-operation-ramz-disrupts-mena.html); [Help Net Security, 2026-05-18](https://www.helpnetsecurity.com/2026/05/18/interpol-mena-cybercrime-operation-ramz-201-arrests/)). Outcomes: 201 arrests, 382 further suspects identified, 3,867 victims, 53 servers seized, ~8,000 intelligence data points disseminated. Algerian authorities dismantled a phishing-as-a-service operation, seizing a server, computer and hard drives containing phishing software and scripts. Moroccan police seized devices with banking data and phishing tooling; Omani investigators identified a residential server with active malware infection. Jordanian police rescued 15 human-trafficking victims who had been coerced into running cybercrime operations — the same forced-labour-to-cyber-scam pipeline documented in Southeast Asian fraud compounds. Industry partners: Group-IB, Kaspersky, Shadowserver Foundation, Team Cymru, TrendAI. The operation is partially funded by the EU and Council of Europe under the CyberSouth+ project.

**Why it matters to us:** MENA-based PhaaS kits routinely target EU banking customers and EU payment rails (SEPA-Inst flagging, IBAN-based phishing lures); the disruption reduces commodity-kit availability and the Shadowserver / Group-IB intelligence shared via the operation will surface in NCSC / BSI / NCSC-CH advisories over the coming weeks. The trafficking-to-scam pipeline confirmed in Jordan is the same operator model EUROPOL has been mapping for fraud-compound disruption.
