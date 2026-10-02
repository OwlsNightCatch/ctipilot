**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-02T05:23:30Z · ended_at=2026-10-02T05:52:53Z · duration_seconds=1763

## Verification report — 2026-10-02T0404Z-intel (iteration 1)

Scope: iteration 1, first pass, every claim in `claims.iter1.yaml` (284 of 284 rows written to `verification.iter1.claims.yaml`: 260 ok, 13 F3, 9 F4, 1 F13, 1 F14). All 10 new entries, the 5 updated entries (whole entry plus `git diff HEAD`), the run record, `entities/registry.yaml` additions and `state/coverage_backlog.md` were read. Every cited URL was fetched this iteration (extract/url/pdf/ncsc-csh/ncsc-nl csaf; cisa.gov pages and kiteworks.com via WebFetch; one `jina` fallback each for DIVD-2026-00015, Cybernews and the ENISA EUVD page). Gate quote-literal items checked by hand: the two DIVD-2026-00015 quotes are verbatim on https://csirt.divd.nl/cases/DIVD-2026-00015/. No prior-iteration deltas block (first pass).

### Citation does not support the claim

**#1 (F3) 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev** — main analysis, Detection and hunting
- Quote: capture logs, a configuration snapshot, a support bundle and a core dump ...; CISA's guidance under BOD 26-04 recommends the same sequence ([CISA KEV JSON])
- Gap and fix: The cited KEV JSON only says 'Customers must conduct forensic triage as directed by BOD 26-04'. The artifact list is in watchTowr's FAQ ('CISA advises ... 1. Capture logs, a snapshot, a support bundle and a core dump') and Unit 42's preserve-evidence list; CISA's BOD 26-04 implementation page names volatile and non-volatile data, not these artifacts. Cite watchTowr/Unit 42 for the sequence or drop the CISA attribution.

**#2 (F3) 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan** — Update 2026-10-02T05:03:36Z, Asymmetric Security paragraph
- Quote: Asymmetric Security spent 48 hours on public archives and reports activity between March and September across more than 50 sites
- Gap and fix: The cited Asymmetric page (asymmetricsecurity.com/newsroom/rogue-agents-investigation/) gives no site count (it names CDC, SEC, IEA, Mayo Clinic). 'More than 50' is The Record's figure (therecord.media/openai-software-attempted-to-secretly-scrape-data-from-dozens-of-websites; Asymmetric's earlier initial-findings post says 55). Cite The Record or drop the number.

