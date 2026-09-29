---
name: design-system
description: The site's visual language, its Claude Design source project, and the invariants any site/build.py or CSS change must respect
type: reference
---

# Design system — where it lives and what not to break

Source: the "CTI Pilot Design Modernization" Claude Design project (id `1ca3b2f3-7d01-40ca-8d48-781bbf3c08b9`, via DesignSync MCP). Live implementation: `site/assets/css/styles.css` (component classes `.seg .aibar .alarm .feedhead .tl-* .finding .sect .verif .bcard .erail .rankbar …`), `site/build.py` (`base_template` + renderers), JS `theme.js`/`app.js`/`brief.js` (DOM contract: `data-theme/-font/-density` on `<html>`; `cti:filterchange` links app.js chips → brief.js timeline).

**Design DNA:** dark-first analyst console (`--bg #0e1116`), one crimson accent, sans/mono split (mono = every machine fact), border-not-shadow, small radii, no emoji, no IOCs.

**Brandable surface** = `config/branding.yaml` only ([[customization-framework]]): colors/fonts/radii/logos/nav/hero/ai-bar copy; overriding an accent hex auto-derives `--accent-rgb` so translucent fills follow. Fonts stay system-stack — no external webfont (CSP + load).

Invariants learned the hard way:
- **Never re-enable `"dlig"`** in heading `font-feature-settings` — stray glyph artifacts on Linux fallback fonts. Keep `"kern","liga"`.
- Inline-token prose rules sharing a class with a badge need a `:not(.b)` guard (`.finding .cve` once inflated `.b.cve` badges).
- Trends statistical honesty: the running ISO week is partial and never compared; deltas = latest complete week vs prior.
- Verification flags render neutral — red is reserved for priority/exploited.
- Classification badges/scheme text are config-driven (`_load_classification_scheme()`); never re-hardcode doctrine. `_chrome_text()` sanitizes config strings for chrome (em dash → `·`, per [[ui-writing-style]]).
- Routes: `/live/` (rolling, ordered by activity; only non-internal `type: update` records re-float) and `/daily/` (completed days). `/weekly/` was removed 2026-08-27 with the weekly routine; entry pages carry timestamped `## <Type> — <at>` blocks + a revision-history panel.

## Document contract (2026-08-29 design pass)

Rendering invariants a `site/build.py` change must not regress. All three are
mechanically checkable across the emitted store, so re-check them after any
renderer edit:

- **One heading outline per page.** Exactly one `<h1>` (redirect stubs excepted
  — `/cves/*`, `/topics/*`, folded entries and `/live/` are meta-refresh pages
  with none), no skipped levels. Embedded markdown never keeps its own level:
  `render_markdown(..., heading_base=N)` pins a document's own top heading to
  N whatever it was authored at (records open at `#` OR `##`, so a fixed
  `heading_offset` skips a level in half of them). `heading_base` now
  RE-LEVELS in reading order (first heading lands on the base; each later one
  is a sibling of, or one below, its nearest shallower ancestor), so an
  authoring gap (an entry opening at `####` whose `###` appears only later)
  can never emit a skipped level. Run notes pass `head_level`; entry bodies
  pin to h3, under the Analysis section's h2. Day-brief section headers are `<h2
  class="sect">`, not divs.
- **Ids are unique per page and every `#anchor` resolves.** Heading anchors
  take `anchor_prefix` (run id) and de-duplicate within a document
  (`_unique_anchor`); `#update-<at>` is emitted only on the entry permalink
  (`anchor=False` everywhere else); finding anchors use the entry id, not the
  slug (two dates can share a slug); the ATT&CK directory gives the bare
  `#T…` to the first occurrence and namespaces tactic repeats; a matrix cell
  is a link only when its directory row exists.
- **AA contrast in BOTH themes, measured with alpha compositing.** Translucent
  tints must be composited before the ratio means anything. `--text-muted` is
  the most-used text colour — it has to clear 4.5:1 on `--bg`, `--bg-elev`,
  `--bg-elev-2` AND `--kbd-bg`. Heat/tint surfaces (ATT&CK cells) fail from
  opposite directions per theme; page-text colour is the only value that
  clears both. Never de-emphasise with `opacity` (0.45 = ~2.5:1) — use
  `--text-muted`.

