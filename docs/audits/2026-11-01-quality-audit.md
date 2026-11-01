# Quality audit — 2026-11-01

**Run record:** [runs/2026-11-01/2026-11-01T1312Z-audit.md](../../runs/2026-11-01/2026-11-01T1312Z-audit.md) · **Prompt:** v4.24 · **Window:** 2026-10-25T13:08Z → 2026-11-01T13:12Z (the trailing week since the 2026-10-25 audit)

## Method

Scheduled weekly audit, claimed on `main` before the first spawn (`work/2026-11-01T1312Z-audit/audit.claim`, base `7eda38f`). The open partial claim of cleanup wave 05 (`2026-10-21T1147Z-audit`, `wave=05`) was ignored under Phase 0 step 2.

- **Scope:** 54 entries with activity from the week's seven intel fires (35 filed in the week, 19 older entries the fires updated), each read whole.
- **Out of scope (v4.22):** 16 entries whose only in-window activity is records of the 2026-10-25 audit, which its own verifier loop checked.
- **Truth passes:** TA to TF, 244 to 301 claims each, 1,651 in all (`work/2026-11-01T1312Z-audit/truth-T{A..F}.yaml`). Each claim was checked against a freshly fetched cited source. The cited-page pre-pass (`page-checks.txt`) handed three leads to the passes and left four on out-of-scope entries.
- **Coverage re-sweeps:** G1 (vulnerabilities, 46 of 46 sources), G2 (incidents, region and policy, 42 of 42) and G3 (research blogs, 45 of 45), each one spawn.
- **Main-agent reads for the fixes:** Belden PSIRT-10, Schneider SESB-2026-295-01, Wibu-Systems, Wordfence Intelligence, CIQ, Ubuntu, Red Hat, Adobe APSB26-162 and APSB26-73, the MSRC update-guide API, Edge release notes, Morphisec, GitGuardian, KAIO Bern, Datadog, Zscaler, Palo Alto, NCSC Switzerland post 13105, Siemens, The Hacker News, Broadcom VMSA-2026-0006, Infosecurity Magazine, GitLab, Ruby, dotnet/announcements #495, privatim, the KEV catalogue. They are under `work/2026-11-01T1312Z-audit/deep/`.
- **Budget:** 13 of 20 spawns (six truth passes, G1 to G3, four verifier passes), 6,885,964 sub-agent tokens: 4,748,994 before the verifier loop and 2,136,970 in it (`work/2026-11-01T1312Z-audit/budget.tsv`). Verification: four passes; iterations 1 and 2 NEEDS_FIXES (remediated), iteration 3 CLEAN, iteration 4 (confirmation) NEEDS_FIXES with no truth finding and two editorial ones, applied; published on decision rule 5 with residual 2.

## Verdict

**30 of 54 entries clean, 22 with imprecisions only, 2 with factual errors.**
- The two factual errors:
  - The Joomla Gridbox analysis still said there was no exploitation signal and that the cookie name was withheld, two weeks after its own update sections recorded both.
  - The PHP2Shell OT entry said NetModule NRSW had no fix while Belden's advisory names 5.0.0.105.
- Most imprecisions are publisher revisions made after an entry's last record:
  - Wordfence assigned a CVE.
  - CIQ shipped kernels.
  - Broadcom added 8.0 U2f and 7.0 guidance.
  - NCSC Switzerland and CISA confirmed exploitation.
  - Siemens named an upgrade path.
- Composition errors are fewer than last week:
  - a wrong fixed-version set (.NET CVE-2026-114148);
  - Python releases listed as protected that predate the denylist;
  - a cited page that does not carry the CVE it is cited for (Ivanti);
  - an unsupported "standard" qualifier (privatim).
- Every exploited flaw and KEV listing of the week has an entry. The re-sweeps found six developments on covered findings, published as records, and nothing that needed a new entry.
- Changes to a reader's patch or hunt decision:
  - NRSW now has a fix.
  - Campaign Classic build 9402, the fix the store gave, is affected again (APSB26-162).
  - Microsoft added Edge to the exploited Windows Shell flaw's fix list.
  - GhostAction now reaches developer machines through a VS Code task and leaves cron persistence that survives cleaning the repository.

