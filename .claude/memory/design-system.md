---
name: design-system
description: "The site's visual design system, its Claude Design source project, and the full brandable surface for a rebrand"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 02f7ff62-41ad-43c6-a29a-dc723bbb5feb
---

The published site's visual language is the **"CTI Pilot Design Modernization"** Claude Design project (read via the `DesignSync` MCP / `/design-sync`): project id `1ca3b2f3-7d01-40ca-8d48-781bbf3c08b9`, comps `CTI Pilot.dc.html` (authoritative site design) + `CTI Pilot Reading Experience.dc.html` (a canvas exploration, not a site view), plus a token design-system under `_ds/…/tokens/` (colors/typography/spacing/effects/base/accessibility). That system was itself lifted from this repo's `site/assets/css/styles.css` + `config/branding.yaml`, so the tokens already matched — the modernization was layout/component, not a re-skin.

**Design DNA:** dark-first analyst console (`--bg #0e1116`), one crimson accent (`--accent #e85d75` dark / `#b62b46` light), sans/mono split (mono = every machine fact), border-not-shadow surfaces, small radii, short linear motion. No IOCs, no emoji.

**Where the design lives now:** `site/assets/css/styles.css` (component classes match the comp — `.seg .aibar .actnow .tl-* .finding .f-h .sect .verif .arc .bcard .dpop .fchip .prov`), `site/build.py` (`base_template` shell + the reading-page renderers + `render_finding`/`render_timeline_item`/`render_actnow` helpers), and JS `theme.js` / `app.js` / `brief.js` (see the DOM contract: `data-theme/-font/-density` on `<html>`, `cti:filterchange` event links app.js chip state → brief.js timeline).

**Brandable surface (all in [[customization-framework]] `config/branding.yaml`, current values = defaults, empty = inherit):** colors (dark+light), fonts, radii, topbar height, logos/favicon, site name/wordmark/taglines/lede/footer/copyright, **plus new keys**: `site.nav_live/nav_daily/nav_weekly`, `site.hero_eyebrow/hero_title/hero_subtitle`, `site.ai_bar_html/ai_bar_link_label`. Overriding `theme.dark.accent`/`info` with a hex **auto-derives** `--accent-rgb`/`--info-rgb` (branding_config `_rgb_decls`), so a rebrand's accent propagates to every translucent rgba() fill from one value. Fonts stay system-stack (Inter/JetBrains Mono named mid-stack) — no external webfont ships (keeps CSP + instant load).

## v3 UX layer (2026-07-09 session — "modern TI platform" overhaul)

Appended as the `v3 UX redesign` block at the end of `styles.css`; all colors flow from theme tokens, so the branding override layer re-skins every new component (verified by building with a test accent/bg override — `--accent-rgb` propagated).

- **Knowledge-base subnav** — second topbar row (desktop-only), `_subnav_html()` in build.py: Entities · CVEs · Sources · Trends · Operations, active state via `base_template(active_page=…)`. Mobile keeps these links in the drawer.
- **Home** — split hero (`.hero--split`): copy left, `.hero-status` platform panel right (live findings + crit/high mix, entities/CVEs/sources counts; `render_home_page(counts=, last_updated=)`); `.pivotband` tile row under the brief cards.
- **Live** — `.pulserow` window-mix chips (`data-window-crit/high/upd/total`, mirrored in brief.js render()); source rows dedup by publisher (render_source_line + briefbook `sources_min`).
- **Day/weekly** — `.secnav` section-jump chips inserted after the TL;DR (`_secnav_html`; `.sect` now carries `id=slugify(title)`).
- **Entry page** — `.entry-layout--rail` two-column ≥1100px (body class `entry-detail`, NOT `:has()`): sticky `.erail` pivot rail (CVEs w/ status+CVSS, entities, ATT&CK→attack.mitre.org, affected products, tags/regions/sectors). Rail present → inline "Entities & scope" block suppressed.
- **Entity pages** — story-timeline drops `delta_summary` when == title; "Peak priority" KPI tile (replaces duplicate Entries tile); `.pivot-panel` "Hunting pivots" (aggregated techniques ×N → MITRE, products, tags); embedded entries = 3 newest full cards + `.mini-card` grid for the rest; cited-sources in a collapsed `<details class="cite-details">` with real `.cite` row styling; "other" donut slice always neutral.
- **Ranked bars** — `.rankbar-list/.rankbar` (label + inline track + value) replaced unlabeled SVG bar rows on /sources/ most-cited, entity section-distribution, and CVE by-year (old bars were invisible at 1-vs-511 scale).
- **CVE index** — year filter chips (`data-filter-chip="cve-year"`; app.js facet prefix `cve-` → scope `cves`); coverage column = latest day + "+N more"; single-type donut suppressed (render_overview_charts skips donut when 1 type).
- **Trends** — tiles link to first cohort tag/region page (`a.trends-card`, keeps text ink not link-blue); deltas colored ▲ warn / ▼ ok.
- **Ops** — Last-run tile sub = intel/weekly mix (was duplicate fetch-failure count); cadence chart = runs-per-day series (was a solid `[1]*n` bar wall).
- **Typography** — display headlines now sans 700 (`--serif` token kept for forks). **NEVER re-enable `"dlig"`** in heading `font-feature-settings`: on Linux fallback fonts it renders stray slash/caret glyph artifacts (seen on Chromium headless, DejaVu/Liberation). Keep `"kern","liga"` only.
- Flags/badges: verification flags render neutral (`.badge`, lowercased) everywhere — red is reserved for priority/exploited.
