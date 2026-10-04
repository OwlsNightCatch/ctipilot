**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T11:45:13Z · ended_at=2026-09-30T12:19:13Z · duration_seconds=2040

## Verification report — 2026-09-30T0639Z-audit (iteration 2, slice s4 of 4, post-fix pass)

Scope: 16 existing entries of `scope.iter1.s4.txt` read whole, each with `git diff HEAD`; the run record; the audit report. Ledger `claims.iter2.s4.yaml`: all 354 claims have a verdict row in `verification.iter2.s4.claims.yaml` (336 ok, 9 F4, 5 F3, 2 F14, 1 F5, 1 unreadable: the BSI WID page for WID-SEC-2026-2027 is an Angular shell on every rung, as in iteration 1). Full pass, no sampling. Checks were run against the disk state at about 12:15Z; other slices were still remediating, so counts in the report and run record should be recomputed once they finish.

### Citation does not support the claim

**#1 F3, 2026-05-08/pro-russian-hacktivists-modify-ot-pump-settings-at-five-poli**: body, APT sentence (low confidence). Quote: "The state-sponsored actors it lists, APT28, APT29 and UNC1151, are described as espionage and influence operators"  
Evidence and fix: ABW p.36 describes them as APT groups carrying out "sophisticated, long-term espionage and sabotage operations" with the objective of "strategic intelligence, cyber espionage, the conduct of influence operations, and ... disinformation". The entry drops "sabotage", the one word that matters to a water-sector reader deciding whether these actors are relevant to the plant breaches.

**#2 F3, 2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti**: body para 1, ACP sentence (written this run). Quote: "A known username is enough, and a default board's public member list supplies it, but the Administration Control Panel still asks for the account password" ([Pentest-Tools.com, 2026-06-08])  
Evidence and fix: The cited Pentest-Tools page (fetched) still prints the old ACP sentence but adds "[Later edit: Jun 15, 2026] Thank you to the anonymous reader who pointed out an attacker can, in fact, directly access the ACP panel after impersonating an admin user. We've updated the vulnerability description to reflect that." So the source retracted the very claim the entry now asserts, and Aikido (2026-06-10) says the opposite ("there is another password check in front of the Admin Control Panel (ACP) that cannot be bypassed"). For a defender this decides whether an admin-session bypass reaches extension install/RCE. State that the discoverer later corrected itself and ACP access after admin impersonation is possible, surface the Aikido disagreement (F9) and revisit the impact wording; drop the "still asks for the account password" clause.

**#3 F3, 2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default**: body para 1, "removes the wildcard" (low confidence). Quote: "Version 1.26.3 removes the wildcard and makes reverse-proxy authentication opt-in and admin-configured" ([Gitea, 2026-06-21])  
Evidence and fix: The Gitea release post says only "The Docker images shipped a REVERSE_PROXY_TRUSTED_PROXIES = * default ... Reverse-proxy authentication is now opt-in and admin-configured". Wildcard removal is stated by The Hacker News ("with the '*' wildcard now removed and reverse-proxy authentication made opt-in"), which is not cited on this clause. Cite THN too or drop "removes the wildcard".

**#4 F3, 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass**: body para 2, Huntress code-execution sentence (low confidence). Quote: "Huntress turned the resulting root file read and write into code execution by creating a launch daemon that runs a reverse shell at reboot or by modifying a shell startup file"  
Evidence and fix: The Huntress post says only "Remote code execution is achieved through a number of mechanisms, introducing varied opportunities for success: Creation of a LaunchDaemon ... Modification of persistence within a shell startup file"; it does not say Huntress performed them, and it ties them to the frame-length PoC path (see F9). Attribute the mechanisms to Huntress's description, not to Huntress having done it.

**#5 F3, 2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev**: body sentence 1, CVSS 7.8 cited to Help Net Security (low confidence). Quote: "CVE-2026-87886 (CVSS 7.8) is a local privilege-escalation flaw from insecure file permissions ... both on Linux" ([Help Net Security, 2026-09-16])  
Evidence and fix: The fetched Help Net Security page carries no CVSS number (it says only that the CVSS string indicates low complexity). The 7.8 score is on BleepingComputer ("assigning it a severity score of 7.8"), which is not cited on this clause. Cite BleepingComputer for the score.

