# Iteration 1 remediation log (main agent)

Ref = slice#finding in verification.iter1.s<k>.findings.yaml. A = applied, D = declined (reason).

## 2026-05-14 GemStuffer
- s2#1 A: "not a RubyGems service" and "no source places RubyDoc.info inside RubyGems' trust boundary" removed from the section and the record summary (rubyhack.ai calls it RubyGems' automatic build system).
- s2#2 A: Exposure now says installs and pushes for existing users were unaffected (Ruby Central's words); "so no software consumed by others was compromised" dropped.
- s2#3 A: Triage clause replaced by Socket's own advice to block gem uploads from CI that does not publish.
- s2#4 A: "impersonating OpenAI" became "self-identifies with OpenAI" (rubyhack lists it under agents self-identified as OpenAI).
- s2#5 A: "July's" dropped (Euractiv gives no month).
- s2#6 A: the "find and use unremediated flaws" inference dropped.
- s2#31 A (this entry): priority high to notable (no constituency exposure, no compromise of existing packages).
- s2#32 D: credibility 2 stays; the entry's core finding (the registry used as an exfiltration channel) rests on Socket's analysis and RubyGems' own account, two assessors; the attribution is presented as the researchers' claim.
- s2#37 A (this entry): "replace detection advice Socket did not give" removed from section and summary.
- s2#38 D: earlier records' summaries are append-only (2026-09-19 GemStuffer, 2026-05-25 7-Eleven).
- s2#39 A: tags supply-chain and data-breach removed.
- s2#41 A: registry summary of tool:gemstuffer-rubygems-2026 rewritten.
- s2#43 A (quote case): evidence quote starts with lowercase "we" as on the page.

## 2026-05-10 Bauman University
- s1#4 A: "the documents themselves were not published" dropped from the section and the record summary.
- s1#24 A: priority notable to routine (no defender decision, no attacker behavior).
- s1#32 A: the record summary states the VSquare fact instead of narrating citation housekeeping.

## 2026-05-10 Braintrust
- s1#2 A: "org-level" now cited to SecurityWeek, which quotes Braintrust's notice; TechCrunch keeps the clause it carries.
- s1#14 A: T1496.004 replaced by T1528 (Steal Application Access Token), matching the sourced "likely gave the attackers access to the API keys"; "abuse signal" became "signal". Braintrust's own notice (trust.braintrust.dev/updates) is a JavaScript-only page no transport reads, so the entry stays aggregator-only.

## 2026-05-10 ClickFix macOS
- s1#33 A: two "rather than" clauses narrating removed text dropped.

## 2026-05-10 cPanel
- s1#5 A: the scores are attributed to the CVE records (HackerOne as numbering authority, per the EUVD API's assigner field), not to cPanel, in the body, the section, the sourcing note and the record summary.

## 2026-05-10 Groupe 3R
- s1#31 A: the record summary no longer narrates the removed playbook and actions.

## 2026-05-10 JDownloader
- s1#3, s1#15 A: the hash list is cited to JDownloader's own notice (its "known SHA256 checksums of the malicious substitute installer files"), and the "rather than a manifest of its own" negative is gone from the body and the record summary.

## 2026-05-11 pfSense CE
- s1#28 A: the privilege disagreement is stated: Netgate disputes CVE-2025-69691 as admin-only, while the CVE record's vector scores low privileges (EUVD-2025-209739).

## 2026-05-11 SMS-blaster
- s1#34 A: "not an Android 12 network-type call" and "not through the TelephonyManager call" dropped.

## 2026-05-12 Crimenetwork
- s1#19 A: "The only forward-looking statement" dropped (Help Net also quotes the BKA on another administrator).
- s1#35 A: the clause narrating removed claims dropped.

## 2026-05-12 GTIG AI threat tracker
- s1#6 A: "AI API secrets" dropped from the Exposure line (GTIG lists AWS keys and GitHub tokens).
- s1#16 A: headline says its discovery "may have prevented" mass exploitation, GTIG's own hedge.

