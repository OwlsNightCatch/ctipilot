---
name: Source fetch blocks & primary-source substitutes
description: The fetch ladder, working recipes for blocked/JS hosts, jina key-pool rules, PDF extraction, and the probe/health traps
type: reference
---

# Source fetch blocks & recipes (condensed 2026-08-28)

A block is transport, not death — **never demote a source for a 403 / anti-bot challenge / exhausted reader credit**.

**Healthy = working, not answering (2026-09-29, v4.16).** `tools/source_health.py` reads every source through its own recipe and adds a content verdict: `relevant` / `shell` / `unreadable` / `irrelevant` / `stale` (newest dated item > `max_staleness_days`, default 60). The first content sweep flagged 27 of 190 sources the old reachability-only probe called green (challenge and JS shells, a PSIRT landing page with no bulletin text, blogs that moved hosts and left a frozen listing behind). Traps: trafilatura's `date:` header is the fetch date on listing pages, never item freshness; listing pages extract to chrome only, so judge them on raw HTML + extract; a structured query API (SEC EDGAR, OSV) with a small or empty result set is working, not a shell; general news feeds (`content_scope: general-news`) need only one security term. Fixes live in the record: `url`/`rss_url`/`fetch_method`, `health_cmd` (fetch_source.py argv), `max_staleness_days`, `content_scope`.

## Fetch ladder (v3.33, WebFetch rung v4.18)

RSS feed → `fetch_source.py extract <URL>` (human-header GET + trafilatura → markdown; internal fallbacks, jina strictly last) → structured recipe (`cisa csaf`, `cert-eu recent`, …) → `WebFetch` for hosts the container is walled out of (cisa.gov pages without a structured recipe) → `jina <URL>` only for `fetch_method: jina` hosts (none today) or after every other rung failed. Avoid `WebFetch` for article bodies `extract` reads (summariser drops detail); use it for walled hosts, liveness checks and link discovery. bacs.admin.ch articles read with `extract`. 18/20 representative CTI hosts extract with no reader (`work/2026-08-23T1311Z-audit/trafilatura-rollout.md`).

## Working recipes for blocked hosts

| Host / need | Recipe |
|---|---|
| CISA advisories/directives/news (Akamai 403s every direct UA) | ICS: `cisa csaf-recent [N]` / `cisa csaf <icsa-id>`; KEV = `cisa-kev` (own subcommand, no reader); news, alerts, AA-series, directives: `WebFetch` with the outbound-links template (v4.18; `cisa page` / `cisa feed` need reader credit) |
| GitHub Advisory DB (github.com/api.github.com egress-proxy-blocked; raw.githubusercontent.com IS reachable) | OSV.dev: `osv query <ecosystem> <pkg>` / `osv vuln <GHSA-or-CVE>`; cite `github.com/advisories/<GHSA>` |
| kernel.org (Anubis PoW challenge) | distro trackers: `ubuntu.com/security/CVE-…`, `security-tracker.debian.org/tracker/CVE-…` — count as `role: primary` |
| ncsc-uk | `feed https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml` (HTML listing is a consent shell; `report-rss-feed.xml` alone lags months) |
| ransomware.live | JSON API `https://api.ransomware.live/v2/countryvictims/<CC>` — discovery only, leak-site claims stay single-source |
| NCSC-CH / BACS (moved 2026-08-20 to bacs.admin.ch — Nuxt SPA; old ncsc.admin.ch redirects are explicitly NOT permanent) | **`extract <url>` reads both pages in full via trafilatura-direct — verified 2026-09-27 on `/de/aktuelle-vorfaelle` and `/de/im-fokus`, dated item lists and all.** `ncsc-ch-focus`/`-incidents` = `fetch_method: bridge`. They had drifted to `jina` and sat unreadable for two windows against an empty key pool while this direct path worked; if you find them on `jina` again, that is the bug. Official PDFs on `cms.news.admin.ch`; CSH API = `ncsc-csh` (`/api/v1/posts/...`), cite `security-hub.ncsc.admin.ch/#/posts/<id>` |
| PDF-only advisories (joint advisories, authority reports) | `fetch_source.py pdf <URL>` — select on CONTENT TYPE, never as a failure rung; mirrors (media.defense.gov, ic3.gov) count as the same document |
| infoguard-labs | RSS `https://labs.infoguard.ch/rss.xml` |
| heise-sec | `feed https://www.heise.de/security/feed.xml N` → `extract <article>` (trafilatura-direct, no reader; verified 2026-09-29 on article 11469864 — the older jina-only recipe is superseded; free articles only) |
| Reader-unreachable even via jina | coe.int, downloads.seppmail.com — stay `blocked` |

`TRANSPORT_BLOCKED_UNREACHABLE` in `source_health.py` marks a blocked host as handled; add an id ONLY after direct AND jina AND bridge all fail.

## jina reader pool

