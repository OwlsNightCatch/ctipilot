**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-13T04:22:41Z · ended_at=2026-11-13T04:42:30Z · duration_seconds=1189

## Verification report — 2026-11-13T0256Z-intel (iteration 1)

Scope: 8 new entries, 9 updated entries (whole entries read, `git diff HEAD` read for each), the run record. Claim ledger `claims.iter1.yaml`: 372 claims, 372 verdict rows in `verification.iter1.claims.yaml` (full scope, first pass). Cited pages were re-read this iteration (saved bodies first, live `extract`/`url`/`pdf`/CVE List/ENISA/KEV for the rest; the first ANSSI report PDF was read from rendered pages). Structured findings: `verification.iter1.findings.yaml`.

### Citation does not support the claim (F3)

1. **citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws**: "Seven rows (the authentication request overflow, Endpoint Analysis, a reboot loop, HTTP/2, the B64DECODE expression, credentials written to a log and the Application Firewall decompression row) carry ids that ENISA's database already assigns to unrelated products ([ENISA EUVD, 2026-10-15](…EUVD-2026-102489))". The cited record is the Trudesk flaw CVE-2026-111345 only. The other six ids resolve to EUVD-2026-102487 (111343, pig), 102488 (111344, APITable), 102490 (111346, ZenTao), 102491 (111347, go-ldap-admin), 102492 (111348, Likeshop), 102493 (111349, Craftplan); the CVE List agrees. The fact is true, the page vouches for one row. Cite the six records or narrow the clause.
2. **ptc-windchill-…** (low confidence): "NCSC Switzerland lists the exploitation status as unknown, and neither PTC's change log nor the press report an attack on this flaw ([PTC Trust Center])". The PTC page supports only the change-log silence; NCSC's "UNKNOWN" is on post 13174 and "the press" (THN) is not on the cited page.
3. **signdrop-…**: "the researcher says Mode 2 or 3 is not vulnerable ([Cyderes])". Cyderes says only "Systems where Mode is set to 1 (learning) or 0 (enforcement) are in scope". The statement is in the exploit author's GitHub README ("If it's set to 2 or 3 then you're not vulnerable") and Cyberpress, neither cited.
4. **n-able-n-central-…** (body and 2026-11-13 section): "with a root escalation … that has no CVE ([Huntback])". Huntback describes the nable_wrapper.pl setLDFileOwner escalation and never says it has no CVE (Previdian: "No CVE Assigned Yet" for the whole chain).
5. **n-able-…** and **confluence-dc-…**: "Previdian's honeypot recorded the full chain / attackers attempting the full chain ([Previdian])". The Previdian page says "2 Attempts observed, 1 Unique attacker IP" and that its observations "do not show that the target was vulnerable or that the attempt succeeded"; "complete exploit chain" is BleepingComputer's relay. "Recorded the full chain" also overstates an attempt.
6. **confluence-dc-…**: "the same flaw is exploited against on-premises N-able N-central servers with the Legacy API turned on ([Huntback]; [Previdian])" and "servers that have the Legacy API turned on ([Huntback])". Huntback never says the 21 servers had the Legacy API on; Tenable: Huntback "does not say whether the Legacy API was enabled on those servers". Inference attributed as a sourced fact.
7. **cve-2026-119618-…** (low confidence): "a clean run on 2.4.71 … ([Wordfence])". Wordfence says only that the repository has "2.4.71 and HTTP/1.1-only comparison runs"; "clean" is on the researcher's README, cited for the next clause only.
8. **cve-2026-111497-brotli-desigo-…** (section, Defender takeaway, record summary): the eight Apple releases are all cited to `support.apple.com/en-us/149715`, which is "iOS 27.2.1 and iPadOS 27.2.1" only. The rest are on 149716, 149718, 149719, 149720, 149722, 149724 (each carries the brotli CVE-2026-111497 entry) and none is in `sources[]`.
9. **check-point-php2shell-…**: "The standalone PHP hotfix text names only the two PHP CVEs, and no Jumbo take is listed for R81.10 or R81 … ([sk1000362])". sk1000362 does not mention the standalone PHP hotfix; that text is on sk1000302.
10. **darklunnen-…** (low confidence): Fortinet PSIRT dated 2025-03-31; the advisory's Published Date is Jan 14, 2025 (2025-03-31 is the Updated Date).

