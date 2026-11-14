**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-14T04:10:40Z · ended_at=2026-11-14T04:29:28Z · duration_seconds=1128

## Verification report — 2026-11-14T0255Z-intel (iteration 1)

Scope: all 188 ledger claims walked (claims.iter1.yaml; rows in verification.iter1.claims.yaml: 176 ok, 9 F3, 2 F4, 1 F5). Every cited URL was fetched this iteration (extract / pdf / ncsc-csh / cisa-kev bridge; BSI page 1 read live with pdftotext after the pdf recipe returned pages 2 to 4 only). Not readable by any rung: ConnectWise Trust Center advisory (403 on extract and WebFetch), Ivanti hub advisory pages (script shell), N-able uptime pages (as the run record says). The one quote the gate could not check (NCSC-NL, Dutch) is verbatim on the page, and the English translation is faithful; the one citation-cve mention the gate left (CVE-2026-121653 on the NCSC-NL page) is on the page. The `cves[]` ids and scores of the three entries whose CVE records changed were checked against the per-CVE authority: Quay (Red Hat CVE pages, CSAF), GitLab (CNA record 7.5, GHSA 8.0), Ivanti (EUVD CNA records), Check Point (KEV bridge, FIRST EPSS).

### Citation does not support the claim

- #1 (F3) Danfoss, main analysis para 3: "On 2026-11-02 refrigeration failures reached retailers in at least six more countries and the first German cases followed ([BleepingComputer, 2026-11-02])". BleepingComputer's article names Belgium, the Netherlands, Sweden, Luxembourg, Ireland and Estonia; Germany appears only in a reader comment ("Several stores in Germany have also reported being attacked on their Facebook pages"). The rewrite dropped the heise and WDR citations that carried the German cases; both are still in sources[]. Re-add them to this sentence.
- #2 (F3) ScreenConnect, main analysis para 3: "ConnectWise says clients 26.6.5 and later block the transfer and that a cloud-console update does not update technician clients; Huntress and Blackpoint saw no successful technician compromise (Microsoft; Blackpoint)". Microsoft attributes only "ConnectWise states that ScreenConnect client 26.6.5 and later block the toolkit's attempted endpoint-to-technician transfer technique"; "a cloud-console update does not automatically update those clients" is Microsoft's own sentence. Huntress's "To date we have not observed a successful jump" is on the Huntress page, not cited in this clause.
- #3 (F3) ScreenConnect, Update 2026-11-14T03:57:58Z para 1: "Microsoft relays ConnectWise's statement that clients 26.6.5 and later block the transfer, that the fix for CVE-2026-84869 was released on 2026-09-08 and that a cloud-console update does not update technician clients". Microsoft: "ConnectWise states that ... 26.6.5 and later block ... The fix for CVE-2026-84869 was released on September 8, 2026. ... a cloud-console update does not automatically update those clients." Only the first is attributed to ConnectWise; ConnectWise's own advisory could not be read by any rung.
- #4 (F3) ScreenConnect, Detection first clause: "RMM+ requests with no matching login, and file-transfer-and-run events (event ID 201, per Blackpoint) ([Blackpoint])". Blackpoint carries event ID 201 but nothing on requests with no matching login; that is Huntress ("There was no corresponding login activity and the commands appeared in the logs reviewed linked to RMM+").
- #5 (F3) N-able, Detection: "in N-central's authentication and audit logs from 2026-11-08 onward ... ([Field Effect, 2026-11-09])". Field Effect gives the log classes but no start date; "from November 8 onward" is Huntress's. The rewrite dropped the Huntress citation from this clause.
- #6 (F3) N-able, Update 2026-11-14T04:00:03Z: "the statement that N-able had seen no signs of compromise dates from 2026-11-12 ([Huntress, 2026-11-13])". The Huntress page does not carry that statement; Tenable ("N-able's November 12 update says it has seen no signs of compromise") and BleepingComputer do.
- #7 (F3) Quay, main analysis para 3: "Red Hat fixes both in Quay 3.9.28, 3.10.28, ... 3.18.3 and has already fixed Quay.io ([Red Hat, 2026-11-11](.../cve-2026-110697))". The cited page gives the eight builds for CVE-2026-110697 only; the CVE-2026-123710 page has no fixed-build table (the sourcing note says so). For 123710 the mapping is the CSAF record's vendor_fix errata RHSA-2026:99019 to 99027 (each "Red Hat Quay v3.x.y", read this iteration), which is in sources[] but not cited here.
- #8 (F3) Quay, Detection: "service_key_rotate and service_key_delete events with a null expiration_date ... ([Red Hat, 2026-11-11](.../cve-2026-110697))". Those indicators are on the CVE-2026-123710 page ("Review audit logs for service_key_rotate and service_key_delete events with a null expiration_date"); the cited 110697 page carries only the robot-token pull/push monitoring. Cite both pages.
- #9 (F3, low confidence) Luna Moth, title and para 1: "those firms appear on the group's leak site, which ReliaQuest takes to mean they did not pay"; title "returns to non-paying law firms". ReliaQuest: "which suggests they likely didn't pay the first extortion demand". The hedge is dropped in the body and the title states it as fact.
- #10 (F3, low confidence) Quay, [Red Hat, 2026-11-14] on the solution article 7149923: the page's dateline is "Updated 2026-11-13T10:56:00+00:00" (extract metadata 2026-11-13). One-day drift, not a timezone artifact; the 14th is the run date.
- #11 (F3, low confidence) GitLab, [GitLab, 2026-11-14] on the detection page: the page carries last_verified "2026-11-12" and Sigma rules dated 2026-11-10; no 14 November date. The sourcing note says the date is "the day it was read", which is not a source date.

