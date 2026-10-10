---
schema: 1
kind: vulnerability
title: "Keycloak 26.6.2 — 16 CVEs including OIDC session fixation (CVE-2026-7507), WebAuthn execute-actions token replay (CVE-2026-37982), introspection audience bypass (CVE-2026-37979) and cross-realm IDOR in Authorization Services (CVE-2026-4630)"
headline: "Keycloak 26.6.2 — 16 CVEs including OIDC session fixation (CVE-2026-7507), WebAuthn execute-actions token replay (CVE-2026-37982), introspection audience"
summary: "The Keycloak project shipped 26.6.2 on 2026-05-19, fixing 16 CVEs across identity, authentication and authorisation subsystems; BSI's CERT-Bund issued advisory WID-SEC-2026-1612 on 2026-05-20 classifying the batch as HIGH risk (Keycloak Project, 2026-05-19; BSI CERT-Bund, 2026-05-20)."
discovered_at: "2026-05-21T05:00:05Z"
event_date: 2026-05-20
run_id: 2026-05-21-77cdc4cd
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - auth-bypass
  - patch-available
  - eu-nexus
regions:
  - europe
  - dach
sectors:
  - public-sector
  - healthcare
  - education
entities:
  - "actor:akira"
cves:
  - id: CVE-2026-7507
    cvss: not yet assigned (BSI HIGH classification)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-37982
    cvss: not yet assigned (BSI HIGH classification)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-37979
    cvss: not yet assigned (BSI HIGH classification)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-4630
    cvss: not yet assigned (BSI HIGH classification)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-37978
    cvss: not yet assigned (BSI HIGH classification)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-6856
    cvss: not yet assigned (BSI HIGH classification)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
sources:
  - url: "https://www.keycloak.org/2026/05/keycloak-2662-released"
    publisher: Keycloak Project
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1612"
    publisher: BSI CERT-Bund WID-SEC-2026-1612
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "**Upgrade Keycloak to 26.6.2** with priority on identity-federation deployments (national digital-identity platforms, eHealth federations). The OIDC session-fixation (CVE-2026-7507), WebAuthn execute-actions replay (CVE-2026-37982) and cross-realm IDOR in Authorization Services (CVE-2026-4630) are the operationally-most-dangerous CVEs in the batch (. For Red Hat build of Keycloak, apply the corresponding RHSA advisories on the 26.2.x branch."
migrated_from: briefs/2026-05-21.md
---

The Keycloak project shipped 26.6.2 on 2026-05-19, fixing 16 CVEs across identity, authentication and authorisation subsystems; BSI's CERT-Bund issued advisory WID-SEC-2026-1612 on 2026-05-20 classifying the batch as HIGH risk ([Keycloak Project, 2026-05-19](https://www.keycloak.org/2026/05/keycloak-2662-released); [BSI CERT-Bund, 2026-05-20](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1612)). The operationally highest-priority CVEs for public-sector defenders: **CVE-2026-7507** — session fixation in the OIDC login flow where a crafted `state` parameter before user authentication completes enables account takeover (`T1078` Valid Accounts, `T1556` Modify Authentication Process); **CVE-2026-37982** — execute-actions token replay allowing unauthorised WebAuthn / FIDO2 credential enrollment on a victim account after one user interaction (`T1098.005` Account Manipulation: Device Registration); **CVE-2026-37979** — the OIDC token introspection endpoint `/auth/realms/{realm}/protocol/openid-connect/token/introspect` does not enforce audience restrictions, leaking claims from lightweight access tokens scoped to one client when presented to any introspection-enabled endpoint; **CVE-2026-4630** — cross-resource-server IDOR in the Authorization Services Protection API allowing an authenticated attacker with a token from realm A to read or modify resource permissions in realm B on the same Keycloak instance; **CVE-2026-37978** — cross-role PII leakage via the admin `/auth/admin/realms/{realm}/clients/{client}/evaluate-scopes` endpoint bypassing user-view permissions; **CVE-2026-6856** — acceptable-AAGUID policy bypass in WebAuthn packed self-attestation, allowing enrollment of hardware tokens outside the configured policy list. Fix: upgrade to 26.6.2; Red Hat build of Keycloak (RH-SSO / RHBK) 26.2.x is similarly affected via separate RHSA advisories. **Defender takeaway:** Keycloak is the de-facto standard IAM for EU public-sector and Swiss cantonal / federal identity federation projects, with multiple member-state digital-identity frameworks and national eHealth platforms built on top. Detection concept — admin audit-log entries showing token-introspection responses for mismatched audiences; cross-realm access attempts surfaced as `RESOURCE_TYPE: authorization_resource` in admin event logs; WebAuthn enrollment events with an AAGUID outside the configured policy list.


#### CVE Summary Table

| CVE | Product | CVSS | EPSS | KEV | Exploited | Patch | Source |
|---|---|---|---|---|---|---|---|
| CVE-2026-9082 | Drupal core (PostgreSQL backend) | 20/25 Drupal-scale | not yet scored | No | No (vendor warned of within-hours weaponisation) | 10.4.10 / 10.5.10 / 10.6.9 / 11.1.10 / 11.2.12 / 11.3.10 (2026-05-20) | [Drupal](https://www.drupal.org/sa-core-2026-004) |
| CVE-2026-42822 | Microsoft Azure Local Disconnected Operations (ALDO) | 10.0 | not yet scored | No | No (MSRC: "Exploitation More Likely") | ALDO 2604+ (2026-05-18) | [MSRC](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-42822) |
| CVE-2026-45829 | ChromaDB Python FastAPI server | 10.0 (CVSS 4.0) | not yet scored | No | No (public PoC by HiddenLayer) | None — v1.5.9 unpatched at disclosure | [Hadrian](https://hadrian.io/blog/cve-2026-45829----chromadb-python-server-hands-you-rce-before-it-asks-who-you-are) |
| CVE-2026-7507 | Keycloak (OIDC login session fixation) | not yet assigned (BSI HIGH) | not yet scored | No | No | 26.6.2 (2026-05-19) | [Keycloak](https://www.keycloak.org/2026/05/keycloak-2662-released) |
| CVE-2024-12802 | SonicWall Gen6 SSL-VPN | 9.1 (CVSS 3.1) | not retrieved | No | Yes — Akira-linked, Feb–Mar 2026 | Firmware update insufficient without 6-step LDAP reconfig; Gen6 EoL 2026-04-16 | [Cybersecurity Dive](https://www.cybersecuritydive.com/news/patch-bypass-hackers-exploit-flaw-sonicwall/820600/) |
