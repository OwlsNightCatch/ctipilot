**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-12T05:43:31Z · ended_at=2026-11-12T06:09:11Z · duration_seconds=1540

## Verification report — 2026-11-12T0255Z-intel (iteration 3)

Scope: all 337 ledger claims (claims.iter3.yaml; every claim of the 13 entries remediated in earlier iterations, all 28 changed claims, all 14 CCB claims), rows in `verification.iter3.claims.yaml` (337/337 answered, `tools/claim_ledger.py --coverage 3` reports 0 missing; 332 ok, 3 F4, 2 F3). Pages were re-fetched live (Chrome Releases x4, Edge notes, Siemens CSAF for SSA-834709/-242944/-678870/-443410/-045512, Cisco, Mitel, Huntress, BleepingComputer, Sophos, Unit 42, Microsoft, Red Hat, Debian, Fortinet PSIRT x20, Trend advisory raw HTML and Download Center, NCSC hub, MSRC API, Publica, PK Softech, watson, SRF) or read from the gate's cached bodies where unchanged. `check_run.py --pre-verify` re-run: 58 pass, 0 warn, 0 fail.

### Prior-iteration deltas (iteration 2 findings, all 19)

Checked against the live sources; each remediation is correct:
- IoT2050 headline: now says the flaw hit a VulnCheck canary; VulnCheck: "(Note that VulnCheck Canaries have not observed exploitation of this vulnerability in Siemens products.)" Correct. Siemens CSAF confirms V1.2, eight products, Example Image rows "Currently no fix is available", title and summary still "Industrial OS".
- ScreenConnect July script: now attributed to BleepingComputer with "its link to this campaign unclear"; BleepingComputer: "The relationship between the July malware activity and the current ScreenConnect attacks remains unclear." Correct (but see new F4/F8 on the Huntress update).
- PHP2Shell `cves[].fixed`: hedged ("its readme names no flaw"); Apex One readme: "updates the PHP module to version 8.2.35 to protect against a potential security issue" and, as a separate enhancement, "resolves a potential Remote Code Execution security issue". Correct. Trend advisory still "Last updated: 2026/11/04" with Apex Central/Apex One "Impacted - Critical Patch ETA: Nov. 11", TMMS "Nov. 17", DDAN "Nov. 12" (read from the raw table, the extract drops it).
- Brotli `cves[].fixed` and actions: scoped per advisory and checked against both CSAFs: SSA-242944 has 15 known_affected products, SSA-678870 28 affected and 8 not affected; the actions[1] list names every SSA-242944 product with no fix or no planned fix; Teamcenter, Opcenter and Process Preparation X rest on KB articles PL8869204/PL8869211; HyperLynx/PADS/Xpedition get the firewall block; Innexis, Insights Hub, PAVE360 and the two Simcenter products have no mitigation. Correct.
- Fortinet CVE-2026-126157 split from the IBE group: FG-IR-26-209 says "gain access to other users' secure email accounts", no IBE wording. Correct. The 19 critical rows: I scanned FG-IR-26-176 to -295; exactly 19 pages dated 2026-11-10 carry CVSS >= 9.0 (the 9 original + 10 added) and all 19 are listed, so the sourcing_note's completeness claim holds.
- Falcon summary and stray text: summary matches Unit 42 ("We are currently unaware of how an operator is deploying these browser extensions"); stray fragment gone (but the replacement clause is itself defective, F3/F11 below).
- GSocket hedge: Microsoft: "do not indicate that threat actors selected these sectors deliberately. Exposure is the more likely factor". Correct.
- Certighost: CertSvc restart and staging caveat now in actions[0] and the takeaway ("Restart-Service CertSvc -Force ... Test this in staging first"); "public PoC" wording matches Defender ("A public proof of concept was released on July 24, 2026"). MSRC API: Exploitation Less Likely, exploited "No", latestRevisionDate 2026-07-14.
- Apache: Red Hat's separate-allocator reason present in body and actions[0]; RHSA-2026:98981 and 98978 are "Important".
- Chrome sentence about the entry's own wording removed (but the replacement last sentence is inaccurate, F4 below).
- Plone/Apache/Roundcube/Siemens entity links: all keys exist in the registry (product:plone, product:apache-http-server, product:roundcube-webmail, seven Siemens keys). The declined Entra ID and ScreenConnect product links, the declined Apache priority, the declined KEV additions and the two over-bound main analyses are not re-raised: the KEV rows (CVE-2026-20320, -102895, -111793) carry documented borderline-drop dispositions in the 2026-11-10 and 2026-11-11 run records, and `kev_window_diff` shows no later additions.

