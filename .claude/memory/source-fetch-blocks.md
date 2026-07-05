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

## CISA advisories / directives / news — persistent 403 (ongoing)

`cisa.gov/news-events/{cybersecurity-advisories,directives,news}` reliably 403 both direct `WebFetch` and the `tools/fetch_source.py cisa page ...` bridge (logged in `sources/sources.json` notes; `fetch_gaps_in_window` promotes them each run). CISA **KEV** is fine via `python3 tools/fetch_source.py cisa-kev` (JSON endpoint). For advisory/directive *content*, WebSearch fallback for the underlying CVE/advisory is the standard workaround — covered_anyway, not an unrecovered failure. Log an `Essential-coverage: missed=` line when an essential CISA page 403s.

## JS-rendered pages with no server content (recurring recipe gaps)

Sources whose "recent items" live only in client-hydrated JS, so the fetcher gets an empty shell: NCSC-CH `aktuelle-vorfaelle.html`, OFAC recent-actions table, `sans.org/newsletters/newsbites/`, `prodaft.com/reports` (Next.js SPA). Pivot to their RSS/JSON endpoint where one exists, or a WebSearch pivot; flag as a recipe gap, never fabricate content.
