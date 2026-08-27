# site/ — public reader for the intelligence pipeline

A static, dependency-free GitHub Pages site that renders the pipeline's
content store server-side: per-finding **entries** (`entries/`), per-run
records (`runs/`), and the global **entity registry**
(`entities/registry.yaml`), cross-linked with the source list. The
signature page is **`/live/`** — the brief is a *query*: the reader picks
a time window (default last 24 h) and the page renders a run-grouped
timeline of every run in that window (quiet 0-finding runs included).
`/daily/` archives each **completed** UTC day. A finding has ONE entry for
its whole life (v4.0): developments, corrections and improvements are
appended to it as a dated changelog (`updates[]`), and an update floats
the entry back into the live window under the run that made it. Read-only: the agentic
workflow (`prompts/`, `entries/`, `runs/`, `entities/`, `state/`,
`sources/`) is the source of truth; this folder only **publishes** what
the pipeline produces.

The deployed site lives at <https://ctipilot.ch/>.

## Architecture (v4 — static-site generator + one dynamic page)

Every URL is a real HTML page rendered at build time. The topbar is a
segmented **Live / Daily** control plus a search modal, a display
& accessibility popover (light / dark / system theme, dyslexia-friendly
font, comfortable spacing), and a GitHub-stars badge; a second
**knowledge-base subnav** row (desktop) links every pivot surface exactly
once — Entities · CVEs · ATT&CK · Sources · Trends · Operations on the
left, Feeds · About right-aligned — with the active surface highlighted
(there is no desktop "More" menu; the mobile drawer carries the same
links); the footer is a single minimal row. JavaScript is progressive enhancement only
(search modal + autocomplete, GitHub-stars fetch, finding chip filters,
theme / accessibility toggles, AI-bar dismiss, copy-link, and `/live/`'s
window selector + load-older). With JS disabled the site is fully readable:
`/live/` serves its server-rendered default 24 h timeline; only re-windowing
and the chip filters need JS.

```
site/
├── build.py               # Stdlib-only Python SSG. Single entrypoint.
├── content_model.py       # THE shared parser/loader/validator for entries,
│                          # registry and run records (also imported by
│                          # tools/check_run.py and tools/migrate_briefs.py).
│                          # Schema-invalid content aborts the build.
├── branding_config.py     # Loader for config/branding.yaml — site identity,
│                          # theme overrides, logos, chart palettes, feeds,
│                          # analytics. Fail-loud on unknown keys; the shipped
│                          # config builds a byte-identical site. See
│                          # docs/customization.md.
├── branding/              # Downstream-owned brand assets (logos, favicon,
│                          # fonts, custom.css). Upstream ships only a README.
├── taxonomy.yaml          # Controlled vocabulary (themes, regions, sectors,
│                          # CVE record fields, render-section keys). The
│                          # build refuses any entry using a value not in here.
├── test_build.py          # Stdlib-only smoke tests (Markdown render, content-
│                          # model round-trip, section assembly, briefbook/
│                          # alerts shape, feeds, branding contract).
├── README.md              # this file
└── assets/
    ├── css/styles.css     # Dark-first stylesheet: light/dark/system theme,
    │                      # dyslexia-friendly + comfortable-spacing modes, print
    ├── js/
    │   ├── theme.js       # data-theme (system/light/dark) + data-font (dyslexic)
    │   │                  # + data-density (comfortable); applied before paint
    │   ├── search.js      # Token-prefix scoring across data/search.json
    │   ├── app.js         # Topbar menus/drawer/display popover, search modal,
    │   │                  # AI-bar dismiss, copy-link, finding chip filters
    │   └── brief.js       # /live/ window selector + load-older: re-renders the
    │                      # run-grouped timeline from data/briefbook.json
    └── vendor/
        ├── HASHES         # SHA-256 + SHA-384 known-good hashes; build aborts on mismatch
        ├── marked.min.js  # vendored, unused at runtime (kept integrity-pinned)
        ├── purify.min.js  # vendored, unused at runtime (kept integrity-pinned)
        └── filter.min.js  # First-party in-page filter UI for day pages (under 4 KB)
```

## What the build produces

`python3 site/build.py` writes a self-contained bundle to `site/_site/`:

