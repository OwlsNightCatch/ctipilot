---
schema: 1
kind: vulnerability
horizon: operational
title: "Cisco Crosswork and Secure Workload ship nine CVEs where each identifier stands for a whole class of bugs — six reachable unauthenticated, three at low privilege, and no workaround for any of them"
headline: "One CVE per weakness class means neither platform can be triaged flaw-by-flaw — only by release"
summary: >
  Cisco published two internal-security-review hardening advisories covering Crosswork network
  orchestration and Secure Workload microsegmentation, together carrying nine CVEs, five of them scored
  10.0. The structure is the operationally important part: Cisco grouped multiple internally found bugs by
  weakness class and assigned one CVE per class, scored at the worst underlying bug, so no individual flaw
  can be assessed and remediation is by release rather than by finding. Reading the vendor's own CVSS
  vectors, six of the nine need no authentication and three need only low privilege — not the uniform
  unauthenticated set the score list suggests. Cisco states it is not aware of malicious use and that no
  workarounds exist. On Secure Workload SaaS, Cisco has upgraded the cluster but the agent and connector
  software remains the customer's to patch.
discovered_at: "2026-08-22T05:01:00Z"
event_date: "2026-08-19"
run_id: 2026-08-22T0410Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, sqli, auth-bypass, info-disclosure, path-traversal, pre-auth, patch-available]
regions: [global]
sectors: [telco, public-sector]
entities: []
techniques: [T1190, T1552, T1078]
affected_products: ["Cisco Crosswork Data Gateway", "Cisco Crosswork Network Controller", "Cisco Crosswork Planning", "Cisco Crosswork Workflow Manager", "Cisco Secure Workload"]
cves:
  - id: CVE-2026-20030
    cvss: "10.0"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier"
    fixed: "7.2.1-SP / 2.1.1-SP"
  - id: CVE-2026-20357
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier"
    fixed: "7.2.1-SP / 2.1.1-SP"
  - id: CVE-2026-20358
    cvss: "10.0"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier"
    fixed: "7.2.1-SP / 2.1.1-SP"
  - id: CVE-2026-20359
    cvss: "9.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Cisco Crosswork 7.2.1 and earlier / 2.1.1 and earlier"
    fixed: "7.2.1-SP / 2.1.1-SP"
  - id: CVE-2026-20315
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20317
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20318
    cvss: "9.6"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20231
    cvss: "9.9"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
  - id: CVE-2026-20319
    cvss: "7.5"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Cisco Secure Workload 3.10 and earlier; 4.0"
    fixed: "3.10.9.1; 4.0.4.16"
sources:
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh"
    publisher: "Cisco PSIRT"
    date: "2026-08-19"
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP"
    publisher: "Cisco PSIRT"
    date: "2026-08-19"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0323"
    publisher: "NCSC-NL"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Cisco has grouped these issues by their underlying vulnerability class - Common Weakness Enumeration (CWE) - and assigned a single Common Vulnerabilities and Exposures Identifier (CVE ID) to each CWE grouping."
    publisher: "Cisco PSIRT"
  - quote: "The CVSS score that is assigned to each CVE ID represents the maximum potential severity of the single most impactful underlying vulnerability within that specific CWE category."
    publisher: "Cisco PSIRT"
  - quote: "There are no workarounds that address these vulnerabilities."
    publisher: "Cisco PSIRT"
  - quote: "The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerabilities that are described in this advisory."
    publisher: "Cisco PSIRT"
  - quote: "The Cluster, Agent, and Connector software of Cisco Secure Workload need to be upgraded to resolve all of these vulnerabilities. For SaaS deployments, Cisco has upgraded the Cluster software, and customers need to upgrade only the Agent and Connector software."
    publisher: "Cisco PSIRT"
verification: multi-source
sourcing_note: >
  Cisco's own advisories are the primary and NCSC-NL's independently published record for the Secure
  Workload cluster carries the identical per-CVE vectors, which is corroboration of the numbers rather
  than an independent assessment of the flaws — one assessor, so credibility 2. The per-CVE CVSS vectors
  are not in the advisories' HTML tables, which show only a score per weakness grouping; they were read
  from each advisory's own CSAF 2.0 export, which is what establishes that six of the nine carry PR:N and
  three carry PR:L. Recency: both advisories were first published 2026-08-19 at 16:00 UTC, inside the
  window of the previous fire on 2026-08-20, which did not surface them; the Crosswork advisory was
  revised to Version 2.0 Final on 2026-08-21 and Switzerland's NCSC relayed the cycle the same day, which
  is how it surfaced here. It is published as a recovered miss rather than as fresh news, and the event
  date records the true first publication.
