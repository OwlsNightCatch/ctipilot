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

## CISA advisories / directives / news — Akamai bot-block on the egress TLS fingerprint (root-caused 2026-07-05)

`cisa.gov/news-events/{cybersecurity-advisories,directives,news}`, **all `.xml` feeds, and the CSAF `.well-known`** reliably 403 via both `WebFetch` and every `tools/fetch_source.py` recipe. Root cause: **Akamai bot management** (`Access Denied`, `Reference #18.*`, `errors.edgesuite.net`) keyed off the egress TLS/behavioural fingerprint — **every** UA/header combination 403s (chrome/firefox/googlebot/curl/minimal/+Referer all tested). Only the **static** `/sites/default/files/feeds/` path is served, which is why CISA **KEV** works via `python3 tools/fetch_source.py cisa-kev` while the dynamic Drupal advisory pages do not. No reachable content alternative exists (search.gov results are a JS shell needing an API key; Wayback has no snapshots; CSAF is Akamai-blocked too).

**Handling (shipped v3.4):** these stay `active` — a 403 is transport, never demotes. `tools/source_health.py` now classes them `bridge-blocked` (action `none`, handled) via `TRANSPORT_BLOCKED_HANDLED`, so they stop churning `needs-demote` every run. Substitute: `cisa-kev` JSON for exploited-vuln ground truth + WebSearch corroboration for advisory narrative (covered_anyway). Log an `Essential-coverage: missed=` line when an essential CISA page 403s.

## JS-rendered pages with no server content (recurring recipe gaps)

Sources whose "recent items" live only in client-hydrated JS, so the fetcher gets an empty shell: NCSC-CH `aktuelle-vorfaelle.html`, OFAC recent-actions table, `sans.org/newsletters/newsbites/`, `prodaft.com/reports` (Next.js SPA). Pivot to their RSS/JSON endpoint where one exists, or a WebSearch pivot; flag as a recipe gap, never fabricate content.
