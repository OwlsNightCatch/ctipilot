**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-07T05:33:55Z · ended_at=2026-11-07T05:53:04Z · duration_seconds=1149

## Verification report — 2026-11-07T0256Z-intel (iteration 4)

Scope: 7 new entries, 6 updated entries, run record. Claim ledger closed in full: `claim_ledger.py --coverage 4` reports 233/233 answered (231 ok, 2 F3 low confidence, 0 unreadable). Scope taken: all 15 changed claims, every claim of the four entries remediated since iteration 3 (Cisco SEG, WordPress, OpenSSH, Brotli) and of the run record (read in full, not ledgered), and, because the sources were open, the remaining claims of SonicWall, BOSSAI, Kaspersky, FSA, Aargau, TUM, IoT2050, ARTEX and Danfoss as well. For the unchanged older fragments of the Danfoss and ARTEX summaries I re-checked CERT-FR, ENISA, EFS, SRF, Microsoft (2026-10-21), GTIG, BleepingComputer and Expel; SentinelLABS' attribution sentence read from the gate-saved body ("Responsibility for the European incidents has not been publicly established."). Method: Rapid7 PR 22024 (page, raw-HTML merge state, `.diff` with the module documentation), PR 22018 (page, merge state, `.diff`), Rapid7 wrap-up, both Cisco SEG advisories, Cisco Node.js/Brotli advisory, CISA KEV (`cisa-kev`, catalogVersion 2026.11.06) and CISA alerts (`extract`), SonicWall PSIRT API JSON, Siemens CSAF JSON (SSA-045512, SSA-443410, SSA-834709), Mitel, NCSC.ch posts 13054 and 13155 (`ncsc-csh`), NCSC-NL, OX Security (feed `content:encoded`), Previdian (including raw-HTML timeline), Alpine, heise, The Hacker News, Picus, Wordfence, Patchstack, WordPress.org, CCCS, Acronis, Securelist, Oneconsult, Oz, TUM, ag.ch, Netzwoche, Ransom-ISAC, Unit 42, Microsoft, Check Point, VulnCheck, The Register, all via `extract` or `url`.

### Prior-iteration deltas (6 findings walked)

1. Cisco SEG F13 (stacked COPY TO PROGRAM clause): fixed. The clause is gone. The section now reports PR 22024 and states the log pattern only as that author's account: "Based on the various SQLi's I reproduced from the patch diff, the ECS SQLi (i.e. this module) was the only one that generated this matching IOC." Merge date confirmed from the page state (`mergedTime` 2026-11-05T19:41:01Z; PR 22018 `mergedTime` 2026-10-28T01:47:42Z). Every clause of the rewrite checks against PR 22024, PR 22018 and its diff, the Rapid7 wrap-up and both Cisco advisories (see claims file). One omission remains (F8 below).
2. WordPress F3 (wp-config.php check cited to The Hacker News): fixed. The wp-config.php and database check is cited to Picus (mechanism: "The replacement file can redirect the site to an attacker-controlled empty database") and the Wordfence list to The Hacker News ("administrator accounts no one recognizes", "plugins no one installed", "PHP files in wp-content/upgrade that no one put there"). OK.
3. Cisco SEG F8 (public module for the exploited flaw, poc-public, non-default statement): fixed. PR 22024 is in the section, the summary, the record summary and the CVE-2026-76461 status; "a different non-default feature" is quoted from PR 22024. OK, with the omission below.
4. OpenSSH F9 (14 from 9 vs eight from one address): fixed. The section says "the article's own total, eight attempts from one address geolocated to Japan, differs from the page's totals". Previdian: 14 attempts, 9 IPs, 8 countries; The Hacker News: "a total of eight exploitation attempts from an IP address geolocated to Japan". OK.
5. Run record F4 (KEV sweep bullet): fixed. The four legacy CVEs added on 2026-08-26 are named, with "that the 2026-08-30 audit covers in prose"; S1's digest and `docs/audits/2026-08-30-quality-audit.md` confirm. OK.
6. Brotli F11 (takeaway scope, actions[2] two vendors): fixed. The takeaway is scoped to Common Configurator (Siemens CSAF: Common Configurator on IEM "Uninstall all Management Applications and protect your IEM instance with a Firewall/WAF until a fix is available"; CC on Edge "Stop Common Configurator on Device"; six other applications carry vendor_fix versions) and actions[2] is Mitel only. OK. New wording issues are advisory F11 below.

### Citation does not support the claim

**F3 #1** (low confidence) `2026-11-07/cve-2026-111497-brotli-...` summary and `cves[CVE-2026-111497].affected/fixed`: "Siemens, Mitel and Cisco listed products that bundle the Brotli decoder flaw CVE-2026-111497 ... Cisco names Duo Network Gateway (fixed in 3.4.2) and RoomOS among products with fixes dated up to 2027". Cisco's advisory covers four CVEs in one set of tables (CVE-2026-111497, CVE-2026-105482, CVE-2026-105483, CVE-2026-106069); the fixed-release table has no CVE column and defers per-product detail to bug IDs. Duo Network Gateway 3.4.2 and the RoomOS builds are not shown to relate to the Brotli flaw. The body bullet describes the advisory accurately; the summary and CVE record bind it to one CVE. Claims 5dac0aad0d, b7031a507e.

