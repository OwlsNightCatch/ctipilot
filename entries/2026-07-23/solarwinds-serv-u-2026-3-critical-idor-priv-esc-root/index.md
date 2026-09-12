---
schema: 1
kind: vulnerability
title: "SolarWinds Serv-U 2026.3 — 15 critical IDOR flaws let authenticated users escalate to root RCE on the file-transfer server (CVSS 9.1)"
headline: "SolarWinds patches 15 critical IDOR-to-root flaws in the internet-facing Serv-U managed-file-transfer server"
summary: >
  SolarWinds Serv-U 15.5.4 HF1 and earlier carry 16 CVEs — 15 rated critical (CVSS 9.1) — that are
  insecure-direct-object-reference and broken-access-control flaws in the managed-file-transfer web
  console. An authenticated user, in several cases needing only group- or domain-administrator scope,
  can escalate to system administrator and reach remote code execution as root on the underlying host
  (reduced impact on Windows). All were reported through SolarWinds' bug-bounty program and fixed in
  Serv-U 2026.3 (2026-07-21); no in-the-wild exploitation is confirmed, but Serv-U is an internet-facing
  MFT server of exactly the class ransomware affiliates have targeted post-disclosure.
discovered_at: "2026-07-23T04:34:04Z"
event_date: "2026-07-21"
run_id: 2026-07-23T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, priv-esc, rce, patch-available]
regions: [global]
sectors: [public-sector, finance, energy, telco]
entities: []
techniques: [T1068]
affected_products: ["SolarWinds Serv-U"]
cves:
  - id: CVE-2026-28304
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28302
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28305
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28306
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28307
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28308
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28309
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28310
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28311
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28312
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28313
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28314
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28316
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28317
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28321
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
  - id: CVE-2026-28315
    cvss: "6.2"
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "≤ 15.5.4 HF1"
    fixed: "2026.3"
sources:
  - url: "https://www.solarwinds.com/trust-center/security-advisories/CVE-2026-28304"
    publisher: "SolarWinds PSIRT"
    date: "2026-07-21"
    role: primary
  - url: "https://documentation.solarwinds.com/en/success_center/servu/content/release_notes/servu_2026-3_release_notes.htm"
    publisher: "SolarWinds"
    date: "2026-07-21"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12785"
    publisher: "NCSC Switzerland"
    date: "2026-07-22"
    role: corroborating
  - url: "https://www.heise.de/news/Datentransfersoftware-Serv-U-hat-15-kritische-Sicherheitsluecken-11373098.html"
    publisher: "heise online"
    date: "2026-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "SolarWinds Serv-U is affected by an insecure direct object reference (IDOR) vulnerability that can lead to privilege escalation and remote code execution as root."
    publisher: "SolarWinds"
  - quote: "Successful exploitation allows authenticated attackers to escalate privileges to system administrator and execute arbitrary code with root privileges via network access."
    publisher: "NCSC Switzerland"
verification: multi-source
sourcing_note: "No source in this run confirms in-the-wild exploitation of CVE-2026-28302 et al.; heise's reference to Cl0p/MOVEit is historical context on the file-transfer target class, not an exploitation claim for this chain. NCSC-CH's post enumerates a subset of the CVE ids; the full set is taken from the SolarWinds 2026.3 release notes."
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
  - "Update SolarWinds Serv-U to 2026.3 now and prune domain- and group-administrator role assignments — the escalation chain pivots off an over-privileged authenticated account, so reducing that account population shrinks the exploitable surface immediately."
migrated_from: null
---

Serv-U 2026.3, released 2026-07-21, fixes 16 vulnerabilities — 15 of them critical at CVSS 9.1 — that are insecure-direct-object-reference (IDOR, CWE-639) and broken-access-control flaws in the managed-file-transfer web console rather than memory-safety bugs ([SolarWinds, 2026-07-21](https://documentation.solarwinds.com/en/success_center/servu/content/release_notes/servu_2026-3_release_notes.htm)). The consequential path is authorization: an authenticated user — in several cases needing only group- or domain-administrator scope, not full system administrator — can escalate to system administrator and achieve remote code execution as root on the underlying host, with reduced impact on Windows deployments ([SolarWinds PSIRT, 2026-07-21](https://www.solarwinds.com/trust-center/security-advisories/CVE-2026-28304); [NCSC Switzerland, 2026-07-22](https://security-hub.ncsc.admin.ch/#/posts/12785)). Individual flaws cover privilege escalation via configuration-path modification, arbitrary system-administrator account creation, arbitrary file read/write, account takeover through IDOR, and domain-user-group elevation to an admin group; one medium issue (CVE-2026-28315, CVSS 6.2) is a stored XSS in the admin UI usable for session hijacking. All were reported through SolarWinds' Intigriti bug-bounty program and NCSC-CH records exploitation status as unknown; heise notes Serv-U's history as a target for the Cl0p affiliate in prior MOVEit-class campaigns purely as context for why file-transfer software patch-lag is a recurring high-value target class ([heise online, 2026-07-22](https://www.heise.de/news/Datentransfersoftware-Serv-U-hat-15-kritische-Sicherheitsluecken-11373098.html)).

**Defender takeaway:** the worst-case chain requires an existing authenticated (often admin-tier) session, so this is a lateral-privilege-escalation and full-compromise risk for anyone already inside a Serv-U tenant rather than a pre-auth internet exploitation path — but Serv-U is routinely internet-facing and the whole chain pivots off an over-privileged authenticated account, which is where hardening pays off. Update to 2026.3, review and prune domain/group-administrator assignments, and keep the management interface behind additional network controls rather than open to the internet. In Serv-U's own audit logs, watch domain- and group-administrator accounts for actions outside normal administration — new system-administrator account creation, external-tool configuration-path changes, unexpected domain-to-system-admin role changes — and correlate them with the authentication record for the account performing them. **Triage:** these are the same log events a legitimate administrator generates; the discriminator is scope and sequence — a group- or domain-level account creating a system-administrator account or altering configuration paths it never normally touches, immediately after login, is the escalation signal.
