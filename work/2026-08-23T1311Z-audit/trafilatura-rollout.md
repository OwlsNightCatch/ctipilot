# Trafilatura capture rollout — test evidence (2026-08-24, operator directive)

Operator directive (2026-08-24, mid-audit): capture websites with trafilatura
(github.com/adbar/trafilatura); keep the metered jina reader strictly last-resort
(keys refilled sparsely); avoid WebFetch's summarising fetch for article bodies;
make requests as human as possible.

## What shipped

- `tools/fetch_source.py extract <URL>` — the new preferred article-capture command.
  Ladder: (1) the bridge's direct GET with the full human Chrome header set
  (UA + Sec-CH-UA client hints + Sec-Fetch-*, already mutually consistent) →
  trafilatura extraction to clean markdown with metadata; (2) trafilatura's own
  downloader as an alternate direct transport (auto-skipped in the cloud container,
  where its urllib3 stack cannot use the mandatory egress proxy); (3) jina, last.
- `.claude/hooks/setup-deps.sh` (SessionStart, async) — idempotent pip install of
  trafilatura in each fresh container; fetch_source.py degrades gracefully without it.
- Config: trafilatura extraction runs `output_format=markdown`, `with_metadata=True`,
  `include_links/tables=True`, `favor_recall=True`; its downloader (where usable)
  carries the bridge's BROWSER_UA.

## Compatibility sweep — 20 representative hosts (2026-08-24)

| Host | Result | Notes |
|---|---|---|
| securityweek.com | trafilatura-direct, 4.1 KB | article + full metadata (author, date) |
| thehackernews.com | trafilatura-direct, 3.0 KB | clean |
| bleepingcomputer.com | trafilatura-direct, 13.3 KB | Cloudflare front passes the human header set |
| therecord.media | trafilatura-direct, 3.3 KB | clean |
| dragos.com/blog/ | trafilatura-direct, 3.5 KB | dated listing extracts |
| claroty.com/team82 (article) | trafilatura-direct, 28.6 KB | full research body |
| research.checkpoint.com | trafilatura-direct, 34.9 KB | full research body |
| welivesecurity.com | trafilatura-direct, 4.4 KB | clean |
| securelist.com | trafilatura-direct, 1.6 KB | listing thin but readable |
| unit42.paloaltonetworks.com | trafilatura-direct, 3.0 KB | clean |
| msrc.microsoft.com/blog/ | trafilatura-direct, 1.8 KB | clean |
| access.redhat.com (CVE page) | trafilatura-direct, 3.6 KB | product-state table survives |
| ncsc.admin.ch | trafilatura-direct, 0.9 KB | portal page, thin by nature |
| cert.ssi.gouv.fr | trafilatura-direct, 2.3 KB | clean |
| osv.dev (GHSA page) | trafilatura-direct, 2.8 KB | clean |
| wallix.com/support/alerts/ | trafilatura-direct, 30.4 KB | full advisory list |
| huntress.com/blog | trafilatura-direct, 1.5 KB | clean |
| sentinelone.com/labs/ | trafilatura-direct, 2.1 KB | clean |
| **cisa.gov (advisory page)** | **jina-only — FAILED (pool exhausted)** | Akamai 403s every direct transport; keep `cisa csaf`/`cisa feed` structured recipes first, reader only for dynamic paths |
| **heise.de** | **jina-only — FAILED (pool exhausted)** | consent-wall; already `fetch_method: jina`-pinned |

**Verdict: 18/20 hosts need no reader at all.** The two failures are the two
hosts already known to require jina, and they failed in this sweep only because
the key pool is currently credit-exhausted — which is exactly the condition the
directive is designed to survive: with trafilatura in place, a dead reader pool
now costs only cisa.gov dynamic paths (mitigated by the CSAF mirror recipes) and
heise article bodies.

## Environment caveats (documented in code)

- trafilatura's own downloader ignores `HTTPS_PROXY`; in the cloud container all
  egress is proxy-forced, so that rung self-disables there (checked at runtime).
  On an unproxied machine it works as a second direct transport.
- `extract` returns `direct-raw` when a reachable page has no extractable main
  content (JS shell / bare index) — the raw body is still returned rather than
  spending reader credit.
