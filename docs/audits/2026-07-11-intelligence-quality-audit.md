# Full-store intelligence-quality audit — 2026-07-11

Operator-directed audit (session run record: [`runs/2026-07-11/2026-07-11T1435Z-audit.md`](../../runs/2026-07-11/2026-07-11T1435Z-audit.md)). Mandate: identify published reports that are false or erroneous, coverage that is incomplete or missing, root-cause every failure, and ship the fixes — soundness (no false/marginal content) and completeness (no blind spots) weighted equally.

**Method.** Three independent cold-reader verification passes fetched the primary sources behind **all 55 entries published 2026-07-08 → 2026-07-11** and checked every CVE id, CVSS, KEV/exploitation claim, version boundary, victim statement, attribution, and evidence quote (~85 primary URLs). Three independent landscape re-sweeps re-researched the 2026-07-03 → 2026-07-11 window (vulnerabilities/exploitation; incidents with CH-DACH-EU priority; threat research/APT) and diffed the results against the store. In parallel: run-record telemetry analysis over all 90 runs, source-health cross-checks, and gate/tooling review.

## Verdict

The store is in strong shape on truth: **52 of 55 recent entries verified factually clean, most point-for-point verbatim against their primaries.** No hallucinated victims, no fabricated exploitation/KEV claims, no broken primary URLs, no leak-site claims presented as fact. Coverage is equally strong on the mechanical channels: every in-window CISA KEV addition covered, national-CERT surface clean, no missed Swiss/DACH/EU incident. The failures found are real but narrow, and every one traces to a specific, fixable mechanism — detailed below with the shipped fix.

## Findings — false or erroneous published intelligence

| # | Entry | Defect | Ground truth | Fix |
|---|---|---|---|---|
| 1 | `2026-07-09/talos-wolfssl-geovision-vtkdicom-disclosure` | Three wolfSSL CVE ids don't exist (NVD "Not Found"): CVE-2026-28739, -25106, -33091 | Talos's own per-advisory "Vendor Response" fields: **CVE-2026-7532, CVE-2026-5263, CVE-2026-6678** | Repaired in place + `state/cves_seen.json` re-synced (logged immutability exception) |
| 2 | `2026-07-08/beyondtrust-rs-pra-preauth-bypass-cve-2026-40138-cluster` | CVE-2026-40141 published at CVSS **9.9** — above the cluster's two pre-auth admin bypasses (9.2) | Vendor advisory BT26-03: **High / 8.5** | Repaired in place (logged exception) |
| 3 | `2026-07-10/odido-shinyhunters-vishing-dutch-police-attribution` | `techniques[]` carried **T1656**, revoked in the pinned ATT&CK v19.1 | Superseded by **T1684.001** (Impersonation) | Repaired in place (logged exception) |

**Root causes.** (1) is the worst class: the entry's *cited roundup blog* (Talos's own) misprinted ids that Talos's per-CVE advisory pages contradict — the pipeline's two-source rule couldn't catch it because blog and advisories are one publisher, and nothing required id transcription from the per-CVE authority. A wrong id is not cosmetic: it poisons the CVE dedup index, the `/cve/` pages, and automated triage agents matching alerts by CVE. (2) is a transcription slip the verifier never re-derived from the owning advisory. (3) shipped because a dead ATT&CK id only WARNed at the gate even though the pinned dataset was on disk at compose time.

**Minor findings (documented, no repair warranted):** iCagenda (07-10) attributes the prior Joomla-wave cluster to a cited page that names different examples (the named cluster is independently KEV-confirmed — citation-locality imprecision); Odido's "forensic voice analysis" framing rests on the NOS corroboration rather than the Politie primary (defensible, slightly strengthened); seven 07-08/07-09 vulnerability entries carry `classification: null` (pre-v3.18 runs, grandfathered — the v3.18 always-rated gate already closed this class); one verification pass itself mis-asserted that T1656 was active — a reminder that verifier findings need mechanical ground truth where one exists (the pinned-dataset check is exactly that).

## Findings — missing or incomplete coverage

