---
schema: 1
kind: synthesis
horizon: strategic
title: >
  A researcher-driven Joomla extension file-upload wave produced four unauthenticated RCE
  disclosures this week — several exploited as zero-days before a patch existed
headline: >
  Joomla third-party-extension file-upload RCE wave — four unauthenticated flaws this week,
  several exploited as zero-days, KEV within days
summary: >
  A sustained mySites.guru disclosure wave hit four Joomla third-party extensions across 2026-W28
  — SP Page Builder (CVE-2026-48908) and a second page-builder (CVE-2026-56290), Balbooa Forms
  (CVE-2026-56291), iCagenda (CVE-2026-48939) and RSFiles!/Phoca Download (CVE-2026-57827/57828) —
  every one an arbitrary-file-upload-to-RCE (CWE-434). Several were exploited in the wild as
  zero-days before a fix existed and reached CISA KEV within days, with the observed payload
  planting a hidden Super Administrator account. Any Swiss or European municipal / public-sector
  Joomla site running these extensions should treat an unpatched instance as a compromise event,
  not merely a risk, and hunt for web shells and rogue admin accounts.
discovered_at: "2026-07-12T23:20:00Z"
updated_at: "2026-08-02T23:58:30Z"
event_date: 2026-07-11
run_id: 2026-07-12T2309Z-weekly
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - pre-auth
  - rce
  - zero-day
  - cisa-kev
  - auth-bypass
  - priv-esc
  - sqli
  - patch-available
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - technology
  - education
entities:
  - "trend:joomla-extension-file-upload-rce-wave"
techniques:
  - T1190
  - T1505.003
  - T1136.001
affected_products:
  - Balbooa Gridbox for Joomla
  - Aimy Captcha-Less Form Guard for Joomla
  - JoomShaper SP Page Builder
cves: []
sources:
  - url: "https://mysites.guru/blog/sp-page-builder-zero-day-uploadcustomicon-rce/"
    publisher: mySites.guru
    role: primary
  - url: "https://mysites.guru/blog/balbooa-forms-unauthenticated-file-upload-flaw/"
    publisher: mySites.guru
    role: primary
  - url: "https://mysites.guru/blog/icagenda-zero-day-file-upload-rce/"
    publisher: mySites.guru
    role: primary
  - url: "https://mysites.guru/blog/rsfiles-unauthenticated-file-upload-rce/"
    publisher: mySites.guru
    role: primary
  - url: "https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://mysites.guru/blog/gridbox-critical-authentication-bypass/"
    publisher: mySites.guru
    date: 2026-07-20
    role: primary
  - url: "https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/"
    publisher: mySites.guru
    date: 2026-07-21
    role: primary
  - url: "https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/"
    publisher: mySites.guru
    date: 2026-07-29
    role: primary
  - url: "https://mysites.guru/blog/sp-page-builder-sql-injection-mail-relay-disclosure/"
    publisher: mySites.guru
    date: 2026-07-27
    role: primary
  - url: "https://www.vulncheck.com/blog/aimy-captcha-less-form-guard-object-injection"
    publisher: VulnCheck
    date: 2026-07-30
    role: primary
  - url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release"
    publisher: Balbooa
    date: 2026-07-29
    role: corroborating
closed_sources: []
evidence:
  - quote: "CVE-2026-48908, on the other hand, is said to have been exploited as a zero-day to upload a PHP file by means of an HTTP POST request to the 'index.php?option=com_sppagebuilder&task=asset.uploadCustomIcon' endpoint."
    publisher: The Hacker News
  - quote: "Already exploited in the wild. The payload plants a hidden Super Administrator account, usually with an @secure.local email."
    publisher: mySites.guru
  - quote: "This was a zero-day: it was already being exploited in the wild when we found it, before any patch existed, and those attacks are still going on now against sites that have not updated."
    publisher: mySites.guru
  - quote: "We have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now"
    publisher: mySites.guru
  - quote: "the registration handler adds the default group to whatever groups the visitor asks for, instead of replacing them. So anyone can register a normal account and place themselves straight into an administrator group."
    publisher: mySites.guru
  - quote: "Both list the affected range as 1.0.0 to 2.20.1, which is every Gridbox release there has ever been up to the fix. And both set the exploit maturity to Attacked with an urgency of Red, which is the CVE record's own way of recording that this is being used against real sites rather than sitting as a theoretical risk."
    publisher: mySites.guru
