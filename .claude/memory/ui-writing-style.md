---
name: ui-writing-style
description: "Never use em dashes in the site's UI chrome; entry/brief content may use them sparingly"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 02f7ff62-41ad-43c6-a29a-dc723bbb5feb
---

**Never use em dashes (`—`) in UI components / descriptions on the web page.** Titles, subtitles, section headers, button labels, placeholders, tooltips (`title=`), aria-labels, empty-state text, footer, hero/AI-bar copy, feed titles, and any other chrome string rendered by `site/build.py` must use `·` (the site's separator glyph), `:`, `,`, or a period instead. Empty-value cell glyphs use `–` (en dash), not `—`.

**Why:** the operator's explicit standing instruction (2026-07-06). The em dash reads as AI-generated filler and clashes with the design's terse, mono-separator style.

**How to apply:** when adding or editing any user-facing string in `site/build.py`, `config/branding.yaml`, or the JS, do not introduce `—`. Code comments and docstrings are exempt (dev-facing). Entry/brief CONTENT (the agent-written markdown in `entries/`, headlines, summaries) may use em dashes sparingly — the agent has writing freedom there; do not strip them from content. Related: [[design-system]], [[changelog-hygiene]].
