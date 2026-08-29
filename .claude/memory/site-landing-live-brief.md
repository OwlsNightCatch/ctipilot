---
name: site-landing-live-brief
description: "2026-08-29 landing-page structure: / IS the live brief, findings lead and positioning sits at the foot, § Do now, phone-first timeline, /changes/, raw-md twins"
metadata:
  type: project
---

Operator directive 2026-08-29: minimize clicks-to-content, maximize landing-page
content, first-class AI-agent readability, mobile-friendly.

- **`/` IS the live rolling brief** (`render_live_brief_page`, prefix `""`,
  canonical = site root). The old card home (`render_home_page`) is deleted;
  its pivot band + counts moved BELOW the timeline (`.explore` band reusing
  `.pivotband`). Root JSON-LD: `WebSite` + `Organization` +
  `CollectionPage`/ItemList of the current window.
- **Findings lead, positioning follows (2026-08-29, second directive: "less
  prominent info blocks, focus on content not marketing").** Top of `/` is now
  `.briefhead` only: h1 = branding `live_title` (default "Live threat brief",
  19px), then a one-line `.briefstat` (LIVE dot, updated stamp, window
  `<select>`). The marketing hero (`hero_eyebrow` / `hero_title` /
  `hero_subtitle`) renders at the FOOT as `.sitenote`, below `.explore`. The
  old `.hero--live`, `.livehead`, `.live-lede` and `.rangebar` blocks are
  retired in build.py AND in the CSS — do not reintroduce them. Window bounds
  moved into `.pulsewindow` at the foot of the pulse panel.
- **§ Do now (`render_donow`, `.donow`)** sits between ACT NOW and the pulse
  panel: every `actions[]` task in the reader's window, aggregated into the
  `.action-list` markup the day pages use. It hides itself when the window
  carries no actions. brief.js `donowHtml()` mirrors it on window/filter
  change — keep the two in sync, same as `runItem`/`runDivider`.
- **Phone pass (≤639px, appended last in styles.css).** The timeline drops its
  96px rail: `.tl-item`/`.tl-run` go single-column, the stamp+flag ride above
  the badges as one meta line, and a hairline carries the run rhythm. The
  pulse grid becomes a wrapping stat row. Safe-area insets on `.main`. The
  empty-window stub no longer hard-codes `margin-left:96px` (build.py AND
  brief.js).
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
See [[design-system]], [[customization-framework]] (nav labels/hero/live_title
stay branding-driven, no identity literals in build.py), [[ui-writing-style]].
