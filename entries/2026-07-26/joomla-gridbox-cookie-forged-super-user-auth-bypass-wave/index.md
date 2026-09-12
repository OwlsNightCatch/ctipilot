---
schema: 1
kind: vulnerability
title: >
  CVE-2026-61425 — Balbooa Gridbox for Joomla: a client-supplied cookie is accepted as proof of
  identity, giving anonymous Super User access
headline: >
  The Joomla extension disclosure wave adds a cookie-forgery auth bypass — one anonymous request
  reaches Super User, and Super User means PHP
summary: >
  The mySites.guru research campaign against Joomla third-party extensions produced six further
  disclosures between 2026-07-20 and 2026-07-23, and one of them changes technique class: the
  Balbooa Gridbox page builder (CVE-2026-61425) trusts a client-supplied cookie value as proof of
  identity, so setting an administrator's username in that cookie authenticates the requester as
  that user with no password and no existing session. A Joomla Super User can edit templates,
  which is PHP execution, so this is full site compromise from a single anonymous request. Fixed
  in Gridbox 2.20.1; the vulnerable code had shipped since October 2025. The same week added
  unauthenticated SQL injection and order-forgery flaws in EasyStore, an invoice IDOR in Events
  Booking, and a critical unauthenticated upload in Membership Pro.
discovered_at: "2026-07-26T14:08:00Z"
updated_at: "2026-07-31T04:09:14Z"
event_date: 2026-07-20
run_id: 2026-07-26T1308Z-audit
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - pre-auth
  - sqli
  - rce
  - patch-available
  - actively-exploited
  - priv-esc
  - supply-chain
regions:
  - europe
  - global
sectors:
  - public-sector
  - education
entities:
  - "trend:joomla-extension-file-upload-rce-wave"
techniques:
  - T1190
  - T1505.003
  - T1136.001
affected_products:
  - Balbooa Gridbox
  - JoomShaper EasyStore
  - Joomla Events Booking
  - Joomla Membership Pro
  - Balbooa Gridbox for Joomla
cves:
  - id: CVE-2026-61425
    cvss: "10.0 (CVSS 4.0, discloser's own assessment)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: Balbooa Gridbox before 2.20.1 (vulnerable code shipped from the October 2025 release)
    fixed: Gridbox 2.20.1
  - id: CVE-2026-65759
    cvss: 8.7 (CVSS 4.0)
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: JoomShaper EasyStore for Joomla before 2.0.2
    fixed: EasyStore 2.0.2
  - id: CVE-2026-65760
    cvss: 9.2 (CVSS 4.0)
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: JoomShaper EasyStore for Joomla before 2.0.2
    fixed: EasyStore 2.0.2
  - id: CVE-2026-65761
    cvss: 9.3 (CVSS 4.0)
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: JoomShaper EasyStore for Joomla before 2.0.2
    fixed: EasyStore 2.0.2
  - id: CVE-2026-63047
    cvss: null
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: Events Booking for Joomla before 5.8.2
    fixed: Events Booking 5.8.2
  - id: CVE-2026-62415
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: Membership Pro for Joomla before 4.6.2
    fixed: Membership Pro 4.6.2
  - id: CVE-2026-65884
    cvss: "10.0"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - patch-available
    affected: 1.0.0-2.20.1
    fixed: 2.20.2
  - id: CVE-2026-65885
    cvss: "9.4"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - exploited
      - patch-available
    affected: 1.0.0-2.20.1
    fixed: 2.20.2
sources:
  - url: "https://mysites.guru/blog/gridbox-critical-authentication-bypass/"
    publisher: mySites.guru
    date: 2026-07-20
    role: primary
  - url: "https://mysites.guru/blog/easystore-security-disclosure/"
    publisher: mySites.guru
    date: 2026-07-23
    role: primary
  - url: "https://mysites.guru/blog/events-booking-invoice-idor/"
    publisher: mySites.guru
    date: 2026-07-21
    role: primary
  - url: "https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/"
    publisher: mySites.guru
    date: 2026-07-21
    role: primary
  - url: "https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/"
    publisher: mySites.guru
    date: 2026-07-29
    role: primary
  - url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release"
    publisher: Balbooa
    date: 2026-07-29
    role: corroborating
closed_sources: []
evidence:
  - quote: A critical unauthenticated authentication bypass in Gridbox let anyone become a Super User on a Joomla site by setting a single browser cookie
    publisher: mySites.guru
  - quote: "An anonymous request to the order-repayment endpoint could mark any order paid with no login, no token, and no contact with any payment gateway."
    publisher: mySites.guru
  - quote: "Both list the affected range as 1.0.0 to 2.20.1, which is every Gridbox release there has ever been up to the fix. And both set the exploit maturity to Attacked with an urgency of Red, which is the CVE record's own way of recording that this is being used against real sites rather than sitting as a theoretical risk."
    publisher: mySites.guru
  - quote: "the registration handler adds the default group to whatever groups the visitor asks for, instead of replacing them. So anyone can register a normal account and place themselves straight into an administrator group."
    publisher: mySites.guru
  - quote: "We have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now"
    publisher: mySites.guru
