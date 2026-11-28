---
schema: 1
kind: incident
title: "Kudelski Security: a one-night intrusion at a European insurer, assessed as run by an offensive AI framework, abused customer onboarding, identity migration and a retired API to create accounts in customers' names and extract more than 100 documents, with no malware"
headline: "Kudelski: assessed AI-driven insurer intrusion via onboarding and identity logic, no malware; alert on request bursts"
summary: >
  Kudelski Security's incident responders describe a one-night intrusion at an unnamed European insurer in which about three million identification requests in under nine hours identified about 30 customers, more than a dozen accounts were created in customers' names without their passwords and more than 100 documents were extracted, with no malware and no compromise of the portal's servers. Kudelski assesses with high confidence that an offensive AI framework was used, names none and publishes no indicators, and traces the chain to business-logic weaknesses: the API of a retired web interface that stayed accessible, CAPTCHA and rate limits that were not enforced or were inactive after a migration, registration paths that did not consistently enforce prior identity checks, unverified contact data that inherited verified status, incomplete token validation and an identity-provider flaw in authenticator enrollment.
discovered_at: "2026-11-28T05:03:00Z"
updated_at: null
event_date: "2026-11-27"
run_id: 2026-11-28T0355Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, identity, data-breach]
regions: [europe]
sectors: [finance]
entities: ["incident:kudelski-european-insurer-offensive-ai-intrusion-2026-11"]
techniques: [T1190, T1136, T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface"
    publisher: "Kudelski Security"
    date: "2026-11-27"
    role: primary
  - url: "https://github.com/zitadel/zitadel/security/advisories/GHSA-qqv8-37gw-ww2q"
    publisher: "ZITADEL security advisory (GHSA-qqv8-37gw-ww2q)"
    date: "2026-11-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Kudelski Security assesses with high confidence that an offensive AI framework was leveraged during this intrusion."
    publisher: "Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface"
  - quote: "No malware was identified, and no compromise of the servers hosting the individual customer portal was observed."
    publisher: "Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface"
  - quote: "The identity of the specific framework and its associated indicators are not disclosed in this publication."
    publisher: "Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface"
  - quote: "The observed attack had generated multiple detectable signals well before the data collection phase."
    publisher: "Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface"
  - quote: "The absence of malware should never be interpreted as evidence that no compromise occurred."
    publisher: "Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface"
verification: single-source
sourcing_note: >
  Kudelski Security's incident-response team is the only source and describes a case it investigated; the post gives no date, country, victim name or identity-provider product, and says the framework and its indicators are not disclosed and that the degree of human supervision could not be established, so the AI attribution is Kudelski's assessment. The post cites advisory GHSA-qqv8-37gw-ww2q without naming the product; that id is ZITADEL's advisory, but nothing in the post says the insurer ran ZITADEL. The post gives no ordered attack chain, only the weaknesses it found.
confidence: medium
references:
  - 2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Kudelski Security's incident-response team describes a one-night intrusion at an unnamed European insurer in which about three million identification requests arrived in under nine hours, about 30 legitimate customer identities were identified, more than a dozen customer accounts were created in those customers' names without their passwords, and more than 100 documents with sensitive customer data were extracted ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)). Kudelski found no malware and no compromise of the servers hosting the customer portal, and each forged account could read only its own customer's data ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)). It assesses with high confidence that an offensive AI framework was used, from correlated indicators of compromise, infrastructure characteristics, previously documented attack patterns, machine-speed execution, application-specific reconnaissance and automated handling of complex identity workflows, names no framework and could not establish how much human supervision there was ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)).

Among the weaknesses it lists, mostly business logic rather than software bugs: the API of a retired web interface remained accessible, identity information could be tested at scale, CAPTCHA was not enforced by the underlying API, rate limits were inactive after an infrastructure migration, alternative registration processes that did not consistently enforce prior identity checks, unverified contact information inherited a verified status, token validation was incomplete, authorization-related information was exposed to the client, and an identity-provider vulnerability weakened authenticator enrollment ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)). The identity-provider flaw is cited as GHSA-qqv8-37gw-ww2q, which is ZITADEL's advisory for a missing second-factor check on authenticator enrollment in its Login V2 interface, affecting 4.0.0 through 4.20.4 and fixed in 4.20.5; the post does not say the insurer ran ZITADEL ([ZITADEL, 2026-11-18](https://github.com/zitadel/zitadel/security/advisories/GHSA-qqv8-37gw-ww2q)). Kudelski compares the case with BabidiGhost: that operation tried an AI agent against many organizations, this one explored a single organization's interconnected application and identity ecosystem in depth ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)).

**Exposure:** a customer or citizen portal that runs identity onboarding, identity migration or account recovery; the case came from an insurer, and the post names no public-sector victim.

**Detection:** application and identity telemetry carried the evidence, not endpoint telemetry: Kudelski says abnormal application request volumes, extensive authentication failures and suspicious reconnaissance appeared well before data collection began and the attack still ran through the night ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)). Its recommended detections include distributed requests against one business function across rotating infrastructure, excessive one-time-code failures, authenticator enrollment without completed MFA, activity against retired APIs, source-map access by automated clients and abnormal onboarding and recovery sequences ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)). The sequence to alert on is a burst of identification requests, then accounts created in the names of existing customers without their original passwords, then sensitive information accessed by those accounts.

**Triage:** a newly created account may satisfy the portal's registration requirements, so a single account can look legitimate; Kudelski says abnormal request volumes, extensive authentication failures and reconnaissance activity were detectable well before data collection ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)).

**Defender takeaway:** for any portal with identity lifecycle workflows, Kudelski's hardening list is the checklist: user-supplied contact attributes must not inherit verified status, identity migrations must preserve existing account activation states, retiring a front end includes decommissioning its supporting APIs, and rate limiting, CAPTCHA and server-side validation must be tested again after each change ([Kudelski Security, 2026-11-27](https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface)); alert on identification-request bursts, and move a ZITADEL deployment on 4.0.0 through 4.20.4 to 4.20.5 ([ZITADEL, 2026-11-18](https://github.com/zitadel/zitadel/security/advisories/GHSA-qqv8-37gw-ww2q)).
