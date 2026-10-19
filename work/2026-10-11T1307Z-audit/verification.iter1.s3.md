**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T15:20:22Z · ended_at=2026-10-11T15:50:41Z · duration_seconds=1819

## Verification report — 2026-10-11T1307Z-audit (iteration 1, slice s3)

Scope: 23 entries, 322 ledger claims; every claim has a verdict row in `verification.iter1.s3.claims.yaml` (305 ok, 9 F3, 5 F4, 3 unreadable). Whole entries read, newest section against main analysis, this fire's `git diff` read for every entry. Sources fetched this iteration with `extract`/`url`/`pdf`/`cisa-kev`/`ncsc-csh`; cisa.gov alerts via WebFetch with the outbound-links template; Computing UK (Gambit entry) unreadable on every rung (HTTP 403 on extract/url/jina/WebFetch).

### Citation does not support the claim

**#1 · F3 · `2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou`** — summary; body para 1 ("Seven Dutch universities disconnected Canvas ([DutchNews.nl, 2026-05-08])"); Update 2026-05-10 (lists the seven as having disconnected, cited to DutchNews); Correction 2026-10-11
- Finding: Claim 'Seven Dutch universities disconnected Canvas', cited to DutchNews.nl, is not what that page says. The fact is true (NL Times), but the cited sources do not carry it.
- Evidence: DutchNews 2026-05-08: Canvas break-in 'affecting millions of students ... including seven Dutch universities'; only 'Amsterdam's VU university said ... it had decoupled all its links to the Canvas system'. Techzine 2026-05-08: 'Vrije Universiteit (VU) Amsterdam has disconnected all systems ... Seven Dutch universities have been affected' (UNL lists the seven as 'affected'). NL Times 2026-05-09 (fetched this iteration): 'All seven Dutch universities using the Canvas education platform disconnected the system'. (https://nltimes.nl/2026/05/09/dutch-universities-disconnect-canvas-hackers-claim-continued-access)
- Fix: Add the NL Times article as a source and cite it for 'seven Dutch universities disconnected Canvas' (summary, body, 05-10 section, correction); keep DutchNews for the re-breach message and Techzine for VU's DPA report.

