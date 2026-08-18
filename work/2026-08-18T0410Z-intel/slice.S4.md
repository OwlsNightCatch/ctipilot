# Source slice — S4 — run 2026-08-18T0410Z-intel

Tier `essential` = MANDATORY attempt this run. Tier `standard`/`candidate` = rotation (oldest last_successful_fetch first).
ROTATION PRIORITY (missed on 2+ recent runs): cisa-advisories, cisa-directives, siemens-productcert-csaf.

## venarix — VenariX
- tier: **standard** · status: candidate · fetch_method: `bridge` · reliability: B · language: en
- url: https://venarix.com/blog
- recipe notes: Added 2026-08-04 as the ONE candidate source of this run. Threat-intelligence research blog; surfaced as the primary for the ExfilSquad access-path analysis cited by the 2026-08-04 PNLD entry — first-hand review of leak samples from 11 of 15 claimed victims, identification of the Microsoft Power Pages / Dataverse Anonymous-Users misconfiguration class, and independent live reproduction of unauthenticated Dataverse record retrieval from a public municipal portal. No tracked source covered that finding. FETCH → `python3 tools/fetch_source.py url <article-url>` returned HTTP 200 with the full body (verified this run). Astro-built site; per-post dates render on the article page. Candidate — promote to active after 3 contributing runs. | 2026-08-15: listing is a client-filtered single-page app with no per-post dates in the served HTML; needs an RSS or API recipe before it can be rotated reliably. | 2026-08-17: unreachable again — direct transport refused and the jina reader pool returned HTTP 402 on every rotating key, so the documented ladder had no last rung. Transport blocking plus an exhausted reader quota; NOT demoted.

## bleepingcomputer — BleepingComputer
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en
- url: https://www.bleepingcomputer.com/news/security/
- recipe notes: 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://www.bleepingcomputer.com/news/security/ (listing, with outbound-links template) then webfetch per-article URL for body. AVOID: Do NOT guess article slugs from headlines — start from the listing and follow real links. RSS at /feed/ has been observed 403'd; the /tag/data-breach/ archive lags days — use the security index.. | 2026-07-05 admiralty audit: B (MEDIUM->B) — established security journalism with original scoops + editorial process; keep active. Start from the HTML listing (never guess slugs); RSS /feed/ has 403'd. | 2026-07-14 intel run: contributed corroboration for CrashStealer (macOS infostealer).

## cnil-fr — CNIL France
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: A · language: en,fr
- url: https://www.cnil.fr/en/news
- recipe notes: French data-protection authority. /en (homepage) carries general announcements and is rarely useful for breach/enforcement coverage; /en/news lists actual press releases. For enforcement actions specifically, also check /en/sanctions-and-corrective-measures and the French-language /sanctions-prononcees-par-la-cnil (richer than the English mirror — translate findings to English in the brief). | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://www.cnil.fr/en/news (then webfetch per-article URL for body). AVOID: /en homepage carries general announcements — use /en/news for press releases. English mirror is thinner than the French sanctions page.. | 2026-07-05 admiralty audit: A — French DPA is the primary/definitive authority for its own sanctions and breach-enforcement decisions in-jurisdiction; live and drillable, no change (active).

## cyberinsider — CyberInsider
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: C · language: en
- url: https://cyberinsider.com
- recipe notes: Breach-focused journalism; server-rendered, no observed 403. Discovered 2026-05-27 contributing corroborating primaries to the Charter Communications and 7-Eleven ShinyHunters breach confirmations. Candidate — promote to active after 3 runs with content contribution. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://cyberinsider.com (listing) then webfetch per-article URL. AVOID: No issues — server-rendered, no observed 403, substantive detail pages. No bridge needed.. | 2026-07-05 admiralty audit: C — live server-rendered breach-news site, but mostly re-reporting/aggregation with only occasional original breach corroboration; stays active, corroborate before acting.

## databreaches-net — DataBreaches.net
- tier: **standard** · status: active · fetch_method: `rss` · reliability: C · language: en
- url: https://databreaches.net/
- recipe notes: 2026-06-20 v2.64 fetch-waste review: KEPT — the /feed/ RSS carries ~1.4 KB article bodies per item (readable without drilling). Confirmed full-content feed. | 2026-07-05 admiralty audit: C (was HIGH) — discovery/aggregation layer with some original reporting; trace each breach to victim statement/regulator filing before citing. Live via /feed/, no change (active). | 2026-08-13: RECIPE: individual article URLs 403 on raw WebFetch; use `fetch_source.py feed` for the listing and `fetch_source.py url` for article bodies (auto-falls back to the reader, which succeeded on every article this run).

## ico-uk — UK ICO breach notifications
- tier: **standard** · status: active · fetch_method: `bridge` · reliability: A · language: en
- url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/
- recipe notes: 2026-08-15: health-probe failure this run is an artifact of the exhausted reader key pool, not a recipe defect — fetch_method is pinned to the reader. Not demoted; re-probe once the pool is topped up. | 2026-08-16: source_health flagged needs-demote; a serial re-probe this run returned 50 KB through the generic `url` bridge. Same parallel-contention artifact as ncsc-ch-incidents. NOT demoted. | 2026-08-16 weekly (RECIPE FIX): fetch_method jina -> bridge. The record was pinned to the reader, which is why source_health kept flagging it needs-demote while the reader pool sat at HTTP 402 — the generic `url` bridge reaches this host directly and returned 50 KB for /action-weve-taken/enforcement/ and 40 KB for the media-centre listing on a serial probe this run. Pinning to the reader was the defect; this is a fix, not a workaround. Cite the per-action /action-weve-taken/enforcement/<year>/<month>/<slug> or media-centre URL.

