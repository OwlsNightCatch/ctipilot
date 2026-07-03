---
schema: 1
kind: incident
horizon: operational
title: Xsolis healthcare-AI vendor breach exposes 1.4M patients across seven US health systems — third-party processor pattern
headline: Xsolis healthcare-AI vendor breach exposes 1.4M patients across seven US health systems — third-party processor pattern
summary: "Xsolis, a Tennessee-based healthcare-AI vendor supplying utilization-management software to hospitals, disclosed that a phishing-driven intrusion on 2026-01-20/22 gave an attacker access to a limited environment, exposing data on 1,396,519 patients across at least seven US health systems (HIPAA Journal, 2026-06-23 …"
discovered_at: "2026-06-24T05:11:48Z"
event_date: 2026-06-23
run_id: 2026-06-24-de656486
priority: notable
immediate_action: null
tags:
  - data-breach
  - phishing
  - supply-chain
regions:
  - us
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.hipaajournal.com/xsolis-data-breach/"
    publisher: HIPAA Journal
    role: primary
  - url: "https://securityaffairs.com/194067/cyber-crime/xsolis-data-breach-impacts-1-4-million-people.html"
    publisher: Security Affairs
    role: corroborating
closed_sources: []
evidence:
  - quote: "Xsolis confirmed a phishing attack on January 20-22, 2026 resulted in unauthorized access to a limited environment"
    publisher: HIPAA Journal
  - quote: "The total number of individuals affected across all seven health systems is 1,396,519"
    publisher: HIPAA Journal
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
migrated_from: briefs/2026-06-24.md
---

Xsolis, a Tennessee-based healthcare-AI vendor supplying utilization-management software to hospitals, disclosed that a phishing-driven intrusion on 2026-01-20/22 gave an attacker access to a limited environment, exposing data on 1,396,519 patients across at least seven US health systems ([HIPAA Journal, 2026-06-23](https://www.hipaajournal.com/xsolis-data-breach/); [Security Affairs, 2026-06-23](https://securityaffairs.com/194067/cyber-crime/xsolis-data-breach-impacts-1-4-million-people.html)). Exposed data spans patient names, addresses, dates of birth, dates of service, medical record numbers, diagnosis/treatment and health-insurance information, and — for some individuals — **Social Security numbers** (affected patients were offered credit-monitoring / identity-theft protection); Xsolis says it contained the intrusion within ~48 hours and reports no confirmed misuse of the data as of disclosure. The ~5-month gap between intrusion (January) and broad notification (June) reflects the breach cascading through Xsolis as a HIPAA Business Associate to each covered-entity client's own notification clock.

**Defender takeaway:** No CH/EU victims, but the structure is the lesson for European health and public-sector buyers: a single multi-tenant processor compromise propagates exposure across every client, and phishing-to-limited-environment access points at MFA gaps on a service or staff account with repository access. The EU/CH analogues are GDPR Article 28 processor-audit duties and the 72-hour processor-to-controller notification expectation. Detection focus for any shared patient/records repository: anomalous bulk-export and off-hours query volume from service/API accounts (`T1078` Valid Accounts, `T1567` Exfiltration Over Web Service), and enforced phishing-resistant MFA on every account that can reach the data store.