### Unsupported / hallucinated facts

**#6 F4, 2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after**: Correction section and record summary describe fixes to statements HEAD never made. Quote: record: "An unsupported claim about Swiss applicants and a mention of exposed booking details are removed"; section: "The warning that the attackers had published a data sample on Telegram ... came from Eurail in February ..., not from the Commission"; "No source lists booking details among the exposed data."  
Evidence and fix: git show HEAD for this entry contains no "booking", "Telegram", "sample", "dark web" or Commission-attribution text (grep empty); they appear to come from the run's own earlier working copy (iteration 1 found them there). The published entry never said them, so the record and the Correction section tell readers of a change that did not happen and imply the earlier published text mis-attributed the sample claim to the Commission. Keep only the real changes (late-April date, Dutch DPA/EDPS reviews, Swiss-applicants sentence, priority) and state the Telegram/Eurail attribution as a plain fact in the body Contradiction line, not as a correction.

**#7 F4, 2026-05-08/pro-russian-hacktivists-modify-ot-pump-settings-at-five-poli**: Correction section and record summary misdescribe the earlier published text. Quote: section: "presented the five plant breaches as hacktivist intrusions through weak passwords"; record: "a link between the five plant breaches and hacktivists using weak passwords"  
Evidence and fix: git show HEAD for this entry has no "password" anywhere; HEAD tied the breaches to pro-Russian hacktivists via "IT/OT flat network exploitation leading to HMI manipulation". The weak-password link was only in the run's earlier working copy (iteration 1 finding F13). State the real prior claim (hacktivist attribution via flat-network exploitation) or drop the weak-password clause.

**#8 F4, 2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv**: title/headline not reconciled with the Correction (low confidence). Quote: title/headline: "malware-signing-as-a-service feeding Rhysida, INC, Qilin and Akira ransomware operations"; Correction: "INC, Qilin and Akira are tied to Fox Tempest through cryptocurrency links to affiliates ..., not named as confirmed customers"  
Evidence and fix: Microsoft (exposing-fox-tempest post) confirms only Vanilla Tempest as a customer deploying Rhysida; INC/Qilin/Akira rest on "Cryptocurrency analysis ... clear links tying the actor to ransomware affiliates". "Feeding ... operations" still asserts a supply relationship the entry's own newest section says is not established. Soften title/headline (e.g. "linked to") in the next changelog record.

**#9 F4, 2026-06-12/cve-2026-25089-fortinet-fortisandbox-unauthenticated-os-comm**: cves[CVE-2026-39813].cvss 9.1 vs 9.8 for the other two (low confidence). Quote: cves: CVE-2026-25089 cvss "9.8", CVE-2026-39808 cvss "9.8", CVE-2026-39813 cvss "9.1"; summary: "CVE-2026-39813 (JRPC path traversal authentication bypass, CVSS 9.1)"  
Evidence and fix: Fortinet PSIRT raw HTML (fetched: FG-IR-26-112, -100, -141) shows the same calculator vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:F/RL:O/RC:C and "CVSSv3 Score 9.1" on all three; 9.1 is the temporal score of a 9.8 base vector (9.8 x 0.97 x 0.95). The entry uses base 9.8 for two CVEs and the temporal 9.1 for CVE-2026-39813 (taken from Security Affairs/Help Net Security), so the third looks less severe than Fortinet's own vector says. Use one scoring basis for all three (base 9.8 each per the Fortinet vector, CCB gives 9.8 for CVE-2026-25089) or state the basis.

**#10 F4, 2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default**: Correction section and record summary say the summary also claimed no exploitation (low confidence). Quote: section: "The summary and main text above said no exploitation was reported."; record: "The summary and main text still said no in-the-wild exploitation was reported after the 2026-07-10 update ..."  
Evidence and fix: git show HEAD: only the main text said "No in-the-wild exploitation reported yet"; the HEAD summary/headline contain no exploitation statement (they claimed BSI "hoch", Gitea "of choice for DACH/EU", patched in 1.26.3/1.26.4). Say "the main text" only.

