---
schema: 1
kind: vulnerability
horizon: operational
title: "UPDATE — GeoServer's actively exploited jsonArrayContains SQL injection now has a fix, a published root cause and a service-dependent exploitation path: WFS 1.0 reaches top-level SQL, WFS 2.0 does not"
headline: "GeoServer's exploited SQL injection is patched — vendor and researcher disagree on whether any config change helps"
summary: >
  GeoServer shipped 3.0.1, 2.28.5 and 2.27.6 on 2026-08-14 for the unauthenticated SQL injection in the
  GeoTools jsonArrayContains filter function that this pipeline covered on 2026-08-15 as exploited with no
  vendor fix; Switzerland's NCSC appended the fixed versions to its own advisory on 2026-08-17. Independent
  reversing published with the patch supplies the mechanism: the CQL filter value is interpolated into a
  PostgreSQL jsonb_path_exists() expression through String.format() with no escaping, reachable
  pre-authentication through the public OGC WMS and WFS endpoints of any PostGIS-backed layer with a text or
  JSON column. Exploitability depends on which service answers — WFS 1.0 puts the injection at the top level
  of the statement where a stacked second statement runs, WFS 2.0's count wrapper traps it — and where the
  database role holds superuser or pg_execute_server_program the stacked statement reaches OS command
  execution on the database host. The vendor advisory and the reversing analysis disagree on whether any
  configuration change helps —
  GeoTools states the mitigation published for the 2023 flaw this one regresses is not effective, while the
  reversing analysis states that disabling the encode functions option on the PostGIS data store stops the
  vulnerable translation — so the upgrade is the only remediation both agree on, and restricting the database
  role removes the command execution but not the injection.
discovered_at: "2026-08-18T04:35:00Z"
event_date: "2026-08-14"
run_id: 2026-08-18T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, sqli, pre-auth, actively-exploited, rce, patch-available, poc-public]
regions: [europe, switzerland, global]
sectors: [public-sector, energy, water, transport]
entities: []
techniques: [T1190, T1059.004]
affected_products: ["GeoServer", "GeoTools"]
cves: []
sources:
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html"
    publisher: "GeoServer project"
    date: "2026-08-14"
    role: primary
  - url: "https://github.com/geotools/geotools/security/advisories/GHSA-mqjf-5f49-2fjh"
    publisher: "GeoTools (GitHub Security Advisory)"
    date: "2026-08-15"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12844"
    publisher: "NCSC Switzerland (BACS) — Cyber Security Hub"
    date: "2026-08-17"
    role: corroborating
  - url: "https://hadrian.io/blog/here-be-dragons-geoserver-pre-auth-sql-injection-to-rce"
    publisher: "Hadrian"
    date: "2026-08-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This release addresses security vulnerabilities and is an urgent update for production systems."
    publisher: "GeoServer project"
  - quote: "requires a Text or JSON column; affects PostGIS 12 and up"
    publisher: "GeoServer project"
  - quote: "Actively Exploited, Proof of Concept Available"
    publisher: "NCSC Switzerland (BACS) — Cyber Security Hub"
  - quote: "The value comes directly from the CQL filter, which comes directly from the HTTP request. It is dropped into a SQL string literal with no escaping."
    publisher: "Hadrian"
  - quote: "WFS 1.0 provides a path where a stacked PostgreSQL statement executes at the top level of the query."
    publisher: "Hadrian"
  - quote: "Exploitation does not require preferQueryMode=simple on the JDBC connection. Default pgJDBC configuration is sufficient."
    publisher: "Hadrian"
  - quote: "A restricted PostgreSQL account reduces the impact. It does not remove the injection."
    publisher: "Hadrian"
