---
schema: 1
kind: vulnerability
horizon: strategic
weekly_section: weekly-vuln-rollup
title: "Keycloak 26.6.3 — 16 CVEs in the EU public sector's reference IAM, led by token-exchange privilege escalation and SSRF"
headline: "Keycloak 26.6.3 — 16 CVEs in the EU public sector's reference IAM, led by token-exchange privilege escalation and SSRF"
summary: "Released 2026-06-04 (Keycloak; deep-dived 2026-06-07 daily). CVE-2026-9704 is a privilege escalation in OAuth 2.0 token exchange: a low-privilege client omits the subject_token parameter and Keycloak issues a token under the requesting client's identity rather than rejecting the malformed request, enabling …"
discovered_at: "2026-06-01T05:00:06Z"
event_date: null
run_id: 2026-W23-9118e7bd
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - auth-bypass
  - priv-esc
  - patch-available
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
entities: []
cves:
  - id: CVE-2026-9704
    cvss: n/a
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-4874
    cvss: n/a
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
sources:
  - url: "https://www.keycloak.org/2026/06/keycloak-2663-released"
    publisher: Keycloak 26.6.3 release notes
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W23.md
---

Released 2026-06-04 ([Keycloak](https://www.keycloak.org/2026/06/keycloak-2663-released); deep-dived 2026-06-07 daily). **CVE-2026-9704** is a privilege escalation in OAuth 2.0 token exchange: a low-privilege client omits the `subject_token` parameter and Keycloak issues a token under the requesting client's identity rather than rejecting the malformed request, enabling lateral movement between service identities (`T1550.001`). **CVE-2026-4874** turns the OIDC token endpoint into an SSRF primitive, giving an attacker who can reach the endpoint a pivot into internal services Keycloak is permitted to contact. Additional CVEs of note: CVE-2026-8830 (missing server-side WebAuthn attestation validation — undermines phishing-resistant MFA enrolment assurance); CVE-2026-9802 (restart resets `startupTime`, allowing replay of rotated refresh tokens). No in-the-wild exploitation reported; patch-priority for any internet-reachable Keycloak underpinning e-government SSO or SAML federation. Detection: alert on `token_exchange` events in the Keycloak event log where `subject_token` is absent but a token is issued; watch for outbound connections from the Keycloak service host to non-allow-listed internal addresses correlated with token-endpoint requests.
