**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-12T04:38:29Z · ended_at=2026-11-12T05:04:40Z · duration_seconds=1571

## Verification report — 2026-11-12T0255Z-intel (iteration 1)

Scope read cold: the six new entries, the eight updated entries (whole entries, `git diff HEAD`, every changelog section), the run record, the claim ledger (329 rows, all walked; rows in `verification.iter1.claims.yaml`: 311 ok, 9 F3, 5 F4, 2 F14, 2 F5), the registry diff, prior_coverage.json and `state/cves_seen.json`. Pages were read from the gate's quote-bodies where cached and re-fetched otherwise (MSRC Update Guide API, CISA alerts via WebFetch, NCSC hub posts via `ncsc-csh`, Cisco, Mitel, Quest, Siemens, PDF advisories via `pdf`, NCSC-NL CSAF, the Red Hat RHSAs, the Extended Stable 11-11 post). A 120-page scan of fortiguard.fortinet.com/psirt/FG-IR-26-180..299 found exactly the 19 critical 2026-11-10 rows the Fortinet entry lists. Not findings: the Huntress post's `datePublished` is 2026-11-12T02:00Z against the entry's 2026-11-11 (one-day timezone drift); a web search found no independent coverage of the CCB, Plone or Apache items (consistent with the sourcing notes); the Publica page carries a newer "Stand: 11.11.2026" block with no new fact.

### Citation does not support the claim

1. php2shell-trend-micro-apex-quest-kace-netapp-ontap, Update 2026-11-12T04:18:00Z: "Trend Micro posted the PHP2Shell critical patches for Apex Central (build 7351) and Apex One Service Pack 1 (build 20113) on 2026-11-11, each upgrading the bundled PHP to 8.2.35" is cited to the two downloadcenter.trendmicro.com pages (prodid=1746, 1745), which carry only a date, file name and size; PHP 8.2.35 is in the readmes. The Apex One readme says only "This Critical Patch resolves a potential Remote Code Execution security issue" and never names PHP2Shell, yet title, headline, summary, this section, the record summary and actions[0] state it flatly. Cite the readmes at the clause; hedge the Apex One attribution everywhere, as paragraph 1 and sourcing_note already do.
2. cve-2026-125350-chrome..., Update 2026-11-12T04:16:00Z: "Extended Stable 156.0.8078.100 ... 72 ... four of them Critical" is cited to the Stable 157 post, which does not carry it. The page is https://chromereleases.googleblog.com/2026/11/extended-stable-update-for-desktop_01570615041.html (fetched: 156.0.8078.100, 72 fixes, four Critical rows); it is not in sources[]. Add and cite it.
3. certighost..., body para 1 (low confidence): researcher names (H0j3n, aniqfakhrul) and the 2026-07-24 PoC date sit under the MSRC citation; MSRC carries neither (names appear only inside URLs on CybersecurityNews; the date is on the Defender post).
4. certighost..., body para 2 (low confidence): "the PoC demonstrates a DCSync of the krbtgt secret"; CybersecurityNews says "this access enabled a DCSync attack extracting ... the krbtgt account hash" and separately that a PoC is on GitHub, not that the PoC demonstrates it.
5. certighost..., Update 04:17Z (low confidence): "lets the attackers authenticate as that account"; Kaspersky: "authenticate as the domain controller account".
6. plone-security-hotfix..., body para 1 (low confidence): "expects an exploit to follow quickly"; Plone: "it may not take long to turn them into a working exploit".
7. screenconnect-sckit..., body para 1 (low confidence): "the server decrypts only against the requesting machine's UUID"; Huntress: the server returns key, IV and salt "which the script uses to decrypt".
8. publica-pk-softech..., Defender takeaway (low confidence): "investment-fraud calls built on the leaked salary and pension data"; cybercrimepolice.ch is conditional ("könnten ... nutzen", "könnten auch ... betroffen sein") and names no case.

### Unsupported / hallucinated facts

1. cve-2026-111497-brotli..., actions[1], body para 1, record summary, takeaway last sentence: Teamcenter and the Opcenter family are told to "disable Brotli compression and decompression at the application or proxy layer ... and add the IIS request-filtering rule"; SSA-678870 gives Teamcenter "manual mitigation instructions ... PL8869204" and Opcenter "mitigated on the IIS Reverse Proxy ... PL8869211" (login-gated, unread), HyperLynx/PADS/Xpedition "block brotli compression at the network firewall", and Innexis Architecture Native Acceleration, Insights Hub, PAVE360 Automotive, Simcenter Executable Digital Twin/Studio only "Currently no fix is available". The "application or proxy layer" and UMC IIS wording is SSA-242944's. "a Brotli-disable or IIS request-filter mitigation for the rest" is therefore wrong for at least six software products. Scope the rule to SSA-242944 products, point to the KBs, say where no mitigation is listed.
2. gsocket-relay-client..., techniques[]: T1090.003 (Multi-hop Proxy) has no source support; Microsoft maps the relay to "T1090.002 Proxy: External Proxy". Replace.
3. cve-2026-119618-apache..., cves[].fixed "no fixed standalone mod_h2": the body says the project "names no fixed standalone release"; the project lists mod_h2 2.0.8-2.0.42 as affected and Wiz says "upgrade the module to a version newer than 2.0.42". The field asserts absence.
4. fortinet-hardening-release..., 11-11 section (low confidence): "The October builds fix them" for rows incl. FortiMail 7.2 and FortiOS 7.0 ("Migrate to a fixed release"), disproved by the entry's own 04:20Z correction; fix where it stands.

