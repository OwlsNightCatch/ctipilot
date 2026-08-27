---
schema: 1
kind: threat
horizon: operational
title: >
  Drupal core "highly critical" pre-patch warning — unauthenticated, zero-complexity, patch window
  today 17:00–21:00 UTC
headline: >
  Drupal core "highly critical" pre-patch warning — unauthenticated, zero-complexity, patch window
  today 17:00–21:00 UTC
summary: >
  On 2026-05-18 the Drupal Security Team published PSA-2026-05-18 reserving an emergency
  out-of-band release for today, 2026-05-20, 17:00–21:00 UTC.
discovered_at: "2026-05-20T05:00:00Z"
updated_at: "2026-05-23T05:00:10Z"
event_date: 2026-05-18
run_id: 2026-05-20-a0f7b07f
priority: critical
immediate_action:
  title: Patch Drupal CVE-2026-9082 today on PostgreSQL-backed deployments
  action: >
    Active in-the-wild exploitation was confirmed by Drupal and corroborated by NCSC.ch on
    2026-05-22; Imperva reports observing 15,000+ exploitation attempts against ~6,000 sites across
    65 countries (Imperva, 2026-05-21). The flaw is an anonymous pre-authentication SQL injection in
    the Entity Query API's PostgreSQL path — no login, no role, no user interaction required. Swiss
    federal and cantonal portals, EU institution Drupal instances, and academic SWITCH-hosted sites
    running PostgreSQL backends are direct targets.
tags:
  - vulnerabilities
  - pre-auth
  - no-patch
  - patch-available
  - eu-nexus
  - actively-exploited
  - rce
  - cisa-kev
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - education
  - media
entities: []
techniques: []
affected_products: []
cves:
  - id: CVE-2026-9082
    cvss: "6.5"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
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
  - url: "https://www.drupal.org/sa-core-2026-004"
    publisher: Drupal Security Team SA-CORE-2026-004
    role: primary
  - url: "https://www.csoonline.com/article/4175329/drupal-admins-rushing-to-patch-maximum-severity-sql-injection-vulnerability.html"
    publisher: CSO Online
    role: corroborating
  - url: "https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/"
    publisher: Imperva — Customers Protected Against CVE-2026-9082
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/drupal-critical-sql-injection-flaw-now-targeted-in-attacks/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/"
    publisher: Searchlight Cyber technical analysis
    role: corroborating
closed_sources: []
evidence:
  - quote: "Drupal confirmed: exploit attempts are now being detected in the wild"
    publisher: BleepingComputer
  - quote: "Current exploitation status: Actively exploited"
    publisher: NCSC.ch Security Hub
  - quote: "Imperva sees more than 15,000 exploit attempts against around 6,000 Drupal websites in 65 countries"
    publisher: Imperva
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "**Patch Drupal CVE-2026-9082 today on every PostgreSQL-backed Drupal deployment** — pre-auth SQL injection, active exploitation, 15,000+ attempts measured by Imperva, NCSC.ch status \"Actively exploited\". Target versions: 10.4.10 / 10.5.10 / 10.6.9 / 11.1.10 / 11.2.12 / 11.3.10 per [Drupal SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004). MySQL/MariaDB/SQLite backends are unaffected — if patching slips, swap the backend as a temporary control."
updates:
  - at: "2026-05-21T05:00:07Z"
    run_id: 2026-05-21-77cdc4cd
    type: update
    summary: >
      Drupal patches "highly critical" pre-auth SQL injection (CVE-2026-9082) on PostgreSQL-backed
      installs of Drupal 8.9–11.3; the Security Team warned that "exploits might be developed within
      hours or days" of advisory release. EU/CH government portals and university CMSes are the
      primary exposed surface (Drupal Security Team, 2026-05-20; NCSC-CH, 2026-05-19).
    fields:
      - cves
      - priority
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-05-21/drupal-sa-core-2026-004-cve-2026-9082-ships-highly-critical
  - at: "2026-05-23T05:00:10Z"
    run_id: 2026-05-23-852c21c8
    type: update
    summary: >
      Drupal CVE-2026-9082 now actively exploited; CISA KEV-listed 2026-05-22. Drupal updated
      SA-CORE-2026-004 to confirm in-the-wild exploit attempts on PostgreSQL-backed sites; Imperva
      measured 15,000+ attempts against ~6,000 sites across 65 countries; NCSC.ch Security Hub flipped
      post 12584 to "Actively exploited" the same day (Drupal Security Team, 2026-05-22 · Imperva,
      2026-05-21 · NCSC-CH, 2026-05-22).
    fields:
      - actions
      - cves
      - evidence
      - immediate_action
      - priority
      - sources
      - tags
      - body
    merged_from: 2026-05-23/drupal-cve-2026-9082-cisa-kev-addition-active-exploitation-c