### Unsupported / hallucinated facts

- #12 (F4, low confidence) ScreenConnect, Detection second clause: "process-creation telemetry with the ScreenConnect client service as parent of cmd, PowerShell, msiexec or the .NET compiler". "or the .NET compiler" was added this run. Huntress: "TrapWatch.ps1 is launched as SYSTEM, and compiles RelayTrap.cs"; Microsoft: a scheduled task starts the watcher, which "uses the .NET C# compiler to build RelayTrap.exe". The compiler runs under the TrapWatch PowerShell watcher, not the client service; no source states that parent-child pair.
- #13 (F4, low confidence) Danfoss headline: "Strict mode no barrier". CCB: "strict mode does not eliminate the risk"; Midnight Blue: at the strict level "virtually all the web-accessible attack surface is fenced off from unauthenticated users", leaving at least one pre-auth flaw in the session-control binary. "No barrier" overstates "does not eliminate".

### Claims missing inline citation

- #14 (F5) Danfoss, Update 2026-11-14T03:55:09Z, last sentence: "BACS's statement of 2026-11-10 that updates fix the known flaws predates the report and does not address these six." No inline link. The BACS page does say "stehen Sicherheitsupdates zur Verfügung, welche die bekannten Schwachstellen beheben"; add the link.

### Surface contradiction

- #15 (F9, low confidence) N-able, Exposure: "Huntress notes that an allow-list alone does not close the Agent and Probe check-in endpoints ([Huntress, 2026-11-13])". That caution is from Huntress's 11/12 1:10 AM guidance; its 11/12 6:30 AM update says "New information from N-able changes our guidance from earlier this morning" and advises restricting access if Legacy API must stay on. The entry presents the earlier guidance as current.

### Org-triage line missing / inconsistent

- #16 (F16, low confidence) Ivanti priority `notable`. The entry's own takeaway ("warrants an out-of-cycle update even without reported exploitation"), actions[0] ("now"), NCSC-NL's CSAF rating (probability medium, damage high after the public PoC) and the S1 slice's own proposal point at the `high` bar. The run record documents the decision; surfaced for confirmation, not a hard defect.

### Editorial / less-is-more flags (advisory)

- #17 (F11) Ivanti, Update 2026-11-14T04:01:35Z: "which supplies the fixed build the entry lacked": record-keeping narration in a reader-facing section.
- #18 (F11) Danfoss title (101 words) and summary (303 words) have accreted through fourteen records; rewrite rather than append.
- #19 (F11) Luna Moth: new `actor:silent-ransom-group` has aliases [SRG] only, while the existing `campaign:fbi-flash-csa-260526-...` key carries "Luna Moth" and "UNC3753"; alias resolution splits, and the entry links the FBI USB campaign key (a different campaign) with no cited source tying this activity to it.
- #20 (F11) N-able main analysis lost the only Swiss-nexus fact (Huntback's 21-server country list, which does not include Switzerland) and it appears in no section.

### Checked and clean (no finding)

Every other claim of the five new entries and the new text of the five updated entries matched its page, including all 20 literal evidence quotes the gate checked plus the NCSC-NL Dutch quote and translation; BSI notice (criticality 3 / Orange, no fixed version, no known exploitation); CCB; heise (BSI on firmware 5.4.0); Danfoss advisories page and readme (no advisory on the six flaws); Midnight Blue (six flaws, 5.3.2, root, no secure boot, strict-mode flaw, CVEs pending; page body publication stamp Wed Nov 11 2026); Huntress, Blackpoint, Microsoft, Sophos, The Record and the ConnectWise CNA record (CVSS 4.0 9.3 via EUVD-2026-124597); Huntress/Tenable/Huntback/BleepingComputer/Previdian/Apache for N-able; Ivanti (EUVD, CERT-FR date 12 Nov, NCSC-NL CSAF probability/damage); Elastic and Team Cymru; ReliaQuest; Red Hat CVE pages, CSAF, NCSC 13178; GitLab patch page, GitHub blog, oss-security, Git for Windows, THN; Securelist. KEV and EPSS values on Check Point CVE-2026-123039 confirmed (KEV 2026-11-13, due 2026-11-16, EPSS 0.01274); the internal record carries no reader-facing delta. No IOCs, no em dashes in reader-facing text, all main analyses at or under 550 words, headlines under 120 characters, classification blocks present and within vocabulary on every entry, no org_triage or watchlist use.

Missed angles (F10): none evidenced. Telemetry gaps (sygnia, lab52, belden, connectwise trust center) are recorded and none surfaced an in-window item; searches for in-window exploited flaws, Swiss incidents and KEV additions found nothing the run omitted (the Cisco SD-WAN CVE-2026-20245 hit was June 2026; the Outlook zero-day is covered by an existing entry; UnrealIRCd is a documented borderline-drop). Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 13, editorial: 3, advisory: 4)

### Findings summary (machine-readable)

See work/2026-11-14T0255Z-intel/verification.iter1.findings.yaml (20 records: F3 x11, F4 x2, F5 x1, F9 x1, F16 x1, F11 x4).