- Keys: `JINA_API_KEYS` list (+ legacy `JINA_API_KEY`), spend order, auto-rotate on 402/401; dead keys cached cross-process 6 h (`dead-keys.json`). **Rotation warnings followed by content mean the ladder worked** — never conclude "pool exhausted" from a sub-agent's stderr; check `jina-usage` (whole-pool report). Anonymous free tier is BEST-EFFORT (observed 401) — an exhausted pool can be a reader outage, and a dead pool is a NORMAL condition the pipeline works through (operator refills sparsely; keys never in the repo).
- Cost savers: local 1 h disk cache (`JINA_CACHE_DIR`/`JINA_CACHE_TTL`; repeat fetches = 0 requests) + `X-Cache-Tolerance: 3600`. Quality audit runs `jina-usage` every fire.
- Pool-dead blast radius: `fetch_method: jina` sources + recipes that silently fall back to the reader go dark; KEV survives. Never demote; probe direct alternatives and record them; needs the operator (no in-pipeline fix restores credit).

## PDF extraction honesty (contractual)

- "no text objects found" = **not extractable** (image-only/scanned), NEVER "the document says nothing".
- A CMap-approximated decode is labelled an approximation; selection between decodes is by volume of recovered prose, not a ratio.
- Real PDFs find real bugs — test extractor changes against a genuine advisory, not only the synthetic suite.
- **Decode per font, never file-wide (fixed 2026-09-29).** Microsoft Word PDFs write spaces in a simple font and every other glyph in Type0 fonts whose codes are glyph ids. The old merged-CMap decode turned "North Korean" into "1RUWK.RUHDQ", dropped every digit, and still won on prose volume (the IC3 WaterPlum advisory, CSA 260918, read as mojibake on all 9 pages). `_pdf_render_by_font` walks page resources and decodes each string with its own font's ToUnicode map, falling back to the merged path only when the page tree cannot be walked. If a PDF reads as letter-shifted gibberish or has no digits, suspect a regression here first.

## Health/probe traps

- **The silent recipe gap:** a source can 200 forever and contribute nothing when its listing has no extractable dates (infoguard-labs hid a 22-CVE DACH disclosure for weeks). A `coverage_gaps` recipe-gap note is a repair order, not a status; when fixed, the top of the feed is a backlog — publish first coverage with a sourcing note.
- **A probe must assert the shape the recipe promises, never a proxy.** Byte count, non-empty output and HTTP 200 have each produced a false demotion here (`sec-edgar 8k`: a valid `count: 0` envelope ≈120 B read as dead). A valid empty result is a working source.
- `probe_url` field overrides the probe target when a publisher blocks its directory index but per-item fetches work (siemens-productcert-csaf).
- A national-CERT domain change also needs `NATIONAL_CERT_HOSTS` in `check_run.py`, or the single-source carve-out reports as unearned.
- A "reachable but stale" verdict needs the RAW body read in document order — ncsc-ch-incidents' accordion is newest-first and a truncated read concludes stale.

## NCSC-CH moved to bacs.admin.ch (seen 2026-09-30)

`www.ncsc.admin.ch/ncsc/...` article pages now answer 404; the same content lives under `www.bacs.admin.ch/de/<slug>` (the clickfix advisory is `https://www.bacs.admin.ch/de/clickfix-de`, and trafilatura `extract` reads it). The four June entries that cited the old paths (G7 events warning, week 22/23/25 reviews) were repointed by 2026-09-30T0634Z-audit; the English pages are `/en/26-cyberresilienz-g7-en` and `/en/26w<NN>-en`. `security-hub.ncsc.admin.ch` is a separate host and still reads through the `ncsc-csh` bridge recipe.

## WebFetch is the reader for walled hosts (v4.18, operator directive 2026-09-30)

The container's egress is walled out of cisa.gov (Akamai, every UA) and ssd-disclosure.com (SiteGround captcha), and the jina pool is usually dead. The agent-side `WebFetch` runs outside the container and reads cisa.gov reliably, and ssd-disclosure.com only once in a while. Tested 2026-09-30: cisa.gov `/news-events/news` and `/news-events/cybersecurity-advisories` returned dated lists with item URLs, and `/directives` the six directive links (dates only on each directive's page). SSD is not solved: WebFetch read one advisory page live at about 06:47Z, then SR1's 26 WebFetch calls over 18 URLs returned 24 empty bodies and 2 replays of that cached read. The reader pool was refilled at about 07:40Z, and the funded reader gets the same captcha (8 of 8 tries, and again at 12:3xZ), so no transport reads SSD: it is `fetch_method: blocked` and in `TRANSPORT_BLOCKED_UNREACHABLE`, the health check reports its wall as a handled gap, and discovery is `WebSearch site:ssd-disclosure.com` (leads only). Do not spend reader calls on it. WebFetch's 15-minute cache can make a dead host look alive: re-test after the cache lapses before trusting a single read. CLAUDE.md, both agent definitions and cti-run.md now sanction this; `cisa-kev` and `cisa csaf-recent` stay on the bridge. `source_health.py` gives these records `webfetch-only` (handled, action `none`) while the reader pool is empty, reads them through the reader's fallback while it has credit, and the audit spot-checks them with WebFetch. A funded pool also makes `extract` fall back to the reader on tiny pages (swarmcha-se read as irrelevant that way, so it probes with `url --direct`). Quotes from WebFetch-only pages are not machine-checkable: ask the prompt for the exact sentence and quote only what comes back verbatim.
