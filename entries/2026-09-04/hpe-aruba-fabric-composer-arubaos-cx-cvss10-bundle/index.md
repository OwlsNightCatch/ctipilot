---
schema: 1
kind: vulnerability
title: "HPE Networking Fabric Composer and ArubaOS-CX: an unauthenticated CVSS 10.0 RCE and a CVSS 10.0 authentication bypass in the fabric-management plane, plus a CVSS 9.8 unauthenticated buffer-overflow RCE in the switch OS"
headline: "HPE patches unauthenticated administrative-takeover flaws in the controller that manages Aruba switch fabrics, and a separate pre-auth RCE in ArubaOS-CX itself"
summary: >
  HPE's 2026-09-01 Aruba Networking bulletins fix 52 CVEs in Networking Fabric Composer (AFC), two
  of them unauthenticated CVSS 10.0 flaws reaching full administrative or OS-level compromise, and
  34 in AOS-CX switch firmware, led by a CVSS 9.8 unauthenticated buffer-overflow RCE. HPE reports
  no public discussion or exploit code for either bulletin as of release.
discovered_at: "2026-09-04T05:20:00Z"
updated_at: null
event_date: "2026-09-01"
run_id: 2026-09-04T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, auth-bypass, patch-available]
regions: [global]
sectors: [public-sector]
entities: []
techniques: [T1190]
affected_products: ["HPE Networking Fabric Composer", "HPE Aruba Networking AOS-CX"]
cves:
  - id: CVE-2026-76658
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.3.3 and below"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-76657
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.3.3 and below"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-19766
    cvss: "9.6"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.3.3 and below"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-73701
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.3.3 and below"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-73700
    cvss: "9.0"
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "Fabric Composer 7.3.3 and below"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-73749
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "10.18.x before 10.18.1002 (CERT-FR's reading, HPE lists 10.18.0001); 10.17.1021 and earlier; 10.16.1051 and earlier; 10.13.1180 and earlier; 10.10.1180 and earlier"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+ / 10.10.1181+"
  - id: CVE-2026-73752
    cvss: "8.8"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "10.18.x before 10.18.1002 (CERT-FR's reading, HPE lists 10.18.0001); 10.17.1021 and earlier; 10.16.1051 and earlier; 10.13.1180 and earlier; 10.10.1180 and earlier"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+; no fix on end-of-maintenance 10.10.x"
  - id: CVE-2026-73778
    cvss: "8.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: default-config
    status: [patch-available]
    affected: "10.18.x before 10.18.1002 (CERT-FR's reading, HPE lists 10.18.0001); 10.17.1021 and earlier; 10.16.1051 and earlier; 10.13.1180 and earlier; 10.10.1180 and earlier; only in factory-default or post-ZTP state before credentials are set"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+; no fix on end-of-maintenance 10.10.x"
  - id: CVE-2026-73782
    cvss: "8.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "10.18.x before 10.18.1002 (CERT-FR's reading, HPE lists 10.18.0001); 10.17.1021 and earlier; 10.16.1051 and earlier; 10.13.1180 and earlier; 10.10.1180 and earlier"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+; no fix on end-of-maintenance 10.10.x"
sources:
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt"
    publisher: "HPE Networking (HPESBNW05133)"
    date: "2026-09-01"
    role: primary
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt"
    publisher: "HPE Networking (HPESBNW05134)"
    date: "2026-09-01"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0339"
    publisher: "NCSC-NL"
    date: "2026-09-03"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/"
    publisher: "BleepingComputer"
    date: "2026-09-03"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0340"
    publisher: "NCSC-NL"
    date: "2026-09-03"
    role: corroborating
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1104/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-09-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A vulnerability has been identified in the SSH daemon of HPE Networking Fabric Composer that could allow an unauthenticated remote attacker to gain administrative access to vulnerable AFC hosts."
    publisher: "HPE Networking (HPESBNW05133)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt"
  - quote: "Tracked as CVE-2026-73749, the security issue is a buffer overflow that allows unauthenticated remote attackers to send specially crafted packets to an affected daemon process, achieving code execution with elevated privileges."
    publisher: "BleepingComputer"
  - quote: "HPE Networking is not aware of any public discussion or exploit code that targets the listed vulnerabilities as of the release date of this advisory."
    publisher: "HPE Networking (HPESBNW05134)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt"
verification: single-source
sourcing_note: >
  HPE's two bulletins, published as plain-text advisories, are the primary source for CVE counts,
  scores and affected and fixed versions. NCSC-NL, CERT-FR and BleepingComputer relay the same
  bulletins rather than assessing the flaws independently.
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
  - "Patch every HPE Networking Fabric Composer instance to 7.4.0 (or 7.3.4 on the 7.3 branch) now; until patched, remove the AFC API and web management interface from general-purpose networks onto a dedicated out-of-band management segment and restrict SSH access to the AFC host by source address, because CVE-2026-76658 needs no authentication."
  - "Patch every ArubaOS-CX switch to its branch's fixed release (10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+ / 10.10.1181+; 10.10.x is past HPE's End of Maintenance and received only Critical-severity fixes); audit any switch left in factory-default or immediate post-ZTP state, since CVE-2026-73778's predictable admin password fully compromises a device before an administrator ever sets its own credentials."
updates:
  - at: "2026-09-06T13:45:00Z"
    run_id: 2026-09-06T1308Z-audit
    type: correction
    summary: >
      The affected 10.18 range recorded for CVE-2026-73749 read "10.18.0001-10.18.1001", which
      inverted the branch boundary: HPE's own CVE record gives the affected range as 10.18.0000 up
      to and including 10.18.0001, so 10.18.0001 is the last affected build rather than the first,
      and 10.18.1001 appears in neither cited source. A switch on 10.18.0000 would have read the
      previous range as starting above it. The other four branches and every fixed version were
      already correct.
    fields: [cves, body]
  - at: "2026-09-30T07:19:37Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Several flaw descriptions, counts and version ranges rested on relays and on CVE-record
      mirrors rather than on HPE's own bulletins, which are now the primary source: the Fabric
      Composer bulletin lists 52 CVEs (not 45) affecting 7.3.3 and below, the AOS-CX bulletin lists
      34 CVEs, HPE lists 10.18.0001 as the affected 10.18 build while CERT-FR reads the branch as
      all 10.18.x before 10.18.1002, and the end-of-maintenance 10.10 branch has no fix for the
      lower-rated AOS-CX flaws. HPE's exploitation statement is quoted as written. The SSH-daemon
      description and its evidence quote now come from HPE's own bulletin, and the takeaway now rests on NCSC-NL's warning
      about internet-reachable management interfaces.
    fields: [sources, cves, evidence, sourcing_note, body, summary, actions, title]
migrated_from: null
---

HPE published two Aruba Networking security bulletins on 2026-09-01: HPESBNW05133 for HPE Networking Fabric Composer (AFC) and HPESBNW05134 for HPE Networking AOS-CX ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)) ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)). AOS-CX is HPE Aruba Networking's operating system for its enterprise network switches ([BleepingComputer, 2026-09-03](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)). The Fabric Composer bulletin lists 52 CVEs, two of them CVSS 10.0: CVE-2026-76658 is a flaw in AFC's SSH daemon that "could allow an unauthenticated remote attacker to gain administrative access to vulnerable AFC hosts" and run arbitrary commands as a privileged user, "leading to complete system compromise" ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)), and CVE-2026-76657 is an API authentication bypass that lets an unauthenticated remote attacker circumvent the API's authentication controls and gain administrative privileges ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)). Three more rank Critical: CVE-2026-19766 (9.6, an authentication bypass in the underlying operating system that lets an unauthenticated adjacent attacker run code as a privileged user), CVE-2026-73701 (9.0, unauthenticated privileged code execution that depends on preconditions outside the attacker's control) and CVE-2026-73700 (9.0, stored cross-site scripting by an authenticated low-privilege operator against an administrator) ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)). HPE lists Fabric Composer 7.3.3 and below as affected, fixed in 7.4.0 and 7.3.4, and states that all of these flaws were found by its own internal security research ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)).

