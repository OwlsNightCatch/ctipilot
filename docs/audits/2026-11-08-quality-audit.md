# Quality audit — 2026-11-08

**Run record:** [runs/2026-11-08/2026-11-08T1309Z-audit.md](../../runs/2026-11-08/2026-11-08T1309Z-audit.md) · **Prompt:** v4.24 · **Window:** 2026-11-01T13:12Z → 2026-11-08T13:09Z (the trailing week since the 2026-11-01 audit)

## Method

Scheduled weekly audit, claimed on `main` before the first spawn (`work/2026-11-08T1309Z-audit/audit.claim`, base `cf78df5`). The open partial claim of cleanup wave 05 (`2026-10-21T1147Z-audit`, `wave=05`) was ignored under Phase 0 step 2.

- **Scope:** 47 entries with activity from the week's seven intel fires (30 filed in the week, 17 older entries the fires updated), each read whole.
- **Out of scope (v4.22):** 18 entries whose only in-window activity is records of the 2026-11-01 audit, which its own verifier loop checked.
- **Truth passes:** TA to TE, 259 to 301 claims each, 1,380 in all (`work/2026-11-08T1309Z-audit/truth-T{A..E}.yaml`), every claim checked against a freshly fetched cited source. The cited-page pre-pass (`page-checks.txt`) handed three leads to the passes. TC also re-checked the LiteLLM watch item.
- **Coverage re-sweeps:** G1 (vulnerabilities, 46 of 46 sources), G2 (incidents, region and policy, 44 of 44) and G3 (research blogs, 44 of 44), each one spawn.
- **Main-agent reads for the fixes:** 39 page reads under `work/2026-11-08T1309Z-audit/deep/`, among them Splunk SVD-2026-1015, Siemens SSA-045512, QNAP QSA-26-19, Xerox XRX26-016 v6, the November Android bulletin, Todyl, LiteLLM, Ubuntu, Fortinet FG-IR-26-188, Sophos, NetApp, Cisco's PHP advisory, the BPK notices, Keycloak 26.8.2, Red Hat, both IBM API Connect bulletins and Elastic's report PDF.
- **Budget:** see the run record's notes for the final spawn and token totals (`work/2026-11-08T1309Z-audit/budget.tsv`).

## Verdict

**23 of 47 entries clean, 19 with imprecisions only, 5 with factual errors.** The LiteLLM watch-item entry, outside the window, also carried a factual error.

- **The five factual errors:**
  - Node2Shell kept "Splunk Enterprise 10.0 and lower" after Splunk narrowed it to 10.0 on 2026-11-05 and 11-06.
  - The exposed-app-credentials entry said Todyl does not tie its case to ARTEX, but Todyl's revision of 2026-11-06 does.
  - QNAP QNE (ADRA) was still called unfixed, though QSA-26-19 V1.1 of 2026-11-02 names 1.0.7.q327.
  - Xerox printers were still "no fixed build", though bulletin v6 of 2026-11-06 remediates AltaLink 82xx/81xx, EC81xx and VersaLink.
  - Android SMS of Death gave the October patch level and "no CVE record", though Google's November bulletin lists CVE-2026-58882 at the 2026-11-01 level.
- **The cause is the same as last week.** Eight of the 24 defective entries are publisher revisions made after the entry's last record, all of them inside the week; two more outside the scope (LiteLLM, Cisco's PHP advisory) had the same cause.
- **Composition errors:**
  - The Sophos RCA was cited with the blog's date.
  - Binance's AI-tool mechanism was not disclosed by Binance.
  - Kiesewetter was quoted for heise's own list.
  - The Zyxel default-credential "re-entry" claim and its T1078.001 mapping are not in the source.
  - The BPK assumption was attributed to the wrong party.
  - A Cisco citation was bound to the wrong advisory.
