---
schema: 1
kind: vulnerability
title: >
  CVE-2026-61425 and the follow-up batch, Balbooa Gridbox for Joomla: a client-supplied cookie is
  accepted as proof of identity, giving anonymous Super User access
headline: >
  Balbooa Gridbox for Joomla: anonymous Super User flaws exploited since July; update to 2.20.4.2
summary: >
  The mySites.guru research campaign against Joomla third-party extensions produced six further
  disclosures between 2026-07-20 and 2026-07-23, and one of them changes technique class: the
  Balbooa Gridbox page builder (CVE-2026-61425) trusts a client-supplied cookie value as proof of
  identity, so setting an administrator's username in that cookie authenticates the requester as
  that user with no password and no existing session. A Joomla Super User can edit templates,
  which is PHP execution, so this is full site compromise from a single anonymous request. Fixed
  in Gridbox 2.20.1; the researcher says the vulnerable code shipped for at least nine months. The same week added
  unauthenticated SQL injection and order-forgery flaws in EasyStore, an invoice IDOR in Events Booking, and a critical unauthenticated upload in Membership Pro. A follow-up audit of Gridbox produced eleven more CVEs, fixed in 2.20.2, four of them exploited in the wild, and Gridbox 2.20.3.1 (21 September) fixes a further unauthenticated SQL injection present in every earlier build. Gridbox 2.20.4.2 (27 October) fixes two more unauthenticated SQL injections, CVE-2026-102788 and CVE-2026-102789, with no exploitation reported.
discovered_at: "2026-07-26T14:08:00Z"
updated_at: "2026-10-28T03:52:00Z"
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
    cvss: "10.0 (CVSS 4.0, discloser's own assessment; the published CVE record scores 9.4 on a high-privileges vector)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: Balbooa Gridbox before 2.20.1 (the discloser says the vulnerable code shipped for at least nine months, probably far longer)
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
    cvss: "9.1 (CVSS 3.1)"
    epss: null
    type: logic-flaw
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
  - id: CVE-2026-65887
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "1.0.0-2.20.1"
    fixed: "2.20.2"
  - id: CVE-2026-65888
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "1.0.0-2.20.1"
    fixed: "2.20.2"
  - id: CVE-2026-102788
    cvss: "9.3 (CVSS 4.0, Joomla CNA)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Gridbox 1.0.0 to 2.20.4.1"
    fixed: "2.20.4.2; no fix for sites on the Joomla 3 line, which stops at Gridbox 2.17.0.2"
  - id: CVE-2026-102789
    cvss: "9.3 (CVSS 4.0, Joomla CNA)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Gridbox 1.0.0 to 2.20.4.1"
    fixed: "2.20.4.2; no fix for sites on the Joomla 3 line, which stops at Gridbox 2.17.0.2"
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
  - url: "https://mysites.guru/blog/gridbox-author-sql-injection/"
    publisher: mySites.guru
    date: 2026-09-21
    role: primary
  - url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release"
    publisher: Balbooa
    date: 2026-07-29
    role: corroborating
  - url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update"
    publisher: "Balbooa (Gridbox 2.20.4.2 security update)"
    date: 2026-10-27
    role: corroborating
  - url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
    publisher: mySites.guru
    date: 2026-10-27
    role: primary
closed_sources: []
evidence:
  - quote: A critical unauthenticated authentication bypass in Gridbox let anyone become a Super User on a Joomla site by setting a single browser cookie
    publisher: mySites.guru
  - quote: "An anonymous request to the order-repayment endpoint could mark any order paid with no login, no token, and no contact with any payment gateway."
    publisher: mySites.guru
  - quote: "Every one lists the affected range as 1.0.0 to 2.20.1, which is every Gridbox release there has ever been up to the fix, and four have the exploit maturity Attacked with an urgency of Red, the CVE record’s own way of saying this is being used against real sites rather than sitting as a theoretical risk."
    publisher: mySites.guru
    source_url: "https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/"
  - quote: "the registration handler adds the default group to whatever groups the visitor asks for, instead of replacing them. So anyone can register a normal account and place themselves straight into an administrator group."
    publisher: mySites.guru
  - quote: "We have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now"
    publisher: mySites.guru
  - quote: "Gridbox 2.20.4.1 and earlier"
    publisher: "Balbooa (Gridbox 2.20.4.2 security update)"
    source_url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update"
  - quote: "Neither needs a login, and about 95% of the Gridbox sites we monitor were on an affected version on the morning of the release."
    publisher: mySites.guru
    source_url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
  - quote: "There is no public report of exploitation yet"
    publisher: mySites.guru
    source_url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