In AOS-CX, CVE-2026-73749 (CVSS 9.8) covers flaws in an AOS-CX daemon that an unauthenticated remote attacker triggers by sending specially crafted packets, reaching remote code execution with elevated privileges ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)) ([BleepingComputer, 2026-09-03](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)). HPE lists AOS-CX 10.18.0001, 10.17.1021 and below, 10.16.1051 and below, 10.13.1180 and below, and 10.10.1180 and below as affected, fixed in 10.18.1002, 10.17.1030, 10.16.1060, 10.13.1190 and 10.10.1181 or later ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)). CERT-FR reads the 10.18 branch more broadly, as every 10.18.x release before 10.18.1002 ([CERT-FR, 2026-09-02](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1104/)); the fix on that branch is 10.18.1002 either way. The 10.10 branch is past End of Maintenance and received fixes only for internally identified Critical-severity flaws, so CVE-2026-73749 is fixed there and the bulletin's lower-rated flaws are not ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)). The bulletin lists 33 further CVEs scored 4.9 to 8.8, among them an unauthenticated arbitrary file write through an API endpoint (CVE-2026-73752, 8.8, adjacent network), an unauthenticated format-string flaw in the CLI (CVE-2026-73782, 8.8, adjacent network), and a predictable factory-default password in the Credential Manager (CVE-2026-73778, 8.1) that gives an unauthenticated attacker full administrative control of a switch in factory-default or post-Zero-Touch-Provisioning state before an administrator sets credentials ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)). For both bulletins HPE states it is not aware of any public discussion or exploit code targeting the flaws as of the release date ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)) ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)).

