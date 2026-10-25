# Quality audit — 2026-10-25

**Run record:** [runs/2026-10-25/2026-10-25T1308Z-audit.md](../../runs/2026-10-25/2026-10-25T1308Z-audit.md) · **Prompt:** v4.24 · **Window:** 2026-10-18T13:07Z → 2026-10-25T13:08Z (the trailing week since the 2026-10-18 audit)

## Method

Scheduled weekly audit, claimed on `main` before the first spawn (`work/2026-10-25T1308Z-audit/audit.claim`, base `2582170`). An open partial claim from cleanup wave 05 (`2026-10-21T1147Z-audit`, `wave=05`, nothing pushed since 2026-10-21) was ignored under Phase 0 step 2.

- **Scope:** 36 entries with activity from the week's seven intel fires (27 filed in the week, 9 older entries the fires updated), each read whole. Three narrow checks covered the fixes the 2026-10-18 audit applied after its only verifier pass (Copeland, Bricksforge, ICS calendar invites).
- **Out of scope (v4.22):** 187 entries whose only in-window activity is records of the cleanup waves 01 to 04 (2026-10-20T0835Z 12, 2026-10-21T0800Z 69, 2026-10-21T1148Z 74, 2026-10-21T1149Z 23), of the 2026-10-18 audit (13) or of the 2026-10-11 audit (1); counts overlap.
- **Truth passes:** TA to TD, about 340 claims each (`work/2026-10-25T1308Z-audit/truth-T{A..D}.yaml`); each claim was checked against its freshly fetched cited source. The cited-page pre-pass (`page-checks.txt`) handed six quote leads to the passes.
- **Coverage re-sweeps:** G1 (vulnerabilities, 41 of 42 sources), G2 (incidents, region and policy, 37 of 37) and G3 (research blogs, 48 of 48), each one spawn.
- **Main-agent reads for the fixes:** Palo Alto's CVE-2026-109618 advisory and timeline, QNAP QSA-26-18 and statement, Synology-SA-26:14, HPE's HPESBNW05162 CSAF and text advisory, the Debian tracker and DSA feed, Oracle's October CPU matrices, Horizon3, Microsoft's LiteLLM analysis, Help Net Security, VulnCheck, n8n, Anaconda, VenariX, BleepingComputer, Cyberattaque.org, French Breaches and Cisco's Snort 3 advisory.
- **Budget:** 13 of 20 spawns: 7 before the verifier loop (4.48 M sub-agent tokens) and 6 verifier passes, 7.27 M tokens in all (`budget.tsv`). Iterations 5 and 6 returned a confirmed CLEAN.

## Verdict

**14 of 36 entries clean, 17 with imprecisions only, 5 with factual errors.** Two of the five went stale after the entry's last record: Palo Alto's advisory revision at 05:25Z on 2026-10-25 listed the first PAN-OS hotfixes as released, after that day's fire had read the advisory, and Debian fixed trixie on 2026-10-21 (DSA-6575-1, per Debian's DSA feed). The other three are composition errors. Every exploited flaw and KEV listing of the week has an entry or a recorded drop. The re-sweeps found one gap that clears the gate: QNAP's and Synology's PHP2Shell advisories, recovered as a new entry. Two findings change a reader's patch decision: the first PAN-OS hotfixes are now installable, and the HPE affected ranges named three AOS branches the vendor does not list (HPE presumes end-of-maintenance versions affected instead).

