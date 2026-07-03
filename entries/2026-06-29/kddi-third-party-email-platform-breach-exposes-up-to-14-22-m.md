---
schema: 1
kind: incident
horizon: operational
title: KDDI third-party email platform breach exposes up to 14.22 million credentials across six Japanese ISPs
headline: KDDI third-party email platform breach exposes up to 14.22 million credentials across six Japanese ISPs
summary: "KDDI discloses a third-party email-platform breach exposing up to 14.22 million subscriber credentials across six Japanese ISPs. Attackers exploited a vulnerability in a shared ISP email-management platform (detected ~2026-06-17); email addresses and passwords for STNet, JCOM, Chubu Telecommunications, Nifty, Biglobe and one further KDDI ISP are in scope. No CH/EU nexus, but the leaked credential pairs feed directly into credential-stuffing and phishing-as-initial-access against European targets (BleepingComputer, 2026-06-28)."
discovered_at: "2026-06-29T04:47:13Z"
event_date: 2026-06-28
run_id: 2026-06-29-6d39189a
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - phishing
regions:
  - apac
  - global
sectors:
  - telco
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/data-breach-exposes-up-to-142-million-email-logins-at-six-isps/"
    publisher: BleepingComputer
    role: primary
  - url: "https://securityaffairs.com/194387/data-breach/kddi-data-breach-impacts-up-to-14-2-million-email-accounts-at-six-isps.html"
    publisher: SecurityAffairs
    role: corroborating
  - url: "https://infosecurity-magazine.com/news/kddi-breach-japanese-telcos/"
    publisher: Infosecurity Magazine
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
migrated_from: briefs/2026-06-29.md
---

Japanese carrier KDDI disclosed that a threat actor exploited a vulnerability in third-party software integrated into its centralised ISP email-management platform, with unauthorised access detected on approximately 2026-06-17 ([BleepingComputer, 2026-06-28](https://www.bleepingcomputer.com/news/security/data-breach-exposes-up-to-142-million-email-logins-at-six-isps/)). The breach potentially exposed email addresses and passwords for up to 14.22 million subscriber accounts across six ISPs running on the shared platform — STNet, JCOM, Chubu Telecommunications, Nifty, Biglobe and a further KDDI ISP; KDDI states some passwords were stored hashed or encrypted and that 14.22 million is a worst-case figure pending forensic completion ([SecurityAffairs, 2026-06-28](https://securityaffairs.com/194387/data-breach/kddi-data-breach-impacts-up-to-14-2-million-email-accounts-at-six-isps.html); [Infosecurity Magazine, 2026-06-24](https://infosecurity-magazine.com/news/kddi-breach-japanese-telcos/)). No CVE for the third-party software flaw and no threat actor have been named; KDDI notified Japan's Personal Information Protection Commission and advised affected users to change passwords and enable MFA.

**Why it matters to us:** The structural lesson, not the jurisdiction, is the signal — a single vulnerable dependency in a shared multi-tenant email-management plane produced a six-ISP blast radius, the same exposure model any European telco or managed-ISP operator carries when subscriber-mail administration is consolidated onto one vendor platform. The immediate downstream risk for Swiss/EU defenders is credential-stuffing: 14.22 million leaked email/password pairs will surface in combolists and feed phishing-as-initial-access. Hunt for anomalous authentication against external-facing services from Japanese-ISP email address spaces, and treat any reused-password exposure on those domains as a stuffing precursor. Inventory third-party vendor access to your own subscriber/identity-management platforms and enforce MFA on the administration plane itself.