verification: multi-source
sourcing_note: >
  The disclosures originate with a single specialist researcher (mySites.guru) who found several
  of these being exploited in the wild pre-patch; SP Page Builder's zero-day exploitation and its
  endpoint are independently reported by The Hacker News, and iCagenda reached CISA KEV.
  Reliability B reflects a consistent-track-record specialist researcher; credibility 1 for the SP
  Page Builder / iCagenda strands (corroborated by THN and KEV), lower for the not-yet-exploited
  RSFiles!/Phoca pair — see the operational entries.
confidence: high
references:
  - 2026-07-08/joomla-page-builder-cve-2026-48908-56290-kev-zerodays
  - 2026-07-09/cve-2026-56291-balbooa-forms-joomla-unauth-file-upload-rce
  - 2026-07-10/cve-2026-48939-icagenda-joomla-unauth-file-upload-rce-kev
  - 2026-07-11/joomla-rsfiles-phoca-file-upload-rce-cve-2026-57827-57828
  - 2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave
  - 2026-08-01/aimy-captcha-joomla-cve-2026-65883-object-injection-rce
  - 2026-08-02/sp-page-builder-cve-2026-65766-preauth-sqli-mail-relay
weekly_section: weekly-top-stories
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Inventory every internet-facing Joomla site for the affected extensions (SP Page Builder, Balbooa Forms, iCagenda, RSFiles!/com_rsfiles ≤ 1.17.11, Phoca Download/com_phocadownload ≤ 6.1.2) and update to the fixed builds; where no fix is available, take the component offline."
  - "Hunt every Joomla estate for the wave's post-exploitation artifacts: newly created Super Administrator accounts (notably @secure.local addresses) and .php files written into extension upload/download web-root folders."
updates:
  - at: "2026-07-26T23:47:00Z"
    run_id: 2026-07-26T2309Z-weekly
    type: update
    summary: >
      Update to the Joomla third-party-extension vulnerability wave a prior weekly consolidated as a
      file-upload-to-RCE cluster. The mySites.guru research campaign produced six further disclosures
      between 2026-07-20 and 2026-07-23, and one changes the technique class: the Balbooa Gridbox page
      builder (CVE-2026-61425) trusts a client-supplied cookie value as proof of identity, so setting
      an administrator's username in that cookie authenticates the requester as that user with no
      password and no session — and because a Joomla Super User can edit templates (PHP execution), it
      is full site compromise from a single anonymous request, fixed in Gridbox 2.20.1. The same week
      added unauthenticated SQL injection and order-forgery in EasyStore, an invoice IDOR in Events
      Booking, and a critical unauthenticated upload in Membership Pro. The wave is no longer only
      CWE-434 file uploads; the transferable point for CH/EU municipal and public-sector Joomla
      estates is that these are anonymous, single-request full-compromise flaws in widely-installed
      commercial extensions, and prior wave members reached CISA KEV within days.
    fields:
      - affected_products
      - references
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-07-26/weekly-w30-joomla-extension-wave-status
  - at: "2026-08-02T23:58:30Z"
    run_id: 2026-08-02T2311Z-weekly
    type: update
    summary: >
      Status update on the Joomla third-party-extension vulnerability wave prior weeklies tracked from
      a file-upload-to-RCE cluster through a cookie-as-identity auth bypass. The delta this week is
      evidentiary rather than technical: a vendor-commissioned follow-on audit of Balbooa Gridbox
      found 22 further vulnerabilities in the single component, and a 23rd surfaced not from the audit
      but alongside the live exploitation — the anonymous-registration privilege escalation now
      tracked as CVE-2026-65884. The researcher reports server access logs showing exploitation
      requests arriving plus 92 planted administrator accounts on one connected site — the wave's
      first member with logged in-the-wild abuse rather than disclosure-only status. The Joomla CNA
      marks both Gridbox CVEs as attacked. Cadence continued at the same rate: an unauthenticated PHP
      object injection in Aimy Captcha-Less Form Guard and a five-CVE batch in JoomShaper SP Page
      Builder including an effectively pre-authentication SQL injection that returns the whole Joomla
      database.
    fields:
      - affected_products
      - evidence
      - references
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-02/weekly-w31-joomla-extension-wave-status
migrated_from: null
---