verification: single-source
sourcing_note: >
  mySites.guru is the discloser and the per-vulnerability authority for each of these CVEs; no
  independent second source has covered the batch yet. Scores are CVSS 4.0: the three EasyStore
  values are the Joomla CNA's, while the Gridbox 10.0 is the discloser's own stated assessment
  rather than a CNA score, and Events Booking carries none. On CVE-2026-65760 the CNA vector is
  PR:N but the discloser describes the flaw as reachable by any logged-in customer, so it is
  recorded as post-auth to match the stated mechanism. The researcher withholds endpoint detail
  and proof-of-concept code under a fix-first policy, so there is no public exploitation signal.
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
  - "Inventory Joomla sites for the Balbooa Gridbox page builder and update to 2.20.1 — the vulnerable code has shipped since the October 2025 release, so any site on an older Gridbox has been anonymously takeover-able for roughly nine months; on internet-facing sites also review the Super User account list and template files for changes made in that period."
  - "Update Balbooa Gridbox to 2.20.2 on every Joomla site that runs it — 2.20.1, the fix for the earlier cookie-forgery flaw, does not close these."
  - "On any site that ran Gridbox 2.20.1 or earlier while internet-reachable, enumerate administrator-group members and remove accounts that entered an admin group through self-registration rather than an explicit administrative action, then review the web root for files written since 27 July."
updates:
  - at: "2026-07-31T04:09:14Z"
    run_id: 2026-07-31T0409Z-intel
    type: update
    summary: >
      A follow-on source-code audit of the Balbooa Gridbox page builder for Joomla, commissioned by
      the vendor after an earlier authentication-bypass disclosure, found 23 further vulnerabilities
      in the single component. Two now carry CVEs: CVE-2026-65884 (CVSS 4.0 10.0) because the
      registration handler adds the usergroup IDs a visitor asks for instead of replacing them,
      letting an anonymous user create an administrator account outright, and CVE-2026-65885 (CVSS 4.0
      9.4), an authenticated arbitrary file upload that turns the first into end-to-end
      unauthenticated remote code execution. The Joomla CNA marks both as attacked, and the researcher
      reports server-log evidence of exploitation plus 92 planted administrator accounts on one
      connected site. Every release from 1.0.0 to 2.20.1 is affected; the complete fix is Gridbox
      2.20.2.
    fields:
      - actions
      - affected_products
      - cves
      - evidence
      - priority
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-07-31/balbooa-gridbox-cve-2026-65884-anon-admin-registration-rce
migrated_from: null
---

The Joomla third-party-extension disclosure wave this pipeline has been tracking has been a file-upload story: unauthenticated uploads reaching code execution, several of which were weaponised and CISA-KEV-listed within days of disclosure. The batch mySites.guru published between 2026-07-20 and 2026-07-23 adds a different and more direct failure. In Balbooa's Gridbox page builder, "A critical unauthenticated authentication bypass in Gridbox let anyone become a Super User on a Joomla site by setting a single browser cookie" ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)). The extension treats a client-supplied cookie value as proof of identity rather than as an assertion to be validated against server-side session state, so an anonymous requester who places an administrator's username in that cookie is served the site as that administrator — no password, no login form, no pre-existing session. Because a Joomla Super User can edit templates, and templates are PHP, the practical outcome is code execution on the web server from a single unauthenticated request. Gridbox 2.20.1 fixes it; the vulnerable code had shipped since the previous release in October 2025, roughly nine months of exposure.

The rest of the week's batch is the same research campaign continuing on its original axis, with two flaws that matter beyond the site itself. EasyStore for Joomla carried an unauthenticated SQL injection able to read the whole site database (CVE-2026-65761, scored 9.3 by the Joomla CNA) plus an order-forgery flaw (CVE-2026-65759, 8.7) where "An anonymous request to the order-repayment endpoint could mark any order paid with no login, no token, and no contact with any payment gateway" ([mySites.guru, 2026-07-23](https://mysites.guru/blog/easystore-security-disclosure/)), fixed in 2.0.2. Events Booking exposed invoices containing personal and financial data to anonymous requests that simply walked sequential identifiers, fixed in 5.8.2 ([mySites.guru, 2026-07-21](https://mysites.guru/blog/events-booking-invoice-idor/)). Membership Pro's unauthenticated upload was initially disputed by the vendor — the researcher records that "The vendor called it 'not a critical security issue.' The Joomla CNA disagreed" and it was assigned CVE-2026-62415 at 9.1 critical, fixed in Membership Pro 4.6.2 ([mySites.guru, 2026-07-21](https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/)).

There is no public exploitation signal for any of these: the researcher withholds the exact cookie name, endpoints and proof-of-concept code under a fix-first policy. The reason to act ahead of the routine extension-update cycle is the wave's own track record rather than current telemetry — earlier members of this same disclosure series moved from publication to confirmed in-the-wild exploitation within days once the mechanism became public, and a cookie-forgery bypass is trivially rediscovered by anyone who diffs the 2.20.1 release against its predecessor.