### Unsupported / hallucinated facts (F4)

11. **darklunnen-…** title: "… Group-IB confirms no Swiss victim". Group-IB says the Swiss lists "do not confirm vulnerability or successful exploitation" and that for several operations, including the Swiss S3 restic row ("Production snapshots enumerated"), the evidence "does not independently confirm successful exploitation, unauthorized access, or data exfiltration". It never says no Swiss victim exists. The body wording is correct; the title overstates.
12. **huntress-teams-…**: "… and Huntress saw no post-compromise activity". Huntress: "quickly identified and contained the incident, barring the attack from escalating"; the page also lists subsequent python-requests and node sign-ins, which the entry's own Detection line repeats.
13. **n-able-…** summary and evidence quote 8: "Huntress says a fully patched server should be treated as vulnerable" / "A fully patched N-central server should be treated as vulnerable. There is no fix available at the time of writing." This is Huntress's 1:10 AM ET update; its 6:30 AM ET update says "New information from N-able changes our guidance from earlier this morning … Servers running 2026.4 HF2 with Legacy API disabled are not exposed to this exploit chain." The summary and quote present the superseded guidance as current and contradict the body.
14. **cve-2026-119618-…** summary and record summary: "Debian bookworm and trixie, Ubuntu and Alpine ship 2.4.71 packages". USN-9090-1 lists Ubuntu-versioned backports (e.g. 24.04 2.4.58-1ubuntu8.19, 26.10 2.4.68-1ubuntu6.2), not 2.4.71.
15. **cve-2026-111497-brotli-desigo-…**: "Cisco's advisory, version 1.11 of 2026-11-10 … Identity Services Engine as under investigation". The cited advisory is now version 1.12 of 2026-NOV-12 and lists "Identity Services Engine (ISE) Not impacted". The entry was updated on 2026-11-13 without refreshing the Cisco paragraph.
16. **check-point-php2shell-…**: "installed a backdoor that survives patching" (summary, record summary), "because the implant persists through patching ([Check Point Research])", and "Patching removes none of this." CPR calls TSGA persistent ("backup and snapshot persistence") but never says a hotfix leaves it in place. Inference stated as a sourced fact.
17. **confluence-dc-…** record summary (low confidence): "Apache will not release an Axis 1.x fix"; source: "does not expect to create an Axis 1.x release fixing this problem".
18. **run record** notes: "PTC Windchill/FlexPLM CVE-2026-126325: single national-CERT source (carve-out `single-source-national-cert`)". The entry carries `verification: multi-source`, PTC's Trust Center as primary and four corroborating sources.

### Surface contradiction (F9)

19. **n-able-…** (low confidence): The Hacker News (cited) quotes Previdian that patches for CVE-2026-90436 "were released on November 6, 2026"; the entry says `no-patch` / Apache "does not expect to release" a fix. Apache offers a patch commit, not a release; the discrepancy is not noted.

### Claims missing inline citation (F5)

20. **confluence-dc-…** (low confidence): the **Detection:** line has no citation and no "inference" disclaimer; "child processes of the Confluence JVM" and XML-RPC endpoint logs appear in no cited source.

### Drop / calibration (F16, F12, F17, F18)

21. **citrix-…** priority `high` (low confidence): by the entry's own text the vendor impact is crash or DoS, no exploitation, no PoC, "no source says that code execution is possible". The default-configuration edge-gateway argument is defensible; Phase 4 says doubt resolves to `notable`.
22. **saxony-…** (low confidence): incident floor. No access vector, no actor, three paragraphs, `notable`. The transferable ground can be two sentences at `routine`.
23. **saxony-…** F12 (low confidence): `verification: multi-source` although heise relays Spiegel and the Spiegel body was unread.
24. **saxony-…** F17 (low confidence): credibility 2 although both outlets rest on one informant for message content and keys.
25. **wfx-phantom-…** F18 (low confidence): actions[0] restates the Detection line's strings and bundles hunt, revoke, rotate and AWS/Azure cleanup.

