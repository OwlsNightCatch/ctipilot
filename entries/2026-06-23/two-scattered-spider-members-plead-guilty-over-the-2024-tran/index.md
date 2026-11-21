---
schema: 1
kind: threat
title: Two Scattered Spider members plead guilty over the 2024 Transport for London intrusion
headline: Two Scattered Spider members plead guilty over the 2024 Transport for London intrusion
summary: >
  Thalha Jubair (20) and Owen Flowers (18) changed their pleas to guilty at Woolwich Crown Court
  on 2026-06-22, both admitting conspiracy to commit unauthorised acts against Transport for
  London under the Computer Misuse Act (UK National Crime Agency, 2026-06-22; ITV News,
  2026-06-22).
discovered_at: "2026-06-23T04:52:45Z"
updated_at: "2026-07-17T04:35:00Z"
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
entities:
  - "actor:scattered-spider"
  - "incident:tfl-scattered-spider-2024"
techniques:
  - T1589.001
  - T1566.004
  - T1098
  - T1078
affected_products: []
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
  - url: "https://www.nationalcrimeagency.gov.uk/news/two-sentenced-for-hacking-transport-for-london-in-uk-s-biggest-ever-cyber-crime-case"
    publisher: UK National Crime Agency (NCA)
    date: 2026-07-16
    role: primary
  - url: "https://www.cps.gov.uk/national-news/news/cyberhackers-who-targeted-tfl-jailed-more-five-years-each"
    publisher: UK Crown Prosecution Service (CPS)
    date: 2026-07-16
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446"
    publisher: The Register
    date: 2026-07-16
    role: corroborating
closed_sources: []
evidence:
  - quote: "a total of 148 systems became inoperable, including critical ones that required significant manual workarounds and delays."
    publisher: UK National Crime Agency
  - quote: "Flowers and Jubair purchased partial TfL credentials from \"well-known criminal forums\" and used those to reset the 2FA on employee accounts, a process that took multiple attempts."
    publisher: The Register
  - quote: Woolwich Crown Court heard that the pair impersonated an employee and socially engineered a TfL helpdesk worker into resetting the password for their account.
    publisher: The Register
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-17T04:35:00Z"
    run_id: 2026-07-17T0409Z-intel
    type: update
    summary: >
      Owen Flowers and Thalha Jubair, named by the NCA and CPS as leading Scattered Spider members,
      were sentenced on 2026-07-16 to five years six months each for the Aug-Sep 2024 Transport for
      London intrusion. The new, operationally relevant delta over the June guilty-plea coverage is
      the court-record intrusion chain: the pair bought partial TfL employee credentials from criminal
      forums, impersonated an employee to vish a TfL helpdesk worker into resetting the account
      password and — over multiple attempts — its 2FA, then used the reset credentials as
      valid-account access. TfL later confirmed ~7 million users' data was accessible (not the ~5,000
      first believed); 148 systems were rendered inoperable.
    fields:
      - entities
      - evidence
      - sources
      - techniques
      - body
    merged_from: 2026-07-17/scattered-spider-tfl-sentencing-helpdesk-vishing
migrated_from: briefs/2026-06-23.md
---

Thalha Jubair (20) and Owen Flowers (18) changed their pleas to guilty at Woolwich Crown Court on 2026-06-22, both admitting conspiracy to commit unauthorised acts against Transport for London under the Computer Misuse Act ([UK National Crime Agency, 2026-06-22](https://www.nationalcrimeagency.gov.uk/news/cyber-criminals-who-hacked-into-transport-for-londons-computer-network-are-convicted); [ITV News, 2026-06-22](https://www.itv.com/news/london/2026-06-22/two-young-men-admit-carrying-out-cyber-attack-on-transport-for-london)). The 31 August – 3 September 2024 intrusion disrupted TfL services for three months, forced in-person password resets for all 28,000 staff, and affected roughly 10 million customers including Oyster systems, at a cost the NCA puts at £29M in loss and recovery (ITV and the BBC reported £39M. Flowers additionally admitted attempted intrusions against US healthcare providers Sutter Health and SSM Health; the NCA ties both defendants to the Scattered Spider collective (UNC3944 / Storm-0875), and sentencing is set for 16 July 2026 ([Yahoo/BBC, 2026-06-22](https://ca.news.yahoo.com/two-men-plead-guilty-over-143055796.html)).

**Defender takeaway:** The TfL breach is the canonical Scattered Spider playbook — social-engineering the IT help desk, SIM-swap / MFA-fatigue to defeat second factors, then lateral movement — and none of it turned on a software vulnerability (`T1566` Phishing, `T1078` Valid Accounts, `T1621` Multi-Factor Authentication Request Generation). For EU/CH public-sector operators the durable control is help-desk procedure: require out-of-band secondary verification before any MFA-device reset or password reset on privileged accounts, and alert when a single account generates a burst of MFA push rejections immediately followed by a successful logon. The guilty pleas are a reminder the collective remains active against public-sector and healthcare targets.

## Update — 2026-07-17T04:35:00Z

The guilty-plea entry recorded that two Scattered Spider members admitted the 2024 TfL intrusion but did not carry the access mechanics. The 2026-07-16 sentencing (five years six months each, at Woolwich Crown Court) put the chain on the court record, and it is the reason to revisit this. The pair bought partial TfL employee credentials from criminal forums, then "impersonated an employee and socially engineered a TfL helpdesk worker into resetting the password for their account" and, over multiple attempts, reset the account's 2FA, using the reset credentials for initial and sustained access ([The Register, 2026-07-16](https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446)). The NCA confirmed the impact scale — "a total of 148 systems became inoperable, including critical ones that required significant manual workarounds and delays" ([NCA, 2026-07-16](https://www.nationalcrimeagency.gov.uk/news/two-sentenced-for-hacking-transport-for-london-in-uk-s-biggest-ever-cyber-crime-case)) — and TfL later established that data on roughly 7 million users had been accessible, far beyond the ~5,000 initially believed ([The Register, 2026-07-16](https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446)). The CPS put the remediation cost at £29 million ([CPS, 2026-07-16](https://www.cps.gov.uk/national-news/news/cyberhackers-who-targeted-tfl-jailed-more-five-years-each)).

**Defender takeaway:** the compromise never touched a technical vulnerability — the single control point was the helpdesk's password/MFA-reset process, the recurring Scattered Spider signature. Defenders should treat helpdesk-initiated credential and MFA resets as a distinct, monitorable event class rather than an implicitly trusted administrative action: capture who requested the reset, what identity verification was performed, and how quickly a privileged or unusual action followed. **Triage:** a legitimate reset is tied to a verified requester and is not immediately followed by anomalous access; the discriminators are a reset requested for an account whose owner did not initiate it, repeated 2FA-reset attempts on one account, and a short interval between a helpdesk reset and first sign-in from a new device/location.
