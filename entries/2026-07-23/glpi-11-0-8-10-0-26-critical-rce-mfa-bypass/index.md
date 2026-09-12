---
schema: 1
kind: vulnerability
title: "GLPI 11.0.8 / 10.0.26 — critical RCE via form import and complete MFA bypass in the public-sector ITSM platform"
headline: "GLPI patches a critical form-import RCE and a full MFA bypass in the ITSM/asset platform widely run by EU public-sector, education and healthcare"
summary: >
  GLPI 11.0.8 and 10.0.26 (released 2026-06-24) fix 16 vulnerabilities, two of them critical:
  CVE-2026-48482, a remote code execution via the GLPI 11 form-import feature, and CVE-2026-52848, a
  complete bypass of GLPI 11's multi-factor authentication. The CVEs were publicly disclosed on
  2026-07-21 and CERT-FR published its advisory on 2026-07-22 — the in-window event. High-severity flaws
  add 2FA-code brute-forcing (no OTP rate-limiting), authtype-API privilege escalation, SQL injection,
  arbitrary file deletion and document read. GLPI is an open-source IT-asset/helpdesk platform heavily
  deployed across French and EU public administration, education and healthcare; no in-the-wild
  exploitation is reported.
discovered_at: "2026-07-23T04:34:04Z"
event_date: "2026-07-21"
run_id: 2026-07-23T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, sqli, patch-available]
regions: [europe, global]
sectors: [public-sector, healthcare, education]
entities: []
techniques: [T1190, "T1556.006", T1110, T1068]
affected_products: ["GLPI"]
cves:
  - id: CVE-2026-48482
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI 11.0.x < 11.0.8"
    fixed: "11.0.8"
  - id: CVE-2026-52848
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI 11.0.x < 11.0.8"
    fixed: "11.0.8"
  - id: CVE-2026-49470
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI 11.0.x < 11.0.8"
    fixed: "11.0.8"
  - id: CVE-2026-53625
    cvss: null
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI < 11.0.8 and < 10.0.26"
    fixed: "11.0.8 / 10.0.26"
  - id: CVE-2026-47678
    cvss: null
    epss: null
    type: sqli
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI < 11.0.8 and < 10.0.26"
    fixed: "11.0.8 / 10.0.26"
  - id: CVE-2026-53629
    cvss: null
    epss: null
    type: sqli
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI < 11.0.8 and < 10.0.26"
    fixed: "11.0.8 / 10.0.26"
  - id: CVE-2026-47679
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI < 11.0.8 and < 10.0.26"
    fixed: "11.0.8 / 10.0.26"
  - id: CVE-2026-53626
    cvss: null
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "GLPI 11.0.x < 11.0.8"
    fixed: "11.0.8"
  - id: CVE-2026-55214
    cvss: null
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "GLPI 11.0.x < 11.0.8"
    fixed: "11.0.8"
  - id: CVE-2026-53610
    cvss: null
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "GLPI 11.0.x < 11.0.8"
    fixed: "11.0.8"
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0909/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-07-22"
    role: primary
  - url: "https://www.glpi-project.org/en/glpi-11-0-8-and-10-0-26-available/"
    publisher: "GLPI Project"
    date: "2026-06-24"
    role: primary
  - url: "https://www.it-connect.tech/glpi-11-0-8-and-10-0-26-patch-16-flaws-including-2-critical-vulnerabilities/"
    publisher: "IT-Connect"
    date: "2026-06-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "[SECURITY - ==CRITICAL== 11.0] RCE via Form import (CVE-2026-48482)"
    publisher: "GLPI Project"
  - quote: "De multiples vulnérabilités ont été découvertes dans GLPI. Elles permettent à un attaquant de provoquer une atteinte à la confidentialité des données, une atteinte à l'intégrité des données et un contournement de la politique de sécurité."
    publisher: "CERT-FR"
verification: multi-source
sourcing_note: "Freshness: the GLPI fixes shipped in 11.0.8/10.0.26 on 2026-06-24 (out of window), but the CVEs were coordinated-disclosed on 2026-07-21 and CERT-FR issued CERTFR-2026-AVI-0909 on 2026-07-22 — the in-window event that surfaces the now-public flaws to defenders; event_date records the 2026-07-21 disclosure. GLPI Project and CERT-FR published severity tiers (Medium/High/Critical) but no numeric CVSS scores, so cvss is null throughout; CERT-FR's advisory names only a subset of the 16 CVEs. The release fixes 16 vulnerabilities in total (16 addressed in 11.0.8, 9 in 10.0.26 per IT-Connect) — the critical and high-impact subset whose nature the sources describe is enumerated here; several lower-tier CVEs are not individually characterised by the sources and are omitted rather than guessed. No in-the-wild exploitation reported."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Update internet-facing GLPI instances to 11.0.8 (11.0.x) or 10.0.26 (10.0.x) now — the release fixes a critical form-import RCE and a complete MFA bypass that together defeat the authentication hardening the 11.x branch specifically introduced."
migrated_from: null
---

GLPI 11.0.8 and 10.0.26 shipped on 2026-06-24, fixing 16 vulnerabilities (16 addressed in 11.0.8, 9 in 10.0.26), but the CVEs were publicly disclosed on 2026-07-21 and CERT-FR published its advisory CERTFR-2026-AVI-0909 on 2026-07-22 — the in-window event that brings the flaws to defenders' attention ([GLPI Project, 2026-06-24](https://www.glpi-project.org/en/glpi-11-0-8-and-10-0-26-available/); [CERT-FR, 2026-07-22](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0909/)). Two flaws are critical: CVE-2026-48482, remote code execution via GLPI 11's native form-import feature — an unsafe parsing/deserialization path in the import handler that gives an attacker who can submit a crafted form file code execution with application privileges; and CVE-2026-52848, a complete bypass of GLPI 11's multi-factor authentication mechanism, defeating the 2FA hardening the 11.x branch specifically introduced ([GLPI Project, 2026-06-24](https://www.glpi-project.org/en/glpi-11-0-8-and-10-0-26-available/)). High-severity entries add exploitation depth: account takeover by brute-forcing the 2FA code itself (no rate-limiting on OTP verification, CVE-2026-49470), privilege escalation through the authtype API (CVE-2026-53625), SQL injection in dropdown and history-tab components (CVE-2026-47678, CVE-2026-53629), arbitrary file deletion (CVE-2026-47679) and arbitrary document read (CVE-2026-53626), plus stored and reflected XSS ([IT-Connect, 2026-06-25](https://www.it-connect.tech/glpi-11-0-8-and-10-0-26-patch-16-flaws-including-2-critical-vulnerabilities/)). Affected are GLPI 11.0.x before 11.0.8 and all versions before 10.0.26; no source in this run reports in-the-wild exploitation.

**Defender takeaway:** GLPI is an open-source IT-asset and helpdesk platform used across French and broader EU public administration, education and healthcare — an internet-exposed instance combining the form-import RCE with the MFA bypass is a direct route from unauthenticated-adjacent access to code execution, so prioritise patching public-facing deployments. In GLPI application and web-server logs, watch for form-import operations from accounts that do not normally author forms, repeated failed-then-successful 2FA verifications against a single account (the OTP brute-force has no rate limit), and authtype or profile changes outside administrative workflow; SQL-injection attempts surface as anomalous query patterns against the dropdown and history-tab endpoints. **Triage:** GLPI administrators legitimately import forms and change profiles — the discriminators are the actor (a non-administrative or newly-active account performing these actions), the sequence (many rapid OTP submissions preceding a successful login), and the endpoint (injection strings against the specific dropdown/history components named in the release).
