---
schema: 1
kind: vulnerability
title: "Cisco IOS XE August 2026 hardening release — seven CVEs that each stand for a whole class of internally found bugs, no workarounds, and frontier AI models among the discovery tools"
headline: "Cisco ships one CVE per CWE class rather than per bug, so no IOS XE device can be triaged flaw-by-flaw — only by release"
summary: >
  Cisco published a security hardening release for IOS XE on 2026-08-05 covering seven CVEs
  (CVE-2026-20267 through CVE-2026-20273), topped by CVE-2026-20272 at CVSS 9.8 for command, OS and
  argument injection. The advisory's structure is the operationally important part: Cisco grouped multiple
  internally discovered bugs by CWE class and assigned one CVE per class, so each score represents the worst
  underlying bug in that group and no individual flaw can be assessed. The vulnerabilities affect IOS XE in
  autonomous or controller mode regardless of configuration, there are no workarounds, and Cisco says they
  were found in internal testing using existing processes as well as frontier AI models.
discovered_at: "2026-08-08T05:00:00Z"
event_date: "2026-08-05"
run_id: 2026-08-08T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, priv-esc, patch-available]
regions: [global]
sectors: [public-sector, telco, energy, transport, finance]
entities: []
techniques: [T1190, T1068]
affected_products: ["Cisco IOS XE Software"]
cves:
  - id: CVE-2026-20272
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "IOS XE 17.9, 17.12, 17.15, 17.18 and 26.1 in autonomous or controller mode, regardless of device configuration"
    fixed: "17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2"
  - id: CVE-2026-20267
    cvss: "9.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "IOS XE 17.9, 17.12, 17.15, 17.18 and 26.1"
    fixed: "17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2"
  - id: CVE-2026-20268
    cvss: "8.6"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "IOS XE 17.9, 17.12, 17.15, 17.18 and 26.1"
    fixed: "17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2"
  - id: CVE-2026-20269
    cvss: "8.6"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "IOS XE 17.9, 17.12, 17.15, 17.18 and 26.1"
    fixed: "17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2"
  - id: CVE-2026-20270
    cvss: "8.6"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "IOS XE 17.9, 17.12, 17.15, 17.18 and 26.1"
    fixed: "17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2"
  - id: CVE-2026-20271
    cvss: "8.6"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "IOS XE 17.9, 17.12, 17.15, 17.18 and 26.1"
    fixed: "17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2"
  - id: CVE-2026-20273
    cvss: "8.6"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "IOS XE 17.9, 17.12, 17.15, 17.18 and 26.1"
    fixed: "17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2"
sources:
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ"
    publisher: "Cisco PSIRT"
    date: "2026-08-05"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0279"
    publisher: "NCSC-NL"
    date: "2026-08-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The CVSS score that is assigned to each CVE ID represents the maximum potential severity of the single most impactful underlying bug within that specific CWE category."
    publisher: "Cisco PSIRT"
  - quote: "These vulnerabilities were found during internal testing and are not known to be actively exploited."
    publisher: "Cisco PSIRT"
  - quote: "There are no workarounds that address these vulnerabilities."
    publisher: "Cisco PSIRT"
  - quote: "These vulnerabilities were found during internal security testing using existing testing processes as well as frontier AI models."
    publisher: "Cisco PSIRT"
verification: multi-source
sourcing_note: "Per-CVE scores and CWE classes are taken from Cisco's own per-CVE table in the advisory, not from a summary or a relay; NCSC-NL corroborates the release but is a restatement of Cisco's advisory rather than an independent assessment. Cisco publishes one CVSS vector for the advisory as a whole (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) and no per-CVE vectors, so the pre-auth/zero-click values recorded on each record follow that single published metric; they are not per-flaw statements, and Cisco's CWE-grouping model means the bugs behind each identifier may vary in reachability."
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

Cisco's IOS XE engineering team published a security hardening release on 2026-08-05 carrying seven CVEs, and the disclosure model matters more than any individual identifier. Rather than one CVE per bug, Cisco "grouped these issues by their underlying vulnerability class — Common Weakness Enumeration (CWE) — and assigned a single Common Vulnerabilities and Exposures Identifier (CVE ID) to each CWE grouping", stating plainly that "the CVSS score that is assigned to each CVE ID represents the maximum potential severity of the single most impactful underlying bug within that specific CWE category" ([Cisco PSIRT, 2026-08-05](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ)).

The consequence for anyone running a risk-based patch process is that per-flaw triage is unavailable by construction. CVE-2026-20272 carries CVSS 9.8 for improper neutralisation of special elements — command, OS and argument injection — but that score belongs to the worst bug in the group, and neither the count of bugs behind it nor their individual reachability is published. The remaining six are CVE-2026-20267 (improper access control, 9.0), CVE-2026-20268 (memory-buffer bounds, 8.6), CVE-2026-20269 (resource lifetime, 8.6), CVE-2026-20270 (incorrect calculation, 8.6), CVE-2026-20271 (control-flow management, 8.6) and CVE-2026-20273 (input validation including path traversal, 8.6) ([Cisco PSIRT, 2026-08-05](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ)). The advisory's aggregate CVSS vector is `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` — network-reachable and unauthenticated at the top of the range.

Exposure is broad and configuration-independent: the vulnerabilities "affect Cisco IOS XE Software when it is running in autonomous or controller mode, regardless of device configuration", across releases 17.9, 17.12, 17.15, 17.18 and 26.1, with first fixed releases 17.9.10, 17.12.8, 17.15.6, 17.18.4 or 17.18.4a, and 26.1.2 respectively; Catalyst 3650 and 3850 Series switches run none of these trains and were not evaluated ([Cisco PSIRT, 2026-08-05](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ)). Cisco states "there are no workarounds that address these vulnerabilities" and that the flaws "were found during internal testing and are not known to be actively exploited", with PSIRT aware of no public announcements or malicious use ([Cisco PSIRT, 2026-08-05](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ)). NCSC-NL relayed the release to European constituents on 2026-08-07 ([NCSC-NL, 2026-08-07](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0279)).

One line in the Source section is worth reading twice: "These vulnerabilities were found during internal security testing using existing testing processes as well as frontier AI models" ([Cisco PSIRT, 2026-08-05](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ)). A vendor attributing a bulk hardening release partly to model-assisted review is a plausible signal that such releases become more frequent and larger, which is a planning input for change windows on network infrastructure rather than an immediate threat.

No detection guidance is possible here and none should be attempted: Cisco publishes no per-bug technical detail, no reachable component, and no exploitation pattern, so nothing supports a hunt hypothesis. The advisory does list Snort rules 66897-66898 as associated coverage. This is an inventory-and-schedule item — identify every device on 17.9, 17.12, 17.15, 17.18 or 26.1, and move it to the first fixed release for its train — carried here because there is no configuration that removes the exposure and no interim mitigation to fall back on, not because anything indicates it is being attacked.
