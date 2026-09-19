---
schema: 1
kind: vulnerability
title: "CISA ICS batch (14 Jul): Rockwell 1715-AENTR unauthenticated debug-port takeover (CVE-2026-10577, CVSS 10.0, fixed in firmware 3.011) and a Swiss-vendor ABB T-MAC Plus auth chain (CVSS 9.9)"
headline: "CISA republishes four Rockwell/ABB OT advisories led by a CVSS 10.0 debug-port takeover on an energy/water EtherNet/IP adapter, fixed in firmware 3.011"
summary: >
  CISA published four ICS advisories on 2026-07-14 landing on the energy, water and critical-manufacturing
  sectors and on Swiss-headquartered ABB. The headline is CVE-2026-10577 in the Rockwell Automation
  1715-AENTR EtherNet/IP Adapter (all versions ≤ 3.003, CVSS 10.0): a network-reachable debug port with no
  authentication lets an unauthenticated attacker read/delete files, stop tasks, modify memory and change
  I/O states — Rockwell fixes it in firmware 3.011, with network isolation as the interim control. ABB T-MAC Plus
  4.0-24 (a fuel/chemical terminal-management system, fixed in 4.0-25) is subject to a four-CVE chain led by
  CVE-2025-14771 (CVSS 9.9, authenticated file disclosure); ABB also shipped a fix in Ability Edgenius for the
  previously-disclosed "Copy Fail" kernel flaw (CVE-2026-31431). No in-the-wild exploitation is reported for
  the newly-disclosed items.
discovered_at: "2026-07-15T04:36:00Z"
event_date: "2026-07-14"
run_id: 2026-07-15T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, ot-ics, auth-bypass, patch-available, info-disclosure, priv-esc]
regions: [global]
sectors: [energy, water, manufacturing]
entities: []
techniques: [T1190, T1068]
affected_products: ["Rockwell Automation 1715-AENTR EtherNet/IP Adapter", "ABB T-MAC Plus", "ABB Ability Edgenius", "ABB 800xA for Advant Master"]
cves:
  - id: CVE-2026-10577
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Rockwell Automation 1715-AENTR EtherNet/IP Adapter ≤ 3.003"
    fixed: "3.011"
  - id: CVE-2025-14771
    cvss: "9.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "ABB T-MAC Plus 4.0-24"
    fixed: "4.0-25"
  - id: CVE-2025-14772
    cvss: "8.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "ABB T-MAC Plus 4.0-24"
    fixed: "4.0-25"
  - id: CVE-2025-14773
    cvss: "8.0"
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "ABB T-MAC Plus 4.0-24"
    fixed: "4.0-25"
  - id: CVE-2025-14774
    cvss: "7.4"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ABB T-MAC Plus 4.0-24 (Card Reader service, adjacent network)"
    fixed: "4.0-25"
sources:
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-04"
    publisher: "CISA (ICSA-26-195-04, republishing Rockwell Automation PSIRT)"
    date: "2026-07-14"
    role: primary
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-03"
    publisher: "CISA (ICSA-26-195-03, republishing ABB PSIRT)"
    date: "2026-07-14"
    role: primary
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-02"
    publisher: "CISA (ICSA-26-195-02, ABB Ability Edgenius)"
    date: "2026-07-14"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-01"
    publisher: "CISA (ICSA-26-195-01, ABB Advant Master Online Builder)"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Successful exploitation of this vulnerability could allow an attacker to read or delete files, stop tasks, modify memory, and change I/O states, potentially impacting the confidentiality, integrity, and availability of the device."
    publisher: "CISA (ICSA-26-195-04, republishing Rockwell Automation PSIRT)"
  - quote: "No known public exploitation specifically targeting this vulnerability has been reported to CISA at this time."
    publisher: "CISA (ICSA-26-195-04, republishing Rockwell Automation PSIRT)"
