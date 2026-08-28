---
schema: 1
kind: vulnerability
horizon: operational
title: "iCagenda Calendar module for Joomla: unauthenticated SQL injection via com_ajax needs no session, token or account (CVE-2026-67365, CVSS 9.2) — and the vulnerable module's own version number does not track the package version"
headline: "A Joomla events extension's bundled Calendar module can stay vulnerable for three package releases without the extension manager ever showing it"
summary: >
  The Joomla CNA published CVE-2026-67365 on 2026-08-14: an unauthenticated SQL injection in
  mod_icagenda_calendar, the Calendar module bundled with iCagenda, reachable via Joomla's
  anonymous front-end AJAX entry point with no session, token or account required. Affected
  4.0.0–4.0.11; fixed in 4.0.12. The Calendar module's own version stayed pinned at 4.0.7 through
  three intervening package releases, so a site's extension manager can show a current-looking
  package version while the actually-vulnerable module component is untouched.
discovered_at: "2026-08-28T05:32:00Z"
updated_at: null
event_date: "2026-08-14"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, sqli, pre-auth, patch-available]
regions: [global]
sectors: [public-sector]
entities: [trend:joomla-extension-file-upload-rce-wave]
techniques: [T1190]
affected_products: ["iCagenda (mod_icagenda_calendar) for Joomla"]
cves:
  - id: CVE-2026-67365
    cvss: "9.2"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "iCagenda mod_icagenda_calendar 4.0.0–4.0.11 (module version pinned at 4.0.7 through package releases 4.0.8–4.0.11)"
    fixed: "4.0.12"
sources:
  - url: "https://mysites.guru/blog/icagenda-calendar-module-sql-injection/"
    publisher: "mySites.guru"
    date: "2026-08-17"
    role: primary
closed_sources: []
evidence:
  - quote: "Joomla Extension - icagenda.com - Unauthenticated SQL injection in iCagenda < 4.0.0-4.0.11 - Unauthenticated SQL injection in mod_icagenda_calendar (iCagenda), reachable via com_ajax with no session, token or account."
    publisher: "Joomla CNA (CVE-2026-67365 record), quoted by mySites.guru"
  - quote: "The Calendar module stayed at 4.0.7 through the 4.0.8, 4.0.9, 4.0.10 and 4.0.11 releases and only moved with 4.0.12, so the module version and the package version disagree and a site can look patched when it is not."
    publisher: "mySites.guru"
  - quote: "The feed still lists 4.0.11 from this date and nothing above it, even though 4.0.12 is shipping and installing on real sites. A site running an update check is told it is current."
    publisher: "mySites.guru"
verification: single-source
sourcing_note: >
  mySites.guru reports the Joomla CNA's own CVE record and disclosure credit (Joep van Antwerpen
  of Onvio, not mySites.guru's own find); no vendor advisory or changelog entry exists for this fix
  separately from the CVE record itself at time of writing.
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
  - "Upgrade iCagenda to 4.0.12 or later by manually downloading the release rather than trusting an automated update-status check — the Calendar module's own version stayed pinned at 4.0.7 through package releases 4.0.8-4.0.11, and iCagenda's own update feed had not yet been updated to list 4.0.12 as of this run, so both the extension manager's package version and an automated update check can each independently report a vulnerable site as current."
updates: []
migrated_from: null
---

The Joomla project's CNA published CVE-2026-67365 on 2026-08-14: an unauthenticated SQL injection (CWE-89) in `mod_icagenda_calendar`, the Calendar module bundled with the iCagenda events extension, reachable via `com_ajax` — Joomla's generic anonymous front-end AJAX entry point — with no session, token or account required. Rated CVSS 4.0 9.2 Critical (`AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:L/VA:L/SC:H/SI:H/SA:H`): "Joomla Extension - icagenda.com - Unauthenticated SQL injection in iCagenda < 4.0.0-4.0.11 - Unauthenticated SQL injection in mod_icagenda_calendar (iCagenda), reachable via com_ajax with no session, token or account" ([Joomla CNA record, quoted by mySites.guru, 2026-08-17](https://mysites.guru/blog/icagenda-calendar-module-sql-injection/)). Affected 4.0.0–4.0.11; fixed in 4.0.12. The flaw was reported by Joep van Antwerpen of Onvio, not mySites.guru's own find.

The operationally important detail is a version-tracking trap: the vulnerable Calendar module's own version number stayed pinned at 4.0.7 through package releases 4.0.8, 4.0.9, 4.0.10 and 4.0.11, and only advanced to 4.0.12 with the fix — "The Calendar module stayed at 4.0.7 through the 4.0.8, 4.0.9, 4.0.10 and 4.0.11 releases and only moved with 4.0.12, so the module version and the package version disagree and a site can look patched when it is not." ([mySites.guru, 2026-08-17](https://mysites.guru/blog/icagenda-calendar-module-sql-injection/)). A naive version check against the package number — in either direction — gives a wrong answer for this specific component. A second, independent detection trap sits upstream of that: at the time of mySites.guru's writing, iCagenda's own update feed had not yet been updated to list 4.0.12, even though the fixed release was already shipping and installing on real sites — "the feed still lists 4.0.11 from this date and nothing above it, even though 4.0.12 is shipping and installing on real sites. A site running an update check is told it is current" ([mySites.guru, 2026-08-17](https://mysites.guru/blog/icagenda-calendar-module-sql-injection/)), meaning an automated update-status check could report a vulnerable site as current independent of the module-version trap above. No vendor advisory or changelog entry exists for this fix beyond the CVE record itself at time of writing. This is the second security issue in iCagenda in two months and unrelated to the first: CVE-2026-48939, an unauthenticated file-upload flaw already CISA-KEV-listed, was fixed in 4.0.8/3.9.15 and does not cover this SQL injection.

**Triage:** hunt and inventory tooling should key on the Calendar module's own reported version, not the iCagenda package version, when assessing exposure to this specific CVE. On the wire, unauthenticated `com_ajax` requests targeting the iCagenda calendar component carrying SQL-metacharacter payloads in parameters are the delivery shape; iCagenda's legitimate calendar AJAX traffic carries only structured date/view parameters, so a request with SQL syntax in those fields has no benign explanation.
