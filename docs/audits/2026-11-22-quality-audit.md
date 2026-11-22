# Quality audit — 2026-11-22

**Run record:** [runs/2026-11-22/2026-11-22T1407Z-audit.md](../../runs/2026-11-22/2026-11-22T1407Z-audit.md) · **Prompt:** v4.25 · **Window:** 2026-11-15T14:07Z → 2026-11-22T14:07Z (the trailing week since the 2026-11-15 audit)

## Method

Scheduled weekly audit, claimed on `main` before the first spawn (`work/2026-11-22T1407Z-audit/audit.claim`, base `cdd8f41`). The open partial claim of cleanup wave 05 (`2026-10-21T1147Z-audit`, `wave=05`) was ignored under Phase 0 step 2.

- **Scope:** 49 entries with activity from the week's seven intel fires (34 filed in the week, 15 older entries the fires updated), each read whole.
- **Out of scope (v4.22):** 22 entries whose only in-window activity is records of the 2026-11-15 audit, plus that audit's recovered ARTEX-in-AWS entry, all checked by its own verifier loop.
- **Truth passes:** TA to TF, 161 to 352 claims each, 1,426 in all (`work/2026-11-22T1407Z-audit/truth-T{A..F}.yaml`), every claim answered.
- **Cited-page pre-pass:** `page-checks.txt` found five non-verbatim quotes. The php2shell and agent-framework leads went to TB and TD. The main agent decided the two Publica leads and the Mitel lead on the Brotli entry, which are out of scope.
- **Coverage re-sweeps:** G1 (vulnerabilities, 46 of 46 sources), G2 (incidents, region and policy, 43 of 43) and G3 (research blogs, 48 of 48), one spawn each.
- **Main-agent reads for the fixes:** about 35 page reads, among them Drupal's security feed item for SA-CORE-2026-017, RIKEN's second notice, SafeDep's revised agent-framework post, Mitel MISA-2026-0010 revision 6.0, Keycloak's and Atlassian's Java4Shell posts, Huntress's August ScreenConnect post, Report URI's 17 November update, Ohey's OPTIMJACK post, Spiegel on BundID, Siemens SSA-935812, FortiGuard FG-IR-26-194, N-able's remediation update, VulnCheck's CVE-2026-47101 advisory, GTIG's LLMjacking post, Synology-SA-26:21, Huntress's timeroasting post and the CISA KEV catalogue (2026.11.20).
- **Budget:** 14 of 20 spawns (6 truth passes, 3 re-sweeps, 5 verifier iterations), 6,982,947 sub-agent tokens (`work/2026-11-22T1407Z-audit/budget.tsv`).
- **This audit's verifier loop:** five iterations, ending on the low-residual early exit (truth 1, editorial 1, both remediated after the pass). The loop caught a wrong OpenVox remediation in iteration 1 (the server range does belong to CVE-2026-115731), Siemens' SSA-045512 V1.3 in iteration 2, and an imprecise vCenter detection line in iteration 3; the run record lists every finding.

## Verdict

**24 of 49 entries clean, 22 with imprecisions only, 3 with factual errors.**

- **The three factual errors:**
  - **Drupal SA-CORE-2026-017** said no exploitation was reported. Drupal revised the advisory on 2026-11-21 to Highly critical 20 of 25 and reports exploitation on live sites from 2026-11-19 19:00 UTC. The entry moves to `high`.
  - **Oracle's November CSPU** said none of the unauthenticated critical rows was exploited. Three of them are the Brotli flaw CVE-2026-111497, on CISA KEV since 2026-10-27.
  - **ScreenConnect CVE-2026-84869** said Huntress traced its exploitation back to 20 August. Huntress never ties the August rogue-client incidents to the CVE. The exploitation it confirms runs from October.
- **Publisher revisions remain the largest single cause.** Six of the 25 non-clean entries are revisions made after the entry's last record, plus Mitel's on the out-of-scope Brotli entry:
  - Drupal, RIKEN and SafeDep on agent-framework.
  - Keycloak and Atlassian on Java4Shell.
  - Report URI and Ohey on OptimJack.
  - CISA's KEV listing of the Axis flaw behind N-able's 4EverAble2Shell.