```
_site/
├── index.html                            # Home — live-brief card + latest day + recent updates card
├── live/index.html                       # THE dynamic brief (default: last 24 h server-rendered as a
│                                         #   run-grouped timeline BY ACTIVITY; brief.js re-windows
│                                         #   from data/briefbook.json)
├── daily/
│   ├── index.html                        # day archive, grouped by month
│   └── YYYY-MM-DD/index.html             # static day page — that UTC day's operational entries in
│                                         #   the canonical structure + § Updates to Prior Coverage
│                                         #   (every changelog record dated that day) + run notes
├── entries/YYYY-MM-DD/<slug>/index.html  # per-entry permalink: badge strip, main analysis, evidence,
│                                         #   changelog sections (styled .entry-update blocks),
│                                         #   Revision history, sources with roles, entity links,
│                                         #   run link. Folded v3 update entries' old URLs are
│                                         #   noindex redirect stubs to the living entry (#update-<at>)
├── entities/{index.html,<key>/…}         # unified entity pages (registry + CVEs) — typed
│                                         #   relationships + derived co-occurrence sections
├── graph/index.html                      # interactive threat graph (canvas, assets/js/graph.js)
├── cves/ · topics/                       # type-filtered views + legacy redirect stubs
├── sources/{index.html,<id>/…}           # source list + detail (entry-based citations)
├── tags/<tag>/ · regions/<region>/       # per-tag / per-region entry indexes
├── trends/index.html                     # momentum analysis: cohort tiles (complete-week deltas),
│                                         #   cohort×week matrix, entity + ATT&CK technique momentum
├── ops/index.html                        # operations dashboard, built from runs/** frontmatter
├── feeds/index.html                      # feed discovery
├── feed.xml                              # one item per day page (last 30)
├── feed-items.xml                        # one item per ENTRY (pubDate = discovered_at) + one item per
│                                         #   changelog record (guid <url>#update-<at>, pubDate = at) (last 50)
├── feed-<sector>.xml ×8                  # sector slices of the per-entry feed
├── about/…                               # README, docs/ (incl. pipeline.md), prompts/, changelog
└── data/
    ├── briefbook.json                    # last ~35 days of entries BY ACTIVITY + runs with pre-rendered
    │                                     #   HTML cards and the changelog (updates, updated_at,
    │                                     #   activity_at, activity_run_id, activity_is_update) — the
    │                                     #   /live/ client data
    ├── alerts.json                       # last 7 days (by activity) of critical/high entries with
    │                                     #   immediate_action + updated_at/updates — the notification-hook surface
    ├── graph.json                        # the threat graph: entity/CVE/technique nodes +
    │                                     #   curated typed edges (with source entries) +
    │                                     #   derived co-occurrence/CVE/technique edges
    ├── search.json · site.json · build_manifest.json
```

Plus `.nojekyll`, `404.html`, `sitemap.xml`, `robots.txt`,
`.well-known/security.txt`, and `CNAME`. The reading routes are `/live/`
(rolling) and `/daily/` (completed days); the design refresh renamed the
earlier `/brief/` and `/briefs/` routes and keeps no legacy redirects for
them, and v4.0 retired `/weekly/` with the weekly routine (the historical
`horizon: strategic` entries stay reachable by permalink, entity, CVE, tag,
region and search).

## Discoverability (SEO + machine-readability)

