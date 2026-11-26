---
schema: 1
kind: vulnerability
title: "SEPPmail Secure E-Mail Gateway before 15.1.2: an unauthenticated template injection on the GINA login page can read and take over any GINA account (CVE-2026-130637, vendor score 9.3) and ten more flaws are fixed in the 2026-11-24 patch release; no exploitation or workaround stated"
headline: "SEPPmail 15.1.2 fixes unauthenticated GINA account takeover (9.3) and ten more flaws; update the gateway"
summary: >
  SEPPmail's patch release 15.1.2 of 2026-11-24 fixes eleven flaws in Secure E-Mail Gateway versions before 15.1.2, led by CVE-2026-130637 (vendor score 9.3): request values reflected on the GINA login page were processed by the template engine, which could let an unauthenticated attacker read attributes of any GINA account and take it over. Two more rows score 9.2 (a security-question recovery session accepted by the password-change workflows, and a hard-coded fallback secret for Large File Transfer attachments) and an unauthenticated request could reset a registered account's password without the security question. SEPPmail names no exploitation and no workaround, and does not say whether the 15.0 branch is affected.
discovered_at: "2026-11-26T05:04:00Z"
updated_at: null
event_date: "2026-11-24"
run_id: 2026-11-26T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, auth-bypass, patch-available]
regions: [switzerland, europe]
sectors: [technology]
entities: ["product:seppmail-secure-e-mail-gateway"]
techniques: [T1190, T1078, T1059.004, T1068]
affected_products: ["SEPPmail Secure E-Mail Gateway"]
cves:
  - id: CVE-2026-130637
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124840
    cvss: "9.2"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124843
    cvss: "9.2"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124844
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124838
    cvss: "8.5"
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124842
    cvss: "8.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124839
    cvss: "7.7"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124841
    cvss: "6.9"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124836
    cvss: "6.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124837
    cvss: "6.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
  - id: CVE-2026-124845
    cvss: "6.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure E-Mail Gateway before 15.1.2"
    fixed: "15.1.2"
sources:
  - url: "https://docs.seppmail.com/en/20_revision-history.html"
    publisher: "SEPPmail revision history"
    date: "2026-11-24"
    role: primary
closed_sources: []
evidence:
  - quote: "Request values reflected on the GINA login page were processed by the template engine, which could allow an unauthenticated attacker to read attributes of any GINA account and take it over."
    publisher: "SEPPmail revision history"
    source_url: "https://docs.seppmail.com/en/20_revision-history.html"
  - quote: "An unauthenticated GINA request could reset the password of a registered account without answering the security question."
    publisher: "SEPPmail revision history"
    source_url: "https://docs.seppmail.com/en/20_revision-history.html"
verification: single-source
sourcing_note: >
  SEPPmail is the disclosing vendor for its own product and its revision history is the only record: ENISA's vulnerability database, the CVE program, NCSC.ch and BACS had no entry for these ids at the time of reading. The page prints each score without a CVSS version or vector, and every row says only that versions before 15.1.2 are affected. The scores are the vendor's own and may change once the CVE records appear. The page states no authentication precondition for CVE-2026-124840, CVE-2026-124839, CVE-2026-124843, CVE-2026-124841, CVE-2026-124836, CVE-2026-124837 or CVE-2026-124845, so their authentication and vector fields are a reading of each mechanism to be revised when CVE records appear.
confidence: medium
references:
  - 2026-11-05/seppmail-gateway-15-1-1-unauth-root-rce-and-file-access
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

SEPPmail's revision history lists patch release 15.1.2 of 2026-11-24 with eleven security fixes, each marked as affecting versions before 15.1.2 ([SEPPmail, 2026-11-24](https://docs.seppmail.com/en/20_revision-history.html)). The worst is CVE-2026-130637 (vendor score 9.3): request values reflected on the GINA login page were processed by the template engine, which could let an unauthenticated attacker read attributes of any GINA account and take it over, and the fix stops expanding request values as template placeholders. Two further rows score 9.2: CVE-2026-124840, where a session created by answering the security question was also accepted by the registration and settings workflows, so an attacker who knows the security answer could replace the password, and CVE-2026-124843, where a hard-coded fallback secret was used if the appliance's key material could not be loaded, which could let encrypted Large File Transfer attachments be decrypted outside the appliance ([SEPPmail, 2026-11-24](https://docs.seppmail.com/en/20_revision-history.html)).

The remaining rows are CVE-2026-124844 (8.7), unauthenticated GINA uploads that were never removed and could fill the disk; CVE-2026-124838 (8.5), a configuration-service socket open to every local user; CVE-2026-124842 (8.3), an unauthenticated GINA request that reset the password of a registered account without the security question; CVE-2026-124839 (7.7), a crafted GINA account address that reached a shell command in a maintenance script at start, with elevated privileges; and four rows at 6.9 to 6.3 covering unescaped LDAP filter values (CVE-2026-124841, CVE-2026-124836), a crafted DKIM signature that injects forged Authentication-Results later covered by the gateway's ARC seal (CVE-2026-124837) and a GINA domain lookup that falls back to the default domain settings (CVE-2026-124845) ([SEPPmail, 2026-11-24](https://docs.seppmail.com/en/20_revision-history.html)). The page names no exploitation and no workaround, and does not say whether the 15.0 branch, whose last release is 15.0.7, is affected.

**Exposure:** a SEPPmail Secure E-Mail Gateway before 15.1.2 whose GINA web interface is reachable from outside; the revision history says release 15.1.0 added support for restricting the file types that external communication partners can upload through GINA, which shows external recipients use it ([SEPPmail, 2026-11-24](https://docs.seppmail.com/en/20_revision-history.html)). The page does not state the CVSS vector of any score.

**Detection:** in GINA web access logs, login-page requests whose parameters carry template placeholder syntax, unauthenticated password-reset requests for accounts that are already registered, calls to the registration and settings workflows that follow a security-question recovery, and bursts of unauthenticated uploads; in the gateway's audit log, GINA password changes without the usual recovery sequence. The fixes do not undo an account already taken over, so review GINA password-change and sign-in history for the period before the update. These checks follow from the mechanisms the vendor names; the page publishes no indicator.

**Triage:** an unauthenticated password reset on a GINA account that is not yet registered is legitimate, since the fix keeps it for unregistered accounts only; the same request taking effect on an already registered account without the security-question step is the abuse ([SEPPmail, 2026-11-24](https://docs.seppmail.com/en/20_revision-history.html)).

**Defender takeaway:** update every gateway on 15.1 to 15.1.2 and, for gateways on the 15.0 branch, ask SEPPmail whether these flaws apply, since the page does not say; where GINA is internet-facing, give the update priority within the regular cycle, because the template injection and the unauthenticated reset need no login, and review GINA account changes made before the update.
