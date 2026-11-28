---
schema: 1
kind: vulnerability
title: "Keycloak 26.6.2 fixes 16 security issues, among them an OIDC login session fixation (CVE-2026-7507) and a WebAuthn execute-actions token replay (CVE-2026-37982)"
headline: "Keycloak 26.6.2: a crafted link can hand an attacker the victim's session, up to the master-realm admin account"
summary: >
  Keycloak 26.6.2, released on 2026-05-19, fixes 16 security issues carrying 18 CVE ids. CVE-2026-7507
  (CVSS 7.5, which Red Hat calls critical) lets an unauthenticated attacker pre-create an authentication
  session and take over a victim's account through a crafted /login-actions/restart link, up to the
  master-realm admin account in default deployments; CVE-2026-37982 lets an intercepted execute-actions
  e-mail link register the attacker's WebAuthn authenticator. Red Hat build of Keycloak fixes CVE-2026-7507
  in 26.2.16 and 26.4.12 and CVE-2026-37982 in 26.4.12, and BSI rates its nine-CVE advisory high.
discovered_at: "2026-05-21T05:00:05Z"
event_date: 2026-05-19
run_id: 2026-05-21-77cdc4cd
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - auth-bypass
  - patch-available
regions:
  - global
sectors: []
entities: []
techniques: [T1185, T1098.005, T1212]
affected_products:
  - "Keycloak"
  - "Red Hat Build of Keycloak"
cves:
  - id: CVE-2026-7507
    cvss: "7.5"
    epss: null
    type: auth-bypass
    vector: user-interaction
    auth: pre-auth
    status:
      - patch-available
    affected: "Keycloak before 26.6.2"
    fixed: "Keycloak 26.6.2; Red Hat build of Keycloak 26.2.16 and 26.4.12"
  - id: CVE-2026-37982
    cvss: "6.8"
    epss: null
    type: auth-bypass
    vector: user-interaction
    auth: pre-auth
    status:
      - patch-available
    affected: "Keycloak before 26.6.2"
    fixed: "Keycloak 26.6.2; Red Hat build of Keycloak 26.4.12"
  - id: CVE-2026-37979
    cvss: "6.5"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "Keycloak before 26.6.2"
    fixed: "Keycloak 26.6.2; Red Hat build of Keycloak 26.4.12"
  - id: CVE-2026-4630
    cvss: "6.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "Keycloak before 26.6.2"
    fixed: "Keycloak 26.6.2; Red Hat build of Keycloak 26.4.12"
  - id: CVE-2026-37978
    cvss: "4.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: admin-required
    status:
      - patch-available
    affected: "Keycloak before 26.6.2"
    fixed: "Keycloak 26.6.2; Red Hat build of Keycloak 26.4.12"
  - id: CVE-2026-6856
    cvss: "n/a"
    epss: null
    type: auth-bypass
    vector: user-interaction
    auth: pre-auth
    status:
      - patch-available
    affected: "Keycloak before 26.6.2"
    fixed: "Keycloak 26.6.2"