## 2026-05-12 ICO / South Staffordshire Water
- s1#29 A: the CVE-2020-1472 cvss string now names MSRC's current 5.5 record and its disagreement with MSRC's own description.
- s1#36 A: two "rather than" clauses narrating removed text dropped from the section and the record summary.

## 2026-05-12 Checkmarx Jenkins plugin (TeamPCP)
- s1#7 A: Checkmarx's list is given as "among the applications the payload targets", without the exclusion.
- s1#17 A: headline says the credential-hunting build was live for about 31 hours (Checkmarx's malicious window), not that it hunted for 31 hours.
- s1#37 A: the composition sentence at the end of the section dropped.

## 2026-05-13 BWH Hotels
- s1#20 A: "three brands" became "the ... brands" in the body, the section and the record summary; the summary's narration of removed routes dropped.

## 2026-05-13 SPIP and Centreon (CERT-FR)
- s1#22, s1#23 D: the first sources[] record stays the original primary under the entry lifecycle; both sourcing notes already name the vendor bulletin as the assessment.

## 2026-05-13 Fortinet FortiAuthenticator / FortiSandbox
- s1#13 A: both EUVD source dates set to the records' publication date, 2026-05-12.
- s1#18 A: event_date 2026-05-13 to 2026-05-12, Fortinet's publication date.

## 2026-05-13 Exim dead letter
- s1#8 A: body, section and record summary now say no full exploit against the PIE build was reported: the researcher's side reached a leaked stack address, the LLM never reached a leak (XBOW).

## 2026-05-13 Foxconn
- s1#9 A: the factory-location list is cited to The Record, which carries it, with Foxconn's refusal to say how many were impacted.

## 2026-05-13 Microsoft MDASH
- s1#26 A: the takeaway adds MSRC's interim mitigation for CVE-2026-33824 (block or restrict inbound UDP 500 and 4500), cited to its advisory.
- s1#38 D: the benchmark figures are attributed to Microsoft and describe the tool that is the entry's subject (advisory).
- s1#39 A: "which is the exposure check now stated above" dropped.

## 2026-05-13 Mini Shai-Hulud (TanStack)
- s1#1 D: CISA publishes no per-CVE KEV page; the catalog feed is the store's established KEV citation.
- s1#11 A: the SHA-pinning clause replaced by what GitHub Security Lab says (pull_request_target plus an explicit checkout of an untrusted PR may lead to repository compromise).
- s1#12 A: the actions/cache README and npm docs records carry date null instead of the fetch date.
- s1#27 A: Wiz's qualifier added: a payload bug leaves the malware non-functional in the @uipath and @mistralai packages.

## 2026-05-13 TrickMo
- s1#10 A: the takeaway attributes to ThreatFabric only its finding (takedowns largely ineffective, blocking less effective); the device controls stand as derived advice without a citation.
- s1#40 A: composition narration removed from the section and the record summary.

## 2026-05-14 Ivanti Xtraction batch
- s1#21 A: "every flaw needs an authenticated account and none was exploited" replaced by Ivanti's own words (no evidence of exploitation in the wild) in the takeaway, sections, headline and summary.
- s1#25 A: priority notable to routine.
- s1#42 A: narration of removed claims dropped from the section.

## 2026-05-14 Dutch IGJ / Clinical Diagnostics
- s1#41 A: "that comparison is removed", "which is what the detection guidance above now rests on" and the priority narration dropped.

## 2026-05-14 FamousSparrow
- s2#8 A: the takeaway gives Bitdefender's general lesson (actors re-exploit the access path until it is patched and credentials rotated), not a claim about this case.
- s2#26 D: KEV catalog feed (same reason as s1#1).
- s2#31 A (this entry and the CISA contractor entry): priority high to notable.
- s2#37 A (this entry): "The detection guidance now follows ..." dropped.
- s2#42 D: tool and loader file names (LMIGuardianSvc.exe, winmm.dll, gh-token-monitor, setup.mjs) are behavioral triage artifacts, not hashes, IPs or domains (advisory).

## 2026-05-14 The Gentlemen backend leak
- s2#7 A: DynaRisk's statement is given as the group's discussions (BankInfoSecurity: "regularly discussed ways to disable endpoint security tools ... modify Group Policy Objects and gain domain admin").

