---
schema: 1
kind: vulnerability
horizon: operational
title: "Keycloak 26.6.3: privilege escalation via OAuth token-exchange and SSRF in the EU public sector's reference identity platform"
headline: "Keycloak 26.6.3: privilege escalation via OAuth token-exchange and SSRF in the EU public sector's reference identity platform"
summary: "Keycloak 26.6.3 patches 16 CVEs in the EU public sector's reference IAM, led by a token-exchange privilege escalation. CVE-2026-9704 lets a low-privilege client silently omit the subject_token parameter in an OAuth 2.0 token exchange so Keycloak issues a token under the requesting client's identity, and CVE-2026-4874 turns the OIDC token endpoint into an SSRF primitive. No known in-the-wild exploitation; patch-priority for any internet-reachable Keycloak underpinning e-government SSO (Keycloak, 2026-06-04). Full treatment in § 5."
discovered_at: "2026-06-07T05:00:05Z"
event_date: 2026-06-04
run_id: 2026-06-07-0885f123
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - auth-bypass
  - priv-esc
  - patch-available
regions:
  - europe
  - global
sectors:
  - public-sector
  - finance
  - healthcare
  - education
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
  - id: CVE-2026-8830
    cvss: n/a
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9802
    cvss: n/a
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9792
    cvss: n/a
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-37977
    cvss: n/a
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
sources:
  - url: "https://www.keycloak.org/2026/06/keycloak-2663-released"
    publisher: Keycloak — 26.6.3 release notes
    role: primary
closed_sources: []
evidence:
  - quote: "[CVE-2026-9704] Privilege escalation via silent subject_token removal in token exchange"
    publisher: Keycloak
  - quote: "[CVE-2026-4874] Server-Side Request Forgery via OIDC token endpoint manipulation"
    publisher: Keycloak
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: identity-infra
org_triage: null
watchlist_hit: false
actions:
  - "**Patch Keycloak to 26.6.3** on any internet-reachable or e-government identity deployment (§ 5). If the token-exchange feature is not in use, disable its feature flag to remove the `CVE-2026-9704` path entirely; enforce egress filtering from the Keycloak host to blunt the `CVE-2026-4874` SSRF; re-validate WebAuthn enrolment attestation policy."
migrated_from: briefs/2026-06-07.md
---

**Why this is the deep dive.** Keycloak is the open-source IAM that underpins SSO, SAML and OIDC federation across a large share of EU public-sector and EU-institution deployments, and it is the upstream for the Red Hat build of Keycloak common in DACH government estates. On 2026-06-04 the project released 26.6.3, fixing 16 CVEs as documented in the release notes ([Keycloak, 2026-06-04](https://www.keycloak.org/2026/06/keycloak-2663-released)). There is no reported in-the-wild exploitation, so this is a patch-and-harden item rather than an active-incident one — but the failure modes sit precisely in the identity-protocol machinery (OAuth token exchange, OIDC token endpoint, WebAuthn registration, refresh-token rotation) that this audience builds detections around, and an internet-reachable Keycloak is by definition exposed.

**The token-exchange privilege escalation (`CVE-2026-9704`).** The release notes describe this lead issue as "Privilege escalation via silent subject_token removal in token exchange" ([Keycloak, 2026-06-04](https://www.keycloak.org/2026/06/keycloak-2663-released)). Keycloak's standard (RFC 8693) token-exchange grant takes a `subject_token` identifying the principal whose token is being exchanged; per the release-notes title, *silently removing* that parameter is not rejected as it should be but instead yields a privilege escalation — a low-privilege client obtains a token it should have had to supply and prove a subject for. The relevant prerequisite is that the token-exchange feature is enabled (it is not on by default in all profiles, but is widely turned on for service-to-service and impersonation flows). Maps to `T1550.001` (Use Alternate Authentication Material: Application Access Token) and `T1078.004` (Valid Accounts: Cloud Accounts).

**SSRF via the OIDC token endpoint (`CVE-2026-4874`).** An attacker able to reach the OIDC token endpoint can coerce Keycloak into issuing server-side HTTP requests to attacker-chosen targets, turning the identity server — which typically sits with network reachability into sensitive internal segments — into an SSRF pivot for internal-service reconnaissance. Because Keycloak is usually permitted to talk to internal directories, databases and admin endpoints, the blast radius of SSRF here is larger than on a typical edge web app.

**The rest of the cluster worth knowing.** `CVE-2026-8830` is a missing server-side validation of WebAuthn credential *registration* — a malicious authenticator can submit unvalidated attestation data, which can undercut the assurance of phishing-resistant MFA enrolment (`T1556.006`, Modify Authentication Process: Multi-Factor Authentication). `CVE-2026-9802` is a refresh-token replay window: a server restart resets `startupTime`, allowing reuse of rotated refresh tokens even when `revokeRefreshToken=true`, giving a post-restart replay opportunity (`T1550.001`). `CVE-2026-9792` is a Resource-Owner-Password-Credentials (ROPC) grant bypass of client-policy enforcement. `CVE-2026-37977` reflects `Access-Control-Allow-Origin` from an unverified JWT `azp` claim on the UMA endpoint when Authorization Services / UMA is enabled — a CORS-trust break.

**Detection concepts (no IOCs).** Token-exchange abuse is visible in Keycloak's own event log: alert on `token_exchange` events where the `subject_token` is absent yet a token is issued, and on exchanges that cross a privilege boundary (low-privilege client → high-privilege service-account audience). For the SSRF, watch for outbound connections originating from the Keycloak service account/host to non-allow-listed internal or external addresses correlated with token-endpoint requests. For the WebAuthn flaw, audit credential-registration events for attestation formats that do not match your enrolment policy. For the refresh-token window, correlate refresh-token-grant successes immediately following a Keycloak restart against the expected revocation state.

**Hardening / remediation.** Upgrade to 26.6.3 across all editions including the Red Hat build. If token exchange is not required, disable the feature flag — that removes the `CVE-2026-9704` path entirely. Place the OIDC/admin endpoints behind network restrictions and enforce strict egress filtering from the Keycloak host to blunt the SSRF. Re-validate that phishing-resistant MFA enrolment is gated by an attestation policy, and review `revokeRefreshToken` behaviour around maintenance restarts. CVSS scores for the individual CVEs were not yet published at the time of the release notes; treat exposure by reachability and feature-enablement, not by a score.
