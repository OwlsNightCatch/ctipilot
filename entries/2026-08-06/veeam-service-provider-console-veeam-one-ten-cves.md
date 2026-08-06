---
schema: 1
kind: vulnerability
horizon: operational
title: "Veeam Service Provider Console and Veeam ONE — ten CVEs, headed by an unauthenticated CVSS 10.0 remote code execution on the Veeam ONE agent host"
headline: "Veeam patches ten flaws across the console that manages backups and the platform that monitors them"
summary: >
  Veeam's 2026-08-04 security release fixes ten vulnerabilities across two co-deployed products, carried to European
  constituencies by CERT-FR on 2026-08-05; NCSC-NL's advisory of the same date covers only the four Service Provider
  Console flaws. In Veeam ONE the standout is CVE-2026-64633, an
  unauthenticated remote code execution on the agent host rated CVSS v4.0 10.0; in Veeam Service Provider Console,
  CVE-2026-58073 (9.5) lets an unauthenticated attacker impersonate a managed agent and obtain its credentials and
  CVE-2026-58072 (9.0) gives arbitrary file write on the management server leading to code execution. All ten are
  fixed in Veeam ONE 13.1.0.7034 and Service Provider Console 9.3.0.35057. No party reports exploitation, but these
  are the management and monitoring planes sitting over backup infrastructure, which is the estate ransomware
  operators attack before they encrypt.
discovered_at: "2026-08-06T04:11:48Z"
event_date: "2026-08-04"
run_id: 2026-08-06T0411Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, auth-bypass, sqli, patch-available]
regions: [global]
sectors: [technology, public-sector, healthcare, finance]
entities: []
techniques: [T1190, T1068]
affected_products: ["Veeam Service Provider Console", "Veeam ONE"]
cves:
  - id: CVE-2026-64633
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Veeam ONE 13.0.2.6723 and all earlier version 13 builds"
    fixed: "13.1.0.7034"
  - id: CVE-2026-58073
    cvss: "9.5"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Veeam Service Provider Console 9.2.1.33875 and all earlier version 9 builds"
    fixed: "9.3.0.35057"
  - id: CVE-2026-58072
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Veeam Service Provider Console 9.2.1.33875 and all earlier version 9 builds"
    fixed: "9.3.0.35057"
  - id: CVE-2026-58075
    cvss: "8.7"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Veeam ONE 13.0.2.6723 and all earlier version 13 builds"
    fixed: "13.1.0.7034"
  - id: CVE-2026-58067
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Veeam Service Provider Console 9.2.1.33875 and all earlier version 9 builds"
    fixed: "9.3.0.35057"
  - id: CVE-2026-58074
    cvss: "8.6"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status: [patch-available]
    affected: "Veeam ONE 13.0.2.6723 and all earlier version 13 builds"
    fixed: "13.1.0.7034"
  - id: CVE-2026-64631
    cvss: "8.6"
    epss: null
    type: sqli
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Veeam ONE 13.0.2.6723 and all earlier version 13 builds"
    fixed: "13.1.0.7034"
  - id: CVE-2026-64634
    cvss: "8.4"
    epss: null
    type: priv-esc
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "Veeam ONE 13.0.2.6723 and all earlier version 13 builds"
    fixed: "13.1.0.7034"
  - id: CVE-2026-58071
    cvss: "8.2"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Veeam Service Provider Console 9.2.1.33875 and all earlier version 9 builds"
    fixed: "9.3.0.35057"
  - id: CVE-2026-64630
    cvss: "5.3"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Veeam ONE 13.0.2.6723 and all earlier version 13 builds"
    fixed: "13.1.0.7034"
sources:
  - url: "https://www.veeam.com/kb4892"
    publisher: "Veeam (KB4892)"
    date: "2026-08-04"
    role: primary
  - url: "https://www.veeam.com/kb4893"
    publisher: "Veeam (KB4893)"
    date: "2026-08-04"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0968/"
    publisher: "CERT-FR"
    date: "2026-08-05"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0276"
    publisher: "NCSC-NL"
    date: "2026-08-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A vulnerability allowing remote unauthenticated code execution on the agent host."
    publisher: "Veeam (KB4892)"
  - quote: "impersonate a managed agent and obtain that agent's credentials"
    publisher: "Veeam (KB4893)"
