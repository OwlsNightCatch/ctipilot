---
schema: 1
kind: threat
horizon: operational
title: "UK National Federation of Subpostmasters hit by ransomware via a cPanel flaw; disruption persists into June"
headline: "UK National Federation of Subpostmasters hit by ransomware via a cPanel flaw; disruption persists into June"
summary: "The UK National Federation of Subpostmasters (NFSP) was struck by ransomware around 30 April 2026 after attackers exploited a vulnerability in cPanel to gain initial access, manipulate server-side files, and lock out administrative accounts before deploying ransomware (Computer Weekly, 2026-06-04; Risky …"
discovered_at: "2026-06-05T05:00:03Z"
event_date: 2026-06-05
run_id: 2026-06-05-2c6574c4
priority: notable
immediate_action: null
tags:
  - ransomware
  - vulnerabilities
regions:
  - uk
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.computerweekly.com/news/366643958/Subpostmaster-federation-hit-by-ransomware-attack"
    publisher: "Computer Weekly, 2026-06-04"
    role: primary
  - url: "https://news.risky.biz/risky-bulletin-the-eu-debuts-digital-sovereignty-plan/"
    publisher: "Risky Business, 2026-06-05"
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
migrated_from: briefs/2026-06-05.md
---

The UK **National Federation of Subpostmasters (NFSP)** was struck by ransomware around 30 April 2026 after attackers exploited a vulnerability in **cPanel** to gain initial access, manipulate server-side files, and lock out administrative accounts before deploying ransomware ([Computer Weekly, 2026-06-04](https://www.computerweekly.com/news/366643958/Subpostmaster-federation-hit-by-ransomware-attack); [Risky Business, 2026-06-05](https://news.risky.biz/risky-bulletin-the-eu-debuts-digital-sovereignty-plan/)). As of early June the parent Post Office had suspended all email to and from the `@nfsp.org.uk` domain as a precaution; NFSP says no data was lost and reported the incident to the ICO. The entry vector is the operative detail: cPanel — ubiquitous in shared hosting and small-org infrastructure — remains under-patched, and authentication-bypass / privilege-escalation flaws in it map cleanly to `T1190` (Exploit Public-Facing Application) followed by `T1486` (Data Encrypted for Impact).

**Defender takeaway:** any internet-facing cPanel instance is a ransomware on-ramp. Pin cPanel to the current release (the vendor ships frequent security updates), disable unused modules, and alert on admin-account lockouts and anomalous file-manager / FTP modification events in hosting-management interfaces. Small public-sector-adjacent bodies running their own web hosting are the soft targets here.