**#2 · F3 · `2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen`** — Correction 2026-10-11T14:58:10Z and its record summary
- Finding: 'gateways on them need migration to a supported release rather than a hotfix ([Rapid7])' and the record's 'which have no hotfix path' are not in the cited page.
- Evidence: Rapid7: 'four of the nine affected version branches (R80.20.X, R80.40, R81, R81.10) have reached End of Support. Organizations still running these versions should prioritize migration to a supported release.' Check Point blog: 'Update all affected Security Gateways to the released hotfix', and its table lists the EOS branches as affected with sk185033. Neither says no hotfix exists for the EOS branches. (https://www.rapid7.com/blog/post/etr-critical-check-point-vpn-zero-day-exploited-in-the-wild-cve-2026-50751/)
- Fix: Reword to 'should prioritize migration to a supported release' and drop 'rather than a hotfix' / 'no hotfix path'.

**#3 · F3 · `2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes`** — body paragraph 1 ("issued a formal public statement on 28-29 May 2026 ... ([The Record, 2026-05-29])")
- Finding: The statement is MSRC's blog post of Wednesday 2026-05-27; 28-29 May are the press-coverage dates. It is also a Microsoft/MSRC statement that mentions the DCU, not a DCU statement.
- Evidence: The Record 2026-05-29: 'In a blogpost on Wednesday, Microsoft said ...'. MSRC blog page date 2026-05-27. (https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure)
- Fix: Give 27 May 2026 and attribute it to Microsoft's MSRC blog.

**#4 · F3 · `2026-05-09/cve-2026-40982-spring-cloud-config-server-pre-authentication`** — Exposure line ("...which typically holds credentials for the services that consume it ([Spring, 2026-05-06])")
- Finding: The credentials clause is cited to the Spring advisory, which does not carry it.
- Evidence: Spring advisory: 'Spring Cloud Config allows applications to server arbitrary text and binary files ... a request using a specially crafted URL that can lead to a directory traversal attack.' HeroDevs: 'the Config Server centralizes secrets for an entire fleet of microservices'. (https://www.herodevs.com/blog-posts/cve-2026-40982-critical-spring-cloud-config-server-directory-traversal-cvss-9-8)
- Fix: Cite HeroDevs for the credentials clause.

**#5 · F3 · `2026-08-29/exchange-mrsproxy-auth-bypass-cve-2026-62911-poc`** — body paragraph 1 ("Without that check, an attacker who captures or coerces a Negotiate/NTLM authentication exchange can relay it ... ([MSRC, 2026-08-11])")
- Finding: (low confidence) The relay/Negotiate/NTLM/coercion mechanism clause is terminated by an MSRC citation; MSRC carries only the capture-replay classification and the FAQ line. The mechanism is Franky's Web and MB VRED; the preceding Franky's Web citation mitigates.
- Evidence: MSRC: 'Authentication bypass by capture-replay ... allows an authorized attacker to elevate privileges over a network'; FAQ: 'The attacker would be able to take over the mailboxes of all Exchange users ...'. Franky's Web: 'an attacker can relay the authentication of the server account to the endpoint'. (https://www.frankysweb.de/en/exchange-public-exploit-for-critical-vulnerability-cve-2026-62911/)
- Fix: Add the Franky's Web / MB VRED citations to the mechanism clause.

**#6 · F3 · `2026-09-10/sap-september-2026-overpass-s4get-preauth-rce`** — Correction 2026-10-11T13:56:20Z ("the 7.22 and 8.04 unicode and non-unicode kernels")
- Finding: (low confidence) CERT-EU lists the non-unicode kernel only at 7.22/7.22EXT; 8.04 appears only for the unicode kernel.
- Evidence: CERT-EU 2026-011: 'KRNL64NUC 7.22, 7.22EXT; KRNL64UC 7.22, 7.22EXT, 7.53, 8.04'. (https://cert.europa.eu/publications/security-advisories/2026-011/)
- Fix: Say '7.22 (unicode and non-unicode), 7.53 and 8.04 (unicode)' or drop the unicode clause.

**#7 · F3 · `2026-06-14/cve-2026-20253-splunk-enterprise-unauthenticated-pre-auth-rc`** — sources[0].date
- Finding: (low confidence) Splunk advisory carries date 2026-06-18; the page says Published 2026-06-10, Last Update 2026-06-18 (the exploitation note). The entry's own correction says 'The fixes date from 2026-06-10'.
- Evidence: Splunk SVD-2026-0603 header: Published: 2026-06-10; Last Update: 2026-06-18. (https://advisory.splunk.com/advisories/SVD-2026-0603)
- Fix: Use 2026-06-10 as the source date.

**#8 · F3 · `2026-09-17/mandiant-ai-risk-resilience-report-2026`** — body para 1 ("The 2026 edition, published 2026-09-15") and every [Mandiant, 2026-09-15] citation / sources[0].date
- Finding: (low confidence) No page read this iteration gives 2026-09-15: the Google Cloud page shows only 'September 2026' (extract metadata 2026-10-08); Help Net Security's coverage is dated 2026-09-16.
- Evidence: Google Cloud report page: 'A Mandiant special report 2026 / September 2026'. (https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)
- Fix: Use 'September 2026' or cite a source that dates the release.

### Unsupported / hallucinated facts

**#9 · F4 · `2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen`** — body paragraph 1 ("The kill chain, affected trains and hunt concepts are in the [companion deep-dive of the same day](../2026-06-09/check-point-ikev1-vpn-authentication-bypass-cve-2026-50751.md).")
- Finding: The sentence points readers to a companion deep-dive that this fire deleted (fold, record `merged_from: [2026-06-09/check-point-ikev1-vpn-authentication-bypass-cve-2026-50751]`). `references[]` was emptied but the pointer stayed, and the survivor carries no kill chain or hunt concepts.
- Evidence: git status: 'D entries/2026-06-09/check-point-ikev1-vpn-authentication-bypass-cve-2026-50751.md'; the survivor body has only Exposure/Detection/Defender takeaway lines.
- Fix: Delete the sentence (or fold the sourced kill-chain/hunt content from the deleted entry into the survivor).

**#10 · F4 · `2026-06-14/cve-2026-20253-splunk-enterprise-unauthenticated-pre-auth-rc`** — Defender takeaway ("a host that ran an affected version with the sidecar enabled after mid-June needs a compromise check alongside the upgrade")
- Finding: The 'after mid-June' threshold is in no cited source and is narrower than what the sources allow.
- Evidence: Splunk SVD-2026-0603 (published 2026-06-10; changelog 2026-06-18): 'In June 2026, the Splunk PSIRT became aware of limited exploitation of this vulnerability.' SecurityWeek 2026-06-19: exploited 'only days after its public disclosure' (disclosure 2026-06-10). watchTowr PoC dated 2026-06-12. (https://advisory.splunk.com/advisories/SVD-2026-0603)
- Fix: Anchor the compromise check at the 2026-06-10 advisory (or 'since June 2026').

**#11 · F4 · `2026-09-04/cve-2026-85046-chrome-v8-type-confusion-exploited`** — Correction 2026-10-11T14:02:26Z + its record summary, versus the Detection paragraph
- Finding: The correction says Proofpoint documents 'a fixed curl download-and-execute command ... it does not describe the command itself as configurable', and the record says 'a fixed curl download-and-run command'. Proofpoint documents per-actor variants, so the original 'operator-specified' wording was supported, and the Detection paragraph still says 'because the command is configurable', so the entry now contradicts itself.
- Evidence: Proofpoint 2026-09-08: UNK_DoubleCheck 'Following successful exploitation, the following command is run to download multiple files from a separate actor-controlled domain, rather than the default msgbox.exe configuration: cmd.exe /c curl.exe -k -o ...'; UNK_QuietRacket 'modified the final BlueMoon pp injector shellcode to instead download and execute a DLL-sideloading pair'; the chrome.exe -> cmd.exe -> curl.exe -> msgbox.exe tree is described only for 'Default BlueMoon deployments'. (https://www.proofpoint.com/us/blog/threat-insight/once-bluemoon-multiple-state-aligned-threat-actors-rapidly-adopt-novel-exploit)
- Fix: State the default chain (chrome.exe -> cmd.exe -> curl.exe -> msgbox.exe, URL from the kit's exeUrl) and that other actors change the command or payload; drop or correct the 2026-10-11 section and its record summary.

**#12 · F4 · `2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes`** — body last sentence ("Next Patch Tuesday: 10 June 2026.")
- Finding: False and unsourced: June 2026 Patch Tuesday is Tuesday 9 June (10 June 2026 is a Wednesday).
- Evidence: Calendar: 2026-06-09 = Tuesday, 2026-06-10 = Wednesday; Microsoft Patch Tuesday is the second Tuesday. No cited source gives the date.
- Fix: Correct to 9 June or delete the sentence.

**#13 · F4 · `2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes`** — frontmatter techniques [T1068] (added this fire) and cves[CVE-2026-45585]
- Finding: (low confidence) The T1068 mapping, added by this fire's internal record as 'the privilege-escalation mapping of the local flaws it describes', has no support in the cited pages; cves[] types CVE-2026-45585 as lpe/local/post-auth although the body itself calls YellowKey a 'BitLocker bypass ... requiring physical access'; status no-patch conflicts with the store's sibling entry (mitigation-only) and with MSRC's current page.
- Evidence: heise: GreenPlasma 'allows arbitrary keys to be created in the Windows Registry without authorization'; The Record gives no escalation mechanism; MSRC CVE-2026-45585 page lists KB5095051/KB5094125/KB5094126 and an interim WinRE mitigation script. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585)
- Fix: Re-type YellowKey as a physical-access BitLocker bypass, refresh the patch status, and source or drop T1068.

**#14 · F4 · `2026-06-10/year-old-winrar-flaw-cve-2025-8088-still-fuels-ukraine-intru`** — body ("Both actors moved C2 off Telegram to dedicated servers after Russia's February 2026 Telegram block.")
- Finding: Only SHADOW-EARTH-066/GIFTEDCROOK is reported to have moved off Telegram, and both sources hedge the cause.
- Evidence: The Hacker News 2026-06-09: 'A notable change is the shift from Telegram as an exfiltration channel to dedicated command-and-control (C2) servers, a key modification that likely aligns with Russia's blocking of the messaging platform'. Trend Micro: 'possibly tracks with a broader change'. Earth Dahu is not described as using Telegram in either source. (https://thehackernews.com/2026/06/winrar-flaw-exploited-by-russia-aligned.html)
- Fix: Limit to SHADOW-EARTH-066 and keep the hedge ('likely aligns with').

**#15 · F4 · `2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix`** — main analysis paragraphs 2, 3 and 5, versus sections 2026-08-21/08-24
- Finding: The unchanged main analysis still asserts what the entry's own newest sections disprove: para 3 'no technical analysis of ShieldBreak itself has been published'; para 5 'Detection concepts follow the RoguePlanet chain rather than ShieldBreak's unpublished internals, so they are hypotheses'; para 2 'Treat the reliability figure and the server coverage as unverified until someone reproduces them'.
- Evidence: LevelBlue SpiderLabs (2026-08-19): 'The LevelBlue OpsCTI and THOR teams reviewed and reproduced the complete ShieldBreak exploitation chain with the August 2026 Patch Tuesday updates installed, confirming the PoC functions as described' ... 'runs to full SYSTEM completion ... on any fully patched Windows 11 24H2 or Windows Server 2025 system'. Full mechanism and hunting package published. (https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking)
- Fix: Rewrite the three statements to the current state (mechanism published, independently reproduced incl. Server 2025, engine fix shipped) or mark them as the disclosure-day position.

**#16 · F4 · `2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix`** — frontmatter sourcing_note; evidence[] quote attributed to MSRC
- Finding: sourcing_note still says both sources report only the researcher's claims and that the technical claims 'are so far uncorroborated by any vendor or independent analysis'; the entry now has seven sources, Microsoft's own CVE record naming ShieldBreak, and LevelBlue's independent reproduction on Windows Server 2025. Also (low confidence) the evidence quote 'We are working to provide a high quality security update that addresses this vulnerability.' is no longer on the MSRC page (revised 2026-09-03).
- Evidence: MSRC CVE-2026-69414: 'Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft Defender publicly referred to as "ShieldBreak"'; first version addressed 1.1.26080.3. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)
- Fix: Rewrite sourcing_note to current provenance; mark the MSRC quote as the 2026-08-14 revision or replace it.

### Claims missing inline citation

**#17 · F5 · `2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes`** — body paragraphs 2-3
- Finding: Almost everything after the first sentence is uncited: the six-vulnerability list with CVE ids and in-the-wild exploitation, 'MiniPlasma specifically abuses ... cldflt.sys to achieve a SYSTEM shell ... on fully-patched Windows 11', 'root cause ... incomplete remediation of CVE-2020-17103', and the AppLocker/WDAC advice. The cited pages give ITW exploitation and KEV listing for the first three (The Record) and 'GreenPlasma and MiniPlasma (both tracing back to CVE-2020-17103)' (heise); none names cldflt.sys, SYSTEM, Windows 11 or AppLocker/WDAC.
- Evidence: The Record and heise pages as fetched. (https://www.heise.de/en/news/Too-many-zero-days-Microsoft-threatens-legal-action-11310736.html)
- Fix: Cite each fact or remove the cldflt.sys / SYSTEM / Windows 11 / AppLocker detail.

**#18 · F5 · `2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft`** — cves[] fixed/affected for CVE-2021-22205 and CVE-2021-3199 (and the BIND/Pulse/Bash fixed versions)
- Finding: (low confidence) This fire's internal record adds vendor fix data '(GitLab)' and '(ONLYOFFICE Document Server changelog)' and replaces GitLab's affected range 'All versions starting from 11.9' with GitLab's three ranges, but neither vendor page is in sources[] or the body. The values check out.
- Evidence: GitLab CNA record: '>=11.9, <13.8.8; >=13.9, <13.9.6; >=13.10, <13.10.3'; ONLYOFFICE changelog: '## 5.6.3 ... Fix Path Traversal vulnerability via image upload params (Bug #46113)'. (https://gitlab.com/gitlab-org/cves/-/raw/master/2021/CVE-2021-22205.json)
- Fix: Add the GitLab CVE record and the ONLYOFFICE changelog to sources[] and cite them where the body discusses the CVEs.

### Needs more research

**#19 · F8 · `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce`** — main analysis labelled lines
- Finding: (low confidence) The main analysis closes with Exposure, Detection and Triage but has no '**Defender takeaway:**' line; takeaways exist only inside the 2026-08-06 and 2026-09-30 update sections (two separate ones). The actionability contract requires the line on every entry.
- Evidence: Entry text.
- Fix: Fold one current Defender takeaway into the main analysis and drop the duplicates from the sections.

**#20 · F8 · `2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen`** — Detection line
- Finding: (low confidence) Detection is one sentence (start the log audit on 7 May). Check Point's own post describes post-exploitation behavior (attempts to download ELF files from actor infrastructure overlapping Qilin Linux ransomware binaries; VPS infrastructure matching victim geography) and Help Net Security reports the bypass also works over TCP 443 when UDP is blocked; none of it reached a telemetry-class detection hint on a critical entry.
- Evidence: Check Point blog 'Actor profile': 'attributional overlap between Qilin Linux ransomware binaries and attempts to download malicious ELF files from actor-controlled infrastructure'. (https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/)
- Fix: Add a sourced, telemetry-first detection sentence (remote-access session establishment without a matching authentication event; outbound ELF download attempts).

### Surface contradiction

**#21 · F9 · `2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes`** — title, headline, summary/body para 1 ("Microsoft's Digital Crimes Unit threatens criminal action")
- Finding: The cited primary says Microsoft stopped short of threatening legal action; heise's headline says it threatens legal action. The entry silently takes the stronger reading and 'criminal' appears in neither.
- Evidence: The Record: 'The company stopped short of directly threatening legal action, but said: "Our Digital Crimes Unit will continue bringing cases against these actors ..."'. heise: 'Too many zero-days: Microsoft threatens legal action' ('threatening lawsuits and the police'). (https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more)
- Fix: State the divergence in a Contradiction line and drop 'criminal action' from the title.

### Editorial / less-is-more flags (advisory)

**#22 · F11 · `2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce`** — body paragraph 1
- Finding: Garbled duplicated clause introduced by this fire's rewrite: "Cisco states the flaw was found during the resolution of a Cisco TAC support case and that it is aware of active exploitation it is aware of active exploitation".
- Evidence: Cisco advisory: 'The Cisco PSIRT is aware of active exploitation of this vulnerability.' (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5)
- Fix: Delete the repeated 'it is aware of active exploitation'.

**#23 · F11 · `2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou`** — Update 2026-05-09 and Correction
- Finding: (low confidence) The 2026-05-09 update cites The Register dated 2026-05-12 (a section dated before its own source); the Correction says 'No source supports ... 44 confirmed Dutch institutions' although NL Times 2026-05-05 reports 44 Dutch institutions on ShinyHunters' victim list per BNR (listed, not confirmed).
- Evidence: NL Times 2026-05-05: 'The Dutch impact affects 44 universities, applied sciences universities, and secondary schools ... according to a list of victims shared on the dark web by ShinyHunters, which was reviewed by BNR'. (https://nltimes.nl/2026/05/05/canvas-hack-student-data-44-dutch-universities-schools-taken-massive-breach)
- Fix: Optional: say '44 Dutch institutions appeared on the actor's list per BNR; unconfirmed'.

**#24 · F11 · `2026-08-29/exchange-mrsproxy-auth-bypass-cve-2026-62911-poc`** — body paragraph 2
- Finding: English quotations of German/Dutch text in the main analysis lack the '(translated from German/Dutch)' marker: CERT-Bund 'enabl[es] the complete remote takeover of systems without authentication' and NCSC-NL 'allows an unauthenticated attacker to execute arbitrary code' (the 2026-09-01 section marks its translated quote).
- Evidence: CERT-Bund: 'der die vollständige Übernahme von Systemen aus der Ferne ohne Authentifizierung ermöglicht'; NCSC-NL: 'stelt een ongeauthenticeerde kwaadwillende in staat om willekeurige code uit te voeren'. (https://social.bund.de/@certbund/117171896801475447)
- Fix: Add the translation markers.

**#25 · F11 · `2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes`** — summary, body opener, sourcing_note, labelled lines
- Finding: Workflow-internal language in reader-facing fields: 'UPDATE (originally covered 2026-W21)' in summary and body; sourcing_note 'migration: update target unresolved (no originally-covered date in v2 body)'; summary truncated mid-citation ('(The Record ...'); headline identical to title; no Exposure/Detection/Defender takeaway labelled lines (closing paragraph carries unlabelled advice).
- Evidence: Entry text.
- Fix: Rewrite summary and sourcing_note as plain provenance; add the labelled lines.

**#26 · F11 · `2026-06-10/year-old-winrar-flaw-cve-2025-8088-still-fuels-ukraine-intru`** — sourcing_note, body, entities
- Finding: sourcing_note still reads 'migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)' although this fire replaced that evidence with a verbatim Trend Micro sentence (stale and workflow-internal); ATT&CK ids listed in prose '(T1059.005, T1547.001, T1555.003)'; entities: [] although registry key campaign:uac0226-giftedcrook-winrar-cve-2025-8088 describes this finding; the hunting sentence (Sysmon EID 11, EID 4104) is uncited and partly beyond Trend Micro's own list ('Monitor for mshta.exe execution from the Startup folder'); no labelled lines.
- Evidence: Trend Micro hunting list; registry entry.
- Fix: Rewrite sourcing_note, drop ids from prose, link the registry key, cite or trim the hunt sentence.

**#27 · F11 · `2026-09-21/afpa-third-party-accommodation-tool-data-extraction`** — body
- Finding: Composition-rationale sentence in reader-facing text: 'It is relevant as a European public agency exposed through a vendor-hosted administrative tool.'
- Evidence: Entry text.
- Fix: Delete the sentence (the takeaway already carries the lesson).

**#28 · F11 · `2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix`** — body sections 2026-08-21 and 2026-09-13
- Finding: Workflow-internal language in reader-facing text: 'This pipeline recorded CVE-2026-69414 three days ago ...', 'this entry's standing "no fix available" status was stale', 'which is what this entry has told readers since 2026-08-12', and the 09-13 record summary ends 'Surfaced by this audit's coverage re-sweep.'; three successive 'Defender takeaway' blocks (two superseded).
- Evidence: Entry text.
- Fix: Reword to plain provenance and keep one current Defender takeaway.

**#29 · F11 · `MULTI (shieldbreak 49, mandiant 18, exchange-mrsproxy 16, winrar 6, nightmare 3, kemp 3, sap 2, cisco 2, chrome 1)`** — body/title
- Finding: Reader-facing text contains em dashes (counts exclude the '## <Type> — <at>' headings).
- Evidence: style rule: no em dash in reader-facing entry text
- Fix: Replace with commas or colons.

**#30 · F11 · `MULTI (cve-2026-63077-teamcity, gambit)`** — Correction sections
- Finding: Correction sections narrate the entry's own earlier wording rather than stating a reader-facing delta: TeamCity 'JetBrains did not say it withheld a gadget chain ... The deserialization class comes from CISA's catalog record, and the exploitation status rests on two independent statements'; Gambit 'The 2026-09-25 note that it rebuilt within hours went beyond that.' (check 4c(i): internal-record candidates).
- Evidence: Entry text.
- Fix: Make the section a plain dated statement or mark the record internal.

### Single-source items missing [SINGLE-SOURCE] flag

**#31 · F12 · `2026-09-21/afpa-third-party-accommodation-tool-data-extraction`** — frontmatter verification
- Finding: (low confidence) The 2026-10-11 record lowers credibility to 2 because every fact traces to AFPA via the AFP wire, yet verification stays multi-source; the sourcing_note says Cyberattaque.org and FrenchBreaches only paraphrase AFPA's confirmation. AFPA is the victim, so single-source-victim fits.
- Evidence: Clubic relays AFP/franceinfo quoting AFPA deputy director Pierre Prady; Cyberattaque.org: 'L'AFPA confirme désormais ...'. (https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html)
- Fix: Set verification to single-source-victim (keep the sourcing_note) or state what the trackers corroborate independently.

**#32 · F12 · `2026-06-10/year-old-winrar-flaw-cve-2025-8088-still-fuels-ukraine-intru`** — frontmatter verification
- Finding: verification: multi-source although the audit's own record describes the basis as 'Trend Micro research relayed by The Hacker News'; THN relays Trend Micro's analysis. Trend Micro is not on the national-CERT carve-out list.
- Evidence: THN: 'Trend Micro researchers ... said in an analysis published Monday'. (https://thehackernews.com/2026/06/winrar-flaw-exploited-by-russia-aligned.html)
- Fix: Set verification: single-source and write a sourcing_note naming Trend Micro as the sole assessor.

### Org-triage line missing / inconsistent

**#33 · F16 · `2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix`** — priority
- Finding: (low confidence) priority: high is unchanged since the 2026-08-12 unpatched/public-PoC position. Microsoft shipped engine 1.1.26080.3 (MSRC revised 2026-09-03), its record says Exploited: No, and the only open item is the researcher's own ShieldCrash claim, a 'skeleton PoC' with file reads only and no confirmed in-the-wild exploitation; local post-auth escalation. Research without in-the-wild use is a high-bar disqualifier.
- Evidence: SOCRadar: 'ShieldCrash does not currently have a separate CVE ... a skeleton PoC ... no confirmed evidence that ShieldCrash is being exploited in the wild.' (https://socradar.io/blog/shieldcrash-poc-microsoft-defender-fix-bypass/)
- Fix: Recalibrate to notable (the engine-version action can stay).

### Action-item discipline

**#34 · F18 · `2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix`** — actions[1] ("Hunt for C:\Windows\System32\phoneinfo.dll across the Windows estate now ...")
- Finding: Restates the body's detection paragraph (check 10b b) and is a file-name indicator of the kind the no-IOC rule bars; the body also names phoneinfo.dll, the WD_SCAN symlink name and a hardcoded pipe name. Keep action 0 (engine version).
- Evidence: LevelBlue: 'phoneinfo.dll is not a native Windows DLL; therefore its creation under C:\Windows\System32 should receive immediate attention'. (https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking)
- Fix: Drop the action and describe the behavior (sync-root registration, Defender library load by a non-Defender process, wermgr.exe loading an unexpected DLL) in the body only.

### Notes that are not findings

- Computing UK (https://www.computing.co.uk/news/2026/security/ai-agents-used-to-steal-credit-card-records) cannot be read by any transport; claims cfc7d96ef0, 4ffc4a679c and c1f9fa658d (Gambit entry's 2026-10-11 correction: 'repeatedly rebuilt the infrastructure and continued the attacks') carry verdict `unreadable`, not ok. The 'rebuilt within hours' wording exists only in the append-only 2026-09-25 record summary; the Update body already says 'repeatedly rebuilt'.
- UAT-11587 internal record says the body 'already states' host-information collection (T1082); the body does not, but Talos's command table does ('system_info: Collects host and process context'), so the mapping is supported.
- Shieldbreak record says 'the earlier entry' (singular) for two added references; both referenced entries carry CVE-2026-50656.
- Coverage / missed angles: nothing to add from this slice (WP2Shell, mentioned by the NCSC-CH ClickFix page, is already in the store).

### Verdict

NEEDS_FIXES (truth: 16, editorial: 9, advisory: 9)

### Findings summary (machine-readable)

See `work/2026-10-11T1307Z-audit/verification.iter1.s3.findings.yaml` (one record per finding above).