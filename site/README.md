# site/ — public reader for the brief feed

A static, dependency-free GitHub Pages site that renders the daily and weekly
Markdown briefs, exposes searchable indexes of CVEs / topics / sources, and
cross-links every entity to the briefs that reference it. Read-only — the
agentic workflow (`prompts/`, `state/`, `sources/`) is the source of truth;
this folder only **publishes** what the agent produces.

```
site/
├── index.html             # SPA shell
├── build.py               # Stdlib-only Python: parses content into _site/
├── README.md              # this file
└── assets/
    ├── css/styles.css     # Dark-first stylesheet
    ├── js/
    │   ├── store.js       # Loads JSON bundles, memoizes brief markdown
    │   ├── search.js      # Token-prefix scoring across the unified index
    │   ├── render.js      # View templates per route
    │   ├── router.js      # Hash-based routing
    │   └── app.js         # Boot, global search box, keyboard shortcuts
    └── vendor/
        ├── marked.min.js  # Markdown → HTML  (MIT)
        └── purify.min.js  # HTML sanitizer  (Apache 2.0 / MPL 2.0)
```

## What the build produces

`python3 site/build.py` writes a self-contained bundle to `site/_site/`:

```
_site/
├── .nojekyll
├── index.html
├── assets/...                 # copied unchanged
├── briefs/<name>.md           # copied raw briefs (fetched on demand by the SPA)
├── docs/<name>.md             # copied raw docs for the About page
└── data/
    ├── manifest.json          # one entry per brief
    ├── cves.json              # cves_seen.json + brief appearances
    ├── topics.json            # covered_items.json + extracted brief names
    ├── sources.json           # sources.json + brief appearances
    ├── search.json            # flat unified search index
    └── site.json              # build timestamp + counts
```

The cross-references between entities and briefs are computed once, at build
time, by walking the briefs and joining against state files:

| Entity  | Joined to brief by                                          |
|---------|--------------------------------------------------------------|
| CVE     | regex match on `CVE-YYYY-NNNNN` in the brief markdown       |
| Topic   | `appearances[].brief_path` already in `covered_items.json`  |
| Source  | hostname match between `sources.json#url` and brief links   |

Multi-appearance items get a "story timeline" badge (`×N appearances`)
everywhere they show up, so a reader can immediately tell when a topic has
unfolded across multiple briefs.

## Routing

Hash routes — Pages serves the same `index.html` for every URL:

| URL                      | View                                  |
|--------------------------|----------------------------------------|
| `#/`                     | Home (newest brief TL;DR + stats)     |
| `#/briefs[?q=&kind=]`    | Brief index, grouped by month          |
| `#/briefs/<name>`        | Single brief (full markdown render)    |
| `#/cves[?q=]`            | All CVEs ever referenced              |
| `#/cves/<id>`            | One CVE + brief appearance trail       |
| `#/topics[?q=&type=]`    | Covered items (CVEs/actors/incidents) |
| `#/topics/<key>`         | Topic timeline                        |
| `#/sources[?q=&cat=]`    | Source list                           |
| `#/sources/<id>`         | Source detail + briefs that cite it   |
| `#/search?q=...`         | Cross-entity search results page      |
| `#/about`                | Renders README + workflow + verification |

## Unified search

`assets/js/search.js` runs a small token-prefix scorer over the flat
`search.json` index built by `build.py`. Tokens are AND-combined; CVE ids
match as a single token regardless of the surrounding query. Score weights
favor exact id matches, then title prefixes, then word-prefix matches in the
title, then hint substring matches. Results are grouped by kind on the search
page; the top-bar suggestions return the top 10 across all kinds.

## Keyboard

- `/` — focus the global search box
- `↑` / `↓` — move through suggestions
- `Enter` — open the highlighted suggestion (or run a full search if none)
- `Esc` — clear suggestions and unfocus

## Local development

```bash
# Generate the bundle.
python3 site/build.py

# Serve it. The site is fully static; any HTTP server works.
python3 -m http.server 8765 --directory site/_site
```

Open <http://localhost:8765>. There is no watcher; rerun `build.py` after
editing source files. Browser DevTools → Network → "Disable cache" is useful
when iterating on `assets/`.

## Deployment

The site deploys via [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml).
It triggers on every push to `main` that touches `briefs/`, `state/`,
`sources/`, `docs/`, `README.md`, or `site/`. The workflow runs `build.py`,
uploads `site/_site/` as a GitHub Pages artifact, and deploys it.

One-time enable: GitHub repo → Settings → Pages → Build and deployment →
Source: **GitHub Actions**.

## Why this design

- **Zero build dependencies.** The build script is stdlib-only Python; the
  SPA uses two small vendored libraries. No npm, no transpiler, no lockfile.
  A clean clone builds and serves in under five seconds.
- **The data is the contract.** Everything the SPA does is driven by the
  five JSON files in `data/`. Anyone can write a different reader without
  changing the agentic workflow.
- **Markdown stays canonical.** Briefs are served as raw Markdown, rendered
  client-side. The Markdown files in `briefs/` remain the authoritative
  copy — the site is a view, not a transform.
- **No tracking, no analytics, no cookies.** A pure read-only feed.

## Adding a new view

1. Add a render function in `assets/js/render.js` that returns an HTML string.
2. Wire a route in `assets/js/router.js` `dispatch()`.
3. If new data joins are needed, extend `site/build.py` and bump the data
   shape in `assets/js/store.js` accordingly.
4. `python3 site/build.py && python3 -m http.server 8765 --directory site/_site`.

The split between `store` (data), `search` (matching), `render` (templates),
`router` (URL → render), and `app` (boot + global UI) is deliberately tight
so each file fits in one screen.
