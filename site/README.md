# site/ — public reader for the brief feed

A static, dependency-free GitHub Pages site that renders the daily and weekly
Markdown briefs server-side, exposes a unified searchable index of every
**entity** referenced across briefs (CVEs, actors, campaigns, incidents,
tools, advisories, annual reports, research, techniques) plus the source
list, and cross-links every entity to the briefs that reference it.
Read-only: the agentic workflow (`prompts/`, `state/`, `sources/`) is the
source of truth; this folder only **publishes** what the agent produces.

The deployed site lives at <https://ctipilot.ch/>.

## Architecture (v2 — static-site generator)

Every URL is a real HTML page rendered at build time. JavaScript is used for
progressive enhancement only (topbar search autocomplete, GitHub-stars
badge, list-page filter chips, brief-page tag/region/section toggles, theme
cycle, copy-link button). With JS disabled the site is fully readable —
search and filters are inert but every page still serves its content.

```
site/
├── build.py               # Stdlib-only Python SSG. Single entrypoint.
├── branding_config.py     # Loader for config/branding.yaml — site identity,
│                          # theme overrides, logos, chart palettes, feeds,
│                          # analytics. Fail-loud on unknown keys; the shipped
│                          # config builds a byte-identical site. See
│                          # docs/customization.md.
├── branding/              # Downstream-owned brand assets (logos, favicon,
│                          # fonts, custom.css). Upstream ships only a README.
├── taxonomy.yaml          # Controlled vocabulary (themes, regions, sectors,
│                          # CVE fields, section keys). The build refuses any
│                          # post-cut-over item using a value not in here.
├── test_build.py          # Stdlib-only smoke tests (Markdown render, footer
│                          # parser, Defect A regression, taxonomy validation,
│                          # branding-profile contract).
├── README.md              # this file
└── assets/
    ├── css/styles.css     # Dark-first stylesheet, light/dark/system, print
    ├── js/
    │   ├── theme.js       # Reads/writes data-theme; cycles system → light → dark
    │   ├── search.js      # Token-prefix scoring across data/search.json
    │   └── app.js         # Topbar wiring, list-page filters, copy-link, mobile nav
    └── vendor/
        ├── HASHES         # SHA-256 + SHA-384 known-good hashes; build aborts on mismatch
        ├── marked.min.js  # Markdown → HTML, kept for any future client-side use (MIT)
        ├── purify.min.js  # HTML sanitiser (Apache 2.0 / MPL 2.0)
        └── filter.min.js  # First-party in-page filter UI for brief pages (under 4 KB)
```

The previous SPA scripts (`store.js`, `router.js`, `render.js`) are gone —
their job (loading JSON, hash routing, client-side templates) is now done at
build time. Removing them was a net `-2300` line change.

## What the build produces

`python3 site/build.py` writes a self-contained bundle to `site/_site/`:

```
_site/
├── .nojekyll
├── index.html                            # Home — TL;DR preview of latest brief
├── 404.html
├── feed.xml                              # Daily RSS (URL preserved from v1)
├── feed-weekly.xml                       # NEW: weekly RSS
├── feed-items.xml                        # NEW: per-item RSS (last 50 items with footers)
├── sitemap.xml
├── robots.txt
├── assets/...                            # copied from site/assets, atomic-write
├── briefs/                               # daily index
│   ├── index.html                        # all briefs grouped by month
│   ├── YYYY-MM-DD.md                     # raw Markdown (kept for the "Raw .md" link)
│   ├── YYYY-MM-DD/index.html             # rendered daily brief
│   └── weekly/
│       ├── index.html                    # weekly summaries list
│       ├── YYYY-Www.md                   # raw Markdown
│       └── YYYY-Www/index.html           # rendered weekly summary
├── items/<slug>/index.html               # one page per metadata-footer item
├── entities/
│   ├── index.html                        # unified entity index — KPIs + type-distribution
│   │                                     #   donut + recent-coverage sparkline + filter chips
│   └── <key>/index.html                  # canonical entity detail (CVE / actor / campaign /
│                                         #   incident / tool / advisory / annual-report /
│                                         #   research / technique). Story timeline + KPI
│                                         #   tile grid (sparkline embedded) + section-
│                                         #   distribution bars + source-host donut + related-
│                                         #   entities co-occurrence list + grouped citations
│                                         #   (paragraph + item-footer origins)
├── cves/
│   ├── index.html                        # type-filtered view of /entities/ (type=cve)
│   └── <CVE-ID>/index.html               # HTML meta-refresh stub → /entities/CVE-<ID>/
├── sources/
│   ├── index.html                        # source list (filterable by category + status)
│   └── <id>/index.html                   # source detail
├── topics/
│   ├── index.html                        # type-filtered view of /entities/ (type≠cve)
│   └── <key>/index.html                  # HTML meta-refresh stub → /entities/<key>/
├── tags/<tag>/index.html                 # items by theme tag
├── regions/<region>/index.html           # items by region
├── ops/index.html                        # operations dashboard
├── about/                                # landing page + Documentation + Prompts sections
│   ├── index.html                        # landing (README + section nav)
│   ├── docs/                             # operator-facing system documentation
│   │   ├── index.html                    # documentation index
│   │   ├── architecture/index.html
│   │   ├── operating/index.html          # operator runbook (setup, ops dashboard, troubleshooting)
│   │   ├── analytics/index.html          # what we measure / what we don't
│   │   └── improvements/index.html
│   └── prompts/                          # everything the routine loads at runtime
│       ├── index.html                    # prompts index + recent CHANGELOG headings
│       ├── daily-cti-brief/index.html
│       ├── weekly-summary/index.html
│       ├── verification/index.html       # verification policy (the prompt enforces it)
│       ├── brief-template/index.html     # canonical Markdown skeleton
│       ├── check-brief-fixes/index.html  # how to fix common check_brief.py FAILs
│       └── changelog/index.html          # full prompts/CHANGELOG.md
└── data/
    ├── build_manifest.json               # content-hashed manifest (self-check substrate)
    ├── search.json                       # flat unified search index
    └── site.json                         # build metadata + counts
```

