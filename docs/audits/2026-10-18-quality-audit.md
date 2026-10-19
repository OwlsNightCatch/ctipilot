# Quality audit — 2026-10-18

**Run record:** [runs/2026-10-18/2026-10-18T1307Z-audit.md](../../runs/2026-10-18/2026-10-18T1307Z-audit.md) · **Prompt:** v4.21 · **Window:** 2026-10-11T13:07Z → 2026-10-18T13:07Z (the trailing week since the 2026-10-11 audit)

## Method

Scheduled weekly audit. The fire started on 2026-10-18 under v4.19 with a wider window (2026-09-30 → 10-18, 147 entries) and the legacy queue. It stopped on the API rate limit, and while it stood paused the operator directed that audits stay on the trailing week and inside their session limit; v4.21 shipped that on `main`. On resumption the fire was re-based on `main` (base `74695f56`), its claim (`work/2026-10-18T1307Z-audit/audit.claim`) was pushed before any further work, and the scope was cut to the trailing week. Everything outside the week that the early passes found is carried forward (§ Carry-forward), not fixed here.

- **Primary scope:** 30 entries with activity in the week: 21 filed by the week's fires and 9 older entries the fires updated. NeedyMantis (filed by the 2026-10-11 audit, verified by that audit's own loop) is in the window but had no truth pass here.
- **Excluded:** 115 entries whose only in-week activity is the 2026-10-11 audit's own records; that audit's eight-iteration loop verified them.
- **Truth passes:** the week's 30 entries were covered by passes T1, T2, T3, T6b and T9 (`work/2026-10-18T1307Z-audit/truth-*.yaml`), each claim against its freshly fetched cited source.
- **Coverage re-sweeps:** G1 (vulnerabilities), G2 (incidents and region), G3a and G3b (research), each listing every in-week item against the fires' run records.
- **Main-agent reads for the fixes:** Bricksforge changelog, Previdian, Wordfence (blog and record), CISA ICSA-26-057-10 (CSAF recipe), Claroty Team82, PaperCut's bulletin, Huntress, watchTowr (two posts), GreyNoise, BleepingComputer, the Microsoft Exchange Team's two posts, Netcraft and The Guardian.
- **Sub-agents:** 22 spawns (19 first spawns plus three continuations after the rate limit), all before v4.21 landed, about 11.5 M sub-agent tokens; one closing verifier spawn after it, about 0.5 M (§ Systemic 1). Log: `work/2026-10-18T1307Z-audit/budget.tsv`.

## Verdict

**16 of 29 truth-passed entries clean.** Nine carried imprecisions only and four carried factual errors; a cited-page check found a fourteenth defect, stale quotes on the Exchange entry. Every defect is fixed through a changelog record on its entry. The week's fires covered every in-week item the re-sweeps listed except one research post, recovered here as a new entry. The pipeline's weekly output is sound on its critical and high signal: every exploited or KEV-listed flaw of the week was covered, all nine KEV additions are covered, and no defect changed a reader's patch or hunt decision except Bricksforge's fixed-version story.

