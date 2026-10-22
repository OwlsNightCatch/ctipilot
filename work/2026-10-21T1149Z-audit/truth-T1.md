**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T11:57:16Z · ended_at=2026-10-21T12:21:33Z · duration_seconds=1457

## Truth report T1 (retrospective pass, run 2026-10-21T1149Z-audit)

### 2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days — factual-error

1. **headline / title / summary** (factual-error)
   - Claim: public PoC, no patch, TPM-only BitLocker bypassed ; Windows BitLocker "YellowKey" zero-day (no CVE) ... no patch available
   - Defect: Superseded and, for "no CVE", contradicted by the entry itself: the 2026-05-20 section records CVE-2026-45585, and Microsoft shipped the YellowKey fix in the June 2026 updates. The body never records GreenPlasma's CVE or fix either.
   - Ground truth: MSRC CVE-2026-45585 revision 2 (2026-06-09): "Added links to June 2026 Windows security updates. Microsoft recommends installing this updates as soon as possible." Fixed builds in the MSRC table: KB5094125 (Windows Server 2025, 10.0.26100.32995), KB5094126 (Windows 11 24H2 10.0.26100.8655, 25H2 10.0.26200.8655), KB5095051 (Windows 11 26H1, 10.0.28000.2269). GreenPlasma is CVE-2026-45586 (CTFMON EoP, CWE-59, CVSS 7.8), released 2026-06-09. BleepingComputer 2026-06-10: "On Tuesday, Microsoft fixed the GreenPlasma, MiniPlasma, and YellowKey security vulnerabilities as part of its June 2026 Patch Tuesday updates". <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585>
   - Fix: Through a changelog record, move headline, summary and actions to the current state: YellowKey = CVE-2026-45585, fixed 2026-06-09; GreenPlasma = CVE-2026-45586, fixed 2026-06-09; drop "no CVE" and "no patch".

2. **cves[CVE-2026-45585]** (factual-error)
   - Claim: status: [poc-public, mitigation-only]; affected: null; fixed: null
   - Defect: A security update has been available since 2026-06-09, so mitigation-only is false; MSRC publishes the affected products and fixed builds. id and cvss 6.8 and physical vector / pre-auth (PR:N) are correct.
   - Ground truth: MSRC record: baseScore 6.8, vector CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:W/RC:C, exploited "No", publiclyDisclosed "Yes", "Exploitation More Likely"; remediation table lists Windows 11 24H2/25H2/26H1 and Windows Server 2025 only (no Windows Server 2022). Not in CISA KEV (catalogue 2026.10.20). <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585>
   - Fix: Set status to patch-available (poc-public may stay), fill affected and fixed from the MSRC table; exploited stays No.