verification: single-source-national-cert
sourcing_note: "Each item traces to a single CISA ICS advisory (a government-authority disclosure republishing the vendor PSIRT verbatim) — no second independent source. CVE ids, CVSS scores, CWE classes and affected-vs-fixed version status were transcribed from the machine-readable CSAF JSON for each advisory; the Rockwell CVE-2026-10577 base score is 10.0. For ABB T-MAC Plus the CSAF product status names 4.0-24 as affected and 4.0-25 as the fixed release."
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
  - "Upgrade every Rockwell 1715-AENTR EtherNet/IP Adapter (firmware ≤ 3.003) to firmware 3.011; until the OT change window allows it, confirm the adapter does not answer on a routable or business-network segment and restrict its debug/CLI port to the specific engineering-workstation IPs at the switch/firewall."
  - "Update any ABB T-MAC Plus 4.0-24 terminal-management system to the fixed 4.0-25 release, and update ABB Ability Edgenius to 3.2.4.1."
migrated_from: null
---

CISA published four Industrial Control Systems advisories on 2026-07-14, each a verbatim republication of a vendor PSIRT bulletin, that land squarely on this constituency's energy and water sectors and on a Swiss-headquartered vendor ([CISA, 2026-07-14](https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-04)). The most severe is **CVE-2026-10577** in the **Rockwell Automation 1715-AENTR EtherNet/IP Adapter** (all versions ≤ 3.003), rated CVSS v3.1 10.0 for missing authentication on a critical function (CWE-306): a network-accessible debug port exposes intrusive CLI commands with no authentication, so an unauthenticated remote attacker can "read or delete files, stop tasks, modify memory, and change I/O states" on the device ([CISA / Rockwell PSIRT, 2026-07-14](https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-04)). The advisory names the affected sectors as Energy, Water and Wastewater, and Critical Manufacturing; Rockwell fixes it in **firmware version 3.011** and CISA additionally recommends network isolation for devices that cannot be upgraded immediately ([CISA / Rockwell PSIRT SD1785, 2026-07-14](https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-04)). No known public exploitation has been reported to CISA.

Separately, **ABB T-MAC Plus 4.0-24** (fixed in 4.0-25) — a Terminal Management System operating chemical/petroleum terminals, pipeline and refinery tankage, bulk plants and hydrogen terminals — is subject to four flaws responsibly disclosed by Angelo Catalani of Italy's national cybersecurity agency (ACN): **CVE-2025-14771** (CVSS 9.9, a low-privilege authenticated file disclosure via a crafted HTTP GET against the web application, CWE-552), **CVE-2025-14772** (CVSS 8.8, broken access control letting a low-privilege user perform administrative operations, CWE-639), **CVE-2025-14773** (CVSS 8.0, stored cross-site scripting) and **CVE-2025-14774** (CVSS 7.4, an adjacent-network denial of service of the Card Reader service caused by an unencrypted communication protocol) ([CISA / ABB PSIRT, 2026-07-14](https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-03)). ABB states exploitation requires network or physical access to the terminal LAN rather than internet reachability, and that an update resolves the set. The same day, ABB shipped a fix in **Ability Edgenius** (fixed in 3.2.4.1) for the previously-disclosed **CVE-2026-31431** "Copy Fail" Linux-kernel `algif_aead` local root-escalation flaw — new here only in that a specific Swiss-vendor OT product is now named as an affected instance ([CISA / ABB PSIRT, 2026-07-14](https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-02)) — and a low-severity (CVSS 4.4) DLL search-path fix (CVE-2025-13162) in 800xA for Advant Master / Control Builder A ([CISA / ABB PSIRT, 2026-07-14](https://www.cisa.gov/news-events/ics-advisories/icsa-26-195-01)).

**Defender takeaway:** the Rockwell flaw is the one that changes work this week for OT operators — upgrade the adapter to firmware 3.011, and where an OT change window makes that non-immediate, treat network segmentation as the interim control; because the debug/CLI service is a distinct network service from the normal EtherNet/IP control protocol, the highest-signal telemetry is network-flow monitoring for any connection to that port from a host other than a known engineering workstation; no legitimate remote-management workflow should reach it. **Triage:** on the Rockwell adapter there is no authentication to correlate against, so any inbound session to the debug/CLI port from an unexpected source is itself the indicator; on ABB T-MAC Plus the abuses are authenticated-tier, so the hunt surface is the web-application access log — GET requests probing file paths outside the expected UI structure (the CVE-2025-14771 disclosure path) and administrative API calls issued by accounts holding only low-privilege roles (the CVE-2025-14772 authorization bypass), distinguished from benign admin activity by the mismatch between the session's role and the operation performed.