- **Coverage:** the re-sweeps found no uncovered critical or high item and recovered two new findings, Synology-SA-26:21 and Huntress's timeroasting detection research. Every KEV addition of the week is covered.
- **Verifier convergence improved:** two of seven fires reached a CLEAN, against one last week:
  - 2026-11-16 reached a confirmed CLEAN.
  - 2026-11-19 reached a CLEAN at the cap.
  - The other five published on the low-residual early exit.

## Findings — false or erroneous published intelligence

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| 2026-11-18 Drupal core | "No exploitation is reported", "Critical 18 of 25", `notable` | SA-CORE-2026-017, revised 2026-11-21: Highly critical 20 of 25, E:Exploit, exploited on live sites from 2026-11-19 19:00 UTC | `update` with section; `exploited` status, evidence quote, `high`, compromise check added |
| 2026-11-18 Oracle CSPU | Headline "none exploited"; summary "no source reports exploitation" | Three unauthenticated 9.8 rows are CVE-2026-111497 (Brotli), CISA KEV since 2026-10-27 | `correction` with section |
| 2026-09-12 ScreenConnect | Title, headline, summary and analysis tie the 20 August incidents to CVE-2026-84869; propagation direction reversed; headline 133 characters | Huntress's August post never names the CVE; confirmed exploitation from October; the Host side of a session with an infected client receives the chain | `correction` with section; headline 114 characters |
| 2026-11-07 Brotli (out of scope, pre-pass lead) | Mitel "update planned, not released" for OpenScape SBC; product list at revision 5.0; Siemens SSA-045512 at V1.2 | MISA-2026-0010 rev. 6.0 (2026-11-18): SBC fixed in V11R3.4.5, MiCollab Advanced Messaging patched, Alarm Response to DAKS-IoT V2.00, Performance Analytics added; SSA-045512 V1.3 (2026-11-18) adds SENTRON Powermanager and Integrated PA Suite Tester (.NET updates) and SICAM PAS CC and SICAM SCC (no fix planned) | `update` with section; action moves from workaround to update. Cisco's advisory v1.14 (2026-11-17, product-list changes) is carried to the next audit |
| 2026-11-18 RIKEN Fugaku | "Took or may have taken" the keys | Second notice (2026-11-20): 430 SSH private keys exfiltrated, 233 without passphrase; registration data access traces | `update` with section |
| 2026-11-18 agent-framework | "Published under the microsoft account"; pin advice only | SafeDep update (2026-11-18): same-day maintainer `vibiret` can publish five sibling projects; lock the whole tree with hashes | `update` with section; action and takeaway rewritten |
| 2026-11-18 Java4Shell | Calif called the discoverer; Oracle fixed builds uncited; Keycloak images still affected | Oracle credits Albert Yang and Calif's Quang Luong; Tenable's fixed-build table; Keycloak 26.8.2-3 on OpenJDK 21.0.13.1 (2026-11-19); Atlassian Data Center out-of-cycle patches pending Temurin | `update` with section |
| 2026-11-10 N-able | CVE-2026-90436 not marked KEV; N-able's own reading absent | CISA KEV 2026-11-18; N-able: agent impersonation needs an endpoint foothold | `update` with section |
| 2026-11-17 OptimJack | Exposure limited to cdn.optimizely.com; no end of the Optimizely window; cookie path unconditional; "minute-ly" bound to Report URI | Report URI: customer-hosted snippets affected, files clean from 2026-11-16 23:11 UTC, collection host on hold from 2026-11-17 00:37 UTC; Ohey: router rented by channel code, loader taken down 17 and 18 November; Hudson Rock: cookie path conditional | `update` with section |
| 2026-11-19 nginx2root | Siemens lists "Industrial Edge products" as affected; "root is not established" attributed to Rapid7 | SSA-935812: five device products affected, Hub and Management products not affected; Rapid7 speaks only of worker permissions | `correction` with section; sourcing note trimmed to provenance |
| 2026-11-18 Puppet | OpenVox Agent missing from CVE-2026-115731's affected and fixed versions and from the action | GHSA-ffr6-rwpm-p5wq lists OpenVox Agent (fixed 9.3.0, 8.32.0) and OpenVox Server (fixed 9.2.0, 8.18.0) | `improvement` with section |
| 2026-11-17 BundID | Same-day return of password sign-in "aggregator only"; headline "password sign-in cut"; uncited Swiss sentence | Spiegel quotes the BundID notice: two-factor e-mail code for every password sign-in from the afternoon of 2026-11-16 | `improvement` with section |
| 2026-06-16 LiteLLM chain | CVE-2026-47101 CVSS "n/a"; CISA "the only statement of exploitation" | VulnCheck CVSS 4.0 8.7; GTIG (2026-11-02) attributes an exploited `/key/regenerate` rebind to CVE-2026-40217 | `improvement` with section and contradiction line |
| 2026-10-23 Fortinet | FortiClient exposure without its prerequisite | FG-IR-26-194: only where the FortiPAM service is installed; uninstalling it is the workaround | `improvement` with section |
| 2026-11-20 vCenter | KEV listing only in frontmatter; Detection names an audit log GTIG does not; vSphere Foundation missing | CISA 2026-11-20; GTIG: SSH via the appliance management API, the directory database pulled over the directory service's RPC interface, key and credential files read over SSH; VMSA-2026-0009 impacted products | `improvement` with section |
| 2026-11-20 PHP 8.5.13 | Follow-ups to CVE-2026-109619 without saying it is KEV-listed | CISA KEV 2026-10-26 (PHP2Shell) | `improvement` with section |
| 2026-10-22 ARTEX/Storm-0940 | Exposure line cited Expel for claims it does not make; analysis 726 words | Expel carries the Okta self-registration case only | `improvement` with section; analysis 550 words |
| 2026-10-13 Danfoss | Title "six more countries" (body names more); uncited ANSSI clause; record-keeping sentence in an earlier section | AFP (2026-10-12), a person close to the Prime Minister | `improvement` with section |
| 2026-10-22 Cisco Expressway | Cookies tied to clustering | Cisco gives persistent cookies and TLS Verify Mode certificate validation as separate causes | `correction` with section |
| 2026-11-17 Symantec retailer | "Unsigned DLL"; side-load file pairs named | Symantec does not say unsigned; the pairing is reused by several actors | `correction` with section |
| 2026-11-11 Confluence | Apache thread dated 2026-11-01 | Message dated 2026-11-06 | internal `correction` |
| 2026-11-19 tcherber | "Local" accounts | Cyderes does not say local or directory-backed | internal `correction` |
| 2026-11-20 USI Lugano, 2026-11-21 Basel-Landschaft | English quote longer than its original | Corriere del Ticino; canton FAQ | internal `correction` each |
| 2026-11-22 MONAI Label | Detection detail cited to release notes | GHSA-qc22-rmgc-vg94 | internal `improvement` |