verification: multi-source
sourcing_note: >
  mySites.guru is the discloser and the per-vulnerability authority for each of these CVEs; no
  independent second source had covered the first batch at first publication, and those findings
  still rest on mySites.guru alone. The three EasyStore scores are the Joomla CNA's CVSS 4.0 values; the
  Gridbox 10.0 is the discloser's own CVSS 4.0 assessment, while the published CVE record scores
  CVE-2026-61425 9.4 on a high-privileges vector that the discloser says does not match the anonymous
  attack it reproduced; the Membership Pro 9.1 is a CVSS 3.1 score, and the Joomla CNA published no
  score for Events Booking. On CVE-2026-65760 the CNA vector is PR:N but the discloser
  describes the flaw as reachable by any logged-in customer, so it is recorded as post-auth to
  match the stated mechanism. The researcher first withheld the cookie name and endpoints under a
  fix-first policy and printed the cookie in its 2026-07-29 follow-up. The later Gridbox 2.20.2 coverage adds Balbooa's own release notes and
  the Joomla CNA records, four of which record the exploit maturity as Attacked, and mySites.guru
  reports exploitation seen in server access logs and on compromised sites. That corroborated
  batch, which carries the exploitation, is why verification is recorded as multi-source. The
  2.20.3.1 SQL injection rests on mySites.guru's reading of the release diff and carries no CVE
  yet. The 2.20.4.2 pair rests on Balbooa's notice for the affected and fixed versions and the two
  fixes, and on mySites.guru for the Joomla CNA scores and records, the comparison of the two
  packages and the share of affected sites, which are its own measurements; no source reports
  exploitation of these two flaws.
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
  - "Inventory Joomla sites for the Balbooa Gridbox page builder and update every one to 2.20.4.2, which also closes two unauthenticated SQL injections, CVE-2026-102788 and CVE-2026-102789, and the unauthenticated blind SQL injection in the front-end blog author parameter fixed in 2.20.3.1, present in every earlier build, 2.20.3 and 2.20.2.3 included. Anything below 2.20.2 is also exposed to the exploited follow-up batch, which 2.20.1 does not close."
  - "On any site that ran Gridbox 2.20.1 or earlier while internet-reachable, review the Super User list and administrator-group members, remove accounts that entered an admin group through self-registration rather than an explicit administrative action, and review template files and the web root for changes, with particular attention to files written since 20 July, when the cookie bypass was disclosed."
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
  - at: "2026-09-29T23:37:59Z"
    run_id: 2026-09-29T2134Z-audit
    type: update
    summary: >
      All eleven Joomla CNA records for the Gridbox 2.20.2 batch have now published. Seven are
      Critical, and four carry the exploit maturity Attacked: besides CVE-2026-65884 and
      CVE-2026-65885, already recorded here, CVE-2026-65887 resets the password of any account except
      Super Users and CVE-2026-65888 logs the caller in as any user through the social login method,
      both CVSS 4.0 10.0. Both are added. Balbooa has since shipped 2.20.2.3, a hardening release with
      no CVE, and 2.20.3.1, which fixes an unauthenticated blind SQL injection in the blog author
      parameter present in every earlier build, so the action now points at 2.20.3.1. The sourcing
      note reflects the exploitation now recorded and which parts rest on one source. The mySites.guru
      quotation follows the round-up's current text and names the page it comes from, and one phrase
      about how the coverage was produced is reworded. The summary mentions the follow-up releases,
      and verification is recorded as multi-source now that the vendor's release notes are among the
      sources.
    fields: [evidence, cves, sourcing_note, summary, verification, actions, sources, body]
  - at: "2026-10-28T03:52:00Z"
    run_id: 2026-10-28T0256Z-intel
    type: update
    summary: >
      Balbooa released Gridbox 2.20.4.2 on 2026-10-27, fixing two unauthenticated read-side SQL
      injections, CVE-2026-102788 (the sort-by parameter of store and category post lists) and
      CVE-2026-102789 (an editor task without a permission check), both scored CVSS 4.0 9.3 by the Joomla
      CNA and affecting every release up to 2.20.4.1. No exploitation is reported, Joomla 3 sites have no
      fix, and the action now points at 2.20.4.2.
    fields: [actions, body, cves, evidence, sources, sourcing_note, summary]
  - at: "2026-11-01T13:48:38Z"
    run_id: 2026-11-01T1312Z-audit
    type: correction
    summary: >
      The analysis no longer says there is no exploitation signal or that the cookie name is withheld; the
      October 2025 release is treated as a lower bound on exposure, not its start; the CVE record's 9.4
      score beside the discloser's 10.0, Membership Pro's CVSS 3.1 rating and its default-configuration
      impact, Balbooa's wording on web-server rules and the attribution of the read-side reading are
      corrected; the headline is current.
    fields: [actions, body, cves, headline, sourcing_note, summary, title]
