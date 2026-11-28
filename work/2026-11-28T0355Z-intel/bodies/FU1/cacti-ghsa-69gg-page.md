---
title: Pre-authentication SQL injection via rfilter RLIKE clause in graph_view.php
author: Netniv
url: https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc
hostname: github.com
description: "**Internal audit finding by the Cacti security team.** ## Affected Component `graph_view.php`. SQL `RLIKE` clause construction in graph filter. ## Root Cause The `rfilter` request variable ..."
sitename: GitHub
date: "2026-06-19"
categories: ['repository:29455529']
fingerprint: "7dab47c18e99f2c3"
language: en
image: https://opengraph.githubassets.com/0e085008ae1dd84e3b4576e289dd59c5ecb31f24a73901e90efbfde0b2de4ad2/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc
pagetype: object
filedate: "2026-11-28"
---
  
    **Internal audit finding by the Cacti security team.**

## Affected Component

`graph_view.php`. SQL `RLIKE` clause construction in graph filter.

## Root Cause

The `rfilter` request variable was concatenated into a `RLIKE` SQL clause without sanitization. The endpoint does not require authentication (graph viewing supports guest access via the configured guest user), so the SQLi was reachable pre-auth on installs with guest viewing enabled.

## Fix

Merged in [PR #7054](https://github.com/Cacti/cacti/pull/7054) (commit `891344a5c10b8687a3d2a5d26e6de20f13069e2a`, branch `1.2.x`, merged 2026-04-26).

- `graph_view.php:470` and `graph_view.php:753`: rfilter now passes through `db_qstr_rlike()`.
- Helper `db_qstr_rlike()` in `lib/database.php:2002-2011` caps length at 255, strips `|`, `{`, `}`, NUL, then calls `db_qstr()` for parameterized quoting.

## Verification

At `upstream/1.2.x` HEAD `11b58fd5`:

`$sql_where .= ' gtg.title_cache ' . db_qstr_rlike(get_request_var('rfilter'));`
Audit confirms all RLIKE sinks in `lib/`, root `*.php`, and `cli/` use `db_qstr_rlike()`. Stripping alternation and bounded-repeat metacharacters also limits ReDoS exposure on the RLIKE engine.

## Affected Versions

1.2.x prior to next 1.2.x release containing commit `891344a5`.

## Severity Rationale

Pre-auth reachable on guest-enabled installs. CVSS estimated 9.8 (Critical) given network attack vector, no auth required (guest), and confidentiality/integrity/availability impact via SQL.

## Note

This advisory has CVE-2026-39893 assigned. Full RLIKE audit completed 2026-04-17 confirming no other unhardened sinks.

## Fix

Addressed in: [#7039](https://github.com/Cacti/cacti/pull/7039)

**Internal audit finding by the Cacti security team.**

## Affected Component

`graph_view.php`. SQL `RLIKE` clause construction in graph filter.

## Root Cause

The `rfilter` request variable was concatenated into a `RLIKE` SQL clause without sanitization. The endpoint does not require authentication (graph viewing supports guest access via the configured guest user), so the SQLi was reachable pre-auth on installs with guest viewing enabled.

## Fix

Merged in PR #7054 (commit `891344a5c10b8687a3d2a5d26e6de20f13069e2a`, branch `1.2.x`, merged 2026-04-26).

`graph_view.php:470`and`graph_view.php:753`: rfilter now passes through`db_qstr_rlike()`.`db_qstr_rlike()`in`lib/database.php:2002-2011`caps length at 255, strips`|`,`{`,`}`, NUL, then calls`db_qstr()`for parameterized quoting.
## Verification

At `upstream/1.2.x` HEAD `11b58fd5`:

Audit confirms all RLIKE sinks in `lib/`, root `*.php`, and `cli/` use `db_qstr_rlike()`. Stripping alternation and bounded-repeat metacharacters also limits ReDoS exposure on the RLIKE engine.

## Affected Versions

1.2.x prior to next 1.2.x release containing commit `891344a5`.

## Severity Rationale

Pre-auth reachable on guest-enabled installs. CVSS estimated 9.8 (Critical) given network attack vector, no auth required (guest), and confidentiality/integrity/availability impact via SQL.

## Note

This advisory has CVE-2026-39893 assigned. Full RLIKE audit completed 2026-04-17 confirming no other unhardened sinks.

## Fix

Addressed in: #7039
