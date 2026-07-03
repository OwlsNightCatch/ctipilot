---
schema: 1
kind: incident
horizon: operational
title: "Aflac discloses a Japan-subsidiary breach — 4.38 million policyholders and agents, ~10-day dwell before detection"
headline: "Aflac discloses a Japan-subsidiary breach — 4.38 million policyholders and agents, ~10-day dwell before detection"
summary: "Aflac discloses a Japan-subsidiary breach exposing ~4.38 M policyholders and agents after a roughly ten-day undetected intrusion into a customer web portal (SecurityWeek, 2026-06-30)."
discovered_at: "2026-07-01T04:41:14Z"
event_date: 2026-06-30
run_id: 2026-07-01-af9e697d
priority: high
immediate_action: null
tags:
  - data-breach
regions:
  - apac
sectors:
  - finance
entities: []
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/4977/000162828026046124/0001628280-26-046124-index.htm"
    publisher: SEC EDGAR 8-K
    role: primary
  - url: "https://www.securityweek.com/aflac-japan-data-breach-impacts-4-38-million/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/insurance-giant-aflac-discloses-data-breach-after-subsidiary-hack/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://securityaffairs.com/194488/data-breach/hackers-steal-data-of-4-38-million-aflac-japan-customers.html"
    publisher: SecurityAffairs
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
migrated_from: briefs/2026-07-01.md
---

Aflac Incorporated filed an SEC Form 8-K on 2026-06-30 disclosing that attackers held unauthorized access to Aflac Life Insurance Japan's policyholder web portal for roughly ten days (2026-06-15 to 2026-06-25) and exfiltrated personal data on approximately 4.38 million customers and agents — names, addresses, phone numbers, dates of birth, gender, authentication details and insurance-account information; a subset of roughly 230,000 individuals also had premium-transfer bank-account details exposed, and no card data was accessed ([SecurityWeek, 2026-06-30](https://www.securityweek.com/aflac-japan-data-breach-impacts-4-38-million/) · [SEC EDGAR 8-K, 2026-06-30](https://www.sec.gov/Archives/edgar/data/4977/000162828026046124/0001628280-26-046124-index.htm)). Aflac says the intrusion was contained to Japan-subsidiary systems with US operations unaffected, the affected systems were suspended on discovery, and Japan's Financial Services Agency was notified ([BleepingComputer, 2026-06-30](https://www.bleepingcomputer.com/news/security/insurance-giant-aflac-discloses-data-breach-after-subsidiary-hack/)). No initial-access vector or actor attribution is stated in any of the disclosures; this is Aflac's second disclosed breach in roughly a year, but the prior US incident's Scattered-Spider-adjacent framing has not been extended to the Japan event.

**Defender takeaway:** the operationally relevant fact is the ~10-day undetected dwell inside a customer-facing portal exfiltrating bulk PII — a pattern to hunt for as sustained anomalous authenticated-session data pulls / API enumeration against public benefits, insurance or citizen-services portals, not a patchable CVE. No IOC or CVE was disclosed; treat as an access-pattern anomaly cue.