### Claims missing inline citation

1. cve-2026-119618-apache..., actions[0] and cves[].fixed: RHEL 9 mod_http2 2.0.26-7.el9_9.1 and RHEL 10 mod_http2 2.0.29-5.el10_3.1 are correct (RHSA-2026:98981 and RHSA-2026:98978, fetched) but are on neither the cited Red Hat CVE page (advisory ids only) nor anywhere in sources[]. Add the RHSAs.
2. cve-2026-119618-apache..., Detection (low confidence): "httpd child-process crashes in the error log, often after bursts of HTTP/2 requests" has no source; label it an inference or cut it.

### Needs more research

1. screenconnect-sckit..., actions[0]: the review window "since 2026-11-11" ignores BleepingComputer's quote of Huntress ("other MSPs may have been compromised earlier ... check their Run Command history even if they haven't received alerts") and the 2026-07-25 batch script that searches for rogue client ID ed630cc2c873b091. Drop the bound and add the clause.
2. certighost..., actions[0] (low confidence): the cited CybersecurityNews page gives the interim mitigation `certutil -setreg policy\EditFlags -EDITF_ENABLECHASECLIENTDC` for CAs that cannot patch at once; the entry offers only auditing for unpatched CAs while a ransomware group is attempting the exploit.

### Surface contradiction

1. cve-2026-125350-chrome..., Update 04:16Z (low confidence): the withdrawal of the second XML bug rests on the Stable post; the Extended Stable 11-09 post (cited) still lists High CVE-2026-125346 (bug 572578603) and High CVE-2026-125350 (bug 582442907) separately while the Stable post shows both bug ids under 125350. Add a Contradiction: line.

### Editorial / less-is-more flags (advisory)

1. certighost..., record 04:17Z summary ends "The summary, title, headline, action and Microsoft's exposure conditions and auditing steps move into the entry." Field-name narration; cut.
2. publica-pk-softech... (1099 words) and emudhra-intermediate-ca... (895 words): main analysis is 2x and 1.6x the 550-word bound (deep_dive false); the spawn note says all entries are within it, which is not so. The gate only warns when a fire grows a body.
3. publica-pk-softech..., summary is about 430 words against a 1-3 sentence contract.
4. gsocket..., sectors [education, technology] vs Microsoft's "do not indicate that threat actors selected these sectors deliberately"; techniques omit T1090.002, T1564.001, T1222.002 that Microsoft maps.
5. ccb-entra-id..., tag `phishing` vs "does not say how the codes were obtained".
6. screenconnect-sckit..., references[] omits entries/2026-09-12/cve-2026-84869-connectwise-screenconnect-worm-file-transfer, which Huntress's post itself links to as the September precedent.
7. cve-2026-111497-brotli..., "Cisco's advisory, version 1.8 of 2026-11-06"; the live advisory is at 1.11 (2026-11-10). The facts re-read still hold.

### Quantifier without source

1. falcon-c2..., "39 Roundcube instances in that country, none elsewhere"; Unit 42: "no evidence of any instances affected outside of the target country".
2. screenconnect-sckit..., Exposure "cloud-hosted in every reported case" (low confidence); no source says every case; ConnectWise says on-premises customers must disable the extensions by hand.
3. fortinet-hardening-release..., sourcing_note "Two pages contradict themselves" (low confidence); the Impact-field contradiction also appears on FG-IR-26-202, -207 and -216.

### Name-collision unflagged

1. falcon-c2... (low confidence): "Falcon" with no "not CrowdStrike Falcon" clause (store has product:crowdstrike-falcon and five entries on it); the extension name "PDF Viewer" equals Jewelbug's (references[] links back, body silent on whether Unit 42 treats them as the same).

### Classification missing / inconsistent

1. gsocket-relay-client...: reliability A on a Microsoft Security Blog post; sources.json rates msft-ti B (msrc-blog and msrc-update-guide are A) and the other 11 Microsoft-blog-primary entries since September are all B/2. Set B.

### Checked, no finding

Apache, Plone, CCB, Falcon, ScreenConnect and GSocket facts, versions, dates and quotes otherwise match their pages; Fortinet CVE ids and CVSS (19 rows), CISA KEV rows (CVE-2026-125350 added 2026-11-10, CVE-2026-111497 added 2026-10-27), Siemens product counts (15 + 28, eight not-affected rows), SSA-834709 V1.2, eMudhra incident-report facts (Mozilla bug comment 82, BleepingComputer), Publica/PK Softech update facts, Quest KB, NetApp and Trend advisory facts all verified. Priorities are consistent with the store's treatment of unexploited pre-auth RCEs (Apache and Plone `notable`; Chrome KEV, Fortinet, ScreenConnect, Certighost `high`). Coverage: the borderline-drop lines are defensible under PD-11; I found no missed in-window critical/high item (KEV window empty; Patch Tuesday, SAP, Ivanti EPM, Synology, Confluence already covered by earlier runs). The ConnectWise advisory (403) remains the one unread primary.

### Verdict

NEEDS_FIXES (truth: 16, editorial: 6, advisory: 7)

### Findings summary (machine-readable)

See `work/2026-11-12T0255Z-intel/verification.iter1.findings.yaml` (29 records).
