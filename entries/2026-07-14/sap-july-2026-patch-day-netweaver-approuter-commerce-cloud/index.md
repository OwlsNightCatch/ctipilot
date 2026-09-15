---
schema: 1
kind: vulnerability
title: "SAP July 2026 Security Patch Day: three CVSS ≥9.1 flaws in NetWeaver AS ABAP, Approuter and Commerce Cloud — two reachable without authentication"
headline: "SAP patches an unauthenticated Approuter request-smuggling flaw and a Commerce Cloud public-default-credential exposure; NCSC-CH flags all three"
summary: >
  SAP's July 2026 Security Patch Day carries three critical flaws NCSC Switzerland relayed to its constituents:
  CVE-2026-44747 (CVSS 9.9) memory corruption in the NetWeaver AS ABAP kernel; CVE-2026-27690 (CVSS 9.1) an
  unauthenticated HTTP request-smuggling flaw in SAP Approuter (non-Cloud-Foundry); and CVE-2026-44761 (CVSS 9.1)
  a public, hardcoded sample OAuth2 credential left active in SAP Commerce Cloud. No exploitation is reported yet,
  but the Commerce Cloud item is a config exposure a patch alone does not close.
discovered_at: "2026-07-14T20:19:53Z"
event_date: "2026-07-14"
run_id: 2026-07-14T2009Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, patch-available, auth-bypass]
regions: [global, switzerland, europe]
sectors: [public-sector, finance, energy]
entities: []
techniques: [T1190, T1552.001]
affected_products: ["SAP NetWeaver Application Server ABAP", "SAP Approuter", "SAP Commerce Cloud"]
cves:
  - id: CVE-2026-44747
    cvss: "9.9"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "SAP NetWeaver Application Server ABAP kernel (KRNL64NUC/KRNL64UC and later ABAP kernel releases across the 7.22–9.20 span)"
    fixed: "SAP Note 3747367"
  - id: CVE-2026-27690
    cvss: "9.1"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP Approuter in non-Cloud-Foundry deployments (vulnerable bundled package)"
    fixed: "SAP Note 3720138 (updated Approuter package)"
  - id: CVE-2026-44761
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: default-config
    status: [patch-available]
    affected: "SAP Commerce Cloud instances that ran the documented sample OAuth2 configuration script and retained the shipped secret in production"
    fixed: "SAP Note 3753495"
sources:
  - url: "https://onapsis.com/blog/sap-security-patch-day-july-2026/"
    publisher: "Onapsis Research Labs"
    date: "2026-07-14"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12763"
    publisher: "NCSC Switzerland — Cyber Security Hub"
    date: "2026-07-14"
    role: corroborating
  - url: "https://www.securityweek.com/sap-patches-critical-vulnerabilities-in-netweaver-approuter-commerce-cloud/"
    publisher: "SecurityWeek"
    date: "2026-07-14"
    role: corroborating
  - url: "https://support.sap.com/en/my-support/knowledge-base/security-notes-news/july-2026.html"
    publisher: "SAP Support Portal"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The vulnerability affects SAP Approuter deployments in non-Cloud Foundry environments and allows an unauthenticated attacker to send a specially crafted HTTP request that leads to request-response desynchronization."
    publisher: "SecurityWeek"
  - quote: "Exploitation requires that the customer execute the sample script and retain the resulting OAuth2 client in production without replacing the hardcoded secret."
    publisher: "SecurityWeek"
  - quote: "Successful exploitation of the security defect could allow an attacker to access and modify data, and cause system unavailability, SAP security firm Onapsis explains."
    publisher: "SecurityWeek"
verification: multi-source
sourcing_note: "CVE facts corroborated across Onapsis Research Labs (SAP-security specialist), SecurityWeek, NCSC-CH's Cyber Security Hub bulletin and SAP's own July notes page; the per-CVE SAP Notes are login-gated, so Onapsis is the public transcribing authority. No exploitation reported by any party at publication."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Audit SAP Commerce Cloud for CVE-2026-44761: check whether the instance ever ran SAP's documented sample OAuth2 configuration and left the shipped client secret in production; if so, rotate that secret and apply SAP Note 3753495 — the credential is publicly known, so patching without rotating leaves a valid attacker token."
  - "Patch the unauthenticated, network-reachable SAP Approuter request-smuggling flaw (CVE-2026-27690, SAP Note 3720138) on any non-Cloud-Foundry Approuter fronting shared back-ends, and apply the NetWeaver AS ABAP kernel fix (CVE-2026-44747, SAP Note 3747367)."
migrated_from: null
---

SAP's July 2026 Security Patch Day (14 July) carries three critical flaws NCSC Switzerland's Cyber Security Hub relayed directly to Swiss constituents, none with reported exploitation at publication ([NCSC-CH, 2026-07-14](https://security-hub.ncsc.admin.ch/#/posts/12763); [Onapsis Research Labs, 2026-07-14](https://onapsis.com/blog/sap-security-patch-day-july-2026/)). **CVE-2026-44747** (CVSS 9.9) is a memory-corruption flaw in the SAP NetWeaver Application Server ABAP kernel; SecurityWeek characterises successful exploitation as allowing an attacker to access and modify data and cause system unavailability, and SAP's only interim workaround (disabling the affected ICF nodes) is impractical because it breaks SAP GUI for HTML, so patching the kernel is the real mitigation ([SecurityWeek, 2026-07-14](https://www.securityweek.com/sap-patches-critical-vulnerabilities-in-netweaver-approuter-commerce-cloud/)). **CVE-2026-27690** (CVSS 9.1) is an HTTP request-smuggling flaw in SAP Approuter's non-Cloud-Foundry deployments: an unauthenticated request desynchronises the request/response stream on a shared front-end, a primitive usable to poison or hijack another user's request. **CVE-2026-44761** (CVSS 9.1) is a hardcoded sample OAuth2 credential in SAP Commerce Cloud — any customer that ran SAP's own documented sample configuration and never rotated the shipped secret exposes a publicly-known credential an unauthenticated attacker can use to obtain a valid OCC-API access token ([Onapsis Research Labs, 2026-07-14](https://onapsis.com/blog/sap-security-patch-day-july-2026/)).

**Defender takeaway:** for a Swiss/EU public-sector, finance or utilities SAP estate, sequence by reachability, not CVSS: the Approuter smuggling flaw is unauthenticated and network-reachable, so it patches first; the NetWeaver kernel flaw is authenticated but has enormous blast radius given ABAP's centrality; and the Commerce Cloud item is an environment-specific configuration exposure — a publicly-known default credential that a routine note roll-out does not remediate, because the exposed secret must be rotated. **Triage:** the Commerce Cloud exposure is a config-audit question (did we deploy the sample OAuth2 client, and is its secret still the shipped default?), answerable from configuration review rather than telemetry; the Approuter smuggling flaw manifests in front-end HTTP access logs as request/response desynchronisation anomalies (ambiguous content-length/transfer-encoding framing, responses mismatched to the requesting session) on a shared Approuter, distinct from the well-formed request stream of normal traffic.
