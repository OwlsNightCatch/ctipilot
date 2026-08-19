- **paradigm-shift-research** (rotation) — Paradigm Shift Technology (ps.tc) · https://ps.tc/ · rss=- · fetch_method=bridge · reliability=B · lang=en · last_fetch=2026-07-29
  recipe: 2026-08-16: still SPA-shell only on the direct transport; the reader escalation that would recover it was unavailable all run (all keys HTTP 402). Unchanged status — the gap is the reader pool, not this recipe.
- **cryptotimes** (rotation) — CryptoTimes (cryptotimes.io) · https://www.cryptotimes.io · rss=- · fetch_method=webfetch · reliability=C · lang=en · last_fetch=2026-08-02
  recipe: 2026-08-02: contributed the in-window anchor for the COLDCARD wallet-seed theft entry (Galaxy Research third-wave figures, relayed 2026-08-01T20:36Z).
- **sans-ics** (rotation) — SANS ICS · https://www.sans.org/blog/?focus-area=industrial-control-systems-ics · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-07
  recipe: 2026-07-05 admiralty audit: B — SANS original expert content but training-heavy and non-primary; ICS cadence sparse, filter hard. Live, active retained.
- **team-cymru** (rotation) — Team Cymru S2 Research · https://www.team-cymru.com/blog · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-07
  recipe: 2026-07-05 admiralty audit: B — original telemetry-based infrastructure research; live. Keep active. Listing omits dates — drill /post/ pages for the date.
- **zimperium-zlabs** (rotation) — Zimperium zLabs · https://zimperium.com/blog · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-07
  recipe: 2026-07-05 admiralty audit: B (MEDIUM->B) — original mobile-threat research lab, first-hand telemetry; stays active, no change.
- **ahnlab-asec** (rotation) — AhnLab ASEC · https://asec.ahnlab.com/en/ · rss=- · fetch_method=webfetch · reliability=B · lang=en,ko · last_fetch=2026-08-09
  recipe: 2026-07-05 admiralty audit: B (HIGH->B) — AhnLab vendor research lab, first-hand telemetry; keep active, plain WebFetch works on listing and articles.
- **citizen-lab** (rotation) — Citizen Lab · https://citizenlab.ca/category/research/ · rss=https://citizenlab.ca/feed/ · fetch_method=rss · reliability=B · lang=en · last_fetch=2026-08-09
  recipe: 2026-07-18 (jina-last-resort session): the /category/research/ listing began returning an empty archive (URL-path change suspected, flagged as a coverage gap in the 2026-07-18T0409Z run). RSS at https://citizenlab.ca/feed/ verified working via DIRECT feed fetch (fresh: item dated 2026-07-17) — fetch
- **cloudflare-cf1** (rotation) — Cloudflare Cloudforce One · https://blog.cloudflare.com/tag/cloudforce-one/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-09
  recipe: 2026-07-05 admiralty audit: B — vendor threat-research lab with first-hand internet telemetry, original research; live and drillable, no change (active).
- **coinspect-research** (rotation) — Coinspect Security · https://www.coinspect.com/blog/ · rss=- · fetch_method=bridge · reliability=B · lang=en · last_fetch=2026-08-09
  recipe: Added 2026-08-09 by the weekly quality audit. Application-security research lab focused on wallet and cryptographic-implementation review; broke the CryptoJS 'Ill Bloom' investigation (CVE-2026-71851) that this audit recovered as a coverage miss — a twelve-year-old CSPRNG failure under active exploi
- **trellix** (rotation) — Trellix Blogs · https://www.trellix.com/blogs/ · rss=- · fetch_method=bridge · reliability=B · lang=en · last_fetch=2026-08-09
  recipe: 2026-07-27 intel run: S3 reports the bridge fetch returns header/nav markup only and WebFetch's listing shows posts no newer than April-May 2026, suggesting a stale/cached index rather than the true latest list. Host reachable; recipe needs a deeper fetch or RSS discovery. Not a demotion.
- **fox-it-blog** (rotation) — Fox-IT International Blog (NCC Group) · https://blog.fox-it.com/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-11
  recipe: 2026-07-05 admiralty audit: B — original NCC/Fox-IT DFIR research; no status change (active). Very low cadence (3 posts in ~18 months) — empty window is expected, not a failure.
- **ibm-xforce** (rotation) — IBM X-Force · https://www.ibm.com/think/x-force · rss=- · fetch_method=bridge · reliability=B · lang=en · last_fetch=2026-08-11
  recipe: 2026-07-05 admiralty audit: B — original vendor threat research; listing lacks inline dates so read dateModified from the article HTML via bridge. MEDIUM->B, stays active.