Declined, with reason:
- **Cisco Secure Email Gateway, `critical` five weeks on (TA, low confidence) and the Metasploit record typed `improvement`.** The entry does not float (`updated_at` null), and with a public one-email root exploit an unpatched gateway is still a stop-and-act case. Records are append-only.
- **Puppet `notable` (TD, low confidence).** The reachable condition is a CA-signed agent certificate, so doubt resolves to `notable` under the `high` bar.
- **Java4Shell, the 11-19 record summary's "13 products" and the 11-19 probing telemetry (TC, advisory).** Records are append-only, and the probing adds no decision beyond the entry's update action.
- **Turla Cereal planted DLL names (TB, advisory).** These are hijacked legitimate Windows DLL names that the detection keys on, not indicators.
- **Idunno and Ruby EUVD API citations (TE, low confidence).** The EUVD record is the accepted channel for CNA text.
- **HPE Aruba sourcing-note timestamp (TB).** It is not verifiable because the page is a JS shell; nothing reader-facing depends on it.

**Root causes.**
- *Publisher revisions after the entry's last record (6 entries, plus Brotli out of scope):* Drupal, RIKEN, SafeDep, Keycloak/Atlassian, Report URI/Ohey and CISA KEV (N-able). Fires re-read an advisory only when something else surfaces it (recommendation 1).
- *Composition (17 entries):*
  - ScreenConnect: an inferred CVE link stated as fact.
  - Oracle and PHP: no-exploitation statements written without checking KEV for the release's own or parent CVEs.
  - BundID: a same-day primary, Spiegel quoting the operator's notice, was missed.
  - Attribution, completeness or qualifier drift: nginx, Puppet, LiteLLM, Fortinet, vCenter, ARTEX, Expressway, Symantec, tcherber, OptimJack, Danfoss, Confluence and MONAI.
