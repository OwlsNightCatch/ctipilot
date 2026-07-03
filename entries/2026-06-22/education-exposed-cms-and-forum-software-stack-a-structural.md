---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Education — exposed CMS and forum software stack a structural risk
headline: Education — exposed CMS and forum software stack a structural risk
summary: "Education entities sat under two pressures this week: the continuing ShinyHunters PeopleSoft campaign that W24 documented landing disproportionately on universities, and a cluster of critical web-application CVEs in software ubiquitous across European universities and student communities — JCE for Joomla …"
discovered_at: "2026-06-22T00:14:49Z"
event_date: null
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - data-breach
regions:
  - europe
  - global
sectors:
  - education
  - public-sector
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.joomlacontenteditor.net/news/jce-security-update-and-a-free-patch-for-older-sites"
    publisher: Widget Factory / JCE
    role: primary
  - url: "https://www.drupal.org/sa-core-2026-005"
    publisher: Drupal SA-CORE-2026-005
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W25.md
---

Education entities sat under two pressures this week: the continuing ShinyHunters PeopleSoft campaign that W24 documented landing disproportionately on universities, and a cluster of critical web-application CVEs in software ubiquitous across European universities and student communities — JCE for Joomla (CVE-2026-48907, exploited), phpBB (CVE-2026-48611), Drupal core (CVE-2026-55803, BSI critical) and LiteSpeed shared-hosting (CVE-2026-54420, exploited), all in § 3. The pattern is not a single incident but an attack-surface concentration: the open-source CMS/forum/hosting stack that the education sector runs widely all took critical, partly-exploited disclosures in one week.