**If you did nothing this week:** any internet-facing Joomla site your constituency runs with SP Page Builder, Balbooa Forms, iCagenda, RSFiles! or Phoca Download installed should now be treated as potentially compromised — several of these flaws were exploited in the wild before a patch shipped, and the observed payload gives the attacker a hidden Joomla super-admin.

Across 2026-W28 the specialist Joomla-security researcher mySites.guru disclosed the same bug class — CWE-434 arbitrary file upload leading to remote code execution — in four separate third-party extensions in quick succession, and CISA moved several onto the Known Exploited Vulnerabilities catalog within days. The mechanism is consistent: an upload handler that fails to enforce a server-side extension allow-list, does not block `.php`, and does not verify the declared content type, letting an attacker write an executable script into a web-reachable directory. In SP Page Builder the exploited path was `index.php?option=com_sppagebuilder&task=asset.uploadCustomIcon`, driven by an HTTP POST ([The Hacker News, 2026-07-08](https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html)); the researcher observed that "the payload plants a hidden Super Administrator account, usually with an @secure.local email" ([mySites.guru, 2026-07-08](https://mysites.guru/blog/sp-page-builder-zero-day-uploadcustomicon-rce/)). Balbooa Forms (CVE-2026-56291) was likewise found under live exploitation before any fix existed — "it was already being exploited in the wild when we found it, before any patch existed" ([mySites.guru, 2026-07-09](https://mysites.guru/blog/balbooa-forms-unauthenticated-file-upload-flaw/)) — and iCagenda (CVE-2026-48939) reached KEV as an unauthenticated file-upload-to-RCE ([mySites.guru, 2026-07-10](https://mysites.guru/blog/icagenda-zero-day-file-upload-rce/)). The week closed with two more from the same wave: RSFiles! (CVE-2026-57827, unauthenticated, CVSS 4.0 10.0, fixed 1.17.12) and Phoca Download (CVE-2026-57828, member-authenticated allow-list bypass, fixed 6.1.3), with no confirmed exploitation of that pair yet ([mySites.guru, 2026-07-11](https://mysites.guru/blog/rsfiles-unauthenticated-file-upload-rce/)).

**Why this is the week's operational reality for the constituency:** Joomla is disproportionately common on cantonal, communal and small-agency public-sector sites across Switzerland and the EU, and the ecosystem's risk lives in its third-party extensions, not the core. A wave of unauthenticated, pre-auth-exploited RCEs against exactly that surface, several with a public exploitation record and a self-installing super-admin payload, is a patch-and-hunt priority the normal monthly cadence does not cover.

**Defender takeaway:** treat the extension inventory — not the Joomla core version — as the exposure surface; update or remove every affected component now, and because at least three of these were exploited pre-patch, assume any lagging instance may already carry a web shell or rogue admin. **Triage:** a legitimate Joomla file-upload writes into a media/asset path an authenticated editor triggered; the wave's signal is a `.php` (or double-extension) file appearing in an extension's upload/download folder from an unauthenticated request, frequently followed by the creation of a Super Administrator account with a synthetic domain such as `@secure.local`.

## Update — 2026-07-26T23:47:00Z

The researcher-driven Joomla third-party-extension vulnerability wave a prior weekly consolidated as a file-upload-to-RCE cluster continued this week, and the delta is a new technique class.

The mySites.guru campaign produced six further extension disclosures between 2026-07-20 and 2026-07-23, and the one that matters most is not another file upload. The Balbooa **Gridbox** page builder (CVE-2026-61425) accepts a client-supplied cookie value as proof of identity — mySites.guru describes a critical unauthenticated authentication bypass in Gridbox that lets anyone become a Super User by setting a single cookie value ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)). Because a Joomla Super User can edit templates, and editing a template is PHP execution, that cookie yields full site compromise from a single anonymous request; the flaw is fixed in Gridbox 2.20.1 and the vulnerable code had shipped since October 2025. Alongside it the week added an unauthenticated upload in Membership Pro, unauthenticated SQL injection and an order-forgery flaw in EasyStore, and an invoice IDOR in Events Booking.

