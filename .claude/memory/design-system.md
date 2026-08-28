---
name: design-system
description: The site's visual language, its Claude Design source project, and the invariants any site/build.py or CSS change must respect
type: reference
---

# Design system — where it lives and what not to break

Source: the "CTI Pilot Design Modernization" Claude Design project (id `1ca3b2f3-7d01-40ca-8d48-781bbf3c08b9`, via DesignSync MCP). Live implementation: `site/assets/css/styles.css` (component classes `.seg .aibar .actnow .tl-* .finding .sect .verif .bcard .pulsepanel .erail .rankbar …`), `site/build.py` (`base_template` + renderers), JS `theme.js`/`app.js`/`brief.js` (DOM contract: `data-theme/-font/-density` on `<html>`; `cti:filterchange` links app.js chips → brief.js timeline).

**Design DNA:** dark-first analyst console (`--bg #0e1116`), one crimson accent, sans/mono split (mono = every machine fact), border-not-shadow, small radii, no emoji, no IOCs.

**Brandable surface** = `config/branding.yaml` only ([[customization-framework]]): colors/fonts/radii/logos/nav/hero/ai-bar copy; overriding an accent hex auto-derives `--accent-rgb` so translucent fills follow. Fonts stay system-stack — no external webfont (CSP + load).

Invariants learned the hard way:
- **Never re-enable `"dlig"`** in heading `font-feature-settings` — stray glyph artifacts on Linux fallback fonts. Keep `"kern","liga"`.
- Inline-token prose rules sharing a class with a badge need a `:not(.b)` guard (`.finding .cve` once inflated `.b.cve` badges).
- Trends statistical honesty: the running ISO week is partial and never compared; deltas = latest complete week vs prior.
- Verification flags render neutral — red is reserved for priority/exploited.
- Classification badges/scheme text are config-driven (`_load_classification_scheme()`); never re-hardcode doctrine. `_chrome_text()` sanitizes config strings for chrome (em dash → `·`, per [[ui-writing-style]]).
- Routes: `/live/` (rolling, ordered by activity; only non-internal `type: update` records re-float) and `/daily/` (completed days). `/weekly/` was removed 2026-08-27 with the weekly routine; entry pages carry timestamped `## <Type> — <at>` blocks + a revision-history panel.