## Findings — false or erroneous published intelligence

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| 2026-07-26 Joomla Gridbox | Analysis: "no public exploitation signal", cookie name withheld; October 2025 treated as the start of exposure; CVE record's 9.4 not surfaced; Membership Pro typed RCE; Balbooa "had advised" rules; "returns HTTP 200"; headline 139 characters | mySites.guru 2026-07-29 prints the cookie and reports the follow-up batch exploited; "at least nine months … probably far longer"; record 9.4 on PR:H; CVSS 3.1 9.1, not RCE by default | `correction` with section; analysis 572 → 522 words |
| 2026-10-27 PHP2Shell OT products | NRSW "no patched release"; Schneider list without Foxboro DCS H90; Wibu 5.2.2 | Belden PSIRT-10 v1.1: upgrade to 5.0.0.105; SESB v3.0.0 (2026-10-28) adds H90 with a port-blocking mitigation; Wibu 5.2.3 (2026-10-29) | `update` with section |
| 2026-10-30 WordPress 7.1.4 | Title, summary and body: no CVE assigned | Wordfence CVE-2026-119977 (CVSS 3.1 8.1), published 2026-10-31 | `correction` with section; CVE added to `cves_seen` |
| 2026-10-31 Linux TCP/MPTCP | No CIQ kernel; upstream fixed list of four | CIQ kernels for LTS 9.6, 9.2, 8.6 and FIPS 9.6/9.2 (2026-10-31); stable backports 5.10.272, 5.15.223, 6.1.190, 6.6.159; Red Hat now 9.8 | `update` with section |
| 2026-07-30 VMware VMSA-2026-0006 | Fixed builds without 8.0 U2f and the 7.0 path; Infosecurity "same assessment", dated 08-14; KEV ransomware flag not stated; vector `local` on two flaws; "independent researcher"; a file-extension indicator; pipeline wording | Broadcom .1 (08-03) and .2 (08-19); Infosecurity 2026-08-13 reports only a suspected APT; KEV `knownRansomwareCampaignUse: Known`; AV:N/PR:H; Maxim Suhanov | `correction` with section |
| 2026-05-15 Linux CVE-2026-46300 | 10-29 section: Dream "does not name the vendor"; Exposure without PAN-OS; KEV text paraphrased beyond its words | Dream (updated 10-29) names PAN-OS; Unit 42: patched customers not affected | `correction` with section |
| 2026-10-24 Node2Shell | 10-26 section's "no source reports exploitation" left standing after KEV; NCSC status "unknown"; ELLIO as the only telemetry; Prisma Transporter missing | NCSC 13105 updated 10-29 to actively exploited; Zscaler decoys: 402 events from 20 sources in the first day; Palo Alto lists Transporter Client < 0.2.9 | `correction` with section, plus Datadog's detection layers (G3) |
| 2026-10-26 .NET Brotli | CVE-2026-114148 fixed "10.0.14, 11.0.0-rc.3"; crash clause uncited | dotnet/announcements #495: tarballs 8.0.33/9.0.22, source-built SDKs 8.0.133, 9.0.123, 10.0.114, 10.0.403, 11.0.100-rc.3; JFrog .NET crash | `correction` with section |
| 2026-10-21 eMudhra | 10-25 section: Python 3.15.1, 3.14.9, 3.13.17 patched; uncited build-string sentence; Oracle quote | Python Insider: denylist in 3.15.2, 3.14.10, 3.13.18, 3.12.16, 3.11.18; Oracle page reworded (publisher edit) | `correction` with section |
| 2026-10-13 GitLab CVE-2026-97229 | "No earlier branch"; GitLab-only scope; title 280 characters | CVE-2026-110264 from 7.0, backports 19.1.9, 19.0.10, 18.11.13; Ruby: any app compiling attacker regexes, fixed in 4.0.9, 3.4.12, 3.3.13 | `improvement` with section |
| 2026-10-14 Ivanti Connect Secure | CVE id cited to an Ivanti blog that does not carry it (pre-pass lead); step binding cited to GHSA; 10-31 rewrite dropped Volexity's on-appliance checks | Volexity ties the first two steps to CVE-2026-104935; /tmp and memory forensics | `improvement` with section |
| 2026-10-31 Broadcom PHP2Shell | "CloudSOC SpanVA and CASMA have none" | Umbrella 39404 lists no fix; per-product pages need a login | `correction` with section |
| 2026-10-21 PHP release | Siemens "only through customer support"; THN "carries no correction"; Karimi "first" | SSA-566512 V1.1 (10-28): upgrade to the available PAN-OS version; THN retraction note; Hunt.io puts watchTowr's 10-21 report earliest | folded into this fire's `update` (Morphisec, below) |
| 2026-09-30 Apple CoreGraphics | "among other devices" | Apple 149225 lists four device families | internal `correction` |
| 2026-10-22 PAN-OS PHP2Shell | Summary dates the exploitation statement to the 10-21 advisory | Statement came with the 10-27/28 revision | internal `correction` |
| 2026-10-29 Veeam | Summary: "Veeam reports no exploitation" | KBs carry no such statement; NCSC Switzerland relays it | internal `correction` |
| 2026-10-29 Trend Micro / Quest / NetApp | Title turned the ETA into a firm date; Trend citation dated 10-28 | KA-0024802 "Critical Patch ETA: Nov. 11"; status table of 10-30 | internal `correction` |
| 2026-10-30 privatim | "standard SaaS" | The Merkblatt says SaaS of large international providers; "standard" is DCOD's | internal `correction` |
| 2026-10-16 BeyondTrust | Rapid7 statement cited to BeyondTrust | Rapid7 2026-10-30 | internal `improvement` |
| 2026-10-30 VAPOR PANDA | Exposure and takeaway uncited | CrowdStrike 2026-10-29 | internal `improvement` |

