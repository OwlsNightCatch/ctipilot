# Source slice — S3 — run 2026-08-18T0410Z-intel

Tier `essential` = MANDATORY attempt this run. Tier `standard`/`candidate` = rotation (oldest last_successful_fetch first).
ROTATION PRIORITY (missed on 2+ recent runs): cisa-advisories, cisa-directives, siemens-productcert-csaf.

## paradigm-shift-research — Paradigm Shift Technology (ps.tc)
- tier: **standard** · status: candidate · fetch_method: `bridge` · reliability: B · language: en
- url: https://ps.tc/
- recipe notes: 2026-07-05 admiralty audit: B (HIGH->B) — original primary exploit research, but reliability caps at B (not a CERT/PSIRT). Keep candidate: niche offensive research, no drillable feed/listing (discovery needs a news pivot each time), single prior fetch. | 2026-07-27 intel run: source_health probes bridge-ok, but S3 reports the bridge returns only the SPA shell (page heading, no post listing, no dates). Host reachable, recipe does not reach the post grid — needs a discovered listing path or feed. Not a demotion (no transport failure, no 403). | 2026-08-16: still SPA-shell only on the direct transport; the reader escalation that would recover it was unavailable all run (all keys HTTP 402). Unchanged status — the gap is the reader pool, not this recipe.

## cryptotimes — CryptoTimes (cryptotimes.io)
- tier: **standard** · status: candidate · fetch_method: `webfetch` · reliability: C · language: en
- url: https://www.cryptotimes.io
- recipe notes: 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://www.cryptotimes.io/ (listing w/ dated articles + URLs) then webfetch the article URL for body. Bridge `url` also works (577KB, dated links). RSS /feed/ 403s.. AVOID: RSS at /feed/ returns HTTP 403 via bridge — skip the feed, use WebFetch on the homepage/article. Much of the homepage is general crypto market/price/policy news, NOT security — filter for exploit/hack/breach items (e.g. bridge exploits, North Korea hacks, scam analysis).. | 2026-07-05 admiralty audit: C — general crypto news aggregator, re-reporting; keep candidate (niche, security slice small, no documented multi-run contribution yet). | 2026-08-02: contributed the in-window anchor for the COLDCARD wallet-seed theft entry (Galaxy Research third-wave figures, relayed 2026-08-01T20:36Z).

## sans-ics — SANS ICS
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en
- url: https://www.sans.org/blog/?focus-area=industrial-control-systems-ics
- recipe notes: SANS ICS/OT focused blog series. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://www.sans.org/blog/?focus-area=industrial-control-systems-ics (renders the ICS-filtered listing) then webfetch the per-post https://www.sans.org/blog/<slug> URL for body. AVOID: Bridge 'url' on the focus-area page returns JS-rendered HTML with no clean article hrefs in static markup — use WebFetch (it renders the filtered listing). ICS-specific cadence is sparse: most posts on the general blog are non-ICS; filter hard.. | 2026-07-05 admiralty audit: B — SANS original expert content but training-heavy and non-primary; ICS cadence sparse, filter hard. Live, active retained.

## team-cymru — Team Cymru S2 Research
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en
- url: https://www.team-cymru.com/blog
- recipe notes: Team Cymru — flow / passive-DNS telemetry; strong on adversary infrastructure tracking and DPRK IT-worker investigations (added 2026-05-08). 2026-05-08 audit: WebFetch returned 5 article titles incl. 'Targeting the Defense Industrial Base' and DPRK IT-worker analysis; per-post dates not surfaced on listing — drill into individual posts. Candidate — promote to active after 3 runs. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://www.team-cymru.com/blog (listing — note: dates NOT shown on listing) then webfetch per-post URL for body + date. AVOID: Don't rely on the listing for dates — they only appear on the individual /post/ pages. Drill each post to get the date.. | 2026-07-05 admiralty audit: B — original telemetry-based infrastructure research; live. Keep active. Listing omits dates — drill /post/ pages for the date.