**Defender takeaway:** NCSC-NL warns that where Fabric Composer's SSH management interface is reachable from the internet, unauthorised attackers from outside can use CVE-2026-76658 to take over the data-center network behind it (translated from Dutch) ([NCSC-NL, 2026-09-03](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0339)). Until patched, follow HPE's workaround of restricting the CLI and web-based management interfaces to a dedicated layer 2 segment or VLAN, or firewall policy, with accounting and logging of user activity ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)); restrict SSH access to the AFC host by source address, and review AFC operator authentication logs for administrative logins from outside the management network. For AOS-CX, diffing live fabric configuration (VLANs, ACLs, routes) against an approved baseline is the most likely way to catch exploitation after the fact, since a successful buffer-overflow exploit against a compiled daemon leaves little application-layer telemetry beyond a crash-restart cycle.

## Correction — 2026-09-06T13:45:00Z

The affected range recorded for CVE-2026-73749's 10.18 branch was inverted. BleepingComputer's reading of HPE's bulletin lists the branch as "10.18.0001 → upgrade to 10.18.1002+" ([BleepingComputer, 2026-09-03](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)), and CERT-FR lists every AOS-CX 10.18.x release before 10.18.1002 as affected ([CERT-FR, 2026-09-02](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1104/)). 10.18.0001 is therefore an affected build, not the first fixed one, and the fix on that branch is 10.18.1002.

## Correction — 2026-09-30T07:19:37Z

HPE's own bulletins correct several points. The Fabric Composer bulletin lists 52 CVEs, not the 45 in NCSC-NL's mirror ([NCSC-NL, 2026-09-03](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0339)), and names Fabric Composer 7.3.3 and below as affected, with no lower version bound ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)). The AOS-CX bulletin lists 34 CVEs, CVE-2026-73749 plus 33 others scored 4.9 to 8.8 ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)), more than the 23 further flaws BleepingComputer counted ([BleepingComputer, 2026-09-03](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)) and the 26 CVEs in NCSC-NL's advisory ([NCSC-NL, 2026-09-03](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0340)). For CVE-2026-73749 on the 10.18 branch, HPE lists 10.18.0001 as the affected build ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)) and CERT-FR reads the branch as every 10.18.x release before 10.18.1002 ([CERT-FR, 2026-09-02](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1104/)). Either way the fix is 10.18.1002, and the earlier range of 10.18.0000 to 10.18.0001 did not come from HPE's bulletin. On the end-of-maintenance 10.10 branch only Critical-severity flaws were fixed, so the lower-rated AOS-CX flaws have no fix there ([HPE, HPESBNW05134, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt)). HPE's exploitation statement is that it knows of no public discussion or exploit code, not a statement about active exploitation ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)). HPE titles CVE-2026-76658 an unauthenticated remote code execution in the Fabric Composer SSH daemon, not an authentication weakness ([HPE, HPESBNW05133, 2026-09-01](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt)). The earlier takeaway described Fabric Composer's role without a cited source. It now rests on NCSC-NL's warning that an internet-reachable SSH management interface lets unauthenticated attackers take over the data-center network behind it ([NCSC-NL, 2026-09-03](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0339)).