migrated_from: null
---

The batch of Joomla extension disclosures mySites.guru published between 2026-07-20 and 2026-07-23 includes a direct authentication failure. In Balbooa's Gridbox page builder, "A critical unauthenticated authentication bypass in Gridbox let anyone become a Super User on a Joomla site by setting a single browser cookie" ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)). The extension treats a client-supplied cookie value as proof of identity rather than as an assertion to be validated against server-side session state, so an anonymous requester who places an administrator's username in that cookie is served the site as that administrator, with no password, no login form and no pre-existing session. Because a Joomla Super User can edit templates, and templates are PHP, the practical outcome is code execution on the web server from a single unauthenticated request. Gridbox 2.20.1 fixes it; the researcher says the vulnerable code shipped for at least nine months and probably far longer, and that the published CVE record's 9.4 score on a high-privileges vector does not match the anonymous attack it reproduced ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)).

The rest of the week's batch is the same research campaign continuing on its original axis, with two flaws that matter beyond the site itself. EasyStore for Joomla carried an unauthenticated SQL injection able to read the whole site database (CVE-2026-65761, scored 9.3 by the Joomla CNA) plus an order-forgery flaw (CVE-2026-65759, 8.7) where "An anonymous request to the order-repayment endpoint could mark any order paid with no login, no token, and no contact with any payment gateway" ([mySites.guru, 2026-07-23](https://mysites.guru/blog/easystore-security-disclosure/)), fixed in 2.0.2. Events Booking exposed invoices containing personal and financial data to anonymous requests that simply walked sequential identifiers, fixed in 5.8.2 ([mySites.guru, 2026-07-21](https://mysites.guru/blog/events-booking-invoice-idor/)). Membership Pro's unauthenticated upload was initially disputed by the vendor: the researcher records that "The vendor called it 'not a critical security issue.' The Joomla CNA disagreed" and it was assigned CVE-2026-62415 at 9.1 critical (CVSS 3.1), an anonymous file write that is not code execution on a default configuration, fixed in Membership Pro 4.6.2 ([mySites.guru, 2026-07-21](https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/)).

The researcher's follow-up of 2026-07-29 prints the cookie, and the further Gridbox flaws its full audit found were exploited while the complete fix was still being finalised, so anything on 2.20.1 or earlier is still exposed ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)); the updates below carry that batch and the later fixes.

**Defender takeaway:** inventory Joomla extensions and their versions, not only the Joomla core version, and treat every Gridbox below 2.20.4.2 as exposed; on a site that ran 2.20.1 or earlier while internet-facing, the account and template review matters as much as the update.

**Triage:** a cookie-forgery bypass leaves little at the network layer to distinguish it: the request is perfectly well formed and contains no payload to detect ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)). The observable is the mismatch between authentication and privilege: administrative actions in Joomla's action log attributed to a Super User account with no preceding successful login event for that account, and no session-establishment record. Legitimate administrator activity is preceded by an authentication event from a consistent source; forged-cookie access produces privileged actions that appear without one. On sites running affected Gridbox versions, template-file modifications with no corresponding administrator login are the artefacts worth reviewing.

## Update — 2026-07-31T04:09:14Z

Balbooa's response to CVE-2026-61425, the cookie flaw fixed in 2.20.1, was to commission the same researcher to audit the whole component, and that audit found 23 further vulnerabilities in this one extension ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). The delta that matters is that 2.20.1 is itself vulnerable to a worse flaw than the one it fixed, and that flaw is being exploited.