- **Coverage:** every KEV addition of the week (3) has an entry. The re-sweeps recovered three findings that clear the gate as new entries (Keycloak 26.8.2, IBM API Connect, Elastic's quarterly report) and five developments on covered findings.
- **Verifier convergence improved:** four of seven fires reached a confirmed CLEAN, against none last week.

## Findings — false or erroneous published intelligence

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| 2026-10-24 Node2Shell | Splunk Enterprise "10.0 and lower"; ELLIO "the only first-hand account" | SVD-2026-1015 (rev. 2026-11-05/06): 10.0 vulnerable, 9.4 and 10.2+ not; Zscaler decoys also | `correction` with section |
| 2026-11-06 exposed app credentials | Todyl "does not tie its case to ARTEX" | Todyl update 2026-11-06: agentic credential crawler, ARTEX per Microsoft | `update` with section |
| 2026-10-25 QNAP/Synology PHP2Shell | QNE (ADRA) unfixed; table row quoted as evidence | QSA-26-19 V1.1 (2026-11-02): 1.0.7.q327 | `update` with section |
| 2026-11-02 Xerox | "No fixed build is out" | XRX26-016 v6 (2026-11-06): AltaLink 82xx/81xx, EC81xx, VersaLink remediated; WorkCentre and AltaLink C80xx/B80xx patch | `update` with section |
| 2026-11-02 Android SMS of Death | October patch level; "no CVE record" | Google bulletin 2026-11: CVE-2026-58882, 2026-11-01 level | `update` with section |
| 2026-10-22 LiteLLM (watch item) | Two quotes no longer on the post; "master key"; "force-pushed over" | Post rewritten: administrative key; commit in public history until 2026-10-22 | `correction` with section |
| 2026-11-07 Brotli/Desigo | SSA-045512 rev. 2026-11-06 read as Desigo only | V1.2 adds Gridscale X DSA (fix V5.4) and PSS®E (fix V36.8.0) | `correction` with section |
| 2026-10-31 Linux TCP | Ubuntu 26.10 "in progress"; Fortinet "unchanged"; Sophos absent | Ubuntu 26.10 fixed 7.3.0-10.10 (2026-11-07); FortiGuard IPS FMWP 26.113; Sophos HF110626.1, SD-RED 3.0.012 | `update` with section |
| 2026-10-29 Trend/Quest/NetApp | NetApp list stops at rev. 11.0 | Rev. 12.0 (2026-11-04, final) adds ONTAP 9.17.1P12 | `update` with section |
| 2026-10-09 Publica | BPK "must be assumed so"; Inside IT "working from AWP"; no encryption stage | BPK: neither confirm nor rule out; ransomware installed 2026-09-29; watson: no Akira listing a month on | `correction` with section; T1486 added |
| 2026-08-30 Berlin | Kiesewetter "named" the leaked documents; ministry "confirms" missing agreements | heise's own voice; ministry cites 14 existing agreements | `correction` with section |
| 2026-09-22 Zyxel GS1900 | "Re-enter even after rotation"; T1078.001 | GreyNoise: 564 victims on default credentials, nothing on re-entry | `correction` with section |
| 2026-11-04 Binance | AI tool "let one user act on colleagues' machines" | Binance: "gain control over", details confidential | `correction` with section |
| 2026-11-05 Sophos RCA | RCA cited as 2026-11-04, "undated" | Dateline 20 October 2026 | `correction` with section |
| 2026-11-01 Vaud school | Police communiqué not read | vd.ch 26762/26754: SOC containment, reports to BACS and the data-protection authority | `improvement` with section |
| 2026-11-06 FreeSWITCH | SIP surface only | 1.11.3 also gates the api chat proto in mod_verto | `improvement` with section |
| 2026-10-30 WordPress | wp-config.php check bound to Picus | Picus describes the overwrite, not the check | `improvement` with section |
| 2026-09-22 Synology DSM | Uncited endpoint sentence | NCSC: management-interface prerequisite only | `improvement` with section |
| 2026-10-14 Ivanti | `critical` 10 days after the full-chain patch, no new exploitation | Critical bar fails on in-window and time-to-hour | internal `correction` to `high` |
| 2026-11-04 Barracuda | Detection tool "public since 2026-11-05" | Repository public 2026-11-03 | internal `correction` |
| 2026-09-15 Cisco SEG | 16.0.4-302 / CVE-2026-76461 cited to the hardening advisory (pre-pass lead) | SQL-injection advisory carries both | internal `improvement` |
| 2026-11-08 Apple/BSI | Summary: keep Lockdown Mode on permanently | BSI: consider enabling, then keep on | internal `correction` |
| 2026-11-04 cPGuard | Earlier advisory's access account not noted | Stolen CDN credentials, replaced by sign-up and billing exploit | internal `improvement` |
| 2026-10-21 eMudhra | Pages "carry no date"; CVE-2026-111943 not in `cves[]` | Both pages dated; Go 1.27.3/1.26.10, GitLab 19.5.3 et al. | internal `improvement` |

Declined, with reason:
- **Danfoss, the 2026-10-25 record summary's "a firmware update alone does not close the exposure" (low-confidence F13).** It follows from ANSSI's statement that elementary exposure and weak passwords were exploited, and records are append-only.
- **Dahua, CERT-UA as a national-CERT carve-out (F12).** `prompts/verification.md` calls the list "illustrative rather than exhaustive for same-tier authorities", and CERT-UA is the disclosing party for its own advisory.
- **Cisco SEG, no labelled Exposure and Detection lines (F8, low).** The content is in the prose, the Triage line and the actions, and the analysis sits at the 550-word bound.
- **Node2Shell, the 2026-10-27 record summary on exploitation.** Records are append-only; this fire's correction section states ELLIO's 2026-10-26 report.

Pre-pass leads:
- The Splunk and QNAP quotes were verbatim until the publishers revised their pages; both are replaced.
- The Cisco citation-cve lead was a real binding error and is fixed.
- The Danfoss AFP watch item is confirmed verbatim (Khaleej Times/AFP).

**Root causes.**
- *Publisher revisions after the entry's last record (8 in-scope entries, plus LiteLLM and Cisco's PHP advisory outside it):* Splunk, Todyl, QNAP, Xerox, Google, Siemens, Ubuntu, Fortinet, Sophos and NetApp. Fires re-read an advisory only when something else surfaces it. Recommendation 1 would catch these on the fire's own day.
- *Composition (12 entries):* Sophos RCA, Binance, Berlin, Zyxel (text from cleanup wave 03 of 2026-10-21), Publica (BPK), Cisco SEG, Barracuda, Apple/BSI, WordPress, Synology, eMudhra and cPGuard.
- *Calibration (1 entry):* Ivanti kept `critical` after the bar's in-window element lapsed.