## 2026-05-15 Nextcloud
- s2#12 A: BSI's WID-SEC-2026-1517 is said to cover the four CVEs its CSAF lists.
- s2#28 A (this entry, AMD and F5): priority notable to routine for regular-cycle patches.
- s2#37 A: narration of "the earlier text" dropped.
- s2#43 D: "version" stays before four-part version numbers so the IOC scan does not read them as IPv4 addresses.

## 2026-05-15 Composer
- s2#27 A: the uncited "Personal access tokens are not part of the issue" replaced by the advisory's own statement on classic ghp_ tokens, cited.
- s2#30 A (this entry and Sophos): verification multi-source to single-source, matching the sourcing notes.
- s2#36 A: the advisory's High 7.5 header and its "Severity: medium" text are both stated.

## 2026-05-15 Datadog / Shai-Hulud framework
- s2#9 A: TanStack and UiPath, not OpenSearch.
- s2#10 A: OS-specific lists of more than 100 sensitive file paths.
- s2#11 A: "was not leaked" and "released deliberately" dropped from the section and the record summary; the README and commit facts stand.
- s2#33 A: Detection adds the disguised secrets-dumping workflow and the deleted workflow runs and branches (Datadog's table).
- s2#37 A: "are now stated" dropped from the record summary.

## 2026-05-15 FrostyNeighbor
- s2#21 A: ESET's hedge restored in the summary ("very likely decide manually").
- s2#37 A: "which the detection guidance now covers" dropped from the record summary.

## 2026-05-15 Sophos identity survey
- s2#25 A: the negative replaced by Sophos' own statement that attackers increasingly use stolen credentials as their primary delivery mechanism; the narration of removed cross-links dropped.

## 2026-05-16 AMD-SB-7052
- s2#13 A: the takeaway states what AMD lists (OEM BIOS PI versions for Ryzen-class parts) and what MSRC says (a Windows update for certain AMD models), not the inference that an OS update does not mitigate Ryzen; the record summary drops the same inference.
- s2#37 A: the section paragraph narrating the removed CVE table reduced to the NCSC-NL fact.

## 2026-05-16 Dream Market
- s2#14 A: headline attributes the wallet reactivation to US prosecutors.
- s2#15 D: T1597.002 stays. The US Attorney states the marketplace earned commissions from selling stolen personally identifiable information, and T1597.002 is the purchase of victim data on cybercrime markets; without it the threat-kind gate cannot pass, and inventing an access vector would be worse. Law-enforcement entries without TTP content go to the tracker as an operator recommendation.
- s2#29 A (this entry, Interpol, Arwini, 7-Eleven): priority notable to routine. FunnelKit keeps notable (an exploited flaw with a patch). D: the bodies are not cut to two sentences, because entries are removed only by folds and their verified content stays.

## 2026-05-16 OpenClaw
- s2#17 A: the "CVSS 3.1" label dropped from Cyera's scores in cves[] and the section.
- s2#18 A: the GHSA is described as the advisory for the heredoc allowlist bypass, not as carrying the CVE id.

## 2026-05-16 SentinelOne
- s2#19 A: "JetBrains fixed that flaw" became "JetBrains fixed CVE-2023-42793 ..."; the body already says the post links JetBrains' advisory.

## 2026-05-17 SzafirHost
- s2#20 A: "a Szafir qualified certificate" became "a qualified signature" in the body and summary.

## 2026-05-18 Tycoon 2FA
- s2#22 A: summary says eSentire's hunts look for the signals, not that it found the campaign through them.
- s2#23 A: the negative replaced by eSentire's quoted consent prompt.
- s2#34 D: the first sources[] record stays the original primary (lifecycle); for F5, SecurityWeek and EUVD carry the cited facts and the sourcing note says so.

## 2026-05-19 7-Eleven
- s2#24 A: the 2026-05-01 letter date is cited to Cybersecurity Dive.
- s2#35 A: this run's section adds CyberInsider's later update (Charter dataset leaked, 4.9 million email addresses per Have I Been Pwned).