CVE-2026-65884 carries a CVSS 4.0 base score of 10.0 for a reason that requires no exploit skill at all: the registration handler adds the usergroup IDs supplied in the request to the default group rather than replacing them, so an anonymous visitor can register an ordinary account and place it directly into an administrator group. The researcher describes the defect precisely: the registration handler "adds the default group to whatever groups the visitor asks for, instead of replacing them," so "anyone can register a normal account and place themselves straight into an administrator group" ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). CVE-2026-65885, scored 9.4, is an authenticated arbitrary file upload, and it becomes remote code execution when chained with the first because the attacker can create the account the upload requires. Both published records give the affected range as 1.0.0 to 2.20.1, every version the extension has ever shipped up to the fix, and both are marked with an exploit maturity of attacked and an urgency of red by the Joomla CNA that assigned them ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)).

Exploitation is not an inference. The researcher reports holding server access logs showing the exploitation requests arriving and describes 92 planted administrator accounts on a single connected Joomla site, created in batches from 27 July, with usernames following one generator's pattern of a fixed prefix plus a few hex characters paired to matching webmail addresses ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Balbooa's own release page corroborates attack traffic indirectly, referring to a recent increase in automated attacks and telling customers who added custom web-server rules to block the recent attacks on Gridbox endpoints to remove them after updating ([Balbooa, 2026-07-29](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)).

Getting to a fixed build took three attempts, which is itself operationally relevant for anyone who applied an interim Gridbox update this month. The researcher's account of the coordinated-disclosure process records that the vendor's first proposed fix left several reported findings live, including an anonymous SQL injection returning password hashes that had been patched at only one of several identical reachable entry points, and that the second closed that and the actively-exploited routes but still left a forgeable payment-gateway callback signature and a SQL injection reachable by a low-privilege authenticated user ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Only 2.20.2, released 2026-07-29, closes all of it, and the vendor states the build was given to the reporting researcher for independent verification before release ([Balbooa, 2026-07-29](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)). The remaining 21 findings are described only by shape, with nine further CVE IDs reserved but unpublished, so the public picture of this component's exposure is not yet complete.

**Detection.** Both halves of the chain leave records in places most Joomla operators already keep. For the privilege escalation, the artifact is a user account whose administrator-group membership was established at creation time rather than by a later administrative change, visible in the user table and in Joomla's own action logs as a registration event that produced an elevated account, with no corresponding admin action. Cluster it by timing: automated abuse of this flaw produces accounts in batches minutes apart, not the trickle of genuine sign-ups. For the upload half, the signal is a file appearing in a web-reachable directory with a server-executable extension, written by the web server user, followed by requests to that path from a small number of sources; in web-server access logs, look for POST requests to the extension's registration and upload endpoints from addresses with no prior browsing history on the site.

**Triage:** a public Joomla site with open registration collects spam accounts constantly, so a new unrecognised user is not the signal. The discriminator is the group membership: ordinary registration spam lands in the default registered-users group and stays there, while these accounts sit in an administrator group from the moment they were created. Any self-registered account holding administrative rights on a Gridbox site should be treated as planted rather than misconfigured.

**Defender takeaway:** this is the second time in ten days that Gridbox, a widely used Joomla page builder, has turned out to accept the attacker's own claim about who they are (a cookie on 20 July, requested group IDs on 29 July). A Joomla estate needs an extension inventory that can answer "which of our sites run Gridbox, at what version" quickly, because patching here is fast and the compromise-assessment afterwards is what takes the time.

## Update — 2026-09-29T23:37:59Z