- *Quote-translation drift (2 entries):* English renderings that open with words their quoted originals do not carry.

## Findings — missing or incomplete coverage

**Recovered as new entries (2):**
- **Synology-SA-26:21, CVE-2026-120382 (2026-11-19, revised 2026-11-20).** Argument injection in the DSM OAuth API: unauthenticated arbitrary file read and write, CVSS 3.1 9.8.
  - Fixed in 7.4.1-90080-2 and 7.3.2-86009-6. DSM 7.2.x, 7.1 and BeeStation OS are unfixed; the mitigation is to deactivate the OAuth Service package.
  - Filed at `notable` under PD-11(b), with references to the SA-26:13, SA-26:19 and nginx2root entries.
  - The 2026-11-21 fire swept Synology's listing with a 168 h horizon but saw only SA-26:15 (a sweep defect). The 2026-11-22 fire's verifier found it and withdrew it as out of window, and set the feed recipe that now lists it.
- **Huntress, detecting timeroasting (2026-11-19).** The MS-SNTP sweep leaves no logon event, and Defender for Identity stayed silent across eleven runs. Huntress shipped a cracker for the extended authenticator that modern Windows sends. The holding signal is a host requesting another account's RID.
  - Filed at `notable` under PD-11(d).
  - The 2026-11-21 and 11-22 fires saw it only through the out-of-slice major-lab check and left it to this audit (PD-7). `huntress` had not been in a slice since 2026-11-15.

**Recovered as records on covered entries:** Drupal, RIKEN, agent-framework, Java4Shell, N-able, OptimJack, BundID and Brotli/Mitel (table above).

**Correctly droppable (G1 14, G2 10, G3 16):**
- **Unit 42 on Com-affiliated vishing (2026-11-20).** The 2026-11-21 fire dropped it as incremental to three UNC6671 entries; the victims are in the US, UK and Australia. The call holds.
- **IGEL UMS ISN-2026-44 and -50.** The auth bypass needs a reverse proxy forwarding client certificates; there is no CVE and no exploitation. IGEL's notices are added as a candidate source.
- **Oracle CSPU, 12 unauthenticated 9.8 rows not itemised (Hyperion, AutoVue, Service Delivery Platform, Unified Assurance).** The entry counts all 56 and itemises the identity, middleware, ERP and APEX rows. The three Database Server rows need Create Session, so their omission is right. This closes the Oracle watch item.
- **F5 BIG-IP TMM overflows (NCSC-NL 2026-11-19).** Each needs a non-default iRule or APM policy; no exploitation is reported.
- **Java4Shell vendor statements from Metabase (GHSA-69v7, fixed Docker images) and Adobe Animate (APSB26-208), and the eMudhra entry's pip and pnpm CVEs (CVE-2026-133949, CVE-2026-130756).** These are derivative vendor-impact rows for covered findings: each entry's action already covers the Java runtime or the trust-store update they ship.
- **Others from G1:** Apache Shiro (non-default caching on an LDAP realm), Tomcat clustered TLS-PSK, WatchGuard Dimension, Atlassian's dependency roll-up, Poste.io, Rootways Magento, Microsoft service-side CVEs, UniFi Access bulletin 073. Mitel MX-ONE MISA-2026-0011 is dated 2026-11-11, before the window.
- **Kaspersky Operation ShadowCloud, TrendAI on BYOD ransomware, Talos UAT-12643 and the other G3 borderlines.** The victims are outside the region or the techniques are known classes.
- **G2:** BACS weekly review 46, the eid.admin.ch Java4Shell banner (no scope or duration), the BSI Lagebericht 2026 (statistics), NoName057(16) sanctions and arrest (no new defender action), Stadtwerke Wittenberg (single dpa source), the IIHF defacement, the Salt outage (no security cause), the Berlin forensic interview, e-ID policy items, and OpenSSL CVE-2026-121481 (NCSC-IE: no attacker path). The Saxony pager exposure is dated 2026-11-12, outside the window.

