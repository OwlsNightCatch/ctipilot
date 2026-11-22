**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-22T16:49:17Z · ended_at=2026-11-22T17:07:06Z · duration_seconds=1069

## Verification report — 2026-11-22T1407Z-audit (iteration 5)

Scope: post-fix pass, 84 claim rows in `verification.iter5.claims.yaml`: the 3 changed claims (all Brotli: actions[0], cves[CVE-2026-111497], the SSA-443410 body clause); every claim of the two remediated entries (Brotli 18, Synology 12); the whole recovered timeroasting entry (14); and a seeded random sample of 40 of the other 173 claims (seed 20261122, 19 entries). Result: 83 ok, 1 F3 at claim level. Pages were fetched this pass: `extract` for Synology-SA-26:21, Mitel MISA-2026-0010, Cisco's combined advisory, the sampled vendor and research pages and the nine Apple notes; raw `url` for the Siemens tables (SSA-045512, -443410, -242944, -678870, -935812), their CSAF JSON (status and revision history), FG-IR-26-194, the OpenVox GHSA sidebar, the PHP ChangeLog sections and the Apache thread API; `cisa-kev` (catalogue 2026.11.20: CVE-2026-111497 listed, CVE-2026-120382 not); `ncsc-csh recent 15` for a coverage cross-check.

### Delta verification (iteration 4 findings)

