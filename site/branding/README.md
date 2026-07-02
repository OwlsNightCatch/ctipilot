# site/branding/ — downstream branding assets

This directory is **downstream-owned**: upstream ships only this README, so
a fork can fill it with corporate assets and never see a merge conflict.
Everything here (except `*.md`) is copied verbatim into the built site under
`/branding/` and included in the cache-bust fingerprint.

What goes here, and how it's wired up (see `docs/customization.md` for the
full fork/rebrand guide):

| File | Activated by | Effect |
|---|---|---|
| `logo.svg` / `logo.png` (any name) | `config/branding.yaml` → `logo.header_mark` | Replaces the built-in header mark next to the wordmark |
| any image | `logo.footer_mark` | Replaces the footer's square "CTI" mark |
| `favicon.svg` / `.png` / `.ico` | `logo.favicon` | Replaces the generated SVG favicon |
| `custom.css` | presence of the file | Loaded on every page **after** `styles.css` and the generated `branding.css` — free-form CSS: `@font-face` for corporate fonts, layout tweaks, hiding elements |
| `fonts/*.woff2` | `@font-face` rules in your `custom.css` | Self-hosted webfonts (the CSP allows same-origin fonts; no third-party font CDN will load) |

Rules:

- Referenced paths in `config/branding.yaml` are relative to this directory
  (`logo.svg`, not `site/branding/logo.svg`). The build fails loud if a
  referenced file is missing.
- Per-file size cap: 4 MB (same as vendored JS).
- Theme **tokens** (colors, font stacks, radii) belong in
  `config/branding.yaml` `theme:` — use `custom.css` only for what tokens
  can't express.
- Keep licenses for any fonts you drop here.
