---
name: site-landing-live-brief
description: "Landing-page structure: / IS the live brief; one-line head, compact critical alarm, feed head with counts, whole-row-clickable timeline with Summaries/Headlines switch (2026-09-29: § Do now + pulse panel removed); positioning at the foot, /changes/, raw-md twins"
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
  old `.hero--live`, `.live-lede` and `.rangebar` blocks are retired in
  build.py AND in the CSS — do not reintroduce them. The head is
  `header.livehead` (NOT `.briefhead`, which is the day page's date-nav row).
  The window is named by the `<select>` alone; "load older" past the preset
  choices appends a matching option so the control never lies.
- **2026-09-29 operator directive: nothing between the head and the findings
  but a very short critical alarm.** § Do now (`render_donow`), the big
  ACT NOW card (`render_actnow`) and the window pulse panel (`.pulsepanel`,
  category chips, window-bounds line) are DELETED in build.py, brief.js
  and the CSS; do not reintroduce them. `actions[]` still renders on day
  pages (§ Action Items) and entry permalinks (Defender actions).
- **Critical alarm (`render_alarm`, `.alarm` / `.alarm-row`)**: one compact
  row per `priority: critical` entry in the window: CRITICAL tag,
  `immediate_action.title` (short imperative; headline fallback via
  `_alarm_text`), a mono meta line, the whole row a link. Hidden empty
  container when there is none. It follows the WINDOW, never the chip
  filters. Day pages use the same renderer. brief.js `alarmHtml` mirrors it.
- **Feed head**: h2 + tools (Summaries / Headlines `.viewseg`, Filter) on
  row one, the window counts (`.feedstats`, `data-window-{total,crit,high,
  exp,upd}`) on row two, then one `.feedhint` line ("Click/Tap any finding
  to open its full analysis", Click vs Tap swapped by `(hover: none)`). On
  phone `.feedhead-tools` is `display: contents` so Filter rides the title
  row and the density switch gets its own full-width row.
- **Timeline rows are whole-row links** (`.tl-item[data-card]`): brief.js
  delegates the click to the title link, skips inner links, never hijacks
  a text selection, waits one double-click interval on summary prose so
  double-click-to-copy works, and opens a new tab on ctrl/meta/middle
  click. Hover/focus-within paints a `.tl-body::before` plate. The meta row
  (`.tl-meta`) ends in an aria-hidden "Full analysis →" CTA (not "open ↗":
  ↗ reads as external). Summaries clamp to 6 lines (7 on phone) with CSS
  only, the full text stays in the DOM for agents. `.tl--compact`
  (Headlines, remembered in localStorage `cti-brief-view`) hides summary +
  sources. UPD rows name "first published …" in the meta row.
- **Phone pass (≤639px, appended last in styles.css).** The timeline drops its
  96px rail: `.tl-item`/`.tl-run` go single-column, the stamp+flag ride above
  the badges as one meta line, and a hairline carries the run rhythm.
  Safe-area insets on `.main`. The
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

**Why (2026-09-29):** the operator wants the landing to be skimmed and
triaged in seconds on a laptop or a phone: an alarm that fits in one row,
then the day's entries, with an obvious way into the detail.

**Why (2026-08-29):** the old home was an interstitial costing every reader a click and
giving the most-linked URL the thinnest content; agents/search now get the full
brief + identity + machine endpoints in one fetch of `/`.

**How to apply:** internal links to the brief use the page prefix alone
(`prefix or "./"`), never `live/`. briefbook.json URLs stay `../`-prefixed
(correct relative to the file; brief.js strips and re-applies `cti-site-prefix`).
See [[design-system]], [[customization-framework]] (nav labels/hero/live_title
stay branding-driven, no identity literals in build.py), [[ui-writing-style]].