## Findings — missing or incomplete coverage

**Recovered as new entries (3):**
- **Keycloak 26.8.2.** CVE-2026-117691 is a SAML HTTP-Redirect signature bypass: an unauthenticated login as any federated user, CVSS 3.1 9.1, with no mitigation that meets Red Hat's criteria. Red Hat fixed its build of Keycloak 26.6 in 26.6.9 on 2026-11-07. The release also fixes an unauthenticated JVM termination (CVE-2026-110931).
  - Gate: PD-11(b), the "otherwise" limb.
  - Missed because `keycloak` was last swept on 2026-11-02, a rotation gap.
- **IBM API Connect bulletins of 2026-11-05.** They include hard-coded admin credentials (CVE-2026-17360, 9.8), unauthenticated command injection and path traversal to code execution, a signature-verification bypass and token issuance for other users. IBM gives no workaround.
  - Gate: PD-11(b), "an anonymous, single-request path to full administrative control".
  - Missed because `ibm-support-security-bulletins` has no listing transport, a recipe gap; the EUVD score search found it.
- **Elastic threats, etc. report, November 2026.** Its findings: AI assistants as execution parents, RMM as the payload, ROPC that Conditional Access never evaluates, and device-code compromise ending in a device and a primary refresh token.
  - Gate: PD-9.
  - Fires dropped it as landing-page-only; the full PDF is linked two steps down.

**Recovered as records on covered entries (5):**
- Cisco PHP2Shell advisory v1.11: the URWB/UIWS fix 26.2.1.9 is now available.
- Gridbox 2.20.5.0: four more fixes, including an unauthenticated file deletion.
- CERT-EU: ARTEX "highly likely" used against the EU institutions, plus BACS GovCERT's statement that no autonomous-agent intrusion has been reported in Switzerland (on the 2026-10-22 ARTEX entry).
- The BPK notices (ransomware stage, wording) on Publica.
- The vd.ch primaries on the Vaud school entry.

**Correctly droppable (G1 11, G2 5, G3 12):**
- Plex2Shell: KEV-listed and widely exploited per QNAP, but consumer/SMB media servers with no public-sector deployment shown. Re-open on a Swiss nexus.
- Unexploited, on the regular cycle or end of life: Windows Paint CVE-2026-83844 v2, Android November bulletin, Chrome 157, LXD, the Drupal contrib wave, Absolute Secure Access, AWS Babelfish, Aspera Faspex, HPE Fabric Composer, the Entra device-registration cloud CVE.
- No nexus, vector or obligation change:
  - the BBT SE (Brenner) attack;
  - Gleis D / Medi Porta (Cloak claim);
  - the BACS/police EHRA phishing warnings;
  - the EDÖB SkySale duty-to-inform ruling (private sector, no new obligation);
  - ENISA CNW-2026-05 (no new fact for Danfoss).