**#11 F4, 2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin**: Correction section and record summary say the headline also claimed no exploitation (low confidence). Quote: section: "The headline and summary above said no exploitation was known."; record: "The headline and summary still said Progress reported no known exploitation"  
Evidence and fix: git show HEAD: the headline was "CVE-2026-8037 — Progress Kemp LoadMaster: pre-auth RCE via uninitialized heap in the /accessv2 API" (no exploitation statement); only the summary said "Progress reports no known exploitation". Say "the summary".

**#12 F4, runs/2026-09-30/2026-09-30T0639Z-audit.md**: frontmatter entities_added. Quote: entities_added: []  
Evidence and fix: git diff HEAD -- entities/registry.yaml adds three registry keys this run: product:fortinet-fortisandbox, product:fortinet-fortisandbox-cloud, product:fortinet-fortisandbox-paas (first_seen 2026-06-12), linked from the FortiSandbox entry. docs/pipeline.md defines entities_added as "registry keys added this run", and the 2026-09-29T2134Z audit record lists its four product keys the same way. List the three keys.

**#13 F4, runs/2026-09-30/2026-09-30T0639Z-audit.md**: Scope paragraph: priority count. Quote: "30 priorities recalibrated against the 4.17 `high` bar"  
Evidence and fix: On disk (git diff HEAD, priority line of each changed entry, checked 12:15Z) 36 entries changed priority: 23 high to notable, 2 high to routine, 11 notable to routine. The run record says 30 and the audit report says 35 (22/2/11), so the two documents disagree with each other and with disk. Recompute after the last remediation and use one figure.

**#14 F4, docs/audits/2026-09-30-quality-audit.md**: paragraph after the findings table: priority and record-type counts. Quote: "Thirty-five entries had their priority recalibrated ...: 22 from high to notable, 2 from high to routine and 11 from notable to routine ... The run's 75 records are 70 corrections (8 of them internal), 3 improvements (1 internal) and 2 updates (TeamCity and Bitget)."  
Evidence and fix: Disk at 12:15Z: 36 priority moves (23 high to notable, 2 high to routine, 11 notable to routine); the 75 records are 71 corrections (63 public, 8 internal), 2 improvements (Unbound public, Kaspersky internal) and 2 updates (TeamCity, Bitget). The Cisco ISE record is now a correction (iteration-1 remediation changed it from improvement). Update to 36 (23/2/11) and 71/2/2.

**#15 F4, docs/audits/2026-09-30-quality-audit.md**: Findings: missing coverage, KEV ransomware flips bullet. Quote: "Cisco Secure FMC and the Nx/TanStack entry (fixed with improvement records)"  
Evidence and fix: Both records are type correction on disk (entries/2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited.md and entries/2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands.md; the only improvement records are Unbound and Kaspersky). Only TeamCity (and Bitget) carry type update. prompts/CHANGELOG.md 4.18 says the three were "updated"; say corrections.

**#16 F4, docs/audits/2026-09-30-quality-audit.md**: findings table, Bitget row. Quote: "2026-09-29 Bitget | Downgraded to routine as a theft through an unnamed product with nothing to act on"  
Evidence and fix: git show HEAD:entries/2026-09-29/bitget-hot-wallet-theft-north-korea-nexus.md has priority: high and updates: [] (the only commit touching it is cf1756d1, 2026-09-29T0405Z-intel). The entry was never routine; this run moves it from high to notable through an update record. Rewrite the Defect cell (e.g. "Body named an unnamed third-party product; Mandiant and SlowMist reports published 2026-09-30 name the appliance path") and drop "Downgraded to routine".

