---
name: Source fetch blocks & primary-source substitutes
description: Hosts that block the routine fetcher and the citable primaries to substitute
type: reference
---

# Source fetch blocks & primary-source substitutes

Recurring transport blocks the routine hits, and what to cite instead. A block is transport, not death — never demote a source for a 403/anti-bot challenge.

## kernel.org git frontend — Anubis anti-bot challenge (discovered 2026-07-04)

`git.kernel.org` commit/advisory pages (both `.../commit/?id=<sha>` and `/stable/c/<sha>`) now serve an **Anubis proof-of-work JS challenge** ("Making sure you're not a bot!") to both direct `WebFetch` and `tools/fetch_source.py url`. The existing tooling cannot solve it, so kernel.org commit pages are **not a fetchable primary** for kernel-CVE citations right now.

**Substitute primary for kernel CVEs:** distro security trackers, which name the CVE, give CVSS + per-package fix status, and are not blocked:
- `https://ubuntu.com/security/CVE-YYYY-NNNNN` (Canonical — CVSS, per-package fixed/needed status)
- `https://security-tracker.debian.org/tracker/CVE-YYYY-NNNNN` (per-suite fixed versions)
- Red Hat RHSA / SUSE where the affected distro applies.

These count as `role: primary` (vendor advisory analogs) and are **not** blocked-URL patterns (unlike NVD/MITRE per-CVE pages, which `check_run.py` FAILs).

## GitHub Advisory Database — github.com is egress-proxy-blocked; use OSV.dev (root-caused 2026-07-05)

The `github-advisory` 403 is **NOT** a browser-UA / anti-bot refusal (the source-health audit mislabelled it). `github.com` **and** `api.github.com` are blocked by the **agent egress proxy itself**: each session is bound to its configured repository, so every other github.com / api.github.com path (including `github.com/advisories` and `api.github.com/advisories`) returns HTTP 403 with body `{"message":"This GitHub API path is not available: sessions are bound to their configured repositories..."}`. No UA / header / Sec-CH-UA set recovers it (re-confirmed across chrome/firefox/googlebot/curl/minimal), and it behaves identically in the routine container. `raw.githubusercontent.com` is a *different* host and IS reachable.

**Fix (shipped v3.4):** route through **OSV.dev** (`api.osv.dev`), the reachable full mirror of the GitHub Advisory Database — every GHSA id present, aliased to its CVE:
- `python3 tools/fetch_source.py osv query <ecosystem> <package> [version]` — advisories affecting a watchlist package (ecosystem ∈ npm|PyPI|Go|Maven|crates.io|NuGet|RubyGems|Packagist…). Maps cleanly onto the watchlist-driven model.
- `python3 tools/fetch_source.py osv vuln <GHSA-or-CVE>` — drill one advisory.
Cite the human URL `https://github.com/advisories/<GHSA-ID>`; the bridge supplies the data. `fetch_method` is now `bridge`.

## CISA advisories / directives / news — REACHABLE via reader proxy + CSAF mirror (recovered 2026-07-05)

**Root cause of the block:** `cisa.gov/news-events/*`, **all `.xml` feeds, and the CSAF `.well-known`** 403 a DIRECT fetch (`WebFetch` and `fetch_source.py url`/`cisa page` direct attempt) via **Akamai bot management** (`Access Denied`, `Reference #18.*`, `errors.edgesuite.net`) keyed off the egress TLS/behavioural fingerprint — **every** UA/header combination 403s (chrome/firefox/googlebot/curl/minimal/+Referer). Only the **static** `/sites/default/files/feeds/` path (KEV JSON) is served directly.

