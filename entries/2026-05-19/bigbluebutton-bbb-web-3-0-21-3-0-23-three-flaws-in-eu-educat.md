---
schema: 1
kind: threat
horizon: operational
title: "BigBlueButton bbb-web < 3.0.21 / < 3.0.23 — three flaws in EU education and government virtual-classroom platform: weak session-token randomness, API checksum bypass, SSRF"
headline: "BigBlueButton bbb-web < 3.0.21 / < 3.0.23 — three flaws in EU education and government virtual-classroom platform: weak session-token randomness, API checksum"
summary: "BigBlueButton ≥ 3.0.21 / 3.0.23 fix three flaws in widely-deployed EU academic & government virtual-classroom platform (BBB GHSA-7959-pf2v-xc4h, 2026-05-17). Weak sessionToken randomness (CVE-2026-46351, CVSS 8.1), presentationUploadExternalUrl checksum bypass (CVE-2026-46353, CVSS 8.1), SSRF in presentation URL validation (CVE-2026-46404, CVSS 6.8); BSI corroborated 2026-05-18."
discovered_at: "2026-05-19T05:00:01Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - info-disclosure
  - patch-available
regions:
  - europe
  - dach
  - switzerland
sectors:
  - education
  - public-sector
entities:
  - "trend:bigbluebutton-bbb-web-three-cves-46351-46353-46404-eu-edu"
cves:
  - id: CVE-2026-46351
    cvss: "8.1"
    epss: null
    type: auth-bypass
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-46353
    cvss: "8.1"
    epss: null
    type: auth-bypass
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-46404
    cvss: "6.8"
    epss: null
    type: auth-bypass
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
sources:
  - url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h"
    publisher: BBB GHSA-7959-pf2v-xc4h
    role: primary
  - url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff"
    publisher: BBB GHSA-43hc-5g2m-cqff
    role: corroborating
  - url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h"
    publisher: BBB GHSA-xqm3-6q7q-4v5h
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568"
    publisher: BSI WID-SEC-2026-1568
    role: corroborating
closed_sources: []
evidence:
  - quote: Insecure SessionToken Generation in BigBlueButton
    publisher: BBB GHSA-7959-pf2v-xc4h
  - quote: "Ein entfernter, authentisierter Angreifer kann mehrere Schwachstellen in BigBlueButton ausnutzen, um Sicherheitsvorkehrungen zu umgehen und vertrauliche Informationen offenzulegen"
    publisher: BSI WID-SEC-2026-1568
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
  - "**Upgrade BigBlueButton to `≥ 3.0.21` (CVE-2026-46351, CVE-2026-46353) and `≥ 3.0.23` (CVE-2026-46404)** across cantonal Volksschule, university and Länder e-learning deployments. Audit `bbb-web` logs for anomalous joins using predicted sessionTokens, API calls to `presentationUploadExternalUrl` with unexpected URL parameters, and egress from the BBB server process to RFC1918 / 169.254/16 addresses."
migrated_from: briefs/2026-05-19.md
---

BigBlueButton (BBB) — the de facto open-source virtual classroom platform deployed across German DFN, Swiss SWITCH, and pan-European GÉANT academic networks, including cantonal school deployments — published three GitHub Security Advisories on 2026-05-17 covering distinct flaws in its `bbb-web` component, all in versions before 3.0.21 (two of three) and 3.0.23 (one). CVE-2026-46351 (CVSS 8.1) is a CWE-330 weakness: the `sessionToken` is generated with insufficiently random values, letting an authenticated low-privilege attacker who shares or has observed a meeting determine other participants' session tokens and impersonate any conference user ([BBB GHSA-7959-pf2v-xc4h, 2026-05-17](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h)). CVE-2026-46353 (CVSS 8.1) is a CWE-284 access-control bypass in the `presentationUploadExternalUrl` endpoint: by supplying specific URL parameters an attacker can bypass checksum validation and send valid API requests to restricted endpoints without proper authentication, with high confidentiality + integrity impact ([BBB GHSA-43hc-5g2m-cqff, 2026-05-17](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff)). CVE-2026-46404 (CVSS 6.8) is a CWE-918 SSRF in presentation URL validation: insufficient redirect-following checks allow a high-privilege authenticated attacker to reach RFC1918 and link-local (169.254.0.0/16) addresses from the BBB server context ([BBB GHSA-xqm3-6q7q-4v5h, 2026-05-17](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h)). BSI's WID-SEC-2026-1568 corroborated on 2026-05-18 ([BSI WID-SEC-2026-1568, 2026-05-18](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568)).

**Why it matters to us:** BBB is operated at scale by Swiss cantonal Volksschule deployments, German Länder ministries of education and university IT, EU national-research-and-education networks (NRENs). The combination of session-token prediction + checksum bypass would let a low-privilege classroom participant impersonate other students and teachers or send arbitrary authenticated API calls; SSRF on the server gives a presenter-role lateral-movement primitive into RFC1918 networks (KVM hosts, internal LDAP, SIS endpoints). Upgrade `bbb-web` to ≥ 3.0.21 for the first two CVEs and ≥ 3.0.23 for the SSRF; monitor `bbb-web` logs for anomalous joins using close-by sessionTokens and for API calls to `presentationUploadExternalUrl` carrying unexpected URL parameters; alert on egress from the BBB server process to RFC1918 / 169.254/16 ranges. MITRE T1212 (Exploitation for Credential Access) covers the session-token-prediction primitive; the SSRF maps to T1190 (Exploit Public-Facing Application) chained with internal-network reach.
