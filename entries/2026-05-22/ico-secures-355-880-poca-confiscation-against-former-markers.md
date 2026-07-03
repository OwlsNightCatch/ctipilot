---
schema: 1
kind: incident
horizon: operational
title: "ICO secures £355,880 POCA confiscation against former Markerstudy Insurance employee for off-hours bulk record access and sale"
headline: "ICO secures £355,880 POCA confiscation against former Markerstudy Insurance employee for off-hours bulk record access and sale"
summary: "The UK Information Commissioner's Office announced on 2026-05-21 a £355,880.10 confiscation order at Manchester Crown Court under the Proceeds of Crime Act against Rizwan Manjra, a former Markerstudy Insurance Services Limited employee (ICO, 2026-05-21)."
discovered_at: "2026-05-22T05:00:02Z"
event_date: 2026-05-21
run_id: 2026-05-22-5b90d5a1
priority: notable
immediate_action: null
tags:
  - insider-threat
  - data-breach
  - law-enforcement
regions:
  - uk
sectors:
  - finance
entities: []
cves: []
sources:
  - url: "https://ico.org.uk/action-weve-taken/enforcement/2026/05/rizwan-manjra-proceeds-of-crime-act/"
    publisher: "UK ICO, 2026-05-21"
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
migrated_from: briefs/2026-05-22.md
---

The UK Information Commissioner's Office announced on 2026-05-21 a £355,880.10 confiscation order at Manchester Crown Court under the Proceeds of Crime Act against Rizwan Manjra, a former Markerstudy Insurance Services Limited employee ([ICO, 2026-05-21](https://ico.org.uk/action-weve-taken/enforcement/2026/05/rizwan-manjra-proceeds-of-crime-act/)). Manjra had pleaded guilty in December 2024 under Computer Misuse Act 1990 s.1 after accessing over 32,000 insurance policies on weekends — outside his scheduled hours — and exfiltrating data via mobile phone for onward sale to a third party. The POCA order requires disgorgement of financial benefit; non-payment triggers a 3.5-year default prison term. The enforcement pattern — weekends, anomalously high read volume, exfiltration via mobile rather than corporate network — is the canonical UEBA/behavioural-analytics insider-threat detection profile: any user account generating bulk read activity against insurance, medical, or government record databases outside scheduled shift patterns warrants alert triage (Windows EID 4663 object access on sensitive share / DLP network egress alert on mobile-hotspot NAT patterns). The POCA track running parallel to the GDPR fine channel represents a meaningful escalation in UK enforcement posture applicable to CH/EU insider-threat compliance modelling.
