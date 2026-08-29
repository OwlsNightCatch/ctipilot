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

## Document contract (2026-08-29 design pass)

Rendering invariants a `site/build.py` change must not regress. All three are
mechanically checkable across the emitted store, so re-check them after any
renderer edit:

- **One heading outline per page.** Exactly one `<h1>` (redirect stubs excepted
  — `/cves/*`, `/topics/*`, folded entries and `/live/` are meta-refresh pages
  with none), no skipped levels. Embedded markdown never keeps its own level:
  `render_markdown(..., heading_base=N)` pins a document's own top heading to
  N whatever it was authored at (records open at `#` OR `##`, so a fixed
  `heading_offset` skips a level in half of them). Run notes pass
  `head_level`; entry bodies pin to h2. Day-brief section headers are `<h2
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

Traps: `var(--muted)` is NOT a token (five rules once asked for it and
silently inherited `--text`); a class rule loses to `.view h2` / `.brief-prose
h2` unless it carries two classes; `a.trends-card { display: block }` beat the
card's own flex; the CSS orphan check must account for classes built by
concatenation (`cls-{tier}`, `sel-{i}`, `upd--{rtype}`, `runs-row__kind--{kind}`)
before deleting anything.
