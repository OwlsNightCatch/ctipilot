---
schema: 1
kind: threat
horizon: operational
title: Two Scattered Spider members plead guilty over the 2024 Transport for London intrusion
headline: Two Scattered Spider members plead guilty over the 2024 Transport for London intrusion
summary: "Thalha Jubair (20) and Owen Flowers (18) changed their pleas to guilty at Woolwich Crown Court on 2026-06-22, both admitting conspiracy to commit unauthorised acts against Transport for London under the Computer Misuse Act (UK National Crime Agency, 2026-06-22; ITV News, 2026-06-22)."
discovered_at: "2026-06-23T04:52:45Z"
event_date: 2026-06-22
run_id: 2026-06-23-165387f6
priority: notable
immediate_action: null
tags:
  - organized-crime
  - law-enforcement
  - identity
  - phishing
regions:
  - uk
  - europe
sectors:
  - transport
  - public-sector
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.nationalcrimeagency.gov.uk/news/cyber-criminals-who-hacked-into-transport-for-londons-computer-network-are-convicted"
    publisher: UK National Crime Agency
    role: primary
  - url: "https://www.itv.com/news/london/2026-06-22/two-young-men-admit-carrying-out-cyber-attack-on-transport-for-london"
    publisher: ITV News
    role: corroborating
  - url: "https://ca.news.yahoo.com/two-men-plead-guilty-over-143055796.html"
    publisher: Yahoo/BBC
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
migrated_from: briefs/2026-06-23.md
---

Thalha Jubair (20) and Owen Flowers (18) changed their pleas to guilty at Woolwich Crown Court on 2026-06-22, both admitting conspiracy to commit unauthorised acts against Transport for London under the Computer Misuse Act ([UK National Crime Agency, 2026-06-22](https://www.nationalcrimeagency.gov.uk/news/cyber-criminals-who-hacked-into-transport-for-londons-computer-network-are-convicted); [ITV News, 2026-06-22](https://www.itv.com/news/london/2026-06-22/two-young-men-admit-carrying-out-cyber-attack-on-transport-for-london)). The 31 August – 3 September 2024 intrusion disrupted TfL services for three months, forced in-person password resets for all 28,000 staff, and affected roughly 10 million customers including Oyster systems, at a cost the NCA puts at £29M in loss and recovery (ITV and the BBC reported £39M. Flowers additionally admitted attempted intrusions against US healthcare providers Sutter Health and SSM Health; the NCA ties both defendants to the Scattered Spider collective (UNC3944 / Storm-0875), and sentencing is set for 16 July 2026 ([Yahoo/BBC, 2026-06-22](https://ca.news.yahoo.com/two-men-plead-guilty-over-143055796.html)).

**Defender takeaway:** The TfL breach is the canonical Scattered Spider playbook — social-engineering the IT help desk, SIM-swap / MFA-fatigue to defeat second factors, then lateral movement — and none of it turned on a software vulnerability (`T1566` Phishing, `T1078` Valid Accounts, `T1621` Multi-Factor Authentication Request Generation). For EU/CH public-sector operators the durable control is help-desk procedure: require out-of-band secondary verification before any MFA-device reset or password reset on privileged accounts, and alert when a single account generates a burst of MFA push rejections immediately followed by a successful logon. The guilty pleas are a reminder the collective remains active against public-sector and healthcare targets.
