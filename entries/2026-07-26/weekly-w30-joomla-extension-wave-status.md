---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Joomla third-party-extension vulnerability wave status: the mySites.guru campaign added a new technique class this week — a client-supplied cookie accepted as proof of identity, giving anonymous Super User access"
headline: "The tracked Joomla extension wave broadened beyond file-upload RCE — Balbooa Gridbox trusts a cookie value as identity, and six more extension flaws landed"
summary: >
  Update to the Joomla third-party-extension vulnerability wave a prior weekly consolidated as a file-upload-to-RCE cluster. The mySites.guru research campaign produced six further disclosures between 2026-07-20 and 2026-07-23, and one changes the technique class: the Balbooa Gridbox page builder (CVE-2026-61425) trusts a client-supplied cookie value as proof of identity, so setting an administrator's username in that cookie authenticates the requester as that user with no password and no session — and because a Joomla Super User can edit templates (PHP execution), it is full site compromise from a single anonymous request, fixed in Gridbox 2.20.1. The same week added unauthenticated SQL injection and order-forgery in EasyStore, an invoice IDOR in Events Booking, and a critical unauthenticated upload in Membership Pro. The wave is no longer only CWE-434 file uploads; the transferable point for CH/EU municipal and public-sector Joomla estates is that these are anonymous, single-request full-compromise flaws in widely-installed commercial extensions, and prior wave members reached CISA KEV within days.
discovered_at: "2026-07-26T23:47:00Z"
event_date: 2026-07-20
run_id: 2026-07-26T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - pre-auth
  - rce
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
entities:
  - trend:joomla-extension-file-upload-rce-wave
cves: []
techniques:
  - T1190
  - T1505.003
affected_products:
  - "Balbooa Gridbox for Joomla"
sources:
  - url: "https://mysites.guru/blog/gridbox-critical-authentication-bypass/"
    publisher: "mySites.guru"
    date: "2026-07-20"
    role: primary
  - url: "https://mysites.guru/blog/membership-pro-unauthenticated-file-upload/"
    publisher: "mySites.guru"
    date: "2026-07-21"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: "The Gridbox wave is disclosed by mySites.guru, the specialist Joomla-security researcher that drove the tracked wave; treated as single-source (the discloser is the primary and only technical source for these specific extension flaws), consistent with the wave's prior operational coverage. Included as a status delta on an already-consolidated trend, not a new claim."
confidence: high
update_of: 2026-07-12/weekly-w28-joomla-file-upload-rce-wave
references:
  - 2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-12):** the researcher-driven Joomla third-party-extension vulnerability wave a prior weekly consolidated as a file-upload-to-RCE cluster continued this week, and the delta is a new technique class.

The mySites.guru campaign produced six further extension disclosures between 2026-07-20 and 2026-07-23, and the one that matters most is not another file upload. The Balbooa **Gridbox** page builder (CVE-2026-61425) accepts a client-supplied cookie value as proof of identity — mySites.guru describes a critical unauthenticated authentication bypass in Gridbox that lets anyone become a Super User by setting a single cookie value ([mySites.guru, 2026-07-20](https://mysites.guru/blog/gridbox-critical-authentication-bypass/)). Because a Joomla Super User can edit templates, and editing a template is PHP execution, that cookie yields full site compromise from a single anonymous request; the flaw is fixed in Gridbox 2.20.1 and the vulnerable code had shipped since October 2025. Alongside it the week added an unauthenticated upload in Membership Pro, unauthenticated SQL injection and an order-forgery flaw in EasyStore, and an invoice IDOR in Events Booking.

**Defender takeaway:** the wave is no longer describable as "the file-upload extensions" — its common denominator is now anonymous, single-request, full-compromise flaws in commercial Joomla extensions widely installed across CH/EU municipal and public-sector sites, spanning file upload, cookie-as-identity auth bypass, unauthenticated SQL injection and access-control failures. Because prior members of this wave reached CISA KEV within days of disclosure, the operational posture for any public-sector Joomla estate is to inventory installed commercial extensions against this campaign's disclosure list and patch to the fixed versions on a compressed timeline, treating an unpatched, internet-reachable instance running an affected extension as a compromise-assessment candidate rather than a routine update. Per-flaw versions and the full extension list are in the referenced operational entry.
