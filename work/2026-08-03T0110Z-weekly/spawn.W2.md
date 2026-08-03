# W2 tasking — weekly strategic run 2026-08-03T0110Z-weekly

**Domain:** W2 — Strategic & policy horizon.
**Findings file:** `work/2026-08-03T0110Z-weekly/findings.W2.yaml`
**Ledger:** `work/2026-08-03T0110Z-weekly/url-liveness.tsv`
**Anchor:** today 2026-08-03T01:10:22Z · `window_days: 8` · ISO week under review **2026-W31** = Mon 2026-07-27 00:00 UTC → Sun 2026-08-02 24:00 UTC. A source must be published inside that window.
**Watchlist duty:** `none`.

## Scope (exclusively) — the standing policy / regulatory watch

Organization: Swiss federal SOC. Coverage focus: Switzerland and Europe, with Swiss and European critical infrastructure and government at the centre. Primary sector public-sector; additional sectors energy, water, transport, healthcare, finance, telco.

- **NCSC.ch announcements.** Use `python3 tools/fetch_source.py` (direct WebFetch 403s): `ncsc-csh recent N`, and the bridge for the Im-Fokus and Aktuelle-Vorfälle pages. The Swiss half of this domain is the highest-value part — spend real time here.
- **FINMA guidance** (Swiss financial-market regulator).
- **EU NIS2 / DORA / CRA developments** — transposition steps, implementation deadlines, delegated and implementing acts, Commission or member-state milestones. Two clocks already tracked: the Dutch NIS2 Cyberbeveiligingswet entering into force 2026-08-15, and the CRA Article 14 24-hour exploited-vulnerability reporting obligation beginning 2026-09-11. Report in-window movement on those and anything comparable.
- **OFCOM / BAKOM publications** (Swiss communications regulator).
- **Council of Europe cybercrime convention items.**
- **Sanctions and law-enforcement actions affecting publicly-known threat-actor infrastructure** — OFAC / EU designations, Europol / Eurojust operations, indictments, takedowns, domain seizures.
- **In-window regulator publications and enforcement actions** — ENISA, EDPB, national DPAs (CNIL, UK ICO, Swiss FDPIC), market-regulator actions with breach-disclosure implications, EU-level critical-infrastructure / health / energy sector guidance.

## Dedup context (read both before fetching)

- `work/2026-08-03T0110Z-weekly/prior_coverage.json` — 113 records, last 14 days. **There are zero policy-kind operational entries this week**, so nothing in your domain was covered operationally and your return is the sole input to the weekly's policy section. The 11 `horizon: strategic` records dated 2026-07-26 are the prior weekly (W30); its policy entries covered the ENISA EUMSS certification consultation (opened 2026-07-24, closes 2026-09-13), the ENISA Health Action Plan hospital-procurement guidance (2026-07-22), and BaFin's EUR 240,000 TeamViewer market-abuse ad-hoc-disclosure fine (announced 2026-07-20). Those are consolidated — return them only with a fresh in-window delta, marked `novelty: update-of:<entry-id>`.
- `entities/registry.yaml` — name entities by canonical registry key (policy items register as `policy:<slug>`); flag genuinely new ones as `new_entity` suggestions with sourced 1–3 sentence summaries.

## Rotation priority

`ccn-cert-es` (fetch_method jina) — missed on 2+ recent runs.

## Source slice — ESSENTIAL (attempt all)

