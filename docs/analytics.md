# Reader analytics — what we measure, what we don't

This site uses [Umami Cloud](https://umami.is) for aggregate visitor counts. The integration is config-driven: `analytics:` in [`config/branding.yaml`](../config/branding.yaml) carries the website id and the two Umami hosts, and `provider: "none"` turns analytics off entirely — no snippet on any page and no third-party origin left in the CSP (the build self-check then asserts zero analytics tags; see [docs/customization.md](customization.md)). Umami is a privacy-by-design alternative to mainstream analytics:

- No cookies. No fingerprinting. No personal data persisted.
- Aggregates only: page URL, referrer host, country (IP discarded after lookup), and a daily-rotated hash for unique-visitor counting.
- Search-string parameters are excluded from collection.
- The site's strict CSP allows only `'self'`, `https://cloud.umami.is` (the script), and `https://gateway.umami.is` (the beacon endpoint). No other third-party origin can run code or receive data.

Block at the network layer if you don't want to be counted: `cloud.umami.is` and `gateway.umami.is` in your browser, ad-blocker, or DNS resolver. The site keeps working without them.

> **Maintainer note — script host ≠ beacon host.** The loader (`cloud.umami.is/script.js`) and the beacon endpoint (`gateway.umami.is/api/send`) are two *different* hosts. The CSP `connect-src` must list the beacon host, or the browser silently blocks every pageview POST — the script loads, but nothing is recorded. The original integration hard-coded the now-retired `api-gateway.umami.dev` beacon host and shipped it from the first commit; the mismatch went undetected until analytics were noticed to be empty (2026-06-20). To prevent recurrence, `site/build.py` derives both the snippet and the CSP from single-source-of-truth constants (`UMAMI_SCRIPT_HOST` and `UMAMI_BEACON_HOST`, both read from `config/branding.yaml` `analytics.umami:`, plus the hardcoded `UMAMI_RETIRED_HOSTS` memory) and asserts at import time that the CSP permits the beacon host and re-lists no retired host — so a bad edit aborts `python3 site/build.py` (and the deploy) instead of silently killing analytics. `site/test_build.py` carries the same checks. Re-derive the beacon host from the live script's `/api/send` default before changing it in the config; do not trust memory for that value.

## Per-page coverage

Every emitted HTML page on the site loads the Umami snippet exactly once: the home page, the dynamic brief at `/live/`, every day and weekly page, every entry permalink, every entity / source page, every tag and region index, the operations dashboard, the about pages, and the 404 fallback. The build's self-check verifies the snippet is present on every page.

Each click registers as a normal Umami pageview because every URL is a real HTML page (the site is a static-site generator, not a SPA). The legacy `#/...` hash-routes from the previous SPA still work via the home page's redirect bootstrap, but the redirect resolves to a clean URL before Umami sees it — so the indexed-old-URL → clean-URL transition is a single normal pageview from Umami's perspective.

## RSS feeds — deliberate non-tracking

RSS feeds are pure XML; they cannot run JavaScript, and well-behaved RSS readers strip any active content. We accept that and do **not** try to track feed opens or link clicks via tagged URLs:

- Feed `<link>` and `<guid>` URLs are plain canonical URLs. **No UTM parameters anywhere.** No query strings, no per-source variants. The build's self-check greps for `utm_` across the entire output and fails if anything appears.
- Feed click-through registers as a normal Umami pageview on the destination page (the user's RSS reader is the referrer). That is the only visibility into feed readership; feed opens themselves are not measured, and no custom events are fired.

If a future operator wants feed-open metrics, they can add a server-side beacon (Cloudflare Worker, etc.). The current prompt does not authorize one, and the source list of allowed beacon endpoints in the CSP would need to be extended in the same change.

## What never leaves the site

- IP addresses (Umami discards after country lookup).
- Browser version, OS version, hardware fingerprinting.
- Referer header data beyond the host.
- Any cookie, ever.
- Any LLM editorial signal: visitor data does not feed back into the agent's source-selection or topic-prioritisation logic. The pipeline is editorially neutral with respect to readership; what is read is not reflected in what is written.

## Telemetry the agent emits

Distinct from the site analytics: every fire writes a run record (`runs/YYYY-MM-DD/<run-id>.md`) whose frontmatter carries the run's telemetry — models, sub-agent allocation, fetch failures, entry counts, verification iterations. Those files are committed to the public repo and rendered at the operations dashboard `/ops/`. They contain no visitor data — only what the agent itself did during the run.