## zimperium-zlabs — Zimperium zLabs
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en
- url: https://zimperium.com/blog
- recipe notes: Primary mobile threat research (Android/iOS banking trojans, mobile EDR). Discovered via the Rokarolla Android-banker disclosure cited in briefs/2026-06-17.md (S3). Candidate — promote to active after 3 runs with content contribution. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://zimperium.com/blog (listing) then webfetch per-article URL. AVOID: No 403/SPA issues. Note: zLabs research posts often summarise and point to an external full report — the on-page body can be thin; pivot to the linked report for technical depth.. | 2026-07-05 admiralty audit: B (MEDIUM->B) — original mobile-threat research lab, first-hand telemetry; stays active, no change.

## ahnlab-asec — AhnLab ASEC
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en,ko
- url: https://asec.ahnlab.com/en/
- recipe notes: AhnLab Security Emergency-response Center — Korean CTI; particularly strong on DPRK Lazarus/Kimsuky and East-Asia targeted campaigns (added 2026-05-08). 2026-05-08 audit: WebFetch returned 5 dated reports Apr 13-22 2026. Candidate — promote to active after 3 runs. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://asec.ahnlab.com/en/ (listing) then webfetch the per-article https://asec.ahnlab.com/en/<id>/ URL for body; RSS alternative at https://asec.ahnlab.com/en/feed/. AVOID: Nothing to avoid — plain WebFetch works on both listing and article. No bridge needed.. | 2026-07-05 admiralty audit: B (HIGH->B) — AhnLab vendor research lab, first-hand telemetry; keep active, plain WebFetch works on listing and articles.

## citizen-lab — Citizen Lab
- tier: **standard** · status: active · fetch_method: `rss` · reliability: B · language: en
- url: https://citizenlab.ca/category/research/
- rss_url: https://citizenlab.ca/feed/
- recipe notes: 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://citizenlab.ca/category/research/ (listing) then webfetch the per-research URL for the body. AVOID: Nothing — WebFetch works fine on both listing and article. Cadence is slow (research org, not a news feed), so expect weeks between posts.. | 2026-07-05 admiralty audit: B (research-lab) — University of Toronto forensic research lab, original spyware research; live, WebFetch clean (slow cadence expected). Status stays active. | 2026-07-18 (jina-last-resort session): the /category/research/ listing began returning an empty archive (URL-path change suspected, flagged as a coverage gap in the 2026-07-18T0409Z run). RSS at https://citizenlab.ca/feed/ verified working via DIRECT feed fetch (fresh: item dated 2026-07-17) — fetch_method webfetch→rss, rss_url set. Recipe: feed https://citizenlab.ca/feed/ N, then url <article> for bodies.

## cloudflare-cf1 — Cloudflare Cloudforce One
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en
- url: https://blog.cloudflare.com/tag/cloudforce-one/
- recipe notes: Cloudflare's threat intelligence unit; large-scale internet telemetry. Cadence sparse. 2026-05-08 audit: WebFetch returned 5 dated CF1 articles Aug 2025 - Mar 2026. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://blog.cloudflare.com/tag/cloudforce-one/ (listing) then webfetch per-article blog.cloudflare.com/<slug>/ for body. AVOID: Cadence is sparse — do not flag 'no items' as broken; latest CF1-tagged posts may be days/weeks apart. | 2026-07-05 admiralty audit: B — vendor threat-research lab with first-hand internet telemetry, original research; live and drillable, no change (active).

## coinspect-research — Coinspect Security
- tier: **standard** · status: candidate · fetch_method: `bridge` · reliability: B · language: en
- url: https://www.coinspect.com/blog/
- recipe notes: Added 2026-08-09 by the weekly quality audit. Application-security research lab focused on wallet and cryptographic-implementation review; broke the CryptoJS 'Ill Bloom' investigation (CVE-2026-71851) that this audit recovered as a coverage miss — a twelve-year-old CSPRNG failure under active exploitation, reachable by any application that used WordArray.random() for a security-sensitive value, so its relevance is not confined to cryptocurrency. FETCH: python3 tools/fetch_source.py url https://www.coinspect.com/blog/<slug>/ returned the full article body directly, no reader fallback needed. Candidate — promote to active after 3 contributing runs.

## trellix — Trellix Blogs
- tier: **standard** · status: active · fetch_method: `bridge` · reliability: B · language: en
- url: https://www.trellix.com/blogs/
- recipe notes: platform)/<slug>/ hrefs and `url <full>` each for the body (no RSS feed). AVOID: WebFetch 403s the whole host — skip WebFetch entirely, go straight to the bridge. No RSS feed exists.. | 2026-07-05 admiralty audit: B — original vendor malware/detection research; live via bridge (WebFetch 403s the host). Keep active. | 2026-07-27 intel run: S3 reports the bridge fetch returns header/nav markup only and WebFetch's listing shows posts no newer than April-May 2026, suggesting a stale/cached index rather than the true latest list. Host reachable; recipe needs a deeper fetch or RSS discovery. Not a demotion.

