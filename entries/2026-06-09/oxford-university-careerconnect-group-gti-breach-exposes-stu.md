---
schema: 1
kind: incident
horizon: operational
title: Oxford University CareerConnect (Group GTI) breach exposes students at multiple UK universities
headline: Oxford University CareerConnect (Group GTI) breach exposes students at multiple UK universities
summary: "The University of Oxford disclosed a breach after Group GTI, the third-party provider of the CareerConnect career-services platform, reported its systems were compromised on 28 May 2026 (BleepingComputer, 2026-06-08; Oxford Careers Service, 2026-06-01)."
discovered_at: "2026-06-09T05:00:00Z"
event_date: 2026-06-08
run_id: 2026-06-09-40d562df
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - phishing
regions:
  - uk
  - europe
sectors:
  - education
entities: []
cves: []
sources:
  - url: "https://www.careers.ox.ac.uk/article/careerconnect-secured-and-safe-to-use-following-data-security-incident"
    publisher: Oxford Careers Service statement
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/oxford-university-discloses-data-breach-after-careerconnect-platform-hack/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.theregister.com/security/2026/06/06/oxford-university-data-pwned-again-by-career-platform-breach/5251754"
    publisher: The Register
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
migrated_from: briefs/2026-06-09.md
---

The University of Oxford disclosed a breach after Group GTI, the third-party provider of the CareerConnect career-services platform, reported its systems were compromised on 28 May 2026 ([BleepingComputer, 2026-06-08](https://www.bleepingcomputer.com/news/security/oxford-university-discloses-data-breach-after-careerconnect-platform-hack/); [Oxford Careers Service, 2026-06-01](https://www.careers.ox.ac.uk/article/careerconnect-secured-and-safe-to-use-following-data-security-incident)). Exposed data includes student first names, last names and email addresses; for users who do not authenticate via institutional Single Sign-On, encrypted passwords were also taken. CareerConnect is used by Oxford, King's College London and the University of Manchester among others, so the breach spans multiple UK higher-education institutions ([BleepingComputer, 2026-06-08](https://www.bleepingcomputer.com/news/security/oxford-university-discloses-data-breach-after-careerconnect-platform-hack/)); The Register notes further unnamed UK and overseas institutions are affected ([The Register, 2026-06-06](https://www.theregister.com/security/2026/06/06/oxford-university-data-pwned-again-by-career-platform-breach/5251754)). GTI assessed the intrusion as credential-harvest oriented, raising the likelihood of follow-on phishing against institutional email addresses.

**Defender takeaway:** SSO adoption directly limited blast radius here — SSO users' passwords stayed with the identity provider, leaving only names and emails exposed. The case reinforces segregation of authentication credentials away from in-app stores and treating shared SaaS career/HR platforms as part of the institutional attack surface. Swiss *Hochschulen* using shared SaaS career portals should expect targeted phishing waves against the harvested address sets.
