**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-13T04:49:40Z · ended_at=2026-11-13T05:10:53Z · duration_seconds=1273

## Verification report — 2026-11-13T0256Z-intel (iteration 2)

Scope walked: every claim in claims.changed.iter2.yaml (47/47), every claim of the twelve remediated entries (Citrix, Windchill, SignDrop, WFX, DarkLunnen, Huntress, N-able, Confluence, Apache httpd, Brotli/Desigo, Check Point, Trend Micro PHP2Shell), and a sample of the remaining four entries (ANSSI 7/16, Microsoft .NET 16/30, ScreenConnect 13/22, Dixell 18/27; each updated entry's new section read in full). 333 verdict rows written to verification.iter2.claims.yaml (329 ok, 2 F3, 1 F4, 1 F5). Every iteration-1 remediation was re-checked against its source (below).

### Prior-iteration deltas (all 32 items)
Items 1-20, 22-25, 27-31 re-read against the cited pages this iteration: remediation correct unless noted. Notes:
- 1 Citrix: the tail clause is narrowed correctly, but the sentence still asserts seven collisions on one citation (finding F3 #1).
- 2 Windchill: NCSC 13174 'UNKNOWN' and 'Behind a customer login'; PTC change log 11/11/2026 carries no attack statement: correct.
- 3 SignDrop: sentence now states only Cyderes' 'Mode ... 1 (learning) or 0 (enforcement) are in scope': correct.
- 4-6, 13, 17, 19, 20 N-able/Confluence: Huntback (21 nc_ rigs, 19 on 2026.4.1.26, countries US 9 / ZA 4 / CA 4 / UK DE FR SE 1; no Legacy API statement), Previdian ('2 exploitation attempts ... 1 unique attacker IP', 'No CVE Assigned Yet'), Huntress 6:30 AM ET ('Servers running 2026.4 HF2 with Legacy API disabled are not exposed to this exploit chain', verbatim), Apache post ('does not expect to create an Axis 1.x release'), THN (Dewhurst: patches 'released on November 6'): all remediations correct.
- 7, 14 httpd: researcher README 'shows httpd 2.4.71 clean under the same traffic'; Debian tracker bookworm 2.4.71-1~deb12u1 / trixie 2.4.71-1~deb13u1 fixed, forky vulnerable; Alpine 3.21-3.24 2.4.71-r0; USN-9090-1 Ubuntu-versioned backports; SUSE pending: correct.
- 8, 15, 27 Brotli: Apple pages 149715/149716/149718/149719/149720/149722/149724 (Released November 9, 2026) and 149851 (HomeView 27.2, November 12, 2026) each list 'brotli ... An out-of-bounds write issue was addressed with improved input validation ... CVE-2026-111497'; Cisco advisory read live: version 1.12 Interim 2026-NOV-12, ISE Not impacted, Duo Network Gateway 3.4.2, RoomOS 11.41.2.3 / 26.7.4.3, PSIRT 'aware that proof-of-concept exploit code is available ... not aware of any malicious use': correct. HomeView not carried into cves[] (advisory item below).
- 9, 16 Check Point: sk1000302 carries the standalone-hotfix text and Jumbo takes; sk1000362 lists only Jumbo takes (no R81.10/R81), 'Check Point observed an active exploit ... a couple of dozen customers'; takeaway now labels the implant-persistence point an inference: correct.
- 10, 11 DarkLunnen: Fortinet FG-IR-24-535 date 2025-01-14 and Group-IB wording ('do not confirm vulnerability or successful exploitation'; restic row 'Production snapshots enumerated'): correct, title now hedged.
- 12 Huntress: 'quickly identified and contained the incident, barring the attack from escalating': correct.
- 18 run record: inclusion note now matches the entry (multi-source): correct.
- 21 (declined, Citrix high): judged below (F16, low confidence, defensible).
- 22-24 Saxony entry: file absent in entries/2026-11-13/ (7 files), no reference to it in other entries or the registry; run-record disposition matches.
- 25 WFX action: rewritten without the search strings, one task: correct.
- 26 (declined, Swiss ClickFix site): accepted; the Swiss site is unnamed in the cited material and the delivery class is covered.
- 28, 29, 30, 31: SignDrop file name kept (advisory F11 #3 sharpens the wording); actor:darklunnen and malware:wfx-phantom are in entities[] and in the registry; Huntress techniques now carry T1550.004 and T1539; the Trend Micro record is an update with heading and updated_at (2026-11-13T03:48:26Z) in step, and the Analyzer ETA move 12 to 18 Nov is on KA-0024802 (last updated 2026/11/12).
- 32 (declined, rolling pages dated by reading): accepted; the Apache page itself dates 2.4.71 to 2026-11-11, the other pages are labelled as readings.

### Citation does not support the claim
- #1 F3 citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws. Claim: "Seven rows (the authentication request overflow, Endpoint Analysis, a reboot loop, HTTP/2, the B64DECODE expression, credentials written to a log and an Application Firewall decompression row) carry ids that collide with unrelated products in the CVE database, one of them a Trudesk flaw in ENISA's record ([ENISA EUVD, 2026-10-15](...EUVD-2026-102489))". The cited record carries only CVE-2026-111345 (Trudesk; aliases CVE-2026-111345, GHSA-xm42-mhff-286m). The other six collisions are real (fetched: CVE-2026-111343 EUVD-2026-102487 pig; 111344 EUVD-2026-102488 APITable; 111346 EUVD-2026-102490 ZenTao; 111347 EUVD-2026-102491 go-ldap-admin; 111348 EUVD-2026-102492 Likeshop; 111349 EUVD-2026-102493 Craftplan) but are not cited. Fix: add and cite those six records or cut the sentence to the one cited record.
- #2 F3 wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens. Claim: "StepSecurity counts more than 63,000 such probes by 2026-11-12, Aikido ... counts 4,837 compromised accounts and at least 1,835 repositories ..., and Endor Labs counts 8,926 infected repositories ([Aikido]; [Endor Labs])". The 63,000 figure ('As of 07:40 UTC on November 12, GitHub search returns more than 63,000 of the attacker's probe pull requests') is on the StepSecurity page only; Aikido gives 61,839 probe PRs and 61,764 repositories, Endor Labs 8,926. Fix: add the StepSecurity citation at that clause.

### Unsupported / hallucinated facts
- #3 F4 (low confidence) confluence-dc-cve-2026-90436-apache-axis-remote-api-rce, summary: "Atlassian's out-of-cycle advisory of 2026-11-09". The Atlassian advisory ('Advisory Release Date Tue, Nov 9 2026 22:00 PST'), BSI WID-SEC-2026-4427 (initial release 2026-11-09T23:00Z) and the Apache post say nothing about cadence; the word is pre-existing text from the 2026-11-11 run and no cited source supports it.

### Claims missing inline citation
- #4 F5 (low confidence) cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo, Update 2026-11-13T03:56:37Z last sentence: "the iOS 18.7.12 and watchOS 26.6.1 releases list no Brotli entry ...". True (support.apple.com/en-us/149717 lists AirPlay, Bluetooth, CoreUtils x2, MediaRemote, rapportd; /149723 lists AirPlay, Bluetooth, CoreUtils x2, rapportd) but uncited and not in sources[].

### Needs more research
- #5 F8 (low confidence) check-point-php2shell-sk1000302-portal-and-vpn-gateways: Check Point Research says TSGA and TSProxy are modified variants of PhiliKit (ESET: UNC5221, Ivanti campaigns), share code, configuration and key material with it, and cautions that the evidence does not support high-confidence attribution. The body drops the lineage; only the sourcing_note says attribution is open. One sentence would give hunters the pivot.

### Missed angles
- #6 F10 (low confidence) Cisco BroadWorks CVE-2026-20320: KEV dateAdded 2026-11-10 (cisa-kev bridge, 'unauthenticated, remote attacker', XXE); in no entry and not in state/cves_seen.json; outside this run's window and borderline-dropped by earlier fires per S1, so the run record's dropped list does not name it. Swiss exposure uncertain. Query: "Cisco BroadWorks CVE-2026-20320 exploited KEV XXE OCI-P". Coverage otherwise looks complete: the run's four slices and five deep reads cover the window's exploited edge CVEs, the Check Point/ScreenConnect/N-able developments, the home-region (NCSC-CH, BACS, Group-IB Swiss list) items; no further in-window gap evidenced.

### Org-triage / priority
- #7 F16 (low confidence, judgement call) citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws, priority high. Facts the entry cites: vendor impact 'unpredictable behaviour or denial of service', CERT-EU 'Citrix reports no exploitation, and no public proof-of-concept has been confirmed', NCSC-CH exploitation status UNKNOWN, no workaround; heise (read this iteration) says these are the first patches of a new monthly security-release program close to Patch Tuesday. Default-configuration reach of CVE-2026-120868 supports fast patching, which the body says; the high bar asks for a decision beyond the regular cycle. The main agent's rationale is defensible; if high stays, surface the monthly-cycle fact in the body.

### Editorial / less-is-more flags (advisory)
- #8 F11 Brotli: HomeView Software 27.2 is in summary, body, sources[] and affected_products but not in cves[CVE-2026-111497].affected/.fixed; no Apple key is in entities[] while the run record lists apple-visionos, apple-watchos, apple-homeview-software as entities_added.
- #9 F11 Huntress: the source's ATT&CK table also maps T1557 and T1684.001 (active in the pinned 20.1), both behaviours in the body.
- #10 F11 SignDrop: "hid.dll ... a file that does not ship with Windows" and Detection "because the file does not ship with Windows"; Cyderes: 'The real hid.dll lives in C:\Windows\System32' and 'does not ship there'. Say 'in that directory'.
- #11 F11 Citrix sourcing_note names heise as a restating source; heise is not in sources[] or cited (https://www.heise.de/news/Angreifer-koennen-Citrix-NetScaler-ADC-und-NetScaler-Gateway-lahmlegen-11522940.html, 2026-11-12). The note also says the colliding ids 'are not carried in the CVE records here' (pipeline wording).
- #12 F11 DarkLunnen: tag cisa-kev with cves: [] and no cited KEV record; CVE-2024-55591 is in KEV (bridge: 2025-01-14), so cite it or drop the tag.
- #13 F11 Confluence Exposure: "likeliest to have" is an inference without the label the Detection line carries.
- #14 F11 Microsoft .NET update: MSRC lists two fixed KBs for Server 2025 (KB5131077, KB5131080) and Windows 11 24H2-26H2 (KB5132043, KB5132061); '(ESU)' is not in the record; the record also lists PowerShell 7.4-7.6 and Visual Studio 2017-2026.
- #15 F11 Apache httpd: Ubuntu 20.04 fix is 2.4.41-4ubuntu3.23+esm11 (ESM); the researcher repository (cited) lists mod_h2 2.0.43 as fixed.

### Items checked and clean (no finding)
All other claims in scope read as cited: Windchill (PTC change log, NCSC 13174, ENISA/CVE record scores, THN version lists, KEV for CVE-2026-12569), SignDrop (Cyderes, BleepingComputer, SecurityOnline), WFX Phantom (StepSecurity, Aikido, Endor Labs, BleepingComputer), DarkLunnen (Group-IB, Fortinet PSIRT), Huntress, N-able (Huntress updates, Huntback, Previdian, Tenable, Field Effect, BleepingComputer, release notes, THN, Apache post), Confluence (Atlassian, BSI, Huntback), Apache httpd (project page, Red Hat, Wiz, Wordfence, Debian, Alpine, Ubuntu, SUSE, researcher repo), Brotli (Apple x8, Cisco, Mitel, Siemens SSA-045512/443410/242944/678870 including the 15 and 28 row counts, CISA KEV), Check Point (sk1000302, sk1000362, CPR), Trend Micro (KA-0024802 table incl. B7351 / B20113 / Nov. 17 / Nov. 18, Download Center, KEV 2026-10-26, NetApp data), ScreenConnect (ConnectWise CNA README incl. CVSS 4.0 9.3, The Record, Blackpoint, Huntress, ENISA EUVD-2026-124597), ANSSI CTI-010 (12 Nov 2026; 64 breaches, 5 ministries, OFB IDOR >1000, France Travail 60 000 + SMS, VACAF ~1.2 M dossiers 8-10 Oct, 25 of 30 académies), Microsoft .NET (MSRC revision 7, KB mapping, .NET blog, announcements #494), Dixell (VulnCheck x4 + ENISA 14 records / seven at 9.2-9.3, Copeland bulletin, Dixell France PDF, NCSC 13054, BACS, Ransom-ISAC, CERT-FR). Classification, org_triage (null everywhere), watchlist (false), single-source flags and sourcing notes, em dash, IOC and workflow-vocabulary scans: no defect. updated_at mirrors equal the new record `at` in all nine updated entries; no silent edit evidenced.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 4, advisory: 8)

### Findings summary (machine-readable)
See verification.iter2.findings.yaml (15 records).
