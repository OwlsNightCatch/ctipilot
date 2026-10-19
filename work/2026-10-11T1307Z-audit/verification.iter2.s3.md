**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T16:13:00Z · ended_at=2026-10-11T16:31:44Z · duration_seconds=1124

## Verification report — 2026-10-11T1307Z-audit (iteration 2, slice s3)

Scope: 19 entries, 252 ledger claims, every claim answered (240 ok, 7 F3, 3 F4, 2 F5; see verification.iter2.s3.claims.yaml). Every cited page was fetched or read from the quote-bodies cache this iteration. Axios (direct 403, trafilatura/jina block) was read through a Wayback copy; the CloudSEK victim chart (an image) was read directly.

### Prior-iteration deltas (iteration 1 findings for this slice)

- MuddyWater F4 (government/defence victim wording): Applied; holds. Correction and record now say Rapid7 describes no government or defence victim in this intrusion (Rapid7 gives no victim sector).
- MuddyWater F4 (T1041 to T1105): Applied, but the remediation introduced a defect: Rapid7's own ATT&CK table lists 'T1041 Exfiltration Over C2 Channel', so 'no exfiltration channel being named' in the record summary is contradicted (finding 1).
- SEPPmail F3 InfoGuard scores: Applied; holds. 'the scores are NCSC-CH's' cited to NCSC-CH 12551 (scores match).
- SEPPmail F3 Censys/DACH split: Applied; holds. Two InfoGuard statements stated separately.
- SEPPmail F3 CVSS version / GINA v2 scope: Partly holds. Title, summary and body no longer name the CVSS version and the GINA v2 sentence is scoped to the 15.0.4 notes; but frontmatter cves[].cvss still reads '(CVSS 4.0)' (true per cve.org, uncited) and the 2026-05-20 section still cites InfoGuard for '(CVSS 4.0 10.0)' (finding 8).
- SEPPmail F4 Aargau: Applied; holds ('canton of Aargau' gone; Neuenhof confirmed on the contact page).
- SEPPmail F8 GINA v2 activation: Applied; the Exposure line carries it, but without an inline citation (finding 5).
- Daemon Tools F14 (dozen machines): Applied; holds in headline, summary, section and record (Securelist: 'a dozen machines').
- Daemon Tools F11 (The Record date, earliest signal): The Record is now dated 2026-05-06 (confirmed, datePublished 2026-05-06T16:52Z). The rest of the finding (startup cmd.exe claim, 'earliest signal', C2 beacon step) was not remediated and not declined (finding 10).
- G7 F16 priority: Priority is routine and a section was added, but the main analysis and takeaway still give present-tense pre-event advice ('now', 'before the event window'), contradicting the section (finding 12).
- Week 23 F7 (declined): Rationale does not hold as stated: the 2026-09-30 audit rewrote title, summary and body, so the entry is not 'untouched'. The underlying judgement is defensible (home-region NCSC-CH weekly review), so it is a low-confidence finding (finding 14).
- SimpleHelp F3 (Blackpoint citation): Applied; holds. Detection sentence cited to Blackpoint, which carries the exact text; Blackpoint added to sources.
- SimpleHelp F8 (mechanism): Applied; holds. CCB Belgium's unsigned-token sentence is present and verbatim-supported.
- TeamCity F8 (declined): Rationale does not hold: this fire already records a correction with fields [verification, body] on the entry, so a takeaway could be folded in without a further record (finding 15).
- Chrome V8 F4: Applied; holds. Body reverted, Detection is internally consistent ('operator-specified'... 'configurable'), record is an internal improvement mapping T1068/T1055/T1105, all supported by Proofpoint.
- SAP F3 (kernel list): Applied; holds. Correction text and cves[] follow CERT-EU (7.22 both kernels, 7.53 and 8.04 unicode).
- Cisco ISE F11 (duplicated clause): Applied; holds. The body now reads 'it is aware of active exploitation' once.
- Gentlemen F4 (detection re-based): Applied; holds. Takeaway and Triage describe victim-visible access and state the commands ran on the operator's server. One residual summary overstatement (finding 17).
- Entra F11 (em dashes, declined): Rationale holds. prompts/cti-run.md states the site strips em dashes and the gate (check_run.py reader-text-internals) flags them on updated entries only in new changelog sections; F11 is advisory.
- ShinyHunters F3 (BleepingComputer recap): Applied; holds. Update 2026-09-27 and the new correction attribute the non-confirmation to BleepingComputer's recap of the FBI's first response; the BC 2026-09-26 page says exactly that.
- Switzerland motion F4 (evidence quote): Applied; holds. Quote is now the status-name field. Note: the server returns the escaped form (\u00dc); the quote is the JSON-decoded value and check_run's quote-literal normalises \u escapes, so I accept it.
- Storm-3168 F3 ('no prior operational history'): Applied; holds. The clause now sits outside the citation as 'each principal's normal call pattern'.

