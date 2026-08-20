---
schema: 1
kind: vulnerability
horizon: operational
title: "Oracle's August 2026 Critical Security Patch Update carries three unauthenticated CVSS 10.0 flaws — one of them in the LDAP server of Oracle Internet Directory"
headline: "943 patches in a monthly release, and the ones that decide the sequencing are the three needing no credential and no user interaction at all"
summary: >
  Oracle published its August 2026 Critical Security Patch Update — its monthly release, distinct from the
  quarterly cumulative Critical Patch Update — on 2026-08-18 with 943 new security patches, and Switzerland's
  NCSC relayed it to its own constituency the following day. Three flaws in the release carry a
  CVSS 3.1 base score of 10.0 with Privileges Required and User Interaction both None in Oracle's own risk
  matrix: CVE-2026-61241 in the LDAP server of Oracle Internet Directory, and CVE-2026-70880 and CVE-2026-70921
  in Hyperion Data Relationship Management and Hyperion Financial Management. Fusion Middleware alone accounts
  for 262 patches of which Oracle states 182 may be remotely exploitable without authentication, and E-Business
  Suite for 120 of which 27 may be. No flaw in this cycle is reported as exploited by any source.
discovered_at: "2026-08-20T04:44:00Z"
event_date: "2026-08-18"
run_id: 2026-08-20T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, auth-bypass, patch-available, identity]
regions: [global, europe, switzerland]
sectors: [public-sector, finance, healthcare, energy]
entities: []
techniques: [T1190]
affected_products: ["Oracle Internet Directory", "Oracle Hyperion Data Relationship Management", "Oracle Hyperion Financial Management", "Oracle E-Business Suite", "Oracle WebLogic Server", "Oracle Fusion Middleware"]
cves:
  - id: CVE-2026-61241
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0 — OID LDAP Server, reachable over LDAP"
    fixed: "August 2026 Critical Security Patch Update"
  - id: CVE-2026-70880
    cvss: "10.0"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Hyperion Data Relationship Management 11.2.25.0.000 — Access and security component, reachable over TCP"
    fixed: "August 2026 Critical Security Patch Update"
  - id: CVE-2026-70921
    cvss: "10.0"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Hyperion Financial Management 11.2.25.0.000 — Security component, reachable over TLS"
    fixed: "August 2026 Critical Security Patch Update"
  - id: CVE-2026-60782
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3-12.2.15 — Oracle Payments, File Transmission component, reachable over HTTP"
    fixed: "August 2026 Critical Security Patch Update"
  - id: CVE-2026-70926
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3-12.2.15 — Oracle Workflow, Workflow Notification Mailer component, reachable over SMTP"
    fixed: "August 2026 Critical Security Patch Update"
  - id: CVE-2026-60672
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server — Core component, reachable over T3 and IIOP"
    fixed: "August 2026 Critical Security Patch Update"
sources:
  - url: "https://www.oracle.com/security-alerts/cspuaug2026.html"
    publisher: "Oracle"
    date: "2026-08-18"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12862"
    publisher: "NCSC Switzerland — Cyber Security Hub"
    date: "2026-08-19"
    role: corroborating
  - url: "https://www.securityweek.com/943-patches-rolled-out-with-oracles-august-2026-security-update/"
    publisher: "SecurityWeek"
    date: "2026-08-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This Critical Security Patch Update contains 943 new security patches across the product families listed below."
    publisher: "Oracle"
  - quote: "Oracle continues to periodically receive reports of attempts to maliciously exploit vulnerabilities for which Oracle has already released security patches. In some instances, it has been reported that attackers have been successful because targeted customers had failed to apply available Oracle patches."
    publisher: "Oracle"
verification: multi-source
sourcing_note: >
  Every per-flaw fact here — the identifiers, the CVSS 3.1 base scores, the affected components and protocols,
  the affected version strings, and the Privileges Required and User Interaction values — is read from Oracle's
  own risk matrices on the advisory page rather than from a roundup. The per-family patch counts and the
  unauthenticated-exploitability counts are Oracle's own preamble text for each family. No source fetched this
  run reports exploitation of any CVE in this cycle; NCSC-CH's relay records exploitation status as unknown for
  the whole batch and carries no CVE-level detail of its own.
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
  - "Sequence this release by unauthenticated network exposure rather than by product owner — and note it is Oracle's monthly Critical Security Patch Update, not the quarterly cumulative one, so the next release is 15 September: the three flaws Oracle scores 10.0 — CVE-2026-61241 in the Oracle Internet Directory LDAP server, CVE-2026-70880 and CVE-2026-70921 in Hyperion Data Relationship Management and Financial Management — all carry Privileges Required: None and User Interaction: None in Oracle's own matrix, so any instance of those three reachable from a user network or the internet is the first patch, ahead of the higher-count families."
