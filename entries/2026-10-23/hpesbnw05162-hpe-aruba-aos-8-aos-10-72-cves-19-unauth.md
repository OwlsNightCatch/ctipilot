---
schema: 1
kind: vulnerability
title: "HPESBNW05162, HPE Networking (Aruba) AOS-8 and AOS-10 wireless: 72 CVEs fixed in one bulletin, 19 of them unauthenticated and network-reachable at CVSS 9.0 or above, across controllers, gateways and access points"
headline: "HPE's Aruba wireless bulletin fixes 19 unauthenticated network flaws at CVSS 9.0+; HPE knows of no public exploit code"
summary: >
  HPE Networking's bulletin HPESBNW05162 of 2026-10-22 fixes 72 CVEs in AOS-8 and AOS-10 for Mobility Conductors, Controllers,
  Gateways and access points, 33 of them at CVSS 3.1 9.0 or higher and 19 of those reachable over the network without authentication
  (eight at 10.0). HPE found the flaws through internal research, knows of no public discussion or exploit code, and strongly urges
  patching; its only workaround is to confine the CLI and web management interfaces to a dedicated segment behind firewall policy.
discovered_at: "2026-10-23T03:36:00Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-23T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, auth-bypass, sqli, patch-available]
regions: [global]
sectors: []
entities: ["product:hpe-networking-aos-10", "product:hpe-networking-aos-8"]
techniques: [T1190, T1210]
affected_products: ["HPE Networking AOS-10", "HPE Networking AOS-8"]
cves:
  - id: CVE-2026-79844
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14"
  - id: CVE-2026-79845
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14"
  - id: CVE-2026-79846
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79847
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14"
  - id: CVE-2026-79848
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79849
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79850
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79851
    cvss: "10.0 (CVSS 3.1)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14"
  - id: CVE-2026-79852
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected; AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14, AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79853
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14"
  - id: CVE-2026-79854
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14"
  - id: CVE-2026-79855
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79856
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79857
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79858
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79859
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79860
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-8.13.3.1, AOS-8.10.0.24"
  - id: CVE-2026-79861
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14"
  - id: CVE-2026-79872
    cvss: "9.4 (CVSS 3.1)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "AOS-10 10.8.0.0 to 10.8.1.1, 10.7.0.0 to 10.7.2.6, 10.4.0.0 to 10.4.1.13; end-of-maintenance versions presumed affected; AOS-8 8.13.0.0 to 8.13.3.0, 8.10.0.0 to 8.10.0.23; end-of-maintenance versions presumed affected"
    fixed: "AOS-10.8.1.2, AOS-10.7.2.7, AOS-10.4.1.14, AOS-8.13.3.1, AOS-8.10.0.24"
sources:
  - url: "https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US"
    publisher: "HPE Networking (security bulletin HPESBNW05162 rev. 1)"
    date: "2026-10-22"
    role: primary
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json"
    publisher: "HPE Networking (CSAF for HPESBNW05162)"
    date: "2026-10-22"
    role: primary
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt"
    publisher: "HPE Networking (HPESBNW05162 text advisory)"
    date: "2026-10-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Authentication bypass vulnerabilities in the affected interface of AOS-10 could allow an unauthenticated remote attacker to run arbitrary commands on the underlying host if certain preconditions outside of the attacker's control are met."
    publisher: "HPE Networking (CSAF for HPESBNW05162)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json"
verification: single-source
sourcing_note: >
  HPE Networking's bulletin and its CSAF file are the first-party source for its own products. The bulletin page carries a
  2026-09-30 template timestamp while its CSAF records the initial release as 2026-10-22T16:00Z, which is the date used here; the
  CVE records below list only the unauthenticated network-reachable rows scored 9.0 or higher, and the counts come from the CSAF's
  CVSS 3.1 scores.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every HPE Networking (Aruba) Mobility Conductor, Controller, Gateway and access point on AOS-10 or AOS-8 to the fixed build of its train (10.8.1.2, 10.7.2.7, 10.4.1.14, 8.13.3.1 or 8.10.0.24), and until then confine the CLI and web management interfaces to a dedicated layer 2 segment or VLAN behind firewall policy, as HPE advises."