### Citation does not support the claim

**#3** `2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag` (body Detection: 'followed within the session by a new MFA device registration for the same user')
- (low confidence) Rapid7 says the TA instructed users during the Teams chats to modify MFA to include attacker-controlled devices, but does not state the registration occurs within the screen-sharing session.
- Source: Rapid7: 'The TA explicitly instructed victims to enter credentials into locally created text files ... and to modify MFA configurations to include attacker-controlled devices.' <https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/>
- Fix: Drop 'within the session' or say 'during or soon after the chat' as the entry's own discriminator, outside the citation.

**#8** `2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3` (section Update 2026-05-20T05:00:12Z: 'CVE-2026-2743 (CVSS 4.0 10.0) is a pre-authentication path traversal ... ([InfoGuard Labs, 2026-05-18])')
- (low confidence; older section, outside the ledger) The cited InfoGuard page carries no CVSS score or version (the 10.0 is on The Hacker News, the 4.0 only in the cve.org record). The iteration-1 remediation dropped the CVSS version from title, summary and body but left it here and in every cves[].cvss.
- Source: InfoGuard page contains no 'CVSS' string; THN: 'CVE-2026-2743 (CVSS score: 10.0)'; cve.org record: version 4.0, baseScore 10. <https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html>
- Fix: Cite THN for 10.0 and drop 'CVSS 4.0' from the sentence, or cite the cve.org record for the version.

**#10** `2026-05-09/daemon-tools-lite-supply-chain-quic-rat-deployed-via-signed` (body paragraph 1 and **Detection:** 'At startup the trojanised binaries run `cmd.exe`, which runs PowerShell to download an executable ...' and 'is the earliest signal')
- (low confidence) Securelist says the binaries at startup run a backdoor thread that sends GET requests to a typosquatted C2 domain; cmd.exe and PowerShell run only when the server returns a shell command. The iteration-1 finding (F11) raised this together with the date; the remediation corrected only The Record date. The earliest observable signal is the beacon, not the cmd.exe chain.
- Source: Securelist: 'Whenever one of these binaries is launched, which happens at startup, a backdoor gets activated ... used to send GET requests to the following URL ... In response to the requests sent, the server may return a shell command to be executed through the cmd.exe process.' <https://securelist.com/tr/daemon-tools-backdoor/119654/>
- Fix: Reword: at startup the binaries beacon to a typosquatted lookalike of the vendor's download domain with the computer name; on a server reply they run cmd.exe/PowerShell; add network telemetry (DNS/HTTP to the typosquat) as the earliest signal and drop 'earliest signal' from the process chain.

**#13** `2026-06-03/ncsc-switzerland-warns-of-cyber-operations-around-the-g7-via` (section Correction 2026-10-11T14:02:54Z: 'The G7 summit in Évian took place from 15 to 17 June 2026 ([NCSC Switzerland, 2026-06-01])')
- (low confidence) The cited page is a pre-event advisory (dateline 2026-06-01) that says the summit 'will take place from 15 to 17 June 2026'; it supports the dates but cannot state that the summit took place.
- Source: NCSC: 'the G7 summit, organised by France, which will take place from 15 to 17 June 2026 in Évian' <https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en>
- Fix: Phrase as 'was scheduled for 15 to 17 June 2026' or cite a post-event report.

**#18** `2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass` (section Correction 2026-10-11T14:08:41Z: '... so a default installation is not exposed without user action.')
- (low confidence) The conclusion is carried by the citation to The Hacker News, but THN exempts default-marketplace users only from 'the branch-name version of the attack' and states 'it is not established that installing a Gemini CLI plugin from GitHub avoids the flaw'; the sentence generalises to all four agents, and the second sentence of the section then says Gemini CLI has a distinct variant, so the section leaves the reader with a blanket 'default installation is not exposed'.
- Source: THN: 'So a reader who installs plugins only from the agents' default, GitHub-based marketplaces is not exposed to the branch-name version of the attack'; 'So it is not established that installing a Gemini CLI plugin from GitHub avoids the flaw'. <https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html>
- Fix: Scope to 'to the branch-name variant' and add that Gemini CLI's variant is not established as blocked on default installs.