### Citation does not support the claim

#1 (F3) `2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo`, body para 4 (claim 7c20326e6a): "a longer list whose fixes are dated November 2026 to July 2027" cited to the Cisco advisory (the paragraph now cites version 1.11 of 2026-11-10). The live v1.11 fix table dates are "Nov 2026", "Dec 2026", "Feb 2027", "Mar 2027" and "ES 202701"; "July 2027" appears nowhere on the page (raw HTML stripped and searched). The July end of the range is from an older advisory version and was kept when the revision label was updated. Fix: "November 2026 to March 2027".

#2 (F3) `2026-11-12/falcon-c2-browser-implant-government-webmail-script-tag`, body para 2 (claim 2877dffa08): "a Chrome extension named PDF Viewer, like Jewelbug's extension, which the sources read do not tie to this one, ..." cited to Unit 42. The Unit 42 page carries the extension name, developer-mode sideload, 3 to 4 minute check-ins for more than 3 weeks and the exfiltration, but does not say Jewelbug's extension is named PDF Viewer; its only Jewelbug mention is a bare "Additional Resources" link. The clause comes from the store's own Jewelbug entry and is uncited. Drop it or give it its own sentence with the Symantec source and "Unit 42 does not link the two".

### Unsupported / hallucinated facts

#3 (F4) `2026-11-12/screenconnect-sckit-toolkit-pushed-to-hundreds-of-endpoints`, summary, body para 2 and sourcing_note (claims ec90421781, bfafd5e3e6): "How the panels were reached is unknown"; "How the panels were reached is not known: Huntress's telemetry points to compromised credentials or hijacked operator sessions and it calls this abuse of legitimate functionality, not a flaw"; sourcing_note "No source says how the panels were reached ... or reconciles ConnectWise's suspicion of third-party extensions with the Run Command activity Huntress observed". The entry's own primary now carries an update block ("Update: 11/11/26 @ 11:34pm ET"): "Huntress has learned that the activity seems to be related to one of the specific extensions that had already been disabled by ConnectWise, RMM+"; "versions 1.0.31 and 1.0.32 contained a serious authentication flaw: if an administrator had never configured the extension's access key, RMM+ would accept a blank one"; "There was no corresponding login activity and the commands appeared in the logs reviewed linked to RMM+." The gate's cached copy (fetched 04:35Z) predates the update; my fetch at about 05:58Z has it (JSON-LD datePublished 2026-11-12T02:00Z, so the post itself was edited). The three statements now contradict the primary. Rewrite them; keep the BleepingComputer sentence only as Huntress's earlier position. The ConnectWise advisory returns 403 on WebFetch and every bridge transport and BleepingComputer has not picked the update up yet, so attribute the finding to Huntress alone.

#4 (F4) `2026-11-11/cve-2026-125350-chrome-xml-use-after-free-exploited-kev`, update section last sentence (claim 7b563e4d3a; same imprecision in 61f8d56cd4 and the record summary): "Google's pages disagree about whether a second XML bug was fixed." Stable 157.0.8103.50 lists one row "[TBD][572578603][582442907] High CVE-2026-125350 ... Reported by Arni Hardarson (Neonix Security) on 2026-10-12 and anonymous on 2026-11-06" and says "This update includes 9 security fixes" over 8 CVE rows, so the second bug is still counted and listed, folded into one CVE; Extended Stable 156.0.8078.96 lists "[572578603] High CVE-2026-125346" and "[582442907] High CVE-2026-125350". They disagree on the CVE id of bug 572578603, not on whether it was fixed. Reword accordingly.

#5 (F4, low confidence) `2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail`, Detection: "OSPF or BGP events from routers that are not configured neighbours". FG-IR-26-268 (CVE-2026-126254, Attack Type Authenticated): the flaw "may allow a configured ibgp neighbor to send malicious/malformed attributes", so the sender is a configured peer; the "not configured neighbours" test fits OSPF (FG-IR-26-267) only. Unlabelled composer inference; split the clause.

### Quantifier without source

