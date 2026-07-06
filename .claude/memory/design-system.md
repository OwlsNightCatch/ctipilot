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
