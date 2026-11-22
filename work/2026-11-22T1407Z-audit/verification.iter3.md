**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-22T16:10:35Z · ended_at=2026-11-22T16:27:22Z · duration_seconds=1007

## Verification report — 2026-11-22T1407Z-audit (iteration 3)

Scope: post-fix pass. 121 claim rows in `verification.iter3.claims.yaml`: all 20 changed claims; every claim of the seven entries remediated after iteration 2 (Puppet 8, Oracle 14, vCenter 11, N-able 5, Synology 12, Brotli 15, Drupal 11); the whole recovered timeroasting entry (14); the Confluence record (1); and a seeded random quarter of the remaining 122 claims (30, spread over 15 entries). Result: 117 ok, 3 F3, 1 F4 (the three F3 rows are two claims of one finding plus one). Pages were fetched this pass (extract, raw `url` for Siemens, Oracle, FortiGuard and GitHub tables, `cisa-kev`, the Drupal security feed, `WebFetch` for the two CISA alerts and the Drupal advisory page). The run record and audit report were checked for the tallies, the Puppet and Brotli rows, `entities_added` and the iteration-2 block.

### Delta verification (iteration 2 findings)

- Puppet F4 (provenance clause): holds. The record summary and the report row no longer carry the false clause; GHSA-q4hm-33rc-572g lists OpenVoxDB 9.2.0 and 8.18.0 and the oss-security notice lists openvoxdb 9.2.0 and 8.18.0; GHSA-ffr6-rwpm-p5wq lists Agent (<= 9.2.0 and <= 8.31.1, fixed 9.3.0 and 8.32.0) and Server (<= 9.1.0 and <= 8.17.0, fixed 9.2.0 and 8.18.0). Record typed `improvement`, fields match the diff.
- Oracle headline: holds ("Brotli rows on KEV"); KEV catalogue 2026.11.20 lists CVE-2026-111497 (Google Brotli) added 2026-10-27, and all three rows (CDSR PMAC Node.js, Unified Assurance Core Brotli, PeopleTools OpenSearch Dashboards Node.js) are 9.8, HTTP, remote without authentication. Matrix tallies recomputed: 655 patches, 62 rows at 9.0+, 56 unauthenticated, six at 10.0; no other CVE among the 56 unauthenticated rows is in KEV.
- Oracle Exposure and actions[0]: hold and now agree with the takeaway.
- vCenter CVE-2026-123893 scope: holds (9.1.x.x and 9.0.x.x rows 'SDDC Manager/ VCF Installer' for VCF and VVF, 5.x row VCF SDDC Manager only; fixed 9.1.1.0200, 9.0.2.0100, 5.2.5).
- N-able CISA clause: holds (alert of 2026-11-18 lists 'CVE-2026-90436 Apache Axis Unsafe Reflection Vulnerability'; the appositive is gone). The N-able and Huntress contrast holds against both pages.
- Synology version-location clause: holds (dropped). Synology "recorded here": does not hold, see finding #7.
- Brotli SSA-045512 V1.3: holds for the section, main analysis, cves[].affected, affected_products and Exposure (SENTRON Powermanager V8/V9 and IPAS Tester take the .NET updates; SICAM PAS CC >= V6.02 and SICAM SCC >= V7.01 'no fix is planned'). The takeaway, actions[0] and cves[].fixed were not extended, see finding #4.
- Record summaries (Drupal, Brotli): hold, no field bookkeeping left.
- vCenter duplicate CISA sentence: declined with a valid reason (main analysis states state, section the dated delta); not re-raised.
- Audit report "14 of the 331 earlier iterations": holds. Report figures re-checked: ScreenConnect headline 114 characters, ARTEX analysis 550 words, Publica 1,100, eMudhra 878, Zammad 1,068, AhsayCBS 599, 25 non-product registry records in the window, 7 `last_seen` bumps plus one new CVE row.
- Cisco advisory v1.14 (2026-NOV-17, 'Updated products under investigation, vulnerable products, and products confirmed not vulnerable'): carried by the main agent; every Cisco clause in the entry still holds on v1.14; not re-raised.

### Citation does not support the claim

- #1 (F3, firm) vCenter Detection line and Improvement section 2026-11-22T14:57:35Z: "reads of the Directory Service database, the master key and the PostgreSQL credential file over SSH" and "describes the Directory Service, master-key and credential-file reads as taking place over SSH". GTIG: the authenticated administrator session lets the actor "acquire files, including the data.mdb database, by leveraging the vCenter Server Directory Service (`vmdird`) RPC interface `vmdirdbcp`"; BONESAW streams the LMDB; only "the vCenter internal master crypto key file as well as the PostgreSQL password file" were taken "using SSH", after SSH was enabled through the VAMI API. The entry's main analysis has the order right. Fix the line, the section and the audit report vCenter row ("reads over SSH").
- #2 (F3, low confidence) Brotli Defender takeaway: the Cisco citation ends a sentence that also carries Mitel's SBC V11R3.4.5 and the SESAP and Contact Center workarounds; the Cisco page carries only Duo Network Gateway 3.4.2 and Guestshell 4.9. Cite Mitel for its half.

