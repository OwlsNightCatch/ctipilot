# Reader analytics — what we measure, what we don't

This site uses [Umami Cloud](https://umami.is) for aggregate visitor counts. Umami is a privacy-by-design alternative to mainstream analytics:

- No cookies. No fingerprinting. No personal data persisted.
- Aggregates only: page URL, referrer host, country (IP discarded after lookup), and a daily-rotated hash for unique-visitor counting.
- Search-string parameters are excluded from collection.
- The site's strict CSP allows only `'self'`, `https://cloud.umami.is` (the script), and `https://api-gateway.umami.dev` (the beacon endpoint). No other third-party origin can run code or receive data.

Block at the network layer if you don't want to be counted: `cloud.umami.is` and `api-gateway.umami.dev` in your browser, ad-blocker, or DNS resolver. The site keeps working without them.

## Per-page coverage

Every emitted HTML page on the site loads the Umami snippet exactly once: the home page, every brief page, every per-item page, every CVE / source / topic page, every tag and region index, the operations dashboard, the about pages, and the 404 fallback. The build's self-check verifies the snippet is present on every page.

When you click through from one page to another, the navigation registers as a normal Umami pageview. The clean URL layout means each route is a distinct pageview rather than a hash-fragment that some readers compress to a single home-page hit.

## RSS feeds — deliberate non-tracking

RSS feeds are pure XML; they cannot run JavaScript, and well-behaved RSS readers strip any active content. We accept that and do **not** try to track feed opens or link clicks via tagged URLs:

- Feed `<link>` and `<guid>` URLs are plain canonical URLs. **No UTM parameters anywhere.** No query strings, no per-source variants. The build's self-check greps for `utm_` across the entire output and fails if anything appears.
- Feed click-through registers as a normal Umami pageview on the destination page (the user's RSS reader is the referrer).
- The "RSS — daily / weekly / per-item" links visible on the site fire `umami.track('feed-click', { feed: 'daily' | 'weekly' | 'items' })` via the standard Umami event helper before the user leaves the site. That's the one place we measure RSS interest, and it's measured *before* the user leaves. We do not measure feed opens themselves.

If a future operator wants feed-open metrics, they can add a server-side beacon (Cloudflare Worker, etc.). The current prompt does not authorize one, and the source list of allowed beacon endpoints in the CSP would need to be extended in the same change.

## What never leaves the site

- IP addresses (Umami discards after country lookup).
- Browser version, OS version, hardware fingerprinting.
- Referer header data beyond the host.
- Any cookie, ever.
- Any LLM editorial signal: visitor data does not feed back into the agent's source-selection or topic-prioritisation logic. The brief is editorially neutral with respect to readership; what is read is not reflected in what is written.

## Telemetry the agent emits

Distinct from the site analytics: the agent persists `state/run_log.json` per run, listing sub-agent allocation, fetch failures, deep-dive picks, etc. That file is committed to the public repo and rendered at [`/ops/`](../site/_site/ops/). It contains no visitor data — only what the agent itself did during the run.