## Findings — false or erroneous published intelligence

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| 2026-10-12 Bricksforge CVE-2026-85097 | Fix placed in 4.0.1; "whether 4.0.0 is affected is not stated"; Previdian quoted as tagging a PoC only (factual error) | The vendor changelog, revised after publication, says the CVE was fixed in 3.1.8.10 and 4.0.0; 4.0.1 fixes a related upload issue affecting every Pro Forms site; Previdian now lists it exploited | `update` record (title, headline, summary, cves, evidence, sourcing note, action, body) |
| 2026-08-29 PaperCut NG/MF | Release 3's regressions attributed to Release 2 (factual error); log hunt missed the `LogonMessage` route and was uncited; 47% figure undated; GreyNoise's 12 called a final tally of 395; the attacker-chosen Derby database name printed as an indicator | Bulletin: Release 3 "addresses two known regressions"; watchTowr documents `LogonMessage`; Huntress 28 August; GreyNoise "at time of last observation" | `correction` record (summary, actions, body); the 2026-09-03 record's own summary is append-only and is named in the correction |
| 2026-10-08 SonicWall SMA1000 | Previdian count attributed wrongly (factual error) | THN 2026-10-12 carries the count; Previdian's page now shows 1,887 attempts from five addresses, 9 to 16 October | `correction` record |
| 2026-10-10 MikroTik CVE-2026-84411 | 7.23.8 changelog line quoted as naming one CVE (factual error) | "system - improve stability (includes CVE-2026-84411, CVE-2026-103903);" | `correction` record; CVE-2026-103903 added to `state/cves_seen.json` |
| 2026-08-28 Claroty Copeland XWEB | Said CISA ICSA-26-057-10 could not be located and three CVEs were unpublished; CVE-2026-21718 typed a logic flaw; "zero interaction"; field link "RS-485 and Ethernet"; energy sector | The advisory exists and lists all 23 ids (CVE-2026-3037, -22877, -20797 added); both sources call 21718 an authentication bypass; RS485 serial Modbus; Claroty names food retail and healthcare | `correction` record; entry now two-source; three CVEs added to `cves_seen` |
| 2026-09-28 Citrix CVE-2026-88771 | Headline calls both zero-days default-configuration; "periodically" unsupported; an evidence quote's continuation unreadable at its source | CVE-2026-88772 needs DTLS (on by default only on VPN vServers); watchTowr shows a log search for two Pitboss strings; BleepingComputer carries the quote up to "again" | `correction` record |
| 2026-10-18 Rank Math PRO 3.0.123 | No CVE id | Wordfence assigned CVE-2026-111862 (CVSS 3.1 9.8, affected 3.0.123, patched 3.0.124) | `improvement` record; id added to `cves_seen` |
| 2026-10-14 Ivanti Connect Secure | CVE-2026-111357 score null; 25.1.3.0 missing from the fixed builds | CVE record 7.0 (CVSS 3.1); Ivanti's CNA record lists 25.1.3.0 unaffected | internal `improvement` record (cves) |
| 2026-10-16 BeyondTrust RS, 2026-10-16 PeerStitch | `cisa-kev` status and tag missing | Both CVEs entered KEV on 2026-10-16 | internal records |
| 2026-10-10 AhsayCBS | CVSS 4.0 figures no cited source carries | — | internal record (dropped) |
| 2026-10-09 Publica PK | "the funds" overstated | Inside IT: "some of the funds" | internal record |
| 2026-10-13 Danfoss AK-SM/AK-SC | Defender takeaway's wording beyond the evidence quote | CERT-FR: removing the compromised instance's persistence | internal record |
| 2026-10-14 Exchange October SU | Two evidence quotes no longer on the cited page | Microsoft replaced the banner on 2026-10-16 with a link to its follow-up post | internal `improvement` record re-pointing the evidence to the follow-up post |

