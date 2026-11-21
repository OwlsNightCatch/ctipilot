---
schema: 1
kind: threat
title: "NCSC Switzerland warns of cyber operations around the G7 Évian summit (15–17 June)"
headline: "NCSC Switzerland warns of cyber operations around the G7 Évian summit (15–17 June)"
summary: "NCSC Switzerland issued a pre-event cyber advisory ahead of the G7 Évian summit, scheduled for 15–17 June: the NCSC explicitly anticipated hacktivist DDoS against Swiss organisations (NCSC Switzerland, 2026-06-01). An independent threat map additionally flags state intelligence collection against hotel/telecom infrastructure and mobile-device targeting, echoing the NoName057(16) DDoS waves seen during Bürgenstock 2024 (ZENDATA, 2026-05-03). Most delegations transit Swiss infrastructure (Geneva–Vaud corridor)."
discovered_at: "2026-06-03T05:00:00Z"
event_date: 2026-06-01
run_id: 2026-06-03-ee0eae61
priority: routine
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
  - url: "https://www.bacs.admin.ch/dam/en/sd-web/-wzJ1QS9mdil/massnahmen-grossanlaesse_internat-veranstaltungen-en.pdf"
    publisher: NCSC Switzerland
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
  - at: "2026-10-11T14:02:54Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      Relabels the closing line as the Defender takeaway. The G7 summit the warning concerned was scheduled for 15 to 17 June 2026, so the summary and takeaway now read as a record of the warning and its lasting lesson, and the priority moves from high to routine. The takeaway attributes NCSC's baseline measures to its own measures document and the event-specific steps to ZENDATA.
    fields: [body, priority, summary, sources]
  - at: "2026-10-21T08:21:06Z"
    run_id: 2026-10-21T0800Z-audit
    type: improvement
    summary: >
      The analysis gains its Exposure and Detection lines: NCSC expected the DDoS attacks to target Swiss
      organisations' websites and online services and rated event participants and their organisations as
      likely targets, and ZENDATA gives the speed of network-layer attacks and a post-event hunt. The
      analyst-judgement scope moves into the Exposure line unchanged.
    fields: [body]
migrated_from: briefs/2026-06-03.md
---

On 2026-06-01 Switzerland's National Cyber Security Centre published a pre-event advisory warning that large events and international conferences are "often used as an opportunity to stage a cyberattack" and that it "expects disruptive maneuvers in cyberspace again" around the G7 summit in Évian (France, 15–17 June) ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)). Although the summit sits on French soil, most delegations land at Geneva airport and stay on the Swiss side ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). An independently published threat map for the event frames the expected activity against the template of the 2024 Bürgenstock summit, when the pro-Russia hacktivist collective NoName057(16) ran DDoS waves against Swiss federal sites and conference-linked organisations on each summit day; the same map additionally flags state intelligence collection against hotel and telecom infrastructure, rogue-base-station cellular interception, and social engineering of hotel help desks as plausible vectors ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). The NCSC advisory itself recommends generic protective measures and DDoS preparedness for organisations linked to the event.

**Exposure:** the websites and online services of Swiss organisations, which the DDoS attacks NCSC anticipated during the summit were expected to target, and the participants of such events and their organisations, which NCSC rates as likely targets ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)). In analyst judgement that put Swiss federal and cantonal administrations, conference-linked suppliers and Swiss telecom operators in the blast radius; ZENDATA adds that state services target the providers around a summit, such as hotels, transport and telecom operators, and asks organisations around Lake Geneva whether they sit in a target's supply chain ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)).

**Detection:** inbound traffic volume and the availability of websites and online services, which a DDoS floods until they are partially or completely inaccessible ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)); ZENDATA notes that most network-layer attacks now end in under ten minutes, faster than any human can authorise mitigation ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). After an event, ZENDATA's hunt looks for in-memory implants, suspicious driver signatures, anomalous OAuth grants, persistence in supplier networks and login-page anomalies on exposed platforms ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)).

**Defender takeaway:** the warning's lasting lesson is NCSC's baseline for organisations around large international events, which it recommends regardless of the current threat situation: a second factor or passkey on every remote-access channel, prompt patching, offline backups, an anti-DDoS solution for essential web services, EDR or XDR on clients and servers, and restricted access to exposed systems ([NCSC Switzerland, measures for major events](https://www.bacs.admin.ch/dam/en/sd-web/-wzJ1QS9mdil/massnahmen-grossanlaesse_internat-veranstaltungen-en.pdf)). ZENDATA's map adds event-specific steps, such as rotating administrative credentials before and after the event and reviewing MFA on customer-facing identity providers ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)).

## Correction — 2026-09-30T06:43:01Z

ZENDATA's risk map for the summit names social engineering of hotel help desks among the plausible vectors, not social engineering of event staff, and the analysis now says so ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). The observation that most delegations arrive through Geneva and stay on the Swiss side comes from the same map and now cites it. NCSC Switzerland's advisory warns that large events and conferences are "often used as an opportunity to stage a cyberattack", not that the summit is a high-value target, and the analysis now quotes it. Neither source says that the Swiss administrations, suppliers and telecom operators the analysis places in the blast radius will be targeted at Évian, so that exposure is now marked as analyst judgement. The advisory is cited at its new address on bacs.admin.ch ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)).

## Correction — 2026-10-11T14:02:54Z

The G7 summit in Évian was scheduled for 15 to 17 June 2026 ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)), so the warning's event window has passed; the entry stays as a record of the warning, at routine priority instead of high. The summary records the warning in the past tense, and the takeaway separates NCSC's baseline measures, which it recommends regardless of the current threat situation ([NCSC Switzerland, measures for major events](https://www.bacs.admin.ch/dam/en/sd-web/-wzJ1QS9mdil/massnahmen-grossanlaesse_internat-veranstaltungen-en.pdf)), from the event-specific steps in ZENDATA's map ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)).

## Improvement — 2026-10-21T08:21:06Z

NCSC expected the DDoS attacks around the summit to target the websites and online services of Swiss organisations, and it rated the participants of such events and their organisations as likely targets ([NCSC Switzerland, 2026-06-01](https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en)). ZENDATA notes that most network-layer attacks now end in under ten minutes, faster than any human can authorise mitigation, and its post-event hunt looks for in-memory implants, suspicious driver signatures, anomalous OAuth grants, persistence in supplier networks and login-page anomalies on exposed platforms ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)).
