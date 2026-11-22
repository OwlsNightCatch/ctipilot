**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-22T15:42:30Z · ended_at=2026-11-22T16:05:48Z · duration_seconds=1398

## Verification report — 2026-11-22T1407Z-audit (iteration 2)

Scope: post-fix pass. Deltas block walked first (every `verify_in_this_iteration: true` item re-read against a page fetched this pass). Ledger: 108 required claims (29 changed plus every claim of the Puppet, vCenter, Brotli, BundID, Synology, timeroasting, N-able, Java4Shell, OptimJack and Oracle entries) all answered, plus 88 of the remaining 97 claims of the other 17 entries (LiteLLM, ScreenConnect, Danfoss, Expressway, ARTEX, Fortinet, Symantec, RIKEN, Drupal, agent-framework, nginx, tcherber, PHP, MONAI and the Confluence record); 196 rows in `verification.iter2.claims.yaml` (191 ok, 2 F3, 2 F4, 1 F5). Nine claims outside the required scope were not answered (the USI and Basel record summaries on Italian and German originals, four Fortinet rows citing FortiMail and FortiOS advisories, the Symantec derived Detection line, one nginx row citing CERT.at and Wiz, one PHP row citing GHSA-qc49). Pages were re-fetched this pass (extract, raw `url` where the extract drops tables or sidebars, `cisa-kev` for the catalogue, `WebFetch` for the two CISA alerts, `pdf` for the BSI notice). Evidence quotes of all 27 entries were re-checked against the cached and fresh pages: no non-contiguous quote on the changed text.

### Delta verification (iteration 1 findings)

