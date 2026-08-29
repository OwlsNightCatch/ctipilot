---
schema: 1
kind: vulnerability
title: "MZ Automation libIEC61850: unauthenticated heap-overflow RCE via crafted MMS Initiate (CVE-2026-49035) plus four sibling OT-library flaws"
headline: "A pre-auth RCE in the widely-embedded libIEC61850 substation library — energy and water OEMs, not a single product, are affected"
summary: >
  CISA advisories ICSA-26-204-06/-07 disclose five flaws in MZ Automation's open-source libIEC61850 and lib60870
  protocol libraries, embedded in IEC 61850 / IEC 60870-5-104 substation-automation and SCADA telecontrol gear.
  The most severe, CVE-2026-49035, is an unauthenticated heap-based buffer overflow reachable via a crafted MMS
  Initiate request, with RCE demonstrated where ASLR is disabled. No public exploitation is reported.
discovered_at: "2026-07-24T04:36:09Z"
event_date: "2026-07-23"
run_id: 2026-07-24T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, ot-ics, rce, pre-auth]
regions: [global, europe]
sectors: [energy, water, manufacturing]
entities: []
techniques: [T1190]
affected_products: ["MZ Automation libIEC61850", "MZ Automation lib60870"]
cves:
  - id: CVE-2026-49035
    cvss: "8.1 (CVSS 3.1) / 9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "libIEC61850 1.0.0 – 1.6.1"
    fixed: "not stated in advisory"
  - id: CVE-2026-50039
    cvss: "7.5 (CVSS 3.1) / 8.7 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "libIEC61850 1.0.0 – 1.6.1"
    fixed: "not stated in advisory"
  - id: CVE-2026-50032
    cvss: "7.5 (CVSS 3.1) / 8.7 (CVSS 4.0)"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "libIEC61850 1.0.0 – 1.6.1"
    fixed: "not stated in advisory"
  - id: CVE-2026-50103
    cvss: "6.5 (CVSS 3.1) / 7.1 (CVSS 4.0)"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "libIEC61850 1.0.0 – 1.6.1"
    fixed: "not stated in advisory"
  - id: CVE-2026-16002
    cvss: "8.2 (CVSS 3.1) / 8.8 (CVSS 4.0)"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "lib60870 ≤ 2.4.0"
    fixed: "not stated in advisory"
sources:
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-06"
    publisher: "CISA (ICSA-26-204-06)"
    date: "2026-07-23"
    role: primary
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-07"
    publisher: "CISA (ICSA-26-204-07)"
    date: "2026-07-23"
    role: primary
closed_sources: []
evidence:
  - quote: "The affected product is vulnerable to a heap-based buffer overflow via a crafted MMS Initiate request. Remote code execution (RCE) has been demonstrated when ASLR is disabled; memory corruption or denial of service may occur in configurations where ASLR is enabled."
    publisher: "CISA (ICSA-26-204-06)"
  - quote: "No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time."
    publisher: "CISA (ICSA-26-204-06)"
verification: single-source-national-cert
sourcing_note: "Single-source national-CERT carve-out (CISA ICS-CERT is the sole authority for these advisories). Neither advisory page, as retrieved, states a fixed version number — the fix status shown is 'patch-available' per the advisory's remediation section, but operators must confirm the specific fixed release with MZ Automation and the linked CSAF JSON before assuming availability."
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
actions: []
migrated_from: null
---

CISA advisory **ICSA-26-204-06** (2026-07-23) discloses four vulnerabilities in MZ Automation's open-source **libIEC61850** (versions 1.0.0 through 1.6.1), a C library implementing the IEC 61850 MMS/GOOSE substation-automation protocols and embedded as an OEM component in energy-sector protection, control and monitoring equipment worldwide ([CISA, 2026-07-23](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-06)). The most severe, **CVE-2026-49035** (CWE-122 heap-based buffer overflow, CVSS 3.1 8.1 / CVSS 4.0 9.2), is triggered by a crafted MMS Initiate request with no authentication and no user interaction; CISA states remote code execution has been demonstrated where ASLR is disabled, degrading to memory corruption or denial of service where it is enabled ([CISA, 2026-07-23](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-06)). The three companion flaws are a stack overflow via a crafted ReadRequest (CVE-2026-50039), and two null-pointer-dereference DoS conditions — one in the shared L2 GOOSE/R-GOOSE parser via a malformed TLV (CVE-2026-50103), one in the MMS Write Named Variable List handler via a WriteRequest with an empty `listOfData` field (CVE-2026-50032). A companion advisory, **ICSA-26-204-07**, covers the sibling **lib60870** library (versions ≤ 2.4.0, implementing IEC 60870-5-104 SCADA telecontrol used in chemical, energy and water/wastewater sectors) with an out-of-bounds-read parser-crash DoS, CVE-2026-16002 ([CISA, 2026-07-23](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-07)). CISA reports no known public exploitation of any of the five.

**Defender takeaway:** The risk here is embedded-supply-chain, not a single product to patch: libIEC61850 and lib60870 are linked into protection relays, RTUs, gateways and substation controllers from many vendors, so a package-manager version check will miss them. Swiss and European electricity-transmission, distribution and water operators should ask their substation-automation and telecontrol OEMs which firmware embeds these libraries and at what version, and prioritise the pre-auth RCE (CVE-2026-49035) on any device whose IEC 61850 MMS interface (TCP 102) is reachable beyond a tightly segmented process network. Because no fixed version is stated in the advisory text as retrieved, confirm remediation status directly with MZ Automation and via the advisory's CSAF JSON before assuming a fix exists. Standard OT segmentation applies with elevated weight given the unauthenticated, network-reachable profile: keep MMS/IEC 60870 endpoints off any business or internet-reachable path, and prefer up-to-date VPN-fronted access over direct exposure for any required remote engineering.
