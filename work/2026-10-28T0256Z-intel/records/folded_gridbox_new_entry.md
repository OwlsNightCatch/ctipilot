---
schema: 1
kind: vulnerability
title: "CVE-2026-102788 / CVE-2026-102789, Balbooa Gridbox for Joomla: two unauthenticated SQL injection routes into the site database through a public sort parameter and an editor task without a permission check, fixed in 2.20.4.2 (CVSS 4.0 9.3)"
headline: "Gridbox 2.20.4.2 fixes two unauthenticated SQL injections in Joomla sites; most monitored sites ran an affected version"
summary: >
  Balbooa released Gridbox version 2.20.4.2 on 2026-10-27 for two unauthenticated SQL injection flaws in the Joomla page builder, CVE-2026-102788
  (the sort-by parameter of store and category post lists) and CVE-2026-102789 (an editor task that loads blog posts without a permission
  check), both scored CVSS 4.0 9.3 by the Joomla CNA and affecting every release up to 2.20.4.1. Both are read-side, so the Joomla user table
  with its password hashes is readable; mySites.guru says about 95% of the Gridbox sites it monitors ran an affected version on the morning of
  the release, and Joomla 3 sites have no fix. No source reports exploitation of these two flaws.
discovered_at: "2026-10-28T03:52:00Z"
updated_at: null
event_date: "2026-10-27"
run_id: 2026-10-28T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, sqli, pre-auth, info-disclosure, patch-available]
regions: [global]
sectors: []
entities: ["product:balbooa-gridbox-for-joomla", "product:joomla"]
techniques: [T1190]
affected_products: ["Balbooa Gridbox for Joomla"]
cves:
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
  - url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update"
    publisher: "Balbooa (Gridbox 2.20.4.2 security update)"
    date: "2026-10-27"
    role: primary
  - url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
    publisher: "mySites.guru"
    date: "2026-10-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Gridbox 2.20.4.1 and earlier"
    publisher: "Balbooa (Gridbox 2.20.4.2 security update)"
    source_url: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update"
  - quote: "In 2.20.4.1 that task had no login or permission check, so an anonymous visitor could call it"
    publisher: "mySites.guru"
    source_url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
  - quote: "Neither needs a login, and about 95% of the Gridbox sites we monitor were on an affected version on the morning of the release."
    publisher: "mySites.guru"
    source_url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
  - quote: "There is no public report of exploitation yet"
    publisher: "mySites.guru"
    source_url: "https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/"
verification: multi-source
sourcing_note: >
  Balbooa's notice is the vendor source for the affected and fixed versions and the two fixes; the CVSS 4.0 scores and the CVE records come from
  mySites.guru's reading of the Joomla CNA records, and its comparison of the two packages and its share of affected sites are its own
  measurements. Gridbox carried an exploited wave in July 2026, covered in the entry listed under references, but no source reports exploitation
  of these two flaws.
confidence: medium
references: ["2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Update Gridbox to 2.20.4.2 on every Joomla site your organisation, its web agencies or its hosting suppliers run, public-facing communal and campaign sites included, and on any site that still runs the Joomla 3 line plan the move to a supported Joomla, because Gridbox 2.17.0.2 has no fix; on a site that was exposed, check the Joomla user list for administrator accounts nobody created."
updates: []
migrated_from: null
---

Balbooa released Gridbox version 2.20.4.2, a Joomla page builder, on 2026-10-27 with two security fixes rated Critical, for the versions 2.20.4.1 and earlier ([Balbooa, 2026-10-27](https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update)). CVE-2026-102788 is in the sort-by URL parameter of store and category post lists, for which Balbooa added a strict allowlist validation in GridboxHelper::getBlogPosts(); mySites.guru says the value previously went into the ORDER BY part of the database query ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)). CVE-2026-102789 is a missing permission check on the editor task EditorController::getBlogPosts(), which Balbooa fixed by adding GridboxHelper::checkUserEditLevel() ([Balbooa, 2026-10-27](https://www.balbooa.com/blog/gridbox/gridbox-2-20-4-2-security-hardening-update)). mySites.guru reads the second as a second anonymous route to the same query, found that only two PHP files differ between 2.20.4.1 and 2.20.4.2, each one of the fixes, and reports that the Joomla CNA scores both CVSS 4.0 9.3 and lists every release from 1.0.0 to 2.20.4.1 as affected ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)).

Both flaws read data: an anonymous visitor can extract the Joomla user table, with its password hashes, and every other table the site's extensions created ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)). mySites.guru says about 95% of the Gridbox sites it monitors ran an affected version on the morning of the release, that sites on the Joomla 3 line stop at Gridbox 2.17.0.2, which has no fix for this year's flaws, and that there is no public report of exploitation yet ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)).

**Exposure:** every Joomla site with the Gridbox extension at 2.20.4.1 or below; the installed version shows in the Joomla administrator's extension manager, and the sort parameter is reachable by any anonymous visitor on a page that renders a Gridbox store or category list ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)).

**Detection:** in web access and database query logs, store or category list requests whose sort-by value is not one of the known sort keys, repeated anonymous calls to the Gridbox editor's blog-post task, and slow-query bursts from the web account; because the flaws only read, the post-patch check is credential hygiene on a site that was exposed, starting with administrator accounts nobody created, since the password hashes can be worked on offline ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)).

**Defender takeaway:** update to 2.20.4.2 now, communal and agency sites included, and move Joomla 3 sites to a supported Joomla; mySites.guru places the actively exploited July Gridbox flaws in versions below 2.20.2, so a site that lagged behind that update needs a check for administrator accounts nobody created ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)).
