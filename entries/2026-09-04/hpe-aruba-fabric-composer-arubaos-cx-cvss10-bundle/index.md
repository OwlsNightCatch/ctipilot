---
schema: 1
kind: vulnerability
title: "HPE Networking Fabric Composer and ArubaOS-CX: two unauthenticated CVSS 10.0 RCEs in the fabric-management plane, plus a CVSS 9.8 unauthenticated buffer-overflow RCE in the switch OS"
headline: "HPE patches unauthenticated administrative-takeover flaws in the controller that manages Aruba switch fabrics, and a separate pre-auth RCE in ArubaOS-CX itself"
summary: >
  HPE's September 2026 Aruba Networking bulletins fix 45 CVEs in Networking Fabric Composer (AFC),
  two of them unauthenticated CVSS 10.0 flaws reaching full administrative or OS-level compromise,
  plus a separate CVSS 9.8 unauthenticated buffer-overflow RCE in ArubaOS-CX switch firmware. No
  exploitation or public proof-of-concept reported for either bulletin.
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
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.0.0 through 7.3.3"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-76657
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.0.0 through 7.3.3"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-19766
    cvss: "9.6"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.0.0 through 7.3.3"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-73701
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fabric Composer 7.0.0 through 7.3.3"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-73700
    cvss: "9.0"
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "Fabric Composer 7.0.0 through 7.3.3"
    fixed: "7.4.0 (or 7.3.4 for the 7.3 branch)"
  - id: CVE-2026-73749
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "10.18.0000-10.18.0001; 10.17.1021 and earlier; 10.16.1051 and earlier; 10.13.1180 and earlier; 10.10.1180 and earlier"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+ / 10.10.1181+"
  - id: CVE-2026-73752
    cvss: "8.8"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "See HPE's ArubaOS-CX bulletin version table"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+ / 10.10.1181+"
  - id: CVE-2026-73778
    cvss: "8.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: default-config
    status: [patch-available]
    affected: "Switches left in factory-default or immediate post-Zero-Touch-Provisioning state before an administrator sets credentials"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+ / 10.10.1181+"
  - id: CVE-2026-73782
    cvss: "8.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "See HPE's ArubaOS-CX bulletin version table"
    fixed: "10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+ / 10.10.1181+"
sources:
  - url: "https://cveawg.mitre.org/api/cve/CVE-2026-76658"
    publisher: "MITRE CVE Program (HPE as CNA)"
    date: "2026-09-01"
    role: primary
  - url: "https://cveawg.mitre.org/api/cve/CVE-2026-76657"
    publisher: "MITRE CVE Program (HPE as CNA)"
    date: "2026-09-01"
    role: primary
  - url: "https://cveawg.mitre.org/api/cve/CVE-2026-73749"
    publisher: "MITRE CVE Program (HPE as CNA)"
    date: "2026-09-01"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/"
    publisher: "BleepingComputer"
    date: "2026-09-03"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0339"
    publisher: "NCSC-NL"
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
  - quote: "A vulnerability has been identified in the SSH daemon of HPE Networking Fabric Composer that could allow an unauthenticated remote attacker to gain administrative access to vulnerable AFC hosts. Successful exploitation could allow an attacker to execute arbitrary commands as a privileged user on the underlying operating system leading to complete system compromise."
    publisher: "MITRE CVE Program (HPE as CNA)"
  - quote: "Multiple vulnerabilities exist in a daemon of AOS-CX that may allow for improper processing of malformed input. An unauthenticated remote attacker could exploit these vulnerabilities by sending specially crafted packets to the affected service."
    publisher: "MITRE CVE Program (HPE as CNA)"
verification: single-source
sourcing_note: >
  HPE is the primary disclosing party for its own products (Admiralty vendor-PSIRT carve-out);
  its own bulletin pages (support.hpe.com hpesbnw05133en_us / hpesbnw05134en_us) sit behind an HPE
  support-portal login wall and could not be fetched directly, so MITRE's CVE records (HPE as the
  assigning CNA) served as the vendor-authoritative primary for the individual flaw descriptions.
  BleepingComputer, GBHackers, securityonline.info, NCSC-NL and CERT-FR all relay the same HPE
  bulletins rather than independently assessing them, so credibility stays at 2 rather than 1.
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
  - "Patch every HPE Networking Fabric Composer instance to 7.4.0 (or 7.3.4 on the 7.3 branch) now; until patched, remove the AFC API and web management interface from general-purpose networks onto a dedicated out-of-band management segment and restrict SSH access to the AFC host by source address — CVE-2026-76658 has no authentication factor to fall back on."
  - "Patch every ArubaOS-CX switch to its branch's fixed release (10.18.1002+ / 10.17.1030+ / 10.16.1060+ / 10.13.1190+ / 10.10.1181+ — note 10.10.x is past HPE's End of Maintenance and receives only critical fixes); audit any switch left in factory-default or immediate post-ZTP state, since CVE-2026-73778's predictable admin password fully compromises a device before an administrator ever sets its own credentials."
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
migrated_from: null
---

