---
schema: 1
kind: vulnerability
title: "Sourcerer for Joomla: unauthenticated RCE exploited in the wild since before a working fix existed — the vendor's first two patches did not close it, and the CVE was re-scoped in place to widen the affected range"
headline: "Every site that 'patched' Sourcerer between 17 and 26 August was exploitable the entire time, and its own extension manager said otherwise"
summary: >
  CVE-2026-74253 (CVSS 4.0 10.0) in Regular Labs' Sourcerer, the Joomla extension that renders
  embedded PHP/JS/CSS, has been under active exploitation since roughly 2026-08-19 per the Joomla
  Security Strike Team — two days after the vendor's first "fix" shipped and seven days before a
  working one existed. Only 16.0.0 (26 Aug) closes it; the Joomla CNA re-scoped the CVE's affected
  range in place from 1.0.0-13.1.1 to 1.0.0-15.0.0, meaning sites that updated to 14.0.0, 14.0.1 or
  15.0.0 in good faith were exploitable throughout.
discovered_at: "2026-08-28T05:35:00Z"
updated_at: null
event_date: "2026-08-19"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, actively-exploited, patch-available]
regions: [global]
sectors: [public-sector]
entities: [trend:joomla-extension-file-upload-rce-wave]
techniques: [T1190, T1059]
affected_products: ["Sourcerer for Joomla (plg_system_sourcerer, plg_editors-xtd_sourcerer)"]
cves:
  - id: CVE-2026-74253
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "Sourcerer 1.0.0–15.0.0 (re-scoped in place from an original 1.0.0–13.1.1; 14.0.0, 14.0.1 and 15.0.0 were affected despite being presented as fixes)"
    fixed: "16.0.0"
  - id: CVE-2026-64796
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Sourcerer 1.0.0–12.2.8 — closed only the article-content path, does not protect against CVE-2026-74253"
    fixed: "13.0.0"
sources:
  - url: "https://mysites.guru/blog/sourcerer-14-unverified-content-php-execution/"
    publisher: "mySites.guru"
    date: "2026-08-26"
    role: primary
closed_sources: []
evidence:
  - quote: "The Joomla CNA widened CVE-2026-74253 from \"Sourcerer < 14.0.0\" to \"Sourcerer < 16.0.0\", moving the affected range from 1.0.0-13.1.1 to 1.0.0-15.0.0, after the vendor's first two attempts at a fix turned out not to close the flaw."
    publisher: "mySites.guru"
  - quote: "Exploited Yes, in the wild since roughly 19 August 2026 per the Joomla Security Strike Team, confirmed to us 24 August 2026."
    publisher: "mySites.guru, citing the Joomla Security Strike Team"
  - quote: "Code written in a WYSIWYG editor arrives with its angle brackets converted to HTML entities. So that code still runs, Sourcerer decodes entities inside its own tags before handling the contents."
    publisher: "mySites.guru"
verification: single-source
sourcing_note: >
  mySites.guru is the primary technical source; the Joomla Security Strike Team's confirmation of
  in-the-wild exploitation is reported via mySites.guru's own direct correspondence with JSST
  member David Jardin rather than an independent JSST publication this run could locate — carried
  as reported.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade Sourcerer to 16.0.0 immediately on every Joomla site, and treat any site that updated to 14.0.0, 14.0.1 or 15.0.0 between 17 and 26 August as having been exploitable the entire window regardless of what the extension manager reported — the CVE's own affected range was widened after the fact to admit this."
  - "Do not rely on HTML-escaping as a compensating control while awaiting the 16.0.0 upgrade — Sourcerer decodes HTML entities inside its own tags by design, so escaped input still executes."
updates: []
migrated_from: null
---

CVE-2026-74253 (Regular Labs' Sourcerer, the Joomla extension that renders PHP, JS and CSS embedded in content) is CWE-94 (Improper Control of Generation of Code), CVSS 4.0 10.0 (`AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H` — every metric at its worst), credited to finder Lukasz Rybak. Before Sourcerer 14.0.0, only article-text content had its origin verified before Sourcerer would execute embedded code; code reaching the page through a module, component, page head, or any other rendering position ran unconditionally. 14.0.0 (17 Aug) added trust-marking for article content and unmodified custom-module output, but did not close every route by which untrusted content could reach the render — URL and form parameters, raw request bodies, uploads, cookies and headers all remained live — and the CVE record originally scoped the fix as "<14.0.0", affected 1.0.0–13.1.1.

The flaw has been under active exploitation since roughly 2026-08-19 per the Joomla Security Strike Team: "Exploited Yes, in the wild since roughly 19 August 2026 per the Joomla Security Strike Team, confirmed to us 24 August 2026" ([mySites.guru, citing the Joomla Security Strike Team, 2026-08-26](https://mysites.guru/blog/sourcerer-14-unverified-content-php-execution/)) — two days after the first "fix" shipped and seven days before a working one existed. Sourcerer 15.0.0, also never tagged a security release, also failed to close it. Only 16.0.0 (26 Aug) closes the untrusted-input-delivery routes and additionally blocks common filesystem-write PHP functions by default. On 2026-08-26 the Joomla CNA re-scoped CVE-2026-74253 in place, widening the affected range from 1.0.0–13.1.1 to 1.0.0–15.0.0: "the Joomla CNA widened CVE-2026-74253 from 'Sourcerer < 14.0.0' to 'Sourcerer < 16.0.0', moving the affected range from 1.0.0-13.1.1 to 1.0.0-15.0.0, after the vendor's first two attempts at a fix turned out not to close the flaw" ([mySites.guru, 2026-08-26](https://mysites.guru/blog/sourcerer-14-unverified-content-php-execution/)) — meaning every site that updated to 14.0.0, 14.0.1 or 15.0.0 in good faith, told by both its extension manager and the CVE record itself that it was patched, was exploitable the entire time.

HTML-escaping input is explicitly not a mitigation here, and the reason is design rather than oversight: "code written in a WYSIWYG editor arrives with its angle brackets converted to HTML entities. So that code still runs, Sourcerer decodes entities inside its own tags before handling the contents" ([mySites.guru, 2026-08-26](https://mysites.guru/blog/sourcerer-14-unverified-content-php-execution/)) — the decoding cannot distinguish administrator-typed code from attacker-supplied text. PHP execution is enabled by default; the default forbidden-function list blocks shell-exec functions but not file-write functions. A separate, earlier CVE, CVE-2026-64796 (fixed in 13.0.0, affected 1.0.0–12.2.8), closed only the article-content path and does not protect against this one.

**Triage:** any site that "patched" Sourcerer to 14.x or 15.0.0 between 17 and 26 August must be re-verified against 16.0.0 and treated as having been exposed the entire window regardless of what its extension manager reported. Look for PHP execution originating from content-rendering code paths outside article bodies — module output, page-head injection, or request-parameter-derived content reaching Sourcerer's render function — since that is exactly the delivery route the 14.0.0/15.0.0 fixes failed to close. A web-server process spawning a shell or writing new PHP files to disk from within Joomla's content-rendering pipeline has no legitimate explanation.
