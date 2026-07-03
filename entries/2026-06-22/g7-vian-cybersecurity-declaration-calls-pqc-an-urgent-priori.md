---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "G7 Évian cybersecurity declaration calls PQC an \"urgent priority\" — and the expected hacktivist DDoS materialised on day one"
headline: "G7 Évian cybersecurity declaration calls PQC an \"urgent priority\" — and the expected hacktivist DDoS materialised on day one"
summary: "Policy: the G7 called PQC an \"urgent priority\" and the predicted NoName057(16) DDoS hit Swiss-border Haute-Savoie sites; the CRA's first reporting obligation lands 11 September. (ANSSI, Cyberattaque.org)"
discovered_at: "2026-06-22T00:15:09Z"
event_date: 2026-06-17
run_id: 2026-W25-0aacfe65
priority: high
immediate_action: null
tags:
  - ddos
  - hacktivism
  - eu-nexus
  - russia-nexus
regions:
  - europe
  - switzerland
sectors:
  - public-sector
  - transport
entities:
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
cves: []
sources:
  - url: "https://cyber.gouv.fr/en/publications/jointly-led-international-publications/declaration-of-the-g7-cybersecurity-working-group/"
    publisher: ANSSI — G7 CWG Declaration
    role: primary
  - url: "https://www.cyberattaque.org/g7-devian-plusieurs-sites-publics-de-haute-savoie-cibles-par-des-cyberattaques/"
    publisher: Cyberattaque.org — Haute-Savoie DDoS
    role: corroborating
  - url: "https://digital-strategy.ec.europa.eu/en/news/european-commission-welcomes-g7-cybersecurity-declaration-strengthen-global-digital-resilience"
    publisher: European Commission
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
migrated_from: briefs/weekly/2026-W25.md
---

The G7 Cybersecurity Working Group declaration, adopted around the Évian summit (15–17 June), names post-quantum cryptography an "urgent priority" with a call for coordinated industry-government migration, alongside AI-cyber dual-use risk, telecom resilience and SME cybersecurity; the European Commission issued a welcome statement linking it to the NIS2/CRA stack ([ANSSI](https://cyber.gouv.fr/en/publications/jointly-led-international-publications/declaration-of-the-g7-cybersecurity-working-group/); [European Commission, 2026-06-17](https://digital-strategy.ec.europa.eu/en/news/european-commission-welcomes-g7-cybersecurity-declaration-strengthen-global-digital-resilience)). The PQC-urgency framing aligns with Swiss federal cryptographic-migration planning. Resolving the W24 looking-ahead watch item: the NCSC-CH-predicted hacktivist DDoS did materialise — NoName057(16) ran layer-7 DDoS on 15 June against public-sector and tourism sites in the Swiss-bordering Haute-Savoie department (Évian-les-Bains, Thonon-les-Bains, Saint-Gingolph municipalities, the EVA'D transport portal), causing temporary outages with no data compromise ([Cyberattaque.org, 2026-06-16](https://www.cyberattaque.org/g7-devian-plusieurs-sites-publics-de-haute-savoie-cibles-par-des-cyberattaques/); [NCSC-CH pre-event advisory](https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/massnahmen-grossanlaesse-konferenzen-g7.html)). Attribution rests on the group's Telegram self-claim; no Swiss federal sites were reported hit. The lesson reconfirmed: NCSC-CH's pre-event DDoS guidance for summit-adjacent organisations was correctly calibrated, and the NoName057(16) pattern around Swiss-adjacent summits (cf. Bürgenstock 2024) holds.