confidence: high
update_of: null
references: ["2026-08-08/cisco-ios-xe-august-2026-hardening-release-cwe-grouped-cves"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade Crosswork Data Gateway, Network Controller, Planning and Workflow Manager to 7.2.1-SP or 2.1.1-SP, and Secure Workload to 3.10.9.1 or 4.0.4.16 — Cisco states there is no workaround for any of the nine, so patching is the only remediation. On Secure Workload SaaS, do not treat this as handled: Cisco has upgraded the cluster software but the agent and connector software is still the customer's to upgrade."
migrated_from: null
---

Cisco published two hardening advisories out of internal security review on 2026-08-19 covering Crosswork — its network orchestration, planning and workflow platform — and Secure Workload, its workload microsegmentation product. Together they carry nine CVEs, five of them scored 10.0 and two more 9.9 ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh), [Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP)). The number to read past is the score; the structure behind it is what changes a defender's options. Cisco states it grouped the issues by underlying weakness class and assigned one CVE identifier per grouping, and that each score represents the maximum potential severity of the single most impactful underlying bug within that class ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh)). One identifier can therefore stand for several distinct bugs, and no individual flaw is assessable from the advisory — the estate is triaged by release, not by finding. This pipeline recorded the identical construction in Cisco's August IOS XE hardening release, so it now reads as a settled disclosure practice on internally found bug batches rather than a one-off.

The authentication picture is more mixed than a list of tens implies, and the vendor's own vectors settle it. On Crosswork, CVE-2026-20030 (SQL injection), CVE-2026-20357 (missing authentication for a critical function) and CVE-2026-20358 (external control of a file path) all carry `PR:N` at 10.0, while CVE-2026-20359 (insufficiently protected credentials, 9.9) carries `PR:L` and therefore needs an existing low-privilege account. On Secure Workload, CVE-2026-20315 (improper access control) and CVE-2026-20317 (improper authentication) are `PR:N` at 10.0 and CVE-2026-20319 (a memory-buffer restriction failure, 7.5, availability impact only) is `PR:N`, while CVE-2026-20231 (injection, 9.9) and CVE-2026-20318 (improper input validation, 9.6) are both `PR:L`. NCSC-NL's independently published record for the Secure Workload cluster carries the same five vectors ([NCSC-NL, 2026-08-21](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0323)). Six unauthenticated and three at low privilege is not a reassuring split: low privilege on an orchestration or microsegmentation control plane means any read-only API consumer or delegated operator role is a sufficient foothold.

Cisco is explicit that it is not aware of any public announcements or malicious use of these vulnerabilities, and equally explicit that there are no workarounds that address them ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP)). Two further details change the work involved. Cisco credits the discovery to internal security testing "using existing testing processes as well as frontier AI models" ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh)) — the second Cisco hardening batch this month attributed partly to model-assisted internal review, which is a plausible explanation for why these arrive in classes rather than singly. And on Secure Workload SaaS, the fix is not fully server-side: Cisco states the cluster, agent and connector software all need upgrading and that for SaaS deployments it has upgraded the cluster while customers must still upgrade the agent and connector ([Cisco PSIRT, 2026-08-19](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP)). A SaaS tenant that assumed its provider had closed this out has client-side work outstanding.

Because the advisories describe weakness classes rather than reachable interfaces, there is no honest per-flaw detection guidance to give and this entry does not invent any. What is available is exposure reduction and the audit trail these platforms already produce: establish which interfaces of each product answer from outside the management network at all, and treat the low-privilege accounts on both platforms as part of the blast radius rather than as a trust boundary — service accounts and delegated operator roles on an orchestration platform are the foothold three of these nine flaws need. Both products' own audit logging is the place a defender would see the consequence of exploitation rather than the attempt: configuration writes, policy changes and credential reads that do not correspond to a change request.