**Defender takeaway:** Joomla is common in European public-sector, municipal and education web estates, and this class of flaw sits in third-party extensions that rarely appear in vulnerability-management inventories keyed on the CMS core version. Enumerate installed extensions and their versions as first-class inventory, not as a property of the Joomla install, and prioritise Gridbox given the nine-month exposure window and the anonymous-to-admin outcome.

**Triage:** a cookie-forgery bypass leaves little at the network layer to distinguish it — the request is well-formed and returns HTTP 200. The observable is the mismatch between authentication and privilege: administrative actions in Joomla's action log attributed to a Super User account with no preceding successful login event for that account, and no session-establishment record. Legitimate administrator activity is preceded by an authentication event from a consistent source; forged-cookie access produces privileged actions that appear without one. On sites running affected Gridbox versions, template-file modification timestamps postdating the October 2025 release, with no corresponding administrator login, are the artefacts worth reviewing.

## Update — 2026-07-31T04:09:14Z

The earlier entry covered CVE-2026-61425, the Gridbox flaw that accepted a client-supplied cookie as proof of identity, fixed in 2.20.1. Balbooa's response was to commission the same researcher to audit the whole component, and that audit found 23 further vulnerabilities in this one extension ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). The delta that matters is that 2.20.1 — the version the previous entry pointed operators at — is itself vulnerable to a worse flaw than the one it fixed, and that flaw is being exploited.

CVE-2026-65884 carries a CVSS 4.0 base score of 10.0 for a reason that requires no exploit skill at all: the registration handler adds the usergroup IDs supplied in the request to the default group rather than replacing them, so an anonymous visitor can register an ordinary account and place it directly into an administrator group. The researcher describes the defect precisely: the registration handler "adds the default group to whatever groups the visitor asks for, instead of replacing them," so "anyone can register a normal account and place themselves straight into an administrator group" ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). CVE-2026-65885, scored 9.4, is an authenticated arbitrary file upload, and it becomes remote code execution when chained with the first because the attacker can create the account the upload requires. Both published records give the affected range as 1.0.0 to 2.20.1 — every version the extension has ever shipped up to the fix — and both are marked with an exploit maturity of attacked and an urgency of red by the Joomla CNA that assigned them ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)).

Exploitation is not an inference. The researcher reports holding server access logs showing the exploitation requests arriving and describes 92 planted administrator accounts on a single connected Joomla site, created in batches from 27 July, with usernames following one generator's pattern of a fixed prefix plus a few hex characters paired to matching webmail addresses ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Balbooa's own release page corroborates attack traffic indirectly, referring to a recent increase in automated attacks and telling customers to remove the temporary web-server rules it had advised adding to block attacks against Gridbox endpoints ([Balbooa, 2026-07-29](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)).

Getting to a fixed build took three attempts, which is itself operationally relevant for anyone who applied an interim Gridbox update this month. The researcher's account of the coordinated-disclosure process records that the vendor's first proposed fix left several reported findings live, including an anonymous SQL injection returning password hashes that had been patched at only one of several identical reachable entry points, and that the second closed that and the actively-exploited routes but still left a forgeable payment-gateway callback signature and a SQL injection reachable by a low-privilege authenticated user ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Only 2.20.2, released 2026-07-29, closes all of it, and the vendor states the build was given to the reporting researcher for independent verification before release ([Balbooa, 2026-07-29](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)). The remaining 21 findings are described only by shape, with nine further CVE IDs reserved but unpublished, so the public picture of this component's exposure is not yet complete.

**Detection.** Both halves of the chain leave records in places most Joomla operators already keep. For the privilege escalation, the artifact is a user account whose administrator-group membership was established at creation time rather than by a later administrative change — visible in the user table and in Joomla's own action logs as a registration event that produced an elevated account, with no corresponding admin action. Cluster it by timing: automated abuse of this flaw produces accounts in batches minutes apart, not the trickle of genuine sign-ups. For the upload half, the signal is a file appearing in a web-reachable directory with a server-executable extension, written by the web server user, followed by requests to that path from a small number of sources — and in web-server access logs, POST requests to the extension's registration and upload endpoints from addresses with no prior browsing history on the site.

**Triage:** a public Joomla site with open registration collects spam accounts constantly, so a new unrecognised user is not the signal. The discriminator is the group membership: ordinary registration spam lands in the default registered-users group and stays there, while these accounts sit in an administrator group from the moment they were created. Any self-registered account holding administrative rights on a Gridbox site should be treated as planted rather than misconfigured.

**Defender takeaway:** this is the second time in ten days that a widely-installed Joomla page-builder extension has turned out to accept the attacker's own claim about who they are, and the pattern across this wave is that the fix version from one disclosure is the vulnerable version in the next. A Joomla estate — common across European municipal, cantonal and education sites — needs an extension inventory that can answer "which of our sites run Gridbox, at what version" quickly, because patching here is fast and the compromise-assessment afterwards is what takes the time.