- Research with no constituency decision:
  - Anubis/Lindnor (Symantec): a single US victim, no access vector;
  - CERT-In CRAFTY FALCON: Indian banking victims, generic hardening;
  - Microsoft's exploited-vulnerabilities analysis and its fake-download campaign;
  - Check Point's ChatGPT Lockdown bypass (fixed 2026-09-18);
  - CrowdStrike's ecosystem post;
  - Recorded Future's October CVE landscape;
  - Sophos financial-services ransomware;
  - ESET SlippyNunchucks and Gorbag;
  - Trend Micro Matryoshka;
  - Censys ARTEX exposure counts.

**KEV:** three additions since 2026-11-01 (CVE-2026-119977, CVE-2024-27834, CVE-2026-19868), all COVERED; no COVERED-STALE or RANSOMWARE row.

**Backlog:**
- ARX Group SA was struck at expiry by the 2026-11-07 fire. G2 found only tracker re-listings, and no victim or press confirmation, so it stays closed.
- ChimeraZ/ZOHE is held to 2026-11-17 with a named condition.

**Rotational lookback:**
- Four rotation defects: Keycloak (last swept 11-02), mySites.guru (last swept 11-03, Gridbox 11-04), `cert-eu-blog` (no fire swept it in the window) and the Cisco PHP advisory revision (swept 11-06 at 02:55Z, revised 14:21Z).
- One sweep defect: Netzwoche's 2026-11-02 BACS remark was inside the 2026-11-05 fire's lookback.
- Three recipe or reading gaps: IBM bulletins (no listing), the QNAP QSA feed (stopped at 2026-10-22) and Elastic's two-step PDF.

## Findings — systemic / operational

1. **Fix did not take: gate output was never committed.** The 2026-11-01 audit made `check_run.py` write `work/<run-id>/gate.log`, but `.gitignore`'s `work/**/*.log` rule (cleanup W7-07, 2026-10-20) swallowed it. None of the week's seven fires committed one.
   - The fires do write the file; it never reached git.
   - Fixed: `!work/**/gate.log` re-includes it, and this fire's own `gate.log` is committed.
2. **Publisher revisions (carried watch item, unchanged rate).** 8 of 24 defective in-scope entries, against 9 of 24 last week.
3. **Verifier convergence (carried; better).**
   - Confirmed CLEAN on 2026-11-02, 03, 04 and 06.
   - 2026-11-05 published on a single CLEAN at the cap, after iteration 6's CLEAN was refuted only by a stale word-count note.
   - 2026-11-07 published at the cap with residual 3, after iteration 7's CLEAN was refuted.
   - 2026-11-08 took the early exit with residual 1.
   - Iterations per fire: 6, 6, 8, 8, 6, 8, 2.
   - Two passes left claims unanswered: 2026-11-04 iteration 3 (229/211) and 2026-11-07 iteration 6 (237/236). Neither was a CLEAN, so neither broke the chain rule.
4. **Calibration alarm:** as published, the 47 in-scope entries held 11 `high` and 2 `critical` (`high` 23%). After this audit moved Ivanti from `critical` to `high` they hold 12 `high` and 1 `critical`, so `high` is 25.5%, at the alarm. New entries: 4 of 30 `high` (13%).
   - I re-graded all 12 against the Phase 4 `high` bar: constituency exposure, an out-of-cycle decision within 7 days, and an in-window development. None failed, so none moved.
   - Seven are exploited or KEV-listed flaws in products the constituency runs: SIMATIC IoT2050, Synology DSM, Zyxel GS1900, Ivanti Connect Secure, Node2Shell, WordPress core and SonicWall SSL VPN.
   - Barracuda ESG is a no-login path to root on an email gateway, with a public proof of concept.
   - Four are incidents or campaigns inside the constituency, its region or its target class: Publica, the Swiss refrigeration attacks, Vaud device-code phishing, and the Entra app-credential campaign that reached government MSP clients.
   - The share sits at the threshold because Ivanti moved down from `critical`, not because more entries were rated `high`.
5. **Discipline:**
   - `actions[]` on new entries: 14 empty, 14 with one action, 1 with two, 1 with three.
   - Technique density on new entries: threat 10.6, incident 8.7, vulnerability 1.8.
   - `exploitation-consistency` passes over the window. No CVE-sharing pair in the window lacks a `references[]` link.
   - Over-length analyses did not grow this week: Danfoss fell from 1,291 to 711 words and Berlin from 709 to 705; this fire's records grow none.
   - Registry: 58 records added in the window, 35 of them products. `3AM` was added to the 3AM ransomware record's `ambiguous_labels`, since it is a time of day. No unrelated attachment found.