migrated_from: null
---

Oracle published its August 2026 Critical Security Patch Update on 2026-08-18, stating that it "contains 943 new security patches across the product families listed below" ([Oracle, 2026-08-18](https://www.oracle.com/security-alerts/cspuaug2026.html)); Switzerland's NCSC put it in front of its own constituency the next day ([NCSC-CH, 2026-08-19](https://security-hub.ncsc.admin.ch/#/posts/12862)). This is worth naming precisely, because the release type sets the patch window: a Critical Security Patch Update is Oracle's monthly release — the page states that security patches ship on the third Tuesday of each month and lists 15 September 2026 as the next one — and it is a distinct thing from the quarterly cumulative Critical Patch Update it complements, the next of which is 20 October 2026 ([Oracle, 2026-08-18](https://www.oracle.com/security-alerts/cspuaug2026.html)). An estate that treats this as the quarterly cycle will both misjudge how soon the next batch lands and, more importantly, wait a quarter for fixes that are already out. Most of a release this size is still routine maintenance; what takes a handful of items past routine is their own mechanics, and those are not in the families with the largest counts.

Three CVEs in the release carry a CVSS 3.1 base score of 10.0, and in Oracle's own risk matrices all three record Privileges Required as None, User Interaction as None, and Scope as Changed — an anonymous, single-request path to full compromise of the component and beyond it. CVE-2026-61241 is in the OID LDAP Server component of Oracle Internet Directory, reachable over LDAP, affecting versions 12.2.1.4.0 and 14.1.2.1.0. The other two, CVE-2026-70880 and CVE-2026-70921, are in the Access and security component of Hyperion Data Relationship Management (reachable over TCP) and the Security component of Hyperion Financial Management (reachable over TLS), both at 11.2.25.0.000 ([Oracle, 2026-08-18](https://www.oracle.com/security-alerts/cspuaug2026.html)). The Internet Directory flaw is the one that should move first in a public-sector estate: an LDAP directory server is identity infrastructure, it is normally reachable from every application that authenticates against it, and a scope-changed compromise of it is not contained to the directory.

The concentration behind those three is what makes the sequencing work non-trivial. Oracle records 262 new patches for Fusion Middleware, of which it states 182 "may be remotely exploitable without authentication", and 120 for E-Business Suite, of which 27 may be; Hyperion carries 262 patches with 107 in that category ([Oracle, 2026-08-18](https://www.oracle.com/security-alerts/cspuaug2026.html)). Within E-Business Suite the two highest-scored unauthenticated flaws sit on inbound processing paths that an internet-facing deployment exposes by design — CVE-2026-60782 in the File Transmission component of Oracle Payments over HTTP, and CVE-2026-70926 in the Workflow Notification Mailer over SMTP, both 9.8. In Fusion Middleware, CVE-2026-60672 is an unauthenticated 9.8 in the WebLogic Server core reachable over T3 and IIOP, a protocol pair with a long history of public exploit work following Oracle releases.

No source fetched this run reports exploitation of any individual flaw in this cycle, and NCSC-CH's relay records exploitation status as unknown for the batch as a whole ([NCSC-CH, 2026-08-19](https://security-hub.ncsc.admin.ch/#/posts/12862)). Oracle's own advisory makes the point that matters more than any single score: it "continues to periodically receive reports of attempts to maliciously exploit vulnerabilities for which Oracle has already released security patches. In some instances, it has been reported that attackers have been successful because targeted customers had failed to apply available Oracle patches" ([Oracle, 2026-08-18](https://www.oracle.com/security-alerts/cspuaug2026.html)). For estates that cannot patch 943 items at once, the useful hardening step in the meantime is network placement rather than version: T3, IIOP, RMI, CORBA and LDAP listeners on middleware and directory hosts have no business being reachable from a general-purpose user network, and restricting them removes the reachability half of every unauthenticated flaw in this release regardless of which one is patched first.

**Defender takeaway:** treat this release as three out-of-band items wrapped in a routine monthly one. Patch the two Hyperion components and Oracle Internet Directory on the schedule you would give an emergency advisory, then work the rest of Fusion Middleware and E-Business Suite by whether the affected component listens on a network anyone untrusted can reach. The absence of an exploitation report for a flaw that needs no credential and no interaction is a statement about the present, not a property of the flaw.
