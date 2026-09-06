---
schema: 1
kind: incident
title: >
  KDDI third-party email platform breach exposes up to 14.22 million credentials across six
  Japanese ISPs
headline: >
  KDDI third-party email platform breach exposes up to 14.22 million credentials across six
  Japanese ISPs
summary: >
  KDDI discloses a third-party email-platform breach exposing up to 14.22 million subscriber
  credentials across six Japanese ISPs. Attackers exploited a vulnerability in a shared ISP
  email-management platform (detected ~2026-06-17); email addresses and passwords for STNet, JCOM,
  Chubu Telecommunications, Nifty, Biglobe and one further KDDI ISP are in scope. No CH/EU nexus,
  but the leaked credential pairs feed directly into credential-stuffing and
  phishing-as-initial-access against European targets (BleepingComputer, 2026-06-28).
discovered_at: "2026-06-29T04:47:13Z"
updated_at: "2026-07-09T12:38:00Z"
event_date: 2026-06-28
run_id: 2026-06-29-6d39189a
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - phishing
  - zero-day
regions:
  - apac
  - global
sectors:
  - telco
entities:
  - "incident:kddi-isp-email-platform-breach-2026"
techniques: []
affected_products: []
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
  - url: "https://www.bleepingcomputer.com/news/security/japanese-telecom-giant-kddi-says-data-breach-affects-12-million-people/"
    publisher: BleepingComputer
    date: 2026-07-08
    role: primary
closed_sources: []
evidence:
  - quote: "\"As a result of our investigation, as of June 17, 2026, the date of our confirmation, this vulnerability was not recognized by the software vendor,\" KDDI said."
    publisher: KDDI (via BleepingComputer)
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "Where you host third-party software components on infrastructure holding subscriber or credential data, prioritise behavioural/EDR detection and egress monitoring over patch-management alone — the exploited flaw here was a zero-day the software vendor itself had not recognised, so no patch cadence would have closed it."
  - "Confirm your incident-response playbook includes rapid regulator notification once exploitation is confirmed (KDDI notified Japan's PPC and MIC and completed a forensic audit), and account for multi-tenant platform compromises that cascade across several downstream brands."
updates:
  - at: "2026-07-09T12:38:00Z"
    run_id: 2026-07-09T1211Z-intel
    type: update
    summary: >
      KDDI's 6 July update on the shared email platform serving STNet, JCOM, Chubu Telecommunications,
      NIFTY and BIGLOBE discloses the root cause — a zero-day in an unnamed third-party software
      component, unrecognised by the vendor at KDDI's 17 June discovery date — and confirms final
      scale of 12,233,087 exposed email addresses and 7,616,173 exposed passwords. The transferable
      lesson: a genuine vendor-unknown zero-day that no patch-management process alone would have
      caught, underscoring behavioural/EDR detection on infra hosting third-party components.
    fields:
      - actions
      - entities
      - evidence
      - sources
      - tags
      - body
    merged_from: 2026-07-09/kddi-isp-email-breach-zero-day-root-cause-update
migrated_from: briefs/2026-06-29.md
---

Japanese carrier KDDI disclosed that a threat actor exploited a vulnerability in third-party software integrated into its centralised ISP email-management platform, with unauthorised access detected on approximately 2026-06-17 ([BleepingComputer, 2026-06-28](https://www.bleepingcomputer.com/news/security/data-breach-exposes-up-to-142-million-email-logins-at-six-isps/)). The breach potentially exposed email addresses and passwords for up to 14.22 million subscriber accounts across six ISPs running on the shared platform — STNet, JCOM, Chubu Telecommunications, Nifty, Biglobe and a further KDDI ISP; KDDI states some passwords were stored hashed or encrypted and that 14.22 million is a worst-case figure pending forensic completion ([SecurityAffairs, 2026-06-28](https://securityaffairs.com/194387/data-breach/kddi-data-breach-impacts-up-to-14-2-million-email-accounts-at-six-isps.html); [Infosecurity Magazine, 2026-06-24](https://infosecurity-magazine.com/news/kddi-breach-japanese-telcos/)). No CVE for the third-party software flaw and no threat actor have been named; KDDI notified Japan's Personal Information Protection Commission and advised affected users to change passwords and enable MFA.

**Why it matters to us:** The structural lesson, not the jurisdiction, is the signal — a single vulnerable dependency in a shared multi-tenant email-management plane produced a six-ISP blast radius, the same exposure model any European telco or managed-ISP operator carries when subscriber-mail administration is consolidated onto one vendor platform. The immediate downstream risk for Swiss/EU defenders is credential-stuffing: 14.22 million leaked email/password pairs will surface in combolists and feed phishing-as-initial-access. Hunt for anomalous authentication against external-facing services from Japanese-ISP email address spaces, and treat any reused-password exposure on those domains as a stuffing precursor. Inventory third-party vendor access to your own subscriber/identity-management platforms and enforce MFA on the administration plane itself.

## Update — 2026-07-09T12:38:00Z

KDDI's 6 July update — reported by BleepingComputer on 8 July — discloses the confirmed root cause and exact scale of the breach of the shared email platform serving STNet, JCOM, Chubu Telecommunications, NIFTY and BIGLOBE. The platform was compromised on 16 May 2026 via a zero-day vulnerability in an (still unnamed) third-party software component — a flaw that, per KDDI, "was not recognized by the software vendor" as of KDDI's 17 June confirmation date and which the vendor is now reporting to public authorities ([BleepingComputer, 2026-07-08](https://www.bleepingcomputer.com/news/security/japanese-telecom-giant-kddi-says-data-breach-affects-12-million-people/)). KDDI confirmed final counts of 12,233,087 exposed email addresses and 7,616,173 exposed passwords — down from the earlier "up to 14.22 million" estimate ([BleepingComputer, 2026-06-28](https://www.bleepingcomputer.com/news/security/data-breach-exposes-up-to-142-million-email-logins-at-six-isps/)) — deployed EDR post-incident, completed a forensic audit on 23 June confirming the flaw was patched with no other issues remaining, and notified Japan's Personal Information Protection Commission and the Ministry of Internal Affairs and Communications.

Neither report names the exploited third-party product; KDDI has stated only "third-party software", and that ambiguity is in the source, not omitted here. **Defender takeaway:** the delta of interest for telco and any multi-tenant-platform operator is the disclosure timeline — a multi-tenant email platform serving several ISPs was compromised via a genuine zero-day the software vendor itself had not identified, a scenario no patch-management process alone would have caught, which is the concrete argument for behavioural/EDR detection and egress monitoring on infrastructure hosting third-party components and for rapid regulator notification once exploitation is confirmed.