### Unsupported / hallucinated facts

**F4 #1** (low confidence) run record, "Updates and what each moved": "Cisco Secure Email Gateway (public Metasploit module for a second injection, believed CVE-2026-76443; Cisco names no fixed 16.0 build)". Stale after the rewrite: the entry now carries two modules, among them the one merged 2026-11-05 matched at medium confidence to CVE-2026-76461, with poc-public on that CVE. The notes omit the PR 22024 module and the status move (the OpenSSH and WordPress bullets keep theirs).

### Needs more research

**F8 #1** Cisco SEG update 2026-11-07T03:49:14Z: PR 22024's module documentation (https://github.com/rapid7/metasploit-framework/pull/22024.diff) says "URL Filtering and URL Retrospective Service must both be enabled." and its scenario targets an appliance "which has the URL Filtering and URL Retrospective Service features enabled for inbound mail." The entry gives the S/MIME module's precondition ("Public-key harvesting must be enabled on the inbound mail flow policy") and calls only S/MIME "a non-default feature", but not the ECS module's, while Cisco's advisory says CVE-2026-76461 affects the gateway "regardless of device configuration". Exposure to the public exploit for the CISA-listed flaw is therefore undetermined for a reader, and the tension with Cisco's wording is a further reason for the author's "medium confidence". Fix: add the precondition and the tension to the section and the CVE status text; cite the 22024 .diff.

**F8 #2** (low confidence) Cisco SEG Triage line, actions[1], immediate_action: still present the mail_logs grep as the check ("hunt mail_logs for the exploitation pattern before assuming a device is clean") while the new section says only the ECS injection left that pattern; PR 22024 implies the S/MIME injection (same injection class in Cisco's table) does not. Say a clean grep does not exclude the S/MIME vector.

### Surface contradiction

**F9 #1** (low confidence) WordPress Exposure: "any WordPress site on 4.7 to 7.1.3" follows Wordfence; Picus says "The underlying updater and copy behavior affects WordPress 2.7.0 through 7.1.3" and The Hacker News says "the flaw goes back to WordPress 2.7". The entry adds "4.6 and earlier get no fix" without saying those sites are affected. One clause fixes it.

### Editorial / less-is-more flags (advisory)

**F11 #1** (low confidence) Brotli takeaway and actions[2]: "the advisories read report no attacks on these products" is garbled and only Cisco says it is not aware of malicious use (Siemens and Mitel are silent); "apply Mitel's workaround articles where an update is still planned" misfits Mitel's table (update planned for all seven affected products, workaround article named for three). Claims e572d697ee, fed7a5b315.

**F11 #2** (low confidence) Cisco SEG tags lack poc-public although `cves[CVE-2026-76461].status` gained it.

**F11 #3** Run record: the iteration-3 F8 summary is cut off mid-word ("...(author's medium-confidence mappin").

### Checks that passed (no finding)

SonicWall: every score, CWE, version table and the "seven flaws" count match the PSIRT JSON; CISA alert and BleepingComputer confirmed; priority `high` fits. Siemens SSA-834709 V1.1 (2026-11-04) lists the four IoT2050 variants with the quoted part numbers and fix "Update to V4.3.4-1 or later version"; CERT-FR and NCSC-NL list only the Advanced variant. Danfoss update: NCSC.ch post 13054 edit of 2026-11-06 (reason text, checklist, "does not establish a common attack method"), Ransom-ISAC (743 writes, 31 devices, 588 across 26, 155 across five, 110 and 150 degrees, default-credential statement, alert thresholds) and Unit 42 (1,853, 558, 316) all match. ARTEX update: Microsoft (Storm-3358, WISP/vshell/AdaptixC2, netcat and curl, behavioral signals, decoys) and Check Point (2,557, 1,608, ten instances exposing the database, signing-shop vulnerability list including "Missing authentication on Web APIs") match. BOSSAI, Kaspersky, FSA, Aargau, TUM claims match their sources. Entity keys of all 13 entries resolve in the registry; no IOCs, no em dashes outside the update headings, no pipeline vocabulary in reader-facing text. Source dates: the Picus page's own JSON-LD datePublished is 2026-11-04T20:53Z with "LAST UPDATED ON NOVEMBER 05, 2026" visible; the entry's 2026-11-05 is within one day.

Coverage: two WebSearch probes for in-window critical items and Swiss public-sector incidents found no gap I can name with a source; KEV window shows only CVE-2026-19868 (published).

### Verdict

NEEDS_FIXES (truth: 2, editorial: 3, advisory: 3)

### Findings summary (machine-readable)

See `verification.iter4.findings.yaml` (8 records: F8, F8, F9, F3, F4, F11, F11, F11).
