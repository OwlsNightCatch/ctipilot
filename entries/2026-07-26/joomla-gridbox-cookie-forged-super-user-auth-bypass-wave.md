---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-61425 — Balbooa Gridbox for Joomla: a client-supplied cookie is accepted as proof of identity, giving anonymous Super User access"
headline: "The Joomla extension disclosure wave adds a cookie-forgery auth bypass — one anonymous request reaches Super User, and Super User means PHP"
summary: >
  The mySites.guru research campaign against Joomla third-party extensions produced six further
  disclosures between 2026-07-20 and 2026-07-23, and one of them changes technique class: the
  Balbooa Gridbox page builder (CVE-2026-61425) trusts a client-supplied cookie value as proof
  of identity, so setting an administrator's username in that cookie authenticates the requester
  as that user with no password and no existing session. A Joomla Super User can edit templates,
  which is PHP execution, so this is full site compromise from a single anonymous request. Fixed
  in Gridbox 2.20.1; the vulnerable code had shipped since October 2025. The same week added
  unauthenticated SQL injection and order-forgery flaws in EasyStore, an invoice IDOR in Events
  Booking, and a critical unauthenticated upload in Membership Pro.
discovered_at: "2026-07-26T14:08:00Z"
event_date: "2026-07-20"
run_id: 2026-07-26T1308Z-audit
priority: notable
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, sqli, rce, patch-available]
regions: [europe, global]
sectors: [public-sector, education]
entities: [trend:joomla-extension-file-upload-rce-wave]
techniques: [T1190, T1505.003]
affected_products: ["Balbooa Gridbox", "JoomShaper EasyStore", "Joomla Events Booking", "Joomla Membership Pro"]
cves:
  - id: CVE-2026-61425
    cvss: "10.0 (CVSS 4.0, discloser's own assessment)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Balbooa Gridbox before 2.20.1 (vulnerable code shipped from the October 2025 release)"
    fixed: "Gridbox 2.20.1"
  - id: CVE-2026-65759
    cvss: "8.7 (CVSS 4.0)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "JoomShaper EasyStore for Joomla before 2.0.2"
    fixed: "EasyStore 2.0.2"
  - id: CVE-2026-65760
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "JoomShaper EasyStore for Joomla before 2.0.2"
    fixed: "EasyStore 2.0.2"
  - id: CVE-2026-65761
    cvss: "9.3 (CVSS 4.0)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "JoomShaper EasyStore for Joomla before 2.0.2"
    fixed: "EasyStore 2.0.2"
  - id: CVE-2026-63047
    cvss: null
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Events Booking for Joomla before 5.8.2"
    fixed: "Events Booking 5.8.2"
  - id: CVE-2026-62415
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Membership Pro for Joomla before 4.6.2"
    fixed: "Membership Pro 4.6.2"
sources:
  - url: "https://mysites.guru/blog/gridbox-critical-authentication-bypass/"
    publisher: "mySites.guru"
    date: "2026-07-20"
    role: primary
  - url: "https://mysites.guru/blog/easystore-security-disclosure/"
    publisher: "mySites.guru"
    date: "2026-07-23"
    role: primary
  - url: "https://mysites.guru/blog/events-booking-invoice-idor/"
    publisher: "mySites.guru"
    date: "2026-07-21"
    role: primary
  - url: "https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/"
    publisher: "mySites.guru"
    date: "2026-07-21"
    role: primary
closed_sources: []
evidence:
  - quote: "A critical unauthenticated authentication bypass in Gridbox let anyone become a Super User on a Joomla site by setting a single browser cookie"
    publisher: "mySites.guru"
  - quote: "An anonymous request to the order-repayment endpoint could mark any order paid with no login, no token, and no contact with any payment gateway."
    publisher: "mySites.guru"
