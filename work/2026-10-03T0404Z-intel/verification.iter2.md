**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-03T05:02:16Z · ended_at=2026-10-03T05:12:46Z · duration_seconds=630

## Verification report — 2026-10-03T0404Z-intel (iteration 2)

Scope: post-fix pass. All four entries were remediated, so every one of the 86 ledger claims is in scope (`verification.iter2.claims.yaml`: 81 ok, 3 F3, 1 F4, 1 F14; `tools/claim_ledger.py --coverage 2`: 86/86 answered, 0 missing). Pages read this iteration: Fortinet FG-IR-26-175 (extract and raw HTML), BleepingComputer FortiMail and Warlock articles, Belnet notice, NCSC-CH hub posts 13027 and 13021 (`ncsc-csh post`), NCSC-NL 0398, CISA alerts of 2026-10-01 and 2026-09-30 (WebFetch), Cisco advisory v1.1, Cisco Live Protect page (extract and raw), VulnCheck, Risky Bulletin, Symantec, Microsoft ToolShell guidance, FIRST EPSS API, pinned ATT&CK v19.2 (all 16 Warlock and 5 FortiMail ids active). All evidence quotes of the four entries were substring-checked against the fetched bodies: 17 of 17 verbatim.

### Prior-iteration deltas, verified
1. FortiMail file table (F3): fixed. The Fortinet page (extract, raw HTML) has no liblog/ld.so.preload/webconsole/mailservice/httpd.conf/migadmin.tar strings and its IoC section lists two IPs, system-event lines and encryption lines. BleepingComputer: "Fortinet also published indicators of compromise (IOCs) ... including several files that were added or modified on compromised systems", then the table. NCSC-CH 13027: "Observed attacks deploy malicious binaries and modified system files (e.g., ld.so.preload, ...)". The new attribution is correct.
2. FortiMail workaround framing (F4): fixed. Page now says "Disable access to the FortiMail webmail interface from the internet or limit the access only from trusted private network" plus the WAF rule and a Timeline with only "2026-10-01: Initial publication". BleepingComputer and NCSC-CH say "management interface". The previous fire's verifier file (`work/2026-10-02T0404Z-intel/verification.iter8.claims.yaml:645`) read "management interface" and a file table on the same page, which matches the run-record's "revised without a timeline entry" note.
3. FortiMail evidence[1]: fixed, verbatim on the page.
4. Cisco Live Protect date: fixed. Raw HTML "Updated: July 1, 2026".
5. Warlock key rotation (F3): PARTIALLY fixed. Exposure line is correct (Microsoft step 6/7 quoted). The Defender takeaway still ends in the Symantec link while carrying "rotate the machine keys if a web shell is found", and the action attributes a web-shell-conditional rotation to Microsoft. See F3 #1. The run-record remediation text ("the takeaway says 'per Microsoft's guidance' via that citation") does not match the entry.
6. Warlock Triage (F4): fixed. Symantec installs the tunnel on Computer 4, a further host.
7. Warlock Symantec links (F5): fixed on both sentences.
8. NCSC-NL contradiction (F9): fixed, stated in Exposure and accurate ("Fortinet heeft beveiligingsupdates uitgebracht" vs "upcoming").
9. KEV citation (F2): fixed, CISA alert page of 2026-10-01 lists "CVE-2026-104286 Fortinet FortiMail Path Traversal Vulnerability".
10. Cisco shield rule (F8): fixed. Live Protect page policy: "Cisco creates Vulnerability Shields for the SD-WAN release that is current when the shield is published and for the two immediately preceding releases in each supported release train that includes Live Protect." The entry's wording matches.
11. FortiMail Update indicators (F11): fixed; no webconsole/mailservice or any other file-name, IP, domain or hash string appears in any of the four entries.
12. Belnet and Cisco Update sections (F11): Belnet section is now delta-only (but see F11 #1 on the record summary); Cisco section unchanged except the rule sentence, which is correct.
13. Warlock T1036.010: fixed, active in the pinned data; Symantec: "The account name is likely an attempt at masquerading."
Warlock cuts: the analysis is 542 words; the diff against iteration 1's ledger shows the only dropped content is the regional-focus sentence (opportunistic vs deliberate tasking) and the "inference, Symantec does not address key replacement" caveat; nothing sourced was distorted. Regions and the Portuguese/Spanish-speaking clause are retained in summary and first paragraph.

### Citation does not support the claim
- F3 #1: Warlock (claims 73df725d6f, 2bbb33f5f6). Takeaway: "...and rotate the machine keys if a web shell is found; in Active Directory domains, watch SYSVOL scripts paths for executables ([Symantec, 2026-10-01])". Symantec text (grep for rotat/replac/restart/IIS/machine key) only says the web shell harvests the keys; no rotation advice. Microsoft (read): "After applying the latest security updates above or enabling AMSI, it is critical that customers rotate SharePoint server ASP.NET machine keys and restart Internet Information Services (IIS) on all SharePoint servers", unconditional. actions[0] says "where a web shell turns up, rotate ... as Microsoft's ToolShell guidance says", which narrows Microsoft's guidance. Cite Microsoft on the takeaway's rotation clause (or move it out of the Symantec-terminated clause) and align the condition or drop the attribution.
- F3 #2 (low confidence): FortiMail summary and Update, "Belnet, the Belgian government and research network, updated its incident notice ... ([Belnet, 2026-10-02])". The Belnet notice does not describe Belnet; Risky Bulletin does ("a government-funded internet provider that caters to the Belgian government, educational institutions, and science and research centres") and is cited only in the Belnet entry. Cite Risky Bulletin or drop the descriptor here.

### Unsupported / hallucinated facts
- F4 #1 (low confidence): Warlock paragraph 2, "The attackers then used DLL sideloading, ..., enumerated domain accounts and trusts, ..." after the 2026-07-28 sentence. Symantec dates the side-loading pairs and `net user /domain` / `nltest /domain_trusts` to July 24, before "The exploitation chain proper began" on July 28. Replace "then" with "also".

### Quantifier without source
- F14 #1 (low confidence): FortiMail summary, "...so the vendor workarounds are the only control." No cited source says "only"; Fortinet lists three workarounds and BleepingComputer says "apply the shared workarounds until a security update can be installed". Reword to "the available mitigation".

### Action-item discipline
- F18 #1: Cisco actions[1], "run the compromise check described in the body and open a Severity 3 Cisco TAC case ...". Not executable without re-reading the entry (10b(c)). Name the log checks or drop it; the immediate_action already carries the TAC step.

### Editorial / less-is-more flags (advisory)
- F11 #1: Belnet `updates[0].summary` states more than the Update section (09-25 remediation, "FortiMail path traversal ... without naming the product", the priority change); the section was cut to the delta, the summary was not.
- F11 #2 (low confidence): FortiMail "a cron job launched from the migration directory" / "admin-migration archive": sources give only "/migadmin" and "migadmin.tar.gz"; "migration" is the entry's expansion.
- F11 #3: FortiMail Update closing sentence "The workaround and exposure statements above follow the current Fortinet text." is composition narration.

### Checked and clean
- FortiMail: CVSS 9.8 and CVE id on the Fortinet page, affected ranges, upcoming fixes, three workarounds, IoC log patterns, KEV alert, Belnet window (71 days to disclosure, "about ten weeks"), NCSC-NL contradiction, `updated_at` = record `at`, record `fields` cover every changed line in `git diff`, no silent edit, main analysis consistent with the newest section (no "management interface" asserted as Fortinet wording).
- Belnet: 65-day window arithmetic, all four evidence quotes, 2026-09-29 actions, CCB, Risky Bulletin claim, descriptor supported by Risky in this entry, `notable` defensible (access vector now known, referenced to the CVE entry).
- Cisco: v1.1 text, shield limitation quotes, fixed-release table, log paths, TAC procedure, VulnCheck mechanism and counts, CISA alert, NCSC-CH 13021, Live Protect dateline and rule. EPSS 0.01096 is stale against the FIRST API (0.01575 on 2026-10-02) but is a daily value and was not touched by this run.
- Warlock: every Symantec figure and date, 3 evidence quotes verbatim, BleepingComputer relay, Microsoft quote, classification B/2 and `single-source`, registry key and aliases, ToolShell CVE index records, two Swiss SharePoint references exist and are SharePoint breaches, no IOC strings, no em dashes, no workflow language.
- Run record: KEV sweep (two Zammad CVEs COVERED), 7 open backlog rows incl. the Qilin/TCS 2026-10-05 expiry, update dispositions, contradictions paragraph and the FortiMail revision note all hold against disk and the sources. The record's `verification_residual_count` and clock re-stamp are loop-in-progress items.
- Missed angles: none. NCSC-CH hub listing since 2026-09-28 shows only covered items (Citrix, FortiMail, Zimbra, Cisco, WatchGuard, Kiteworks); web searches for in-window zero-days and Swiss public-sector incidents returned nothing new. Coverage looks complete for critical/high signal.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 3)

### Findings summary (machine-readable)
See `work/2026-10-03T0404Z-intel/verification.iter2.findings.yaml` (8 records).