Every page ships from `base_template()` with a full search/social/AI head:
`<title>`, meta description, `<link rel=canonical>`, per-page-type
OpenGraph + Twitter cards, and schema.org **JSON-LD** data islands
(`<script type="application/ld+json">` — non-executable, so the CSP
`script-src 'self'` self-check exempts them; every string is
unicode-escaped so entry text can't break out of the element). The
structured-data builders are the `_ld_*` helpers just above
`base_template`; each render function passes a small `seo=` dict
(`og_type`, `breadcrumb`, `article`, `json_ld`):

| Page | `og:type` | JSON-LD |
|---|---|---|
| Home | `website` | `WebSite` + `Organization` |
| Entry permalink | `article` | `Article` / `TechArticle` (`datePublished` = `discovered_at`, `dateModified` = `updated_at`, `keywords` from tags+regions, `about` → CVEs/entities) + `BreadcrumbList` |
| Day brief | `article` | `CollectionPage` + `ItemList` of the brief's entries + `BreadcrumbList` |
| Index / entity / source / tag / region | `website` | `CollectionPage` (+ `ItemList` where cheap) + `BreadcrumbList` |

Identity fields (`WebSite`/`Organization` name, publisher, `sameAs`)
resolve from the branding constants — never a literal — so a fork
rebrands from `config/branding.yaml`. Breadcrumb trails are explicit
(not URL-derived) so every crumb points at a page that exists.
`sitemap.xml` lists only canonical, indexable URLs: the legacy
`noindex` meta-refresh redirect stubs (`/cves/<id>/`, `/topics/<key>/`)
are written for back-compat but excluded (`emit_html(..., index=False)`).
`robots.txt` is fully permissive (`Allow: /` for every crawler, including
AI agents) and points at the sitemap. No `og:image` ships by default (the
site is deliberately image-free); the `seo["image"]` hook lets a fork add
one. No `llms.txt` — Google Search ignores it and it adds nothing.

## Cross-references

All joins are computed at build time from frontmatter — there is no
scraping and no state-file joining:

| Join | Source |
|---|---|
| Entry → sections | `kind` (+ `deep_dive` → Deep Dive) via `content_model.KIND_DAILY_SECTION`; § Updates is derived from `updates[]` records dated in the day |
| Entity → entries | explicit `entities:` registry keys, plus word-boundary name/alias phrase matching against titles/bodies (short all-caps acronyms match case-sensitively) |
| Entity ↔ entity | curated typed `relations[]` (registry; each edge cites its establishing entry) + derived same-entry co-occurrence — rendered on entity pages and `/graph/` |
| CVE → entries | `cves[].id` frontmatter records (+ `state/cves_seen.json` for historical context) |
| Source → entries | longest-prefix URL match between `sources.json#url` and `sources[]` records |
| Tag / Region | `tags:` / `regions:` frontmatter (taxonomy-validated) |
| Changelog | `updates[]` records paired with `## <Type> — <at>` body sections (`content_model.split_update_sections`); rendered as blocks on cards and entry pages, as update cards in a day's § Updates, as `.tl-update` rows in the live timeline, as extra feed items, and as the Revision history panel |
| Run → entries | `run_id` frontmatter (published) + `updates[].run_id` (updated); the run detail page lists both |

## Determinism

Two consecutive runs with no input changes produce a byte-identical site
(`writes=0` on the second run): the build's "now" is the newest content
moment (`discovered_at` / `updated_at` / run `completed`) rather than wall-clock;
`pubDate` comes from `discovered_at` (true discovery latency); the
cache-bust hash comes from asset bytes; writes are atomic with an
end-of-build orphan prune. A failed build leaves the previous live site
untouched — schema-invalid entries abort loudly instead of publishing
partial output.

## Local development

```bash
python3 site/build.py          # generate the bundle
python3 site/test_build.py     # run the unit tests
python3 -m http.server 8765 --directory site/_site
```

Open <http://localhost:8765/>. No watcher; rerun `build.py` after editing.

## Deployment

Via [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml):
triggers on every push to `main` touching `entries/`, `runs/`, `entities/`,
`state/`, `sources/`, `docs/`, `prompts/`, `README.md`, or `site/`; runs
`build.py` and force-pushes the result to `gh-pages`.

One-time enable: GitHub repo → Settings → Pages → Build and deployment →
Source: **Deploy from a branch** → **gh-pages** / **/ (root)**.

## Why this design

- **Zero build dependencies.** Stdlib-only Python; vendored libs are
  integrity-checked by SHA-256 on every build.
- **HTML is the contract.** All content is in the served HTML; readers with
  JS disabled, scrapers, archive.org snapshots and feed readers all see the
  same thing. The dynamic brief degrades to its server-rendered default window.
- **Frontmatter is canonical.** The entry files in `entries/` remain the
  authoritative copy — the site is a view, not a transform. `briefbook.json`
  and `alerts.json` expose the same structured metadata to automation
  (notification hooks key off `priority` + `immediate_action`).
- **Privacy-by-design analytics only.** Umami Cloud (no cookies, no
  fingerprinting). Documented at `/about/docs/analytics/`.
- **Defence in depth at the sink.** Strict CSP (JSON data islands only —
  no executable inline scripts). Build-time Markdown rendering allowlists
  tags + URI schemes; no `<script>`, no `<iframe>`, no `javascript:` /
  `data:` URIs survive.

## Adding a new view

1. Add a renderer in `site/build.py` (Python f-string template).
2. Wire it into `main()` — call `emit_html(rel_url, html)` to publish.
3. If new data joins are needed, extend the entry/entity annotators + the
   search index.
4. `python3 site/build.py && python3 -m http.server 8765 --directory site/_site`.