- Puppet F4 (OpenVox Server removed): remediation holds for cves[], action and section (GHSA-ffr6-rwpm-p5wq lists OpenVox Agent <= 9.2.0 and <= 8.31.1, patched 9.3.0 and 8.32.0, and OpenVox Server <= 9.1.0 and <= 8.17.0, patched 9.2.0 and 8.18.0), but the rewritten record summary introduced a new false clause (finding #1).
- vCenter "does not state exploitation": holds; neither the VMSA page nor the Q&A (Q19 "Not as listed by Broadcom") says anything about exploitation of the vCenter flaw.
- Brotli takeaway and evidence quote: hold (Mitel rev 6.0: "Update to V11R3.4.5. Workaround available, see KB article"; SESAP and Contact Center keep planned updates and workarounds).
- BundID sourcing_note and the e-mail-code clause: hold; the clause now cites Spiegel, which quotes the site notice ("Sie erhalten nun bei jeder Anmeldung mit 'Benutzername & Passwort' zusätzlich einen Sicherheitscode per E-Mail"), and heise and Handelsblatt keep only the switch-off.
- Synology "does not mention exploitation" and the 6.2.4 build: hold (the product table has no DSM 6.2 row).
- Timeroasting Exposure: holds; scoped to Windows DCs, one tested DC, Samba without the extended form.
- N-able dateline 2026-11-13: holds ("Published Time: 2026-11-13T22:59:21+00:00"; the agent-impersonation passage sits under "Publication 2: November 12").
- vCenter vSphere Foundation scope: holds for vSphere Foundation; VCF Installer 5.x remains (finding #3).
- Java4Shell labels: hold (five source labels read "Calif"; Oracle credits Albert Yang and Quang Luong of Calif.io; Calif's page says "Discovered and reported by Calif").
- OptimJack "registrar hold (clientHold)": holds (Report URI update 17 Nov 09:17 UTC: "put on `clientHold` at 17 Nov 00:37 UTC").
- Oracle takeaway: the takeaway holds, but Exposure and actions[0] were not aligned (finding #6). Oracle title: holds.
- Eleven record summaries rewritten: no pipeline vocabulary left except two bookkeeping phrases (finding #8).
- Run record stamps: `completed` 15:42:01Z follows every new entry's `discovered_at` (15:05:00Z, 15:08:00Z); the Phase 6 re-stamp is still pending, as stated.
- Audit report figures: hold (49 scoped entries carry 15 high; 8 of the 34 new; 24/22/3 and 1,426 claims reproduce from truth-T*.yaml; G1 returned 15 items, 14 droppable and all 14 now named; actions counts 10/19/4/1; technique densities 11.0/3.0/2.9), apart from the denominator nit (finding #10).
- Declined F10 (Metabase, Adobe Animate): reason holds; not re-raised.

### Citation does not support the claim

- #3 (F3, low confidence) vCenter `cves[CVE-2026-123893].affected`: "SDDC Manager and VCF Installer in VMware Cloud Foundation 9.1, 9.0 and 5.x and in VMware vSphere Foundation 9.1 and 9.0". VMSA-2026-0009 lists "SDDC Manager / VCF Installer" for 9.1.x.x and 9.0.x.x (VCF, VVF) but the 5.x row is "VMware Cloud Foundation | SDDC Manager | 5.x | 5.2.5" only. Scope VCF Installer to 9.1 and 9.0.
- #4 (F3, low confidence) N-able Update 2026-11-22T14:52:29Z: "CISA added the Apache Axis flaw CVE-2026-90436, the entry point of 4EverAble2Shell, ... ([CISA, 2026-11-18])". The alert lists "CVE-2026-90436: Apache Axis, Unsafe Reflection Vulnerability" and names neither N-central nor 4EverAble2Shell. Cite the tie to BleepingComputer, Huntback and the Apache announcement, or reword.

### Unsupported / hallucinated facts

- #1 (F4) Puppet correction record and audit report: "OpenVoxDB's fixed versions come from OpenVox's release notice, not from the pages first given for them" and "OpenVoxDB clause cited to pages that do not name it". GHSA-q4hm-33rc-572g (raw page) lists "OpenVoxDB (OpenVox/Puppet) <= 9.1.0 and <= 8.17.0 | 9.2.0 and 8.18.0"; only SecurityWeek lacked the versions. The old citation was supportable; drop the provenance clause and fix the report row.
- #2 (F4, low confidence) Oracle headline "... Brotli rows exploited": CISA lists the Brotli CVE (KEV 2026-10-27); Oracle flags no row and the body says "no exploitation of the other rows is reported"; no source reports exploitation of the Oracle builds. Reword to "CISA lists the Brotli flaw behind three rows".

### Claims missing inline citation

- #5 (F5, low confidence) Synology Exposure: "the running version is shown in the DSM control panel." No citation; the advisory does not say it.

### Needs more research

- #6 (F8, low confidence) Oracle: the takeaway leads with "Communications Diameter Signaling Router, Communications Unified Assurance and PeopleSoft PeopleTools first", but actions[0] still reads "apply the November 2026 CSPU first to internet-reachable Access Manager, WebLogic Server, E-Business Suite and APEX or REST Data Services instances" and Exposure omits the three products. Align them.

### Missed angles

- #7 (F10) Brotli entry, in-window publisher revision on an edited entry. Siemens SSA-045512 is now V1.3, Last Update 2026-11-18: "V1.3 (2026-11-18): Added SENTRON Powermanager V8 and V9, SICAM PAS CC, SICAM SCC, and IPAS Tester to the list of affected products." SICAM PAS CC (>= V6.02) and SICAM SCC (>= V7.01): "Currently no fix is planned. Temporarily disable Brotli compression and decompression at the application or proxy layer"; SENTRON Powermanager V8/V9 and IPAS Tester: "Install the latest .NET security updates via Windows Update." The entry still says "Siemens' advisory SSA-045512, revised on 2026-11-06, lists Desigo CC V8 and V9 ... Gridscale X ..."; cves[].affected, fixed, body and actions omit all five, and no entry names SICAM or SENTRON. Cisco's Brotli advisory is now version 1.14 of 2026-NOV-17 against the entry's "version 1.13 of 2026-11-13" (delta not itemised on the page, low confidence). Search: Siemens ProductCERT SSA-045512 history. This is the audit's own publisher-revision theme and the fire's Mitel update touched the entry.

### Editorial / less-is-more flags (advisory)

- #8 (F11) Record summaries: Drupal "... and the entry moves to high." and Brotli "... the SBC action moves from workaround to update." Field bookkeeping; state the reader-facing change.
- #9 (F11) vCenter: the CISA KEV sentence now sits in the main analysis and again as the first sentence of the Improvement section and record summary.
- #10 (F11) Audit report systemic item 3: "14 of 331 iterations"; with this run's own iteration 1 the store has 332 iterations with both counters (14 mismatches, none CLEAN).
- #11 (F11) Synology sourcing_note: "a news site restates it without adding anything" names and cites no site; "is the state recorded here" is record-keeping phrasing.

### Checked and holding

Whole-entry reads of the two recovered entries (Synology-SA-26:21: table rows, revisions, CWE-88, CVSS 3.1 9.8, 6.2.4 build, OnGoing rows; timeroasting: every Huntress claim including eleven runs over five hours, 5156, own-RID rule, 120-byte form, Samba, Triage lines) and the changed sections of the 25 updated entries against fetched primaries: Mitel rev 6.0 rows; Cisco Expressway (two separate causes); Drupal feed item (Highly critical 20 of 25, E:Exploit, 2026-11-19 19:00 UTC); Oracle matrices (655 patches, 62 rows at 9.0+, 56 unauthenticated, six at 10.0, three Brotli rows); KEV dates (CVE-2026-111497 2026-10-27, CVE-2026-109619 2026-10-26, CVE-2026-115731 2026-11-17, CVE-2026-123890 2026-11-20, CVE-2026-40217 and CVE-2026-90436 2026-11-18, CVE-2025-61882 ransomware-known); RIKEN notices; SafeDep and Socket; Report URI, Ohey and Hudson Rock; Symantec; Siemens SSA-935812 and SSA-443410, SSA-242944 (15 products); PHP GHSA pair and ChangeLog (18/14/13/12/18 CVEs); MONAI advisory; tcherber/Cyderes; Danfoss/AFP; ARTEX sources; FortiGuard FG-IR-26-194; GTIG ARMORY CASTLE and LLMjacking; VulnCheck 8.7; Keycloak, Atlassian, Oracle credits, Calif page (JVM options sit in a collapsed block the extract drops; raw page carries them). The 25 records: 7 update, 10 correction, 8 improvement, 5 internal; `updated_at` mirrors only the seven updates. Coverage telemetry: no uncovered critical or high item found beyond finding #7; the droppable list holds (Poste.io has no exploitation stated; Rootways is a Magento extension outside the constituency).

### Verdict

NEEDS_FIXES (truth: 4, editorial: 3, advisory: 4)

Firm: #1 and #7. Low confidence: #2 to #6.

### Findings summary (machine-readable)

See `work/2026-11-22T1407Z-audit/verification.iter2.findings.yaml`.