sources:
  - url: "https://www.keycloak.org/2026/05/keycloak-2662-released"
    publisher: "Keycloak"
    date: "2026-05-19"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1612"
    publisher: "BSI WID-SEC-2026-1612"
    date: "2026-05-19"
    role: corroborating
  - url: "https://access.redhat.com/security/cve/CVE-2026-7507"
    publisher: "Red Hat CVE-2026-7507"
    date: "2026-05-19"
    role: primary
  - url: "https://www.redhat.com/security/data/cve/CVE-2026-37982.html"
    publisher: "Red Hat CVE-2026-37982"
    date: null
    role: primary
  - url: "https://www.redhat.com/security/data/cve/CVE-2026-37979.html"
    publisher: "Red Hat CVE-2026-37979"
    date: null
    role: primary
  - url: "https://www.redhat.com/security/data/cve/CVE-2026-4630.html"
    publisher: "Red Hat CVE-2026-4630"
    date: null
    role: primary
  - url: "https://www.redhat.com/security/data/cve/CVE-2026-37978.html"
    publisher: "Red Hat CVE-2026-37978"
    date: null
    role: primary
  - url: "https://github.com/keycloak/keycloak/issues/48388"
    publisher: "Keycloak issue #48388"
    date: null
    role: corroborating
  - url: "https://access.redhat.com/errata/RHSA-2026:19594"
    publisher: "Red Hat RHSA-2026:19594"
    date: "2026-05-20"
    role: corroborating
  - url: "https://access.redhat.com/errata/RHSA-2026:19596"
    publisher: "Red Hat RHSA-2026:19596"
    date: "2026-05-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This allows for full takeover of the master-realm admin account in default Keycloak deployments."
    publisher: "Red Hat CVE-2026-7507"
    source_url: "https://access.redhat.com/security/cve/CVE-2026-7507"
  - quote: "Exploitation requires WebAuthn required actions to be enabled and the email link to be compromised."
    publisher: "Red Hat CVE-2026-37982"
    source_url: "https://www.redhat.com/security/data/cve/CVE-2026-37982.html"
  - quote: "By knowing or obtaining a resource's unique identifier (UUID) belonging to another Resource Server within the same realm, the client could bypass authorization checks."
    publisher: "Red Hat CVE-2026-4630"
    source_url: "https://www.redhat.com/security/data/cve/CVE-2026-4630.html"
verification: single-source
sourcing_note: >
  The Keycloak release notes and Red Hat's CVE pages and errata come from the same maintainers and are
  one assessment; BSI's WID-SEC-2026-1612 restates nine of the CVEs, and no exploitation was reported.
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
migrated_from: briefs/2026-05-21.md
updates:
  - at: "2026-10-21T20:33:44Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Keycloak's CVE-2026-4630 is a same-realm cross-resource-server IDOR, not a cross-realm one,
      CVE-2026-7507 runs through the /login-actions/restart endpoint with a crafted link, and the
      highlighted CVEs carry Red Hat scores from 4.9 to 7.5 with authenticated preconditions for three of
      them. The release fixes 16 issues with 18 CVE ids, Red Hat build of Keycloak 26.2.16 fixes
      CVE-2026-7507 and 26.4.12 fixes both, and no source links Akira.
    fields: [actions, affected_products, body, classification, cves, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, verification]
---