verification: single-source
sourcing_note: "mySites.guru is the discloser and the per-vulnerability authority for each of these CVEs; no independent second source has covered the batch yet. Scores are CVSS 4.0: the three EasyStore values are the Joomla CNA's, while the Gridbox 10.0 is the discloser's own stated assessment rather than a CNA score, and Events Booking carries none. On CVE-2026-65760 the CNA vector is PR:N but the discloser describes the flaw as reachable by any logged-in customer, so it is recorded as post-auth to match the stated mechanism. The researcher withholds endpoint detail and proof-of-concept code under a fix-first policy, so there is no public exploitation signal."
confidence: medium
update_of: null
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
migrated_from: null
---

The Joomla third-party-extension disclosure wave this pipeline has been tracking has been a file-upload story: unauthenticated uploads reaching code execution, several of which were weaponised and CISA-KEV-listed within days of disclosure. The batch mySites.guru published between 2026-07-20 and 2026-07-23 adds a different and more direct failure. In Balbooa's Gridbox page builder, "A critical unauthenticated authentication bypass in Gridbox let anyone become a Super User on a Joomla site by setting a single browser cookie" ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)). The extension treats a client-supplied cookie value as proof of identity rather than as an assertion to be validated against server-side session state, so an anonymous requester who places an administrator's username in that cookie is served the site as that administrator — no password, no login form, no pre-existing session. Because a Joomla Super User can edit templates, and templates are PHP, the practical outcome is code execution on the web server from a single unauthenticated request. Gridbox 2.20.1 fixes it; the vulnerable code had shipped since the previous release in October 2025, roughly nine months of exposure.

The rest of the week's batch is the same research campaign continuing on its original axis, with two flaws that matter beyond the site itself. EasyStore for Joomla carried an unauthenticated SQL injection able to read the whole site database (CVE-2026-65761, scored 9.3 by the Joomla CNA) plus an order-forgery flaw (CVE-2026-65759, 8.7) where "An anonymous request to the order-repayment endpoint could mark any order paid with no login, no token, and no contact with any payment gateway" ([mySites.guru, 2026-07-23](https://mysites.guru/blog/easystore-security-disclosure/)), fixed in 2.0.2. Events Booking exposed invoices containing personal and financial data to anonymous requests that simply walked sequential identifiers, fixed in 5.8.2 ([mySites.guru, 2026-07-21](https://mysites.guru/blog/events-booking-invoice-idor/)). Membership Pro's unauthenticated upload was initially disputed by the vendor — the researcher records that "The vendor called it 'not a critical security issue.' The Joomla CNA disagreed" and it was assigned CVE-2026-62415 at 9.1 critical, fixed in Membership Pro 4.6.2 ([mySites.guru, 2026-07-21](https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/)).

There is no public exploitation signal for any of these: the researcher withholds the exact cookie name, endpoints and proof-of-concept code under a fix-first policy. The reason to act ahead of the routine extension-update cycle is the wave's own track record rather than current telemetry — earlier members of this same disclosure series moved from publication to confirmed in-the-wild exploitation within days once the mechanism became public, and a cookie-forgery bypass is trivially rediscovered by anyone who diffs the 2.20.1 release against its predecessor.

**Defender takeaway:** Joomla is common in European public-sector, municipal and education web estates, and this class of flaw sits in third-party extensions that rarely appear in vulnerability-management inventories keyed on the CMS core version. Enumerate installed extensions and their versions as first-class inventory, not as a property of the Joomla install, and prioritise Gridbox given the nine-month exposure window and the anonymous-to-admin outcome.

**Triage:** a cookie-forgery bypass leaves little at the network layer to distinguish it — the request is well-formed and returns HTTP 200. The observable is the mismatch between authentication and privilege: administrative actions in Joomla's action log attributed to a Super User account with no preceding successful login event for that account, and no session-establishment record. Legitimate administrator activity is preceded by an authentication event from a consistent source; forged-cookie access produces privileged actions that appear without one. On sites running affected Gridbox versions, template-file modification timestamps postdating the October 2025 release, with no corresponding administrator login, are the artefacts worth reviewing.