### Unsupported / hallucinated facts

- #3 (F4, low confidence) Brotli summary: "Between 2026-10-27 and 2026-11-13 Siemens, Mitel and Cisco listed affected products" while the same summary now carries Mitel rev 6.0 (Last Updated 2026-11-18, SBC 'Update to V11R3.4.5') and the Siemens V1.3 revision is also 2026-11-18. Extend or drop the bound.

### Needs more research

- #4 (F8, low confidence) Brotli: Exposure names SENTRON Powermanager, SICAM PAS CC and SICAM SCC; the takeaway, actions[0] and cves[].fixed still give the Desigo CC remedy only. Name the V1.3 remedies.
- #5 (F8, low confidence) Oracle: the correction ranks CDSR, Unified Assurance and PeopleTools first, but affected_products omits them and cves[] has no CVE-2026-111497 record.

### Missed angles

- #6 (F10, low confidence) Brotli entry carries no Oracle rows and no references[] link to the Oracle CSPU entry (three fixed rows for CVE-2026-111497, 2026-11-17). Suggested search: Oracle CSPU November 2026 CVE-2026-111497.

### Editorial / less-is-more flags (advisory)

- #7 (F11) Synology sourcing_note still ends "is the state recorded here"; the run record's iteration-2 line says the phrase was removed. Reword the note or correct the line.
- #8 (F11, low confidence) Oracle sourcing_note "the page says nothing about exploitation": the Oracle page has a generic paragraph about attempts to exploit already-patched flaws; restore "of these rows".

### Checked and holding

Whole-entry reads: Synology (table rows, revisions 1 and 2, CWE-88, CVSS 3.1 9.8, 6.2.4 build, OnGoing rows, APM, DSM Enterprise and SRM not affected; reliability A, credibility 2) and timeroasting (every Huntress claim: eleven runs over five hours, event 5156, event 5136 for the targeted variant, own-RID rule, 68 and 120-byte forms, Samba, hashcat placeholder mode, Triage lines). Updated entries: Drupal feed item (Highly critical 20 of 25, E:Exploit, exploitation report as early as 2026-11-19 19:00 UTC; the advisory page itself reads through WebFetch, shows no revision date, and the audit report's "revised on 2026-11-21" rests on the truth pass's page metadata read, not re-verifiable here); Mitel rev 6.0 rows; Siemens SSA-045512 V1.3, SSA-242944 and SSA-678870 (15 and 28 rows), SSA-443410 V1.1, SSA-935812; Cisco Brotli and Expressway advisories; Apple 149715, 149721, 149851; KEV catalogue 2026.11.20 (vCenter, Axis, LiteLLM, Puppet, Brotli, PHP, Roller dates); GTIG ARMORY CASTLE and LLMjacking; VulnCheck CVE-2026-47101; Huntress ScreenConnect posts (42 MSP servers, 20 October to 16 November); ARTEX (Wiz, Microsoft); BundID (heise, Handelsblatt, Spiegel); OptimJack (Report URI 23:11 UTC, Optimizely under 5%, Zscaler over 450 domains, Hudson Rock 21 properties, Ohey 31 renter codes); Symantec; Java4Shell (Tenable fixed builds, Atlassian, Keycloak); agent-framework (SafeDep, Socket: 20:35:20Z and 21:08:39Z); RIKEN (430 keys, 233 without passphrase); nginx2root SSA-935812; tcherber (Cyderes); PHP GHSA-g3vh and GHSA-2fjv CVE ids; USI Lugano quote against the Italian original; Fortinet FG-IR-26-219 and -194. Run record: record tallies (7 update, 9 correction, 9 improvement, 5 internal; one record per entry across 25 entries), `entities_added` (eight rows present in the registry diff), truth-pass sums (1,426 claims, 24 clean, 22 imprecision, 3 factual-error), iteration-1 and iteration-2 blocks consistent with the iteration reports. Coverage telemetry: nine KEV additions all covered; no uncovered critical or high item found.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 3, advisory: 2)

Firm: #1. Low confidence: #2 to #6 and #8.

### Findings summary (machine-readable)

See `work/2026-11-22T1407Z-audit/verification.iter3.findings.yaml`.
