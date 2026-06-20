# Source-accessibility audit protocol — ctipilot.ch (2026-06-20)

You are auditing CTI sources for an autonomous threat-intel newsletter serving a Swiss
federal SOC. Your job: for **each** source in your assigned batch, determine whether an
LLM agent can actually fetch **current, relevant, drillable** content from it today, and
recommend correct metadata. You do **not** edit `sources/sources.json` or any other repo
file — you only fetch, assess, and **write one results JSON file** plus return a short summary.

Today's date is **2026-06-20**. "Recent" means within the last ~30 days.

## Tools you use

- `WebFetch` — the routine's default fetcher. Some publishers 403 it or return only a
  JS navigation shell (SPA). When you call WebFetch, ALWAYS use this prompt template so
  URLs survive:

  > "List this page's main content. Return: (1) page title; (2) whether it shows a list of
  > dated articles/advisories or only navigation/marketing; (3) the 3 most recent item
  > titles WITH their publication dates AND their full absolute URLs (Outbound links —
  > include every href verbatim, do not summarise them away); (4) one sentence on what
  > kind of security content this source publishes."

- `python3 tools/fetch_source.py <subcommand>` — the operator bridge (desktop-Chrome UA,
  stdlib, read-only, no JS). Subcommands you will use:
  - `url <URL>` — plain GET of any HTTPS page with a browser UA (defeats most UA-based 403s).
  - `feed <FEED_URL> [N]` — parse any RSS/Atom feed → JSON (title/link/published/summary).
  - `wayback <URL> [ts] [minsize]` — closest Wayback snapshot (fallback for Cloudflare-blocked hosts).
  - `cisa-kev` | `cisa page <URL>` | `ncsc-csh recent [N]` | `ncsc-csh post <ID>` |
    `enisa-euvd recent [KIND]` | `bsi-rss` | `bsi-csaf <ID>` | `ncsc-nl recent [N]` |
    `ncsc-nl csaf <ID>` | `cert-eu recent [N]` | `cert-fr avis-recent [N]` |
    `cert-fr actu-recent [N]` | `ico-uk enforcement [N]` | `sec-edgar 8k [start] [end] [item]`
  - Run `python3 tools/fetch_source.py --help` if unsure of a subcommand's args.
- `WebSearch` — only to confirm a publisher is still actively publishing when every fetch
  path fails (e.g. `site:example.com 2026`), or to find a feed URL.

## Per-source procedure (do this for every source in your batch)

1. **Primary fetch** using the source's documented `fetch_method`:
   - `webfetch` → WebFetch the `url` (template above).
   - `rss` → `feed <rss_url> 5`. The rss URL is in the source's `notes` or is the `url`
     itself; if not, derive it (try `/feed/`, `/rss/`, `/feed.xml`, `/rss.xml`, `/atom.xml`).
   - `bridge` → `url <url>` (or the documented bridge subcommand named in `notes`).
   - `api` → the documented subcommand (`cisa-kev`, `ncsc-csh recent`, `ncsc-csh post`, etc.).
   - `blocked` → still RETEST: try `url <url>`, then `wayback <url>`. A blocked source may have recovered.

2. **Drill-down test (REQUIRED).** A working listing/feed is NOT enough — confirm you can
   reach an actual **article/advisory detail page** with title + date + substantive body.
   Take the most recent real item URL from step 1 and fetch it (WebFetch template, or
   bridge `url <article_url>`). Record the exact URL you drilled into and whether the body
   was substantive (a few real paragraphs / advisory fields) vs. empty/navigation/paywall/SPA-shell.

3. **Escalate only if the primary method failed or returned no drillable content.** Try in
   this order, recording each attempt's outcome (HTTP code / "empty SPA" / "navigation only"
   / "paywall" / bytes returned):
   a. `WebFetch` the `url` directly (if not already tried).
   b. `python3 tools/fetch_source.py url <url>` (bridge direct fetch of the whole page).
   c. A feed: derive a feed URL (see 1) and `feed <feedurl> 5`.
   d. `python3 tools/fetch_source.py wayback <url>`.
   e. `WebSearch` `site:<host> 2026` to confirm the publisher still publishes at all.

