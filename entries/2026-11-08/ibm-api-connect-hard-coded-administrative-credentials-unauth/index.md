---
schema: 1
kind: vulnerability
title: "IBM API Connect: hard-coded administrative credentials, unauthenticated command injection and authentication bypass among the CVEs fixed in v12.1.1.3 and 10.0.8.13"
headline: "IBM API Connect: hard-coded admin credentials and pre-auth code execution fixed in v12.1.1.3 and 10.0.8.13"
summary: >
  IBM's two security bulletins of 2026-11-05 for API Connect fix, among many CVEs, flaws that need no privileges at CVSS 3.1 9.8: hard-coded
  credentials that give a remote attacker full administrative control (CVE-2026-17360, v12 only), OS command injection and path traversal
  to arbitrary code execution, an authentication bypass through improper signature verification, token issuance for other users and missing
  authorization over tenants. Affected are API Connect V12 on-premises v12.1.0.0 to v12.1.1.2 (fixed in v12.1.1.3) and V10.0.8.0 to 10.0.8.12
  (fixed in 10.0.8.13); IBM lists no workaround and no source reports exploitation.
discovered_at: "2026-11-08T14:16:00Z"
updated_at: null
event_date: "2026-11-05"
run_id: 2026-11-08T1309Z-audit
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, pre-auth, patch-available]
regions: [global]
sectors: []
entities: ["product:ibm-api-connect"]
techniques: [T1190, T1078.001, T1059]
affected_products: ["IBM API Connect"]
cves:
  - id: CVE-2026-17360
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "API Connect V12 on-premises v12.1.0.0 to v12.1.1.2"
    fixed: "v12.1.1.3; IBM lists no workaround"
  - id: CVE-2026-17403
    cvss: "9.0 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "API Connect V12 on-premises v12.1.0.0 to v12.1.1.2; API Connect V10.0.8.0 to V10.0.8.12"
    fixed: "v12.1.1.3; 10.0.8.13"
  - id: CVE-2026-17408
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "API Connect V12 on-premises v12.1.0.0 to v12.1.1.2; API Connect V10.0.8.0 to V10.0.8.12"
    fixed: "v12.1.1.3; 10.0.8.13"
  - id: CVE-2026-17340
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "API Connect V12 on-premises v12.1.0.0 to v12.1.1.2"
    fixed: "v12.1.1.3"
  - id: CVE-2026-17301
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "API Connect V12 on-premises v12.1.0.0 to v12.1.1.2; API Connect V10.0.8.0 to V10.0.8.12"
    fixed: "v12.1.1.3; 10.0.8.13"
  - id: CVE-2026-16720
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "API Connect V12 on-premises v12.1.0.0 to v12.1.1.2; API Connect V10.0.8.0 to V10.0.8.12"
    fixed: "v12.1.1.3; 10.0.8.13"
  - id: CVE-2026-17362
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "API Connect V12 on-premises v12.1.0.0 to v12.1.1.2"
    fixed: "v12.1.1.3"
sources:
  - url: "https://www.ibm.com/support/pages/node/7295635"
    publisher: "IBM Support (Security Bulletin, API Connect V12 on-premises)"
    date: "2026-11-05"
    role: primary
  - url: "https://www.ibm.com/support/pages/node/7295637"
    publisher: "IBM Support (Security Bulletin, API Connect V10.0.8)"
    date: "2026-11-05"
    role: primary
closed_sources: []
evidence:
  - quote: "IBM API Connect could allow a remote attacker to gain full administrative control due to the use of hard-coded credentials."
    publisher: "IBM Support (Security Bulletin, API Connect V12 on-premises)"
    source_url: "https://www.ibm.com/support/pages/node/7295635"
  - quote: "IBM API Connect could allow a remote attacker to execute arbitrary code due to improper neutralization of special elements in an OS command."
    publisher: "IBM Support (Security Bulletin, API Connect V12 on-premises)"
    source_url: "https://www.ibm.com/support/pages/node/7295635"
  - quote: "IBM strongly recommends addressing the vulnerability now by upgrading to v12.1.1.3"
    publisher: "IBM Support (Security Bulletin, API Connect V12 on-premises)"
    source_url: "https://www.ibm.com/support/pages/node/7295635"
verification: single-source
sourcing_note: >
  IBM's two bulletins are the vendor's own statements and the CVSS source for every row; neither says which API Connect component a flaw sits
  in or mentions exploitation. The CVE records here are a selection of the unauthenticated rows, not the full list.
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
  - "Upgrade every IBM API Connect V12 on-premises installation to v12.1.1.3 and every V10.0.8 installation to 10.0.8.13, those reachable from the internet first."
updates: []
migrated_from: null
---

IBM's security bulletins of 2026-11-05 for API Connect, its API management platform, list more than two hundred CVEs, and 18 rows of the v12 bulletin need no privileges at CVSS 3.1 9.0 or higher; among them is CVE-2026-17360, through which a remote attacker can gain full administrative control because of hard-coded credentials, scored CVSS 3.1 9.8 on the v12 bulletin ([IBM, 2026-11-05](https://www.ibm.com/support/pages/node/7295635)). The same bulletin lists, each at 9.8 with no privileges or user interaction, OS command injection to arbitrary code execution (CVE-2026-17408), path traversal to arbitrary code execution (CVE-2026-17340), an authentication bypass through improper verification of a cryptographic signature (CVE-2026-17301), valid access tokens for other users because authentication against a connected directory service is not sufficiently enforced (CVE-2026-16720), and missing authorization that lets a remote attacker create, modify or delete tenants (CVE-2026-17362); a second hard-coded credential row, CVE-2026-17403, scores 9.0 ([IBM, 2026-11-05](https://www.ibm.com/support/pages/node/7295635)). The V10.0.8 bulletin carries CVE-2026-17403, CVE-2026-17408, CVE-2026-17301 and CVE-2026-16720 as well ([IBM, 2026-11-05](https://www.ibm.com/support/pages/node/7295637)).

API Connect V12 on-premises v12.1.0.0 to v12.1.1.2 is fixed in v12.1.1.3 and V10.0.8.0 to 10.0.8.12 in 10.0.8.13; IBM lists no workaround or mitigation on either page ([IBM, 2026-11-05](https://www.ibm.com/support/pages/node/7295635); [IBM, 2026-11-05](https://www.ibm.com/support/pages/node/7295637)). Neither bulletin mentions exploitation, and neither says which component each flaw sits in.

**Exposure:** an API Connect installation in the listed ranges that an attacker can reach over the network; the bulletins give no per-component split, so every reachable API Connect endpoint counts ([IBM, 2026-11-05](https://www.ibm.com/support/pages/node/7295635)).

**Detection:** in API Connect and reverse-proxy access logs, administrative or tenant-management actions without a preceding authenticated session from an expected administrator, and access tokens issued to identities that did not authenticate against the directory; in process telemetry on the API Connect hosts, shells or interpreters spawned by the API Connect service accounts (inferences from the flaw descriptions).

**Defender takeaway:** treat these as out-of-cycle updates, because the worst rows need neither credentials nor user interaction and IBM offers no workaround; after upgrading, check administrator, tenant and token-issuance events for activity nobody can account for, because patching removes the credential, not an account or token an attacker already created.
