---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: DigiCert support portal compromise — Salesforce-based support-chat social engineering yielded 60 fraudulent EV code-signing certificates
headline: DigiCert support portal compromise — Salesforce-based support-chat social engineering yielded 60 fraudulent EV code-signing certificates
summary: DigiCert confirmed on 2026-05-04 that a targeted social-engineering attack on its Salesforce-based customer-support portal in early April 2026 resulted in the fraudulent generation of 60 Extended Validation code-signing certificates.
discovered_at: "2026-05-04T05:00:19Z"
event_date: 2026-05-06
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - supply-chain
  - data-breach
  - identity
  - phishing
  - china-nexus
regions:
  - global
sectors:
  - technology
entities:
  - "incident:digicert-support-portal-2026"
cves: []
sources:
  - url: "https://www.helpnetsecurity.com/2026/05/04/digicert-breach-code-signing-certificates-malware/"
    publisher: Help Net Security — DigiCert breach
    role: primary
  - url: "https://www.securityweek.com/digicert-revokes-certificates-after-support-portal-hack/"
    publisher: SecurityWeek — DigiCert revokes certificates
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
migrated_from: briefs/weekly/2026-W19.md
---

DigiCert confirmed on 2026-05-04 that a targeted social-engineering attack on its Salesforce-based customer-support portal in early April 2026 resulted in the fraudulent generation of 60 Extended Validation code-signing certificates. Two analyst endpoints were infected via a malicious Windows screensaver (.scr) repeatedly submitted via support chat; the second analyst's endpoint went undetected for approximately twelve days due to absent or degraded EDR coverage. The attacker used portal access to obtain certificate initialization codes and generated 60 EV certificates across multiple customer accounts; DigiCert confirmed 27 were directly attacker-linked; a community member subsequently identified 11 used to sign the **Zhong Stealer** malware family (Chinese e-crime, cryptocurrency-asset targeting). All 60 certificates revoked; MFA now mandatory on portal access; file upload functionality restricted ([Help Net Security, 2026-05-04](https://www.helpnetsecurity.com/2026/05/04/digicert-breach-code-signing-certificates-malware/) · [SecurityWeek, 2026-05-04](https://www.securityweek.com/digicert-revokes-certificates-after-support-portal-hack/) · [daily 2026-05-06](/briefs/2026-05-06/)). **Defender takeaway:** software signed with DigiCert-backed EV certificates during early April through 2026-05-04 warrants validation against the revoked certificate list; the recurring root cause across this and the third-party-analytics incidents in § 2 is that *support-tier* and *analyst-tier* endpoints frequently receive lower EDR-coverage bar than production endpoints despite holding equivalent or higher operational privilege.