- **intel471** (rotation) — Intel 471 Blog · https://www.intel471.com/blog · rss=https://www.intel471.com/blog/feed · fetch_method=rss · reliability=B · lang=en · last_fetch=2026-08-11
  recipe: 2026-08-16 weekly: the HTML blog listing did not expose post titles or dates to WebFetch; lead with the recorded rss_url (https://www.intel471.com/blog/feed) for discovery on this host rather than the listing page.
- **unit42** (rotation) — Palo Alto Networks Unit 42 · https://unit42.paloaltonetworks.com/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — flagship vendor threat-research lab, original first-hand research; both WebFetch HTML and /feed/ RSS work. No status change.
- **talos** (rotation) — Cisco Talos · https://blog.talosintelligence.com/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — original Cisco threat-research lab; live. Keep active.
- **mandiant-gtig** (rotation) — Google Cloud / Mandiant (GTIG) · https://cloud.google.com/blog/topics/threat-intelligence · rss=https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v · fetch_method=rss · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — GTIG/Mandiant original first-hand threat research. Reliability HIGH->B, status stays active. Use feedburner RSS for dates (HTML landing is dateless).
- **checkpoint-research** (rotation) — Check Point Research · https://research.checkpoint.com/ · rss=- · fetch_method=rss · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-14 intel run: fetched via feed + article, contributed the Annual AI Security Report 2026 entry.
- **eset** (rotation) — ESET WeLiveSecurity · https://www.welivesecurity.com/en/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — vendor research lab, original telemetry-driven research (esp. EU APTs); live, keep active.
- **kaspersky-securelist** (rotation) — Kaspersky Securelist (GReAT) · https://securelist.com/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-18 weekly audit: the securelist.com LISTING renders several post titles with NO visible publish date on a plain fetch, silently pushing new in-window posts below the visible fold (caused the GoSerpent 07-16 miss, recovered by the audit). For discovery, sweep the RSS feed (https://securelist.
- **sentinellabs** (rotation) — SentinelOne / SentinelLabs · https://www.sentinelone.com/labs/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — vendor threat-research lab, original malware/APT research; live and drillable. Status stays active.
- **proofpoint** (rotation) — Proofpoint Threat Research · https://www.proofpoint.com/us/blog/threat-insight · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-26 weekly quality audit: promoted candidate → active on the documented lifecycle bar (cited by published entries from 11 distinct runs; the bar is 3). The promotion had never been executed because nothing counted contributing runs — the digest now emits sources.promotion_due (tools/run_summa
- **sophos-xops** (rotation) — Sophos X-Ops (incl. former Secureworks CTU) · https://www.sophos.com/en-us/blog · rss=https://www.sophos.com/en-us/blog/feed?id=blt6f15f4f7deaf4242 · fetch_method=rss · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — original vendor threat-research lab with first-hand telemetry; feed recovered and clean. Keep active.
- **elastic-seclabs** (rotation) — Elastic Security Labs · https://www.elastic.co/security-labs · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — vendor research lab, first-hand original research; live, keep active.
- **crowdstrike** (rotation) — CrowdStrike Threat Research · https://www.crowdstrike.com/blog/category/counter-adversary-operations/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — vendor threat-intel lab, original adversary research from own telemetry; live and drillable, no change (active).
- **recordedfuture-insikt** (rotation) — Recorded Future Insikt Group · https://www.recordedfuture.com/research/insikt-group · rss=https://www.recordedfuture.com/feed · fetch_method=rss · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-08-16 weekly (RECIPE FIX): the logged recipe gap is resolved — https://www.recordedfuture.com/feed returns a full, dated RSS feed with direct article links (the /research/rss.xml path 404s). fetch_method webfetch -> rss with that rss_url; the /research/insikt-group landing page remains a missio
- **group-ib** (rotation) — Group-IB · https://www.group-ib.com/blog/ · rss=- · fetch_method=bridge · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-08-13: contributed the WindRelay/SpyNote NFC-relay research this run; blog RSS at https://www.group-ib.com/blog/rss.xml parsed cleanly and the article body was reachable via `fetch_source.py url`.
- **huntress** (rotation) — Huntress Labs · https://www.huntress.com/blog · rss=- · fetch_method=rss · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — original IR/EDR telemetry research; filter product/marketing posts. HIGH->B, stays active.
- **volexity** (rotation) — Volexity · https://www.volexity.com/blog/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-05 admiralty audit: B — independent APT/forensics research lab, original first-hand research; sparse cadence is expected, not a failure. No status change.
- **zscaler-threatlabz** (rotation) — Zscaler ThreatLabz · https://www.zscaler.com/blogs/security-research · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-27 intel run: PROMOTED candidate -> active. tools/run_summary.py reported it in sources.promotion_due with 3 contributing runs (most recent 2026-07-26T2309Z-weekly), meeting the three-contributing-run bar.
- **dragos** (rotation) — Dragos · https://www.dragos.com/blog/ · rss=- · fetch_method=webfetch · reliability=B · lang=en · last_fetch=2026-08-17
  recipe: 2026-07-10: blog feed https://www.dragos.com/blog/feed/ returned 404 direct; jina fallback timed out (S3). Recipe/feed-URL review needed; WebSearch surfaced only the Feb-2026 annual report (out of window). NOT demoted (transport).