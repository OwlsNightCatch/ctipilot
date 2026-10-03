---
schema: 1
kind: threat
title: "NCSC Switzerland warns of cyber operations around the G7 Évian summit (15–17 June)"
headline: "NCSC Switzerland warns of cyber operations around the G7 Évian summit (15–17 June)"
summary: "NCSC Switzerland issues a pre-event cyber advisory ahead of the G7 Évian summit (15–17 June): the NCSC explicitly anticipates hacktivist DDoS against Swiss organisations (NCSC Switzerland, 2026-06-01). An independent threat map additionally flags state intelligence collection against hotel/telecom infrastructure and mobile-device targeting, echoing the NoName057(16) DDoS waves seen during Bürgenstock 2024 (ZENDATA, 2026-05-03). Most delegations transit Swiss infrastructure (Geneva–Vaud corridor)."
discovered_at: "2026-06-03T05:00:00Z"
event_date: 2026-06-01
run_id: 2026-06-03-ee0eae61
priority: high
immediate_action: null
tags:
  - hacktivism
  - ddos
  - espionage
  - nation-state
  - russia-nexus
regions:
  - switzerland
  - europe
sectors:
  - public-sector
  - telco
  - transport
entities: ["report:g7-evian-2026"]
techniques: [T1498]
cves: []
sources:
  - url: "https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en"
    publisher: NCSC Switzerland
    role: primary
  - url: "https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/"
    publisher: ZENDATA Cybersecurity
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
classification:
  reliability: A
  credibility: 3
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:43:01Z"
    run_id: 2026-09-30T0634Z-audit
    type: correction
    summary: >
      ZENDATA's risk map names social engineering of hotel help desks, not of event staff, and is the
      source of the Geneva arrivals claim, so the analysis now says so and cites it. NCSC warns that
      such events are often used for cyberattacks rather than calling the summit a high-value target,
      and the analysis now quotes it and marks the exposure of Swiss administrations and suppliers
      as analyst judgement. The NCSC citation follows the page to its new address on bacs.admin.ch.
    fields: [sources, techniques, classification, summary, entities, body]
migrated_from: briefs/2026-06-03.md
---

On 2026-06-01 Switzerland's National Cyber Security Centre published a pre-event advisory warning that large events and international conferences are "often used as an opportunity to stage a cyberattack" and that it "expects disruptive maneuvers in cyberspace again" around the G7 summit in Évian (France, 15–17 June) ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)). Although the summit sits on French soil, most delegations land at Geneva airport and stay on the Swiss side ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). In analyst judgement that puts Swiss federal and cantonal administrations, conference-linked suppliers and Swiss telecom operators in the blast radius. An independently published threat map for the event frames the expected activity against the template of the 2024 Bürgenstock summit, when the pro-Russia hacktivist collective NoName057(16) ran DDoS waves against Swiss federal sites and conference-linked organisations on each summit day; the same map additionally flags state intelligence collection against hotel and telecom infrastructure, rogue-base-station cellular interception, and social engineering of hotel help desks as plausible vectors ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). The NCSC advisory itself recommends generic protective measures and DDoS preparedness for organisations linked to the event.

**Why it matters to us:** Organisations operating in the Geneva–Vaud corridor and Swiss federal/cantonal SOCs should pre-stage DDoS mitigation playbooks now, review MFA on customer-facing identity providers, rotate administrative credentials before the event window, and brief travelling staff on mobile-device physical security. By inference, hunt for anomalous authentication spikes from the summit region around 15–17 June.

## Correction — 2026-09-30T06:43:01Z

ZENDATA's risk map for the summit names social engineering of hotel help desks among the plausible vectors, not social engineering of event staff, and the analysis now says so ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). The observation that most delegations arrive through Geneva and stay on the Swiss side comes from the same map and now cites it. NCSC Switzerland's advisory warns that large events and conferences are "often used as an opportunity to stage a cyberattack", not that the summit is a high-value target, and the analysis now quotes it. Neither source says that the Swiss administrations, suppliers and telecom operators the analysis places in the blast radius will be targeted at Évian, so that exposure is now marked as analyst judgement. The advisory is cited at its new address on bacs.admin.ch ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)).