**Fix (shipped v3.5) — the content IS now fetchable with full detail:**
- `python3 tools/fetch_source.py cisa page <cisa-url>` — advisory / directive / news **body**. Tries a direct fetch first (auto-recovers if Akamai ever lifts), else falls back to the **r.jina.ai** reader proxy, which fetches from its own egress (bypasses the Akamai fingerprint) and returns clean markdown with the full body.
- `python3 tools/fetch_source.py cisa feed <feed-url> [N]` — a cisa.gov RSS/Atom feed (`news.xml`, `cybersecurity-advisories/all.xml`, `ics-advisories.xml`, `ics-medical-advisories.xml`) → `{title, link}` items via the reader proxy. Drill each `link` with `cisa page`.
- `python3 tools/fetch_source.py cisa csaf-recent [N]` — recent **ICS/OT** advisories from the **cisagov/CSAF** GitHub mirror `changes.csv` (newest-first, ISO-dated). Reachable via `raw.githubusercontent.com` (NOT proxy-blocked), NO third party.
- `python3 tools/fetch_source.py cisa csaf <icsa-YY-DDD-NN | icsma-YY-DDD-NN>` — the full **CSAF v2 JSON** for one ICS advisory (CVEs, CVSS, product tree, remediations) — richest machine-readable form CISA publishes.
- `cisa-kev` JSON stays the exploited-vuln ground truth. **Deprecated/dead:** `/cisa/blog.xml` (`/blog.xml`) returns Access-Denied even through the reader — do not use it.

**Health/lifecycle:** these probe `bridge-ok` now. They remain in `source_health.py TRANSPORT_BLOCKED_HANDLED` only as a transient-outage safety net (a reader-proxy blip is treated as a transport block → never demote). Reader proxy is anonymous by default; set `JINA_API_KEY` env if a run ever hits its rate limit.

## jina reader (r.jina.ai) is a GENERAL-PURPOSE transport, not just the CISA path (v3.8, 2026-07-06; ladder order superseded by v3.25 below)

The reader was wired only into `cisa page`/`cisa feed`. It is now a **first-class, universal fetch transport** — `python3 tools/fetch_source.py jina <URL> [html]`. It fetches from **its own egress** (bypasses anti-bot / WAF / geo blocks that 403 ours) **and executes page JavaScript** (hydrates JS-only SPAs that return an empty shell to a plain GET), returning the full body as clean markdown. `fetch_source.py url` auto-falls-back to the reader on a challenge/403 (`--direct` opts out); `feed` falls back too (`method: jina` in its result). `fetch_method: jina` marks sources whose only working transport is the reader. Reader-unreachable hosts (401 even to r.jina.ai): `coe.int`, `downloads.seppmail.com` — those stay `blocked`. **Ladder order: see the v3.25 note below — the reader is now the LAST rung, not rung 3.**

## group-ib.com + ccn-cert.cni.es — RECOVERED via the reader (2026-07-06, supersedes the block below)

Both were long marked `fetch_method: blocked` (Cloudflare Managed-Challenge / geo-gate). The 2026-07-06 jina-fallback audit found **both are reachable**: `www.group-ib.com/blog/` now returns 200 to a **direct** browser-UA fetch (~800 KB real blog, current posts) — moved to `fetch_method: bridge` (with reader as backup); `www.ccn-cert.cni.es` still 403s direct but the **reader** returns the full body (~39 KB) — moved to `fetch_method: jina`. Both **removed from `TRANSPORT_BLOCKED_UNREACHABLE`** (now emptied) and probe `bridge-ok`/`jina-ok`. Recipes + backups are in their `sources.json` notes. The reader is a transport, not a citation — cite the publisher URL.

## `TRANSPORT_BLOCKED_UNREACHABLE` — reserved for hosts the reader ALSO fails (mechanism kept, set emptied 2026-07-06)

The frozenset in `tools/source_health.py` still exists to mark a `fetch_method: blocked` host as **handled** (`action: none`, coverage gap) instead of churning as `needs-demote` every sweep — but it is now **empty**, because the reader recovered the two hosts that were in it. Add a source-id **only** after confirming direct AND the **jina reader** AND the bridge all fail (transport block, not death — a genuine 404/5xx/dead host still surfaces). Per rule A1 a 403 transport block **never demotes**; document any addition in the source's `sources.json` notes too.

## JS-rendered pages with no server content (recurring recipe gaps)

Sources whose "recent items" live only in client-hydrated JS, so the fetcher gets an empty shell: NCSC-CH `aktuelle-vorfaelle.html`, OFAC recent-actions table, `sans.org/newsletters/newsbites/`, `prodaft.com/reports` (Next.js SPA). Pivot to their RSS/JSON endpoint where one exists, or a WebSearch pivot; flag as a recipe gap, never fabricate content.

## jina reader v2 — authenticated, browser engine; heise.de per-article bodies RECOVERED (2026-07-12)