**#17 F4, docs/audits/2026-09-30-quality-audit.md**: Systemic finding 5, finding count. Quote: "raised 150 truth findings (F3, F4, F5, F13, F14)"  
Evidence and fix: Summing work/2026-09-30T0639Z-audit/verification.iter1.s1-s4.findings.yaml gives 237 findings: truth (F1-F4, F13-F15) = 150 (F1 1, F3 58, F4 76, F13 9, F14 6). F5 is an editorial code (14 findings) and is not in the 150; the list also omits F1. Say "(F1, F3, F4, F13, F14)" or "150 truth findings and 87 editorial or advisory".

**#18 F4, docs/audits/2026-09-30-quality-audit.md**: Systemic finding 1 and Verdict: entry totals (low confidence). Quote: "478 of 962 entries came from the v2 daily briefs" (also prompts/CHANGELOG.md 4.18, prompts/quality-audit.md 6b, .claude/memory/legacy-corpus.md)  
Evidence and fix: At HEAD the store holds 966 entries, 478 with migrated_from; after this run's three folds it holds 963, 475 with migrated_from (475 = 468 pending + 7 reviewed in state/legacy_review.json). 962 is the count before the 0404Z fire merged. The 478 is right for the pre-fold store; the denominator is not. Use 478 of 966, or 475 of 963 after the folds.

**#19 F4, docs/audits/2026-09-30-quality-audit.md**: Fixes shipped, site bullet (low confidence). Quote: "a full build of 46 s measured on 2026-09-30"  
Evidence and fix: The build logs the run kept (scratchpad build-11.log 0m42.9s, build-final2.log 0m43.8s, build-final4.log 0m43.3s) and the site progress log ("full build 1m50s -> 43s") show 43 s; the last build log (build-final.log, 07:35) records no time. prompts/CHANGELOG.md says "about 45s". No 46 s measurement was found. Cite the measured figure or re-measure and keep the log.

### Claims missing inline citation

**#20 F5, 2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev**: body, "Fixed builds" sentence (low confidence). Quote: "Fixed builds: cPanel & WHM plugin 1.9.3 HF3 (build 1.9.3.1021), Plesk extension build 1.8.11.638."  
Evidence and fix: No inline citation, and the immediately preceding citation is the KEV feed, which carries no build numbers. The values are on BleepingComputer (builds earlier than 1.9.3.1021 fixed in 1.9.3 HF3; earlier than 1.8.11.638 fixed in 1.8.11); note Help Net Security names only 1.9.3 HF3 and 1.8.11.

### Drop (low relevance / off-audience / duplicate)

**#21 F7, 2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after**: relevance ground (low confidence). Quote: "The breach is relevant as a European transport supplier to an EU programme whose participants include young Europeans."  
Evidence and fix: Out-of-nexus breach (no Swiss link, no vector, no actor, no TTP). The stated ground matches none of the four grounds the stricter breach bar names (global significance, transferable TTP, actor plausibly targeting the constituency, imminent shared threat). It is a routine, two-sentence entry as required, so the defect is only the thin ground; acceptable to leave as-is if the operator accepts it (published entries cannot be removed).

### Needs more research

**#22 F8, 2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p**: headline/takeaway/cves[].fixed stale: fix pack 9.0.5.29 has shipped. Quote: headline: "has only an interim fix until fix packs arrive, targeted for 3Q2026"; takeaway: "rather than waiting for Fix Packs 9.0.5.29 and 8.5.5.30, which IBM's bulletin targets for 3Q2026"  
Evidence and fix: IBM fix page https://www.ibm.com/support/pages/90529-websphere-application-server-traditional-version-90529 (fetched): "Fix release date: 08 September 2026 ... Status: Recommended" for Fix Pack 9.0.5.29, which the bulletin names as the fix ("Apply Fix Pack 9.0.5.29 or later"). The run refreshed the KEV status "as of 2026-09-29" but left the fix state as future tense, so on 2026-09-30 the headline and takeaway tell readers to run an interim fix instead of waiting for a fix pack that is already out. Add the released fix pack to cves[].fixed, headline and takeaway (the 8.5.5.30 state was not established).