Declined, with reason:
- Adobe Commerce Events ≤ 1.20.0 for CVE-2026-48356 (TE, low confidence): only the CVE record API binds that product to this CVE; APSB26-73 covers fourteen CVEs in one table, and the entry already says the table covers every fix.
- MDaemon/ClamAV CVE-2025-8088 KEV ransomware flag and CNA 8.4 score: these concern the WinRAR vector, not the ClamAV path the entry covers.
- WS_FTP mitigation for CVE-2026-90867: low confidence, and stated only in the CVE record API, which may not be cited.
- Joomla Gridbox `high` (TD, low-confidence F16): the in-window development is an unauthenticated SQL injection that reads the user table on every release, in an extension whose sibling flaws were exploited within days in July, so the `otherwise` limb holds.
- Linux CVE-2026-46300 T1611: Help Net Security's container-cluster risk statement supports it.
- Publica's "rather small" volume beside the 100 GB report: both sources are cited with their dates.

Publisher edits left as they are (gate leads): Siemens and Oracle reworded their pages after the entries quoted them. The Siemens quote is replaced by the current text, and the Oracle quote now follows the alert's current wording.

**Root causes.**
- *Publisher revisions after the entry's last record: 9 entries.* WordPress, Linux TCP, NetModule (Belden v1.1, Schneider v3, Wibu), VMware (August revisions never caught), Node2Shell (NCSC 10-29), Linux 46300 (Dream 10-29), PHP (Siemens, THN), Trend Micro and Ivanti. The weekly truth pass is still the only mechanism that catches them; the VMware revisions were three months old.
- *Supersession misses: 3 entries.* Gridbox and Node2Shell kept sentences that their own later sections disproved, and the Linux 46300 10-29 section kept "unnamed vendor" after the 11-01 record. The 10-28 Node2Shell record summary even says the earlier statement was replaced, but the text never was.
- *Composition: 6 entries.* .NET fixed versions, eMudhra Python versions, the Ivanti and BeyondTrust citations, privatim and the PAN-OS summary date.

