# CTI Brief v2 — implementation plan (historical)

> **Status: shipped.** Every item in this plan landed in prompt v2.23 (the
> v2 schema cut-over) and v2.24 (prompt-clarity tightening). The document
> is kept as a historical record of why the v2 cut-over happened and what
> was in scope. For current behaviour, read the live source of truth:
>
> - **Editorial:** [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md), [`prompts/weekly-summary.md`](../prompts/weekly-summary.md), [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md).
> - **Build:** [`site/build.py`](../site/build.py), [`site/taxonomy.yaml`](../site/taxonomy.yaml), [`site/test_build.py`](../site/test_build.py).
> - **Architecture:** [`docs/architecture.md`](architecture.md), [`docs/workflow.md`](workflow.md), [`site/README.md`](../site/README.md).

This document is the original engineering scaffolding for the v2 upgrade.
The prompts are now the editorial source of truth, and the build script
is the SSG source of truth — this file explains how the pieces were
designed to fit together.

## Goals (in order of priority)

1. Move the reader site from a JS-only SPA to a real static site. Every brief,
   every item, every CVE, every source, every topic, every tag, every region
   has its own static URL that renders without JavaScript.
2. Give the agent a structured per-item metadata footer that the build can
   parse, so the SSG can emit per-item pages and the granular RSS feed.
3. Restructure the daily brief: Immediate Actions (often absent), Active
   Threats / Incidents tagged by region + sector, consolidated Trending
   Vulnerabilities, Research & Investigative Reporting, and a derived-from-
   today Action Items block.