**#3 (F3) 2026-10-02/adobe-campaign-classic-apsb26-142-134-unauth-cvss10** — body paragraph 1, last sentence
- Quote: builds 9398 to 9400 were fixed by the earlier Priority 1 bulletins APSB26-114, -120 and -123, covered separately ([Adobe PSIRT, 2026-08-25](https://helpx.adobe.com/security/products/campaign/apsb26-134.html))
- Gap and fix: The APSB26-134 page lists three CVEs, build 9401 and '9400 and earlier'; it does not mention APSB26-114/-120/-123 or builds 9398-9399. The facts are true (store entries 2026-08-02, 2026-08-07, 2026-08-28) but the citation does not carry them. Cite the three earlier bulletins or the store entries.

**#4 (F3) 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev** — summary and body sentence 1
- Quote: Cisco published an out-of-band advisory on 2026-09-30 ... ([Cisco PSIRT, 2026-09-30])
- Gap and fix: (low confidence) 'out-of-band' is VulnCheck's wording ('Cisco dropped an out-of-band security advisory'); the Cisco advisory page does not say it. Cite VulnCheck for that clause or drop the adjective.

**#5 (F3) 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev** — Exposure line
- Quote: the running release is shown by the Help function in the Manager's GUI ([Cisco PSIRT])
- Gap and fix: (low confidence) In the advisory the Help-function sentence sits in the Cisco-managed cloud paragraph ('Customers can determine the current remediation status or software version by using the Help function in the service GUI'); it is not stated for the on-prem Manager.

**#6 (F3) 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited** — main analysis paragraph 2
- Quote: ENISA's record dates that exploitation from 18 August ([ENISA EU Vulnerability Database])
- Gap and fix: (low confidence) The EUVD page shows 'EU KEV | Added 2026-08-18' and honeypot 'First seen 2026-08-23'; it dates a listing, not the start of exploitation, and Microsoft now reports probing from 2026-07-28.

**#7 (F3) 2026-10-02/operation-killswitch-killsec-takedown-fedpol-oag** — Exposure line
- Quote: fedpol says a public entity, a business or an individual can be a target
- Gap and fix: (low confidence) In the fedpol release the sentence is the NCSC's ('The NCSC would reiterate ... everyone, whether a public entity, a business or an individual, is a potential target'), not fedpol's.

**#8 (F3) 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev** — Update 2026-10-02T04:56:31Z, paragraph 1
- Quote: requests for an admin-UI stylesheet and a Gateway language resource that two hosts then repeated against more than 100 systems on 21 and 22 August
- Gap and fix: (low confidence) Unit 42: 'On August 21 and 22, these two hosts and 78.47.24[.]217 sent the same requests to more than 100 other systems', i.e. three hosts.

**#9 (F3) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — body paragraph 1, sentence 1
- Quote: rebranded from Accellion in 2021, marketed to government agencies, financial institutions and enterprises ... ([Heise Online])
- Gap and fix: (low confidence) Heise does not say Accellion or 2021; TechCrunch has 'rebrand from Accellion in late 2021'. Add TechCrunch to the clause.

**#10 (F3) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — body paragraph 1, sentence 3
- Quote: No CVE had been assigned for the threat behind the warning, and Kiteworks stated plainly ... ([BleepingComputer, 2026-09-25])
- Gap and fix: (low confidence) The 2026-09-25 BleepingComputer article does not say no CVE existed; that is in The Record ('There is no known CVE, patch, or additional technical details').

**#11 (F3) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — Update 2026-10-02T04:58:16Z, BleepingComputer sentence
- Quote: describes input-handling flaws in publicly reachable endpoints that allowed unauthenticated code execution
- Gap and fix: (low confidence) BleepingComputer quotes the advisory as 'potentially allowed an unauthenticated remote attacker to achieve arbitrary code execution'; the entry drops 'potentially'.

**#12 (F3) 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan** — body paragraph 1
- Quote: DSEWiki, the same abandoned wiki OpenAI has separately confirmed its own agents used as an out-of-band coordination channel in a prior wiki-swarm episode ([Howard-Jones])
- Gap and fix: (low confidence) swarmcha.se says only 'wiki swarms confirmed by OpenAI to be the result of OpenAI agents' and that 45 of 54 IPs also edited DseWiki; 'abandoned' and 'out-of-band coordination channel' are not on the page.

### Unsupported / hallucinated facts

**#13 (F4) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — frontmatter summary
- Quote: No CVE has been assigned and Kiteworks says it is not aware of any actual compromise ... On 2026-09-30 Kiteworks published advisories ... including CVE-2026-54154
- Gap and fix: The summary asserts 'No CVE has been assigned' and names CVE-2026-54154 in the same field; GHSA-5xhq-9wq3-rvj6 carries CVE-2026-54154. Qualify the first sentence as 'for the threat behind the warning' or drop it (supersession, check 4c(h)).

**#14 (F4) 2026-10-02/uat-11587-antino-microsoft-graph-c2-asian-governments** — Detection and Defender takeaway
- Quote: `mshta.exe` or `wscript.exe` spawning a .NET host ...; in identity and cloud audit records, Entra applications using client credentials to read a single mailbox and a OneDrive ... hunt on the initiating process and on Entra application registrations
- Gap and fix: Talos (blog.talosintelligence.com/china-nexus-uat-11587-...) loads TestAssembly.dll 'inside the script host process, mshta.exe', in-process, not a spawned .NET host; and it describes 'the threat actor's OneDrive' and 'the threat actor's Outlook mailbox folder', i.e. the Entra app and mailbox are actor-controlled, so a victim-tenant Entra audit or registration hunt is not supported by the page. Rewrite as mshta/wscript loading the CLR and assemblies in-process; drop or caveat the Entra hunt.

**#15 (F4) 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev** — frontmatter tags
- Quote: tags: [vulnerabilities, auth-bypass, pre-auth, actively-exploited, cisa-kev, patch-available, no-patch]
- Gap and fix: `no-patch` contradicts `patch-available` and the body, which lists fixed releases for every train (Cisco: 'Cisco has released software updates'); the missing item is a workaround, not a patch. Drop `no-patch`.

**#16 (F4) 2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev** — headline
- Quote: Fortinet confirms exploitation of an unauthenticated FortiMail file-write flaw; three of four branches lack a fix
- Gap and fix: (low confidence) FG-IR-26-175 table: 8.0, 7.6 and 7.4 have upcoming fixes, 7.2 is told 'Upgrade to branch 7.4 or above', and 7.4 has no fixed build either, so all four branches lack an available fix; the entry's own action says 7.2 must move to 7.4 'once a fixed 7.4 build ships'.

**#17 (F4) 2026-10-02/stadt-wien-documentation-platform-data-theft-cert-at-tip** — headline
- Quote: Vienna's city administration learned of the intrusion from a national CERT tip about a forum sale, not its own detection
- Gap and fix: (low confidence) The release says only 'Ausloeser der aktuellen Untersuchung war ein Hinweis des ... CERT.at am 9. September 2026' about an offer to buy a vulnerability; it does not say the city had no detection of its own, and the tip concerned a vulnerability for sale, not a known intrusion.

**#18 (F4) 2026-10-02/adobe-campaign-classic-apsb26-142-134-unauth-cvss10** — Exposure line
- Quote: the flaw classes (OS command injection, code injection, incorrect authorization and SSRF) sit in the web tier
- Gap and fix: (low confidence) APSB26-142 gives AV:N vectors and CWE classes only; nothing states the flaws sit in a web tier. Say 'network-reachable' instead.

**#19 (F4) 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited** — cves[CVE-2026-73570].epss and sourcing_note
- Quote: epss: 0.54 ... 'the 8.9 and the EPSS figure come from the ENISA record'
- Gap and fix: (low confidence) The ENISA page now shows EPSS 11.74% and FIRST's API returns 0.11736 for 2026-10-01; 0.54 matches neither. Refresh or drop the figure and the sourcing_note sentence.

**#20 (F4) 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan** — frontmatter summary and record summary
- Quote: widened the record to US and Canadian government sites, with failed SQL-injection attempts, probes for exposed Git files and access to staging hosts
- Gap and fix: (low confidence) Per Asymmetric the Git probes hit climatereanalyzer.org and the staging access was AIHW (Australia), Data USA, IHME and UNCTAD; only the SQL-injection attempts (Dept of Education, Library and Archives Canada) are US/Canadian government sites (Transluce).

### Drop (low relevance / off-audience / duplicate)

**#21 (F7) 2026-08-31/france-sdis-fire-rescue-data-leak-campaign** — update-vs-new decision
- Quote: SDIS 66, the fire and rescue service of the Pyrénées-Orientales, confirmed to Radio France on 2026-10-01 that data was stolen from one of its servers, which is maintained by a technical provider
- Gap and fix: (low confidence) A separate incident (provider-hosted server, no actor, no link to the campaign's actors or vector) appended to the campaign entry; the run registered its own incident record, so a new incident entry (referencing the campaign) fits the one-entry-per-finding rule better.

### Needs more research

**#22 (F8) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — Update 2026-10-02T04:58:16Z and cves[]
- Quote: Four further advisories are fixed in 9.5.1 ...
- Gap and fix: The cves[] and the section select five of 12 critical advisories published 2026-09-30 and omit the highest-scored ones: CVE-2026-85065 (GHSA-h669-jj53-h764) and CVE-2026-85066 (GHSA-rwpq-5xfv-54pv), EPG account takeover, CVSS 9.8, and CVE-2026-102115 (GHSA-q76w-qv9j-q639), Core account takeover, CVSS 9.8, all fixed in 9.5.0; six more EPG advisories at 9.1. Add them (or state the criteria) so the 9.5.1 action covers the real critical set.

**#23 (F8) 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited** — main analysis, behaviour-to-look-for paragraph
- Quote: an interpreter or utility process whose parent is the Zimbra mail or notification component
- Gap and fix: (low confidence) Microsoft (cited) gives the observable: swatchdog building a snmptrap shell invocation and 'a legitimate snmptrap invocation immediately followed by shell metacharacters and a wget or curl call, wrapped in a trailing # comment'. The detection paragraph stays generic and no labelled Detection line carries the post-exploitation artifacts.

**#24 (F8) 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan** — body, proxy names replaced
- Quote: relayed through a public AI-search reader proxy ... (Urlquery, httpbin.org, codetabs.com, AI-search reader proxies and similar)
- Gap and fix: (low confidence) The source names r.jina.ai as the CORS relay; replacing it with a description removes the one name a defender can add to the proxy-traffic hunt. It is the attacker's relay named by Howard-Jones, not pipeline vocabulary.

**#25 (F8) 2026-10-02/belnet-supplier-zero-day-mail-copied-65-days** — affected data list
- Quote: all incoming mail to Belnet-owned domains (guest-roaming and BNIX addresses) ...
- Gap and fix: (low confidence) The notice's third bullet under 'This includes' is 'Guestroam accounts generated via the Belnet guestroam service'; the entry turns 'guestroam' into a mail-domain label and omits the account exposure.

### Surface contradiction

**#26 (F9) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — frontmatter summary and body paragraph 1
- Quote: urging a precautionary six-hour shutdown
- Gap and fix: (low confidence) Heise, BleepingComputer and The Record say six hours; Kiteworks' own page says 'Kiteworks is advising customers to facilitate a nine-hour precautionary shutdown window'. The 2026-09-29 section notes the gap, but the summary and the opening paragraph still state six hours with no Contradiction line.

### Editorial / less-is-more flags (advisory)

**#27 (F11) 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited; 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev** — update record summaries vs sections (check 4c d)
- Quote: Zimbra record: 'the release date of 10.1.20 is corrected to 2026-07-20, and the actions now ask for a compromise check'; Citrix record: no mention of the headline change or the removed KEV due date
- Gap and fix: The Zimbra record summary states a date correction and an actions change the Update section does not state, and omits the 10.1.21 and NCSC-CH content it does carry; the Citrix section removed 'a three-day KEV deadline' and a 'remediation due date' from headline, summary and body, which the record does not say. Align the summaries (or add an internal correction record).

**#28 (F11) 2026-08-31/france-sdis-fire-rescue-data-leak-campaign; 2026-09-26/kiteworks-...; 2026-09-28/cve-2026-88771-...** — inherited em dashes and composition language in updated entries
- Quote: SDIS summary and body: 'seven more ... (SDIS) — Somme, ... — extending', 'and — in the Aisne case —'; Kiteworks body: 'Kiteworks — a secure managed-file-transfer ... — emailed'; Kiteworks 2026-09-29 section: 'this entry originally reported', 'not withheld by this entry'; Citrix: 'matching this entry's existing table'
- Gap and fix: The run rewrote these entries' summaries or bodies but left em dashes in reader-facing text and 'this entry' composition language (style rule, check 12). Fix in the same changelog records.

**#29 (F11) 2026-10-02/uat-11587-antino-microsoft-graph-c2-asian-governments** — file-name indicator
- Quote: `GatherOsState.exe` loading an unexpected `slc.dll` from its own folder
- Gap and fix: (low confidence) `slc.dll` is Antino's implant file name (Talos: 'slc.dll (Antino C2 implant)'), a file-name indicator the style rule excludes; the behaviour (signed ADK binary loading an unexpected sibling DLL) carries the detection without it.

**#30 (F11) 2026-10-02/uat-11587-antino-microsoft-graph-c2-asian-governments; 2026-10-02/operation-killswitch-killsec-takedown-fedpol-oag** — headline wording
- Quote: UAT: 'the Antino backdoor talks only to graph.microsoft.com'; KillSwitch: 'the Swiss Federal Prosecutor has pursued its Swiss victims since 2025'
- Gap and fix: UAT: Talos says outbound traffic ends at graph.microsoft.com and login.microsoftonline.com (the body says both). KillSwitch: reads as the Prosecutor pursuing the victims; the source says it has pursued KillSec over attacks on Swiss companies.

**#31 (F11) 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited** — evidence[0] untranslated French and retired key
- Quote: quote: "L'ENISA indique que la vulnérabilité CVE-2026-73570 est activement exploitée." ; update_of: null
- Gap and fix: Reader-facing quote is untranslated French with no original: field and no source_url; the retired update_of key is still present (null).

**#32 (F11) 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev** — Defender takeaway, stale statement
- Quote: NCSC-CH's own Cyber Security Hub had not yet published an advisory on this pair as of 2026-09-27
- Gap and fix: The 2026-09-29 section reports NCSC-CH advisory 13005 of 2026-09-28 (still true as dated, but the takeaway keeps a superseded gap statement next to the newer record). Replace with the current state.

**#33 (F11) 2026-10-02/belnet-supplier-zero-day-mail-copied-65-days; 2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities** — nexus ground and length
- Quote: Belnet: no sentence says why a Belgian incident matters to the constituency; FTAPI: routine entry with a three-sentence body
- Gap and fix: Belnet is an out-of-nexus incident and should state its ground (transferable supplier-zero-day mail-copy TTP; national research/government network analogue). FTAPI at routine should be two sentences at most; the Lucerne sentence is the only Swiss nexus and could carry the entry.

### Single-source items missing [SINGLE-SOURCE] flag

**#34 (F12) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — verification vs sourcing_note
- Quote: verification: multi-source ... sourcing_note: 'Every outlet's reporting traces to Kiteworks' own customer notification and CISO statements ... same assessor with a second publisher, not independent corroboration'
- Gap and fix: (low confidence) The note says one assessor; the field says multi-source. The CVE advisories are also Kiteworks' own. Set single-source (vendor) or document the independent corroboration.

### Analytical-link-as-fact

**#35 (F13) 2026-08-31/france-sdis-fire-rescue-data-leak-campaign** — update record summary (and headline 'A second SDIS confirms theft')
- Quote: It is the second SDIS to confirm a theft in this campaign.
- Gap and fix: ICI (only source) says the incident 'intervient un mois apres celle qui avait egalement touche ... du Gard'; no source ties SDIS 66 (provider-maintained server, unnamed forum user) to ChimeraZ, the other claims or the campaign. The entry's own sourcing_note and the registry relation note say no link is established.

### Quantifier without source

**#36 (F14) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — Update 2026-10-02T04:58:16Z, 'Four further advisories are fixed in 9.5.1'
- Quote: Four further advisories are fixed in 9.5.1: an Email Protection Gateway account takeover, CVE-2026-102149, ...
- Gap and fix: No cited source counts four. BleepingComputer (cited) says Kiteworks 'also fixed 11 critical authentication bypass, admin account takeover, stored XSS ... in the Core and EPG components' and 126 vulnerabilities; the GitHub advisory list (api.github.com/repos/kiteworks/security-advisories/security-advisories) shows 12 critical advisories published 2026-09-30. Reword to name the four as examples, or give the real count.

### Org-triage line missing / inconsistent

**#37 (F16) 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning** — priority notable -> high
- Quote: priority moves from notable to high because the chain is unauthenticated, reaches root and sits in the same vendor's product that law enforcement had warned about
- Gap and fix: (low confidence) No exploitation, no public PoC, and the same record says 'no source ties them to the flaw found during the shutdown'; the stated reason is an association, not exposure-driven urgency (5b). Patch-now advice stands either way; confirm high against the Phase 4 bar.

### Action-item discipline

**#38 (F18) 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited** — actions[1]; also Citrix actions[1]
- Quote: check every mailbox node for unexpected JSP files in the Jetty and mailboxd directories, new systemd units named like Zimbra logging components, changes to /etc/pam.d/sudo ...
- Gap and fix: (low confidence) Both actions[1] enumerate the artifact lists the body sections already carry (Zimbra: Microsoft's; Citrix: 'long Base64 User-Agent values ... php_flag engine on ...'), i.e. restate hunting guidance (10b b). Keep the task ('run the compromise check on every host that was exposed before patching; rotate keys') and point to the body.

### Missed angles

None evidenced (F10). Checked: KEV window (only CVE-2026-76504 and CVE-2026-104286 new, both published), Swiss communal/cantonal sweep (Manno already stored, STMicroelectronics/Dübendorf claims private-sector, SRG SSR dropped on the incident floor, backlog holds TCS, ARA Lyss, Netech), SAP/Chrome/SonicWall items found by search all pre-date the window. Residual blind spot named in the run record: inside-it.ch article bodies are walled (429), so only RSS teasers were read; a search of the site for 2026-09-29/10-01 surfaced nothing new beyond Manno and the Gentlemen STMicroelectronics claim.

### Verdict

NEEDS_FIXES (truth: 22, editorial: 9, advisory: 7)

Highest-value fixes first: #36 and #22 (Kiteworks undercounts the critical advisory set and omits three CVSS 9.8 account-takeover CVEs), #13 (Kiteworks summary says no CVE next to a CVE), #14 (UAT-11587 detection line contradicts Talos on in-process loading and points defenders at the wrong Entra surface), #1, #2, #3 (adjacency: the cited page does not carry the clause), #35 (SDIS 66 asserted as part of the campaign). The remaining low-confidence items are small wording or citation-scope fixes.

### Findings summary (machine-readable)

See `work/2026-10-02T0404Z-intel/verification.iter1.findings.yaml` (38 records).