- Synology F4 (sourcing_note): holds. The page does not make Synology the CNA and the clause is gone. The remaining note matches the page: the description lists "before 6.2.4-25556-9, 7.1.1-42962-10, 7.2.1-69057-14, 7.2.2-72806-11, 7.3.2-86009-6, and 7.4.1-90080-2" while the table marks DSM 7.2.2, 7.2.1 and 7.1 "OnGoing" and has no DSM 6.2 row; the entry says it follows the product table.
- Run-record F4 (iteration-3 Brotli line): holds on disk. The takeaway now reads "disable Brotli where it is not required on SICAM PAS CC and SICAM SCC" and names Integrated PA Suite Tester; actions[0] carries SENTRON and Integrated PA Suite Tester and no SICAM item, which the line states. One wording residual, see the advisory below.
- Brotli F8: holds as scoped. SSA-045512 V1.3 (raw table): "Integrated PA Suite Tester | All versions | Install the latest .NET security updates via Windows Update."; "SICAM PAS CC | All versions >= V6.02" and "SICAM SCC | All versions >= V7.01", each "Currently no fix is planned Temporarily disable Brotli compression and decompression at the application or proxy layer if it is not strictly required." Takeaway, actions[0], cves[] and affected_products carry these correctly. The Exposure line and the analysis sentence do not name Integrated PA Suite Tester (finding #2).
- Dropped analysis sentence (Industrial Edge mitigation): the replacement clause "fixes six configurator and monitoring applications and has no fix for Common Configurator" holds against SSA-443410 (six rows with versioned fixes: Cloud Connector Configurator, Data Flow Monitoring, Databus, DataXess, Edge OPC UA Server, Flow Creator; both Common Configurator rows "Currently no fix is available"). The uninstall/firewall mitigation survives in the takeaway and actions[1] as a derived line and matches SSA-443410.

### Citation does not support the claim

- #1 (F3, low confidence) 2026-10-23 Fortinet hardening entry, Exposure line (claim 73a4f1abb2). The sentence "FortiMail 8.0.0 to 8.0.1, 7.6.0 to 7.6.6, 7.4.0 to 7.4.8 or any 7.2; FortiAuthenticator 8.0.0 to 8.0.3 and 6.6.0 to 6.6.10; FortiOS below the fixed builds and any 7.0; FortiAnalyzer and FortiManager 8.0.0 to 8.0.2 ...; FortiClient 7.4.0 to 7.4.7 and, on Windows, 7.2.0 to 7.2.14, with the FortiPAM service installed, which Fortinet's workaround removes" ends in one citation, https://fortiguard.fortinet.com/psirt/FG-IR-26-194. That page carries only the FortiClient clause (7.4.0 through 7.4.7; 7.2.0 through 7.2.14; "For FortiClient to be impacted, the FortiPAM service must be installed. To prevent the vulnerability, the FortiPAM service can be uninstalled") and says nothing about the other four products. The line was uncited before this fire; the added citation now claims the whole chain. Fix: end the sentence after the FortiAnalyzer/FortiManager clause and put the FortiClient clause in its own sentence with the citation.

### Needs more research

- #2 (F8, low confidence) Brotli entry, Exposure line and analysis. Quote: "a Desigo CC, SENTRON Powermanager, SICAM PAS CC or SICAM SCC host, a Gridscale X DSA or PSS®E installation below its fixed version". SSA-045512 V1.3 lists Integrated PA Suite Tester (all versions, .NET updates), and the takeaway, actions[0], cves[] and affected_products carry it, but Exposure omits it and the analysis says "since V1.3, SENTRON Powermanager and two SICAM products". Exposure is lifted onto the product page, so the new Integrated PA Suite Tester record would show no exposure line. Add it to Exposure and to the analysis sentence.

### Editorial / less-is-more flags (advisory)

- #3 (F11, pre-existing label) Brotli, Cisco paragraph: "Cisco's advisory, version 1.13 of 2026-11-13, says ..." The page read this iteration, and the audit's own cached copy, shows "1.14 ... Interim 2026-NOV-17" on top of the revision table. All facts drawn from it still hold at 1.14 (PoC statement, no malicious use known, the not-impacted list, Duo 3.4.2, Spaces 24.22.1, RoomOS 11.41.2.3 and 26.7.4.3, Nexus Guestshell 4.9 and NX-OS builds), so only the version label is stale. The run record and audit report carry v1.14 to the next audit; re-labelling costs nothing.
- #4 (F11, wording) Run record, iteration-3 Brotli line: "the SICAM no-fix state only cves[].fixed" understates; cves[].affected ("SICAM PAS CC from V6.02 and SICAM SCC from V7.01 (no fix planned)") and the 2026-11-22T14:49:25Z section carry it too. Say "among the remedy fields, only cves[].fixed".

### Whole-run checks

- Changelog contract, Brotli (4c): the 2026-11-22T14:49:25Z record is an `update`, `updated_at` equals its `at`, the section closes the body, the record summary matches the section, and every changed frontmatter line in `git diff cdd8f41 --` (title, summary, affected_products, cves, evidence, sourcing_note, references, actions, body) is named in `fields`. Mitel rev 6.0 and SSA-045512 V1.3 are inline-cited; the analysis no longer contradicts the newest section.
- Run record and audit report: 25 updated entries, 25 records of this run (7 update, 9 correction, 9 improvement, 5 internal), `updated_entry_ids` equals the set of entries carrying a record of this run, ten registry product records in the diff match `entities_added` and the report's registry line, the report's Brotli row matches Mitel rev 6.0 and SSA-045512 V1.3, the iteration-4 block matches `verification.iter4.md` (106 claims, 1035 s, truth 2, editorial 1, advisory 0, three findings), run duration 9705 s equals 14:07:07Z to 16:48:52Z.
- Style scan of Synology, Brotli and timeroasting: no em dash outside headings, no workflow vocabulary, no IOCs. Synology A/2 (vendor PSIRT, single source, `single-source` with a sourcing note), timeroasting B/2 and Brotli A/2 are consistent with their sourcing.
- Coverage: nine KEV additions all covered (`kev-window.txt`); the fifteen newest NCSC.ch security-hub posts map to covered entries or to items before the window. No missed angle found; coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 2)

Both blocking findings are low confidence and small: an adjacency problem on one Exposure sentence that gained a citation this fire, and one product missing from an Exposure line. All three iteration-4 remediations hold. No other claim in the 84-row scope failed.

### Findings summary (machine-readable)

See `work/2026-11-22T1407Z-audit/verification.iter5.findings.yaml`.