6. **Sources.**
   - The health snapshot flags only `connectwise-trust-center`, which read directly at 11:25Z and returned 403 at about 13:30Z; it is still flapping and stays `blocked`.
   - `ico-uk` and `sygnia` are documented transport-blocked hosts.
   - `novee-security` is demoted after a third marketing-only sweep.
   - New candidate: `balbooa-blog`.
7. **Telemetry.**
   - Seven daily fires at about 02:56Z, each with a 24 h gap and no coverage hole.
   - Durations ran 1.0 to 5.2 h, and every record is `publish_status: ok`.
   - The jina pool (context only) has 2 live keys, about 98k tokens. G1 and G3 fell through to the reader six times between them.
8. **Fix effectiveness (2026-11-01 audit).**
   - The gate log did not take; fixed above.
   - `gitguardian` was swept on 11-02 and 11-08.
   - `sans-isc` now reads as relevant.
   - The `msrc-update-guide` revision note was in use: swept every fire.
   - The ATT&CK pin was current until upstream v20.1 (2026-11-05); updated this fire, with no technique-level changes.

## Fixes shipped in this commit

- **Records:** 27 entries carry one record each: 9 updates, 11 corrections and 7 improvements, 6 of them internal.
- **New entries (3):** Keycloak 26.8.2, IBM API Connect, Elastic's November report.
- **`state/cves_seen.json`:** 18 CVEs added and 40 `last_seen` dates bumped.
- **Registry:**
  - new: `report:elastic-threats-etc-2026-11`, plus three product records from `sync_products.py` (IBM API Connect, Gridscale X DSA, Gridscale X PSS®E);
  - `3AM` added to `malware:threeam`'s ambiguous labels;
  - the exposed-app-credentials campaign's summary and ARTEX relation note updated to Todyl's revision.
- **ATT&CK pin:** v20.0 → v20.1. No technique-level changes; self-test, `site/build.py` and `site/test_build.py` green.
- **`.gitignore`:** `!work/**/gate.log`.
- **Sources:**
  - candidate `balbooa-blog`;
  - `novee-security` demoted;
  - recipe notes on `elastic-seclabs`, `vulncheck`, `mandiant-gtig`, `crowdstrike`, `ibm-support-security-bulletins`, `qnap-security-advisories` and `connectwise-trust-center`.
- **Warning sweep:** one new acknowledgment, `2026-11-05T0255Z-intel: final CLEAN is unconfirmed`. This audit re-verified all eleven entries that fire touched.

## Recommendations (operator decisions, not shipped)

1. **A revision re-read for covered advisories** (carried from 2026-11-01, sharpened). Eight of this week's 24 defective entries were publisher revisions, all inside the week (among them QNAP 11-02, NetApp 11-04, Splunk 11-05/06, Xerox 11-06, Todyl 11-06).
   - A per-fire duty to re-read the vendor pages behind the last seven days' vulnerability entries and diff their revision history would have caught each within a day.
   - It costs a fire roughly 20 to 30 reads.
2. **Unexploited critical vendor bundles** (carried from 2026-10-11). This audit published IBM API Connect at `notable` under PD-11(b)'s "otherwise" limb (hard-coded admin credentials, no privileges). October's fires dropped IBM Verify Access under the same limb. Decide which reading the prompt should state.
3. **Bring the over-length entries back within the bound** (carried). Over 550 words and none grew this week:
   - Publica 1,143
   - eMudhra 909
   - LiteLLM 854
   - ARTEX 726
   - Danfoss 711
   - Berlin 705
4. Legacy repair pace (carried from 2026-09-30).
5. Non-adversarial items (carried from 2026-10-11).
6. Effort settings (carried from 2026-10-18): try `high` on the main agent; keep `xhigh` on research and verifier.

## Watch items

- **Publisher revisions** (carried): 8 in-scope entries this week. Resolution: recommendation 1 adopted, or the weekly truth pass keeps catching them.
- **Over-length entries** (carried): see recommendation 3.
- **Cleanup wave 05 claim** (carried): still open since 2026-10-21 with no push. Resolution: the waves resume, or the claim is withdrawn.
- **connectwise-trust-center** (carried): still flapping. Resolution: a stable recipe, or the status-page substitute recorded as its working route.
- **Gate log** (new): `gate.log` is now committed. Resolution: next week's fires each commit one.
- **Out-of-scope page-check leads** (closed): the LiteLLM quotes are corrected, and the Danfoss AFP passage is confirmed.
- **ARX Group SA** (closed): struck at expiry by the 2026-11-07 fire; a new backlog row opens only on a confirmation.
- **Legacy queue, non-CVE duplicates, out-of-week findings** (carried): owned by the cleanup program (`docs/cleanup/STATUS.md`).