**Defender takeaway:** the wave is no longer describable as "the file-upload extensions" — its common denominator is now anonymous, single-request, full-compromise flaws in commercial Joomla extensions widely installed across CH/EU municipal and public-sector sites, spanning file upload, cookie-as-identity auth bypass, unauthenticated SQL injection and access-control failures. Because prior members of this wave reached CISA KEV within days of disclosure, the operational posture for any public-sector Joomla estate is to inventory installed commercial extensions against this campaign's disclosure list and patch to the fixed versions on a compressed timeline, treating an unpatched, internet-reachable instance running an affected extension as a compromise-assessment candidate rather than a routine update. Per-flaw versions and the full extension list are in the referenced operational entry.

## Update — 2026-08-02T23:58:30Z

The prior weekly recorded this wave broadening beyond file-upload RCE into a cookie-trusted-as-identity auth bypass, with no member yet confirmed exploited in the wild. That changed this week.

A follow-on source-code audit of Balbooa Gridbox, commissioned by the vendor after its earlier authentication-bypass disclosure, found 22 further vulnerabilities in that one component — and the researcher is explicit that the flaw this entry leads on was not among them: "Number 23 is not from the audit. It surfaced alongside the active exploitation" ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Its mechanism is a single line of logic: "the registration handler adds the default group to whatever groups the visitor asks for, instead of replacing them. So anyone can register a normal account and place themselves straight into an administrator group." ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Chained with an authenticated arbitrary file upload, that becomes end-to-end unauthenticated remote code execution. The affected range is total — the researcher notes that both CNA records "list the affected range as 1.0.0 to 2.20.1, which is every Gridbox release there has ever been up to the fix. And both set the exploit maturity to Attacked with an urgency of Red, which is the CVE record's own way of recording that this is being used against real sites rather than sitting as a theoretical risk." ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)), with the complete fix in Gridbox 2.20.2 ([Balbooa, 2026-07-29](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)). Note that 2.20.1 was itself the fix for the prior weekly's cookie-forgery flaw, so a site that patched in response to that disclosure is still exposed to these.

What moves the wave's status is the evidence class rather than the severity. Previous members were disclosed, sometimes with a public proof-of-concept, occasionally KEV-listed later. This one arrives with logs: "we have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now" ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). Ninety-two planted administrator accounts on a single site is not opportunistic scanning; it is an automated campaign that has already run.

Cadence did not slow. VulnCheck disclosed an unauthenticated PHP object injection in Aimy Captcha-Less Form Guard, where the anti-spam token is deserialized with no signature and the XOR keystream needed to forge it ships in the same page ([VulnCheck, 2026-07-30](https://www.vulncheck.com/blog/aimy-captcha-less-form-guard-object-injection)). And mySites.guru reported four vulnerabilities in JoomShaper SP Page Builder — 6.7.1 closes five in total, the fifth being one the discloser states it neither reported nor tested — the sharpest of them being an `ORDER BY` injection whose only guard is a Joomla anti-CSRF token that Joomla issues to every anonymous visitor — making it effectively pre-authentication SQL injection returning the entire Joomla database, password hashes included ([mySites.guru, 2026-07-27](https://mysites.guru/blog/sp-page-builder-sql-injection-mail-relay-disclosure/)).

**Defender takeaway:** for the Swiss and European municipal, cantonal and public-sector Joomla estates this wave targets, the operative point is that these components are not discoverable from outside. An internet-wide scan does not enumerate which commercial extensions a site has installed, and one of this week's three only renders on the specific forms an administrator attached it to. The inventory has to come from the Joomla extension manager on each site, which makes a central register of installed extensions across the estate the prerequisite for responding to this wave at all — and the wave has now produced three disclosures in one week from one researcher, so the register is going to be needed again. Where a site ran an affected version while reachable, the Gridbox case gives a concrete artifact to hunt rather than a general suspicion: administrator-group members whose account creation and group assignment happened in the same transaction.