4. **Assess** and record:
   - `live`: `true`/`false` — does ANY method return current (≤~30d) content?
   - `drilldown`: `true`/`false` — can you reach a real article/advisory detail page (not just a listing/feed-summary)?
   - `working_recipe`: the EXACT command or method an LLM agent should use, e.g.
     `"feed https://example.com/feed/ N"`, `"webfetch (listing) then webfetch per-article"`,
     `"bridge: python3 tools/fetch_source.py url <URL>"`, `"api: ncsc-csh recent"`,
     `"BLOCKED — no method works; wayback empty; websearch only"`.
   - `dont_waste`: what an agent should NOT try (e.g. "WebFetch 403s — skip it",
     "homepage is SPA shell — go straight to the feed", "RSS lags months — use HTML").
   - `observed_recent`: the single most-recent dated item you actually saw —
     `{title, date, url}` (proof of liveness; null if nothing found).
   - `relevance`: 1 sentence — is the content relevant CTI (vulns/TTPs/campaigns/advisories/
     breaches/OT/ransomware/regulatory) for a Swiss-federal-SOC Tier-2/3 audience? Note the
     actual topics you saw.
   - `category_assessment`: are the source's current `category` values correct for what it
     actually publishes? Recommend a corrected list (values ONLY from the controlled
     vocabulary in `work/source-audit-2026-06-20/vocab.json`).
   - `reliability_assessment`: is the current tier right? (HIGH = authoritative/original
     sourcing/primary; MEDIUM = aggregates or occasional errors; LOW = discovery-only).
   - `recommended_status`: `active` | `candidate` | `demoted`.
     - Promote a `candidate` → `active` only if it is live + drillable + clearly relevant.
     - Keep `candidate` if live but unproven / niche / needs more runs.
     - Recommend `demoted` ONLY when NO method (webfetch, bridge direct, feed, wayback)
       yields drillable relevant content AND you've documented why. **A pure UA-403 where
       the bridge then works is NOT a demotion** — it stays active with the bridge recipe.
       A dead host / 404 / removed-blog / SPA-with-no-API-and-no-feed-and-no-wayback IS a demotion.
   - `recommended_fetch_method`: the method that actually works (`webfetch`/`rss`/`bridge`/`api`/`blocked`).

5. **Write results.** Append a record per source. Be terse but concrete. NEVER fabricate a
   date, title, or URL — if you didn't fetch it, say `null` / `"not verified"`.

## Output (TWO things)

**(A) Write a JSON file** to `work/source-audit-2026-06-20/results/batch-<NN>.json` (use the
EXACT batch number from your input filename) — a JSON array, one object per source:

```json
[
  {
    "id": "source-id",
    "live": true,
    "drilldown": true,
    "working_recipe": "feed https://example.com/feed/ 5  (then webfetch per-article URL for body)",
    "dont_waste": "WebFetch on the homepage returns a SPA shell — skip it",
    "observed_recent": {"title": "...", "date": "2026-06-18", "url": "https://..."},
    "relevance": "Vendor PSIRT advisories with CVE IDs and affected versions — directly relevant.",
    "current_category": ["research"],
    "recommended_category": ["vulns", "vendor-psirt"],
    "reliability_current": "HIGH",
    "recommended_reliability": "HIGH",
    "status_current": "candidate",
    "recommended_status": "active",
    "recommended_fetch_method": "rss",
    "attempts": ["webfetch url -> 403", "bridge url -> 200, 18KB, dated articles", "drill article -> 200 substantive"],
    "notes_for_operator": "One-line dated audit note to append to the source's notes, e.g. '2026-06-20 audit: <verdict + recipe>.'"
  }
]
```

**(B) Return a short summary** in your final message: one line per source —
`id: live=Y/N drill=Y/N status <cur>→<rec> rel <cur>→<rec> method <cur>→<rec> — <recipe>`.
Then a 2-3 line overall note (which sources are dead/blocked, which need re-categorising).

## Hard rules
- Do NOT edit `sources/sources.json` or any file except your `results/batch-<NN>.json`.
- Do NOT fetch NCSC CSH posts marked `TLP:AMBER`/`TLP:RED` (TLP:CLEAR only).
- Be efficient: ~2 calls for a healthy source (listing + drill), up to ~6 for a failing one.
  If a source clearly works on the first method + drill, stop and move on.
- If `tools/fetch_source.py` errors on a subcommand, fall back to `url <URL>`.
- Stay within your batch. Finish every source in the batch — partial is worse than terse.