verification: contradicted
sourcing_note: >
  Three independent assessors — the GeoServer/GeoTools project for the flaw and the fix, Hadrian for the
  reversed mechanism, and NCSC-CH for exploitation status relayed to Swiss operators. One discrepancy is
  carried rather than resolved: the GitHub advisory rates the flaw Critical at CVSS 3.1 9.8
  (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) while GeoServer's own release announcement labels the same advisory
  identifier High. A second discrepancy sits on a defender-facing point and is surfaced in the body rather
  than resolved: GeoTools states the CVE-2023-25158 mitigation — prepared statements plus disabling encode
  functions — is not effective, while Hadrian's remediation guidance states that disabling encode functions
  prevents the vulnerable translation. The entry reports both and recommends neither as a substitute for the
  upgrade, and carries `verification: contradicted` on that basis. Note what is and is not in dispute: the
  flaw, the fixed versions, the affected ranges and the active exploitation are corroborated across three
  independent assessors and uncontested, which is why the credibility rating stays at 1; what the two
  primaries contradict each other on is the one question a defender without a patch window would act on.
  No CVE has been assigned; GeoServer states it will update its announcement when one
  exists, so a CVE-keyed patch process still cannot see this flaw.
confidence: high
update_of: 2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited
references: []
deep_dive: true
deep_dive_category: web-app-rce
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Upgrade every GeoServer instance backed by a PostGIS data store to 3.0.1, 2.28.5 or 2.27.6 (GeoTools 35.1 / 34.5 / 33.6) — do not substitute a configuration change, because preferQueryMode=extended is not a mitigation and the vendor advisory and the reversing analysis contradict each other on whether disabling encode functions is one."
  - "For any instance that was internet-reachable and unpatched between 12 and 14 August, review the PostgreSQL role GeoServer connects as: if it held superuser or pg_execute_server_program, treat the database host as in scope for a compromise assessment rather than only upgrading."
migrated_from: null
---

**UPDATE (originally covered 2026-08-15):** the flaw this pipeline described as exploited with no vendor fix — where the only advice available was exposure reduction — has been patched, and the patch arrived with enough published detail to change how an operator scopes the exposure. GeoServer released 3.0.1, 2.28.5 and 2.27.6 on 2026-08-14, each bundling the corresponding GeoTools fix, and the project calls the release "an urgent update for production systems" ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html)). Switzerland's NCSC appended the fixed versions to its own advisory on 2026-08-17, while still recording the exploitation status as "Actively Exploited, Proof of Concept Available" ([NCSC-CH, 2026-08-17](https://security-hub.ncsc.admin.ch/#/posts/12844)). The advisory is tracked as GHSA-mqjf-5f49-2fjh; GeoTools scopes the affected package to `org.geotools:gt-jdbc-postgis` versions 35.0, ≥34.0 and ≥33.1, fixed in 35.1, 34.5 and 33.6 ([GeoTools, 2026-08-15](https://github.com/geotools/geotools/security/advisories/GHSA-mqjf-5f49-2fjh)). No CVE identifier exists yet, so this remains invisible to a purely CVE-driven patch process.