URL layout is **permanent** — never renamed, never repathed. The legacy SPA
hash routes (`#/briefs/<name>`, etc.) get a one-time inline JS bootstrap on
the home page that converts indexed hash URLs to the clean URL.

## Cross-references

The cross-references between entities and briefs are computed once at build
time, by walking the briefs and joining against state files. Every entity
flows through one annotator (`annotate_entities`) and one renderer
(`render_entity_page`); the `type` field distinguishes a CVE from an actor,
campaign, incident, tool, advisory, annual report, research item, or
technique.

| Entity   | Joined to brief by                                                  |
|----------|---------------------------------------------------------------------|
| Entity   | `appearances[].brief_path` from `covered_items.json` (structured), or for CVE-only entries the brief-name list synthesised from `cves_seen.json` |
| Source   | longest-prefix URL match between `sources.json#url` and brief links |
| Tag      | `Tags:` field in the per-item metadata footer (taxonomy-validated)  |
| Region   | `Region:` field in the per-item metadata footer                     |
| Item     | per-H3 split + metadata-footer parse                                |

Per-entity inline links come from two sources, deduped and origin-tagged
on the page: every paragraph (unit) that mentions the entity contributes
its inline `[label](url)` links (matched by CVE id, title-phrase, or
anchor token; the legacy >3-CVE filter is dropped for the broader set),
and every matched item's footer Source / Additional source URLs are
registered with `origin: "item-footer"` so the curated set is visually
distinguished from inline chatter.

Multi-appearance items get a "story timeline" badge (`×N appearances`)
everywhere they show up. Topics tagged with a verification flag in any
brief carry it through to the listings, where the chip filter lets a
SOC reviewer pull every `[SINGLE-SOURCE]` item across briefs.

The deploy URL the feeds embed comes from the `SITE_URL` env var
(`SITE_URL=https://ctipilot.ch/` by
convention; the default falls back to the same value).

## RSS feeds

Three valid RSS 2.0 feeds:

| URL                | Contents                                                  | Truncation |
|--------------------|-----------------------------------------------------------|------------|
| `/feed.xml`        | One item per daily brief                                  | last 30    |
| `/feed-weekly.xml` | One item per weekly summary                               | last 30    |
| `/feed-items.xml`  | One item per metadata-footer block in any brief           | last 50    |

`<pubDate>` is the actual git first-commit timestamp on `main` for the
underlying brief (sourced from
`git log --diff-filter=A --format=%aI -- briefs/...`), falling back to file
mtime — never to midnight-of-brief-date.

`<content:encoded>` carries the full brief (or item) body rendered to HTML
on the build side. No raw Markdown emphasis (`**bold**`, `[link](url)`,
`` `code` ``) survives into the feed payload — a regex check in the build's
self-check fails the build if it does. No UTM parameters anywhere — every
link is plain canonical.

## Routing (clean URLs)

Every page has a real URL; deep links work, browser history works, view-
source shows the content.