**#20** `2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal` (body paragraph 2 and Triage: 'five distinct OAuth tokens were issued' / 'multiple overlapping OAuth tokens')
- (low confidence) The Microsoft post says 'five unique tokens issued for the service principal' and never says OAuth; iteration 1 raised this as a minor point and it was not remediated.
- Source: Microsoft: 'We observed five unique tokens issued for the service principal used for destruction and credential collection – four tokens supported deletion, while the fifth token handled storage inventory and key retrieval.' <https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/>
- Fix: Say 'five unique tokens' (or 'access tokens').

### Unsupported / hallucinated facts

**#1** `2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag` (record summary 2026-10-11T14:21:21Z ('no exfiltration channel being named'); frontmatter techniques[] (T1041 dropped))
- (low confidence) The record summary says T1041 was dropped because 'no exfiltration channel [is] named', but Rapid7's own ATT&CK table lists T1041 for this intrusion, so the source does name the mapping.
- Source: Rapid7 MITRE ATT&CK table: 'T1041 | Exfiltration Over C2 Channel | Data exfiltration to external infrastructure'. Prose: 'the TA exfiltrated data from the compromised environment'. <https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/>
- Fix: Either restore T1041 in techniques[] (source-stated) or reword the record summary to 'Rapid7's prose names no exfiltration channel'.

**#2** `2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag` (section Correction 2026-10-11T14:21:21Z: 'no certificate was stolen or forged')
- (low confidence) Absence stated as fact. Rapid7 says the code-signing certificate 'used to validate the malware samples' is a known MuddyWater resource and was 'revoked shortly after deployment'; it does not say whether the certificate was stolen, forged or fraudulently obtained.
- Source: Rapid7: 'The "Donald Gay" certificate is a known shared resource within MuddyWater's toolkit.' (no statement on theft or forging) <https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/>
- Fix: Reword to 'Rapid7 describes no certificate theft or forging; the code-signing certificate is attribution evidence'.

**#17** `2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft` (frontmatter summary: 'attempts to exploit a public-facing GLPI SQL injection and attempts Zerologon/MS17-010 for lateral movement')
- (low confidence) The correction hedged the body to Talos's 'traces suggesting exploitation', but the summary still states Zerologon/MS17-010 as attempts and as lateral-movement steps; Talos places the traces in Phase 4 (expanding into the internal network and AD), and lateral movement is Phase 5 (NetExec/Impacket authentication attempts).
- Source: Talos Phase 4: 'We also observed traces suggesting the exploitation of CVE-2020-1472 (Zerologon) and the vulnerabilities associated with MS17-010.' <https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/>
- Fix: Reword to 'with traces suggesting Zerologon and MS17-010 exploitation' and keep lateral movement for the NetExec/Impacket authentication attempts.

**#21** `2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal` (frontmatter techniques[] includes T1190)
- (low confidence) T1190 (Exploit Public-Facing Application) is not tied to this intrusion by the cited source: Microsoft says initial access is unclear and, of the App Service probing, 'we found no App Service to ARM credential path for the impacted tenant'.
- Source: Microsoft 'Application Probing': 'the App Service targets did not overlap with the affected Azure subscriptions, and we found no App Service to ARM credential path for the impacted tenant.' <https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/>
- Fix: Drop T1190 or map the exposed-secret route as a possible T1552.004/T1078.004 path only.

### Claims missing inline citation

**#5** `2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3` (body **Exposure:** 'GINA v2 has to be explicitly activated in the system settings, which is how to tell whether its flaws apply.')
- (low confidence) The sentence carries no inline citation; the source is InfoGuard, which is cited only on the next sentence (Censys count).
- Source: InfoGuard: 'The updated GINA v2.x, available since approximately January 2025, fortunately requires explicit activation in the system settings.' <https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/>
- Fix: Add the InfoGuard citation to the activation clause.

**#16** `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce` (main analysis paragraph 2: 'A TeamCity server holds the credentials its pipelines deploy with, the signing material its artifacts are stamped with, and write access to the outputs every downstream consumer trusts ...')
- (low confidence) Uncited factual characterisation; JetBrains states the server can expose 'TeamCity data, configurations, and stored credentials' and compromise 'the integrity of build artifacts and downstream CI/CD pipelines' but does not mention signing material.
- Source: JetBrains advisory 'Technical details': 'a successful attack could expose TeamCity data, configurations, and stored credentials, modify server state, and potentially compromise the integrity of build artifacts and downstream CI/CD pipelines.' <https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/>
- Fix: Cite JetBrains for stored credentials and artifact integrity and drop 'signing material' or mark it as analyst inference.