**KEV:** nine additions since 2026-11-15 (`kev-window.txt`), all covered, with no COVERED-STALE or RANSOMWARE row.

**Backlog:** no open row.

**Rotational lookback:**
- *One sweep defect:* Synology (above), fixed by the 2026-11-22 fire's recipe change.
- *One rotation lag:* Huntress, unswept from 2026-11-15 to 11-22, with the next sweep due inside its 168 h lookback. Research sources' rotation cursors have a median age of 3 days; 8 of 153 are at 6 days or more.

## Findings — systemic / operational

1. **Publisher revisions (carried watch item).** 6 of 25 non-clean entries in scope (plus Brotli), against 8 of 29 last week. Drupal's revision turned a `notable` entry into an exploited `high` one three days before this audit. Recommendation 1 stands.
2. **"None exploited" written without checking KEV for the release's own CVEs (new; observation).** The Oracle entry and the PHP entry both made a no-exploitation statement about a release that carries a CVE already on KEV (CVE-2026-111497; CVE-2026-109619's follow-ups). `kev_window_diff.py` checks only additions inside the window, not KEV status of every CVE an entry names. No tool change ships: Oracle's 56 rows are not in `cves[]`, so a `cves[]`-based check would not have caught it. The verifier's truth pass did.
3. **Claim counters (carried; observation).** 2026-11-22 recorded 102 of 107, 108 of 113 and 82 of 87 claims checked on its three iterations. Across the store, 14 of the 331 earlier iterations that carry both counters record a mismatch, all on NEEDS_FIXES passes, so no CLEAN was ever short of its scope. No gate change.
4. **Calibration alarm:** in-scope `high` is 15 of 49 (31%) after this audit's changes, above the alarm.
   - I re-graded the 14 `high` entries at Phase 0 against the Phase 4 bar. All 14 clear it: each is exploited, or reachable pre-auth with a public PoC or announced exploit, has plausible constituency exposure, and has an in-window development. Drupal joins them.
   - New entries: 8 of 34 `high` (24%), Drupal included. The week carried an unusual run of exploited or pre-auth flaws (vCenter, REDCap, TYPO3, nginx2root, Java4Shell, Ruby).
5. **Discipline:**
   - `actions[]` on new entries: 10 empty, 19 with one action, 4 with two and 1 with three (nginx2root).
   - Technique density: threat 11.0, vulnerability 3.0, incident 2.9.
   - `exploitation-consistency` and `entry-shape` pass over the window. No CVE-sharing pair touching the window lacks a `references[]` link.
   - Registry: 25 non-product records added by the window's fires. No entity grew by more than two window entries, and no unrelated attachment was found.
6. **Sources.**
   - The Phase 0 snapshot flagged one: `checkpoint-support` (shell, "request blocked"). It reads `relevant` again on its existing recipe, so the block was transient; the note is recorded.
   - `safeonweb-be` reads `relevant` again (newest item 2026-11-20).
   - No `webfetch-only` record.
   - `lab52` is still unreadable on every transport (last post 2026-10-05).