**The mechanism, now public.** GeoServer hands CQL-to-SQL translation to GeoTools, and the `jsonArrayContains` filter function builds its SQL by formatting the attacker-supplied value straight into a PostgreSQL `jsonb_path_exists()` jsonpath expression: "The value comes directly from the CQL filter, which comes directly from the HTTP request. It is dropped into a SQL string literal with no escaping" ([Hadrian, 2026-08-14](https://hadrian.io/blog/here-be-dragons-geoserver-pre-auth-sql-injection-to-rce)). Every other GeoTools filter function uses parameterised queries; this one does not, because PostgreSQL does not accept bind parameters inside a jsonpath expression, so the function was written with string formatting instead. The reachable surface is the `CQL_FILTER` parameter of the public OGC WMS and WFS endpoints, which accept unauthenticated input by design, against any PostGIS-backed layer that "requires a Text or JSON column; affects PostGIS 12 and up" ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html)). GeoTools describes the flaw as a regression of CVE-2023-25158 confined to this single function.

**Why the service version decides the outcome.** The escalation from arbitrary SQL to arbitrary commands turns on the *shape* of the query GeoServer generates, which differs per service. WFS 2.0 has to populate `numberMatched`, so it wraps the filter in a derived-table count query and a semicolon in the injected value never escapes the wrapper. WFS 1.0 carries no `numberMatched` in its response schema, so no wrapper is generated: "WFS 1.0 provides a path where a stacked PostgreSQL statement executes at the top level of the query" ([Hadrian, 2026-08-14](https://hadrian.io/blog/here-be-dragons-geoserver-pre-auth-sql-injection-to-rce)). Where the stacked statement lands and the PostgreSQL role holds superuser or `pg_execute_server_program`, `COPY ... TO PROGRAM` executes a command on the database host — Hadrian confirmed this against a lab deployment, with the command running as the `postgres` account. WMS `GetMap` is also exploitable but needs a geometry column and more parenthesis closure. The JDBC setting operators reach for first is not a control: "Exploitation does not require preferQueryMode=simple on the JDBC connection. Default pgJDBC configuration is sufficient" — the driver splits semicolon-separated SQL and executes each sub-statement even in extended mode.

**What a locked-down database role does and does not buy.** Removing superuser and `pg_execute_server_program` removes the command-execution path, and nothing else: "A restricted PostgreSQL account reduces the impact. It does not remove the injection" ([Hadrian, 2026-08-14](https://hadrian.io/blog/here-be-dragons-geoserver-pre-auth-sql-injection-to-rce)). Two extraction routes survive it — an error-based route that casts an expression to an integer so PostgreSQL leaks the result inside its type error, which works through both WFS and WMS with no special JDBC settings, and a time-based blind route through a subquery, which works even where prepared statements are enabled precisely because a subquery is not a stacked statement. Anything the GeoServer database user can read is therefore reachable, including credentials and connection strings held in other tables. On whether any configuration change helps, the vendor advisory and the reversing analysis disagree, and the disagreement is worth stating plainly rather than resolving. GeoTools says no mitigation is available, and specifically that the CVE-2023-25158 mitigation of enabling prepared statements and disabling encode functions is not effective ([GeoTools, 2026-08-15](https://github.com/geotools/geotools/security/advisories/GHSA-mqjf-5f49-2fjh)). Hadrian's remediation guidance says the opposite of one half of that pairing: "Disabling the encode functions option on the PostGIS datastore prevents jsonArrayContains from being translated into the vulnerable SQL form" ([Hadrian, 2026-08-14](https://hadrian.io/blog/here-be-dragons-geoserver-pre-auth-sql-injection-to-rce)). The two are not quite addressing the same thing — the advisory rates the 2023 pairing as a whole, the analysis isolates one setting — but an operator who cannot patch this week has one source telling them a switch closes the path and the vendor telling them it does not. Treat it as unproven and not a substitute for the upgrade: it is worth setting where the estate can tolerate it, and worth verifying against your own deployment rather than trusting either statement.

**Detection, telemetry class first.** In web and reverse-proxy access logs, the anchor is an unauthenticated WMS or WFS request whose `CQL_FILTER` parameter invokes `jsonArrayContains`, with the WFS 1.0 service version the one that matters most because it is the version that reaches top-level SQL. In application logs, a JDBC driver error reporting that multiple result sets were returned by the query is a by-product of a stacked statement having executed, not a parsing failure — it is a post-exploitation signal, not a probe. In database audit telemetry (PostgreSQL statement logging or pgAudit), the signals are a `COPY ... TO PROGRAM` invocation from the GeoServer service role, malformed jsonpath arguments to `jsonb_path_exists()`, repeated integer-cast type errors from the same client session, and `pg_sleep` inside a subquery. **Triage:** legitimate GIS clients do call `jsonArrayContains`, so the function name alone is not the signal — the discriminators are quote and semicolon characters inside the value argument, the same client session producing a run of type-conversion errors against a layer it otherwise reads cleanly, and a shift of that client's traffic onto the WFS 1.0 endpoint when the rest of the estate's tooling speaks WFS 2.0.

**Defender takeaway:** upgrading is the only remediation, and it is the one an estate can act on today where three days ago it could not. This matters disproportionately for the profiled constituency because GeoServer is the platform behind cadastral, planning, environmental and utility-network geoportals across European public administrations, and those endpoints are public by design — the exposure is not an accident of configuration that can be firewalled away. Two follow-ups are worth the hour: confirm which PostgreSQL role each GeoServer connects as before assuming the OS-command path was unavailable, and check whether the estate answers WFS 1.0 at all, since disabling an unused legacy service version removes the cleanest stacked-statement route while the upgrade rolls out.
