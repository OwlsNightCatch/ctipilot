# Quality audit — 2026-11-15

**Run record:** [runs/2026-11-15/2026-11-15T1407Z-audit.md](../../runs/2026-11-15/2026-11-15T1407Z-audit.md) · **Prompt:** v4.25 (shipped by this audit) · **Window:** 2026-11-08T13:09Z → 2026-11-15T14:07Z (the trailing week since the 2026-11-08 audit)

## Method

Scheduled weekly audit, claimed on `main` before the first spawn (`work/2026-11-15T1407Z-audit/audit.claim`, base `b010c9a`). The open partial claim of cleanup wave 05 (`2026-10-21T1147Z-audit`, `wave=05`) was ignored under Phase 0 step 2.

- **Scope:** 56 entries with activity from the week's seven intel fires (38 filed in the week, 18 older entries the fires updated), each read whole.
- **Out of scope (v4.22):** 20 entries whose only in-window activity is records of the 2026-11-08 audit, plus that audit's three recovered entries, all checked by its own verifier loop.
- **Truth passes:** TA to TF, 196 to 312 claims each, 1,646 in all (`work/2026-11-15T1407Z-audit/truth-T{A..F}.yaml`), every claim answered. The cited-page pre-pass (`page-checks.txt`) found two non-verbatim quotes: the Danfoss one went to TA, the LiteLLM one (out of scope) was decided by the main agent.
- **Coverage re-sweeps:** G1 (vulnerabilities, 46 of 46 sources), G2 (incidents, region and policy, 44 of 44) and G3 (research blogs, 42 of 42), one spawn each.
- **Main-agent reads for the fixes:** about 40 page reads, among them Microsoft's Edge security notes and Security Update Guide record, SUSE CVE-2026-119618 and SUSE-SU-2026:5231-1, VulnCheck's XWEB EVO disclosure and CVE-2026-124014 advisory, FortiGuard FG-IR-26-244, -268 and -187, NCSC.ch post 13155, QNAP QSA-26-21, the BPK notice page, Ahsay's v9.17.0 release notes, the Sophos, Ubuntu, Veeam and Debian pages for CVE-2026-98432, Cisco's Brotli and eMudhra advisories, Apple's tvOS 27.2.1 notes, CERT-FR AVI-1507, Unit 42's refrigeration post and Datadog's ARTEX post.
- **Budget:** 16 spawns (6 truth passes, 3 re-sweeps, 7 verifier iterations), 8,667,965 sub-agent tokens (`work/2026-11-15T1407Z-audit/budget.tsv`).
- **This audit's verifier loop:** seven iterations. Iteration 6 was CLEAN, and iteration 7's full cold pass over all 183 claims confirmed it. Iteration 1 caught and reverted the SonicWall update, and later iterations found fixes that had gone stale (Apache forky in the main analysis, newer Ahsay builds). The run record lists every finding and its remediation.

## Verdict

**27 of 56 entries clean, 24 with imprecisions only, 5 with factual errors.**

- **The five factual errors:**
  - Fortinet told FortiAnalyzer and FortiManager 7.2 owners to migrate for CVE-2026-126229; FG-IR-26-244 fixes 7.2 in 7.2.13, and only 7.0 migrates. This was wrong when written.
  - SSHole still said NCSC.ch rates exploitation unknown; NCSC.ch has rated it "Actively Exploited, PoC Available" since 2026-11-10 09:59.
  - Chrome zero-day said Edge desktop had no fix; Microsoft's notes list Edge 157.0.4341.46, and the Security Update Guide added Edge on 2026-11-13.
  - Apache httpd mod_http2 named SUSE as unfixed; SUSE shipped SUSE-SU-2026:5231-1 for SLE 15 SP7 on 2026-11-13, and its CVE page lists further products as fixed.
  - Dixell/Copeland XWEB EVO said no exploitation and no fixed build. VulnCheck reports CVE-2026-124014 exploited from 2026-11-12 and CVE-2026-124010 probed from 2026-11-13, and says the injection class is fixed on the current branch.