| URL                                | View                                                        |
|------------------------------------|-------------------------------------------------------------|
| `/`                                | Home — TL;DR preview of the latest daily brief              |
| `/briefs/`                         | Brief index, grouped by month                               |
| `/briefs/<YYYY-MM-DD>/`            | Single daily brief (full content + aside-toc + cited footer)|
| `/briefs/weekly/`                  | Weekly summaries list                                       |
| `/briefs/weekly/<YYYY-Www>/`       | Single weekly summary                                       |
| `/items/<slug>/`                   | One page per metadata-footer item                           |
| `/entities/`                       | Unified entity index — every CVE / actor / campaign / incident / tool / advisory / annual report / research / technique. KPI strip, type-distribution donut, recent-coverage sparkline, filter chips |
| `/entities/<key>/`                 | Canonical entity detail. Story timeline + KPI tiles + section-distribution bars + source-host donut + co-occurring entities + grouped citations + embedded brief items |
| `/cves/`                           | Type-filtered view of `/entities/` (type=cve) — same CVE table as before, with the entity KPI strip + by-year bars on top |
| `/cves/<CVE-ID>/`                  | HTML meta-refresh stub → `/entities/CVE-<ID>/` (`noindex`)  |
| `/topics/`                         | Type-filtered view of `/entities/` (type≠cve) — same topic listing with verification-flag chips, KPI strip + type donut on top |
| `/topics/<key>/`                   | HTML meta-refresh stub → `/entities/<key>/` (`noindex`)     |
| `/sources/`                        | Source list                                                 |
| `/sources/<id>/`                   | Source detail + briefs that cite it                         |
| `/tags/<tag>/`                     | Items by theme tag                                          |
| `/regions/<region>/`               | Items by region                                             |
| `/ops/`                            | Run log + stale active sources                              |
| `/about/`                          | Landing page (Documentation + Prompts sections, plus README) |
| `/about/docs/`                     | Documentation index                                         |
| `/about/docs/<name>/`              | One page per `docs/<name>.md`                               |
| `/about/prompts/`                  | Prompts index + recent CHANGELOG headings                   |
| `/about/prompts/<name>/`           | One page per `prompts/<name>.md` (excl. CHANGELOG)          |
| `/about/prompts/changelog/`        | Full `prompts/CHANGELOG.md`                                 |
| `/feed.xml`, `/feed-weekly.xml`, `/feed-items.xml` | RSS                                       |

## Unified search

`assets/js/search.js` runs a small token-prefix scorer over the flat
`search.json` index built by `build.py`. Tokens are AND-combined; CVE ids
match as a single token regardless of the surrounding query. The top-bar
autocomplete returns the top 10 across all kinds; `Enter` navigates to the
top match. Search results route to the canonical `/entities/<key>/` URL
for both CVE and non-CVE hits.

The search data is loaded on demand the first time the user types, then
cached for the session.

## Keyboard

- `/` — focus the global search box
- `↑` / `↓` — move through suggestions
- `Enter` — open the highlighted suggestion (or the top match)
- `Esc` — clear suggestions and unfocus

## Determinism

Two consecutive runs with no input changes produce a byte-identical site
(`writes=0` on the second run). Achieved by:

- `pubDate` from git commit timestamps, not `now()`
- `<lastBuildDate>` from the most-recent input timestamp, not `now()`
- Asset cache-bust hash from asset bytes, not build moment
- Atomic per-file writes (temp + `os.replace`)
- End-of-build orphan prune

A failed build leaves the previous live site untouched.

## Local development

```bash
# Generate the bundle.
python3 site/build.py

# Run the unit tests.
python3 site/test_build.py

# Serve. The site is fully static; any HTTP server works.
python3 -m http.server 8765 --directory site/_site
```

Open <http://localhost:8765/>. There is no watcher; rerun `build.py` after
editing source files. Browser DevTools → Network → "Disable cache" is useful
when iterating on `assets/`.

## Deployment

The site deploys via [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml).
It triggers on every push to `main` that touches `briefs/`, `state/`,
`sources/`, `docs/`, `prompts/`, `README.md`, or `site/` (the inputs the
build reads). The workflow runs `build.py` and force-pushes the result to
the `gh-pages` branch.

One-time enable: GitHub repo → Settings → Pages → Build and deployment →
Source: **Deploy from a branch** → **gh-pages** / **/ (root)**.

## Why this design

- **Zero build dependencies.** The build script is stdlib-only Python; the
  vendored libs are integrity-checked by SHA-256 on every build. No npm,
  no transpiler, no lockfile.
- **HTML is the contract.** All content is in the served HTML; readers
  with JS disabled, scrapers, archive.org snapshots, and feed readers all
  see the same thing.
- **Markdown stays canonical.** The Markdown files in `briefs/` remain the
  authoritative copy — the site is a view, not a transform. The "Raw .md"
  link on every brief page exposes the underlying file.
- **Privacy-by-design analytics only.** Umami Cloud (no cookies, no
  fingerprinting). Documented at `/about/docs/analytics/`.
- **Defence in depth at the sink.** Strict CSP. Build-time Markdown
  rendering allowlists tags + URI schemes; no `<script>`, no `<iframe>`,
  no `javascript:` / `data:` URIs survive.

## Adding a new view

1. Add a renderer in `site/build.py` (Python f-string template).
2. Wire it into `main()` — call `emit_html(rel_url, html)` to publish.
3. If new data joins are needed, extend the annotators + the search index.
4. `python3 site/build.py && python3 -m http.server 8765 --directory site/_site`.