### Missed angles / thin (F10, F8)

26. **F10 (low confidence):** Akamai StrikeStub (ClickFix PowerShell RAT served from a compromised legitimate .ch site; S3 notes "kept only for the compromised .ch delivery site"), https://www.akamai.com/blog/security-research/2026/nov/strikestub-clickfix-powershell-malware-modular-rat, 2026-11-12. Query: `StrikeStub ClickFix Akamai compromised .ch site`. Otherwise coverage looks complete: Patch Tuesday, Ivanti EPM, Outlook KEV, SonicWall and the PHP2Shell vendor wave are already covered; the other borderline drops are defensible.
27. **F8 (low confidence):** Apple HomeView Software 27.2 (support.apple.com/en-us/149851, 2026-11-12) carries the same brotli fix and is in the run's saved bodies but not in the Apple list.

### Editorial / less-is-more flags (advisory, F11)

28. SignDrop (hid.dll in the ink directory) and WFX Phantom (branch `wfx-docs`, commit messages, `wfx-ci` credentials) carry actor-chosen file, branch, commit and credential names; they read as detection hooks but are indicator-like, and WFX's strings are repeated in the action.
29. DarkLunnen (Group-IB-tracked operator) and WFX Phantom / wfx-loot have no actor/campaign/malware registry key; `entities_added` lists products only.
30. Huntress entry: `techniques[]` omits T1550.004 (session replay, quoted as evidence) and T1539, both in the source's ATT&CK table.
31. PHP2Shell vendor entry: the 2026-11-13 `improvement` section carries a vendor delta (Analyzer ETA moved 12 to 18 November); an `improvement` never floats the entry.
32. Rolling tracker or listing pages (Debian, Alpine, SUSE, Copeland download page) are dated with the reading date.

### Checked and fine (no finding)

New entries: Citrix scores, builds, bulletin counts (28 rows, 9 at 9.0+, 10 High on CIA) and ENISA/CVE-List 9.3 versus bulletin 9.4; PTC release lines (11 Windchill, 10 FlexPLM), CVSS 3.1/4.0; Dixell seven 9.2 to 9.3 VulnCheck records, EoS bulletin, Dixell France guide, CERT-FR alert (last version 2026-10-16), NCSC 13054, BACS, Ransom-ISAC XWEB Pro; SignDrop chain, detection table and quotes; WFX counts (63,000+, 4,837, 1,835, 8,926, 1,838) and StepSecurity detail; DarkLunnen counts and recommendations; Saxony (heise facts, German originals and translations); Huntress Teams chain. Updated entries: Siemens SSA-045512/443410/242944/678870 counts (15 + 28, 8 not affected), Mitel rev 5.0 (8.1), Cisco fix table, Check Point sk1000302/1000362 takes and CPR detail, Trend Micro KA-0024802 of 2026-11-12, Quest KB, NetApp advisory data, MSRC revision 7 and KB list, the .NET OOB pages, ScreenConnect sources (Huntress, ConnectWise CNA/EUVD, The Record, Blackpoint, Sophos, BleepingComputer), ANSSI CTI-006 (pages 2 to 7 read visually) and CTI-010. Evidence quotes: all re-checked against saved or live pages; the ones the gate could not machine-check (NCSC 13174; Cisco, Siemens, Mitel, Atlassian) are verbatim. No em dashes or workflow vocabulary in reader-facing text; classification blocks present everywhere; no org_triage or watchlist use.

### Verdict

NEEDS_FIXES (truth: 18, editorial: 9, advisory: 5)

Truth = F3 x10 (#1 to #10) + F4 x8 (#11 to #18). Editorial = F5 x1, F8 x1, F9 x1, F10 x1, F12 x1, F16 x2, F17 x1, F18 x1. Advisory = F11 x5. Highest-value fixes: #13 (N-able summary and evidence quote contradict Huntress's own latest guidance), #14 and #16 (Apache summary on Ubuntu; Check Point "survives patching"), #15 (Cisco paragraph stale against the live advisory), #11 (DarkLunnen title), #8 (Apple sources), #1 (Citrix EUVD adjacency).