- **The cause is the same as the last two weeks.** Eight of the 29 non-clean entries are publisher revisions made after the entry's last record: Chrome/Edge, Apache/SUSE, SSHole/NCSC.ch, AhsayCBS, Linux TCP, Brotli, eMudhra and Dixell.
- **Coverage:** the re-sweeps found no uncovered critical or high item. They recovered one new finding, Datadog's ARTEX activity in AWS, and two developments on covered findings. Every KEV addition of the week has a disposition.
- **Verifier convergence fell back:** one of seven fires reached a confirmed CLEAN (2026-11-09), against four last week; the other six published on the low-residual early exit.

## Findings — false or erroneous published intelligence

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| 2026-10-23 Fortinet | FortiAnalyzer/FortiManager 7.2 "migrate" for CVE-2026-126229; iBGP CVE typed memory corruption; release dated 2026-10-22 for all products | FG-IR-26-244: 7.2.0 to 7.2.12 fixed in 7.2.13, only 7.0 migrates, and the 7.6, 7.4 and 7.2 lines are exposed as well as 8.0; FG-IR-26-268: numeric truncation, denial of service, virtual patch added 2026-11-13; FortiMail and FortiAuthenticator built 2026-10-21 | `correction` with section |
| 2026-11-06 SSHole | NCSC.ch "rates exploitation unknown"; unsourced Previdian count in summary | NCSC.ch post 13155, update 2026-11-10 09:59: Actively Exploited, PoC Available; QNAP QSA-26-21: NAS not affected | `correction` with section |
| 2026-11-11 Chrome zero-day | "Edge desktop pending"; cvss null; "Security Update Guide has no record" | Edge 157.0.4341.46 (2026-11-09) carries the fix; MSRC record rev. 1.1 (2026-11-13), CVSS 8.8 (CISA ADP) | `update` with section |
| 2026-11-12 Apache httpd | SUSE "lists the issue as pending" and has no fix | SUSE-SU-2026:5231-1 (2026-11-13), SLE 15 SP7 apache2 2.4.71-150700.4.30.1, LTSS lines and Tumbleweed; Debian forky and sid fixed in 2.4.71-1; CISA ADP scores 8.1 | `update` with section |
| 2026-11-13 Dixell XWEB EVO | "no exploitation", "no fixed build", "no log artefacts", `notable` | VulnCheck 2026-11-13: CVE-2026-124014 (8.8, through 5.8.8) exploited, CVE-2026-124010 probed; injection class fixed on the current branch; request-level indicators | `update` with section; CVE-2026-124014 added; `high`; one action |
| 2026-10-09 Publica | BPK notice PDF dead (404); "same company as Publica" cited to BPK; `Darkweb` in a quote's original; a superseded gloss in the 2026-10-20 section | BPK notice page carries the 9 October notice without the same-company sentence; AWP reports it; watson reads `Darknet` | `correction` with section; contradiction on fraudulent contacts noted |
| 2026-10-10 AhsayCBS | Fix presented as partner-only hotfixes; headline 127 characters; analysis 705 words | v9.17.0 (2026-11-12) patches both CVEs, remote API and JSP engine off by default; v10.3.6 (2026-11-02) lists the same patchset; latest partner hotfixes v9.15.2.78 and v10.3.4.55 (2026-10-27); current v10 build v10.3.6.14 (2026-11-13); CISA calls CVE-2026-105134 command injection | `update` with section; analysis 599 words, headline 110 characters |
| 2026-10-31 Linux TCP | Sophos at version 3; Ubuntu variant list of 2026-11-10; Debian 6.12.116-1; Veeam delivery overstated | Sophos v5: UTM patch 2026-11-10, end-of-life RED unfixed; Ubuntu 2026-11-14; Debian 6.12.117-1; Veeam KB4966 (2026-11-13) adds Recovery Orchestrator 13.1 | `update` with section; actions split |
| 2026-11-07 Brotli | Cisco v1.12; tvOS missing | Cisco v1.13 (2026-11-13): Nexus 3000/9000 Guest Shell, fixes December 2026 to February 2027; tvOS 27.2.1 | `update` with section |
| 2026-10-21 eMudhra | Cisco v1.9; Microsoft's 2026-11-12 table missing; uncited migration sentence; "browsers block them" ambiguous | Cisco v1.11; Microsoft's table (VS Code 1.147.0, Azure CLI 2.93.0); Mozilla bug 2083449 | `improvement` with section |
| 2026-11-11 CopperDragon | Triage: SoftEther "in a non-system path" | Check Point: tools placed in existing system paths, SoftEther renamed to system-process names | `correction` with section |
| 2026-11-11 GhostFrame | Triage: binary "named vmhostd"; credential recovery stated flatly | Insikt: file /opt/vmhostd-core, process vmhostd; "may be able to obtain credentials" | `correction` with section |
| 2026-11-10 BluePhishing | Blueprint default "soon" | MC1506733: from 2026-11-04, rollout complete by late November, "Users can create agent blueprints" setting | `improvement` with section |
| 2026-11-09 LLMjacking | GTIG's CVE id for the /key/regenerate rebind dropped | GTIG names CVE-2026-40217; Obsidian, the discloser, describes that id as the guardrail sandbox escape fixed in v1.83.14-stable | `improvement` with section |
| 2026-10-29 Check Point | R82.20 built-in IPS protection and the portal-crash signal missing; uncited KEV feed source | sk1000302; Check Point Research | `improvement` with section |
| 2026-07-25 Certighost | `high` on a four-month-old patch; one clause cited to the wrong page | MSRC still "Exploited No"; Kaspersky: Citrus targets Russian companies only, attempts only | internal `correction` to `notable` |
| 2026-11-10 N-able | Agents-then-Probes order called mandatory | N-able recommends the order, requires the upgrade | internal `correction` |
| 2026-11-11 Adobe Connect | Headline "fixed in 12.12.a and earlier" | 12.12 and earlier affected, 12.12.a fixed | internal `correction` |
| 2026-11-11 Qubole | "Inside each account" | Wiz: "Once inside multiple victim AWS environments" | internal `correction` |
| 2026-11-10 SAP | Affected lists abridged | SAP Patch Day table | internal `improvement` |
| 2026-11-13 Citrix | CVE List "held no record" | Records published 2026-11-13 | internal `improvement` |
| 2026-10-31 Cursor | Uncited loader sentence | Microsoft Threat Intelligence | internal `improvement` |
| 2026-10-13 Danfoss | Stray word in a French quote's original; record-keeping narration; two uncited sources | French MFA page; style rule | internal `correction` |
| 2026-10-02 ANSSI, 2026-11-12 SCKit, 2026-10-29 Trend/NetApp | `sources[]` records cited nowhere (a duplicate report page, an EUVD API record, two duplicate advisory pages) | PD-2 | internal `improvement` each |
| 2026-10-22 LiteLLM (out of scope, pre-pass lead) | Quote bound to a GitHub issue whose comment is collapsed | Wiz carries the same statement | internal `improvement` |