## Findings — missing or incomplete coverage

- **Developments recovered as records (6):**
  - GitGuardian's GhostAction escalation of 2026-10-27 (G3, `update`).
  - Datadog's Node2Shell detection layers and Zscaler's first-day decoy telemetry (G3, folded into the correction).
  - Canton Bern's ICSG/IDSV in force from 2026-11-01, with Grundschutz BE due in Q1 2027 and the AGB ISDS BE contract terms (G2, `update`).
  - Microsoft's addition of Edge 154.0.4258.62 to the fix list of exploited CVE-2026-96951, revision 2 of 2026-10-26 (G1, `update`).
  - Morphisec's PHP2Shell post-exploitation on Windows IIS with PHP-CGI (G1, `update`).
  - Adobe's APSB26-162 of 2026-10-27, which leaves build 9402, the store's fix for Campaign Classic, affected by a pre-auth CVSS 9.8 SQL injection (G1, `update` on the 2026-10-02 entry).
- **Correctly droppable (G1 17, G2 12, G3 12):**
  - Vulnerabilities, unexploited and on the regular cycle: Contact Form 7 6.2.4, Sophos UTM CVE-2026-118633 (end of life, manual patch), TeamViewer, the Drupal contrib wave, Splunk, Mitel, Jenkins and others.
  - Incidents and claims without a vector, nexus or confirmation: SolNet, SIHF, SoftwareOne, Leipzig University, Fehmarnbelt, Verrières-en-Forez.
  - Policy items with no defender consequence: the Federal Council alerting dispatch, the e-evidence rule, the Geneva e-voting step, the EFK ZEMIS report.
  - Research with no constituency decision: ESET APT Activity Report Q2-Q3 (the 11-01 fire's drop is right), Talos VOLTA and NIK C2, Check Point Yoba, Elastic wesp.sys, Symantec AI relays, Group-IB MadApe, Microsoft's DPRK AI staging, Kaspersky's cloud isolation case, the MEP letter, Apple's notification wave, and Zimperium's Coruna and DarkSword counts.
- **KEV:** ten additions since 2026-10-25, all covered; no COVERED-STALE or RANSOMWARE row.
- **Backlog:** one open row, ARX Group SA (Aurora claim), held to 2026-11-07. G2 found no victim, client or press statement in DE, FR, IT or EN, so it stays held.
- **Rotational lookback:**
  - Three rotation defects:
    - Datadog's 10-29 post: `datadog-security-labs` was never swept after it became a candidate on 10-26.
    - Morphisec's 10-28 post: last swept at 02:56Z that day.
    - Adobe's APSB26-162: last swept at 02:56Z on 10-27, before the bulletin.
  - One sweep defect: Zscaler's 10-28 post was inside the lookback of the 10-29 fire, which swept `zscaler-threatlabz` and did not use it.
  - Two source gaps: GitGuardian (now a candidate) and KAIO Bern.
  - One recipe gap: MSRC revisions reach no feed. G1 found Edge through the update-guide API's `latestRevisionDate` filter, which is now noted on the source record.

## Findings — systemic / operational

1. **Verifier convergence (carried; worse).** None of the seven intel fires reached a confirmed CLEAN.
   - Iterations per fire: 3, 4, 8, 8, 4, 3, 8.
   - Three fires reached the cap. 2026-10-28 published on a CLEAN at iteration 8 with the confirmation waived. 2026-10-29 published at residual 5, and 2026-11-01 at residual 3.
   - Three single CLEANs were refuted by the next pass (2026-10-29 iterations 5 and 7, 2026-11-01 iteration 5).
   - Defect rate: 24 of 54 in-scope entries carried a defect, against 22 of 36 last week.
2. **Publisher revisions (carried watch item).** 9 entries this week, including two Broadcom revisions from August that no fire or audit caught. Fires re-read a covered advisory only when something new surfaces on it.
3. **Calibration alarm.** `high` is 11 of 54 in-scope entries (20%) and 2 of 35 new ones (6%). This is below the alarm level, so there was no re-grade. No truth pass raised an F16 except the low-confidence Gridbox one, declined above.
4. **Discipline.**
   - `actions[]` on new entries: 10 empty, 24 with one action, 1 with two; none generic.
   - Technique density on new entries: threat 8.0, incident 2.8, vulnerability 1.5.
   - `exploitation-consistency` and the new-entry `entry-shape` checks pass over the window.
   - Registry: 79 records added between the last audit and this fire, 51 of them products, plus one product record from this fire. Volt Typhoon was keyed for the first time (no earlier actor record), and no ambiguous label surfaced.
   - No CVE-sharing pair in the window lacks a `references[]` link.
5. **Sources.**
   - `sans-isc` read as irrelevant because its feed titles are terse. It is set to `content_scope: general-news`, and freshness is still judged.
   - `ico-uk` is a transport outage, the same as on the 11-01 fire; it is not demoted.
   - `ssd-disclosure` failed at 11:24Z and read cleanly at 14:05Z.
   - `connectwise-trust-center` still flaps and stays `blocked`.
   - No record carried `webfetch-only`.
6. **Telemetry.** Seven daily fires at about 02:56Z, each with a 24 h gap and no coverage hole. Durations ran 2.0 to 6.9 h, and every record is `publish_status: ok`. The jina pool (context only) has 6 of 10 keys live, with a balance of about 46.8 M. G3 saw `extract` fall through to the reader seven times on Dark Reading; that is noted on the record.
7. **Fix effectiveness (2026-10-25 audit).**
   - v4.24 took: no in-window record grew an analysis past the bound. Records shrank PHP (2,059 → 1,944), PAN-OS (652 → 551), Ivanti (630 → 550) and GitLab (711 → 676).
   - The `kev_window_diff.py --since` fix ran cleanly in Phase 0.
   - Recommendation 2 (keep each fire's gate output) was not adopted; it ships now in the tool. Three of this week's four page-check quote leads were publisher rewordings, which a gate log would have shown at the time.
   - The ATT&CK pin is current (v20.0).

## Priority calibration

No November report carried this section, so this fire owns the monthly review.

| Scope | n | critical | high | notable | routine |
|---|---|---|---|---|---|
| Store | 1,052 | 30 (2.9%) | 376 (35.7%) | 588 | 58 |
| September 2026 (2026-10-11 audit) | 128 | 13 (10%) | 36 (28%) | 66 | 13 |
| October 2026 | 117 | 6 (5%) | 22 (19%) | 81 | 8 |
| This window, new entries | 35 | 0 | 2 (6%) | 28 | 5 |

**Movement.** October's `high` share fell from 28% to 19% and `critical` from 10% to 5%. The store-wide share fell from 41% (2026-10-11) to 35.7% as the cleanup waves re-graded legacy entries.

**F16.** The month's run records carry 29 F16 findings:
- 15 on intel fires: 6 fixed in the fire, 6 declined with reasons, 1 decided, 2 (2026-10-02) without a recorded outcome.
- 14 on audits and cleanup waves.

Both directions appear: a stale `critical` lowered (2026-10-10), `notable` raised to `high` (2026-10-15 for exploited software, 2026-10-21 for the Publica incident), and 68-day-old or no-vector incidents lowered (2026-10-07, 2026-10-11). The 2026-10-26 fire kept the PHP release entry `critical` after Unit 42's retraction. This audit's truth pass confirms the bar on independent ground: KEV on 10-26, honeypot and sensor shells through 10-31, Palo Alto's confirmed exploitation, and Dream's verified chain.

**Verdict:** no drift. The `high` bar is graded on constituency exposure, and the falling share reflects that. This week's exploited vendor-notice entries sit at `notable` with the reason stated, because no source shows constituency exposure (Drupal Commerce, Adobe Commerce). No calibration edit ships.

## Fixes shipped in this commit

- **Records:** 24 entries carry one record each: 7 updates, 13 corrections and 4 improvements, 7 of them internal.
- **No new entry.**
- **`state/cves_seen.json`:** 9 CVEs added (the eight of APSB26-162 and CVE-2026-119977), and 54 `last_seen` dates bumped.
- **Registry:** one product record, Prisma Cloud Application Security Transporter Client, from `sync_products.py`.
- **`tools/check_run.py`:** every run-scope invocation appends its output to `work/<run-id>/gate.log`, with a header line per call. The 10-25 audit's recommendation 2 is now mechanical, and `docs/pipeline.md` § The mechanical gate says so. It was exercised on this fire's own gate runs (`work/2026-11-01T1312Z-audit/gate.log`).
- **Sources:**
  - New candidate `gitguardian`.
  - `sans-isc` content scope.
  - Health notes on `ico-uk`, `ssd-disclosure` and `connectwise-trust-center`.
  - Re-sweep recipe notes on `msrc-update-guide`, `morphisec`, `bsi-de`, `news-admin-ch`, `lumen-black-lotus-labs`, `team-cymru`, `nict-cynex-lettice`, `mandiant-gtig` and `darkreading`.
- **Warning sweep:** one new acknowledgment, `2026-10-28T0256Z-intel: final CLEAN is unconfirmed`. That fire's first CLEAN came at iteration 8, the cap, and this audit re-verified all 14 entries it touched. `check_run.py --all` ends 0 warn · 0 fail, and `site/build.py` emits no self-check warning.

## Recommendations (operator decisions, not shipped)

1. **Bring the over-length entries back within the bound** (carried from 2026-10-25). Of the window's entries, these are still over 550 words, and none of them grew this week:
   - Publica 1,158
   - PHP 1,917
   - ConnectWise 1,047
   - eMudhra 910
   - VMware 768
   - ARTEX 726
   - GitLab 662
   - PAN-OS 551

   Gridbox came back to 522 through its correction.
2. **A revision re-read for covered advisories.** Each fire could re-read the vendor advisories behind the newest week's exploited entries and diff their revision history. Nine of this week's 24 defective entries were publisher revisions, two of them from August. This is a prompt duty with a real cost per fire, so it is the operator's call.
3. Unexploited critical vendor bundles (carried from 2026-10-11).
4. Legacy repair pace (carried from 2026-09-30).
5. Non-adversarial items (carried from 2026-10-11).
6. Effort settings (carried from 2026-10-18): try `high` on the main agent; keep `xhigh` on research and verifier.

Retired: 2026-10-25 recommendation 2 (gate output), now shipped in the tool.

## Watch items

- **Publisher revisions** (carried): 9 entries this week. Resolution: recommendation 2 adopted, or the weekly truth pass keeps catching them.
- **Over-length entries** (carried): see recommendation 1.
- **Cleanup wave 05 claim** (carried): still open since 2026-10-21 with no push, and wave 06 (which owns the Mini Shai-Hulud/Nx Console link, W4-15) has not started. Resolution: the waves resume, or the claim is withdrawn.
- **connectwise-trust-center** (carried): still flapping. Resolution: a stable recipe, or the status-page substitute recorded as its working route.
- **ARX Group SA backlog row** (carried): held to 2026-11-07. Resolution: a victim, client or press confirmation, or expiry.
- **Out-of-scope page-check leads** (new): the LiteLLM maintainers' root-cause post was rewritten after the 2026-10-25 audit verified two quotes from it, and the AFP page behind the Danfoss quote no longer returns the passage to a direct read. Both entries are out of scope this week. Resolution: the next truth pass that owns them re-quotes or confirms them.
- **Legacy queue, non-CVE duplicates, out-of-week findings** (carried): owned by the cleanup program (`docs/cleanup/STATUS.md`).
