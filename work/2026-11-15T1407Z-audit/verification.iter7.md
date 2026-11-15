**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T18:13:09Z · ended_at=2026-11-15T18:40:17Z · duration_seconds=1628

## Verification report — 2026-11-15T1407Z-audit (iteration 7, confirmation pass)

Scope: the full claim ledger `work/2026-11-15T1407Z-audit/claims.iter7.yaml` (183 claims), the new ARTEX entry read whole, the 27 updated entries (every changed field and section read against `git diff b010c9a5 -- <path>`), the SonicWall CVE-2026-19868 entry (no diff against base), the run record and the audit report. Every claim has a verdict row in `verification.iter7.claims.yaml` (183 ok, 0 non-ok). Cold pass: no prior-iteration deltas block was supplied, and I did not rely on the iteration 6 verdict.

### Method
- Fetched every one of the 63 distinct cited URLs this iteration (extract; `url --direct` for the Check Point sk page, Ahsay announcement listing, Siemens/Adobe/FortiGuard raw pages; `ncsc-csh post` for Security Hub; `pdf` for the Dixell and Copeland PDFs; `cisa-kev` for the KEV catalogue), plus about 25 further pages the ledger claims lean on (Cisco eMudhra advisory, Bitdefender, Huntress N-able post, Huntback, Previdian, Onapsis x2, SAP Patch Day, MSRC per-CVE API, CNA records from the CVE List API for the Ahsay, Dixell, Citrix and LiteLLM CVEs, FortiGuard raw pages for all 14 cited advisories, Bugzilla REST comments, Ahsay listing HTML).
- Checked the fire's changed text clause by clause (adjacency), not only the fact: dates, versions, counts and attributions against the page named at the clause.
- Checked the run record and audit report claims against disk: 27 updated ids and records (6 update, 10 correction, 11 improvement, 12 internal), SonicWall entry reverted (no diff), six truth batches (27 clean / 24 imprecision / 5 factual; 1,646 ledger claims), 38 new + 18 older entries, 14 of 56 `high`, 6 of 38 new `high`, actions 11 empty / 25 one / 2 two, word counts (Publica 1,100, eMudhra 878 from 895, AhsayCBS 599 from 705), KEV 12 additions with 4 not covered (GPUStack, Openwave, BroadWorks, UnrealIRCd; live catalogue agrees), `state/cves_seen.json` (CVE-2026-124014 added, 16 `last_seen` bumps), registry (six product records, two `ambiguous_labels`), prompt v4.25 banner and CHANGELOG, `sources.json` changes, `check_run.py` change and `test_check_run.py` 9/9. The one-of-seven confirmed-CLEAN convergence statement holds across the week's seven run records.

