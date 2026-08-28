---
schema: 1
kind: vulnerability
horizon: operational
title: "Claroty Team82: Danfoss AK-SM 800A refrigeration system managers — undocumented 'code-of-the-day' authentication bypass and post-authentication command-injection RCE across thousands of internet-exposed devices"
headline: "A hidden authentication mechanism discloses internal network layout before an attacker even needs the two post-auth flaws that follow it"
summary: >
  Companion disclosure to Claroty's Copeland research, same team and publish day. Danfoss AK-SM
  800A refrigeration system managers — used in supermarkets, cold storage and commercial HVAC —
  carry an undocumented 'code-of-the-day' authentication bypass disclosing internal IPs, usernames
  and store names (CVE-2025-41450), a post-authenticated OS command injection in the alarm-email
  configuration (CVE-2025-41451), and an Nginx configuration-injection flaw enabling denial of
  service (CVE-2025-41452). Claroty's own internet-wide scan found thousands of exposed devices.
discovered_at: "2026-08-28T06:54:00Z"
updated_at: null
event_date: "2026-08-09"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, patch-available, ot-ics]
regions: [global, europe]
sectors: [healthcare, energy]
entities: []
techniques: [T1190, T1059]
affected_products: ["Danfoss AK-SM 800A"]
cves:
  - id: CVE-2025-41450
    cvss: "8.2"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Danfoss AK-SM 800A firmware before build 4.2"
    fixed: "Firmware build 4.2"
  - id: CVE-2025-41451
    cvss: "7.6"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Danfoss AK-SM 800A firmware before R4.3.1"
    fixed: "Firmware R4.3.1"
  - id: CVE-2025-41452
    cvss: "5.4"
    epss: null
    type: dos
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Danfoss AK-SM 800A firmware before R4.3.1"
    fixed: "Firmware R4.3.1"
sources:
  - url: "https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers"
    publisher: "Claroty Team82"
    date: "2026-08-09"
    role: primary
closed_sources: []
evidence:
  - quote: "The application accepts a specially crafted authentication request containing a generated 'code of the day.'"
    publisher: "Claroty Team82"
  - quote: "The field value being formatted into the shell command is not sanitized and could include OS shell directives controlled by an attacker."
    publisher: "Claroty Team82"
  - quote: "An attacker could abuse it to implant arbitrary routing directives into the Internet-facing Nginx configuration."
    publisher: "Claroty Team82"
  - quote: "To understand the real-world exposure of the Danfoss AK-SM 800A, we searched publicly available internet-wide scanning platforms."
    publisher: "Claroty Team82"
verification: single-source
sourcing_note: >
  Claroty Team82 is the sole source; Danfoss's own advisory (DSA-2025-08-01) is linked from the
  Claroty page but was not independently fetched this run, so verification stays single-source on
  Claroty alone. CVE identifiers are 2025-dated despite the 2026-08-09 public disclosure —
  reserved-then-disclosed-later is a normal CNA pattern, not a dating error. The RCE and
  Nginx-injection primitives require prior authentication; Claroty's article does not explicitly
  confirm the code-of-the-day mechanism as a pre-auth path into the two post-auth primitives, so
  this entry treats the chain as auth-gated unless a combined path is independently confirmed.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade Danfoss AK-SM 800A refrigeration system managers to firmware R4.3.1 (build 4.2 closes CVE-2025-41450 alone) on every deployment, and treat any of the thousands of internet-exposed devices Claroty found via public internet-scan platforms as a priority — take management interfaces off the public internet entirely where the upgrade cannot happen immediately."
updates: []
migrated_from: null
---

Companion disclosure to Claroty Team82's Copeland XWEB Pro research, published the same day (2026-08-09T17:59Z), covering the Danfoss AK-SM 800A refrigeration system-manager platform used in supermarkets, cold-storage facilities and commercial HVAC. Claroty found "thousands of publicly accessible management interfaces" via internet-wide scan data, using platforms including Shodan and Censys: "to understand the real-world exposure of the Danfoss AK-SM 800A, we searched publicly available internet-wide scanning platforms" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)) — Claroty does not publish a precise device count.

CVE-2025-41450 (CWE-287 Improper Authentication, CVSS 3.1 8.2) is a hidden, undocumented "code-of-the-day" authentication mechanism: the application accepts a specially crafted authentication request containing a generated "code of the day" that bypasses normal login and discloses a web report with internal IPs, usernames and store names — "the application accepts a specially crafted authentication request containing a generated 'code of the day'" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)) — patched in firmware build 4.2. CVE-2025-41451 (CWE-77 OS Command Injection, CVSS 3.1 7.6) is a post-authenticated command injection in the alarm-to-email (SMTP) configuration field: a user-supplied value is formatted unsanitized into a shell command executed on the device, which Claroty used to achieve remote code execution: "the field value being formatted into the shell command is not sanitized and could include OS shell directives controlled by an attacker" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)). CVE-2025-41452 (CWE-15 External Control of Configuration Setting, CVSS 3.1 5.4) lets a post-authenticated user inject arbitrary Nginx directives via the exposed `headers.conf` include: "an attacker could abuse it to implant arbitrary routing directives into the Internet-facing Nginx configuration" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)), enabling denial-of-service. Danfoss shipped firmware R4.3.1 fixing CVE-2025-41451/41452 (build 4.2 for CVE-2025-41450). The RCE and Nginx-injection primitives require prior authentication; Claroty's article does not explicitly confirm the code-of-the-day mechanism as a pre-auth path into the two post-auth primitives, so this entry treats the chain as auth-gated unless a combined path is independently confirmed.

The undocumented authentication mechanism is instructive tradecraft on its own terms even setting aside the RCE chain: a hidden authentication bypass disclosing internal network topology (IPs, usernames, store identifiers) before an attacker needs any further vulnerability is exactly the class of vendor-authentication-mechanism audit finding that a Tier 2/3 responder auditing an OT/building-management estate should be watching for, distinct from a conventional missing-authentication bug. **Triage:** monitor authentication attempts against AK-SM 800A management interfaces for requests carrying a non-standard authentication parameter shape (a "code" field distinct from the normal username/password flow) — legitimate operator logins never use the code-of-the-day mechanism, so its presence in a request is itself the discriminator. On the post-auth side, unexpected shell-metacharacter content in the alarm-email SMTP configuration field, or unexplained changes to the device's Nginx routing configuration, have no benign explanation for a device whose configuration should change only through documented administrative workflows.