| id | publisher | url / feed | fetch | rel |
|---|---|---|---|---|
| advisories-ncsc-nl | NCSC-NL Security Advisories | https://advisories.ncsc.nl/rss/advisories | rss | A |
| anssi-fr | ANSSI / CERT-FR | https://www.cert.ssi.gouv.fr/ | api | A |
| bsi-de | BSI CERT-Bund WID | https://wid.cert-bund.de/content/public/securityAdvisory/rss | rss | A |
| cert-at | CERT.at (Austria) | https://www.cert.at/en/ | webfetch | A |
| cert-eu | CERT-EU | https://cert.europa.eu/publications/security-advisories | api | A |
| cert-pl | CERT Polska / NASK | https://cert.pl/en/news/ | webfetch | A |
| cisa-advisories | CISA Advisories | https://www.cisa.gov/cybersecurity-advisories/all.xml | bridge — never WebFetch cisa.gov | A |
| cisa-directives | CISA Directives | — | bridge | A |
| enisa | ENISA news | https://www.enisa.europa.eu/news | webfetch | A |
| ncsc-ch-focus | NCSC.ch — Im Fokus | https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus.html | bridge (403s direct) | A |
| ncsc-ch-incidents | NCSC.ch — Aktuelle Vorfälle | https://www.ncsc.admin.ch/ncsc/de/home/aktuell/aktuelle-vorfaelle.html | bridge | A |
| ncsc-ch-security-hub | NCSC.ch CSH / GovCERT.ch | `python3 tools/fetch_source.py ncsc-csh recent 40` | api | A |
| ncsc-uk | NCSC UK | https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml | bridge | A |

## Source slice — ROTATION (standard/candidate, oldest-fetch first)

| id | publisher | url / feed | fetch | rel | last fetch |
|---|---|---|---|---|---|
| ccn-cert-es | CCN-CERT Spain | https://www.ccn-cert.cni.es/en/ | jina | A | 2026-07-29 · rotation priority |
| infoguard-labs | InfoGuard Labs (CH) | https://labs.infoguard.ch/ | webfetch | B | 2026-07-28 |
| jpcert | JPCERT/CC | https://www.jpcert.or.jp/english/index.html | webfetch | A | 2026-07-29 |
| synacktiv | Synacktiv Publications | https://www.synacktiv.com/publications.html | webfetch | B | 2026-07-29 |
| openssf-policy | OpenSSF Policy | https://openssf.org/policy/ | webfetch | C | 2026-07-29 |
| cisa-news | CISA News | https://www.cisa.gov/news.xml | bridge | A | 2026-07-30 |
| cnil-fr | CNIL France | https://www.cnil.fr/en/news | webfetch | A | 2026-07-30 |
| compass-security | Compass Security (CH) | https://blog.compass-security.com/feed/ | webfetch | B | 2026-07-30 |
| edpb | European Data Protection Board | https://www.edpb.europa.eu/news/news_en | bridge | A | 2026-07-30 |
| govcert-at | GovCERT Austria | https://www.govcert.gv.at/en/ | webfetch | A | 2026-07-30 |
| ico-uk | UK ICO | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/ | jina | A | 2026-07-30 |
| ncc-research | NCC Group Research | https://www.nccgroup.com/research-blog/ | bridge | B | 2026-07-30 |
| prodaft | PRODAFT Reports | https://www.prodaft.com/reports | jina | B | 2026-07-30 |
| truesec | Truesec | https://www.truesec.com/hub/blog/feed/ | rss | B | 2026-07-30 |

Beyond the slice, go directly to the primary authority pages for the domains above — finma.ch, bakom.admin.ch, EUR-Lex and the Commission's digital-strategy pages, coe.int, europol.europa.eu, OFAC press releases, EU sanctions announcements. The slice is a floor, not a boundary.

## The weekly bar

Higher than an intel run's. Return an item only if it answers at least one of:

- (a) **what is on fire if no one acted this week**;
- (b) a **cross-day pattern** no single day's coverage surfaces;
- (c) a **strategic / horizon shift** that changes defender obligations — a regulatory deadline, a new obligation, an enforcement precedent, an ecosystem change.

A policy item with no defender-obligation consequence for a Swiss or European public-sector / critical-infrastructure defender is not worth returning.

**Separately mark** any **items already in motion** carrying a concrete dated clock — a deadline, a consultation close, an entry-into-force, a scheduled publication. These feed the weekly's looking-ahead list, which carries items already in motion, never predictions.
