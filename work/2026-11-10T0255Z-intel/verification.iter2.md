**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-10T04:28:26Z · ended_at=2026-11-10T04:51:32Z · duration_seconds=1386

## Verification report — 2026-11-10T0255Z-intel (iteration 2)

Scope: all 11 entries (4 new, 7 updated), the run record, the whole ledger (272 claims; every changed claim, every claim of every remediated entry, and the unremediated remainder; verdict rows in `verification.iter2.claims.yaml`: 260 ok, 3 F3, 1 F4, 2 F5, 6 unreadable; `claim_ledger.py --coverage 2` reports 272/272 answered). Every cited page was fetched this iteration (extract, raw url, pdf, `ncsc-csh post`, `cisa-kev`; CISA alerts of 2026-11-09 and 2026-11-06 with WebFetch). Unreadable on every rung: the OX Security post (403 on extract, url, WebFetch, jina), the SonicWall PSIRT affected-product table (script-built; the jina capture lacks it) and the BSI WID advisory body (script-built; the WID listing API confirmed classification and CVE only). Dedup: no new entry's CVEs or entities appear in prior coverage except the declared N-able references.

### Prior-iteration deltas (checked before the cold pass)

- N-able: write-ups and Python PoC clause now rests on Field Effect ("technical writeups, screenshots, captured output, and Python PoC code"): fixed. "proof-of-concept exploit code", "earlier flaw waves", the single action and the two-date sourcing_note (BleepingComputer "late Sunday, November 8", Censys PoC "released publicly on November 9") are right. The reworded Detection line is supported for its first clause (Huntress "Review login and authentication activity from November 8 onward"; Field Effect lists administrator account creation, privilege changes, configuration modifications, API integrations); its second clause now has a new adjacency defect (finding #2).
- OpenSSH: Alpine's advisory carries the detection, restart, container, fixed-branch table (3.16 9.0_p1-r6 and every other row), 3.16 and cloud-image text. NCSC's "other software using similar authentication paths may also be affected" is on post 13155. "gridpoint" is GreyNoise's word. Residual: OX-only clauses (#3), Alpine's treat-as-compromised condition (#4).
- Barracuda: headline matches the source (Barracuda's statement names no flaw; CCCS AV26-1112 Update 1 names CVE-2026-116606); the narration sentence is gone.
- BluePhishing: Proofpoint's "According to Microsoft documentation, inherited permissions are not visible in the Entra portal or via Microsoft Graph" and its test caveat ("silent inheritance ... only observed for delegated permissions granted by a user consent link") are now carried; "default Microsoft Entra users" is Proofpoint's and Message Center's wording. Fixed.
- Danfoss: "A separate incident reached healthcare cold storage" is correct against EFS's release; the prosecutor's arrest-warrant request and Reuters' "could not establish exactly how the French made their determination" are on the NBC page (fetched) and NBC is in sources[]; one name for the unit ("centre électronique et cyber") matches the ministry text; the French original in `original:` is a verbatim substring of the ministry page and the translation is faithful. CERT-FR report CTI-009 (read with the pdf bridge) supports the indicator list, the FOFA, CyberbanNews, Farsi, Schneider reconnaissance and Modbus port 502 statements; Sekoia's "may have been conducted by the same threat actor" quote is verbatim.
- FreeSWITCH KEV update: KEV JSON `dateAdded` 2026-11-09 for CVE-2026-116779, CISA alert text "based on evidence of active exploitation" present; verification, sourcing_note and body are consistent. The edited action is garbled (#14).
- Ahsay: new section is supported by Huntress's follow-up (five webshell families, PNG steganography, signed-API shell with 4 GB chunked transfer, self-deleting shell, second XMRig miner with a backdated one-minute SYSTEM task, embedded Python started from a Run key with the MachineGuid marker, gost/chisel, AnyDesk/Atera/Splashtop, Defender exclusions, Veeam credential-theft command, re-image advice); the Sigma, WinRing0 and Horizon3 artifact items are restored and verified. Residuals #6 and #12.
- IBM: event_date 2026-11-07 and "IBM lists the fix for Linux" match the bulletin (initial publication 07 Nov 2026; fix table platform Linux). Entities linked.

### Citation does not support the claim

- #3 F3 (low confidence, unreadable) openssh entry: clauses that still rest on OX Security. "OX scores the flaw CVSS 3.1 8.1", the mechanism sentence, "On Alpine's official AWS and Azure images the passwordless alpine user can run doas without a password, so the bypass chains to root", `cves[].fixed` "per OX Security", the OX evidence quote and the sourcing_note "OX Security's analysis is the source of the CVSS score" cannot be checked (403 on every rung). Readable pages attribute 8.1 elsewhere (GreyNoise timeline "Published to NVD CVE-2026-123158, CVSS 8.1"; The Hacker News "CVSS score: 8.1"). Alpine's page states the image condition more strictly: tiny-cloud qcow2, VHD and AMI images "are safe on first boot" and "become exploitable as soon as any `$6$` hash exists on the machine". The fixed-package table is Alpine's own. Cite Alpine for the condition and the table; attribute the score to NVD or drop "OX scores".
- #4 F3 (low confidence) openssh Detection: "treating the machine as compromised if one is found" vs Alpine "If you cannot rule out a login, treat the machine as compromised." Restore Alpine's condition.
- #5 F3 (low confidence) openssh summary: "Previdian counts 20 attempts from 13 addresses" in the present tense; the page (saved by the gate at 03:54 UTC and fetched now) says "22 exploitation attempts, 14 unique attacker IPs, and 10 countries ... last observed Nov 10, 2026. Listed in CISA KEV." Update or date the figures.
- #2 F3 (low confidence) N-able Detection, second clause ("process-creation and script-execution events whose parent is the RMM agent, new software deployments, remote-control sessions and automation-policy changes ...") cited to Huntress alone. Huntress: "monitor for anomalous remote access sessions, new scripts being deployed, or the unauthorized creation of new administrator accounts". Deployments and policy changes are Field Effect's; the parent-process telemetry is the entry's inference.
- #6 F3 (low confidence) Ahsay Update 2026-11-10: "Huntress reads the additional Linux-style and decoy folders as a sign that the exploit simply tried every likely location." Uncited, and Huntress ties "simply tried every likely location" to the Linux-style paths only; the random six-character folders are described separately ("imitate the structure of an AhsayCBS install").
- #7 F3 (low confidence, unreadable) FreeSWITCH: BSI WID-SEC-2026-4364 "critical" and CVE confirmed through the WID listing API (classification kritisch, base score 98, product SignalWire FreeSWITCH); the "versions before 1.11.3" statement and the 2026-11-05 date are not readable (the listing row is dated 2026-11-06T10:29Z, status UPDATE).
- #8 F3 (low confidence, unreadable; declined in iteration 1) SonicWall hardware-family and NSv-model lists: no readable capture carries the product table; nothing contradicts it and the sourcing_note discloses the capture limit. If re-declined, this item alone should not hold the chain.

### Generic / oversight URLs (replace with specific article)

- #1 F2 (low confidence) openssh entry: https://sshole.events.greynoise.io/ is GreyNoise's live event dashboard (subdomain root, changing counters and tables) and carries the KEV-update evidence alone. BleepingComputer's 2026-11-09 article https://www.bleepingcomputer.com/news/security/hackers-exploit-sshole-openssh-flaw-to-breach-linux-systems/ (fetched this iteration) states the same facts: first successful exploitation "on November 7 at 00:46 UTC", the implant that "couldn't reach its command-and-control (C2) server", cloud-metadata queries, authorized_keys edits. Add it as a corroborating source.

### Unsupported / hallucinated facts

- #9 F4 (low confidence) SAP body: "ENISA shows an EPSS score of 0.0 for each, that is, not yet scored." The EUVD records carry only `"epss":0.0`; none says what the value means.

### Claims missing inline citation

- #10 F5 (low confidence) openssh Update 2026-11-10: "NCSC Switzerland's advisory, last edited on 2026-11-06, still rates the exploitation status unknown." True (post 13155 lastModified 2026-11-06T10:35:52Z, "Current exploitation status: UNKNOWN") but unlinked.
- #11 F5 (low confidence) SonicWall Update 2026-11-10: "The advisory's first version named no workaround." Unlinked; BleepingComputer 2026-11-06 (in sources[]) says SonicWall "says no workarounds are available".

### Needs more research

- #12 F8 (low confidence) Ahsay Detection: the rewrite dropped "where the service process is the CBS JVM on Linux" (Horizon3: "Suspicious child processes spawning from cbssvcX64.exe (Windows) or the CBS JVM (Linux)") although the Exposure line cites Horizon3 for the Linux chain; it also dropped Huntress's "renamed copy of the NSSM service manager" pivot. Restore the Linux parent.
- #13 F8 (low confidence) openssh: no actor class for the exploitation. BleepingComputer and SecurityWeek (both 2026-11-09): watchTowr observed exploitation "associated with botnets and cryptomining activity"; BleepingComputer: GreyNoise's 16 successful chains from six source addresses are "not representative of the broader activity". One cited sentence.

### Action-item discipline

- #14 F18 FreeSWITCH actions[0]: "because the advisory lists disclosure of configuration and credentials as an impact says exploitation has been observed and CISA lists the flaw as exploited." The edit dropped the "and" and the subject of "says"; the sentence is ungrammatical in the aggregated task list. Suggested: "...as an impact, the vendor says exploitation has been observed and CISA lists the flaw as exploited".

### Editorial / less-is-more flags (advisory)

- #15 F11 run record notes: "Four new entries ... and six changelog records (OpenSSH, Barracuda, SonicWall, the French refrigeration attacks, the PK Softech funds, AhsayCBS)" while `entries_updated: 7` and the next bullet say FreeSWITCH also shipped an update.

### Checks that passed (not findings)

N-able (Huntress, Field Effect, BleepingComputer, Censys: 33 flaws, four chains, build 2026.4.0.31 pre-release, 15:15 UTC statement, 1,728 hosts, no CVE ids, no-reboot-hotfix caveat; all four evidence quotes verbatim; source dates match). BluePhishing (all three evidence quotes verbatim; JSON-LD datePublished 2026-11-09T17:39Z and the visible dateline "November 09, 2026" match the entry, the `article:published_time` meta says 2026-11-07, which the run record discloses). IBM (CVSS 9.8, 5.0.0 to 5.0.19, 5.0.19 PL1 Linux, no workaround; KEV text verbatim; CISA alert read with WebFetch). SAP (four EUVD records and the four CVE JSON records: CVSS 3.1 10.0 with vector AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, note numbers, version lists, component grouping; published 2026-11-10 hours before Patch Day). Barracuda (advisory timeline, updated 2026-11-09 9:00pm EST, patch ids, CVE record ranges `lessThanOrEqual` 9.4.0.27 / 6.4.0 / 11.0.1 / 16.1.100.100 / 5.5.4.0 / 2.2.1 and `lessThan` 9.4.0.030, watchTowr chain, Campus 9.4.0.029). SonicWall (PSIRT text, workaround, Last Updated 2026-11-09, CISA 2026-11-06 alert). FreeSWITCH (GHSA text, CVSS 9.8, <= 1.11.2, 1.11.3 release note "Add enable-chat-api-proto"). Publica (admin.ch, PK Softech notice, watson.ch 2026-11-03, NZZ, EDÖB, Inside IT 2026-11-09 for the Zug fund). Danfoss (SRF, ENISA, Ransom-ISAC 743 writes, Khaleej AFP, ministry, NBC, Sekoia, CERT-FR PDF). Record types and updated_at mirrors are correct; sections match record summaries; no IOCs, no em dash outside headings, no workflow vocabulary, classification blocks within vocabulary, no org_triage or watchlist use. Priority calibration is consistent with the store (KEV-listed non-edge products such as Adobe Commerce and Drupal Commerce are `notable`; edge products `high`); SAP stays `notable` and the iteration-1 F7 and GPUStack points are not re-raised: the analysis states why the mechanics force the timeline, and GPUStack remains a defensible borderline-drop. Coverage looks complete: NCSC Security Hub (latest posts 13157, 13155, 13054, 13144 all covered or out of scope), a Swiss public-sector incident search and an N-able hotfix search found nothing newer in the window.

### Verdict

NEEDS_FIXES (truth: 9, editorial: 5, advisory: 1)

### Findings summary (machine-readable)

See `work/2026-11-10T0255Z-intel/verification.iter2.findings.yaml` (15 records; #14 is a definite defect, #15 is advisory, the rest are low-confidence).