## ransom-isac — Ransom-ISAC
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: C · language: en
- url: https://ransom-isac.org/blog/
- recipe notes: 2026-07-05 admiralty audit: C (MEDIUM->C) — original extortion case studies but newer/niche with self-noted unverified attributions; corroborate specifics. Keep candidate. Note: canonical domain is ransom-isac.org (not .com). | 2026-07-28: status candidate -> active. State digest reported it in sources.promotion_due with 3 contributing runs, meeting the three-contributing-run promotion bar. | 2026-08-15: the /blog/ path is a client-rendered shell with no server-side post list; the site's own /feed.xml works cleanly and is the recipe to use.

## ransomware-live — Ransomware.live
- tier: **standard** · status: active · fetch_method: `api` · reliability: C · language: en
- url: https://www.ransomware.live/
- recipe notes: Public extortion-leak observatory — scrapes ransomware groups' shaming sites and exposes new claims (added 2026-05-08). 2026-05-08 audit: WebFetch returned 5 fresh victim entries (5h-old). For automated monitoring, use the JSON API at https://api.ransomware.live/v2/groups (one entry per group with recent victims). Discovery — always corroborate against victim statement / regulator filing before citing as confirmed breach. Candidate — promote to active after 3 runs. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → api: python3 tools/fetch_source.py url https://api.ransomware.live/v2/recentvictims  (new victim claims, one record each with victim/group/activity/country/claim_url); /v2/groups for per-group view. AVOID: Do NOT rely on the homepage HTML for automation — use the JSON API. Treat as discovery: every claim is an unverified extortion-site post; corroborate before citing as confirmed breach.. | 2026-07-05 admiralty audit: C — community leak-site tracker (Mousqueton); accurate mirror of extortion posts but claims unverified, corroborate before citing as confirmed breach. Live, active retained.

## sec-disclosures-edgar — SEC EDGAR (8-K cyber filings)
- tier: **standard** · status: active · fetch_method: `api` · reliability: A · language: en
- url: https://efts.sec.gov/LATEST/search-index?q=%22Item+1.05%22&forms=8-K
- recipe notes: US public-company breach disclosures via Item 1.05; primary source. Use the EDGAR full-text search API at https://efts.sec.gov/LATEST/search-index?q=...&forms=8-K with date range parameters (&dateRange=custom&startdt=YYYY-MM-DD&enddt=YYYY-MM-DD). Best query strings: q=%22Item+1.05%22 (most precise — only material cyber incidents) or q=%22cybersecurity+incident%22 (broader). The API returns metadata only (no doc_text); drill into each match's per-company filing index at https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<CIK>&type=8-K to read the actual filing. Cite the per-filing URL (e.g. /Archives/edgar/data/<CIK>/<accession>/...). | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → api: `python3 tools/fetch_source.py sec-edgar 8k <startdt> <enddt> 1.05` (returns Item 1.05 hits w/ filing_url) then bridge `url <filing_index>` to find the .htm doc, then bridge `url <doc.htm>` to read the Item 1.05 body. AVOID: The documented efts.sec.gov ...search-index API URL returns metadata only (no doc text) — don't expect the body there. Use the sec-edgar subcommand for discovery, then drill the per-filing .htm. WebFetch on efts JSON is unnecessary.. | 2026-07-05 admiralty audit: A (was HIGH) — SEC's official EDGAR system; Item 1.05 8-Ks are first-party regulatory breach disclosures by the companies, i.e. primary-authority ground truth. Justified A: government regulator + legally-accountable first-party filings. Status stays active.

## troyhunt — Troy Hunt — Have I Been Pwned
- tier: **standard** · status: active · fetch_method: `rss` · reliability: B · language: en
- url: https://www.troyhunt.com/
- rss_url: https://feeds.feedburner.com/TroyHunt
- recipe notes: Troy Hunt's blog — HIBP breach-disclosure analysis, identity / credential-stuffing research. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → feed https://www.troyhunt.com/rss/ 5 (or https://feeds.feedburner.com/TroyHunt) for dates, then webfetch the post URL for body. AVOID: Homepage WebFetch lists post titles but does NOT surface dates — use the RSS feed for dates. Many posts are 'Weekly Update' video roundups (lower IOC/TTP density).. | 2026-07-05 admiralty audit: B — original first-hand breach research (HIBP), high reputation; weekly video roundups are low IOC/TTP density but that does not lower the source-reliability letter. No status change.

## zaufana-trzecia-strona — Zaufana Trzecia Strona
- tier: **standard** · status: candidate · fetch_method: `webfetch` · reliability: B · language: pl
- url: https://zaufanatrzeciastrona.pl/
- recipe notes: 2026-08-13: added as candidate after breaking the MyDr electronic-health-record intrusion — original first-hand investigation by Adam Haertle, including direct contact with the claimants, independent verification of a subset of claimed records, and explicit statements of what the outlet could and could not verify. Polish-language original security journalism with unusually disciplined claim/fact separation; a primary rather than an aggregator for Polish incidents. Article bodies fetched cleanly via `fetch_source.py url` this run. Promote after 3 contributing runs.