## 2026-05-19 CISA contractor (Nightwing)
- s2#16 A: T1593.003 removed (the only repository scanning described is GitGuardian's, a defender).

## Slice 3 dispositions
- s3#1 A: Calypso, JFMBackdoor's capabilities follow PwC, self-removal included.
- s3#2 A: Storm-2949, the takeover of the web app is Microsoft's belief.
- s3#3 A: Storm-2949, the Defender step is an attempt ("tried to weaken"); the log clearing stays (Microsoft's detections table lists it).
- s3#4 A: ChromaDB, "ChromaToast" and the CVSS 4.0 label are cited to Hadrian, BleepingComputer keeps the maximum-severity clause.
- s3#5 A: Webworm, the Aquatic Panda alias is cited to The Hacker News.
- s3#6 A: Keycloak, the summary splits the fixes (CVE-2026-7507 in 26.2.16 and 26.4.12, CVE-2026-37982 in 26.4.12).
- s3#7 A: CVE-2026-41091, the 2026-04-16 publication is cited to Help Net Security.
- s3#8 A: CVE-2026-41091, the Detection order follows Help Net Security (files dropped and renamed, then discovery, then the exploits).
- s3#9, s3#16 A: Sparx, the scores are attributed to CCB and the disagreement with the vendor is stated.
- s3#10, s3#11 A: Drupal, Exposure and Detection follow the advisories (Symfony/Twig wording, the scanning markers).
- s3#12 A: vm2, CVE-2026-26956 affected is "3.10.4 and earlier" per the GHSA.
- s3#13 A: vm2, CVE-2026-44007 auth is admin-required (PR:H).
- s3#14 A: fast16, T1014 removed.
- s3#15 A: PinTheft, the title says "among the distributions it tested".
- s3#17 A: Nx, StepSecurity's 12:36 UTC publication time is stated beside Nx's times.
- s3#18 A: ChromaDB, Hadrian's acknowledgement on 2025-12-16 and the silence after it are stated.
- s3#19 A: Storm-2949, Detection adds the Authentication Methods registration events.
- s3#20 A: SonicWall, cves[] affected and fixed carry the full advisory table (Gen7 7.0.1 and 7.1.1 lines, Gen8 TZ80, Gen6 NSv fix, SMA100), Exposure adds one sentence, and SonicWall SMA 100 is in affected_products.
- s3#21 D: Keycloak CVE-2026-6856 keeps no score: Red Hat's figure is a preliminary score on a page the entry does not cite, and the CVE's facts are carried by the GitHub issue.
- s3#22, s3#23, s3#24 A: Defender CVE-2026-45584, Azure Local CVE-2026-42822 and B1ack's Stash moved from notable to routine.
- s3#25 A: Calypso, high to notable.
- s3#26 D: the correction sections state what the published entries got wrong; those entries were live since May, so readers saw the statements now corrected (docs/pipeline.md, record types: a correction section "records what was wrong"). None is a metadata-only section.
- s3#27 A: 17 record summaries rewritten to state the finding rather than the rewrite (main/narrating-summaries.json).
- s3#28 A: CVE-2026-41091, "CVSS 3.1 base score 4.0".
- s3#29 D: the DBIR entry is an annual report whose content is the year-over-year figures, kept at notable as primary research.
- s3#30 D: sources[] roles are only primary and corroborating; the Chancellery page backs the entry's Swiss exposure remark and stays.
- s3#31 A: report and run record give 398 mappings over 171 distinct ids (recounted after the slice fixes) and 35 priority moves.
- s3#32 D (pre-existing): the Bronze Medley alias on the Calypso campaign record goes to tracker row W4-07 with the Red Lamassu actor proposal.
- s1#30 D: CVE-2026-41940 is already named as a coverage gap in the run record and goes to the tracker.
- s1 gate WARN A: Sophos survey maps T1078 (Sophos: attackers increasingly use stolen credentials as their primary mechanism for delivery). Bauman, NCSC UK and Braintrust keep their WARNs: no TTP content, no TTP content, and a JavaScript-only primary.
- s2#40 A: F5 and 7-Eleven sourcing notes state which source carries the facts, without narrating fetch failures.