Root causes: publisher revisions after publication (Bricksforge, SonicWall's Previdian count, Exchange, Ivanti's CVE record, Rank Math's later CVE, two KEV listings after the entries were filed) account for seven of the fourteen. The rest are the known composition drifts: a sentence that interprets where the source states (PaperCut regressions, Copeland "zero interaction"), and an unreadable source left standing in an earlier pass (Citrix community blog, Copeland's CISA advisory, readable since v4.18's CSAF recipe).

## Findings — missing or incomplete coverage

- **Recovered (1):** Netcraft, 2026-10-16, ICS calendar-invite phishing that Outlook with Exchange Online and Gmail add to the calendar without a click and keep after the email is deleted, the delivery path of EvilTokens device-code phishing. The 2026-10-16 fire attempted Netcraft and returned nothing on it. Published as `entries/2026-10-19/ics-calendar-invite-phishing-auto-added-outlook-gmail.md` (notable); `tool:eviltokens` registered.
- **Correctly droppable:** every other in-week item the four re-sweeps listed (G1 14 in-week items, among them the October Patch Tuesday, Exchange OOB, Juniper, Fortinet, SAP and Oracle CPU; G2 the Safepay DD-Automation and Arcadia incidents; G3a/G3b UAT-6275, ARTEX, QuartzLine, Aoki, YAM Store) carries a covered entry or a `borderline-drop` line with its reason in a week's run record.
- **KEV:** all nine additions of the week are covered (`work/2026-10-18T1307Z-audit/kev-window.txt`); no RANSOMWARE row.
- **Backlog:** one open row (Beyond Gravity, expires 2026-10-20); G2 re-checked it: no vector, behaviour or data class is public, so it stays held on its named condition.

## Findings — systemic / operational

1. **Session budget.** The fire ran 22 spawns before v4.21 existed, two above the new 20-spawn bound. Under v4.21 the budget was spent on resumption, so the closing loop ran as the hard-invariant minimum: one verifier spawn on this fire's changed claims (NEEDS_FIXES, four truth findings, all fixed after the pass and not re-verified, residual 4), then a forced cut recorded in `verification.budget_cut`. Seven of the 22 spawns (D1 to D3, L and its continuation, and the legacy-updated passes T4 and T5) were secondary work that v4.21 now reserves for operator-directed partial audits.
2. **Publisher revisions dominate the week's defects** (7 of 14). The weekly truth pass catches them; nothing in the intel fire can.
3. **Main-analysis growth through updates** (carried): long-lived entries grow past the 550-word limit through supersession rewrites; the length check covers new entries only. Watch item.
4. **Gate false positives** (carried to the secondary fire): `quote-literal` misreads literal angle-bracket text, "(opens in a new window)" labels and meta-only post text; `citation-cve` reports "does not mention" on an image-only PDF. A tool fix is drafted and held for the operator-directed fire.
5. **Model baseline** (Sonnet 5 → 5.5 at `xhigh`): median fire 153 → 148 min; mean verifier iterations 7.3 → 5.2; confirmed-CLEAN 3/9 → 6/18; iteration-1 truth findings per entry 0.77 → 1.53; research sub-agent median 9 → 22 min with 2.4 → 6.1 items. Recommendation: keep `xhigh` on the verifier and research roles (the finding rate doubled, which is the point of those roles); the main agent can try `high`.
6. **Calibration alarm:** `high` passed 8 of the week's 21 new entries (38%, alarm above about 25%). Re-graded against the `high` bar: Drupal SA-CORE-2026-014 fails it (unexploited, no public exploit, every known path through a contributed module) and moves to `notable`; GitLab CVE-2026-97229 is borderline (public PoC, unexploited, needs push access) and holds; the other six are exploited or carry a constituency nexus and hold. The monthly calibration section is in the 2026-10-11 report.

## Fixes shipped in this commit

- 15 existing entries carry a record from this fire (the table above plus Drupal's priority move), 1 recovered entry, 3 registry records (`tool:eviltokens`, plus `product:google-calendar` and `product:microsoft-exchange-online`, which `sync_products.py` created for the new entry's affected products), 5 `cves_seen` rows.
- ATT&CK pin moved to v20.0 (`python3 tools/attack_data.py --update`; selftest clean).
- Warning sweep: one new acknowledgment, `2026-10-11T1307Z-audit: duration_seconds=713500` (the 198.2 h spans that fire's eight-day pause on an API session limit; its own record says so).

## Recommendations (operator decisions, not shipped)

1. **Run the deferred secondary work as one operator-directed partial audit** after this one is live. It holds the out-of-week findings below plus the gate fix of systemic 4. Budget it as v4.21 says: one fire, at most 20 spawns.
2. **Unexploited critical vendor bundles** (carried from 2026-10-11).
3. **Legacy repair pace** (carried from 2026-09-30).
4. **Non-adversarial items** (carried from 2026-10-11).
5. **Red Canary** (carried from 2026-10-11).
6. **`ssd-disclosure`** (carried from 2026-10-11).
7. **Google TAG and Mandiant/GTIG overlap** (carried from 2026-09-29).
8. **Effort settings:** per systemic 5, try `high` on the main agent; keep `xhigh` on research and verifier.

Retired: 2026-10-11 recommendation 3 (the 10-04 audit did not fire): v4.21's one-audit-at-a-time claim answers it.

## Carry-forward (out of scope for this week)

The early passes of this fire verified 188 entries outside the week before the scope was cut: 43 clean, 68 with imprecisions, 77 with factual errors, most of them legacy entries and duplicate groups (D1 to D3, L). The defects and the fixes they need are recorded in `work/2026-10-18T1307Z-audit/truth-{T1,T2,T4,T5,T6a,T7,T8a,T8b,T9,D1,D2,D3,L}.yaml` and `fetch-worklist.md`; none is applied here. They are the first input of recommendation 1. Sixteen of the factual-error entries sit outside the legacy and duplicate batches (passes T1 to T9, filed 2026-05-18 to 2026-10-10); take those first.

## Watch items

- **Legacy queue.** Unchanged at 408 pending (no legacy work ran). Resolution: queue empty.
- **Non-CVE duplicates** (carried). Resolution: folded or linked.
- **Nightmare Eclipse 2026-05-30** (carried; D1 found it wrong again). Resolution: re-verified and rewritten.
- **`webfetch-only` sources and their quotes** (carried).
- **Publisher revisions** (carried, sharpened): seven of this week's fourteen defects. Resolution: the weekly pass keeps catching them.
- **Beyond Gravity backlog row**, expires 2026-10-20. Resolution: dispositioned by the fires.
- **Out-of-week findings** (new): Resolution: applied by the operator-directed partial audit of recommendation 1.