The reader connector (`tools/fetch_source.py` `_jina_fetch`) now sends, on every keyed markdown page fetch: `Authorization: Bearer <key>` (env-only — keys are NEVER stored in the repo; the routine env carries them), `X-Engine: browser` (highest-fidelity rendering tier, authenticated rungs only), `X-With-Links-Summary: true` (outbound URLs survive the markdown conversion), `X-Cache-Tolerance: 300` and `X-Retain-Images: none`. The `fmt="html"` feed path keeps the default engine so the `<hN><a href>` feed parse stays stable.

- **heise-sec RECOVERED** (was demoted as fetch-waste since v2.64): the browser-engine reader returns the FULL per-article body that the TollBit/heise+ gate denies every direct transport. Recipe: `feed https://www.heise.de/security/feed.xml N` for discovery → `jina <article-url>` for body. Free articles only; a heise+ article stays paywalled → pivot.
- **Key lifecycle:** `python3 tools/fetch_source.py jina-usage` reports EVERY configured key's remaining token balance plus the pool total (Jina dashboard API) and WARNs on stderr below 1 M tokens combined / when every key is dead → operator generates a new key at https://jina.ai/api-dashboard/ and adds it to the env. The quality-audit run should include a `jina-usage` check so a dying pool is caught before it silently degrades the reader to the anonymous tier.
- No key in env → reader still works anonymously (shared rate limit, no browser engine) — same behaviour as before v2.

## jina reader v3 — multi-key pool + anonymous free-tier fallback (2026-07-13)

Shipped after the 2026-07-12→13 runs lost every jina fetch to a spent key (HTTP 402 was a terminal, non-retryable error). `_jina_fetch` now walks a **credential ladder** per fetch:

- **Key pool:** `JINA_API_KEYS` (new) takes one or more keys separated by commas/semicolons/whitespace — listed order = spend order; the original `JINA_API_KEY` still works and is appended after the list (it may itself carry a separated list). Duplicates are collapsed.
- **Rotation:** a key answering **402** (balance exhausted) or **401** (invalid/revoked) is marked dead for the rest of the process (`_JINA_DEAD_KEYS`, so a multi-fetch invocation doesn't re-burn it per page) and the next key is tried immediately — no backoff wasted on a dead key. A stderr line names the rotated key by suffix.
- **Anonymous backstop:** when no live key remains, the request runs on the reader's **anonymous free tier** (no `Authorization`, no `X-Engine: browser` — requesting the browser engine keyless is itself a 402). An exhausted pool degrades fidelity, never availability; heise-style TollBit-gated bodies are what the anonymous tier may miss.
- **Health semantics:** `source_health.py`'s `reader-quota` class now only fires when the whole pool is dead AND the anonymous rung also failed for that fetch; its action text says to add a fresh key to `JINA_API_KEYS`. The final connector error still carries the `HTTP 402` / `balance exhausted` markers the classifier keys on.

## jina reader v3.1 — token/request savers: local response cache + 1 h reader cache tolerance (2026-07-13)

Two cost controls in `_jina_fetch`, both on by default:

- **Local disk cache** — reader bodies are cached under `JINA_CACHE_DIR` (default `/tmp/ctipilot-jina-cache`, OUTSIDE the repo, dies with the container), keyed by SHA-256 of `(return-format, url)`, TTL `JINA_CACHE_TTL` (default 3600 s; `0` disables). A hit costs **zero API requests and zero tokens**. This kills the run's built-in double spend: the Phase 5.7 verifier re-fetches every entry source Phase 1 research already fetched — same container, same hour → all cache hits. Atomic writes (tmp+rename, parallel-sub-agent safe); best-effort (any cache I/O error → live fetch); challenge/blocked bodies raise BEFORE the cache put, so they are never stored; measured 1.2 s live → 0.14 s hit.
- **`X-Cache-Tolerance` 300 → 3600** — the reader may serve its own snapshot up to an hour old instead of re-crawling/re-rendering. Aligned with the local TTL: an intel run processes a multi-hour window, so hour-stale content cannot cost it a finding. If a fetch ever NEEDS to be bypass-fresh (rare — e.g. re-probing a page that just changed), run it with `JINA_CACHE_TTL=0` (local bypass; the header still allows the reader's snapshot).

## ncsc-uk — WORKING recipe found (2026-07-11 audit); "reachable but unreadable" is a failure class

The NCSC-UK HTML listing (`/section/keep-up-to-date/reports-advisories`) had been a "recipe gap" in nearly every July run — consent-banner shell to WebFetch AND jina — while `sources.json` showed it green (an HTTP 200 bumped `last_successful_fetch`): an **essential source dark for weeks with healthy-looking bookkeeping**. Recipe: the combined feed `https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml` is FRESH (verified 2026-07-11; items days old) — use `python3 tools/fetch_source.py feed <that URL> 20` for discovery, drill item links for citation. (`report-rss-feed.xml` alone lags months — that's what earned RSS its bad reputation in the old note.) General lesson: a 200 that yields no parseable items is a coverage gap, not a success — when a source repeats as a "recipe gap" across runs, spend the five minutes probing its API/feed endpoints instead of re-logging the gap.

## ransomware.live — use the JSON API, not the HTML (2026-07-11 audit)

The HTML site returns chrome with no parseable victim table. Working recipe for country sweeps: `https://api.ransomware.live/v2/countryvictims/CH` (any ISO country code) via plain fetch. Leak-site claims stay single-source PD-6 material — the API is discovery, never confirmation.

## jina reader v4 — LAST-RESORT rung; anonymous tier NOT guaranteed; fresh key verified (v3.25, 2026-07-18)

The 2026-07-18T0409Z run exhausted the key pool mid-window (HTTP 402) **and the anonymous free tier answered HTTP 401** — falsifying the v3 assumption "exhausted pool = degraded fidelity, never availability". Operator-directed changes (prompt v3.25):

- **Ladder reordered — the reader is rung 4 of 4:** RSS (`feed`) → direct `WebFetch` → **direct bridge** (`url <URL>` raw body / structured publisher recipe) → **jina reader LAST**. Every reader fetch spends metered API-key credit; routine fetches must never burn it when a free direct transport serves the same content. Force `jina <URL>` directly ONLY for `fetch_method: jina` sources (heise article bodies via browser engine, cisa.gov dynamic paths, ccn-cert geo-gate — hosts proven to need it) or after every direct rung failed. `url`'s auto-reader-fallback is unchanged, so nothing requires switching commands mid-read.
- **Full-detail reads:** prefer `url <URL>` (whole raw body, nothing summarised away) over the reader; heavy raw HTML goes to `work/<run-id>/` and gets extracted on disk (grep/python), keeping bulk out of main context — the 2026-07-18 deep-read proved this path.
- **Anonymous rung:** `_jina_fetch` now treats 401/402 on the anonymous credential as non-retryable (no backoff burned); all docs say an exhausted pool can be a reader OUTAGE. Treat `jina-usage` "pool dead" as an incident, not a footnote.
- **Institutionalized watch:** quality-audit Phase 3 item 4 runs `python3 tools/fetch_source.py jina-usage` weekly; low/dead pool → operator recommendation (new key at jina.ai/api-dashboard → `JINA_API_KEYS` env; keys NEVER in the repo).
- **2026-07-18 session verification:** a fresh operator-supplied key (suffix `…MrZOsc`, 10 M tokens, trial to 2036) was tested from this repo: `jina-usage` reports it live; rotation off the dead env key (`…xI3xEh`, 402) worked; heise article body (VMware Avi, id 11368661) and cisa.gov/news-events/directives both returned full content through it. Operator still needs to update the routine container env vars.

## ncsc-ch-incidents (aktuelle-vorfaelle.html) — read the FULL accordion before judging freshness (2026-07-18)

The 07-18 audit's G2 sweep flagged the page "reachable-but-stale: Oct-2025 consumer-phishing only". **False alarm, operator-corrected same day:** the documented bridge fetch (`python3 tools/fetch_source.py url <page URL>` — this admin.ch page does NOT 403 the bridge) returns the full accordion, 10 dated entries newest-first, latest **01.07.2026 13:22** (SwissNovaChat/SwissNovaCare fake-subscription warning). The trap: 4 of 10 entries cluster in Oct 2025, so a truncated or summarized read that misses the top of the accordion concludes "stale". Rule: judge this page's freshness only from the raw bridge body, scanning every `DD.MM.YYYY` in document order (newest is first). Cadence is genuinely slow (quarterly-ish) and the surface is consumer-fraud by design — operational/sector incidents live on the Cyber Security Hub (`ncsc-csh`) / Im Fokus; neither fact is staleness.