**#23 F8, 2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default**: Exposure omits the trusted-proxies discriminator (low confidence). Quote: **Exposure:** instances running the official Gitea Docker image 1.26.2 or earlier with ENABLE_REVERSE_PROXY_AUTHENTICATION = true whose HTTP port is reachable other than through the authenticating proxy  
Evidence and fix: GHSA and The Hacker News both condition the flaw on the admin having left REVERSE_PROXY_TRUSTED_PROXIES at the image default ("leaves the trusted-proxies setting at 'the default'"). An instance whose admin set the trusted proxy explicitly is not exposed, and that is the fastest triage question for a defender; it is only implied in the action text.

### Surface contradiction

**#24 F9, 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass**: main analysis para 2 and Triage line rest on the side of a source disagreement the main analysis does not surface. Quote: body: "fG! described a separate pre-authentication defect in the same daemon"; Triage: "an attach with the SRP type or with a root or null user has no benign explanation on a managed Mac"  
Evidence and fix: Huntress (cited, fetched) says fG!'s PoC is "tracked as CVE-2026-65400" and that the frame-length stale-return is the CVE-2026-65400 mechanism; Calif (cited) says that stale return is fG!'s separate first bug (fixed in 26.6, no CVE) and CVE-2026-65400 is a different state-machine desync. The disagreement is set out only in the 2026-08-11 section. The main analysis adopts Calif's "separate" reading in para 2 and then gives Huntress's SRP/root/null indicator, derived from the frame-length PoC, as an unqualified Triage discriminator for CVE-2026-65400. Add a Contradiction line to the main analysis and hedge the Triage line ("in the bypass Huntress analysed").

### Missed angles