The Keycloak project released 26.6.2 on 2026-05-19 with fixes for 16 security issues carrying 18 CVE ids, several of them in bundled third-party components such as Bouncy Castle ([Keycloak, 2026-05-19](https://www.keycloak.org/2026/05/keycloak-2662-released)); BSI's WID-SEC-2026-1612, first released at 22:00 UTC that day, lists nine of the Keycloak CVEs and rates them high ([BSI WID-SEC-2026-1612](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1612)). CVE-2026-7507, which Red Hat calls a critical session fixation flaw although it scores CVSS 7.5, lets an unauthenticated attacker pre-create an authentication session and lure a victim to a crafted link: the `/login-actions/restart` endpoint lacks CSRF protection and cookie ownership checks, so single sign-on authenticates the victim and the attacker takes over the required-action form, which in default deployments reaches full takeover of the master-realm admin account ([Red Hat CVE-2026-7507](https://access.redhat.com/security/cve/CVE-2026-7507)). CVE-2026-37982 (6.8) lets an attacker who intercepts an execute-actions e-mail link replay its token and register their own WebAuthn authenticator on the victim's account, where WebAuthn required actions are enabled ([Red Hat CVE-2026-37982](https://www.redhat.com/security/data/cve/CVE-2026-37982.html)). CVE-2026-37979 (6.5) lets any confidential client with valid credentials read, through the token introspection endpoint, claims of lightweight access tokens meant for other resource servers ([Red Hat CVE-2026-37979](https://www.redhat.com/security/data/cve/CVE-2026-37979.html)); CVE-2026-4630 (6.8) lets an authenticated client that knows the UUID of another resource server's resource in the same realm read, change or delete it through the Authorization Services Protection API ([Red Hat CVE-2026-4630](https://www.redhat.com/security/data/cve/CVE-2026-4630.html)); CVE-2026-37978 (4.9) lets a low-privilege administrator with the `view-clients` role read other users' profile and role data through the `evaluate-scopes` Admin API ([Red Hat CVE-2026-37978](https://www.redhat.com/security/data/cve/CVE-2026-37978.html)); and CVE-2026-6856 lets an authenticator that sends self-attestation bypass the acceptable-AAGUID allowlist during WebAuthn registration ([Keycloak issue #48388](https://github.com/keycloak/keycloak/issues/48388)). Red Hat fixed CVE-2026-7507 in Red Hat build of Keycloak 26.2.16 ([RHSA-2026:19594](https://access.redhat.com/errata/RHSA-2026:19594)) and it, CVE-2026-37982, CVE-2026-37979, CVE-2026-4630 and CVE-2026-37978 in 26.4.12 ([RHSA-2026:19596](https://access.redhat.com/errata/RHSA-2026:19596)).

**Exposure:** Keycloak before 26.6.2; CVE-2026-7507 needs only a victim who follows a link, while the others need a confidential or authenticated client, an intercepted execute-actions e-mail link or an administrator holding `view-clients` ([Red Hat CVE-2026-7507](https://access.redhat.com/security/cve/CVE-2026-7507)) ([Red Hat CVE-2026-37982](https://www.redhat.com/security/data/cve/CVE-2026-37982.html)) ([Red Hat CVE-2026-37978](https://www.redhat.com/security/data/cve/CVE-2026-37978.html)).

**Detection:** Keycloak user and admin event logs: CVE-2026-37982 ends in an attacker's WebAuthn authenticator on the victim account, which Red Hat calls persistent account takeover ([Red Hat CVE-2026-37982](https://www.redhat.com/security/data/cve/CVE-2026-37982.html)), so the upgrade does not remove it; review WebAuthn credentials registered through execute-actions links before the upgrade.

**Defender takeaway:** upgrade Keycloak to 26.6.2 ([Keycloak, 2026-05-19](https://www.keycloak.org/2026/05/keycloak-2662-released)), or Red Hat build of Keycloak to 26.4.12 or 26.2.16 on those branches ([RHSA-2026:19596](https://access.redhat.com/errata/RHSA-2026:19596)) ([RHSA-2026:19594](https://access.redhat.com/errata/RHSA-2026:19594)); deployments whose users could be sent a crafted login link are the first in line because of CVE-2026-7507.

## Correction — 2026-10-21T20:33:44Z

CVE-2026-4630 is not a cross-realm flaw: it lets an authenticated client reach another resource server's resources within the same realm ([Red Hat CVE-2026-4630](https://www.redhat.com/security/data/cve/CVE-2026-4630.html)). CVE-2026-7507 works through the `/login-actions/restart` endpoint, with an attacker-created authentication session and a crafted link the victim follows, not through a crafted `state` parameter ([Red Hat CVE-2026-7507](https://access.redhat.com/security/cve/CVE-2026-7507)), and CVE-2026-37982 needs an intercepted execute-actions e-mail link ([Red Hat CVE-2026-37982](https://www.redhat.com/security/data/cve/CVE-2026-37982.html)). The highlighted CVEs carry Red Hat CVSS scores from 4.9 to 7.5 rather than none, CVE-2026-37979, CVE-2026-4630 and CVE-2026-37978 need an authenticated client or administrator, and the release fixes 16 issues with 18 CVE ids, nine of which BSI lists ([Keycloak, 2026-05-19](https://www.keycloak.org/2026/05/keycloak-2662-released)) ([BSI WID-SEC-2026-1612](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1612)). No source links the release to the Akira ransomware group.
