---
schema: 1
kind: incident
title: >
  A dark-web identity-theft storefront sells 153 million+ driver's-license scans traced to
  identity-verification vendor IDScan.net; FBI opens a formal investigation
headline: >
  Victim-timestamp correlation, not vendor detection, exposed a year-long exfiltration from an
  ID-verification vendor used at 20,000+ locations worldwide
summary: >
  A dark-web identity-theft service called Nexus appeared around 2026-08-31 advertising 153
  million+ U.S. and Canadian driver's-license scans, traced by independent verification to
  identity-verification vendor IDScan.net. Krebs on Security confirmed the link by matching
  volunteers' own license-scan timestamps to physical document-presentation events at kiosks
  using IDScan.net's technology; the FBI's New Orleans field office opened a formal investigation
  on 2026-09-01, independently confirmed to Reuters and BleepingComputer, and class-action
  investigations followed. No access vector into IDScan.net's own systems has been confirmed
  publicly.
discovered_at: "2026-09-06T04:50:00Z"
updated_at: null
event_date: "2026-08-31"
run_id: 2026-09-06T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, identity]
regions: [us]
sectors: []
entities: ["incident:idscan-net-nexus-driver-license-breach-2026-09"]
techniques: [T1213]
affected_products: ["IDScan.net identity-verification / document-scanning platform"]
cves: []
sources:
  - url: "https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/"
    publisher: "Krebs on Security"
    date: "2026-09-01"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/"
    publisher: "BleepingComputer"
    date: "2026-09-04"
    role: corroborating
  - url: "https://www.securityweek.com/153-million-driver-license-images-offered-on-dark-web/"
    publisher: "SecurityWeek"
    date: "2026-09-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have been continuously exfiltrating new data for over a year into our private database"
    publisher: "Nexus service operator, quoted by Krebs on Security"
    source_url: "https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/"
  - quote: "the technology scans IDs with both infrared and ultraviolet light. Idscan.net says the company’s systems and technology perform more than 21 million verifications monthly, at more than 20,000 locations around the world."
    publisher: "Krebs on Security, citing idscan.net's own documentation"
    source_url: "https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/"
  - quote: "Earlier this afternoon, I was added to a conference call with a half-dozen FBI agents, including senior leaders from the agency’s cyber division. During that call, the FBI shared that earlier today their New Orleans field office opened an official investigation into an apparent breach involving idscan.net."
    publisher: "Krebs on Security"
    source_url: "https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/"
  - quote: "A threat actor this week started offering on the dark web digital scans of over 153 million US and Canadian driver’s licenses."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/153-million-driver-license-images-offered-on-dark-web/"
verification: multi-source
sourcing_note: >
  Krebs on Security is the discovering and verifying primary (victim-side timestamp correlation
  against the operator's own claims); SecurityWeek and BleepingComputer independently confirm the
  FBI investigation and add the class-action and vendor-notification developments. No IDScan.net
  vendor statement, research-lab post or regulator filing was reachable as a direct citable
  source as of this writing (IDScan.net's own acknowledgement is relayed only through Krebs's
  reporting) — included with reduced confidence: only aggregator/press sources available despite
  a fair attempt to reach a vendor primary. No access vector into IDScan.net's own systems has
  been publicly confirmed by any party.
confidence: medium
references: []
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

A dark-web identity-theft storefront called Nexus appeared on the Russian cybercrime forum Exploit around 2026-08-31, advertising searchable access to more than 153 million U.S. and Canadian driver's-license scans, 10 million ID cards, 3 million travel documents and 579,000 medical cards; Krebs on Security observed the driver's-license count grow by nearly 400,000 records over the 24 hours before publication ([Krebs on Security, 2026-09-01](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/)). Krebs on Security verified the data against volunteers' own licenses: each record carries six image files — front and back, plain, infrared and ultraviolet scans — with an embedded capture timestamp; of more than a dozen volunteers whose licenses were checked, nine were found in the database, and each of those nine had a timestamp matching a point where they had physically handed a license to a clerk operating a document-scanning terminal, at a car-rental counter or a cannabis dispensary among the observed examples. That scanning technology traces to IDScan.net, a Louisiana-based identity-verification vendor whose own documentation states its systems perform more than 21 million verifications a month at more than 20,000 locations worldwide ([Krebs on Security, 2026-09-01](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/)); the Nexus operators themselves claimed to have been continuously exfiltrating new data for over a year. IDScan.net has acknowledged it is investigating the matter but had issued no public statement naming a root cause as of this writing.

The FBI's New Orleans field office opened a formal investigation on 2026-09-01, confirmed directly to Krebs by FBI cyber-division leadership on a briefing call ([Krebs on Security, 2026-09-01](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/)) and independently to Reuters ([BleepingComputer, 2026-09-04](https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/)); the Nexus service went offline within hours of Krebs's story publishing ([Krebs on Security, 2026-09-01](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/)), though the underlying dataset remains in criminal hands ([BleepingComputer, 2026-09-04](https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/)). By 2026-09-04, multiple U.S. law firms had opened class-action investigations, and IDScan reportedly began notifying some business customers around 2026-09-01 ([BleepingComputer, 2026-09-04](https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/)).

This is a vendor-concentration and data-retention failure, not a classic network intrusion narrative: IDScan.net retained multi-year, multi-modal document scans captured at thousands of downstream client locations, and the exposure surfaced through independent victim-side timestamp correlation, not vendor detection — by the operators' own account, exfiltration had run undetected for over a year. No access vector into IDScan.net's own systems has been confirmed publicly by any party.

**Defender takeaway:** any organization, including a government agency, that outsources physical identity-document verification or kiosk scanning to a third party should ask that vendor three questions this incident makes concrete: how long raw document images are retained after the verification transaction completes; whether infrared/ultraviolet biometric scan data is retained beyond that transaction; and what the vendor's own breach-detection capability actually is, given this vendor apparently ran undetected exfiltration for over a year. The transferable risk is concentration — a single verification vendor holding scans from thousands of unrelated physical locations is a single point of failure for all of them at once.