**#19** `2026-09-24/microsoft-entra-id-sspr-enumeration-resetspy` (body **Detection:** paragraph (the Detection sentence 'Entra ID / Azure AD self-service-password-reset audit events are the telemetry class ...'))
- The correction record says 'the detection, triage and takeaway lines gain their LevelBlue citation', but the Detection sentence ends with no citation; the single LevelBlue link in that paragraph terminates the Triage sentence. LevelBlue does carry the substance (Entra Audit Logs, status failures for 'user is not member of the password reset users group', bulk requests with no completed reset).
- Source: LevelBlue: 'Monitoring Entra Audit Logs for status failures with "user is not member of the password reset users group" can identify enumeration or malicious activity.' <https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal>
- Fix: Add the LevelBlue citation at the end of the Detection sentence.

### Drop (low relevance / off-audience / duplicate)

**#14** `2026-06-10/ncsc-ch-week-23-coordinated-surge-in-job-seeker-targeting-fa` (whole entry (priority notable, four paragraphs); iteration-1 finding declined)
- (low confidence) The decline rationale ('operator-level length judgement on an earlier fire's notable entry the audit did not touch beyond relabelling') does not hold as stated: the 2026-09-30 audit rewrote title, summary and body of this entry, so it is not untouched, and the sound-throughout rule applies to every entry in the brief. Substance of the original finding stands: two of the three cases (calendar-invite credential phishing, reshipping identity theft) are consumer fraud with no SOC-actionable telemetry, and only the LinkedIn-to-GitHub infostealer case has a transferable behaviour. The Swiss national-CERT source and home-region nexus make the entry defensible, so this is a judgement call.
- Source: NCSC-CH week 23: 'Using three reported cases, the NCSC demonstrates how these scams work'; only the third case describes a malware chain. <https://www.bacs.admin.ch/en/26w23-en>
- Fix: Keep the decline with a rationale that matches the record (home-region nexus, NCSC-CH weekly review), or shorten the first two cases to a clause.

### Needs more research

**#7** `2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3` (main analysis: no **Detection:** line)
- The analysis has Exposure and Defender takeaway but no Detection line although InfoGuard describes observable behaviour for exploitation: POST to /v1/file.app with traversal in the file field writing /etc/syslog.conf, a syslogd pipe entry spawning a Perl shell after the 15-minute newsyslog reload, and unauthenticated calls to /api.app/template, /api.app/hello?op=env and attachment/preview. The earlier text carried 'monitor /v1/file.app POST requests with ../ sequences; alert on unexpected Perl process trees spawned by syslogd' and the rewrite dropped it. The PoC request is public in the same write-up and the entry does not say so.
- Source: InfoGuard: 'the application extracts a file parameter directly from the user-supplied JSON payload'; 'newsyslog ... runs every 15 minutes via cron ... automatically sends a SIGHUP to syslogd'; section 'Full PoC Request'. <https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/>
- Fix: Add a Detection line (web access logs for /v1/file.app and /api.app/* requests from the internet, changes to /etc/syslog.conf, unexpected child processes of syslogd, post-patch compromise check) and state that InfoGuard published PoC detail.

**#15** `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce` (main analysis: no **Defender takeaway:** line; iteration-1 finding declined)
- (low confidence) The decline rationale ('the 2026-09-30 update carries the current takeaway; folding the takeaways is left to the next record on the entry') does not hold: this fire already records a correction with fields [verification, body] on this entry, so the main analysis was being edited anyway and no extra record is needed. The contract requires a Defender takeaway on every entry; the main analysis closes with Exposure, Detection and Triage only, and the takeaways sit in two separate update sections (2026-08-06 and 2026-09-30).
- Source: Entry text: main analysis ends after **Triage:** ...; '**Defender takeaway:**' appears only inside '## Update — 2026-08-06T04:11:48Z' and '## Update — 2026-09-30T06:52:00Z'. <https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/>
- Fix: Add one current Defender takeaway to the main analysis (patch plus compromise assessment, because ransomware use is recorded) and drop or merge the two section copies.

### Surface contradiction

**#6** `2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3` (body: 'CVE-2026-44126 (9.2), an insecure deserialization, was fixed in 15.0.3' and cves[].fixed/affected for CVE-2026-44126)
- (low confidence) The per-CVE record (NCSC.ch as CNA) lists CVE-2026-44126 as affecting versions 'before version 15.0.4' while InfoGuard's table and The Hacker News place the fix in 15.0.3 and the SEPPmail 15.0.3 notes do not name CVE-2026-44126; the entry states 15.0.3 flatly and carries a Contradiction line only for CVE-2026-2743.
- Source: cveawg.mitre.org CVE-2026-44126: 'SEPPmail Secure Email Gateway before version 15.0.4 insecurely deserializes untrusted data ... may allow unauthenticated remote attackers to execute code'; affected lessThan 15.0.4. InfoGuard table: '15.0.3 | CVE-2026-44126: Insecure deserialization'. <https://cveawg.mitre.org/api/cve/CVE-2026-44126>
- Fix: Add a Contradiction line for CVE-2026-44126 (InfoGuard/THN 15.0.3 vs CVE record 15.0.4) or state the fix as 'by 15.0.4'.

**#12** `2026-06-03/ncsc-switzerland-warns-of-cyber-operations-around-the-g7-via` (main analysis **Defender takeaway:** 'should pre-stage DDoS mitigation playbooks now, review MFA ..., rotate administrative credentials before the event window ... hunt for anomalous authentication spikes from the summit region around 15–17 June' versus Correction 2026-10-11T14:02:54Z 'the pre-event preparations this warning recommended have lapsed')
- Supersession (check 4c(h)): the iteration-1 remediation set priority routine and added the section, but the main analysis and its takeaway still instruct the reader in the present tense ('now', 'before the event window') about a summit that ended four months ago; the entry contradicts its own newest section. summary also still reads as a live pre-event warning.
- Source: NCSC advisory (2026-06-01): 'will take place from 15 to 17 June 2026 in Évian'; entry's own Correction 2026-10-11: 'the pre-event preparations this warning recommended have lapsed'. <https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en>
- Fix: Rewrite the takeaway in the past tense or replace it with the transferable lesson (event-driven DDoS planning), and re-word summary/body to a record of the warning; declare 'body' in the record fields.

### Editorial / less-is-more flags (advisory)

**#4** `2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag` (body paragraph 1: '(`ms_upd.exe`) ... (`Game.exe`)')
- (low confidence) Check 12: file-name indicators of the attacker tooling in reader-facing text (policy: no file-name indicators).
- Fix: Describe as 'a downloader' and 'the Darkcomp backdoor' without file names.

**#9** `2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3` (title: 'five more flaws (CVE-2026-44128 et al., CVSS up to 9.3)')
- (low confidence) Title/headline cover the NCSC six only while cves[] carries CVE-2026-2743 at 10.0, so 'CVSS up to 9.3' understates the entry's own top score.
- Source: cves[] CVE-2026-2743 cvss 10.0; summary 'InfoGuard's write-up adds the LFT path traversal CVE-2026-2743 (10.0)' <>
- Fix: Say 'six flaws in NCSC-CH's advisory' or drop the score ceiling from the title.

**#11** `2026-05-09/daemon-tools-lite-supply-chain-quic-rat-deployed-via-signed` (body paragraph 1: file names `envchk.exe`, `DTHelper.exe` etc.)
- (low confidence) Check 12: file-name indicators of attacker tooling (`envchk.exe`) in reader-facing text.
- Fix: Describe the .NET information collector without its file name, or accept as detection-relevant.

### Verdict

NEEDS_FIXES (truth: 10, editorial: 8, advisory: 3). Every truth finding carries a quoted source passage; most are marked (low confidence). The most consequential: #10 (Daemon Tools startup cmd.exe/earliest-signal misstatement left unremediated), #12 (G7 stale pre-event advice contradicting the new section), #7 (SEPPmail Detection line dropped by the rewrite though InfoGuard's observable chain supports it), #17 (Gentlemen summary firmer than Talos on Zerologon/MS17-010), #1 (MuddyWater T1041 removal contradicted by Rapid7's table).

Coverage: no new missed-angle findings from this slice (its entries are one-entry-per-finding rewrites; dedup is not in question). The Detection gap in SEPPmail and the stale G7 advice are the substantive items.

### Findings summary (machine-readable)

See verification.iter2.s3.findings.yaml (21 records).