7. **Telemetry.**
   - Seven daily fires (gap 24 h, no coverage hole), 1.1 to 5.0 h each, all `publish_status: ok`.
   - The jina pool (context only) has every key exhausted; the fires and re-sweeps read through the direct rungs.
8. **Fix effectiveness (2026-11-15 audit).**
   - Only slice rows count as rotation attempts (v4.25): 25 outside-slice checks were recorded this week, none counted in `sources_attempted`.
   - `entry-shape` checking uncited sources an update adds: it passes over the window.
   - ATT&CK pin current (v20.1).

## Fixes shipped in this commit

- **Records:** 25 entries carry one record each: 7 updates, 9 corrections and 9 improvements, 5 of them internal.
- **New entries (2):** Synology-SA-26:21 and Huntress's timeroasting detection research.
- **`state/cves_seen.json`:** CVE-2026-120382 added; 7 `last_seen` dates bumped.
- **Registry:** ten product records from `sync_products.py` (Microsoft Active Directory, Mitel MiCollab Advanced Messaging, Mitel Performance Analytics, OpenVox Agent, Oracle Communications Diameter Signaling Router, Siemens Integrated PA Suite Tester, Siemens SENTRON Powermanager, Siemens SICAM PAS CC, Siemens SICAM SCC, Synology BeeStation OS).
- **Sources:** `igel-kb-security` added as a candidate; `checkpoint-support` note.
- **Warning sweep:** Phase 0 `check_run.py --all` stood at 1 warn · 0 fail · 29 acknowledged. One acknowledgment was added: `verification-confirmation` for `2026-11-19T0355Z-intel` (single CLEAN at the 8-iteration cap, era-correct, entries re-verified by this audit). No row was removed: all 29 earlier rows still silence a live warning. The build emits no self-check warning.
- **No prompt or tool change.**

## Recommendations (operator decisions, not shipped)

1. **A revision re-read for covered advisories** (carried from 2026-11-01). Six of this week's 25 non-clean entries, plus Brotli out of scope, were publisher revisions, one of them a vendor-reported exploitation (Drupal) that stood unrecorded for three days.
2. **Unexploited critical vendor bundles** (carried from 2026-10-11).
3. **Bring the over-length entries back within the bound** (carried). Still over 550 words:
   - Publica 1,100, eMudhra 878, AhsayCBS 599.
   - Zammad 1,068, newly listed: in scope this week, clean, and grown before the window.
   - ARTEX/Storm-0940 is back at 550.
4. Legacy repair pace (carried from 2026-09-30).
5. Non-adversarial items (carried from 2026-10-11).
6. Effort settings (carried from 2026-10-18): try `high` on the main agent; keep `xhigh` on research and verifier.

## Watch items

- **Publisher revisions** (carried): 6 entries in scope this week, plus Brotli. Resolution: recommendation 1 adopted, or the weekly truth pass keeps catching them.
- **Over-length entries** (carried): see recommendation 3.
- **Cleanup wave 05 claim** (carried): still open since 2026-10-21. Resolution: the waves resume, or the claim is withdrawn.
- **Drupal SA-CORE-2026-017 exploitation** (new): Drupal reports exploitation without detail, and the CVE is not on KEV (catalogue 2026.11.20). Resolution: a KEV listing or a second source on the exploitation, recorded by the fires.
- **Publica NZZ quotes** (new, pre-pass): the NZZ article is paywalled, and the fetched teaser cannot confirm or refute the two German quotes. Resolution: a full read through another transport, or the quotes are replaced by the BPK or AWP wording.
- **safeonweb-be** (closed): reads `relevant` again.
- **Oracle Critical Patch Update of 2026-11-17** (closed): the entry tallies all 56 unauthenticated rows and itemises the identity, middleware, ERP and APEX ones; its exploitation statement is corrected.
- **Legacy queue, non-CVE duplicates, out-of-week findings** (carried): owned by the cleanup program (`docs/cleanup/STATUS.md`).