## Entry permalink (2026-08-29 rebuild)

`render_entry_page` is a header + a reading column + a rail, in one grid:
`.ehead` spans both columns, `.entry-main` is column 1, `.erail` is column 2
(explicit `grid-column` / `grid-row`, so the source order stays header ->
article -> rail and the phone order comes out right without `order`).

- **All metadata lives in the rail, labelled.** `render_entry_rail` groups it
  in use order: CVEs, Affected products, Assessment, Entities, ATT&CK
  techniques, Builds on, Tags, Regions, Sectors, and **Record last** (published
  / event / sources / raw `index.md` / producing run / imported-from). The
  run-dashboard link belongs in Record, never under the title (operator
  directive 2026-08-29). Every table row is a `.frow` (`__l` label / `__v`
  value); `.assess-*` and `.erail-cve__meta|__ver|__vl` are retired.
- **The rail never scrolls on its own and is never sticky.** A metadata column
  the reader has to scroll separately is a second document. One page, one
  scrollbar.
- **Under the title: one dateline and the share button.** `.emeta__stamps`
  carries published + updated (the updated stamp deep-links to the newest
  `#update-<at>`), nothing else. `.edeck` is gone; the headline renders as
  `.elede` and is **suppressed when it merely restates the title** (723 of
  1222 entries). The stored `summary` is never repeated here, the reader
  read it on the page that linked in.
- **The gap under the header belongs to the header.** `.ehead` carries
  `margin-bottom: 34px` and BOTH columns zero their first child
  (`.entry-main > :first-child`, `.erail > :first-child`), so the callout,
  the first `.esec` and the rail all start on the same line and an entry
  with no immediate action is spaced exactly like one with it. Putting the
  margin on `.immediate-action` instead gave 0px with a callout and 34px
  without one.
- **One measure.** `--entry-col` / `--entry-rail` / `--entry-gap` live on
  `body.entry-detail` INSIDE the >=1100px query; `.view` max-width is derived
  from them and `.elede` / `.emeta` borrow `--entry-col` (fallback 100%), so
  header and body share both edges at every width.
- **Body order is actionable-first:** immediate action, Defender actions,
  Analysis, Cited evidence, Updates, ATT&CK mapping, Sources, Revision
  history and provenance, every one an `.esec` with an `h2.esec-h` (count in
  `.esec-n`), so the page is a sequence of equal sections.
- **A quote appears once.** The immediate-action callout carries neither the
  first evidence quote (Cited evidence owns every quote) nor a link to the
  page it is already on. `.entry-cite--inline` is retired.
- **No in-body ATT&CK section** (removed 2026-08-29): the rail lists every
  mapped technique and each chip pivots to `{prefix}attack/#<tid>`, which
  already carries the definition, the MITRE page and every other entry
  mapping it. `render_entry_attack_section` is deleted;
  `render_entity_attack_section` (entity pages) stays.
- **A chip must be able to shrink.** An entity name as a bare text node
  inside an inline-flex chip cannot wrap and spills back over the type
  label; the name needs its own `.echip-t` span with `min-width: 0`, and
  `.echip` needs `max-width: 100%`.
- **Affected-product chips link to the product entity** ([[product-entities]]);
  the entity page's own pivot row does too, minus the page's own product.
- **Pipeline internals stay out of the reading flow.** `render_update_block`
  takes `with_provenance`; the permalink passes False, so the run link and the
  raw changed-field names appear only in the Revision-history panel. Day pages
  and feeds keep them (no history panel there).
- **`.erail .erail-h` needs two classes** or `.view h2` steals its size and
  margin, the same trap as everything else in this file.

## Site-wide audit pass (2026-09-29)

A laptop + phone review of every template; the fixes live in the
"SITE-WIDE AUDIT PASS" block near the end of styles.css. Contracts:

- **Sticky header needs `overflow-x: clip`, never `hidden`, on html/body.**
  `hidden` on both made body the scroll container and silently killed
  `position: sticky` site-wide. Header is sticky at >=861px only (phones
  scroll it away); anchors clear it via `html { scroll-padding-top:
  calc(var(--sticky-h) + 12px) }` (`--sticky-h` 106px desktop, 0 phone).
- **One gutter token** `--gutter` (14/18/26px) pads topbar, subnav, AI bar,
  mobile seg, main and footer, so every left edge lines up.
- **The brand SVG has no intrinsic size**: `.brand-mark svg` must be sized
  in CSS (22px) or it renders 0x0.
- **theme.js loads WITHOUT `defer`** so theme/font/density and
  `data-ai-ack` land before first paint. The AI bar ships visible in the
  HTML (no `hidden`) and CSS hides it under `:root[data-ai-ack]`; no-JS
  readers always see the disclosure.
- **Search modal is a real dialog**: focus trap, scroll lock
  (`body.modal-open`), focus returns to the opener, combobox ARIA,
  "no match" status line, visible close button (native search clear
  hidden), results list is static inside the panel. `Search.highlight`
  is one pass over RAW text (never regex over already-escaped HTML).
- **Phone topbar** carries a search icon next to the hamburger; the
  drawer closes on Escape / outside tap / opening search and swaps its
  icon + label.
- **List filter chips are `<button aria-pressed>`**, never spans; every
  filtered list shows a `.filter-empty` line when nothing matches. Day
  page filters also hide TL;DR lines / alarm rows / action items via
  `data-entry-id`, update section counts ("1 of 2 items"), hide jump
  chips of emptied sections, and a closed filter panel is
  `visibility: hidden` (out of the tab order).
- **CVE links point at `entities/<CVE>/`**, not the `/cves/<id>/`
  meta-refresh stub (badge, rail, pivot chips, brief.js).
- **One colour per entity type**: the graph's `--g-*` tokens drive the
  list label dot (`.e-tag--<type>` sets `--et`) and the type donut
  (`_entity_palette_color`, unless a fork sets `charts.entity_palette`).
- **Common-word entity names** ("fingerprint", "Falcon", "Troy") are
  handled by the registry's curated `ambiguous_labels` field (main,
  2026-09-29), not by a build-time heuristic: listed labels never
  phrase-match prose. Do not reintroduce a frequency guard in build.py.
- **Entry rail CVEs** collapse past 6: exploited/KEV keep cards, the rest
  are one-line rows in a `<details>`; CVE card facts use a label/value grid.
- **List pages** (/entities/, /cves/) wrap their charts in
  `details.kb-stats[data-fold-on-phone]` (app.js folds it on phones); the
  /cves/ table stacks into cards below 640px. `/changes/` expands the last
  7 days (`CHANGES_OPEN_DAYS`) and folds older days. `/tags/` and
  `/regions/` index pages exist. Docs under /about/ use the reading
  measure.
- **/attack/ compare mode** dims non-matching cells by background +
  `--text-muted` (never opacity) and the Navigator export reads the same
  `passingTechniques()` roll-up as the matrix, so layer == what is shown.
  The matrix box is viewport-capped with sticky tactic headers and the
  legend above it. **/graph/** has zoom buttons + pinch, `touch-action:
  pan-y` until the canvas is tapped (the page must stay scrollable past
  it on a phone), a server-rendered type legend from the same `--g-*`
  tokens, and a device-neutral "path to…" action (no shift-click only).
- **Internal links use →, external ↗.** Run records naming a source id
  outside sources.json render plain text (`_source_ref`), never a 404.

Traps: `var(--muted)` is NOT a token (five rules once asked for it and
silently inherited `--text`); a class rule loses to `.view h2` / `.brief-prose
h2` unless it carries two classes; `a.trends-card { display: block }` beat the
card's own flex; the CSS orphan check must account for classes built by
concatenation (`cls-{tier}`, `sel-{i}`, `upd--{rtype}`, `runs-row__kind--{kind}`)
before deleting anything.
