**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-12T06:12:59Z · ended_at=2026-11-12T06:34:13Z · duration_seconds=1274

## Verification report — 2026-11-12T0255Z-intel (iteration 4)

Scope (post-fix pass): all 18 claims of `claims.changed.iter4.yaml`; every claim of the five entries remediated in iteration 3 (ScreenConnect 15, Brotli 26, Falcon 14, Chrome 22, Fortinet 51); and, beyond the required quarter, every claim of the four new entries not in that set (CCB 14, GSocket 13, Apache 21, Plone 13) plus the Certighost, IoT2050, PHP2Shell, eMudhra and Publica claims that sit in this run's new sections or that I could check against a live page (17 + 9 + 10 + 5 + 5). 235 rows in `verification.iter4.claims.yaml` (232 ok, 1 F3, 2 F14 rows for one defect). The 98 ledger claims without a row are the unsampled remainder of the five older entries (Certighost 4, IoT2050 12, PHP2Shell 16, eMudhra 31, Publica 35), whose earlier sections no changed claim touches; 46 of those 144 (32 percent, above the quarter) are rowed, so `tools/claim_ledger.py --coverage 4` reports 98 missing by design of the post-fix scope, not a skipped scope. Pages were fetched live this iteration: Huntress, BleepingComputer (extract and raw), Sophos, Unit 42, Symantec, Trend (PeckBirdy), Chrome Releases x4, Edge notes, SecurityWeek, NCSC hub (13165, 13092), CISA alerts (WebFetch) and KEV JSON, Cisco, Siemens CSAF (SSA-242944/-678870/-045512/-443410/-834709) and HTML, Mitel, 20 Fortinet PSIRT pages (HTML for CVSS, CVE id, 'Known Exploited'; the OSPF CSAF for the attack vector) and the Fortinet blog, Apache, Red Hat CVE and both RHSA pages, Wiz, Debian tracker, Plone (three posts and five GitHub advisories), Microsoft GSocket blog, CCB and both Microsoft Learn pages, Kaspersky Citrus, the Defender Certighost post and CybersecurityNews, VulnCheck, Trend KA-0024802 and four Download Center pages, Quest KB, NetApp advisory data, Mozilla bug 2083449 comments, BleepingComputer eMudhra, Publica, PK Softech, watson, SRF. Claims resting on a CSAF field parse carry a description of the parsed fields as their passage rather than a prose quote.

### Prior-iteration deltas (iteration 3 findings, all 9)

- ScreenConnect F4/F8 (Huntress update): remediation correct. Huntress now: "Huntress has learned that the activity seems to be related to one of the specific extensions that had already been disabled by ConnectWise, RMM+" and "versions 1.0.31 and 1.0.32 contained a serious authentication flaw: if an administrator had never configured the extension's access key, RMM+ would accept a blank one." The summary, body paragraph 2, Exposure (RMMPlus.AccessKey and version discriminator), Detection (RMM+ requests with no matching login), takeaway and actions[0] now match; the old "access is unknown / not a flaw" statements are gone. One new defect in the rewritten sentence (F3 below).
- Brotli F3 (Cisco dates): correct. Live Cisco v1.11 (2026-NOV-10) fix table carries Nov 2026, Dec 2026, Feb 2027, Mar 2027 and ES 202701; "November 2026 to March 2027" is right and "July" appears nowhere.
- Falcon F3/F11 (PDF Viewer): correct. Symantec: "The group's primary implant was a malicious browser extension named “PDF Viewer”"; Unit 42 lists "The Jewelbug Dossier [PDF]" only under Additional Resources, so "Unit 42 lists it only as a further resource" is accurate and the Unit 42 sentence no longer carries the Jewelbug clause.
- Chrome F4: correct. Stable 157.0.8103.50 has one row "[TBD][572578603][582442907] High CVE-2026-125350"; Extended Stable 156.0.8078.96 lists "[572578603] High CVE-2026-125346" and "[582442907] High CVE-2026-125350" separately; "both pages list it as fixed and differ only on its CVE id" holds. 83/72 fixes and 5/4 Critical rows on the 2026-11-11 pages hold (five Critical use-after-free rows on Stable).
- Fortinet F14: only partly remediated. The 2026-11-11 section now says "none of the 2026-11-10 advisories states exploitation", but the summary tail and the first body paragraph still carry the absolute form (F14 below).
- Fortinet F4 (BGP detection): correct. FG-IR-26-268: "a configured ibgp neighbor to send malicious/malformed attributes to all connected routers"; the detection line now says "OSPF advertisements from unexpected hosts and unusual updates from iBGP neighbours". The OSPF "adjacent network" wording is supported by the advisory's CVSS vector (AV:A in the Fortinet CSAF).
- Fortinet F11: pointer fixed ("the update below"), the section sentence about the entry's earlier wording is gone; residue in the sourcing_note and one phrase in the section (F11 below).
- Declined items (Apache priority, pre-window KEV additions, Entra ID and ScreenConnect product links, over-bound Publica and eMudhra analyses): not re-raised. `kev_window_diff` and a live KEV read (catalogVersion 2026.11.10, count 1779) show no addition newer than the covered ones.

### Citation does not support the claim

