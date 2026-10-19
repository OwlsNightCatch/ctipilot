# Audit working notes — 2026-10-11T1307Z-audit (main agent, persisted per guard #4)

## Phase 0
- Clock: local = network 2026-10-11T13:07:20Z, skew 0 s. Newest run on origin/main: 2026-10-11T0256Z-intel.
- LAST_AUDIT (any audit record): runs/2026-09-30/2026-09-30T0639Z-audit.md, started 2026-09-30T06:39:43Z. Window 270.5 h.
- Last FULL audit (truth passes + G re-sweeps): 2026-09-27T1308Z-audit. The 09-29T2134Z (SR1-3, T1-4 page triage), 09-30T0634Z (SR1) and 09-30T0639Z (R1, SITE) audits were operator-directed partial audits with no coverage re-sweep. Gap: 09-27T13:08 → 09-30T06:39 never re-swept; 5 entries published in it never truth-checked by any audit (wwahost 09-27 was the 09-27 audit's own recovery; storm-2570 09-29; manno, star-blizzard, storm-3068 09-30). Remedy this fire: G sweeps extended to 09-27T13:08 by addendum; the 5 entries added to T1.
- check-all: 25 pass · 1 warn (2026-09-30T0639Z-audit duration 100.8 h) · 0 fail · 23 acknowledged.
- ATT&CK pin: up to date, local v19.2 == upstream v19.2.
- Page-checks: ran from 2026-09-01 because the prompt's detection string ("--page-checks-since") is absent from every report, although the 2026-09-29 audit report records the backfill ("The cited-page backfill ran", from 2026-07-01). The one-time instruction is stale. 255 entries, 923 pages: 1024 quotes verbatim, 101 not machine-checkable; 3 quote-literal + 5 citation-cve WARNs → leads to T1, T4, T7, T8.
- Calibration: no October report carries `## Priority calibration` → this fire owns Phase 3b.
- Legacy batch L1: 20 entries (queue 468 pending, 7 reviewed).
- 10-04 scheduled audit: no record on main (weekly Sunday 13:08 audits fired 09-20, 09-27; the 0639Z operator session was open until 2026-10-04T11:30Z). Availability signal for the operator, not a cadence judgment.
- 10-01 intel fire: no record; 10-02 fire gap 48 h, window 50 h, S3 ran the outage-backfill vendor-listing sweep (S3.progress 04:09:58Z). Self-heal held.

## Phase 3 (local)
- Discipline (34 new entries): actions 0/1/2 = 19/6/9 (empty-is-normal holds); priority 2 critical / 6 high / 23 notable / 3 routine (high 18 %, high+crit 24 %); classification B2 15, A2 13, A1 4, B1 2; techniques mean threat 10.6, vulnerability 4.5, incident 2.8, research 2.7.
- exploitation-consistency over 126 window entries: PASS. entry-shape: 9 WARNs (7 main analyses over 550 words: FortiMail 666, SD-WAN 596, Zammad 1048, Citrix 88779 566, Atlassian 659, Denmark CPR 700, SonicWall 102255 627; 2 headlines 125 chars: Zammad, Denmark CPR).
- KEV (G1a's kev_window_diff --since 2026-09-30): 10 additions, all COVERED; no COVERED-STALE.
- Fix effectiveness: kev-window.txt written by all 10 fires (v4.10 holds); RANSOMWARE row (PAN-OS CVE-2026-0257) surfaced 10-05 (borderline-drop pending fold), dispositioned 10-06 as an update (v4.19 holds); cisa-news swept 3/10 fires, cisa-directives 2/10, cisa-advisories 10/10 (v4.18 holds).
- Entity hygiene: 37 new non-product entities, one prose-only attachment (Flax Typhoon on the 2026-08-28 DOJ QScan entry — a genuine mention). Clean.
- Backlog: 4 open rows (Guardium CVE-2026-85542 held to 10-14; SafePay ARA Lyss-Limpachtal to 10-14; Payload/Netech to 10-14; Beyond Gravity to 10-20). Guardium: national-CSIRT exploitation report + three new unauthenticated CVSS 9.8 flaws 10-08 — re-gate against PD-11(b) after G1b returns.
- Duplicates: 43 unlinked CVE-sharing pairs in 24 groups; 24 legacy "UPDATE (originally covered …)" entries.

## Model-generation baseline (intel fires)
| | Sonnet 5 (09-22..09-29, n=8) | Sonnet 5.5 (09-30..10-11, n=11) |
|---|---|---|
| fire duration, median | 2.50 h | 2.79 h |
| verifier iterations, mean | 7.2 | 5.6 |
| confirmed double-CLEAN | 3/8 | 5/11 |
| iteration-1 truth findings per published+updated entry | 0.78 | 1.55 |
| research sub-agent duration, mean | 9 min | 23 min |
| research items returned per fire | 9.8 | 25.2 |
Confound: v4.17 (claim ledger: iteration 1 walks every claim instead of sampling) landed 2026-09-29/30 with the model change, so iteration-1 findings and convergence are not attributable to the model alone.

## Coverage triage (G3a / G3b)
- NeedyMantis (Microsoft TI 2026-09-28; Storm-3069, China-origin, intergovernmental organisations + government contractors; grew out of the DAEMON Tools investigation): dropped by 09-30 / 10-02 / 10-03 fires as "out of window, limited-victim". Recency reason misapplied (msft-ti is a rotational standard record; PD-7(d) lookback covers a 2-day-old post). Candidate recovery (threat, notable). Root cause also in transport: `msft-secblog recent` returns only the newest 10 items, so a lookback longer than ~2 days on that recipe misses older posts (G3a).
- Correctly droppable, fires' recorded reasons stand: MDDR 2026 (statistics, no decision), MSP360→ScreenConnect (well-understood, comparable entries), TA419 (US/Japan), DragonForce Lab52 second backdoor (10-03: single-lab attribution, entry guidance covers TURN egress + sideloading), Zscaler ransomware report, GTIG vuln-trends (statistics), ARTEX (Korea), Huntress Akira (no new capability), MATCHBOIL (Ukraine), UAT-11985 (Taiwan).
- G3b borderlines: ReliaQuest quarterly (periodic vendor stats), Push AI lures (minor delta on 10-04 ChatGPT entry), GlassWorm themes (2 of 10 malicious, removed), AISI GPT-6 Astra (simulation), DarkSword (patched, untested), TeamViewer TV-2026-1010 (not exploited, auth needed: fails PD-11 b), SRG chat leak (unverified provenance), SAMSIK (Denmark threat level, no technical content), DTU IAM breach (no vector beyond compromised profiles; incident floor).
- T4 note: Exchange MRSProxy quote-literal WARN is a gate false positive — Mastodon post text lives only in og:description/description meta tags, which the extractor does not read. Tool fix candidate in check_run.py quote-literal.
- FIX SHIPPED (pending commit): tools/check_run.py _page_skeletons keeps description/og:description/twitter:description meta content as text; re-run on 2026-08-29 Exchange MRSProxy: 9 quotes verbatim, 0 WARN (was 2 WARN).
- FIX SHIPPED (pending commit): tools/fetch_source.py _pdf_streams skips an uncompressed image stream (image filter in its dictionary, or <85 % printable bytes) instead of keeping it as "content" because it happens to hold "BT"/"Tj" bytes. ANSSI CERTFR-2026-CTI-006.pdf (image-only) had come back as 467 KB of JPEG bytes, which the citation-cve check then searched and flagged (false positive). New test test_uncompressed_image_stream_is_not_content; 14/14 pass. Stale cached body deleted; live re-check after Phase 1/2.

## Phase 3b calibration data
- Store (997): critical 30 (3 %) / high 408 (41 %) / notable 540 (54 %) / routine 19 (2 %). Aug: 1/96/98/1 (n=196, high 49 %). Sep: 13/36/66/13 (n=128, crit 10 %, high 28 %). Trailing 30 d: 10/20/67/16 (n=113, 9 % / 18 %). Oct 1-11: 2/6/23/3 (n=34, 6 % / 18 %).
- Sep high fell from ~50 % mid-month to 28 % after v4.17's exposure-graded high bar and the 09-30 audit's 36 recalibrations (23 high→notable, 2 high→routine, 11 notable→routine).
- F16 in month's run records: 12 findings; October 6: Kiteworks high kept (declined, 10-02), Belnet → routine, Liechtenstein high → notable, Citrix 107406 high → notable, PaperCut critical → high (patch ≥1 week, no new exploitation), IDC Frontier → routine. All in the generous direction; none under-alerting.
- Criticals Sep–Oct (15): every one an exploited (or KEV-listed) flaw on internet-facing infrastructure the constituency runs (JFrog ×2, MikroTik, N-able, Magento, Check Point ×3 incl. VPN, Cisco SEG, ISE, SD-WAN, Arista VeloCloud, F5 APM, WordPress, Citrix NetScaler, FortiMail). Standing question from 09-13/09-20/09-27: the elevated critical rate tracks a heavy September edge-exploitation month, not a drifted bar; October's rate (6 %) is back toward the store's 3 %.
- Linked same-day twins also need folding (the duplicate scan only finds unlinked pairs): CVE-2026-50751 (2026-06-09 ×2, linked by the 09-30 audit, T5 flags F7) and CVE-2026-87491 (2026-09-10 BlueMoon kit vs Chrome V8 zero-day: likely distinct, link stands).

## Phase 4 note: taxonomy gap for non-adversarial items (2026-10-11T14:31Z)
The legacy DENIC .de DNSSEC outage entry (2026-05-09) is a non-adversarial operational incident. `incident`
and `threat` require techniques[] (FAIL), `research` WARNs when empty, so the only warning-free kind is
`policy`, whose definition (PD-11 c, regulatory action) does not fit. Recorded as `policy` (same rendered
section as research). Recommendation for the operator: decide whether non-adversarial resilience items stay
in scope at all, and if so add a kind or an explicit techniques-exemption rule for them.