migrated_from: briefs/2026-05-20.md
---

On 2026-05-18 the Drupal Security Team published [PSA-2026-05-18](https://www.drupal.org/psa-2026-05-18) reserving an emergency out-of-band release for today, 2026-05-20, 17:00–21:00 UTC. The pre-advisory scores the flaw 20/25 on Drupal's own published security scale — the second-highest tier — with **Access Complexity "None"** and **Authentication "None"**, meaning exploitation is unauthenticated and requires no special conditions; the chained score sits below the theoretical 25/25 only because the Drupal Security Team rates the affected configuration as "Uncommon". CVE assignment and class are embargoed until release. Affected branches: 10.5.x, 10.6.x, 11.2.x, 11.3.x receive official patches; Drupal also reserved manual emergency patch files for EOL branches 8.9, 9.5, 10.4 (→ 10.4.9) and 11.1 (→ 11.1.9) — an unusual step that itself signals severity. Drupal 7 is not affected. The Security Team explicitly notes ["exploits might be developed within hours or days"](https://www.securityweek.com/drupal-to-patch-highly-critical-vulnerability-at-risk-of-quick-exploitation/). NCSC.ch's Security Hub corroborates the urgency, reiterating that ["Successful exploitation could allow unauthenticated attackers to fully compromise affected Drupal installations"](https://security-hub.ncsc.admin.ch/#/posts/12584). BSI WID-SEC-2026-1579 carries the same advance warning ([BSI CERT-Bund](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1579)).

**Why it matters to us:** Drupal is the dominant CMS for Swiss federal / cantonal / municipal portals, European Commission and EU-agency sites, universities, and public-sector NGOs. No technical mitigation exists pre-patch. Schedule the patch window now and monitor the [Drupal Security Advisories feed](https://www.drupal.org/security) for the CVE and patch links the moment they publish at 17:00 UTC.

## Update — 2026-05-21T05:00:07Z

Yesterday's brief carried Drupal's PSA pre-warning that a "highly critical" core advisory was scheduled for 2026-05-20; today the [SA-CORE-2026-004 advisory](https://www.drupal.org/sa-core-2026-004) landed with **CVE-2026-9082** assigned — an anonymous SQL-injection in Drupal core's database abstraction API (CWE-89) rated **20/25 on Drupal's risk scale (Highly Critical)** that affects only PostgreSQL-backed installations. Specially-crafted HTTP requests slip past sanitisation in the core DB-API layer and inject arbitrary SQL with no authentication; successful exploitation leads to information disclosure, privilege escalation and — in some database configurations — RCE. The Drupal Security Team explicitly stated that "exploits might be developed within hours or days" of advisory release ([Drupal PSA, 2026-05-18](https://www.drupal.org/psa-2026-05-18)).

Affected versions: 8.9.0 through 10.4.10, 10.5.x < 10.5.10, 10.6.x < 10.6.9, 11.0.0 through 11.1.10, 11.2.x < 11.2.12, 11.3.x < 11.3.10. Patched: 10.4.10 / 10.5.10 / 10.6.9 / 11.1.10 / 11.2.12 / 11.3.10 (released 2026-05-20). MySQL / MariaDB / SQLite installations are not affected by this CVE. Drupal 7 is unaffected; sites on EOL Drupal 8/9 majors must apply manual patch files. [Drupal Steward WAF](https://www.drupal.org/steward) subscribers receive vendor-provided rules at advisory release per the service description; non-subscriber sites must apply the core update. NCSC-CH carried the advisory in its Security Hub ([NCSC-CH, 2026-05-19](https://security-hub.ncsc.admin.ch/#/posts/12584); [SecurityWeek, 2026-05-19](https://www.securityweek.com/drupal-to-patch-highly-critical-vulnerability-at-risk-of-quick-exploitation/); [CSO Online, 2026-05-20](https://www.csoonline.com/article/4175329/drupal-admins-rushing-to-patch-maximum-severity-sql-injection-vulnerability.html)).

**Defender takeaway:** detection — PostgreSQL slow-query logs and `pg_stat_activity` for abnormal SQL statements from the Drupal application user; web-server access logs for unusual URL-encoded SQL meta-characters in POST/GET parameters proxied through the Drupal DB-API layer; WAF rules targeting PostgreSQL-specific injection patterns (`UNION`, `CAST`, `pg_sleep`). Hardening — patch immediately on PostgreSQL backends; if patch deployment is blocked by change-control, temporarily front the site with the Drupal Steward WAF or apply a temporary WAF rule covering known SQL-injection vectors at the DB-API layer.

## Update — 2026-05-23T05:00:10Z

On 2026-05-22 Drupal updated [SA-CORE-2026-004](https://www.drupal.org/sa-core-2026-004) to confirm that exploit attempts targeting CVE-2026-9082 — the anonymous pre-authentication SQL injection in the Entity Query API's PostgreSQL path — are now being detected in the wild. NCSC.ch updated [Security Hub post 12584](https://security-hub.ncsc.admin.ch/#/posts/12584) to "Actively exploited" status the same day at 13:52Z, also recording the addition of CVE-2026-9082 to the CISA Known Exploited Vulnerabilities catalog on 2026-05-22 (the NCSC-CH post is the brief's source of record on the KEV add; the CISA news-events alert URL constructed earlier in the day returned a 404 at composition time).

Imperva reports observing **15,000+ exploitation attempts against approximately 6,000 Drupal sites across 65 countries** within days of disclosure ([Imperva, 2026-05-21](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-9082-in-drupal-core/)). The technical mechanism (now public via the [Searchlight Cyber write-up](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/)): on the case-insensitive `IN` operator path through `core/lib/Drupal/Core/Entity/Query/Sql/Condition::compile()` / `ConditionAggregate::compile()`, a JSON-encoded array value survives into the SQL placeholder name without sanitisation, allowing injection when the backend is PostgreSQL. Fixed versions: 10.4.10, 10.5.10, 10.6.9, 11.1.10, 11.2.12 and 11.3.10; best-effort patches for EOL Drupal 8.9 and 9 are also available. MySQL/MariaDB/SQLite-backed Drupal sites remain unaffected, which is the temporary control to fall back on if the patch window slips past today.

Defender vantage update from yesterday's brief: the operational frame is no longer "patch when convenient" but **patch today** — the § 0 Immediate Action carries the operational framing; this UPDATE captures the source-of-record links and the technical mechanism for anyone composing internal advisories or hunt queries. CH/EU specifics: NCSC.ch Security Hub is the authoritative jurisdictional source for Swiss federal and cantonal operators; Drupal-on-PostgreSQL is widespread across FITKO and SWITCH-hosted university sites, French `gouvernement.fr` instances and EU institution portals. Detection: WAF telemetry for nested JSON arrays in user-supplied fields hitting Drupal endpoints; PostgreSQL `log_min_duration_statement` to surface anomalous query shapes; web-server logs for unexpected POST payloads to anonymous routes.