## fox-it-blog — Fox-IT International Blog (NCC Group)
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en
- url: https://blog.fox-it.com/
- recipe notes: Fox-IT (NCC Group subsidiary) DFIR primary disclosures; distinct property from ncc-research (nccgroup.com/research-blog). Surfaced by S1/S3 as the primary for the Lazarus RemotePE memory-only RAT teardown (2026-05-22). Candidate — promote to active after 3 runs with content contribution. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://blog.fox-it.com/ (then webfetch per-post URL for body). AVOID: Nothing blocks it. Very low cadence (3 posts in ~18 months) — empty window is normal, not a failure.. | 2026-07-05 admiralty audit: B — original NCC/Fox-IT DFIR research; no status change (active). Very low cadence (3 posts in ~18 months) — empty window is expected, not a failure.

## horizon3-ai — Horizon3.ai (Attack Research / NodeZero)
- tier: **standard** · status: active · fetch_method: `webfetch` · reliability: B · language: en
- url: https://horizon3.ai/attack-research/
- recipe notes: Discovered 2026-06-13 via CVE-2026-48558 (SimpleHelp OIDC auth-bypass) — Horizon3 was the primary-discovery vendor with public PoC/IOC disclosure; consistent original research on RMM/enterprise-tooling auth bypasses. Fetched 200 this run. Candidate — promote to active after 3 runs with content contribution. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → webfetch https://horizon3.ai/attack-research/ (listing) then webfetch the /attack-research/disclosures/<slug>/ article for body. AVOID: Cadence is sparse (CVE disclosures, not daily) — gaps of weeks are normal, not a failure. | 2026-07-05 admiralty audit: B — original vuln discovery/disclosure with PoC/IOC; stays active. Sparse cadence (CVE-driven) is normal, not a failure.

## ibm-xforce — IBM X-Force
- tier: **standard** · status: active · fetch_method: `bridge` · reliability: B · language: en
- url: https://www.ibm.com/think/x-force
- recipe notes: IBM X-Force Threat Intelligence; annual X-Force Threat Index. URL CORRECTED 2026-05-08: legacy securityintelligence.com 301-redirects to www.ibm.com/think/security; the X-Force-specific sub-page is /think/x-force. The hub is a marketing portal rather than a dated blog — sub-agents reliably mis-report 'no items' because per-post dates are sparse in the listing. Drill into the X-Force Threat Intelligence Index (annual) and any podcast/webinar entries with explicit dates. Reliability MEDIUM until IBM publishes a clean dated archive again. | 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → bridge: python3 tools/fetch_source.py url https://www.ibm.com/think/x-force (listing) then bridge url <article /think/x-force/<slug>> for body. AVOID: WebFetch now 403s on BOTH the /think/x-force index AND article pages — skip WebFetch, go straight to the bridge. Listing has no inline per-post dates; read dateModified from the article HTML.. | 2026-07-05 admiralty audit: B — original vendor threat research; listing lacks inline dates so read dateModified from the article HTML via bridge. MEDIUM->B, stays active.

## intel471 — Intel 471 Blog
- tier: **standard** · status: active · fetch_method: `rss` · reliability: B · language: en
- url: https://www.intel471.com/blog
- rss_url: https://www.intel471.com/blog/feed
- recipe notes: 2026-06-20 full audit (v2.62): live=Y, drill=Y. FETCH → feed https://www.intel471.com/blog/feed 5  (then webfetch per-post /blog/<slug> for body) — or webfetch /blog directly. AVOID: Feed mixes original threat research (ransomware, threat-hunting) with CTI-program/marketing posts — filter for the research items.. | 2026-07-05 admiralty audit: B — original cybercrime/access-broker research; filter CTI-program marketing posts. HIGH->B, stays active. | 2026-08-16 weekly: the HTML blog listing did not expose post titles or dates to WebFetch; lead with the recorded rss_url (https://www.intel471.com/blog/feed) for discovery on this host rather than the listing page.