3. **actions[0] and actions[1]** (factual-error)
   - Claim: YellowKey (no CVE) bypasses TPM-only BitLocker ... Disable WinRE access where operationally viable (`reagentc /disable`). ; Microsoft's WinRE `BootExecute` registry mitigation is per-device and fragile under Windows feature updates that re-stage WinRE ... Public PoC, no patch (MSRC CVE-2026-45585)
   - Defect: "No CVE" and "no patch" are stale, and the MSRC page cited for "no patch" now links the June 2026 updates; the reagentc /disable advice and the claim that the mitigation is fragile under feature updates appear in no cited source (MSRC's own script uses reagentc to mount, then disable and re-enable WinRE to re-seal BitLocker trust).
   - Ground truth: BleepingComputer: Beaumont "recommended using a BitLocker PIN and a BIOS password"; NCSC-CH #12574: "Implement BIOS passwords and setting a BitLocker PIN mitigates the current public PoC". MSRC FAQ: "if you are using TPM+PIN the vulnerability is not exploitable." No source mentions feature updates re-staging WinRE. <https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/>
   - Fix: Replace both actions with one task derived from the sources (BitLocker PIN plus BIOS password on TPM-only laptops, or install the June 2026 update); delete reagentc /disable and the fragility claim.

4. **body paragraph 1** (factual-error)
   - Claim: Microsoft states it is "actively investigating."
   - Defect: The quoted phrase is in none of the cited sources (BleepingComputer, The Register, NCSC-CH, MSRC); it is an invented quotation.
   - Ground truth: BleepingComputer: a Microsoft spokesperson "stated that the company is committed to investigating reported security issues, "and update impacted devices to protect customers as soon as possible."" <https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/>
   - Fix: Quote the BleepingComputer statement verbatim or remove the quotation marks.

5. **body paragraph 1** (imprecision)
   - Claim: bringing the total of unpatched Nightmare Eclipse Windows zero-days to four
   - Defect: No cited source states four. BleepingComputer says two unpatched flaws and says RedSun was silently patched; The Register counts five zero-days this year with RedSun and UnDefend unfixed. Four is the entry's own subtraction over sources that disagree on RedSun.
   - Ground truth: The Register 2026-05-13: "YellowKey and GreenPlasma are the latest in a series of five Microsoft zero-day bugs the researcher has exposed this year ... Both RedSun and UnDefend remain unfixed"; BleepingComputer: "Microsoft silently patched the RedSun vulnerability". <https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758>
   - Fix: Drop the total, or attribute it to The Register and note the BleepingComputer disagreement on RedSun.

6. **body paragraph 1 (YellowKey mechanism and affected scope)** (imprecision)
   - Claim: crafted `FsTx` folder contents placed on a USB drive or the EFI partition are replayed by WinRE ... The current public PoC defeats TPM-only BitLocker configurations on Windows 11 and Windows Server 2022/2025; the researcher asserts the full bypass also defeats TPM+PIN but the unpublished variant is unconfirmed.
   - Defect: Three omissions: (1) Dormann could reproduce only with the USB drive, not the EFI partition; (2) Microsoft states TPM+PIN is not exploitable and Dormann says the public exploit does not work with TPM+PIN, a researcher-versus-vendor contradiction the entry never surfaces; (3) MSRC lists Windows 11 24H2/25H2/26H1 and Windows Server 2025 only, so "Windows Server 2022" is the researcher's and BleepingComputer's claim, not the vendor's affected list.
   - Ground truth: BleepingComputer: Dormann "could not reproduce the bug using the EFI partition"; "the current YellowKey exploit does not work in a TMP+PIN environment". MSRC FAQ: "No, if you are using TPM+PIN the vulnerability is not exploitable." <https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/>
   - Fix: State USB confirmed, EFI-partition variant claimed but not reproduced; add a Contradiction line (researcher claims TPM+PIN bypass, Microsoft says not exploitable); scope the product list to the MSRC table.

7. **body paragraph 1** (imprecision)
   - Claim: deleting `winpeshl.ini` — the file that suppresses the recovery shell
   - Defect: No source says what winpeshl.ini does, and the BleepingComputer quotation implies the opposite: with the file deleted, WinRE opens a command prompt instead of the recovery environment, so the file is what launches the recovery environment.
   - Ground truth: Dormann (BleepingComputer): "The result of this is that the X:\Windows\System32\winpeshl.ini is deleted, and when Windows Recovery is entered, rather than launching the actual Windows Recovery environment, it pops up a CMD.EXE. With the disk still unlocked". <https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/>
   - Fix: Say "deleting winpeshl.ini, so WinRE opens CMD.EXE with the disk unlocked instead of the recovery environment".

8. **body paragraph 1 (ATT&CK) and frontmatter techniques[]** (imprecision)
   - Claim: MITRE ATT&CK: T1542.001 (Pre-OS Boot: System Firmware), T1006 (Direct Volume Access). ; techniques: []
   - Defect: techniques[] is empty while the body names four ids. T1542.001 names a behavior no source describes: YellowKey replays NTFS transaction logs in WinRE and no firmware is modified. All four ids are active in ATT&CK v20 (checked: T1542.001, T1006, T1134, T1068); T1006 is also a weak fit (low confidence).
   - Ground truth: Dormann (BleepingComputer): "Windows looks for \System Volume Information\FsTx directories on attached drives, and will replay any NTFS logs". <https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/>
   - Fix: Drop T1542.001 from the prose and carry the supported mapping in techniques[].

9. **body paragraph 1 (Immediate mitigations)** (imprecision)
   - Claim: set BIOS/UEFI boot password and disable USB/external-media boot; disable WinRE where operationally viable (`reagentc /disable`)
   - Defect: The cited sources give a BitLocker PIN and a BIOS password only; disabling USB/external-media boot and `reagentc /disable` are uncited.
   - Ground truth: BleepingComputer: "He recommended using a BitLocker PIN and a BIOS password as a mitigation." NCSC-CH: "Implement BIOS passwords and setting a BitLocker PIN". <https://security-hub.ncsc.admin.ch/#/posts/12574>
   - Fix: Cite a source for the extra items or delete them.

10. **section 2026-05-20T05:00:11Z** (imprecision)
   - Claim: Microsoft's interim mitigation requires per-endpoint work on every device using TPM-only BitLocker ... mount the WinRE image, remove the `autofstx.exe` entry ... ; add a BitLocker PIN or password protector ... The WinRE registry edit is fragile and breaks on Windows feature updates
   - Defect: MSRC says Microsoft "recommends that you consider" the mitigation, not that it is required on every device; MSRC replaced the manual steps with a script on 2026-05-21 (revision 1.2), so the described manual procedure is superseded; no source says feature updates break the edit; MSRC names TPM+PIN, not a "password protector".
   - Ground truth: MSRC revision 1.2 (2026-05-21): "Added a script to implement a mitigation and removed the manual mitigations." FAQ: "Microsoft recommends that you consider implementing these mitigations if you are concerned your devices and data are at risk of being compromised or stolen." <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585>
   - Fix: Describe the MSRC script, say it is recommended where theft risk exists, and drop the fragility claim and "password protector".

11. **frontmatter** (imprecision)
   - Claim: classification: null ; affected_products: [] ; sectors: [public-sector, defense, education] ; event_date: 2026-05-14
   - Defect: No Admiralty rating and no affected_products although the body names Windows 11 and Windows Server; the sectors appear in no cited source; event_date is a day after the primary's publication.
   - Ground truth: BleepingComputer datePublished 2026-05-13T12:37:49-04:00; no cited source names a sector. <https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/>
   - Fix: Add classification and affected_products, drop the unsupported sectors, align event_date with 2026-05-13.

12. **priority** (imprecision)
   - Claim: priority: high
   - Defect: Context only: on today's facts the flaw is a physical-attack-only bypass (CVSS 6.8, AV:P), MSRC lists it exploited "No", it is not in CISA KEV and has been fixed since 2026-06-09, so it no longer meets the high bar.
   - Ground truth: MSRC: exploited "No"; "bypass a security feature with a physical attack". <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585>
   - Fix: Re-grade when the entry is brought to the current state.

### 2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes — factual-error

1. **title / headline** (factual-error)
   - Claim: Microsoft's Digital Crimes Unit threatens criminal action
   - Defect: Overstates the statement and silently picks the stronger of two source readings. Microsoft wrote that its Digital Crimes Unit "will continue bringing cases"; The Record says Microsoft "stopped short of directly threatening legal action"; heise reads it as threatening lawsuits and the police. No cited source says "criminal action" (the words "criminal activity" describe the researchers' targets, the attackers).
   - Ground truth: MSRC blog 2026-05-27: "Our Digital Crimes Unit will continue bringing cases against these actors and those that enable their criminal activity – coordinating as needed with law enforcement around the world." The Record: "The company stopped short of directly threatening legal action". heise: "The company is threatening lawsuits and the police." <https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more>
   - Fix: Headline: "Microsoft warns its Digital Crimes Unit will keep bringing cases"; add a Contradiction line that The Record and heise read the statement differently.

2. **summary / body paragraph 1** (factual-error)
   - Claim: Microsoft's Digital Crimes Unit issued a formal public statement on 28–29 May 2026
   - Defect: Wrong date and issuer. The statement is a Microsoft Security Response Center blog post dated 2026-05-27 (a Wednesday), with the Digital Crimes Unit named in one sentence; The Record and heise reported it on 2026-05-29.
   - Ground truth: MSRC blog "A shared responsibility: Protecting customers through Coordinated Vulnerability Disclosure", date 2026-05-27. The Record 2026-05-29: "In a blogpost on Wednesday, Microsoft said". <https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure>
   - Fix: Write "Microsoft (MSRC) published a statement on 27 May 2026, reported by The Record on 29 May".

3. **body paragraph 1** (factual-error)
   - Claim: responded by threatening a new vulnerability release on 14 July 2026 (the next Patch Tuesday)
   - Defect: 14 July is the Patch Tuesday after next (the next one after 29 May was 9 June 2026), and The Record gives no causal link between Microsoft's statement and the threat.
   - Ground truth: The Record: "The researcher threatened a further release on July 14 — the date scheduled for Microsoft's Patch Tuesday". BleepingComputer 2026-06-10: Microsoft fixed the flaws "On Tuesday ... as part of its June 2026 Patch Tuesday updates" (9 June). <https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more>
   - Fix: Drop "responded" and "the next"; write "threatened a further release on 14 July 2026, the July Patch Tuesday".

4. **body paragraph 3** (factual-error)
   - Claim: Next Patch Tuesday: 10 June 2026.
   - Defect: June 2026 Patch Tuesday was 9 June 2026 (second Tuesday), not 10 June.
   - Ground truth: BleepingComputer 2026-06-10: "On Tuesday, Microsoft fixed the GreenPlasma, MiniPlasma, and YellowKey security vulnerabilities as part of its June 2026 Patch Tuesday updates"; MSRC revisions dated 2026-06-09. <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/>
   - Fix: Change to 9 June 2026, or drop the sentence now that the date has passed.

5. **cves[CVE-2026-45585]** (factual-error)
   - Claim: cvss: n/a; type: lpe; vector: local; auth: post-auth; status: [poc-public, no-patch]
   - Defect: CVE-2026-45585 is YellowKey, a BitLocker security feature bypass by physical attack with CVSS 6.8 and PR:N, not a local privilege escalation; the body itself calls it a "BitLocker bypass ... requiring physical access". It has also been patched since 2026-06-09, so no-patch is false.
   - Ground truth: MSRC: "Windows BitLocker Security Feature Bypass Vulnerability", CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, "bypass a security feature with a physical attack"; revision 2 (2026-06-09): "Added links to June 2026 Windows security updates". <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585>
   - Fix: Correct the record (security feature bypass, physical, 6.8, pre-auth, patched) or drop the cves[] record: the entry is about Microsoft's disclosure statement, and YellowKey has its own entry.

6. **title / cves[].status / body paragraph 2** (factual-error)
   - Claim: GreenPlasma and MiniPlasma (cldflt.sys SYSTEM escalation) remain unpatched ; YellowKey ..., GreenPlasma (LPE class), and MiniPlasma remain unpatched as of 30 May 2026
   - Defect: Undated in the title and in cves[].status, and false today: Microsoft fixed all three on 2026-06-09. The body sentence is true only as of 30 May 2026 and the entry carries no update.
   - Ground truth: YellowKey = CVE-2026-45585 (KB5094125 Server 2025 10.0.26100.32995; KB5094126 Windows 11 24H2 10.0.26100.8655 / 25H2 10.0.26200.8655; KB5095051 26H1 10.0.28000.2269). GreenPlasma = CVE-2026-45586, CTFMON EoP, CWE-59, CVSS 7.8, released 2026-06-09 (e.g. Server 2022 10.0.20348.5256 KB5094128). MiniPlasma = addressed by the 2026-06-09 re-release of CVE-2020-17103: "To comprehensively address the vulnerability identified by CVE-2020-17103 and recently publicly referred to as "Mini-Plasma" Microsoft recommends installing the June 2026 updates". None of the three is in CISA KEV. <https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/>
   - Fix: Record the 2026-06-09 fixes through a changelog record and remove "remain unpatched" from the title and status.

7. **headline** (imprecision)
   - Claim: GreenPlasma and MiniPlasma (cldflt.sys SYSTEM escalation)
   - Defect: cldflt.sys is the MiniPlasma component only; GreenPlasma is a CTFMON flaw. The cited heise article conflates them ("both tracing back to CVE-2020-17103").
   - Ground truth: BleepingComputer: GreenPlasma is a "Windows CTFMON Arbitrary Section Creation Elevation of Privileges Vulnerability"; MiniPlasma "impacts the 'cldflt.sys' Cloud Filter driver". MSRC CVE-2026-45586: "Windows Collaborative Translation Framework (CTFMON) Elevation of Privilege". <https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/>
   - Fix: Tie cldflt.sys to MiniPlasma only.

8. **body paragraph 2** (imprecision)
   - Claim: the root cause is assessed as an incomplete remediation of CVE-2020-17103 (no CVE yet assigned to MiniPlasma itself)
   - Defect: Uncited and unattributed: the incomplete-fix claim is the researcher's (BleepingComputer 2026-05-17), later confirmed in effect by Microsoft's re-release of CVE-2020-17103; "assessed" hides who assessed it.
   - Ground truth: BleepingComputer 2026-05-17: Chaotic Eclipse says "the exact same issue that was reported to Microsoft by Google project zero is actually still present, unpatched". MSRC CVE-2020-17103 revision 2 (2026-06-09): "This CVE has been re-released to comprehensively address the vulnerability identified by CVE-2020-17103". <https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/>
   - Fix: Attribute to the researcher and cite BleepingComputer; add the June 2026 fix.

9. **summary / body / sourcing_note** (imprecision)
   - Claim: UPDATE (originally covered 2026-W21) ; migration: update target unresolved (no originally-covered date in v2 body) ; summary ends "(The Record …"
   - Defect: Workflow-internal text in reader-facing fields, a reference to a weekly entry that no longer exists, and a summary cut off mid-sentence.
   - Ground truth: n/a (entry text) <https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more>
   - Fix: Rewrite in plain prose and complete the summary.

10. **body paragraph 3** (imprecision)
   - Claim: Defenders on Windows 11 estates should monitor for `cldflt.sys`-related anomalies and consider AppLocker/WDAC policies blocking unsigned executables from low-privileged user sessions while patches are pending.
   - Defect: Uncited; the only detection guidance in the sources is ThreatLocker's registry-key monitoring (BleepingComputer 2026-05-17 update), and the advice is now moot because MiniPlasma was fixed on 2026-06-09.
   - Ground truth: BleepingComputer: ThreatLocker "organizations should monitor the following Registry keys for modifications using their EDR platform to detect exploitation". <https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/>
   - Fix: Cite the source detection guidance or drop the sentence when the entry is brought to the current state.

11. **frontmatter** (imprecision)
   - Claim: classification absent; techniques absent; affected_products absent; sectors: []
   - Defect: No Admiralty rating, no ATT&CK mapping and no affected products although the body names Windows 11 and its components.
   - Ground truth: n/a (frontmatter) <https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more>
   - Fix: Add classification (multi-source: The Record, heise, MSRC) and the structured fields.

### 2026-05-25/ghost-cms-cve-2026-26980-clickfix-the-cms-compromise-to-endp — imprecision

1. **body, Exposure line** (imprecision)
   - Claim: **Exposure:** self-hosted Ghost from 3.24.0 to 6.19.0
   - Defect: The cited advisory gives the range without any hosted or self-hosted distinction; no cited source says Ghost(Pro) was unaffected or patched server-side, so "self-hosted" is an uncited qualifier on the exposure.
   - Ground truth: Ghost advisory: "This vulnerability is present in Ghost v3.24.0 to v6.19.0." BleepingComputer: "many sites failed to install the security update." <https://github.com/TryGhost/Ghost/security/advisories/GHSA-w52v-v783-gw97>
   - Fix: Write "Ghost from 3.24.0 to 6.19.0" and say how to tell (the running Ghost version), without "self-hosted" unless a Ghost statement is found.

2. **summary** (imprecision)
   - Claim: XLab counts more than 700 sites whose Admin API keys were stolen and whose posts were injected
   - Defect: XLab counts more than 700 poisoned victim domains (confirmed in its 2026-05-17 enumeration); the Admin API key theft is described for the observed chain, and XLab does not say how the second actor it found gained access, so "whose Admin API keys were stolen" is not XLab's count. The body's "more than 700 by its report of 2026-05-21" is true but the as-of date of the figure is 2026-05-17.
   - Ground truth: XLab: "we have cumulatively identified more than 700 poisoned victim domains"; timeline: "2026-05-17: Second Round of Compromised Site Enumeration Completed: 700+ victim domains confirmed". <https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/>
   - Fix: Say "more than 700 poisoned domains, per XLab's 2026-05-17 enumeration".

3. **updates[0].summary (2026-10-11 correction)** (imprecision)
   - Claim: the file name, the 2024 ClickFix history, the region and sector, the Ghost(Pro) statement and the self-quoted evidence had no source
   - Defect: Five of the six items are right (checked: no source for the 2024 history, region, sector or Ghost(Pro)), but the file name did have a source: BleepingComputer and XLab both name the Electron payload; it was removed under the no-file-name-indicator rule, not for lack of a source (low confidence on which file name the record means).
   - Ground truth: BleepingComputer: "an Electron-based malware sample named UtilifySetup.exe"; XLab: "UtilifySetup.exe is an installation file packaged with Inno Setup". <https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/>
   - Fix: Say the file name was removed because the store carries no file-name indicators.

4. **cves[CVE-2026-26980].cvss** (imprecision)
   - Claim: cvss: "9.4"
   - Defect: Correct per the vendor advisory (GitHub CNA, CVSS 3.1 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L); the scorer is not named and NVD's own score differs (7.5), which a machine consumer comparing against NVD will see.
   - Ground truth: Ghost advisory page: "Critical 9.4 CVSS overall score"; NVD API: security-advisories@github.com 9.4 (C:H/I:H/A:L), nvd@nist.gov 7.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N). <https://github.com/TryGhost/Ghost/security/advisories/GHSA-w52v-v783-gw97>
   - Fix: Note the scorer ("9.4 per the vendor/GitHub CNA; NVD 7.5").

### 2026-05-25/large-scale-clickfix-campaign-mass-compromises-self-hosted-g — factual-error

1. **body, "Why it matters to us"** (factual-error)
   - Claim: self-hosted Ghost is used across EU/CH universities, NGOs and independent media — exactly the named victim profile
   - Defect: No cited source says Ghost is used across EU or Swiss institutions, and the "named victim profile" (Harvard, Oxford, Auburn, DuckDuckGo) is not EU/CH; XLab's victim table is 48.1% personal blogs, 14.8% software/SaaS blogs, 2.7% education, 2.1% nonprofit.
   - Ground truth: XLab victim table rows: Personal Blog / Independent Site 368 (48.1%); Education / Academia 21 (2.7%); Nonprofit / Religion / Community 16 (2.1%); no country or region analysis in XLab or BleepingComputer. <https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/>
   - Fix: Delete the EU/CH usage claim; if a nexus is wanted, say the victim mix is mostly personal and software blogs and cite the table.

2. **body, "Why it matters to us"** (factual-error)
   - Claim: while *every visitor* to a compromised site is a ClickFix target
   - Defect: Contradicted by the cloaking mechanism: only visitors who pass the fingerprinting see the lure; researchers and crawlers see a harmless page.
   - Ground truth: XLab: "real victims will receive the malicious payload, while security researchers or crawlers will only see a harmless "safe page""; BleepingComputer: "Visitors passing the verification are served a fake Cloudflare prompt". <https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/>
   - Fix: Say "visitors who pass the cloaking script's fingerprinting".

3. **body, "Why it matters to us"** (imprecision)
   - Claim: `cmd.exe` / `powershell.exe` spawned from a browser process tree following a Run-dialog paste
   - Defect: No source gives the process lineage. XLab's chain is a WIN+R paste of `cmd /c move ... && tar -xf ... && start /min update.bat`; a Run-dialog launch is parented by the shell, not the browser, so a hunt keyed to a browser process tree would miss it (low confidence: reasoning from how the Run dialog launches, not from a cited page).
   - Ground truth: XLab: "1. Use the WIN+R shortcut to open the command window 2. Use Ctrl+V to paste the command 3. Press Enter to execute the command." <https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/>
   - Fix: Describe the sourced chain (Run-dialog command extracting an archive and starting a batch file, then hidden PowerShell and rundll32) without asserting a browser parent.

4. **body paragraph 1 (citation adjacency)** (imprecision)
   - Claim: instructing them to paste a supplied command into the Windows Run dialog, which drops DLL loaders, JavaScript droppers, or an Electron-based sample (`UtilifySetup.exe`) ; ... plus DuckDuckGo
   - Defect: The Run-dialog detail belongs to XLab; BleepingComputer, the page cited, says "on their Windows command prompt". DuckDuckGo is named by BleepingComputer only: the XLab report (fetched in full) does not mention it. The payload file name is a file-name indicator the store excludes.
   - Ground truth: BleepingComputer: "The page instructs victims to verify that they are human by pasting a provided command on their Windows command prompt"; "threat actors planted malicious code on the websites of Harvard University, Oxford University, Auburn University, and DuckDuckGo." XLab names "Harvard University, Oxford University, Auburn University, etc." and no DuckDuckGo. <https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/>
   - Fix: Cite XLab for the Run-dialog step, attribute DuckDuckGo to BleepingComputer, and drop the file name.

5. **frontmatter** (imprecision)
   - Claim: cves: [] ; regions: [global, europe] ; sectors: [education, media, technology, public-sector] ; classification and techniques absent
   - Defect: CVE-2026-26980 is named in the title, summary and body but cves[] is empty; "europe" and "public-sector" appear in no cited source (education, media and technology do match XLab's victim table); no Admiralty rating and no ATT&CK mapping.
   - Ground truth: XLab victim table has no public-sector category and no regional breakdown; Ghost advisory: CVE-2026-26980, fixed 6.19.1. <https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/>
   - Fix: Fold into the rewritten entry (the survivor); only verified facts move.

6. **body (editing artefacts)** (imprecision)
   - Claim: per § 2 and § 5 ; whether you run Ghost (. ; summary ends "AI/SaaS companies …"
   - Defect: Dangling references to brief sections that do not exist, a truncated closing parenthesis, and a summary cut off mid-list.
   - Ground truth: n/a (entry text) <https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/>
   - Fix: Remove on fold.

### 2026-05-17/pwn2own-berlin-2026-master-of-pwn-outcomes-the-new-ai-agents — factual-error

1. **summary / Exchange paragraph / Operational implication** (factual-error)
   - Claim: chained three undisclosed Exchange bugs to SYSTEM-level unauthenticated RCE ; the DEVCORE chain achieves SYSTEM-level direct RCE without authentication ; an unpatched unauthenticated SYSTEM RCE class
   - Defect: "Unauthenticated" is in neither ZDI nor BleepingComputer. The one chain bug later identified, CVE-2026-62911, is scored by Microsoft as requiring low privileges ("authorized attacker", PR:L), and a public analysis of the demo describes a low-privileged domain-joined attacker.
   - Ground truth: ZDI Day 2: "Orange Tsai (@orange_8361) of DEVCORE Research Team chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points." MSRC CVE-2026-62911: "allows an authorized attacker to elevate privileges over a network", CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H. <https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results>
   - Fix: Delete "unauthenticated" and "without authentication" everywhere; say ZDI and BleepingComputer do not state the authentication level.

2. **summary / AI Agents paragraph** (factual-error)
   - Claim: the new AI Agents category produced exploits or collisions across all entered targets — ... with Claude Code, Chroma, Megatron Bridge and Ollama producing collisions ; the entries either landed exploits or collided with bugs ZDI already had on file
   - Defect: Contradicted by the ZDI pages: Oracle Autonomous AI Database (AI Database category) was entered and failed; a Codex attempt failed; Chroma was a full SUCCESS (two bugs, $20,000), not a collision; Megatron Bridge had three successes besides one collision. Collisions are described as "previously known to the vendor" or "with a previous attempt", not as bugs ZDI had on file.
   - Ground truth: ZDI Day 1: "FAILURE - Unfortunately, Park Jae Min could not get their exploit of Oracle Autonomous AI Database working within the time allotted."; "SUCCESS - haehae (@haehaeYang) of Out Of Bounds chained 2 bugs (CWE-190, CWE-362) to exploit Chroma, earning $20,000 and 2 Master of Pwn points."; "Satoki Tsuji ... NVIDIA Megatron Bridge ... $20,000". <https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results>
   - Fix: Say which targets produced exploits, which collisions and which failures; drop "all entered targets".

3. **headline / summary / AI Agents paragraph** (imprecision)
   - Claim: the new AI Agents category ; Pwn2Own Berlin 2026 was the first year ZDI ran an AI Agents track
   - Defect: ZDI has no "AI Agents" category. An AI category already existed in 2025; for 2026 it was split into AI Databases, Coding Agents, Local Inferences and NVIDIA, and only the Coding Agent category is called new. LM Studio, LiteLLM and Ollama are Local Inference targets, Chroma is AI Database, Megatron Bridge and NV Container Toolkit are NVIDIA.
   - Ground truth: ZDI announcement 2026-03-11: "Last year, we added Artificial Intelligence as a category ... This year, we're expanding this and splitting it into multiple different categories: AI Databases, Coding Agents, Local Inferences, and a separate category for NVIDIA products."; "As this is a new category" (Coding Agent). <https://www.thezdi.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026>
   - Fix: Name the real categories and say Coding Agents is the new one.

4. **Day 1 paragraph and AI Agents paragraph** (factual-error)
   - Claim: Compass Security exploited OpenAI Codex through a CWE-150 "improper neutralization of special elements" bug for $40,000 — the first publicly-known weaponised exploit of OpenAI's coding agent ; centres on improper neutralisation of special characters in tool-invocation arguments
   - Defect: "First publicly-known weaponised exploit" has no source and is contradicted by the same page, which lists a Codex collision with a bug "previously known to the vendor"; the quoted label is not ZDI's text and is not CWE-150's name; "tool-invocation arguments" is invented detail.
   - Ground truth: ZDI Day 1: "used a single CWE-150 bug to exploit OpenAI Codex, earning $40,000 and 4 Master of Pwn points"; "maitai (@MaitaiThe) of Doyensec ... targeting OpenAI Codex ... used a bug that was previously known to the vendor". MITRE: "CWE-150: Improper Neutralization of Escape, Meta, or Control Sequences". <https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results>
   - Fix: Say ZDI reported a CWE-150 bug in Codex, $40,000; drop "first", the quoted label and the tool-invocation detail.

5. **AI Agents paragraph and actions[0]** (factual-error)
   - Claim: The recurring pattern across LiteLLM, LM Studio, Cursor and the OpenAI Codex attempts is **agent-instruction-injection → server-side request forgery → arbitrary code execution**, mapped to `T1059.007` and `T1090` ; Pwn2Own Berlin 2026 demonstrated `T1190 → T1090 → T1059` chains on every AI Agents target; SSRF-pivot to internal endpoints is the load-bearing technique
   - Defect: ZDI names SSRF and code injection only for the LiteLLM chain (3 bugs) and the STARLabs LM Studio chain (5 bugs, "incl."), a code-injection bug for OtterSec on LM Studio, a CWE-150 bug for Codex and no bug class for Cursor; no page mentions agent-instruction injection, an SSRF-then-code-execution ordering, or any ATT&CK id. T1090 (Proxy) is command-and-control proxying, not an SSRF pivot. "Every AI Agents target" is false (failures and collisions only on some).
   - Ground truth: ZDI Day 1: "k3vg3n chained 3 bugs including SSRF and Code Injection to take down LiteLLM"; "chained 5 bugs (incl. SSRF and Code Injection) to exploit LM Studio". ZDI Day 2: "OtterSec used a Code Injection bug to exploit LM Studio"; Cursor entries give no bug class. <https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results>
   - Fix: Replace with what ZDI states per target; delete the pattern claim, the ids and "every AI Agents target" (and the actions[0] sentence built on them).

6. **Background** (factual-error)
   - Claim: with vendor-disclosure happening within minutes of a successful pop and a 90-day Pwn2Own embargo before ZDI publishes technical detail
   - Defect: Neither the rules nor BleepingComputer give a "within minutes" timing, and neither says ZDI publishes technical detail after 90 days; BleepingComputer says vendors have 90 days to patch after the zero-days are disclosed at the contest.
   - Ground truth: BleepingComputer: "Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own." Rules: "Vulnerabilities and exploit techniques revealed by contest winners will be disclosed to the affected vendors and the exploits and whitepapers will become the property of the Sponsor". <https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/>
   - Fix: Say "vendors have 90 days to patch after disclosure at the contest" and drop the minutes and publication claims.

7. **Background** (imprecision)
   - Claim: is the second Berlin edition since Trend Micro / Zero Day Initiative moved the European event off the Vancouver-only schedule in 2025
   - Defect: "Second Berlin edition" is right (ZDI: "our second competition in Berlin", "inaugural competition last year"), but no source says ZDI "moved the European event off the Vancouver-only schedule"; Berlin was a new contest in 2025.
   - Ground truth: ZDI announcement: "After our inaugural competition last year, Pwn2Own returns to Berlin and OffensiveCon." BleepingComputer: the contest runs "at the OffensiveCon conference from May 14 to May 16". <https://www.thezdi.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026>
   - Fix: Write "the second Berlin edition, after the inaugural 2025 contest".

8. **Background** (factual-error)
   - Claim: The Berlin contest historically draws a heavier European researcher field than Vancouver — relevant this year because Swiss firm Compass Security fielded a five-researcher team
   - Defect: "Historically ... heavier European field than Vancouver" has no source (Berlin has run twice); the ZDI pages list five Compass Security researchers but none says the firm is Swiss.
   - Ground truth: ZDI Day 1: "Emanuele Barbeno, Cyrill Bannwart, Yves Bieri, Lukasz D., Urs Mueller of Compass Security (@compasssecurity) used a single CWE-150 bug to exploit OpenAI Codex". <https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results>
   - Fix: Delete the comparison; keep "five Compass Security researchers" and cite a source before calling the firm Swiss.

9. **Background** (factual-error)
   - Claim: Prior Pwn2Own competitions established the cadence: bugs popped in May surface as advisory-tagged CVEs in vendor August or September advisories.
   - Defect: Uncited generalisation and forecast; no cited page states a patch cadence (for the Exchange chain, one bug was later fixed in the 2026-08-11 Exchange update, MSRC CVE-2026-62911, credited to Orange Tsai working with ZDI).
   - Ground truth: BleepingComputer: "Vendors have 90 days to patch". MSRC CVE-2026-62911 released 2026-08-11. <https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/>
   - Fix: Delete.

10. **Background / "Capacity-overflow rejected-researcher PoC wave" paragraph** (factual-error)
   - Claim: the contest's capacity overflow which produced an unprecedented wave of *rejected-researcher* public PoC releases ; ZDI's response — public disclosure of full PoC chains by researchers whose submissions were rejected for slot reasons — produced an unprecedented PoC release wave covering Firefox full-chain RCE, additional Ollama / LM Studio exploitation, NVIDIA driver chains, and at least one researcher's Claude Code exploitation attempt
   - Defect: Not ZDI's response: the only source (Hackread, published 2026-05-12, before the contest, and written as "reportedly") says rejected researchers themselves are releasing findings. It names xchglabs (86 vulnerabilities for NVIDIA, Docker, Linux KVM, PyTorch), ggwhyp (Firefox on Windows opening a calculator) and FuzzingLabs (Oracle Autonomous AI Database); nothing about "full PoC chains", Ollama, LM Studio, NVIDIA drivers or Claude Code, and nothing "unprecedented". Hackread's "close the event's registration early on 7 May" also sits against ZDI's March announcement that registration closed on May 7.
   - Ground truth: Hackread: "Because they were rejected, dozens of researchers are now releasing their secrets for free."; "has reportedly run out of space". ZDI announcement: "registration closes on May 7". <https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/>
   - Fix: Delete the paragraph, or reduce it to one attributed sentence ("Hackread reported ...") with the ZDI timing contradiction noted.

11. **"Capacity-overflow" paragraph** (factual-error)
   - Claim: Operationally, defenders cannot rely on the standard Pwn2Own embargo for any of these — the technical detail is in the wild now.
   - Defect: Unsupported: contest bugs stay under the vendor 90-day window; Hackread describes other researchers' unreleased findings and gives no evidence that contest or rejected-entry technical detail is public.
   - Ground truth: BleepingComputer: "Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own." <https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/>
   - Fix: Delete.

12. **Exchange paragraph / Hardening bullet** (factual-error)
   - Claim: Embargo window: ZDI rules require vendors to ship patches within 90 days; expect Microsoft advisories around 2026-08-14, possibly bundled into August Patch Tuesday. ; plan for an August Patch Tuesday emergency cycle when the DEVCORE embargo expires
   - Defect: Forecast with no source. BleepingComputer says vendors "have 90 days to patch"; ZDI Day 2 contains no embargo, August or emergency-cycle statement. (Outcome, for the record: Microsoft released the Exchange August 2026 update on 2026-08-11 and credited Orange Tsai working with ZDI on CVE-2026-62911.)
   - Ground truth: ZDI Day 2 carries only the result line; BleepingComputer: "Vendors have 90 days to patch". <https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results>
   - Fix: Delete the forecast.

13. **Exchange paragraph ("Operational implication for the next ~12 weeks")** (factual-error)
   - Claim: on-premises Exchange faces (a) the currently-exploited XSS without permanent patch, (b) an unpatched unauthenticated SYSTEM RCE class proven viable on hardened production builds, and (c) the residual ProxyShell/NotShell attack surface that the FamousSparrow Azerbaijani campaign covered in the 2026-05-14 deep dive showed is still being weaponised
   - Defect: (a) is superseded: Microsoft shipped the permanent CVE-2026-42897 fix in June 2026; (b) "unauthenticated" is unsupported (see above) and the contest targets were "fully patched" in "default configurations", not "hardened"; (c) is an uncited cross-reference to another entry.
   - Ground truth: MSRC CVE-2026-42897 revision 2 (2026-06-09): "Added links to June 2026 Exchange Server security updates." Rules: "All targets will be installed in their default configurations". <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42897>
   - Fix: Delete, or bring to the current state with a citation per clause.

14. **Exchange paragraph** (imprecision)
   - Claim: with the EWS / RPC / RemotePS attack surface as the most plausible target set given Orange Tsai's prior ProxyLogon / ProxyShell / ProxyNotShell work
   - Defect: Uncited speculation about the chain's surface. The one bug later identified, CVE-2026-62911, is an authentication-relay flaw in the MRSProxy mailbox-move endpoint, not a RemotePS or RPC surface.
   - Ground truth: MSRC CVE-2026-62911: "Authentication bypass by capture-replay in Microsoft Exchange Server allows an authorized attacker to elevate privileges over a network." <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62911>
   - Fix: Delete the speculation.

15. **Hardening / mitigation summary (all four bullets)** (factual-error)
   - Claim: **Hardening / mitigation summary** (citing the contest blogs for each piece): verify EEMS M2.1.x ... until Broadcom ships a patch; restrict ESXi management network reach ... require tool-plugin code signing ... nothing actionable until vendors ship advisories
   - Defect: The heading claims each piece is cited to a contest blog; none of the three ZDI pages contains EEMS, ESXi hardening, egress or code-signing advice, an August window, or any recommendation at all (they are results pages).
   - Ground truth: ZDI Day 2 / Day 3 / Day 1 pages list contest results, awards and Master of Pwn points only. <https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn>
   - Fix: Remove the "citing the contest blogs" framing and either delete the bullets or cite real guidance (MSRC/Exchange Team for Exchange).

16. **Day 3 paragraph citation / sources[] labels** (factual-error)
   - Claim: ([ZDI, 2026-05-16]; [Hackread, 2026-05-16]) ; Zero Day Initiative — Day 1, 2026-05-13 ; Hackread, 2026-05-16
   - Defect: Hackread was published 2026-05-12 (four days before the label) and is a pre-contest piece that carries no Day 3 result; the ZDI Day One page was published 2026-05-14 (the label uses the URL slug date).
   - Ground truth: Hackread article:published_time 2026-05-12T17:41:26+01:00; ZDI Day One datePublished 2026-05-14T03:27:32-0500. <https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/>
   - Fix: Re-date both citations and cite Hackread only for the capacity report.

17. **Day-by-day paragraph (three details)** (imprecision)
   - Claim: Orange Tsai (DEVCORE) opened the day with a four-bug Microsoft Edge sandbox escape ; 0xDACA / Noam Trobinski ; Compass Security attempted Claude Code but collided with a vulnerability ZDI already had on file
   - Defect: No source says Orange Tsai opened the day (the draw lists chompie first in the 10:30 slot and the results page lists a Viettel failure first); the researcher is "Noam Trobishi"; ZDI describes the Day 3 Compass collision as "a one-vulnerability collision with a previous attempt", not a bug ZDI had on file.
   - Ground truth: ZDI Day 2: "0xDACA (@0xDACA) & Noam Trobishi (@NTrobishi) used a use-after-free bug to exploit NV Container Toolkit". ZDI Day 3: "Compass Security targeted Anthropic Claude Code, hitting a one-vulnerability collision with a previous attempt and earning $20,000". <https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn>
   - Fix: Drop "opened the day", correct the name, and quote the collision wording.

18. **AI Agents paragraph, "Swiss/EU" sentence, headline, frontmatter** (factual-error)
   - Claim: For Swiss/EU public-sector environments specifically: agentic coding tools are entering federal and cantonal developer workflows ahead of any procurement-grade evaluation ; ... for European defenders ; regions: [europe, switzerland, global]; sectors: [public-sector, technology, finance, healthcare, defense]
   - Defect: No source says anything about Swiss, EU, federal or cantonal adoption of coding agents, and no sector other than technology vendors appears in the ZDI pages.
   - Ground truth: ZDI Day 1 / Day 2 / Day 3 and BleepingComputer Day 2 carry no regional or sector statement. <https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results>
   - Fix: Delete the sentence and the Swiss/European framing; set regions to global and sectors to technology.

19. **"Defender concepts" and Exchange follow-ups** (imprecision)
   - Claim: (1) ... even when bound to localhost — they are reachable from any browser tab the developer opens; (2) ... RFC-1918-range alerts from agent containers are a high-signal SSRF indicator ... these are not yet routinely covered by SOC tooling baselines ; The defender posture published with the 2026-05-16 deep dive (verify EEMS service ...)
   - Defect: Uncited assertions of fact and cross-references to other entries; none of the ZDI pages describes localhost reachability, SSRF telemetry or SOC baselines.
   - Ground truth: The three ZDI day pages list results only. <https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn>
   - Fix: Cite or delete.

20. **body, totals sentence** (imprecision)
   - Claim: Across three days: 47 unique zero-days, $1,298,250 paid out — ZDI's largest Berlin payout to date.
   - Defect: Both figures are correct, but "largest Berlin payout to date" is not stated on any cited page; it follows only from comparing with the 2025 figure, which ZDI's announcement and BleepingComputer Day 2 give.
   - Ground truth: ZDI Day 3: "bringing the final totals to $1,298,250 awarded for 47 unique 0-day vulnerabilities across three days". ZDI announcement: "Last year, we awarded $1,078,750 for 28 unique 0-days over the three-day event." <https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn>
   - Fix: Cite the 2025 figure or drop the superlative.

21. **priority / frontmatter** (imprecision)
   - Claim: priority: high ; classification absent ; techniques: [] ; tags: [supply-chain, cloud]
   - Defect: Context: a contest-results roundup with no in-the-wild use is research with no exploitation, a disqualifier for high. The body names ATT&CK ids (T1190, T1059.003, T1068, T1059.007, T1090; all active in v20) while techniques[] is empty; no Admiralty rating; supply-chain and cloud tags appear in no source.
   - Ground truth: n/a (frontmatter); ZDI pages report contest results only. <https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn>
   - Fix: Re-grade, add classification, and align techniques[] with source-supported behavior only.

### 2026-05-17/exchange-cve-2026-42897-pwn2own-devcore-three-bug-system-rce — imprecision

1. **title / summary / Defender takeaway / sources[]** (imprecision)
   - Claim: one later fixed as CVE-2026-62911 ; one of them, CVE-2026-62911, was fixed in the August 2026 Exchange update and has public exploit code
   - Defect: The link between CVE-2026-62911 and the Pwn2Own chain is stated flatly in the title and summary but rests on one blog (Franky's Web). MSRC's per-CVE record, which carries the fix table and the credit, is not cited for it; it credits "Orange Tsai (@orange_8361) of DEVCORE Research Team working with TrendAI Zero Day Initiative" but does not name Pwn2Own or the chain. Franky's Web also says the attacker "does not need valid credentials" while MSRC scores it PR:L ("authorized attacker"); the entry does not repeat that, but cites Franky's Web alone.
   - Ground truth: MSRC CVE-2026-62911 (released 2026-08-11): CVSS 8.0 CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H, "allows an authorized attacker to elevate privileges over a network"; fixed builds Exchange SE RTM 15.02.2562.046 (KB5121573), 2019 CU15 15.02.1748.049 (KB5121574), 2019 CU14 15.02.1544.044 (KB5121575), 2016 CU23 15.01.2507.072 (KB5121576). Franky's Web 2026-08-27: "He demonstrated the vulnerability at Pwn2Own Berlin 2026, where it was part of a chain of three vulnerabilities". <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62911>
   - Fix: Add the MSRC CVE-2026-62911 page as a source for the fix and credit, and word the chain link as reported (Franky's Web, and a public analysis of the demo) in the title and summary.

### Duplicate groups

**T1-ghost**: same finding: yes; survivor/link target: `2026-05-25/ghost-cms-cve-2026-26980-clickfix-the-cms-compromise-to-endp`.
- Note: Same finding: one campaign, one CVE (CVE-2026-26980), same two primaries (XLab, BleepingComputer). The legacy twin is a shorter threat-kind write-up of the 2026-05-25 brief item; the rewritten entry (2026-10-11) is the survivor and already carries the advisory facts, the WAF mitigation, the XLab timeline, detection and takeaway lines. Fold the twin in, moving only the verified facts below; do not move its file name, EU/CH usage claim, "every visitor", browser-process-tree hunt, Europe/public-sector metadata, "(Harvard, Oxford...)" without its XLab/BC attribution split, or its dangling section references.
- Current state: Ghost advisory GHSA-w52v-v783-gw97 (page date 2026-02-16; GitHub release v6.19.1 2026-02-16T16:54:09Z): unauthenticated SQL injection in the Content API, Ghost v3.24.0 to v6.19.0, fixed in 6.19.1, CVSS 9.4 (GitHub CNA; NVD 7.5), temporary WAF rule on slug:[ / slug%3A%5B, rotate keys and review staff users. Not in CISA KEV (catalogue 2026.10.20). XLab 2026-05-21 (published 2026-05-21T12:26Z): detected 2026-05-07, 156 domains by 2026-05-10, 700+ domains confirmed 2026-05-17, two actors; BleepingComputer 2026-05-24 relays it and adds DuckDuckGo to the named victims.
- Facts carried by one entry only: 13 listed (9 verified true, 4 verified false or unsupported); see the groups block of truth-T1.yaml.

**T1-nightmare-yellowkey**: same finding: no; survivor/link target: `2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days`.
- Note: Distinct findings. The 2026-05-15 entry is the technical disclosure of YellowKey and GreenPlasma (12-13 May); the 2026-05-30 entry is Microsoft's 27 May disclosure-dispute statement, the researcher's July threat and a roll-up of the six drops. They share the researcher entity and CVE-2026-45585, which the 2026-05-30 entry models wrongly (LPE, local, post-auth, cvss n/a, no-patch). Link them (references[] both ways); the 2026-05-30 entry should drop its cves[] record or correct it, and the 2026-05-15 entry is the survivor for the CVE thread and needs the 2026-06-09 patch state and GreenPlasma/MiniPlasma outcomes.
- Current state: YellowKey = CVE-2026-45585, MSRC "Windows BitLocker Security Feature Bypass Vulnerability", released 2026-05-19, CWE-77, CVSS 6.8 (CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H; temporal 6.3 with E:P/RL:W/RC:C), publiclyDisclosed Yes, exploited No, "Exploitation More Likely"; mitigation script added 2026-05-21 (revision 1.2, manual steps removed); revision 2 (2026-06-09) "Added links to June 2026 Windows security updates"; fixed builds KB5094125 (Windows Server 2025 10.0.26100.32995), KB5094126 (Windows 11 24H2 10.0.26100.8655, 25H2 10.0.26200.8655), KB5095051 (Windows 11 26H1 10.0.28000.2269); Windows Server 2022 is not in MSRC's product table; MSRC FAQ: "if you are using TPM+PIN the vulnerability is not exploitable". Not in CISA KEV (catalogue 2026.10.20). GreenPlasma = CVE-2026-45586, "Windows Collaborative Translation Framework (CTFMON) Elevation of Privilege Vulnerability", released 2026-06-09, CWE-59, CVSS 7.8 (AV:L/AC:L/PR:L, temporal 6.8, E:U), exploited No, publiclyDisclosed Yes, "Exploitation More Likely"; fixed builds include Windows Server 2019 10.0.17763.8880 (KB5094123), Server 2022 10.0.20348.5256 (KB5094128), Windows 10 21H2/22H2 10.0.19044.7417/10.0.19045.7417 (KB5094127), Windows 11 23H2 10.0.22631.7219 (KB5093998), 24H2 10.0.26100.8655 and 25H2 10.0.26200.8655 (KB5094126), Server 2025 10.0.26100.32995 (KB5094125); not in KEV. MiniPlasma (cldflt.sys, Cloud Files Mini Filter Driver) = addressed by the 2026-06-09 re-release of CVE-2020-17103 (MSRC revision 2: "This CVE has been re-released to comprehensively address the vulnerability identified by CVE-2020-17103"; CVSS 7.0 AV:L/AC:H; exploited No; MSRC gives no structured fixed-build table, only "installing the June 2026 updates"); not in KEV. The researcher's earlier drops are KEV-listed: BlueHammer CVE-2026-33825 (added 2026-04-22), UnDefend CVE-2026-45498 and RedSun CVE-2026-41091 (both 2026-05-20); MSRC marks the last two exploited Yes.
- Facts carried by one entry only: 14 listed (9 verified true, 5 verified false or unsupported); see the groups block of truth-T1.yaml.

**T1-pwn2own**: same finding: no; survivor/link target: `2026-05-17/exchange-cve-2026-42897-pwn2own-devcore-three-bug-system-rce`.
- Note: Distinct findings: the legacy entry is a three-day contest roundup (results, Master of Pwn, AI targets, defender advice); the DEVCORE entry is the single Exchange result and its later CVE. Both already agree on the Exchange facts; the DEVCORE entry links the roundup in references[], the roundup does not link back (add the reciprocal link). Verified claim by claim against the three ZDI day pages (and BleepingComputer Day 2, Hackread, ZDI announcement and rules): every result, researcher, target, bug class, award, point total, date and total in the roundup's day-by-day paragraph is correct except the details flagged false below; the roundup's forecasts, "unprecedented" claims, rejected-researcher wave, AI-pattern analysis, hardening bullets and Swiss/EU framing have no source and are factual errors (see the entry findings). Keep the roundup only if its unsupported analysis is stripped; the verified results table is the part worth keeping.
- Current state: Contest: Pwn2Own Berlin 2026 at OffensiveCon, 14-16 May 2026 (BleepingComputer Day 2; ZDI schedule "Thursday, May 14"); ZDI Day Three: "bringing the final totals to $1,298,250 awarded for 47 unique 0-day vulnerabilities", DEVCORE Master of Pwn "50.5 points and $505,000", STARLabs SG second "25 points and $242,500", Out Of Bounds third "12.75 points and $95,750"; 2025 Berlin total $1,078,750 for 28 unique 0-days (ZDI announcement). Categories: AI Databases, Coding Agents (new), Local Inferences, NVIDIA, plus the classic ones. Exchange chain: ZDI Day 2 "chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points"; neither ZDI nor BleepingComputer states authentication level or CVE. CVE-2026-42897 (separate): MSRC "Microsoft Exchange Server Spoofing Vulnerability" (CWE-79 XSS), released 2026-05-14, exploited Yes, CVSS 8.1, KEV added 2026-05-15, permanent fix in the June 2026 updates (revision 2, 2026-06-09). CVE-2026-62911 (credited to Orange Tsai working with ZDI): MSRC "Exchange Server Elevation of Privilege", released 2026-08-11, CWE-294, CVSS 8.0 (PR:L), exploited No, "Exploitation Less Likely", fixed builds Exchange SE RTM 15.02.2562.046, 2019 CU15 15.02.1748.049, CU14 15.02.1544.044, 2016 CU23 15.01.2507.072; public exploit code reported 2026-08-27 (Franky's Web); not in CISA KEV; its identification as one of the three contest bugs is by Franky's Web and a public analysis of the demo (MB VRED), not by ZDI or MSRC.
- Facts carried by one entry only: 31 listed (22 verified true, 9 verified false or unsupported); see the groups block of truth-T1.yaml.