updates:
  - at: "2026-10-25T14:04:41Z"
    run_id: 2026-10-25T1308Z-audit
    type: correction
    summary: >
      Corrects the affected ranges: HPE's CSAF matches its bulletin (AOS-10 10.8, 10.7, 10.4; AOS-8 8.13,
      8.10) and has no wider 10.6, 10.3 or 8.12 range, which the entry had stated; HPE presumes
      end-of-maintenance versions affected. Also corrects the counts (33 at CVSS 9.0 or higher, ten at
      9.6, 14 adjacent-network).
    fields: [summary, cves, sources, body]
migrated_from: null
---

HPE Networking's bulletin HPESBNW05162 (initial release 2026-10-22) fixes 72 CVEs in the wireless operating systems AOS-8 and AOS-10 for Mobility Conductors, Controllers, Gateways managed by HPE Networking Central, AOS-10 access points (AOS-AP) and AOS-8 Instant access points (AOS-IAP) ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US)). By the CSAF's CVSS 3.1 scores, 33 of the 72 rate 9.0 or higher (eight at 10.0, ten at 9.8, ten at 9.6, one at 9.4 and four at 9.3); the 19 rated 10.0, 9.8 or 9.4 need network access and no privileges, and the other 14 are reachable from the adjacent network ([HPE Networking CSAF, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)). The named mechanisms include authentication bypasses and command injection in the AOS-10 interface and in the PAPI protocol, a buffer overflow and a command injection in the AOS-8 PAPI protocol that arrive as crafted packets on its UDP port, an authentication bypass in the AOS-8 SSH daemon, and SQL injection in the web-based management interface ([HPE Networking CSAF, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)). HPE says the flaws were generally found by its internal security research, that it is not aware of public discussion or exploit code as of the release, and that customers are strongly urged to patch; for some of the critical rows exploitation also needs preconditions outside the attacker's control, which the bulletin does not itemise ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US))([HPE Networking CSAF, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)).

The bulletin and its CSAF name AOS-10 10.8.x up to 10.8.1.1, 10.7.x up to 10.7.2.6 and 10.4.x up to 10.4.1.13, and AOS-8 8.13.x up to 8.13.3.0 and 8.10.x up to 8.10.0.23; fixed builds are AOS-10.8.1.2, 10.7.2.7 and 10.4.1.14 and AOS-8.13.3.1 and 8.10.0.24 ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US))([HPE Networking CSAF, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)). HPE's workaround is to restrict the CLI and web-based management interfaces to a dedicated layer 2 segment or VLAN, controlled by firewall policies at layer 3 and above with accounting controls ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US)).

**Exposure:** any HPE Networking mobility conductor, controller, gateway, access point or virtual machine that runs a listed version; HPE says every compatible hardware model is affected and that its own hardware list is illustrative only, so the check is the software version, not the model ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US)). HPE presumes versions past end of maintenance affected and says installations past end of support should be considered potentially impacted ([HPE Networking, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt)). The named surfaces are the CLI and web management interfaces and the PAPI access-point management protocol on UDP port 8211 ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US))([HPE Networking CSAF, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)).

**Detection:** management-plane access and accounting logs for logins and sessions from outside the management segment, and network flow data for PAPI traffic on UDP 8211 or controller management ports from segments that carry users or guests. HPE publishes no detection guidance, so no post-compromise check is defined ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US)).

**Defender takeaway:** upgrade controllers, gateways and access points to the fixed build of their train, management and PAPI-exposed units first, and apply the management-segment restriction at once where the upgrade has to wait; HPE says it is not aware of public discussion or exploit code, so the order follows exposure of the management and access-point protocol paths rather than a known campaign ([HPE Networking, 2026-10-22](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US)).

## Correction — 2026-10-25T14:04:41Z

HPE's CSAF does not list wider affected ranges than the bulletin text: both name AOS-10 10.8, 10.7 and 10.4 and AOS-8 8.13 and 8.10 up to the stated builds, and neither carries a 10.6, 10.3 or 8.12 range ([HPE Networking CSAF, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)). What HPE adds instead is that versions past end of maintenance are presumed affected and installations past end of support should be considered potentially impacted ([HPE Networking, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt)). The CSAF scores 33 of the 72 flaws at CVSS 9.0 or higher, ten of them at 9.6, and 14 of the 33 are reachable from the adjacent network, not 34, eleven and 15 ([HPE Networking CSAF, 2026-10-22](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)).