Declined, with reason:
- **Danfoss, Unit 42 counts "for France alone" (TA, low confidence).** Unit 42's Figure 2 caption reads "Graph of internet exposed devices in France by date since Oct.1, 2026".
- **Seven threat entries with source-supported techniques the body does not describe (TF, advisory):** CopperDragon, Falcon C2, DarkLunnen, Huntress Teams, WFX Phantom, Gentlemen and PolinRider. Each mapping is source-supported and each body sits at 546 to 550 words, so no record was written; see systemic finding 3.
- **Qubole, the "n0n" claim (TE, low confidence).** An unverified self-claim relayed by a newsletter (PD-6).
- **N-able, two superseded evidence quotes; Barracuda, CVSS 4.0 label; eMudhra, the 2026-10-25 record summary's count.** Nothing reader-facing is false, and records are append-only.
- **Node2Shell (out of scope), five uncited release-page sources.** They are the provenance of its `cves[].fixed` strings and stay.

**Root causes.**
- *Publisher revisions after the entry's last record (8 entries):* Microsoft/Edge, SUSE, NCSC.ch, Ahsay, Sophos/Ubuntu/Veeam, Cisco/Apple, Cisco/Microsoft for eMudhra, and VulnCheck the same day. Fires re-read an advisory only when something else surfaces it (recommendation 1).
- *Composition (9 entries):* Fortinet 7.2, Publica's BPK binding, CopperDragon and GhostFrame triage lines, Certighost, N-able, Adobe Connect, Qubole, Cursor. This audit made the same error once: it published the SonicWall update on a relayed bulletin whose vendor page it had not read (reverted in the verifier loop).
- *An update that added a source without citing it:* SCKit's EUVD record came from the 2026-11-13 fire's update, which `entry-shape` did not check (fixed, systemic finding 2).

