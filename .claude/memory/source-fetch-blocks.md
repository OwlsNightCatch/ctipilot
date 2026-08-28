---
name: Source fetch blocks & primary-source substitutes
description: The fetch ladder, working recipes for blocked/JS hosts, jina key-pool rules, PDF extraction, and the probe/health traps
type: reference
---

# Source fetch blocks & recipes (condensed 2026-08-28)

A block is transport, not death — **never demote a source for a 403 / anti-bot challenge / exhausted reader credit**.

## Fetch ladder (v3.33)

RSS feed → `fetch_source.py extract <URL>` (human-header GET + trafilatura → markdown; internal fallbacks, jina strictly last) → structured recipe (`cisa csaf`, `cert-eu recent`, …) → `jina <URL>` only for `fetch_method: jina` hosts (heise article bodies, cisa.gov dynamic paths, ccn-cert geo-gate) or after every direct rung failed. Avoid `WebFetch` for article bodies (summariser drops detail); use it only for liveness checks and JS-SPA listings it renders that the bridge cannot (bacs.admin.ch). 18/20 representative CTI hosts extract with no reader (`work/2026-08-23T1311Z-audit/trafilatura-rollout.md`).

## Working recipes for blocked hosts

| Host / need | Recipe |
|---|---|
| CISA advisories/directives/news (Akamai 403s every direct UA) | `cisa page <url>` / `cisa feed <feed> [N]` / `cisa csaf-recent [N]` / `cisa csaf <icsa-id>`; KEV = `cisa-kev` (own subcommand, no reader) |
| GitHub Advisory DB (github.com/api.github.com egress-proxy-blocked; raw.githubusercontent.com IS reachable) | OSV.dev: `osv query <ecosystem> <pkg>` / `osv vuln <GHSA-or-CVE>`; cite `github.com/advisories/<GHSA>` |
| kernel.org (Anubis PoW challenge) | distro trackers: `ubuntu.com/security/CVE-…`, `security-tracker.debian.org/tracker/CVE-…` — count as `role: primary` |
| ncsc-uk | `feed https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml` (HTML listing is a consent shell; `report-rss-feed.xml` alone lags months) |
| ransomware.live | JSON API `https://api.ransomware.live/v2/countryvictims/<CC>` — discovery only, leak-site claims stay single-source |
| NCSC-CH / BACS (moved 2026-08-20 to bacs.admin.ch — Nuxt SPA; old ncsc.admin.ch redirects are explicitly NOT permanent) | `ncsc-ch-focus`/`-incidents` = `fetch_method: webfetch`; official PDFs on `cms.news.admin.ch`; CSH API = `ncsc-csh` (`/api/v1/posts/...`), cite `security-hub.ncsc.admin.ch/#/posts/<id>` |
| PDF-only advisories (joint advisories, authority reports) | `fetch_source.py pdf <URL>` — select on CONTENT TYPE, never as a failure rung; mirrors (media.defense.gov, ic3.gov) count as the same document |
| infoguard-labs | RSS `https://labs.infoguard.ch/rss.xml` |
| heise-sec | `feed https://www.heise.de/security/feed.xml N` → `jina <article>` (browser engine; needs a live key; free articles only) |
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

## Health/probe traps

- **The silent recipe gap:** a source can 200 forever and contribute nothing when its listing has no extractable dates (infoguard-labs hid a 22-CVE DACH disclosure for weeks). A `coverage_gaps` recipe-gap note is a repair order, not a status; when fixed, the top of the feed is a backlog — publish first coverage with a sourcing note.
- **A probe must assert the shape the recipe promises, never a proxy.** Byte count, non-empty output and HTTP 200 have each produced a false demotion here (`sec-edgar 8k`: a valid `count: 0` envelope ≈120 B read as dead). A valid empty result is a working source.
- `probe_url` field overrides the probe target when a publisher blocks its directory index but per-item fetches work (siemens-productcert-csaf).
- A national-CERT domain change also needs `NATIONAL_CERT_HOSTS` in `check_run.py`, or the single-source carve-out reports as unearned.
- A "reachable but stale" verdict needs the RAW body read in document order — ncsc-ch-incidents' accordion is newest-first and a truncated read concludes stale.
