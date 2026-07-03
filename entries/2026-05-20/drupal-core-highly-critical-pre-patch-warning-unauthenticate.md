---
schema: 1
kind: threat
horizon: operational
title: "Drupal core \"highly critical\" pre-patch warning — unauthenticated, zero-complexity, patch window today 17:00–21:00 UTC"
headline: "Drupal core \"highly critical\" pre-patch warning — unauthenticated, zero-complexity, patch window today 17:00–21:00 UTC"
summary: "On 2026-05-18 the Drupal Security Team published PSA-2026-05-18 reserving an emergency out-of-band release for today, 2026-05-20, 17:00–21:00 UTC."
discovered_at: "2026-05-20T05:00:00Z"
event_date: 2026-05-18
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
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
  - url: "https://www.securityweek.com/drupal-to-patch-highly-critical-vulnerability-at-risk-of-quick-exploitation/"
    publisher: "SecurityWeek, 2026-05-19"
    role: corroborating
  - url: "https://www.theregister.com/security/2026/05/19/drupal-warns-admins-to-brace-for-highly-critical-core-patch/5242728"
    publisher: "The Register, 2026-05-19"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html"
    publisher: "The Hacker News, 2026-05-19"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1579"
    publisher: BSI WID-SEC-2026-1579
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
migrated_from: briefs/2026-05-20.md
---

On 2026-05-18 the Drupal Security Team published [PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18) reserving an emergency out-of-band release for today, 2026-05-20, 17:00–21:00 UTC. The pre-advisory scores the flaw 20/25 on Drupal's own published security scale — the second-highest tier — with **Access Complexity "None"** and **Authentication "None"**, meaning exploitation is unauthenticated and requires no special conditions; the chained score sits below the theoretical 25/25 only because the Drupal Security Team rates the affected configuration as "Uncommon". CVE assignment and class are embargoed until release. Affected branches: 10.5.x, 10.6.x, 11.2.x, 11.3.x receive official patches; Drupal also reserved manual emergency patch files for EOL branches 8.9, 9.5, 10.4 (→ 10.4.9) and 11.1 (→ 11.1.9) — an unusual step that itself signals severity. Drupal 7 is not affected. The Security Team explicitly notes ["exploits might be developed within hours or days"](https://www.securityweek.com/drupal-to-patch-highly-critical-vulnerability-at-risk-of-quick-exploitation/). NCSC.ch's Security Hub corroborates the urgency, reiterating that ["Successful exploitation could allow unauthenticated attackers to fully compromise affected Drupal installations"](https://security-hub.ncsc.admin.ch/#/posts/12584). BSI WID-SEC-2026-1579 carries the same advance warning ([BSI CERT-Bund](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1579)).

**Why it matters to us:** Drupal is the dominant CMS for Swiss federal / cantonal / municipal portals, European Commission and EU-agency sites, universities, and public-sector NGOs. No technical mitigation exists pre-patch. Schedule the patch window now and monitor the [Drupal Security Advisories feed](https://www.drupal.org/security) for the CVE and patch links the moment they publish at 17:00 UTC.