#6 (F14, low confidence) same entry, summary tail and body para 1: "no Fortinet page states exploitation". The entry cites FG-IR-26-175, which says "This has been reported to be exploited in the wild" for CVE-2026-104286, and itself says the FortiMail builds "also fix the exploited CVE-2026-104286". All 19 advisories of 2026-11-10 show "Known Exploited: No", so scope the quantifier to those advisories.

### Needs more research

#7 (F8) `2026-11-12/screenconnect-sckit-toolkit-pushed-to-hundreds-of-endpoints`, Exposure, Detection, takeaway and actions[0]: the Huntress update supplies the discriminator a defender needs (RMM+ 1.0.31 and 1.0.32 accept a blank access key when `RMMPlus.AccessKey` was never set; RMM+ "bypasses ScreenConnect's user accounts, roles, and MFA"; most RMM+ installs were legitimate; the commands showed no login activity). The action should add checking whether RMM+ is installed with an empty access key and rotating it, beside disabling the five extensions. Only Huntress carries this, so state it as Huntress's finding.

### Editorial / less-is-more flags (advisory)

#8 (F11) `2026-10-23/fortinet-...`: the 2026-11-11 section still says "as the correction below sets out", but the 2026-11-12 record is now typed update with a "## Update" heading; and the 11-12 section's last sentence ("The earlier remark ... was wrong ... and the feed the earlier text relied on is capped at 50 advisories ...") plus the record summary ("an earlier remark that no FortiOS 7.0 row exists was wrong") narrate the entry's own earlier wording and the pipeline's feed cap. Reword the pointer to "the update below" and cut the narration, keeping that two tables list FortiOS 7.0.

#9 (F11) `2026-11-12/falcon-...`: the PDF Viewer clause is hard to parse (relative clause hanging inside the subject) and uses "the sources read"; the Chrome sourcing_note has "in the sources read". Use "cited" and give the Jewelbug note its own sentence.

### Missed angles

None to raise. Re-read the live KEV catalogue (catalogVersion 2026.11.10, count 1779): 2026-11-09/10 additions are all covered by entries (Barracuda ESG, OpenSSH, FreeSWITCH, IBM Aspera, Outlook, Chromium) or carry documented borderline-drop dispositions (BroadWorks XXE, GPUStack, Openwave); Patch Tuesday, Confluence, Ivanti EPM, Synology, Xen Orchestra, Adobe Connect and SAP are already in the store. Coverage looks complete for the critical/high signal I can name.

### Other checks with no finding

- ATT&CK mappings (GSocket T1090.002 and the rest, Falcon, Plone, Apache): each id follows a behavior the sources state; the extra GSocket ids (T1219, T1573, T1546.004, T1068, T1036.011) are supported by Microsoft's text (open-source remote access tool, end-to-end encrypted channel, shell profiles, Dirty Frag attempt, exec -a).
- Classification: Falcon B/2, GSocket B/2 (msft-ti), ScreenConnect B/1 (Huntress and Sophos independent), Apache A/2, Plone A/2, CCB A/2: consistent with sources and corroboration shown.
- Priorities: Apache and Plone stay notable under the store's unexploited-RCE convention (Wiz: no exploit at publication; HTTP/2 and mod_http2 are opt-in on Apache); not re-raised.
- Style: no em dash in any reader-facing field (the one in eMudhra is inside a verbatim OpenJDK quote), no IOCs, no field names or registry keys in prose.
- eMudhra and Publica: all 2026-11-12 sections verified against the Mozilla bug report (RSA key material "handled within the volatile memory of a Python process", cessationOfOperation on 7 Nov, May 2026 production start, last G2C certificate 3 Nov, Action Item 2 due 04-Dec-2026), BleepingComputer, Publica "Stand: 10.11.2026", PK Softech's 2026-11-10 notice, watson 2026-11-11 and SRF 2026-11-10. The main-analysis word counts stay over bound (declined twice; advisory only, left to the audit).

### Verdict

NEEDS_FIXES (truth: 6, editorial: 1, advisory: 2)

The ScreenConnect finding (#3, #7) is the one that matters before publishing: the primary source changed after the gate fetched it and now names the likely access path of a `high` entry.

### Findings summary (machine-readable)

See `work/2026-11-12T0255Z-intel/verification.iter3.findings.yaml` (9 records: F4 x3, F3 x2, F14, F8, F11 x2).
