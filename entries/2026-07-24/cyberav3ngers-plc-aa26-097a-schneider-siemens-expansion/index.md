---
schema: 1
kind: threat
title: "US agencies expand the Iranian PLC-intrusion advisory (AA26-097A) to Schneider Electric and Siemens controllers, with new project-file tampering detection"
headline: "Iran-linked PLC intrusions now hit Schneider and Siemens gear — the fix is exposure and integrity checking, not a patch"
summary: >
  A seven-agency US update to joint advisory AA26-097A widens confirmed Iranian-affiliated exploitation of
  internet-exposed programmable logic controllers from Rockwell/Allen-Bradley to Schneider Electric and Siemens
  models, and adds guidance to detect unauthorised changes to PLC project files and Add-On Instructions. The
  actors reach controllers through direct internet exposure and vendor engineering software, not a software CVE.
discovered_at: "2026-07-24T04:36:09Z"
event_date: "2026-07-22"
run_id: 2026-07-24T0409Z-intel
priority: notable
immediate_action: null
tags: [nation-state, ot-ics, actively-exploited]
regions: [us, europe, global]
sectors: [energy, water, public-sector]
entities: [actor:cyberav3ngers]
techniques: [T1595, T1078, T1565]
affected_products: ["Rockwell Automation CompactLogix", "Rockwell Automation Micro850", "Schneider Electric Modicon M340", "Siemens S7-1200"]
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a"
    publisher: "CISA / FBI / NSA / EPA / DoE / USCYBERCOM / Treasury (joint advisory AA26-097A, updated)"
    date: "2026-07-22"
    role: primary
  - url: "https://www.cisa.gov/news-events/news/cisa-fbi-epa-and-us-government-partners-update-warning-iran-affiliated-threat-actors-targeting"
    publisher: "CISA News"
    date: "2026-07-22"
    role: corroborating
  - url: "https://www.trendmicro.com/en_us/research/26/g/plc-exploitation.html"
    publisher: "Trend Micro Research"
    date: "2026-07-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Iranian-affiliated activity outlined in this advisory has disrupted PLCs across several U.S. critical infrastructure sectors by attempting to download malicious project files and manipulate data on human machine interface (HMI) and supervisory control and data acquisition (SCADA) displays, resulting in operational disruption and financial loss for affected organizations."
    publisher: "CISA News"
  - quote: "Review project files running on PLCs for unauthorized changes. Use vendor-provided integrity checking tools and visually compare the running program to known good logic."
    publisher: "CISA / FBI / NSA / EPA / DoE / USCYBERCOM / Treasury (joint advisory AA26-097A, updated)"
verification: multi-source
sourcing_note: "The advisory (AA26-097A) is a US-jurisdiction warning with no stated European victims; included for the transferable TTP and vendor-agnostic detection value to Swiss/EU energy and water operators running the same Schneider Electric and Siemens controller families."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Baseline the running logic and Add-On Instructions on any internet-reachable Rockwell, Schneider Modicon M340 or Siemens S7-1200 PLC against a known-good copy, and alert on unauthorised changes — the actors disable shutdown/alarm interlocks so HMI displays mask unsafe states."
migrated_from: null
---

Seven US federal agencies (CISA, FBI, NSA, EPA, the Department of Energy, US Cyber Command's Cyber National Mission Force and the Treasury) updated joint advisory **AA26-097A** on 22 July 2026 — first published in April 2026 on Iranian-affiliated exploitation of internet-connected, misconfigured programmable logic controllers ([CISA, 2026-07-22](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)). The update's substance is a widened scope and new detection guidance: targeting previously centred on Rockwell Automation/Allen-Bradley CompactLogix and Micro850 controllers is now confirmed to include Schneider Electric Modicon M340 and Siemens S7-1200 series controllers — both with large installed bases across European water and energy utilities ([CISA News, 2026-07-22](https://www.cisa.gov/news-events/news/cisa-fbi-epa-and-us-government-partners-update-warning-iran-affiliated-threat-actors-targeting)). There is no underlying software CVE: the actors scan common ICS ports (44818/2222 EtherNet/IP, 102 Siemens S7comm, 502 Modbus TCP, and 22 for Dropbear SSH on victim modems), then connect using the manufacturers' own engineering software (Rockwell Studio 5000, Schneider EcoStruxure Control Expert, Siemens TIA Portal) run from leased infrastructure with credentials obtained from weakly-protected devices, and pull down device project files ([Trend Micro, 2026-07-23](https://www.trendmicro.com/en_us/research/26/g/plc-exploitation.html)). The current campaign manipulates control logic directly and has produced confirmed operational disruption and financial loss: the actors modify or delete PLC logic — including reusable Add-On Instructions — and manipulate HMI/SCADA display data to disable shutdown and alarm logic, letting systems enter unsafe states without operator notification ([CISA News, 2026-07-22](https://www.cisa.gov/news-events/news/cisa-fbi-epa-and-us-government-partners-update-warning-iran-affiliated-threat-actors-targeting)).

**Defender takeaway:** The exposure pattern — an internet-reachable PLC management interface plus the vendor's engineering software plus weak or default credentials — is directly transferable to Swiss and European energy and water operators running the same Schneider and Siemens controller families, regardless of the advisory's US framing. Priorities from the advisory, in order: remove PLCs from direct internet exposure and route any remote access through an MFA-gated gateway; set mode switches to RUN and restrict PROGRAM/REMOTE to supervised maintenance windows; enable vendor programming-protection key-switch features (Rockwell SD1771, Siemens TIA Portal access protection); and keep offline, tested backups of PLC logic. **Triage:** the highest-value detection is integrity-based rather than network-based — baseline the running program and AOIs and alert on any deviation from known-good logic, since the malicious changes are made through legitimate engineering software over legitimate protocols and will not surface as exploit traffic; corroborate with inbound connections to OT ports 44818/2222/102/502/22 from unexpected, leased or third-party-hosted source ranges.
