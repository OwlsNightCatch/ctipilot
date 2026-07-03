---
schema: 1
kind: incident
horizon: operational
title: "Lithuania's Centre of Registers loses ~600,000 state-register records to abused institutional credentials; foreign-state actor suspected"
headline: "Lithuania's Centre of Registers loses ~600,000 state-register records to abused institutional credentials; foreign-state actor suspected"
summary: "Lithuania's Centre of Registers breached — ~600,000 property and legal-entity records exfiltrated. Attackers abused login credentials issued to institutions authorised to query the Real Estate Register and Register of Legal Entities, querying from foreign-administered infrastructure; Vilnius's prosecutors suspect a foreign-state actor and the agency head resigned within days (The Record, 2026-05-26). The same register architecture exists in every EU member state."
discovered_at: "2026-05-27T05:00:00Z"
event_date: 2026-05-26
run_id: 2026-05-27-0b6f12dd
priority: high
immediate_action: null
tags:
  - data-breach
  - espionage
  - nation-state
  - identity
  - russia-nexus
regions:
  - europe
  - russia-cis
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://therecord.media/lithuania-investigates-theft-of-state-records"
    publisher: "The Record, 2026-05-26"
    role: primary
  - url: "https://www.euronews.com/2026/05/25/lithuania-warns-mass-data-leak-was-work-of-foreign-country"
    publisher: "Euronews, 2026-05-25"
    role: corroborating
  - url: "https://www.lrt.lt/en/news-in-english/19/2936340/lithuania-probes-theft-of-600-000-records-from-state-registry"
    publisher: "LRT, 2026-05-22"
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
migrated_from: briefs/2026-05-27.md
---

Lithuania's Prosecutor General's Office disclosed that attackers accessed more than 600,000 records from the Centre of Registers — the state enterprise that manages the Real Estate Register and the Register of Legal Entities — over a window running from early April to disclosure ([The Record, 2026-05-26](https://therecord.media/lithuania-investigates-theft-of-state-records)). The access vector was not a software exploit but credential abuse: attackers obtained and misused login credentials assigned to institutions authorised to query the registers, originating the connections from foreign-administered infrastructure ([The Record, 2026-05-26](https://therecord.media/lithuania-investigates-theft-of-state-records)). Exfiltrated fields include names, dates of birth, national ID numbers, property addresses, cadastral numbers and registry identifiers; contact details, bank accounts and payment data were reported as not in the stolen set. Lithuanian officials publicly framed the incident as likely the work of a foreign country, with one politician alleging Russian-intelligence hallmarks, and the head of the Centre of Registers resigned within days ([Euronews, 2026-05-25](https://www.euronews.com/2026/05/25/lithuania-warns-mass-data-leak-was-work-of-foreign-country); [LRT, 2026-05-22](https://www.lrt.lt/en/news-in-english/19/2936340/lithuania-probes-theft-of-600-000-records-from-state-registry)). Reporting cross-references comparable intrusions against Slovakia's land register and Ukraine's state registers.

**Why it matters to us:** property and corporate-entity registers are high dossier-value targets — they let an intelligence service resolve home addresses and asset holdings for officials, diplomats and military personnel — and the identical register-API architecture is in production across every EU member state, Switzerland's commercial register (Zefix) and cantonal land registries included. The kill chain here is authorised-account abuse (`T1078` Valid Accounts / `T1530` Data from Cloud Storage), not a CVE: institutional service accounts querying register APIs need per-institution rate limits, MFA on the service principal, ASN/IP-range anchoring (institutional access should originate from known networks), and query-volume anomaly detection. Hunt for bulk-query bursts from institutional accounts outside business hours or from ASNs inconsistent with the institution's historical access pattern, and retain register access logs long enough to reconstruct a multi-week exfiltration window.