## Findings — false or erroneous published intelligence

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| 2026-10-23 HPE Aruba HPESBNW05162 | All 19 CVE records and the analysis said the CSAF lists wider ranges (10.6, 10.3, 8.12); 34 at CVSS 9.0+, eleven at 9.6, 15 adjacent | CSAF ranges start at 10.8.0.0, 10.7.0.0, 10.4.0.0, 8.13.0.0, 8.10.0.0; 33, ten, 14; HPE presumes end-of-maintenance versions affected. The truth pass also doubted the hardware-model note in the Exposure line; HPE's bulletin page carries it, so it stays | `correction` with section |
| 2026-10-18 ConnectWise SkyKick | Microsoft's 2,900-a-minute figure bound to the ARTEX sign-ins to 2,250+ tenants, in the analysis and a spliced evidence quote; "twice daily" cadence stale | 2,900 a minute is the peak of failed logons in the separate 10 to 14 October spray | `correction` with section |
| 2026-10-22 PAN-OS PHP2Shell | Title, headline, status, fixed ETAs and takeaway still said no fixed build and gave 2026-10-26 for the first hotfixes | Revision of 2026-10-25 lists 10.2.18-h13, 11.1.16-h4, 11.2.10-h16 "as these versions are released" (the solution text still says upcoming); rest 10/27 to 10/30; Palo Alto's current analysis finds no impact of CVE-2026-115560 on PAN-OS | `update` with section |
| 2026-10-20 nginx heap flaws | Headline, summary, Exposure and action said Debian trixie still vulnerable | DSA-6575-1 (2026-10-21) fixed trixie (1.26.3-3+deb13u10); bookworm still vulnerable | `update` with section |
| 2026-10-22 LiteLLM 1.107.0 | Aikido quote two words short | "PyPI has now quarantined and removed version 1.107.0." | folded into this fire's `improvement` (below) |
| 2026-10-12 Bricksforge (narrow check) | Previdian quote spliced "Yes." onto a reworded sentence | "Previdian lists it as a known exploited vulnerability." | internal `correction` |
| 2026-08-09 Metabase | "First" victims; CVE "assigned by the advisory"; KEV due date cited to a page without it; victim detail cited to a since-revised VenariX page; Bits of Gold date; Shipup hedges dropped; T1552.001 | No source says first; CVE now tracked, KEV listing cited; detail re-cited to n8n, BleepingComputer, Anaconda; 2026-08-16; "linked to", "possible", the outlet's reading | `correction` with section |
| 2026-09-28 Citrix CVE-2026-88771 | `affected` said all releases; "no public attribution exists" | Citrix lists 14.1 and 13.1 only; Mandiant's CTO called the initial CVE-2026-88772 intrusions likely state-sponsored (reported 2026-09-30) | `improvement` with section |
| 2026-10-21 Oracle October CPU | No mention of CVE-2026-101767 (EBS, 9.8, pre-auth), whose chain Horizon3 published on release day | Oracle matrix row; Horizon3 write-up with mitigation and indicators | `improvement` with section; CVE added to `cves_seen` |
| 2026-10-22 LiteLLM 1.107.0 | Microsoft's analysis of 2026-10-23 (Windows and macOS execution, do-not-start-Python response) missing | The 2026-10-24 fire found it and left it out of the record | `improvement` with section |
| 2026-05-30 PAN-OS CVE-2026-0257 | CWE-565 and a TLS-handshake step cited to Rapid7; Unit 42 quote predates a copyedit | CWE is Palo Alto's; Rapid7 has no handshake step | `correction` with section |
| 2026-10-21 TeamUpdraft | Must-use check cited to Patchstack and Nethemba; AI suspicion called unsupported | TeamUpdraft's own guidance; it names exploit speed and faulty plugins as its basis | `improvement` with section |
| 2026-10-13 Danfoss | Forescout's attacks "mostly by" two groups | "the most active groups" | internal `correction` |
| 2026-10-21 PHP2Shell | VulnCheck quote edited on the page; PAN-OS dates stale; Publica label date | Live wording; hotfixes due by 2026-10-30; status block 22.10.2026 | internal `improvement` |
| 2026-10-20 Siemens, 2026-10-23 Arista, 2026-10-15 Collabora | KEV listings (2026-10-20, 10-23, 10-23) not in status or tags | KEV catalogue | internal `improvement` records |
| 2026-10-22 k0t | CVSS empty on two CVE records | Fortinet FG-IR-25-910 9.8, FG-IR-19-007 4.3 | internal `improvement` |
| 2026-10-23 BlackX | CVE-2022-21894 mitigation attributed to KB5025885 (a CVE-2023-24932 article) | Kaspersky on the PCA 2011 revocation | internal `improvement` |
| 2026-10-23 MythicRatatoskr | Triage conclusion under ESET's citation | ESET states the observations only | internal `improvement` |
| 2026-10-23 NetScaler PHP2Shell | Source dated 2026-10-22 | Published 2026-10-21 22:23 CEST | internal `improvement` |
| 2026-10-06 Atlassian | Headline 133 characters | — | internal `improvement` (headline only) |