## Findings — missing or incomplete coverage

**Recovered as a new entry (1):**
- **Datadog, ARTEX against AWS (2026-11-09).** It covers anonymous S3 reads opening each session, CloudWatch Logs FilterLogEvents searches for secrets with stolen long-term IAM keys, and Cognito self-registration traded for AWS credentials. Filed at `notable` under PD-11(d), with references to the ARTEX, CyberStrikeAI, exposed-app-credentials and WorkOS entries. Missed through a rotation defect (systemic finding 1).

**Recovered as records on covered entries (2):** Cisco's Nexus rows and Apple tvOS on the Brotli entry; QNAP's not-affected statement on SSHole.

**Reverted:** an `update` on the SonicWall CVE-2026-19868 entry that treated CERT-FR's relay of SNWLID-2026-0021 as a second SonicOS fix. Verifier iteration 1 read the bulletin through SonicWall's PSIRT API: it is the informational eMudhra DPI-SSL advisory, which the eMudhra entry already carries. The entry is back at its base state.

**Correctly droppable (G1 14, G2 12, G3 14):**
- Fire drops that hold on their stated grounds: OpenAM 16.1.4 (no constituency use shown, advisories of 2026-10-22), Payara (admin interface not normally reachable), BroadWorks, GPUStack and UnrealIRCd (KEV-listed, no constituency footprint), Node.js 2026-11-11, React Server Components, Adobe AEM (authenticated), Roundcube 1.7.6, Drupal GraphQL, Plex2Shell.
- Oracle's announcement of the 2026-11-17 Critical Patch Update: the release itself falls to the 2026-11-17 and 11-18 fires.
- VulnCheck tying the agentic secret-hunting address to Langflow exploitation: one vendor's canary, an address-level link, no CVE.
- G1's SonicWall lead (SNWLID-2026-0021 via CERT-FR AVI-1507): the informational eMudhra DPI-SSL advisory, already on the eMudhra entry.
- Danfoss: Belgium's interior minister cites "indications" of links to Iranian actors (one wire relay, no attribution); CERT-FR's C4 report also names the Shahid Shoostari unit, but for earlier attacks, not the refrigeration campaign.
- Swiss and regional items with no vector or obligation change: Erowa (Akira, private manufacturer), Gleis D/Medi Porta, the Liechtenstein register investigation, Vaud CYBER26 exercise, the Microsoft 365 outage-themed phishing relay, Operation Endgame (no Swiss victim), Saxony pagers, the Berlin forensic interview, France's NIS2 bill, BACS ESTV phishing notice.
- Research with no constituency decision: Huntress ClickFix roundup, Malbear "Operation Snowball" (unnamed victims, single small lab), Proofpoint *Europe's Threat Landscape 2026*, Kaspersky Q3 statistics, Sophos retail ransomware, Krebs on the Qilin administrator, Morphisec, TrendAI MCP and Hermes posts, Enea SilentAir, Greeter/Flowise honeypot, Citizen Lab Webloc, lab-only AI-agent research.

