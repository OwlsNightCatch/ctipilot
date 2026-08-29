---
name: ui-writing-style
description: "Never an em dash anywhere the site renders text — chrome AND finding prose; build.py normalises at render and the self-check FAILs"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 02f7ff62-41ad-43c6-a29a-dc723bbb5feb
  modified: 2026-08-29T13:02:28.887Z
---

**Never an em dash (`—`) anywhere a reader sees it.** Operator directive
2026-08-29 widened the 2026-07-06 chrome-only rule to cover EVERYTHING the site
renders: chrome strings, entry prose, headlines, summaries, run records, the
registry, state files, the pinned ATT&CK dataset, docs and prompt pages.

**How it is enforced (v4.5, `site/build.py`):**

- `dedash()` / `dedash_markdown()` rewrite prose at the presentation boundary.
  A PAIRED dash inside one sentence becomes a parenthetical; a SINGLE dash
  becomes `;` when what follows is an independent clause (carries a finite
  verb, does not open with a conjunction/relative pronoun/participle) and `,`
  otherwise; a `**Bold term** —` definition becomes `**Bold term**:`. It is
  idempotent, never drops a word, and never changes the newline count
  (regression tests in `site/test_build.py`).
- `normalise_entry_text()` runs over entries / runs / registry / state /
  ATT&CK after validation in `main()`. `_DEDASH_SKIP_KEYS` protects
  identifiers (`url`, `id`, `at`, …) — as SCALARS; the containers are still
  walked so `sources[].publisher` and `cves[].affected` normalise.
- `render_inline` / `render_markdown` dedash at the parse boundary, which
  covers docs and prompt pages rendered under `/about/`.
- The build self-check FAILs on any em dash in a rendered HTML/XML text node
  or in a CSS/JS string literal (comments stripped, including trailing `//`).

**What deliberately keeps its em dash:** `<pre>` / `<code>` — verbatim
specimens. `## <Type> — <at>` is the NORMATIVE changelog-section heading
(`content_model.UPDATE_HEADING_RE`); dedash skips those heading lines and
code spans entirely, or the site would document a wrong format and orphan
every update section. The content store on disk and each entry's raw
`index.md` twin are never rewritten.

**Empty-value cells** use `·` (the `NO_VALUE` constant), not a dash of any kind.

**Why:** the em dash reads as AI filler and clashes with the design's terse
mono-separator style; the operator wants it gone from the product, not just
from the chrome. Rewriting 1200+ stored entries is impossible under the
one-entry-per-finding lifecycle, so the fix is at render, with
`prompts/cti-run.md` § Style rules keeping new entries clean at the source.

**How to apply:** never type one into `site/build.py`, `config/branding.yaml`,
the CSS or the JS — the build will fail. Related: [[design-system]],
[[site-landing-live-brief]], [[entry-lifecycle-v4]].