### Notable things confirmed against the page (not defects)
- Ahsay: v9.17.0 (12-Nov-2026) and v10.3.6 (02-Nov-2026) release notes list the CVE patchset and the two default-off settings; v10.3.6.14 (13-Nov-2026) lists the Redirector password-logging fix; announcement listing dates (raw HTML) give 03 November for v10.3.6.1 and 27 October for the v9.15.2.78/v10.3.4.55 advisory; VulDB CNA records give 7.3 and 10.0 (CVSS 3.1); CISA's catalog calls CVE-2026-105134 command injection while Horizon3 calls it a file-write path traversal.
- Fortinet: all 14 cited 2026-11-10 PSIRT pages show Known Exploited No; CVE ids and CVSS agree with the entry; FG-IR-26-244 fixes FortiAnalyzer/FortiManager 7.2 in 7.2.13 and only 7.0 migrates; FG-IR-26-268 revised 2026-11-13 with FG-VD-62507.0day (db update 26.118), impact denial of service.
- SSHole: NCSC.ch post 13155 update of 10.11.2026 09:59 "Actively Exploited, PoC Available" (replacing UNKNOWN); QNAP QSA-26-21 (13 Nov) not affected; Previdian first observed 06 Nov; SANS ISC first genuine attempt 05 Nov.
- Chrome/Edge: Edge Stable 157.0.4341.46 (9 Nov) and Edge for Android 157.0.4341.53 (11 Nov) "contain a fix"; MSRC record rev 1.1 of 2026-11-13 added Edge, CVSS 3.1 8.8 (CISA ADP); KEV text names Opera.
- Apache/SUSE: SUSE-SU-2026:5231-1 (2026-11-13, critical, SLE 15 SP7 2.4.71-150700.4.30.1); SUSE CVE page lists LTSS lines and Tumbleweed as released, SLES 16.0 in progress; Debian tracker lists forky and sid fixed in 2.4.71-1; SUSE CNA-ADP 8.1 vs SUSE 9.8.
- Brotli: Cisco advisory 1.13 (2026-NOV-13) lists Nexus 3000/9000 Guest Shell (CSCwx56979) with Guestshell 4.9 / NX-OS dates Dec 2026 to Feb 2027; Apple tvOS 27.2.1 (13 Nov) carries the brotli entry; Siemens SSA-242944 (15 industrial products) and SSA-678870 (28 software products, 8 not affected) match the entry's counts.
- Dixell: VulnCheck CNA records (CVSS 4.0 and affected ranges) match all eight carried CVEs; the blog lists CVE-2026-124014 with the pre-2021 class while the CNA record runs to 5.8.8 (the entry states the disagreement); canary times, four probes, opportunistic-scanner reading and "neither source is evidence of the October campaign" are on the blog; Copeland bulletin: end of software support 16 March 2026, end of sales Oct 2023.
- Linux TCP: Sophos advisory v5 (12 Nov) UTM 9.724 and EOL RED unfixed; Ubuntu tracker "Last updated 14 November 2026" matches the variant-kernel statuses; Veeam KB4966 last modified 2026-11-13; Debian trixie (security) 6.12.117-1.
- Citrix: CVE List API shows the 15 corrected ids PUBLISHED on 2026-11-13.
- ARTEX (new): every sentence and quote traces to Datadog's 2026-11-09 post or Wiz's 2026-10-22 post; no duplicate in the store (three ARTEX entries exist and are referenced as distinct findings); registry product keys exist; 529 words.

### Editorial / less-is-more flags (advisory)
F11 #1 (low confidence). 2026-11-11/ghostframe... and 2026-11-11/copperdragon...: file-name artefacts in reader-facing Triage/Correction text (`/opt/vmhostd-core`, `vmhostd`; `vmtoolsd.exe`, `csrss.exe`) against the "no file-name indicators" rule. Both are the sources' own behavioural discriminators and iteration 3 declined the same point; the main agent may leave it.
F11 #2 (low confidence). 2026-11-11/cve-2026-125350...: the Exposure clause ending "...so a pending relaunch leaves a patched machine still running the old code ([Google, 2026-11-09])" carries chrome://version and relaunch guidance that Google's page does not state (it states only "will roll out over the coming days/weeks"). Operational guidance, not a factual claim about the source.
F11 #3 (low confidence). 2026-11-13/dixell...: "install the latest build from Copeland's update page on any pre-2021 unit" is cited to the Dixell France guide, which does not carry the "pre-2021" qualifier (VulnCheck's blog does). Iteration 6 declined a related point.

### Coverage (check 13)
Coverage looks complete for the window: the 12 KEV additions each have a disposition and the live catalogue shows no further addition since the fire's `kev-window.txt`; the re-sweep telemetry in the run record shows 46/44/42 sources attempted with the unreadable ones named (sygnia, nict-cynex-lettice, belden-psirt, lab52, anssi-cyber-gouv-actualites, EFS press page, SentinelLABS). No missed critical/high item identified.

### Verdict
CLEAN (truth: 0, editorial: 0, advisory: 3)

### Findings summary (machine-readable)
See `work/2026-11-15T1407Z-audit/verification.iter7.findings.yaml` (three F11 advisory records).