**KEV:** twelve additions since 2026-11-08 (`kev-window.txt`). Eight are covered, and all four not covered (GPUStack, Openwave, BroadWorks, UnrealIRCd) carry fire `borderline-drop` lines. No COVERED-STALE or RANSOMWARE row.

**Backlog:** empty; the 2026-11-15 fire struck ChimeraZ/ZOHE with its reason.

**Rotational lookback:**
- One accounting defect, Datadog, fixed in v4.25. The 2026-11-12 fire's S3 checked it outside its slice at 26 h, and listing it moved its rotation cursor past three unswept days.
- No sweep defect. The other recoveries are publisher revisions.

## Findings — systemic / operational

1. **Rotation cursor moved by out-of-slice checks (new; fixed).**
   - Research sub-agents check a list of major labs "in addition to the slice" at the fire's 26 h window and list them in their source ledgers. The run records' `sources_attempted` then carry them, and the cursor (v4.12) treats each as a full lookback sweep.
   - Fixed in `prompts/cti-run.md` v4.25: only allocated slice rows count as attempted.
2. **`entry-shape` skipped sources that an update adds (new; fixed).**
   - The uncited-source check ran on new entries only, so the 2026-11-13 fire's EUVD API record on SCKit passed.
   - `tools/check_run.py` now WARNs a `sources[]` record a fire's update added that no sentence or evidence record cites. A test is in `tools/test_check_run.py` (9/9 pass).
3. **Source-supported techniques left undescribed at the word bound (observation).** Seven of 14 new threat entries map techniques their sources support but their bodies, at 546 to 550 words, never describe. The v4.8 rule asks for dense plain-language naming within the bound. Fires are meeting the bound by dropping those clauses; the verifier flags them only as advisories.
4. **Publisher revisions (carried watch item; rate unchanged).** 8 of 29 non-clean entries, against 8 of 24 last week.
5. **Verifier convergence (carried; worse).**
   - A confirmed CLEAN only on 2026-11-09 (5 iterations). The other six fires took the early exit with residual 1 or 2 after 3 to 6 iterations.
   - 2026-11-11 iteration 4 records 417 claims checked against 212 in scope, a counter the gate does not reconcile.
6. **Calibration alarm:** in-scope `high` is 14 of 56 (25.0%), at the alarm.
   - I re-graded all 14 against the Phase 4 bar. Certighost fails it and moves to `notable`: a patch four months old, no exploitation, and Russia-only targeting by the actor. Dixell XWEB EVO, published at `notable`, now clears it and moves to `high`: exploited, a Swiss authority warning, and a 7-day decision.
   - The share stays 14 of 56. New entries: 6 of 38 `high` (16%).
7. **Discipline:**
   - `actions[]` on new entries: 11 empty, 25 with one action, 2 with two (Dixell gained its action in this audit).
   - Technique density: threat 11.6, vulnerability 2.8.
   - `exploitation-consistency` passes over the window. No CVE-sharing pair touching the window lacks a `references[]` link.
   - Registry: 22 non-product records added by the window's seven intel fires; this audit added six product records. `SRG`, which is also the Swiss broadcaster SRG SSR, and `Cereal` are now `ambiguous_labels`.
8. **Sources.**
   - The Phase 0 snapshot flagged three: `connectwise-trust-center` now has a health check on its CNA disclosure repository, `bfv-verfassungsschutz-de` on `url --direct` of its feed, and both read `relevant`.
   - `safeonweb-be` stays UNSOLVED: the host answers HTTP 500 on every path and transport, a server outage.
   - The five essential sources with no contribution all week (cert-at, cert-pl, ncsc-uk, watchtowr, bacs-press) read cleanly in the re-sweeps. They had nothing in scope.
