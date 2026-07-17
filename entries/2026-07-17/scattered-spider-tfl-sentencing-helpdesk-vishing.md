---
schema: 1
kind: incident
horizon: operational
title: "Scattered Spider duo sentenced to 5.5 years each over the 2024 Transport for London intrusion — court evidence details the helpdesk-vishing/MFA-reset chain"
headline: "TfL hackers sentenced; court record confirms the credential-purchase → helpdesk-vishing → MFA-reset access chain"
summary: >
  Owen Flowers and Thalha Jubair, named by the NCA and CPS as leading Scattered Spider members, were sentenced on
  2026-07-16 to five years six months each for the Aug-Sep 2024 Transport for London intrusion. The new,
  operationally relevant delta over the June guilty-plea coverage is the court-record intrusion chain: the pair
  bought partial TfL employee credentials from criminal forums, impersonated an employee to vish a TfL helpdesk
  worker into resetting the account password and — over multiple attempts — its 2FA, then used the reset
  credentials as valid-account access. TfL later confirmed ~7 million users' data was accessible (not the ~5,000
  first believed); 148 systems were rendered inoperable.
discovered_at: "2026-07-17T04:35:00Z"
event_date: "2026-07-16"
run_id: 2026-07-17T0409Z-intel
priority: notable
immediate_action: null
tags: [law-enforcement, identity, phishing]
regions: [uk]
sectors: [transport, public-sector]
entities: ["actor:scattered-spider", "incident:tfl-scattered-spider-2024"]
techniques: [T1589.001, T1566.004, T1098, T1078]
affected_products: []
cves: []
sources:
  - url: "https://www.nationalcrimeagency.gov.uk/news/two-sentenced-for-hacking-transport-for-london-in-uk-s-biggest-ever-cyber-crime-case"
    publisher: "UK National Crime Agency (NCA)"
    date: "2026-07-16"
    role: primary
  - url: "https://www.cps.gov.uk/national-news/news/cyberhackers-who-targeted-tfl-jailed-more-five-years-each"
    publisher: "UK Crown Prosecution Service (CPS)"
    date: "2026-07-16"
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446"
    publisher: "The Register"
    date: "2026-07-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "a total of 148 systems became inoperable, including critical ones that required significant manual workarounds and delays."
    publisher: "UK National Crime Agency"
  - quote: "Flowers and Jubair purchased partial TfL credentials from \"well-known criminal forums\" and used those to reset the 2FA on employee accounts, a process that took multiple attempts."
    publisher: "The Register"
  - quote: "Woolwich Crown Court heard that the pair impersonated an employee and socially engineered a TfL helpdesk worker into resetting the password for their account."
    publisher: "The Register"
verification: multi-source
sourcing_note: "Sentencing and impact figures from the NCA and CPS (Admiralty A1); the helpdesk-vishing/credential-purchase mechanics are on the court record, reported by The Register and consistent with the CPS/NCA statements. The NCA declines to confirm any link between the two individuals and other Scattered Spider-attributed attacks."
confidence: high
update_of: 2026-06-23/two-scattered-spider-members-plead-guilty-over-the-2024-tran
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-06-23):** the guilty-plea entry recorded that two Scattered Spider members admitted the 2024 TfL intrusion but did not carry the access mechanics. The 2026-07-16 sentencing (five years six months each, at Woolwich Crown Court) put the chain on the court record, and it is the reason to revisit this. The pair bought partial TfL employee credentials from criminal forums, then "impersonated an employee and socially engineered a TfL helpdesk worker into resetting the password for their account" and, over multiple attempts, reset the account's 2FA, using the reset credentials for initial and sustained access ([The Register, 2026-07-16](https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446)). The NCA confirmed the impact scale — "a total of 148 systems became inoperable, including critical ones that required significant manual workarounds and delays" ([NCA, 2026-07-16](https://www.nationalcrimeagency.gov.uk/news/two-sentenced-for-hacking-transport-for-london-in-uk-s-biggest-ever-cyber-crime-case)) — and TfL later established that data on roughly 7 million users had been accessible, far beyond the ~5,000 initially believed ([The Register, 2026-07-16](https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446)). The CPS put the remediation cost at £29 million ([CPS, 2026-07-16](https://www.cps.gov.uk/national-news/news/cyberhackers-who-targeted-tfl-jailed-more-five-years-each)).

**Defender takeaway:** the compromise never touched a technical vulnerability — the single control point was the helpdesk's password/MFA-reset process, the recurring Scattered Spider signature. Defenders should treat helpdesk-initiated credential and MFA resets as a distinct, monitorable event class rather than an implicitly trusted administrative action: capture who requested the reset, what identity verification was performed, and how quickly a privileged or unusual action followed. **Triage:** a legitimate reset is tied to a verified requester and is not immediately followed by anomalous access; the discriminators are a reset requested for an account whose owner did not initiate it, repeated 2FA-reset attempts on one account, and a short interval between a helpdesk reset and first sign-in from a new device/location.
