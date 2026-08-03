# W1 tasking — weekly strategic run 2026-08-03T0110Z-weekly

**Domain:** W1 — Threat-actor, campaign, research & report horizon.
**Findings file:** `work/2026-08-03T0110Z-weekly/findings.W1.yaml`
**Ledger:** `work/2026-08-03T0110Z-weekly/url-liveness.tsv`
**Anchor:** today 2026-08-03T01:10:22Z · `window_days: 8` · ISO week under review **2026-W31** = Mon 2026-07-27 00:00 UTC → Sun 2026-08-02 24:00 UTC. A source must be published inside that window (standard allowance for a fresh in-window delta on an older story).

## Scope (exclusively)

1. **Long-running campaign status re-checks.** For each, name its `entities/registry.yaml` key. Re-check in-window status of, at minimum: the npm / AI-developer-toolchain supply-chain wave (`malware:sandworm-mode`), the Joomla third-party-extension disclosure stream (`trend:joomla-extension-file-upload-rce-wave`), the ShinyHunters identity-provider / SSO campaign (`actor:shinyhunters`), the Cl0p PTC Windchill / FlexPLM extortion wave (`campaign:clop-windchill-flexplm-extortion-2026`), Russian state webmail espionage (`actor:laundry-bear`, `actor:ta458-roundpress`) — plus anything else in the registry with fresh in-window movement.
2. **Threat-actor developments.** New named clusters, attribution shifts, tooling / affiliate / ecosystem moves, law-enforcement or infrastructure takedowns affecting tracked actors.
3. **Research-finding synthesis candidates.** In-window vendor and independent lab research that changes what a Tier 2/3 responder can detect, hunt or harden.
4. **Newly published annual / periodic / quarterly reports.** Flag as `ANNUAL REPORT — {name}`. Cisco Talos IR Trends Q2 2026 was already covered on 2026-07-29 (`report:talos-ir-trends-q2-2026`) — do not return it. Only in-window, not-yet-covered reports.

**Watchlist duty:** `products`. This deployment configures no product and no supplier watchlist, so the sweep is a no-op — report `products checked=0, hits=0; suppliers checked=0, hits=0` and spend no time on it.

## Dedup context (read both before fetching)

- `work/2026-08-03T0110Z-weekly/prior_coverage.json` — 113 records, last 14 days, operational + strategic.
  **Weekly dedup polarity:** an item already covered *operationally* this week is NOT a duplicate for you — the weekly re-frames operational coverage. Mark it `novelty: reframe-of:<entry-id>`. An item already consolidated in a *prior weekly strategic entry* (the 11 records with `horizon: strategic`, all dated 2026-07-26) returns only with a fresh in-window delta, marked `novelty: update-of:<entry-id>`.
- `entities/registry.yaml` — name entities by canonical registry key; flag genuinely new ones as `new_entity` suggestions with sourced 1–3 sentence summaries.

## Rotation priority

`apple-security`, `ccn-cert-es` — missed on 2+ recent runs; try these first among the rotation set.

## Source slice — ESSENTIAL (attempt all)

| id | publisher | url / feed | fetch | rel |
|---|---|---|---|---|
| advisories-ncsc-nl | NCSC-NL Security Advisories | https://advisories.ncsc.nl/rss/advisories | rss | A |
| anssi-fr | ANSSI / CERT-FR | https://www.cert.ssi.gouv.fr/ | api | A |
| bsi-de | BSI CERT-Bund WID | https://wid.cert-bund.de/content/public/securityAdvisory/rss | rss | A |
| cert-eu | CERT-EU | https://cert.europa.eu/publications/security-advisories | api | A |
| cert-pl | CERT Polska / NASK | https://cert.pl/en/news/ | webfetch | A |
| cisa-advisories | CISA Advisories | https://www.cisa.gov/cybersecurity-advisories/all.xml | bridge — never WebFetch cisa.gov | A |
| cisa-directives | CISA Directives | — | bridge | A |
| cisa-kev | CISA KEV Catalog | `python3 tools/fetch_source.py cisa-kev` | api | A |
| enisa-euvd | ENISA EUVD | https://euvd.enisa.europa.eu/ | api | A |
| ncsc-ch-security-hub | NCSC.ch CSH / GovCERT.ch | `python3 tools/fetch_source.py ncsc-csh recent 40` | api | A |
| ncsc-uk | NCSC UK | https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml | bridge | A |

## Source slice — ROTATION (standard/candidate, oldest-fetch first)

| id | publisher | url / feed | fetch | rel | last fetch |
|---|---|---|---|---|---|
| apple-security | Apple Security Releases | https://support.apple.com/en-us/HT201222 | webfetch | A | rotation priority |
| zdi | Zero Day Initiative | https://www.zerodayinitiative.com/blog/ | webfetch | B | 2026-07-14 |
| aikido-security | Aikido Security | https://www.aikido.dev/blog | webfetch | B | 2026-07-14 |
| onapsis | Onapsis Research Labs | https://onapsis.com/blog | webfetch | B | 2026-07-14 |
| morphisec | Morphisec Labs | https://www.morphisec.com/blog/ | webfetch | C | 2026-07-19 |
| push-security | Push Security | https://pushsecurity.com/blog | webfetch | B | 2026-07-19 |
| resecurity | Resecurity | https://www.resecurity.com/blog | webfetch | C | 2026-07-19 |
| sans-ics | SANS ICS | https://www.sans.org/blog/?focus-area=industrial-control-systems-ics | webfetch | B | 2026-07-19 |
| snyk-research | Snyk Security Research | https://snyk.io/blog/ | rss | B | 2026-07-19 |
| socprime | SOC Prime | https://socprime.com/blog/feed/ | rss | C | 2026-07-19 |
| team-cymru | Team Cymru S2 | https://www.team-cymru.com/blog | webfetch | B | 2026-07-19 |
| sonatype | Sonatype | https://www.sonatype.com/blog | rss | B | 2026-07-19 |
| kela-cyber | KELA | https://www.kelacyber.com/blog/ | webfetch | B | 2026-07-21 |
| searchlight-cyber | Searchlight Cyber | https://slcyber.io/research-center/ | webfetch | B | 2026-07-21 |
| exodus-intelligence | Exodus Intelligence | https://blog.exodusintel.com | rss | B | 2026-07-21 |
| sysdig | Sysdig TRT | https://www.sysdig.com/blog/feed | webfetch | B | 2026-07-21 |
| depthfirst | depthfirst.com | https://depthfirst.com | webfetch | C | 2026-07-26 |

Also sweep the majors' research indexes for in-window posts even where not listed: Microsoft Threat Intelligence, GTIG / Mandiant, Cisco Talos, Unit 42, Check Point Research, ESET, Kaspersky, SentinelOne, Proofpoint, Trend Micro, CrowdStrike, Group-IB, Recorded Future. The weekly's research horizon depends on them.

## The weekly bar

Higher than an intel run's. Return an item only if it answers at least one of:

- (a) **what is on fire if no one acted this week** — the operational reality for a reader who ignored the week;
- (b) a **cross-day pattern** no single day's coverage surfaces;
- (c) a **strategic / horizon shift** that changes defender obligations — new actor capability, ecosystem change, a clock that starts.

A re-list of the week's operational items with no new lens is not useful. The constituency is Swiss and European critical infrastructure and government.