9. **Telemetry.**
   - Seven daily fires (gap 24 to 25 h, no coverage hole), 1.1 to 3.9 h each, all `publish_status: ok`.
   - The jina pool (context only) has every key exhausted; the fires and re-sweeps read through the direct rungs.
10. **Fix effectiveness (2026-11-08 audit).**
    - `gate.log` was committed by 7 of 7 fires.
    - `balbooa-blog` was swept twice, and `novee-security` stays demoted.
    - The recipe-noted sources were all swept: elastic-seclabs 4 times, mandiant-gtig 3, vulncheck, crowdstrike, the IBM bulletins and QNAP once each.
    - The ATT&CK pin is current (v20.1).

## Fixes shipped in this commit

- **Records:** 27 entries carry one record each: 6 updates, 10 corrections and 11 improvements, 12 of them internal.
- **New entry (1):** Datadog's ARTEX activity in AWS.
- **Prompt v4.25:** `cti-run.md` Phase 2, only slice rows count as rotation attempts; `quality-audit.md` banner in lockstep; CHANGELOG entry.
- **Tool:** `tools/check_run.py` `entry-shape` now checks uncited sources an update adds, with a test.
- **`state/cves_seen.json`:** CVE-2026-124014 added; 16 `last_seen` dates bumped.
- **Registry:** `ambiguous_labels` on `actor:silent-ransom-group` (SRG) and `malware:cereal` (Cereal); six product records from `sync_products.py`: Amazon Cognito, Amazon CloudWatch Logs, Apple tvOS, Cisco Nexus 3000 Series Switches, Sophos UTM, Veeam Recovery Orchestrator.
- **Sources:** `connectwise-trust-center` (`blocked` to `bridge`, new health check), `bfv-verfassungsschutz-de` (health check), `safeonweb-be` (note).
- **Warning sweep:** `check_run.py --all` was already at 0 warn · 0 fail · 29 acknowledged at Phase 0. No acknowledgment was added or removed.

## Recommendations (operator decisions, not shipped)

1. **A revision re-read for covered advisories** (carried from 2026-11-01). Eight of this week's 29 non-clean entries were publisher revisions, among them Microsoft/Edge, SUSE, NCSC.ch, Ahsay and Sophos. A per-fire duty to re-read the vendor pages behind the last seven days' vulnerability entries would catch each within a day, at roughly 20 to 30 reads a fire.
2. **Unexploited critical vendor bundles** (carried from 2026-10-11).
3. **Bring the over-length entries back within the bound** (carried). Still over 550 words: Publica 1,100, eMudhra 878 (from 895), AhsayCBS 599 (from 705).
4. Legacy repair pace (carried from 2026-09-30).
5. Non-adversarial items (carried from 2026-10-11).
6. Effort settings (carried from 2026-10-18): try `high` on the main agent; keep `xhigh` on research and verifier.

## Watch items

- **Publisher revisions** (carried): 8 entries this week. Resolution: recommendation 1 adopted, or the weekly truth pass keeps catching them.
- **Over-length entries** (carried): see recommendation 3.
- **Cleanup wave 05 claim** (carried): still open since 2026-10-21. Resolution: the waves resume, or the claim is withdrawn.
- **safeonweb-be** (new): HTTP 500 site-wide on 2026-11-15. Resolution: the next health sweep reads content, or a substitute recipe is recorded.
- **Oracle Critical Patch Update of 2026-11-17** (new): the next audit checks that the fires enumerated its unauthenticated 9.8 to 10.0 rows (Database Server, APEX, Fusion Middleware, E-Business Suite).
- **connectwise-trust-center** (closed): the CNA repository is the recorded route.
- **Gate log** (closed): committed by every fire.
- **Legacy queue, non-CVE duplicates, out-of-week findings** (carried): owned by the cleanup program (`docs/cleanup/STATUS.md`).