verification: multi-source
sourcing_note: >
  Veeam is the CNA and sole assessor here; the CERT-FR and NCSC-NL advisories restate its bulletins for their own
  constituencies rather than assessing the flaws independently, so the credibility rating reflects one assessor with
  several publishers. Their coverage is not equivalent: CERT-FR carries both products and all ten CVEs, while
  NCSC-2026-0276 is scoped to Service Provider Console and its four CVEs only. Every CVSS v4.0 score, affected build and fixed build in this entry is transcribed from
  the per-CVE rows of Veeam's own two KB articles rather than from any roundup.
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
  - "Upgrade Veeam ONE to 13.1.0.7034 and Veeam Service Provider Console to 9.3.0.35057 — partial patching does not help here, because both products' full CVE sets are fixed only in those single builds and the 10.0 agent-host flaw needs no credentials."
migrated_from: null
---

Veeam published two security bulletins on 2026-08-04 covering ten vulnerabilities. CERT-FR carried both products and the full set the following day ([CERT-FR, 2026-08-05](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0968/)); NCSC-NL's advisory of the same date covers only Service Provider Console and its four CVEs, and does not mention Veeam ONE or the 10.0 agent-host flaw at all ([NCSC-NL, 2026-08-05](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0276)) — worth knowing if your patch intake is driven by a single national feed. In Veeam ONE, CVE-2026-64633 is described by the vendor as allowing remote unauthenticated code execution on the agent host and is scored CVSS v4.0 10.0 with no privileges and no user interaction required ([Veeam, 2026-08-04](https://www.veeam.com/kb4892)). Its siblings in the same product are CVE-2026-58075 (8.7), an unauthenticated arbitrary file read from the host that the vendor says can be leveraged to escalate privileges locally; CVE-2026-58074 (8.6), arbitrary code execution on the server by a high-privileged user; CVE-2026-64631 (8.6), SQL injection by a low-privileged user extracting database contents; CVE-2026-64634 (8.4), local privilege escalation into the Reporter service context; and CVE-2026-64630 (5.3), retrieval of report data outside a shared link's scope ([Veeam, 2026-08-04](https://www.veeam.com/kb4892)). All affect Veeam ONE 13.0.2.6723 and all earlier version 13 builds, and all are resolved in 13.1.0.7034 ([Veeam, 2026-08-04](https://www.veeam.com/kb4892)).

In Veeam Service Provider Console, CVE-2026-58073 (CVSS v4.0 9.5) allows an unauthenticated attacker to impersonate a managed agent and obtain that agent's credentials — though the vendor's own vector records high attack complexity, which is the one meaningful brake on the four ([Veeam, 2026-08-04](https://www.veeam.com/kb4893)). CVE-2026-58072 (9.0) permits arbitrary file write on the management server leading to remote code execution; CVE-2026-58067 (8.7) lets an unauthenticated attacker exhaust host memory for denial of service; and CVE-2026-58071 (8.2) allows an unauthenticated attacker to reach the proxied appliance API as Portal Administrator during a short window after an administrator session begins ([Veeam, 2026-08-04](https://www.veeam.com/kb4893)). These affect Service Provider Console 9.2.1.33875 and all earlier version 9 builds, resolved in 9.3.0.35057 ([Veeam, 2026-08-04](https://www.veeam.com/kb4893)).

No party — vendor or CERT — reports exploitation of any of the ten. The reason this still warrants attention ahead of the ordinary patch cycle is what the two products are: Service Provider Console is the multi-tenant management plane through which service providers administer customer backup estates, and Veeam ONE is the monitoring platform over that same estate. An agent-credential impersonation flaw on the former and an unauthenticated code-execution flaw on the latter both land on infrastructure that holds broad, standing access into the systems an organisation would rely on to recover — and backup infrastructure is a recognised pre-encryption target rather than a bystander.

**Defender takeaway:** the exposure question is narrower than the CVE count suggests. Establish which Veeam ONE agent hosts and Service Provider Console instances are reachable from outside the management segment at all, since the two flaws that need no credentials (CVE-2026-64633 and CVE-2026-58073) are the ones whose reachability decides your risk; the post-authentication and administrator-context flaws in the same release matter chiefly as escalation once someone is already inside. In telemetry, the behaviour worth watching on these hosts is the monitoring or console service process spawning command interpreters or writing to paths outside its own application directories, and management-plane authentication events for agent identities arriving from addresses that are not the corresponding managed host.
