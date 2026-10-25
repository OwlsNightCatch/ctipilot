# Phase 3 notes — 2026-10-25T1308Z-audit

## Telemetry (window intel fires 2026-10-19 → 2026-10-25, daily at ~02:56Z)
- 7 fires, gap 24 h each, window 26 h, durations 1.6–4.5 h, all publish_status ok. No coverage hole, no self-heal failure.
- New entries 27 (0/4/6/6/8/1/2), updated-entry records by fires: 2/5/4/4/4/9/4.
- Verifier: 0 of 7 fires reached a confirmed CLEAN. Iterations 3/4/7/8/5/3/7 (mean 5.3). Six published on the low-residual early exit, one (10-22) at the cap with residual 5. Only one CLEAN verdict all week (10-21 iteration 6), refuted by iteration 7.
- Partial audits after LAST_AUDIT: cleanup waves 01 (10-20T0835Z), 02 (10-21T0800Z), 03 (10-21T1149Z), 04 (10-21T1148Z); all publish ok. Wave 05 claim (10-21T1147Z, partial, wave=05) open on main since 2026-10-21T11:48Z with no further push: paused or abandoned; ignored per Phase 0 step 2.
- Out of scope per v4.22: 187 unique entries whose only in-window activity is records of another audit fire (10-21T1149Z 23, 10-21T0800Z 69, 10-21T1148Z 74, 10-20T0835Z 12, 10-18T1307Z 13, 10-11T1307Z 1 — Check Point).
- High re-grade (31% of the 36 in-scope entries; 11% of new entries): all 11 hold — exploited edge or app flaws (PAN-OS 0257, Metabase, Zimbra, NetScaler 88779, Atlassian, Arista), Swiss incidents (Publica PK), constituency-supplier or tenant compromises (ConnectWise, TeamUpdraft), Danfoss (NCSC.ch exploitation rating, pro-Russian hacktivists), Fortinet out-of-cycle edge fixes. No priority moved.

## Publish follow-through
- Every window record carries publish_status ok.

## Source health (state/source_health.json, 2026-10-25T09:16Z)
- 261/266 relevant; needs-content-fix: ox-security (shell), securityweek (shell), connectwise-trust-center (blocked but direct reads). Demoted fox-it-blog, threatpost handled; ec-digital-strategy-newsroom documented blocked.
- No source carries the webfetch-only verdict this snapshot (66 fetch_method webfetch records all read relevant in-container except securityweek).

## Discipline
- New entries: priority 1 critical / 3 high / 22 notable / 1 routine (high 11%). All 36 window entries: 11 high + 2 critical (high 31%) → calibration alarm; re-grade.
- actions: 15 one, 2 two, 1 three, 9 empty. Every action reviewed: concrete and finding-derived; none generic.
- techniques density: threat 16.1, incident 7.0, vulnerability 1.9 (unchanged pattern).
- classification: A2 14, B2 8, A1 3, B1 2.
- Length: 18 of 37 window entries over the 550-word analysis bound, all grown through records; headlines over 120 on Atlassian (133) and PHP (124). Root cause: entry-shape length check reads new entries only. Fixed (v4.24 prompt rule + growth WARN).
- exploitation-consistency: PASS over the window. Critical immediate_action names a fixed version on both criticals.
- Registry: 133 records added between the window start and this fire (105 product records, 28 curated: 9 actor, 7 malware, 6 tool, 4 incident, 1 campaign, 1 trend). Product duplicate product:chroma / product:chromadb tombstoned. No duplicate actor key (APT28 had no actor record before 10-21; TA458 is Proofpoint's distinct designation).

## Gate & pin
- check_run --all: 0 fail, 1 warn (2026-10-21T1148Z-audit duration 24.9 h) → acknowledged. ATT&CK v20.0 current. site/build.py: no self-check warning.

## Duplicates (item 13)
- One unlinked CVE-sharing pair touching the window by activity: 2026-05-13 Mini Shai-Hulud pwn-request vs 2026-05-28 Nx Console/TanStack/Daemon cascade (CVE-2026-45321). Both are in-window only through cleanup records (out of scope); the 05-28 entry sits in open rows W1-I and W4-15 (wave 06). Left to wave 06.

## KEV
- 8 additions since 2026-10-18; 3 COVERED; 5 NOT COVERED (4 Plex, SiteGuard) carry borderline-drop lines in 2026-10-21T0256Z-intel and 10-22. No COVERED-STALE, no RANSOMWARE row.
- Bookkeeping gap: Siemens CVE-2026-110936 and Arista CVE-2026-114625 KEV listings not reflected in status/tags (internal records).

## Tooling defects hit this fire
- kev_window_diff --since crashed on the window-start timestamp the audit prompt passes → fixed.
- Truth-pass envelope named ledgers truth-T<X>.ledger.yaml; the ledger script wrote truth-<X>.ledger.yaml (my naming mismatch; every pass found the file).
- Main agent ran kev_window_diff twice (two `--json` calls in one command, one KEV catalogue read each) to test the fix while Phase 1/2 agents ran: a guard #9 deviation, catalogue JSON only.
