---
schema: 1
kind: threat
horizon: operational
title: "NCSC Switzerland warns of cyber operations around the G7 Évian summit (15–17 June)"
headline: "NCSC Switzerland warns of cyber operations around the G7 Évian summit (15–17 June)"
summary: "NCSC Switzerland issues a pre-event cyber advisory ahead of the G7 Évian summit (15–17 June) — the NCSC explicitly anticipates hacktivist DDoS against Swiss organisations (NCSC Switzerland, 2026-06-01); an independent threat map additionally flags state intelligence collection against hotel/telecom infrastructure and mobile-device targeting, echoing the NoName057(16) DDoS waves seen during Bürgenstock 2024 (ZENDATA, 2026-05-03). Most delegations transit Swiss infrastructure (Geneva–Vaud corridor)."
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
entities: []
cves: []
sources:
  - url: "https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/massnahmen-grossanlaesse-konferenzen-g7.html"
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
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-03.md
---

On 2026-06-01 Switzerland's National Cyber Security Centre published a pre-event advisory warning that the G7 summit in Évian (France, 15–17 June) is a high-value target and that it "expects disruptive maneuvers in cyberspace again" ([NCSC Switzerland, 2026-06-01](https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/massnahmen-grossanlaesse-konferenzen-g7.html)). Although the summit sits on French soil, most delegations transit Geneva Airport and lodge on the Swiss side (Geneva, Vaud, Valais), putting Swiss federal and cantonal administrations, conference-linked suppliers, and Swiss telecom operators in the blast radius. An independently published threat map for the event frames the expected activity against the template of the 2024 Bürgenstock summit, when the pro-Russia hacktivist collective NoName057(16) ran DDoS waves against Swiss federal sites and conference-linked organisations on each summit day; the same map additionally flags state intelligence collection against hotel and telecom infrastructure, rogue-base-station cellular interception, and social-engineering against event staff as plausible vectors ([ZENDATA Cybersecurity, 2026-05-03](https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/)). The NCSC advisory itself recommends generic protective measures and DDoS preparedness for organisations linked to the event.

**Why it matters to us:** Organisations operating in the Geneva–Vaud corridor and Swiss federal/cantonal SOCs should pre-stage DDoS mitigation playbooks now, review MFA on customer-facing identity providers, rotate administrative credentials before the event window, and brief travelling staff on mobile-device physical security; hunt for anomalous authentication spikes from the summit region and unexpected reattachment events in MDM/MDM-adjacent telemetry around 15–17 June.