4. Three valid RSS feeds: daily (existing URL preserved), weekly (new),
   per-item granular (new). Close [#2](https://github.com/OwlsNightCatch/ctipilot/issues/2).
5. Tighten sub-agent prompts: trace primary sources, take time, persist.

## URL layout (normative — never rename, never repath)

```
/                                   home (latest brief preview + index)
/briefs/                            daily-brief list (paginated)
/briefs/YYYY-MM-DD/                 single daily brief
/briefs/weekly/                     weekly-brief list
/briefs/weekly/YYYY-Www/            single weekly brief
/items/<slug>/                      single content block
/cves/                              CVE index
/cves/<CVE-ID>/                     single CVE (aggregates briefs)
/topics/                            covered_items.json topic index
/topics/<key>/                      single topic
/sources/                           source index
/sources/<id>/                      single source
/tags/<tag>/                        items by theme tag
/regions/<region>/                  items by region
/ops/                               run_log.json dashboard
/about/                             about + docs + changelog
/feed.xml                           daily feed (existing URL)
/feed-weekly.xml                    weekly feed (new)
/feed-items.xml                     per-item feed (new)
/sitemap.xml, /robots.txt           crawl
```

Per-item slug: `YYYY-MM-DD-<short-kebab-from-heading>`. CVE pages: canonical
CVE id. Topic / source / tag / region pages: their existing keys.

The legacy SPA hash routes (`#/briefs/<name>`, etc.) get a tiny JS bootstrap
in the new `index.html` that converts them to the clean URL. One-time
indexed-redirect path; no ongoing dependency.

## Brief schema (both daily and weekly)

Frontmatter (added on cut-over):

```yaml
---
date: 2026-05-07
edition: 412
kind: daily              # daily | weekly
title: "CTI Daily Brief — 7 May 2026"
summary: "One-paragraph TL;DR for previews / RSS description."
prompt_version: "2.23"
deep_dive_slug: "ivanti-epmm-mass-exploitation"
verification_notes_present: true
---
```

Section order, daily (NORMATIVE):

1. TL;DR
2. Immediate Actions (often absent — render only when the bar is met)
3. Active Threats, Trending Actors, Notable Incidents & Disclosures
4. Trending Vulnerabilities (consolidated)
5. Research & Investigative Reporting
6. Updates to Prior Coverage
7. Deep Dive
8. Action Items
9. Verification Notes

Weekly keeps its eleven-section structure. Both adopt the same per-item
metadata footer.

### Metadata footer (NORMATIVE)

Every individual content block ends with exactly one italic line in this
format, parseable by a single regex:

```
— *Source: [Title](URL) [· Additional source: [Title](URL)] · Tags: tag1, tag2 · Region: region1[, region2] [· CVE: CVE-…] [· CVSS: …] [· Vector: …] [· Auth: …] [· Status: …]*
```

Field order is fixed. `Source`, `Tags`, `Region` always present. CVE-only
fields (`CVE`, `CVSS`, `Vector`, `Auth`, `Status`) appear only on CVE
entries.

The build splits each brief by the per-item heading + footer, generates a
`/items/<slug>/` page per block, populates the tag and region indexes, and
emits one RSS item per block in `feed-items.xml`.

### Controlled vocabularies

Single source of truth: [`site/taxonomy.yaml`](../site/taxonomy.yaml). The
build fails on any post-cut-over item using a value not in the taxonomy.
Pre-cut-over briefs are tolerated: missing footers do not fail the build,
they just don't populate per-item / tag / region pages.

## Build pipeline (`site/build.py`)

The new build:

- Parses every brief, splitting by H3 heading + metadata footer.
- Renders one HTML page per URL listed in the URL layout.
- Writes through `temp + os.replace` so a crashed build never publishes a
  half-written page.
- Maintains a content-addressed manifest at `_site/data/build_manifest.json`
  to make the build deterministic and reproducible. The manifest does not
  need to persist across CI runs (each CI run builds from scratch); its
  primary purpose is the self-check at the end of the build, plus making
  local re-runs byte-identical when inputs are unchanged.
- Computes "publish moment" from `git log --diff-filter=A --format=%aI` for
  each brief. Falls back to file mtime, never to midnight-of-date.
- Self-check at the end: every emitted HTML page contains the Umami
  snippet exactly once, every `<article>` has non-empty `data-tags` /
  `data-regions` / `data-section`, every taxonomy value is recognized,
  every RSS feed parses, no orphan files in `_site/`.

### Determinism

Two runs with no input changes produce a byte-identical site. To make this
work:

- `built_at` in `data/site.json` is the timestamp of the most recent input
  (most recent brief commit), not `now()`.
- `<lastBuildDate>` in each RSS feed is the timestamp of the most recent
  input feeding that feed, not `now()`.
- Asset cache-busting fingerprint is a hash of asset bytes (already
  deterministic).

### Multi-year operation

- No unbounded growth: `_site/.tmp/` is cleared at the start of each run.
- All individual content URLs (briefs, items, CVEs, sources, topics) are
  permanent. List pages may paginate but every URL stays reachable.
- Each RSS feed truncates to its declared N (30 daily / 30 weekly /
  50 items); HTML archives are unbounded.
- A failed build leaves the previous live site untouched (atomic writes,
  manifest committed only at end of successful build).

## Filtering and section toggles

The brief page (`/briefs/YYYY-MM-DD/`) emits semantic structure: each item is
an `<article data-tags="..." data-regions="..." data-section="...">`, each
section is a `<section data-section="...">`. A vendored
[`filter.min.js`](../site/assets/vendor/) (under 10 KB, integrity-checked
in HASHES) wires up tag/region chips and section toggles. The page is fully
readable without JS — filtering is progressive enhancement.

CSP stays strict (no `'unsafe-inline'`). Style toggles drive a class on
`<body>` (`.filter-active`, `.section-hidden-…`); CSS does the work.

## RSS

Three feeds, all valid against the W3C feed validator:

- `/feed.xml` — daily briefs (existing URL preserved). Keeps last 30 items.
- `/feed-weekly.xml` — weekly summaries. Keeps last 30 items. NEW.
- `/feed-items.xml` — granular per-item. Keeps last 50 items. NEW.

Defects fixed (closes [#2](https://github.com/OwlsNightCatch/ctipilot/issues/2)):

- Defect A: Markdown emphasis / links / inline code now render to HTML
  before the body is CDATA-wrapped. A unit test asserts no unrendered
  `**`, `_`, `[..](..)`, ``…`` survive into `<content:encoded>` payloads.
- Defect B: `<pubDate>` is the actual commit moment of the brief on `main`,
  not midnight-of-brief-date. Sourced from
  `git log --diff-filter=A --format=%aI -- briefs/YYYY-MM-DD.md`,
  falling back to file mtime, never to midnight.

`<lastBuildDate>` is the build moment of the feed file, RFC 822 UTC, derived
from the most recent input feeding the feed (deterministic).

No UTM parameters anywhere. Plain canonical URLs. RSS-click attribution is
limited to a `feed-click` Umami event fired on the `<a href="/feed*.xml">`
anchors before the user leaves the site — see `docs/analytics.md`.

## Sub-agent prompt edits

Both prompts gain a "trace to primary source" pass and a "take your time,
persist intermediate state, never block the brief" pass. Sub-agents drop
back to the most-primary source they can verify; aggregators are only
acceptable as fallbacks and must be flagged in Verification Notes.

## Hard invariants — preserved

The full list lives in `prompts/daily-cti-brief.md` § META. The v2 work
must not weaken any of:

1. AI-generated content notice on every brief.
2. Inline source links at point of claim. No bibliographies.
3. No IOCs.
4. No vanity metrics.
5. Always English.
6. Two-source verification with the documented national-CERT carve-out.
7. The two-stage publish chain (direct push → feature branch → auto-merge).
8. Strict CSP and vendored-library SHA-256 integrity check in the build.
9. Umami present on every emitted HTML page; privacy-by-design only.
10. Phase 5.5 self-check gate before commit.
11. No IOCs, no PII, no internal-only material in the repo.

If any v2 work would brush against any of these, the PR description spells
it out explicitly; nothing is silently relaxed.

## Acceptance criteria

The full checklist lives in the v2 implementation prompt. Re-running this
plan as a verification pass should hit every item in that list.

## Implementation order — all shipped

1. ✅ Land plan, taxonomy, footer parser, tests.
2. ✅ Update prompts (v2.23): new section order, metadata footer,
   region+sector tagging, Action Items, Immediate Actions, Trending
   Vulnerabilities inclusion gates, primary-source bias, patience clause.
3. ✅ Land the new SSG end-to-end in `site/build.py`: URL layout, base
   templates, manifest, atomic writes, three RSS feeds, self-check.
4. ✅ Migrate historical briefs through the new pipeline. Legacy
   hash-route bootstrap on `/`.
5. ✅ Sub-agent prompt edits: source tracing + patience.
6. ✅ Cut over.

Subsequent tightening:

7. ✅ Prompt-clarity rewrite (v2.24, 2026-05-07) — daily 1067 → 671 lines,
   weekly 363 → 448 lines, anti-crash guards consolidated at top of each
   prompt, sub-agent spawn templates merged.