**#25 F10, 2026-05-08/cve-2026-5787-cve-2026-6973-ivanti-epmm-pre-auth-certificate**: June 2026 Ivanti EPMM critical update not in the store; the entry's "fixed" builds are inside its affected range (low confidence on CVE ids). Quote: entry: "Fixed in 12.6.1.1, 12.7.0.1 and 12.8.0.1"; cves[].fixed "12.6.1.1 / 12.7.0.1 / 12.8.0.1"  
Evidence and fix: CCCS AV26-567 (fetched, https://www.cyber.gc.ca/en/alerts-advisories/ivanti-security-advisory-av26-567, 2026-06-09, updated 06-11): "Ivanti published security advisories ... critical updates for ... Ivanti Endpoint Manager Mobile - versions 12.9.0, 12.8.0.2, 12.7.0.1 and prior". So the builds this entry names as the fix are affected by a later critical EPMM update. The store has the Sentry pair from that day and the September update, but nothing on the June EPMM advisory (no entry or state/cves_seen.json row names its CVE). Suggested search: "Ivanti EPMM June 2026 security advisory 12.9.0.1 12.8.0.3 12.7.0.2 CVE-2026-10727". Below a new entry's bar; an update record on this entry (patch path now later builds) would do.

### Editorial / less-is-more flags (advisory)

**#26 F11, 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass**: em dashes in text this run wrote/re-emitted. Quote: body lines: "Detection: neither source ..." (— Huntress described —), "**Detection.** ..." and "**Exposure.**" section paragraphs; also Langflow "**Detection:**" line and "Two facts ..." paragraph; Cisco ISE "**Defender takeaway:** patch every ISE/ISE-PIC node and restrict management-plane reachability via ACLs immediately — there is no other mitigation"  
Evidence and fix: git diff HEAD shows these lines among the added lines and each contains an em dash (the Cisco ISE takeaway is new text written this run; the macOS and Langflow lines are re-emitted prior text with edits). The style rule is no em dash in reader-facing text this run wrote; replace with commas or full stops when next touched.

**#27 F11, 2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal**: record summary narrates an unchanged field. Quote: "The ATT&CK mapping, including Exploit Public-Facing Application for the probing of App Service applications, stays as Microsoft lists it."  
Evidence and fix: The record's fields are [title, summary, body]; the sentence describes a field that did not change (and a change that was made and reverted during the run). It is rendered to readers on /changes/ and the entry page and mentions frontmatter/ATT&CK mapping mechanics. Drop it.

**#28 F11, runs/2026-09-30/2026-09-30T0639Z-audit.md**: run record timing (low confidence). Quote: completed: "2026-09-30T07:34:51Z"; duration_seconds: 3308; sub_agents.SITE.started_at: "2026-09-30T06:37:31Z" vs started: "2026-09-30T06:39:43Z"  
Evidence and fix: The record was written before the verification loop: iteration 1 started 07:36:23Z, iteration 2 started 11:45Z, and entry remediation continued past 12:00Z, so completed/duration_seconds understate the run unless finalised after the loop (the runaway watchdog reads duration_seconds). SITE started two minutes before the run itself; if it is a resumed worker, say so in scope. gap_hours 9.09 (from 2026-09-29T2134Z), the SITE sub-agent entry and the die-linke fetch_failures entry from iteration 1 are now correct.

### Single-source items missing [SINGLE-SOURCE] flag

**#29 F12, 2026-05-08/pro-russian-hacktivists-modify-ot-pump-settings-at-five-poli**: verification single-source with sourcing_note null (low). Quote: verification: single-source; sourcing_note: null; sources: only the ABW PDF  
Evidence and fix: Single source is the authority itself (government authority reporting on its own jurisdiction), which the carve-out covers, but the entry neither uses single-source-national-cert nor carries a sourcing_note naming the situation. Separately (low confidence, F8): ABW's press office told CyberDefence24 (https://cyberdefence24.pl/cyberbezpieczenstwo/ataki-na-wodociagi-abw-o-widocznosci-obiektow-z-internetu, 2025-10-08, fetched) that 'potentially compromised entities had IT resources accessible from the public Internet, including HMI panels'; that ABW statement on the access vector of the compromised water plants is not in the entry, which says the plants have no stated access route.

**#30 F12, 2026-09-04/cve-2026-85046-chrome-v8-type-confusion-exploited**: verification: single-source no longer matches sources[] (low confidence). Quote: verification: single-source; sources: Google Chrome Releases (primary), CISA KEV catalog, Proofpoint  
Evidence and fix: The run added the KEV catalog and Proofpoint as sources. CISA lists the flaw "based on evidence of active exploitation" and Proofpoint (fetched, 2026-09-08) documents the BlueMoon kit using CVE-2026-85046 in campaigns from 2026-08-28, so exploitation is independently assessed and observed. The entry still says single-source and its sourcing_note frames Google as sole basis; set verification to multi-source (or state why the corroboration does not count).

### Analytical-link-as-fact

**#31 F13, 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass**: Update 2026-08-16 Detection paragraph (legacy text re-emitted by this run). Quote: "the telemetry discriminator Huntress described ... which was a concern about a proof-of-concept when it was written and is now a description of activity someone has actually performed"; "a Mac sustaining high processor load from a process with no corresponding user session ... is the shape the confirmed cases took"  
Evidence and fix: NCSC-NL and BleepingComputer report only abuse on hosts with port 5900 exposed, root obtained and a Monero miner placed; BC says NCSC "has not shared any details about the reported attacks". No source says the confirmed cases showed the SRP authentication type or a root/null session user, or a "process with no corresponding user session". Huntress derived its discriminator from a PoC of the frame-length bug, which Calif says is the other, pre-26.6 flaw. The section keeps an unsupported link between the confirmed exploitation and Huntress's indicator.

**#32 F13, docs/audits/2026-09-30-quality-audit.md**: findings table, ABW row, Ground truth column. Quote: "ABW names no state actor for the water intrusions and describes altered equipment parameters through weak passwords and internet-exposed panels"  
Evidence and fix: The ABW report (English PDF, pp. 36-37) makes two separate statements: hacktivists exploited poor password policies and unsecured management panels against municipal infrastructure generally (p.36), and breaches at five named water plants let attackers alter equipment parameters (p.37) with no actor or vector named. The published entry now keeps them apart and its Correction says the report "does not tie it to the five plants". The report row re-asserts the tie the entry removed. Write: "ABW names no actor or access vector for the water-plant breaches; its statement on weak passwords and exposed panels concerns municipal infrastructure in general".

### Quantifier without source

**#33 F14, 2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce**: record summary "will never receive a fix"; Update 2026-09-18 "will not receive a fix at all" (low confidence). Quote: record: "the eight CVEs that CERT-FR says ISE 3.1 and 3.2 will never receive a fix for"; section: "The eight CVEs for which Cisco ships no fix on ISE 3.1 and 3.2 are ..."  
Evidence and fix: CERT-FR AVI-1197 (fetched): Cisco says 3.2 and 3.1 "ne seront plus supportées à partir du 30 novembre 2027 et n'ont pas reçu de correctif pour les vulnérabilités CVE-2026-20247, ..." (have not received a fix). Cisco's hardening advisory only says 3.1/3.2 are in the Software Maintenance phase where "only Critical SIR vulnerability fixes are included". Neither source says "never"; say "have no fix on 3.1 and 3.2 as of the advisory".

### Classification missing / inconsistent

**#34 F17, 2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv**: reliability A (low confidence). Quote: classification: {reliability: A, credibility: 2}; primary source Microsoft Threat Intelligence blog  
Evidence and fix: sources/sources.json rates the Microsoft Threat Intelligence blog B (msrc.microsoft.com is A). The reporting is original research/enforcement by Microsoft about its own action, which can justify A, but the cited primary is a B-tier source; consider B2 or state why A.

**#35 F17, 2026-09-04/cve-2026-85046-chrome-v8-type-confusion-exploited**: credibility 2 with independent corroboration (low confidence). Quote: classification: {reliability: A, credibility: 2}  
Evidence and fix: With CISA KEV (independent assessor) and Proofpoint (independent observation of in-the-wild use from 2026-08-28) now corroborating Google's exploitation statement, credibility 1 (confirmed by other independent sources) fits the entry's own sourcing better than 2.

### Action-item discipline

**#36 F18, 2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal**: actions[0] (low confidence). Quote: "Rotate every Azure service-principal client secret, tenant ID or connection string that has ever appeared in a public GitHub issue, PR, commit or gist, including ones since edited or deleted."  
Evidence and fix: A tenant ID is an identifier, not a credential, and cannot be rotated; Microsoft says its client ID, client secret and tenant ID were exposed but the rotation guidance concerns credentials ("Immediately revoke or rotate the affected credentials"). As written the task is partly not executable. Say "client secrets, storage keys and connection strings" and, if wanted, add checking sign-in and ARM activity of the affected principal.

### Prior-iteration deltas (slice s4), confirmed this pass

- F1 Ivanti BSI URL: sources[] now carries BSI 2026-255045-1032; the fetched page is the 07.05.2026 EPMM warning. Confirmed.
- F3 Ivanti 2026-05-09 section: one citation per advisory (CERT-FR, BSI, NCSC-CH post 12548, all fetched); BSI says the credentials may have leaked in the January attacks. Confirmed.
- F3 Eurail: sample-and-sale warning now attributed to Eurail (BleepingComputer) with the Commission's 2026-01-13 "no evidence" line as a Contradiction. Confirmed; but the Correction and record now describe edits that were never published (new F4 #1).
- F3 Fox Tempest SDNY: cited to On the Issues, "civil" gone. Confirmed.
- F3 IBM mitigation and Affected: NCSC-CH attribution scoped to DoS vectors, "Workarounds: None" stated, ranges 9.0.0.0-9.0.5.28 / 8.5.0.0-8.5.5.29 match the bulletin. Confirmed; the fix-pack state is stale as of 2026-09-30 (new F8).
- F3 FortiSandbox: no FortiGate/FortiMail/FortiProxy/FortiClient or "pass as clean" wording remains in the body; the append-only 2026-06-17 record summary still says "FortiGate/FortiMail stack" and cannot be edited. Confirmed.
- F3 phpBB lede and leftover table: home-region claim and table gone. Confirmed; the new ACP sentence is contradicted by its source (new F3 #1).
- F3 Acronis CWE-276 and Chrome first paragraph: now cited to the KEV feed. Confirmed.
- F4 Eurail: "booking details" gone from the body, T1005 is a weak but defensible mapping of "breached its customer database ... transferred files from our network". Confirmed.
- F4 Fox Tempest: identity hedge and $5,000/$7,500/$9,000 tiers exact; labelled lines follow Microsoft's text; no EU-victim, shell-spawning or Key Vault advice left. Confirmed.
- F4 IBM: exploitation "unknown" per NCSC-CH, KEV absence dated and cited (kev.json 2026.09.29 has no CVE-2026-9170); evidence[1] is a contiguous substring of the bulletin; no Swiss or "fix packs out" claim. Confirmed.
- F4 phpBB: one scoring authority (Pentest-Tools 9.4/8.3, NVD 9.8/8.0 via heise), 48612 vector user-interaction, Apache-provider mechanism, both discoverers credited, OAuth workaround scoped to CVE-2026-48612, poc-public and affected/fixed filled. Confirmed.
- F4 Gitea: the ENABLE_REVERSE_PROXY_AUTHENTICATION precondition and known-or-guessable username appear in title, headline, summary, body, Exposure and cves[]; other-CVE descriptions match the Gitea post; no detection relies on an undocumented log field. Confirmed.
- F4 Langflow: KEV lists six Langflow CVEs on kev.json 2026.09.29 (9198, 0770, 55255, 34291, 33017, 3248); OSV/GitHub claims removed. Confirmed.
- F4 macOS: main analysis rewritten; SRP/RSA-SRP discriminator attributed to Huntress and hedged in Detection. Confirmed in part: Triage line and the 2026-08-16 section still over-reach (new F9, F13).
- F4 Chrome: no CVSS figure left; Proofpoint (2026-09-08) supports the BlueMoon chain; CVE-2026-85043 "Incomplete cleanup in Network" matches logic-flaw. Confirmed.
- F4 Cisco ISE: the hardening advisory footnote is reported without claiming CVE-2026-20192 itself is exploited; ISE-ABP and hardening pages carry CVE-2026-76460 and CVE-2026-20192 respectively; re-image instruction is verbatim. Confirmed; "never receive a fix" overstates (new F14).
- F4 Storm-3168: techniques[] identical to HEAD and absent from fields; summary/title use "possible", "unclear", "could not confirm"; takeaway states the SQL API-version failure. Confirmed.
- F13 ABW (entry), Acronis, Storm-3168 title: no passage in the entries ties the plants to hacktivists or weak passwords, states CISA's basis, or presents the secret as the route. Confirmed for the entries; the audit report's ABW row re-asserts the tie (new F13 #2).
- F14 Gitea, F5 Fox Tempest / Kemp, F7 Eurail, F8 IBM / Ivanti / Cisco / Langflow / Fox Tempest, F9 FortiSandbox, F11 (Ivanti title, Kemp / Langflow / Fox Tempest narration, FortiSandbox entities), F16 (IBM, Fox Tempest re-grades; Storm-3168 kept high, defensible: Azure is a widely deployed product and the action is time-bound), F18 (Gitea, Kemp): applied as described. Confirmed.
- F10 Ivanti June advisory: declined in the entry; the CCCS advisory is now confirmed (new F10).
- Audit report / run record from iteration 1: legacy count is 3 (confirmed on disk, git show HEAD), backlog 26 to 15 (confirmed, four of the 26 are 0404Z rows), SITE listed in sub_agents, die-linke in fetch_failures, gap_hours 9.09 (from the 2134Z audit start). Confirmed.

### Verdict

NEEDS_FIXES (truth: 22, editorial: 11, advisory: 3)

Coverage looks complete for the slice (no missed critical/high item beyond the Ivanti June EPMM advisory in F10). Style checks: no IOCs, no US federal KEV deadline used as a reason to act in slice text, inline citations present on factual sentences except the noted cases; em dashes remain in re-emitted text (F11).

### Findings summary (machine-readable)

See `work/2026-09-30T0639Z-audit/verification.iter2.s4.findings.yaml` (36 records).