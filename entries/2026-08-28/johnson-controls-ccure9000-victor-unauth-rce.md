---
schema: 1
kind: vulnerability
horizon: operational
title: "Johnson Controls C-CURE 9000 / victor: unauthenticated adjacent-network deserialization RCE on physical access-control application servers reaches connected security-workstation clients too (CVE-2026-21655, CVSS 9.6)"
headline: "CISA publishes an unauthenticated deserialization RCE that can 'impact physical security controls' on a widely deployed access-control platform"
summary: >
  CISA's ICSA-26-204-01 (Update A, 2026-08-11) covers three CVEs in Johnson Controls C-CURE 9000
  and victor. CVE-2026-21655 (CVSS 9.6) lets an unauthenticated, adjacent-network attacker exploit
  a deserialization path to achieve arbitrary code execution on the C-CURE 9000/victor application
  server, on victor itself, and on connected clients including physical-security-personnel
  workstations. No known public exploitation. CISA's own structured advisory tags this CVE with
  an SSRF-class CWE that contradicts its own deserialization-based description.
discovered_at: "2026-08-28T05:38:00Z"
updated_at: null
event_date: "2026-08-11"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, patch-available, ot-ics]
regions: [global, europe]
sectors: [public-sector, energy, water, transport, healthcare, finance]
entities: []
techniques: [T1210]
affected_products: ["Johnson Controls C-CURE 9000", "Johnson Controls victor Application Server", "Johnson Controls victor", "Johnson Controls victor Web"]
cves:
  - id: CVE-2026-21655
    cvss: "9.6"
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "C-CURE 9000 ≤v3.10.1; victor Application Server ≤v4.10; victor ≤v7.0"
    fixed: "C-CURE 9000 v3.20+; victor Application Server v4.20+; victor v8.0+"
  - id: CVE-2026-21653
    cvss: "9.6"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "victor Web <v7.0"
    fixed: "victor v8.0+"
  - id: CVE-2026-34496
    cvss: "8.0"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "victor Web ≤v7.1"
    fixed: "victor v8.0+"
sources:
  - url: "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsa-26-204-01.json"
    publisher: "CISA (ICSA-26-204-01, CSAF structured advisory)"
    date: "2026-08-11"
    role: primary
  - url: "https://www.isssource.com/johnson-controls-updates-c-cure-9000-victor/"
    publisher: "ISSSource"
    date: "2026-07-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Under certain circumstances, successful exploitation of this vulnerability could allow an unauthenticated attacker on an adjacent network to achieve arbitrary code execution on the C-CURE 9000, victor application server and victor, as well as connected clients (e.g., workstations of physical security personnel). Such attack could impact physical security controls."
    publisher: "CISA (ICSA-26-204-01, CSAF structured advisory)"
  - quote: "Johnson Controls recommends the following upgrades to address the vulnerable deserialization path: Upgrade to C-CURE 9000 v3.20 or later"
    publisher: "CISA (ICSA-26-204-01, CSAF structured advisory)"
verification: multi-source
sourcing_note: >
  Primary is CISA's own structured CSAF advisory data (fetched directly from the agency's GitHub
  mirror after cisa.gov's HTML page returned HTTP 403 to every transport this run) — a national
  authority publishing on a vendor's advisory it coordinated. ISSSource independently reported
  Johnson Controls' own initial patch release on 2026-07-23, ahead of and separate from CISA's
  coordinated advisory, corroborating the existence and timeline of the vulnerability from a
  second origin rather than merely republishing CISA's text. Flagging one internal inconsistency
  rather than silently resolving
  it: CISA's own CSAF vulnerabilities block tags both CVE-2026-21655 and CVE-2026-21653 with
  CWE-918 (Server-Side Request Forgery), even though CVE-2026-21655's own summary and remediation
  text describe it as reaching code execution through "the vulnerable deserialization path" — a
  CWE-502-class description under a CWE-918 tag. This is CISA's own document disagreeing with
  itself, not a third-party summarisation error.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Isolate every C-CURE 9000 / victor application server on a dedicated network segment and restrict access to TCP/8999 to authorized systems only, then upgrade to C-CURE 9000 v3.20+ / victor Application Server v4.20+ / victor v8.0+ — this is an unauthenticated path to code execution that CISA states can propagate to connected physical-security-personnel workstations, not just the server."
  - "Monitor for .NET deserialization exploit signatures (patterns resembling ysoserial.net gadget chains) in traffic to TCP/8999 on C-CURE 9000/victor application servers, and log SoftwareHouse.CrossFire.Server.exe process activity in detail as a compromise-assessment baseline for any instance that was reachable on an adjacent network before patching."
updates: []
migrated_from: null
---

CISA's ICSA-26-204-01 (Update A, released 2026-08-11, tracking an initial release of 2026-07-23) covers three CVEs in Johnson Controls' physical access-control platform. CVE-2026-21655 (CVSS 3.1: 9.6 Critical, `AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`; CVSS 4.0: 9.4) affects C-CURE 9000 ≤v3.10.1, victor Application Server ≤v4.10, and victor ≤v7.0. Per Johnson Controls' own remediation text, exploitation of "the vulnerable deserialization path" by an unauthenticated, adjacent-network attacker can achieve arbitrary code execution — and the blast radius extends past the server itself: "successful exploitation of this vulnerability could allow an unauthenticated attacker on an adjacent network to achieve arbitrary code execution on the C-CURE 9000, victor application server and victor, as well as connected clients (e.g., workstations of physical security personnel). Such attack could impact physical security controls" ([CISA / Johnson Controls, ICSA-26-204-01, 2026-08-11](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsa-26-204-01.json)). Fixed by upgrading to C-CURE 9000 v3.20+ / victor Application Server v4.20+ / victor v8.0+.

CVE-2026-21653 (same 9.6/9.4 CVSS) affects victor Web <v7.0 and lets an attacker forge server-side HTTP requests to reach internal services. CVE-2026-34496 (8.0/8.7, CWE-250 Execution with Unnecessary Privileges) affects victor Web ≤v7.1 and lets low-privilege users reach unauthorized admin pages (Users, Logs). No known public exploitation is reported for any of the three. Mitigations Johnson Controls names: isolate C-CURE 9000/victor application servers on a dedicated network segment, and restrict access to TCP/8999 to authorized systems only.

Worth flagging rather than silently resolving: CISA's own structured advisory data tags both CVE-2026-21655 and CVE-2026-21653 with CWE-918 (Server-Side Request Forgery), even though CVE-2026-21655's own summary and remediation both describe it as reaching code execution through a deserialization path — a CWE-502-class mechanism under a CWE-918 label. This is CISA's own document disagreeing with itself rather than a summarisation error introduced downstream, and it means a triage process filtering advisories by CWE class alone could misclassify this flaw's actual mechanism.

Physical access-control systems sit at the boundary between IT and physical security across government and critical-infrastructure facilities, so an unauthenticated code-execution path that names "connected clients" as reachable — explicitly including the workstations physical-security staff use — is a case where a network intrusion has a stated potential to become a physical-security failure. **Triage:** the detection anchor is unexpected inbound connections to TCP/8999 on any C-CURE 9000/victor application server, and process activity for `SoftwareHouse.CrossFire.Server.exe` that deviates from its normal service-account behaviour — a deserialization exploit against this component would manifest as that process spawning child processes or making outbound connections it does not make during ordinary operation, which has no benign equivalent on an access-control application server.