The LiteLLM GitHub issue quote, another pre-pass lead, is verbatim in a maintainer's comment (truth pass TC). The sixth lead, Google's Pixel bulletin quote on the out-of-scope CVE-2026-58704 entry, is left: the container still receives a copy of the page from before Google's 2026-09-30 revision, as cleanup wave 02 found. Declined with reason: Publica's 2026-10-08 label on an undated lede (the 2026-10-13 record already cites the page as read); OVHcloud's extension name and temp folder (the compromised component and the vendor's own host check, not a hash, address, domain or rule); eMudhra's and PHP's stale wording in append-only record summaries (the current text is right); Cisco CVE-2026-20236 at 9.0 (Cisco's advisory defines it as the class maximum; the 7.5 sits only in the CVE record API, which may not be cited); nginx CNA scores and the Plus range (same API only); Atlassian's paragraph-1 restoration (the takeaway and newest section carry it).

**Root causes.**
- *Revisions after publication: 7 entries, plus the revised parts of 2 more.* The 7 are PAN-OS PHP2Shell, nginx, PHP2Shell, Citrix CVE-2026-88771 (Mandiant's statement came about a day and a half after filing), eMudhra, and the Arista and Siemens KEV listings; the Collabora KEV listing is the same defect on an entry outside the week's scope. The 2 are PAN-OS CVE-2026-0257 (Unit 42 copyedit) and Metabase (VenariX revision). The weekly truth pass is the only mechanism that catches them.
- *Composition: 13 entries.* The worst is HPE, where a CSAF misread produced ranges the vendor never published. ConnectWise bound a figure to the wrong activity, and three citations were mis-attributed (PAN-OS 0257, TeamUpdraft, Mythic). Three quotes were not verbatim (ConnectWise, LiteLLM, Bricksforge). They passed fires that run the `quote-literal` check, which only judges pages a direct transport reads; the fires' gate outputs are not saved, so whether the pages were unreadable then or the verifier missed the quotes is not established. The 2026-10-24 fire dropped Microsoft's LiteLLM analysis at composition although its own findings carried it.

## Findings — missing or incomplete coverage

- **Recovered (1):** QNAP QSA-26-18 and Synology-SA-26:14 (2026-10-22). PHP2Shell reaches the QTS, QuTS hero and QuTScloud web components before authentication. Fixed builds are dated 2026-10-23; Note Station 3, QNE, QVR Surveillance and TVR OS are still unfixed, and QuMagie is listed as affected without a fix row. QNAP saw scanning and exploitation attempts against the PHP flaws. Published as `entries/2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed.md` (notable). Cause: no source record covered either vendor's PSIRT. Both are now candidates.
- **Developments recovered as records:** Palo Alto's 2026-10-25 revision, Debian DSA-6575-1, Microsoft's LiteLLM analysis, Horizon3's EBS chain (table above).
- **Correctly droppable:** Plex2Shell (four KEV CVEs) and SiteGuard (KEV), as the fires judged; the Sophos SSPR-vishing intrusion (three SSPR-abuse entries already cover the technique); Acronis on The Gentlemen locker; Zscaler on the ARTEX operator side; Microsoft's CVE-2026-70197 revision text; Pillow 13.0.0, BIND CVE-2026-94300, Traefik, EDK2 PXE, the Drupal contrib batch and Chrome 156 (unexploited, regular cycle); Kroll and Nord Security statistics; and below the incident floor, Loxone, Medienwerkstatt, the AfD leak, Ircantec, Alliance Police Nationale, GoDaddy's revocations and the Cyberhebdo municipal incidents.
- **KEV:** eight additions since 2026-10-18. Three are covered; five (Plex ×4, SiteGuard) carry borderline-drop lines in the 2026-10-21 fire. No COVERED-STALE row, no RANSOMWARE row.
- **Backlog:** one open row (ARX Group SA, Aurora leak-site claim, held to 2026-11-07 on a named condition). G2 found no victim, client or press statement, so it stays held.
- **Rotational lookback:** no sweep or rotation defect. msft-ti was swept on 2026-10-24 and saw the Microsoft post (a composition drop); the QNAP and Synology miss was a source-list gap; Palo Alto's revision came after the last fire had read the advisory.

## Findings — systemic / operational

1. **Analyses grow through updates (confirmed; carried watch item).** 18 of the 37 entries active in the window (the 36 in scope plus Check Point) were over the 550-word bound and two headlines over 120 characters, all grown through records: the PHP2Shell `critical` entry at 2,061 words, Danfoss at 1,291, Publica PK at 1,161. The `entry-shape` length check read new entries only. Fixed in v4.24 (below). The 18 entries are not rewritten here (see Recommendations).
2. **Verifier convergence.** None of the seven intel fires reached a confirmed CLEAN. Iterations were 3/4/7/8/5/3/7: six published on the low-residual early exit, one at the cap with residual 5 (2026-10-22). The single CLEAN of the week (2026-10-21 iteration 6) was refuted by iteration 7. This is the shape the double-CLEAN gate allows. This week 22 of 36 entries carried a defect, against 13 of 29 last week.
3. **Calibration alarm.** `high` is 11 of the 36 in-scope entries (31%), but only 3 of the 27 new ones (11%, down from 38% last week). Every `high` was re-graded against the bar. All hold: exploited edge and application flaws, the Publica PK incident, the ConnectWise and TeamUpdraft compromises, Danfoss under NCSC.ch's exploitation rating, and Fortinet's out-of-cycle edge fixes. No priority moved.
4. **Discipline.** `actions[]`: 9 of 27 new entries empty, the rest one to three concrete, finding-derived tasks; none generic. Technique density: threat 16.1, incident 7.0, vulnerability 1.9 (unchanged shape). `exploitation-consistency` passes over the window. Registry: 133 records added between the window start and this fire, 105 of them products (143 and 115 with this fire's ten product records). One duplicate (`product:chromadb`) tombstoned onto `product:chroma`. No duplicate actor key: APT28 had no actor record before 2026-10-21, and TA458 is Proofpoint's distinct designation.
5. **Sources.** `source_health` (09:16Z) listed three `needs-content-fix` records. securityweek moved to its working feed. ox-security's miss was transient (the feed reads). connectwise-trust-center flaps between readable and 403; it stays `blocked` with the status-page substitute. No record carried the `webfetch-only` verdict. The re-sweeps' recipe notes are written to nine source records.
6. **Telemetry.** Seven daily fires at about 02:56Z with a 24 h gap each and no coverage hole. Durations were 1.6 to 4.5 h, and every record is `publish_status: ok`. The jina pool (context) has 7 of 10 keys live.
7. **Tooling.** `kev_window_diff.py --since` crashed on the window-start timestamp the audit prompt passes; fixed. This fire's truth-pass brief named ledger files with a `T` prefix the ledger script does not write; each pass found its file.
8. **Fix effectiveness (2026-10-18 audit).** The ATT&CK pin holds at v20.0 (`--check` up to date). Its acknowledgment still matches. All four of its post-pass fixes that no verifier re-read hold (Citrix, Copeland, Bricksforge, ICS calendar invites). The narrow Bricksforge check also confirmed a pre-pass lead, a spliced Previdian quote, now fixed. The calibration alarm cleared on new entries (38% → 11%). The publisher-revision watch item recurred, as expected.

## Fixes shipped in this commit

- **v4.24** (`prompts/cti-run.md`, `prompts/quality-audit.md`, `prompts/CHANGELOG.md`): an update rewrites the analysis in place and keeps it within the bound.
- **`tools/check_run.py` `entry-shape`:** WARNs when a fire's record grows an existing entry's analysis past the bound or lengthens its headline past 120 characters. This fire's own records tripped it four times; all four were trimmed or reverted before the gate passed. A test was added in `tools/test_check_run.py`, and `docs/pipeline.md` is updated.
- **`tools/kev_window_diff.py`:** `--since` accepts a timestamp.
- **Records:** 21 entries carry one record each (6 corrections, 2 updates, 13 improvements; 11 internal). There is 1 recovered entry. 10 product records came from `sync_products.py`, plus the `product:chromadb` tombstone. `state/cves_seen.json`: CVE-2026-101767 added and 46 `last_seen` dates bumped.
- **Sources:** securityweek recipe; notes on ox-security, connectwise-trust-center, msft-ti, cert-lv, inside-it-ch, news-admin-ch, bsi-de, enisa-euvd, drupal-security, chrome-releases and citizen-lab; candidates semperis-research, qnap-security-advisories and synology-security-advisories.
- **Warning sweep:** one new acknowledgment, `2026-10-21T1148Z-audit: duration_seconds=89772`. Cleanup wave 04 spanned two session-limit stops and an overnight idle, and its own notes say so. `check_run.py --all` ends 0 warn · 0 fail, and `site/build.py` emits no self-check warning.

## Recommendations (operator decisions, not shipped)

1. **Bring the 18 over-length entries back within the bound** as a cleanup-program row. Each needs a rewrite verified claim by claim, which is more than a weekly audit's budget holds; v4.24 stops further growth.
2. **Save the gate output of every fire** (`check_run.py ... | tee work/<run-id>/gate.txt`), so an audit can tell an unreadable page from a verifier miss when a non-verbatim quote surfaces later.
3. **Unexploited critical vendor bundles** (carried from 2026-10-11).
4. **Legacy repair pace** (carried from 2026-09-30); the cleanup program reports 308 pending.
5. **Non-adversarial items** (carried from 2026-10-11).
6. **Effort settings** (carried from 2026-10-18): try `high` on the main agent; keep `xhigh` on research and verifier.

Retired: 2026-10-18 recommendations 1 (the cleanup program now runs the deferred secondary work), 5 to 7 (decided by cleanup wave 01 and noted on the source records).

## Watch items

- **Publisher revisions** (carried): 7 of this week's 22 defective entries, and parts of 2 more. Resolution: the weekly truth pass keeps catching them.
- **Over-length entries** (new, from systemic 1): 18 entries. Resolution: recommendation 1 done, or each rewritten by later records.
- **Cleanup wave 05 claim** (new): open since 2026-10-21 with no push. Resolution: the wave publishes or the claim is withdrawn.
- **connectwise-trust-center** (new): flaps between readable and 403. Resolution: a stable recipe, or the status-page substitute recorded as its working route.
- **ARX Group SA backlog row:** held to 2026-11-07. Resolution: a victim, client or press confirmation, or expiry.
- **Mini Shai-Hulud (2026-05-13) and the Nx Console cascade (2026-05-28)** share CVE-2026-45321 without a link. Both are in-window only through cleanup records; the later entry sits in open row W4-15 (wave 06). Resolution: linked or folded by wave 06.
- **Legacy queue, non-CVE duplicates, out-of-week findings** (carried): owned by the cleanup program (`docs/cleanup/STATUS.md`).
- **Closed this week:** Nightmare Eclipse 2026-05-30 (rewritten by cleanup wave 03), the Beyond Gravity backlog row (struck at expiry on 2026-10-20; G2 found no new disclosure).