All eleven CVE records the Joomla CNA assigned to the Gridbox 2.20.2 batch have now published. Every one lists Gridbox 1.0.0 to 2.20.1 as affected, seven are rated Critical, and four carry the exploit maturity Attacked with an urgency of Red ([mySites.guru, revised since](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Two of the four are new to this entry and both are CVSS 4.0 10.0: CVE-2026-65887, a password-reset method that resets any account's password and logs the attacker in as that user, Super Users excepted, and CVE-2026-65888, a social-login method that logs the caller in as any user on the site. mySites.guru reports the exploitation as seen in server access logs and on compromised sites, and the Joomla Security Strike Team reported at least three of the issues exploited on 29 July. The fix for that exploited set is Gridbox 2.20.2. On a site that ran an earlier build while internet-facing, unexpected password resets and social-login sessions for existing accounts belong in the same review as the attacker-registered administrator accounts described above.

Balbooa has shipped three releases since 2.20.2. Version 2.20.2.3 (10 August) is titled "Bug Fixes and Security Hardening" and touches the media manager's access controls, internal path validation and the password-recovery flow, with no CVE, severity or affected range. mySites.guru has not audited it and notes that three of those areas overlap flaws recorded as fixed in 2.20.2 ([mySites.guru, revised since](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Version 2.20.3.1 (21 September) fixes an unauthenticated time-based blind SQL injection in the front-end blog `author` parameter, which went into a database query without being cast to a number. Every build below 2.20.3.1 is affected, 2.20.3 and 2.20.2.3 included, and there is no CVE or CVSS score yet. The vendor filed it as security hardening, and the flaw was reported by Studio Przy Lesie and identified by CERT Polska ([mySites.guru, 2026-09-21](https://mysites.guru/blog/gridbox-author-sql-injection/)). No exploitation of it has been reported. The version to be on then was 2.20.3.1; the later update below moves it to 2.20.4.2. In web-server access telemetry, requests to the Gridbox blog view whose `author` value is not a plain number are the signal, and by inference from the time-based technique, ones that take several seconds to answer are the likelier successful probes. A numeric author filter is normal browsing.

## Update — 2026-10-28T03:52:00Z

Balbooa released Gridbox 2.20.4.2 on 2026-10-27 with two security fixes rated Critical, for the versions 2.20.4.1 and earlier ([Balbooa, 2026-10-27](https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update)). CVE-2026-102788 is in the sort-by URL parameter of store and category post lists and CVE-2026-102789 is a missing permission check on the editor task that loads blog posts ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)); Balbooa's fixes are a strict allowlist validation for the sort-by parameter and a user edit-level check on the editor task ([Balbooa, 2026-10-27](https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update)). mySites.guru says the sort value previously went into the ORDER BY part of the database query and reads the second flaw as a second anonymous route to the same query. mySites.guru reports that the Joomla CNA scores both CVSS 4.0 9.3 and lists every release from 1.0.0 to 2.20.4.1 as affected, and that only two PHP files differ between 2.20.4.1 and 2.20.4.2, one per fix ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)).

mySites.guru reads both flaws as read-side, although the CNA's vector also rates integrity and availability High: an anonymous visitor can extract the Joomla user table, with its password hashes, and every other table the site's extensions created. mySites.guru says about 95% of the Gridbox sites it monitors ran an affected version on the morning of the release, that sites on the Joomla 3 line stop at Gridbox 2.17.0.2, which has no fix for this year's flaws, and that there is no public report of exploitation yet ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)). Nothing here is reported exploited, unlike the July batches above; the version to be on is now 2.20.4.2.

**Detection:** in web access and database query logs, store or category list requests whose sort-by value is not one of the known sort keys, repeated anonymous calls to the Gridbox editor's blog-post task, and slow-query bursts from the web account; since the reported impact is data read out, the post-patch check is credential hygiene on a site that was exposed, starting with administrator accounts nobody created, since the password hashes can be worked on offline.

**Defender takeaway:** update to 2.20.4.2 now, communal and agency sites included, and move Joomla 3 sites to a supported Joomla ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)).

## Correction — 2026-11-01T13:48:38Z

The analysis above still said there was no public exploitation signal and that the researcher withholds the cookie name; the researcher's 2026-07-29 follow-up prints the cookie and reports the follow-up batch exploited, so anything on 2.20.1 or earlier is exposed ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). The October 2025 date is the release before the fix, not the start of exposure: the researcher says the vulnerable code shipped for at least nine months and probably far longer, and that the published CVE record scores CVE-2026-61425 9.4 on a high-privileges vector that does not match the anonymous attack it reproduced ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)). Membership Pro's CVE-2026-62415 is rated 9.1 under CVSS 3.1 and, on a default configuration, is an anonymous file write rather than code execution ([mySites.guru, 2026-07-21](https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/)). Balbooa's 2.20.2 notes address customers who added their own web-server rules against the attacks; they do not say Balbooa had advised them ([Balbooa, 2026-07-29](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)). The "read-side" reading of the 2.20.4.2 pair is mySites.guru's; the CNA's vector also rates integrity and availability High ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)). The compromise review now starts from 20 July, the cookie bypass's disclosure.
