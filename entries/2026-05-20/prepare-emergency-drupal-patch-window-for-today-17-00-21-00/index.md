---
schema: 1
kind: threat
title: "Prepare emergency Drupal patch window for today 17:00–21:00 UTC"
headline: "Prepare emergency Drupal patch window for today 17:00–21:00 UTC"
summary: "Drupal core \"highly critical\" (20/25) pre-patch warning — patch lands today 17:00–21:00 UTC; exploits expected within hours. Pre-auth full-site compromise across all supported branches (10.5.x, 10.6.x, 11.2.x, 11.3.x) plus EOL 8.9 / 9.5 / 10.4 / 11.1 patch files. Drupal Security Team explicitly warns \"exploits might be developed within hours or days\" (Drupal PSA-2026-05-18 · NCSC.ch Security Hub 12584, 2026-05-19). High Swiss/EU public-sector exposure — federal, cantonal, municipal portals, universities. See Immediate Action callout below and § 6."
discovered_at: "2026-05-20T05:00:15Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: critical
immediate_action:
  title: "Prepare emergency Drupal patch window for today 17:00–21:00 UTC"
  action: "Drupal's Security Team has pre-announced a \"highly critical\" (20/25 on Drupal's own scale, the second-highest tier) core vulnerability with unauthenticated exploitation and zero complexity; the patch window opens today at 17:00 UTC and the Team has explicitly warned that exploits may surface within hours of release (Drupal PSA-2026-05-18 · NCSC.ch Security Hub 12584, 2026-05-19). All current branches (10.5.x, 10.6.x, 11.2.x, 11.3.x) plus emergency manual patches for EOL 8.9 / 9.5 / 10.4 / 11.1 are in scope."
tags:
  - vulnerabilities
  - pre-auth
  - no-patch
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - education
entities: []
cves: []
sources:
  - url: "https://www.drupal.org/psa-2026-05-18"
    publisher: Drupal PSA-2026-05-18
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12584"
    publisher: "NCSC.ch Security Hub 12584, 2026-05-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: The Drupal Security Team urges you to reserve time for core updates at that time because exploits might be developed within hours or days.
    publisher: Drupal Security Team
  - quote: Successful exploitation could allow unauthenticated attackers to fully compromise affected Drupal installations.
    publisher: NCSC.ch Security Hub
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
migrated_from: briefs/2026-05-20.md
---

Drupal's Security Team has pre-announced a "highly critical" (20/25 on Drupal's own scale, the second-highest tier) core vulnerability with **unauthenticated** exploitation and **zero complexity**; the patch window opens today at 17:00 UTC and the Team has explicitly warned that exploits may surface within hours of release ([Drupal PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18) · [NCSC.ch Security Hub 12584, 2026-05-19](https://security-hub.ncsc.admin.ch/#/posts/12584)). All current branches (10.5.x, 10.6.x, 11.2.x, 11.3.x) plus emergency manual patches for EOL 8.9 / 9.5 / 10.4 / 11.1 are in scope. Public-sector Drupal-based portals (Swiss federal, cantonal, municipal; EU agency; university) — schedule an emergency change record now, freeze unrelated changes during the window, monitor [Drupal SA feed](https://www.drupal.org/security) immediately at 17:00 UTC for the CVE and patch links, and apply within hours rather than within your normal SLA. No technical mitigation exists pre-patch.