HPE published two Aruba Networking security bulletins in the same release window: Fabric Composer bulletin HPESBNW05133 on 2026-09-01, and an ArubaOS-CX bulletin around the same date, both picked up by NCSC-NL and CERT-FR on 2026-09-02/03. HPE Networking Fabric Composer (AFC), the controller that manages Aruba CX switch fabrics, carries 45 CVEs in one bulletin ([NCSC-NL, 2026-09-03](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0339)), two of them CVSS 10.0: CVE-2026-76658 is an authentication weakness in AFC's SSH daemon that lets an unauthenticated remote attacker connect with no credentials, user interaction or preparation and execute arbitrary commands as a privileged operating-system user ([HPE, via MITRE CVE record, 2026-09-01](https://cveawg.mitre.org/api/cve/CVE-2026-76658)); CVE-2026-76657 is an API authentication-bypass flaw letting an unauthenticated attacker circumvent AFC's API auth controls and obtain administrative privileges. Three more rank Critical: CVE-2026-19766 (9.6, adjacent-network auth bypass to privileged code execution on the underlying OS), CVE-2026-73701 (9.0, unauthenticated privileged RCE with unspecified preconditions) and CVE-2026-73700 (9.0, authenticated stored cross-site scripting reachable by a low-privilege operator against an admin). Fixed in Fabric Composer 7.4.0 (or 7.3.4 for the 7.3 branch); every 7.3.3-and-earlier install is affected, all discovered by HPE's own internal Networking security research team.

Separately, ArubaOS-CX — the network OS on Aruba's CX-series campus and data-center switches — carries CVE-2026-73749 (CVSS 9.8): a buffer overflow in an unnamed AOS-CX daemon that an unauthenticated remote attacker triggers by sending specially crafted packets, reaching remote code execution with elevated privileges ([HPE, via MITRE CVE record, 2026-09-01](https://cveawg.mitre.org/api/cve/CVE-2026-73749)). Affected release branches and fixes, per HPE's bulletin: the 10.18 branch up to and including 10.18.0001, fixing to 10.18.1002+, 10.17.1021 and earlier fix to 10.17.1030+, 10.16.1051 and earlier fix to 10.16.1060+, 10.13.1180 and earlier fix to 10.13.1190+, and 10.10.1180 and earlier fix to 10.10.1181+ — that last branch is already past HPE's End of Maintenance and receives only critical-severity fixes, a category this CVE qualifies for. The same ArubaOS-CX bulletin lists further CVEs including an unauthenticated adjacent-network arbitrary file write via an API endpoint (CVE-2026-73752, 8.8), an unauthenticated format-string flaw in the CLI reachable from an adjacent network (CVE-2026-73782, 8.8), and an unauthenticated predictable factory-default password (CVE-2026-73778, 8.1) granting full admin control on a switch before an administrator sets credentials after Zero-Touch Provisioning. The exact further-CVE count is unresolved between this entry's two cited sources: BleepingComputer's account of HPE's own bulletin states "23 other security vulnerabilities...between 8.1 and 8.8" ([BleepingComputer, 2026-09-03](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)), and its list names at least one identifier (CVE-2026-73781, an authenticated stored XSS) absent from NCSC-NL's independently-mirrored structured advisory data for the same bulletin, which lists 25 further CVEs spanning a wider 4.9-8.8 range ([NCSC-NL, 2026-09-03](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0340)); HPE's own bulletin page sits behind a support-portal login wall this entry could not read directly to resolve the discrepancy. HPE states it is not aware of active exploitation or public proof-of-concept for either bulletin's flaws.

**Defender takeaway:** Fabric Composer sits in the network-management plane rather than on a single application host, so its compromise grants control over the whole switch-fabric configuration — segmentation, routing, persistence below typical EDR visibility. Before patching, remove the AFC API and web management interface onto a dedicated out-of-band management segment, restrict SSH access to the AFC host by source address, and review AFC operator authentication logs for administrative logins originating outside the management network. For ArubaOS-CX, diffing live fabric configuration (VLANs, ACLs, routes) against an approved baseline is the most likely way to catch exploitation after the fact, since a successful buffer-overflow exploit against a compiled daemon leaves little application-layer telemetry beyond a crash-restart cycle.

## Correction — 2026-09-06T13:45:00Z

The affected range this entry recorded for CVE-2026-73749's 10.18 branch was inverted. HPE's own CVE record, published through MITRE as the CNA, states the affected AOS-CX versions as 10.18.0000 up to and including 10.18.0001 ([HPE, via MITRE CVE record, 2026-09-01](https://cveawg.mitre.org/api/cve/CVE-2026-73749)); BleepingComputer's reading of HPE's bulletin agrees, listing the branch as "10.18.0001 → upgrade to 10.18.1002+" ([BleepingComputer, 2026-09-03](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/)). 10.18.0001 is therefore the last affected build on that branch, not the first, and the upper bound 10.18.1001 appears in neither source.

What this changes for a defender: a switch running 10.18.0000 is in scope for this unauthenticated remote code execution and would have read the previous range as beginning above its own version. The fixed release for the branch, 10.18.1002 or later, is unchanged, as are the 10.17, 10.16, 10.13 and 10.10 branches.