#1 (F3) `2026-11-12/screenconnect-sckit-toolkit-pushed-to-hundreds-of-endpoints`, body paragraph 2, claim 8a38f15ec2: "ConnectWise had not identified an initial access vector, suspects the actor used independent third-party extensions that partners may have added, and disabled five (...) in about 400 partner environments; on-premises customers must disable them by hand ([BleepingComputer, 2026-11-11])". BleepingComputer (extract and raw HTML) has the suspected extensions, the five names, "approximately 400 partner environments" and the on-premises note, but nothing in it says ConnectWise had not identified an initial access vector (searched "initial access", "access vector": no hit); its only access statements are Huntress's ("Huntress has not determined how the attackers are gaining access to affected MSP environments"). The clause is in Huntress's Background paragraph: "ConnectWise shared that they had identified five independent third-party extensions ...; they said that they had not yet identified an initial access vector and full scope of the attack." Cite Huntress for that clause (or split the sentence) and adjust the sourcing_note line that attributes all ConnectWise statements to BleepingComputer's quotes.

### Quantifier without source

#2 (F14) `2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail`, summary tail ("...left to migrate or wait; no Fortinet page states exploitation.", claim c887390892) and body paragraph 1 ("The advisories withheld until Patch Tuesday were published on 2026-11-10; no Fortinet page states exploitation, and NCSC.ch listed the status as unknown", claim f8becb1af9). The entry cites FG-IR-26-175 (CVE-2026-104286, 'Known Exploited: Yes'): "This has been reported to be exploited in the wild, customers are urged to apply the workaround below", and the body's last sentence of that block says the FortiMail builds "also fix the exploited CVE-2026-104286". All 19 advisories of 2026-11-10 show 'Known Exploited: No' (read from the raw HTML of each), so the supportable claim is the scoped one. Iteration 3 asked for the scoping in the summary and the body; it was applied only in the 2026-11-11 section. Reword both places to "none of the 2026-11-10 advisories states exploitation".

### Editorial / less-is-more flags (advisory)

#3 (F11) Chrome sourcing_note ("no CVSS score appears in the sources read"; "returned no record for the CVE when it was read") and PHP2Shell summary ("none of the three vendors reports an exploited case in what was read"): composition language; iteration 3 changed the Falcon instance only. Use "in the sources cited" / drop the clause.

#4 (F11) Fortinet sourcing_note: "The advisory feed is capped at 50 items and ordered by title, so the rows were collected from the advisory pages themselves" is pipeline process, not provenance; the 2026-11-12 section's "than the nine first listed, now shown above" narrates the entry's own earlier state. Cut the feed-cap sentence and say "ten further critical rows (CVSS 9.0 or higher) are listed above".

#5 (F11, low confidence) ScreenConnect sourcing_note "could not be read on any transport" (fetch-pipeline vocabulary) and actions[0] "disable the five named extensions starting with RMM+ versions 1.0.31 and 1.0.32, which accept a blank access key" (reads as if the five extensions begin with those versions).

### Missed angles

None to raise. The last two days of NCSC.ch hub posts (13163 N-able, 13165 Chrome, 13167 SAP, 13169 Patch Tuesday) all map to covered entries; KEV catalogue unchanged since 2026.11.10; searches for Swiss communal incidents and further 2026-11-11 exploited-flaw items surfaced nothing in-window beyond what the store carries. Coverage looks complete for the critical/high signal I can name.

### Other checks with no finding

- All 19 Fortinet cves[] ids, CVSS scores and attack types match the advisory pages (CVE-2026-126263 summary says authenticated, metadata unauthenticated, as the entry states; CVE-2026-126229 and -126254 are the two 'Authenticated' rows, listed admin-required and post-auth). The four 'Impact: Denial of service' mismatches named in the sourcing_note (202, 207, 216, 219) are real.
- Apache: project page (critical, 2.4.55 to 2.4.70, mod_h2 2.0.8 to 2.0.42, 2.4.71 on 2026-11-11), Red Hat (9.8, unauthenticated, HTTP/2 only, "public research has demonstrated a reliable exploit", separate allocator, RHEL 9/10 Important, RHEL 8 not affected), Wiz (no exploit at publication; patched "2.0.24 and newer" against its own 2.0.8 to 2.0.42 range), RHSA package names and Debian rows all hold.
- Plone: hotfix post, pre-announcement (including the "Zope's own port" caveat), CMFEditions advisory (9.8, PR:N, "A working proof of concept exists") and the three other Critical and one Moderate advisories match.
- GSocket and CCB: every cited statement, including Microsoft's "multiple unrelated threat actors", the 87.1 / 30.7 percent context sentence and the CCB's 1 February 2027 and 1 July 2027 dates, holds.
- Style: no em dash in reader-facing text outside a verbatim OpenJDK quote and the permitted section headings; no IOCs; no registry keys or field names in prose. Run record notes checked for truth: the six stray root files exist, the KEV and borderline-drop statements are consistent with `kev_window_diff`.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 3)

The two truth findings are small and local (one misattributed clause in ScreenConnect, one unscoped negative left in two places in Fortinet). Everything else in the iteration 3 deltas checks out against the live sources.

### Findings summary (machine-readable)

See `work/2026-11-12T0255Z-intel/verification.iter4.findings.yaml` (5 records: F3, F14, F11 x3).