- **Clear miss (now closed): Kaspersky "Armored Likho / BusySnake Stealer" (2026-07-03).** New APT targeting **government agencies and the electric-power sector**; LLM-generated loader chain; Python stealer with concrete hunt pivots. Squarely PD-11(d) and the profile's sector lens. Published by this audit as `entries/2026-07-11/armored-likho-busysnake-ai-generated-loader-python-stealer.md` with a provenance note.
- **Borderline (correctly-droppable, documented): Infoblox "Lurking Lizard" (2026-07-07)** — new named residential-proxy actor with two transferable hunt angles, but consumer-victim scope and an adjacent in-store proxy-botnet story; does not clear PD-11 standalone. **Roundcube 1.6.17/1.7.2 patch (2026-07-05/06)** — no exploitation of the new CVEs; worth a fold-in reference next Roundcube delta given active targeting coverage in-store.
- **Watch item: `bd.zh.ch` (Kanton Zürich Baudirektion) MedusaLocker leak-site listing (2026-07-01)** — single-source claim, zero corroboration found in dedicated German-language sweeps; correctly excluded under the fake-news guard, flagged in the run record because the claimed victim is core constituency. Re-check for corroboration on future runs.
- **False alarm resolved:** the Argo CD repo-server unauth-RCE (Synacktiv 07-01, NCSC-CH 07-03) initially looked like a critical miss — the store covered it on **2026-07-02**, one day after publication. Pipeline performed correctly.
- **Root cause of the misses.** Both missed items date to the **2026-07-06/07 scheduler outage** window. The 07-08 backfill run (64 h window) swept KEV, national CERTs and aggregators — but vendor **research-blog** publications don't route through CVE/KEV discovery paths, and no duty required a per-publisher listing sweep for the outage dates. The zero-entry runs of 07-04–07-06 were separately audited and found *defensible* (documented borderline drops, quiet-holiday window, sound reasoning) — the volume trough was real-world, not a filter failure; the outage misses were structural.

## Findings — systemic / operational

1. **Runaway main runs.** `2026-07-04T1809Z` ran **17.8 h** and `2026-07-09T2009Z` ran **11.2 h** wall-clock (container stalls), publishing up to ~11 h late. The next scheduled fire overtakes a stalled run and cannot see its in-flight coverage (`2026-07-10T0409Z` computed `gap_hours: 16` because `2009Z`'s record hadn't landed). The overtaken run improvised the correct recovery — re-pull main, re-dedup, publish only the delta — which is now codified.
2. **Publish-status follow-through.** `2026-07-09T1211Z`'s Phase 7 amendment never landed; nothing surfaced it.
3. **Reachability ≠ readability.** Essential source `ncsc-uk` was a "recipe gap" in nearly every July run (consent-banner shell on every transport) while bookkeeping showed it green — an essential source dark for weeks. A working, fresh feed endpoint existed the whole time (`all-rss-feed.xml`).
4. **Action-item inflation (already fixed pre-audit).** Post-v3-cutover entries uniformly shipped 2–3 `actions[]` each (49 rendered action items on 2026-07-09 alone; zero entries with the empty-is-normal shape). v3.19 (2026-07-11) set the do-now bar; this audit confirms the diagnosis was right and adds nothing further — watch the next runs' distribution.
5. **Priority calibration.** Store-wide: 15 critical / 335 high / 564 notable / 1 routine. No `critical` since 2026-06-30 — consistent with the extreme bar, and the verification passes judged recent windows correctly calibrated. No change shipped; the 37 % `high` share is worth a look at the next monthly review.

## Fixes shipped in this commit

- **prompts v3.21** (`cti-run.md` + weekly banner + CHANGELOG): CVE-id/CVSS provenance rule (per-CVE authority beats roundup; unresolvable id never enters `cves[]`); main-run wall-clock watchdog (~3 h → land the run) + mandatory re-sync-and-re-dedup when overtaken; outage-backfill duty (gap > 24 h → per-publisher research-blog listing sweep for the outage dates).
- **Verifier definitions** (both, byte-identical): check 4 now cross-checks every `cves[]` id and CVSS against the per-CVE authority; contradiction or unresolvable id is F4.
- **`tools/check_run.py`:** dead ATT&CK ids in `techniques[]` FAIL on v3.21+ runs (store-wide stays WARN — later pin updates legitimately revoke ids on immutable history); WARN on `duration_seconds` > 3 h (per-run and `--all`); `--all` WARN on a v3.14+ record still missing `publish_status` > 24 h after start.
- **Store repairs** (immutability exceptions, logged): the three factual errors above.
- **`sources/sources.json`:** `ncsc-uk` working recipe (`all-rss-feed.xml` + `fetch_source.py feed`) recorded in notes/rss_url.
- **Memory:** runaway-run/publish-race diagnosis (`scheduler-and-workflow-races.md`); ncsc-uk recipe + "reachable but unreadable" failure class + ransomware.live JSON API recipe (`source-fetch-blocks.md`); repair log (`entry-immutability-exceptions.md`).
- **Entry published:** Armored Likho / BusySnake (audit-recovered).

## Recommendations (operator decisions, not shipped)

1. **Populate the org-profile watchlists.** `config/org-profile.yaml` configures no product or supplier watchlists, so every run's S1/S4 watchlist sweep is a documented no-op. A cantonal/federal deployment would benefit from watching its actual estate (e.g. `*.zh.ch` domains and key suppliers) — the `bd.zh.ch` MedusaLocker listing shows exactly the signal a victim-side watchlist would prioritize for corroboration hunting.
2. **Scheduler-side watchdog.** The in-prompt watchdog can't fix container stalls; the scheduler should alert when a fire runs past ~2 h or a scheduled slot produces no run record within an hour (the 62 h outage was invisible until a human looked).
3. **Monthly priority-calibration review.** The `high` share (37 %) is stable but on the generous side; one pass a month over the priority distribution against F-category drift keeps the notification channel honest.
