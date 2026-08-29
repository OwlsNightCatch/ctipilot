---
name: site-landing-live-brief
description: 2026-08-29 operator-directed site restructure — the landing page IS the live brief; /changes/, raw-md entry twins, llms.txt; what replaced the old home page
metadata:
  type: project
---

Operator directive 2026-08-29: minimize clicks-to-content, maximize landing-page
content, first-class AI-agent readability, mobile-friendly.

- **`/` IS the live rolling brief** (`render_live_brief_page`, prefix `""`,
  canonical = site root). The old card home (`render_home_page`) is deleted;
  its pivot band + counts moved BELOW the timeline (`.explore` band reusing
  `.pivotband`), the hero is the compact `.hero--live` variant (h1 = branding
  `hero_title`; "Latest findings" is an h2). Root JSON-LD: `WebSite` +
  `Organization` + `CollectionPage`/ItemList of the current window.
- **`/live/` is a noindex meta-refresh stub → `/`** (`index=False`, out of the
  sitemap). Never reintroduce a full page there — one canonical URL for the brief.
- **`/changes/`** (`render_changes_page`): every visible `updates[]` record
  store-wide, newest first, grouped by UTC day, deep-linked to
  `<entry>#update-<at>`; third nav segment (Live · Daily · Changes,
  `nav_changes` branding key; mobile `.mseg` flexes all three).
- **Raw Markdown twins:** every entry permalink also serves its exact source at
  `<permalink>index.md` — advertised via `<link rel="alternate"
  type="text/markdown">`, a `raw .md` link on the entry meta line, JSON-LD
  `encoding` MediaObject, and `markdown_url` in `data/briefbook.json`.
  Folded-entry redirect stubs correctly have NO index.md — don't mistake one
  for a regression when spot-checking.
- **`/llms.txt` exists now** (write_llms_txt) — this REVERSED the earlier
  "no llms.txt" decision recorded in site/README.md; AI agents are first-class
  readers per this directive.

**Why:** the old home was an interstitial costing every reader a click and
giving the most-linked URL the thinnest content; agents/search now get the full
brief + identity + machine endpoints in one fetch of `/`.

**How to apply:** internal links to the brief use the page prefix alone
(`prefix or "./"`), never `live/`. briefbook.json URLs stay `../`-prefixed
(correct relative to the file; brief.js strips and re-applies `cti-site-prefix`).
See [[design-system]], [[customization-framework]] (nav labels/hero stay
branding-driven, no identity literals in build.py).
