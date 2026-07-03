---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "Law-enforcement infrastructure takedowns — Operation Saffron (Switzerland JIT), FIOD/Stark Industries, Kimwolf, INTERPOL Ramz"
headline: "Law-enforcement infrastructure takedowns — Operation Saffron (Switzerland JIT), FIOD/Stark Industries, Kimwolf, INTERPOL Ramz"
summary: "Four coordinated actions in the window degraded threat-actor infrastructure relevant to this audience. Operation Saffron dismantled First VPN — a Russian-language criminal anonymisation service marketed to ransomware operators — seizing 33+ servers with the user database captured; **Switzerland was a named Joint …"
discovered_at: "2026-05-18T05:00:38Z"
event_date: 2026-05-23
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - ransomware
  - ddos
regions:
  - europe
  - switzerland
  - global
sectors: []
entities:
  - "campaign:interpol-operation-ramz-mena-cybercrime-13-country-201-arre"
  - "incident:operation-saffron-first-vpn-takedown-33-servers-27-countri"
cves: []
sources:
  - url: "https://www.eurojust.europa.eu/news/eurojust-coordinated-investigation-shuts-down-criminal-vpn-network"
    publisher: Eurojust — First VPN takedown
    role: primary
  - url: "https://www.fiod.nl/fiod-houdt-twee-verdachten-aan-wegens-overtreding-sanctiewetgeving/"
    publisher: FIOD — Stark Industries arrests
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
migrated_from: briefs/weekly/2026-W21.md
---

Four coordinated actions in the window degraded threat-actor infrastructure relevant to this audience. **Operation Saffron** dismantled First VPN — a Russian-language criminal anonymisation service marketed to ransomware operators — seizing 33+ servers with the user database captured; **Switzerland was a named Joint Investigation Team participant**, and the infrastructure is linked to Phobos RaaS ([Eurojust](https://www.eurojust.europa.eu/news/eurojust-coordinated-investigation-shuts-down-criminal-vpn-network); [daily 2026-05-22](/briefs/2026-05-22/)). The **Netherlands FIOD** arrested two suspects for EU-sanctions evasion tied to the Stark Industries bulletproof-hosting front and seized ~800 servers, dismantling NoName057(16) DDoS plumbing ([FIOD](https://www.fiod.nl/fiod-houdt-twee-verdachten-aan-wegens-overtreding-sanctiewetgeving/); [daily 2026-05-23](/briefs/2026-05-23/)). The alleged operator of the **Kimwolf** 30+ Tbps IoT DDoS-for-hire botnet (AISURU variant) was arrested ([US DoJ](https://www.justice.gov/usao-ak/pr/canadian-man-arrested-international-authorities-charged-administrating-kimwolf-ddos); [daily 2026-05-23](/briefs/2026-05-23/)), and **INTERPOL Operation Ramz** logged 201 arrests across a 13-country MENA sweep including a PhaaS-server takedown ([INTERPOL](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region); [daily 2026-05-19](/briefs/2026-05-19/)). The defender-relevant pattern: the takedowns hit anonymisation/hosting/DDoS plumbing rather than end actors, so expect short-term infrastructure churn (new VPN/hosting fronts, rebuilt botnet C2) rather than a durable drop in activity.
