---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: A researcher-driven Joomla extension file-upload wave produced four unauthenticated RCE disclosures this week — several exploited as zero-days before a patch existed
headline: Joomla third-party-extension file-upload RCE wave — four unauthenticated flaws this week, several exploited as zero-days, KEV within days
summary: A sustained mySites.guru disclosure wave hit four Joomla third-party extensions across 2026-W28 — SP Page Builder (CVE-2026-48908) and a second page-builder (CVE-2026-56290), Balbooa Forms (CVE-2026-56291), iCagenda (CVE-2026-48939) and RSFiles!/Phoca Download (CVE-2026-57827/57828) — every one an arbitrary-file-upload-to-RCE (CWE-434). Several were exploited in the wild as zero-days before a fix existed and reached CISA KEV within days, with the observed payload planting a hidden Super Administrator account. Any Swiss or European municipal / public-sector Joomla site running these extensions should treat an unpatched instance as a compromise event, not merely a risk, and hunt for web shells and rogue admin accounts.
discovered_at: '2026-07-12T23:20:00Z'
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
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
entities:
  - trend:joomla-extension-file-upload-rce-wave
cves: []
sources:
  - url: https://mysites.guru/blog/sp-page-builder-zero-day-uploadcustomicon-rce/
    publisher: mySites.guru
    role: primary
  - url: https://mysites.guru/blog/balbooa-forms-unauthenticated-file-upload-flaw/
    publisher: mySites.guru
    role: primary
  - url: https://mysites.guru/blog/icagenda-zero-day-file-upload-rce/
    publisher: mySites.guru
    role: primary
  - url: https://mysites.guru/blog/rsfiles-unauthenticated-file-upload-rce/
    publisher: mySites.guru
    role: primary
  - url: https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: CVE-2026-48908, on the other hand, is said to have been exploited as a zero-day to upload a PHP file by means of an HTTP POST request to the 'index.php?option=com_sppagebuilder&task=asset.uploadCustomIcon' endpoint.
    publisher: The Hacker News
  - quote: Already exploited in the wild. The payload plants a hidden Super Administrator account, usually with an @secure.local email.
    publisher: mySites.guru
  - quote: 'This was a zero-day: it was already being exploited in the wild when we found it, before any patch existed, and those attacks are still going on now against sites that have not updated.'
    publisher: mySites.guru
verification: multi-source
sourcing_note: The disclosures originate with a single specialist researcher (mySites.guru) who found several of these being exploited in the wild pre-patch; SP Page Builder's zero-day exploitation and its endpoint are independently reported by The Hacker News, and iCagenda reached CISA KEV. Reliability B reflects a consistent-track-record specialist researcher; credibility 1 for the SP Page Builder / iCagenda strands (corroborated by THN and KEV), lower for the not-yet-exploited RSFiles!/Phoca pair — see the operational entries.
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - 2026-07-08/joomla-page-builder-cve-2026-48908-56290-kev-zerodays
  - 2026-07-09/cve-2026-56291-balbooa-forms-joomla-unauth-file-upload-rce
  - 2026-07-10/cve-2026-48939-icagenda-joomla-unauth-file-upload-rce-kev
  - 2026-07-11/joomla-rsfiles-phoca-file-upload-rce-cve-2026-57827-57828
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - Inventory every internet-facing Joomla site for the affected extensions (SP Page Builder, Balbooa Forms, iCagenda, RSFiles!/com_rsfiles ≤ 1.17.11, Phoca Download/com_phocadownload ≤ 6.1.2) and update to the fixed builds; where no fix is available, take the component offline.
  - 'Hunt every Joomla estate for the wave''s post-exploitation artifacts: newly created Super Administrator accounts (notably @secure.local addresses) and .php files written into extension upload/download web-root folders.'
---
**If you did nothing this week:** any internet-facing Joomla site your constituency runs with SP Page Builder, Balbooa Forms, iCagenda, RSFiles! or Phoca Download installed should now be treated as potentially compromised — several of these flaws were exploited in the wild before a patch shipped, and the observed payload gives the attacker a hidden Joomla super-admin.

Across 2026-W28 the specialist Joomla-security researcher mySites.guru disclosed the same bug class — CWE-434 arbitrary file upload leading to remote code execution — in four separate third-party extensions in quick succession, and CISA moved several onto the Known Exploited Vulnerabilities catalog within days. The mechanism is consistent: an upload handler that fails to enforce a server-side extension allow-list, does not block `.php`, and does not verify the declared content type, letting an attacker write an executable script into a web-reachable directory. In SP Page Builder the exploited path was `index.php?option=com_sppagebuilder&task=asset.uploadCustomIcon`, driven by an HTTP POST ([The Hacker News, 2026-07-08](https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html)); the researcher observed that "the payload plants a hidden Super Administrator account, usually with an @secure.local email" ([mySites.guru, 2026-07-08](https://mysites.guru/blog/sp-page-builder-zero-day-uploadcustomicon-rce/)). Balbooa Forms (CVE-2026-56291) was likewise found under live exploitation before any fix existed — "it was already being exploited in the wild when we found it, before any patch existed" ([mySites.guru, 2026-07-09](https://mysites.guru/blog/balbooa-forms-unauthenticated-file-upload-flaw/)) — and iCagenda (CVE-2026-48939) reached KEV as an unauthenticated file-upload-to-RCE ([mySites.guru, 2026-07-10](https://mysites.guru/blog/icagenda-zero-day-file-upload-rce/)). The week closed with two more from the same wave: RSFiles! (CVE-2026-57827, unauthenticated, CVSS 4.0 10.0, fixed 1.17.12) and Phoca Download (CVE-2026-57828, member-authenticated allow-list bypass, fixed 6.1.3), with no confirmed exploitation of that pair yet ([mySites.guru, 2026-07-11](https://mysites.guru/blog/rsfiles-unauthenticated-file-upload-rce/)).

**Why this is the week's operational reality for the constituency:** Joomla is disproportionately common on cantonal, communal and small-agency public-sector sites across Switzerland and the EU, and the ecosystem's risk lives in its third-party extensions, not the core. A wave of unauthenticated, pre-auth-exploited RCEs against exactly that surface, several with a public exploitation record and a self-installing super-admin payload, is a patch-and-hunt priority the normal monthly cadence does not cover.

**Defender takeaway:** treat the extension inventory — not the Joomla core version — as the exposure surface; update or remove every affected component now, and because at least three of these were exploited pre-patch, assume any lagging instance may already carry a web shell or rogue admin. **Triage:** a legitimate Joomla file-upload writes into a media/asset path an authenticated editor triggered; the wave's signal is a `.php` (or double-extension) file appearing in an extension's upload/download folder from an unauthenticated request, frequently followed by the creation of a Super Administrator account with a synthetic domain such as `@secure.local`.
