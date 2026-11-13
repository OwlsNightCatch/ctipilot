**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-13T05:15:41Z · ended_at=2026-11-13T05:30:54Z · duration_seconds=913

## Verification report — 2026-11-13T0256Z-intel (iteration 3)

Scope walked: all 17 claims in claims.changed.iter3.yaml, every claim of the ten entries remediated in iteration 2 (Citrix, WFX Phantom, Confluence, Check Point, Brotli/Desigo, Huntress, SignDrop, DarkLunnen, Microsoft .NET, Apache httpd), and a random quarter (38 of 149, seed 20261113) of the remaining claims (N-able, Trend Micro PHP2Shell, ANSSI, ScreenConnect, PTC, Dixell); the six remaining entries were also read end to end. 266 rows in verification.iter3.claims.yaml (263 ok, 2 F3, 1 F4). Pages were fetched this iteration (extract, raw HTML, CSAF/CVE API, saved bodies for the Citrix, Apple, Siemens-cached, Group-IB, Cyderes and Apache sets).

### Prior-iteration deltas (all 15 items re-read against the cited pages)
1. Citrix colliding-id sentence: removed from the body; EUVD-2026-102489 is out of sources[]; the seven collisions (CVE-2026-111343 to 111349) are real (CVE API: pig, APITable, Trudesk, ZenTao, go-ldap-admin, Likeshop, Craftplan). Correct.
2. WFX 63,000: StepSecurity now closes that clause ('As of 07:40 UTC on November 12, GitHub search returns more than 63,000'). Correct.
3. Confluence 'out-of-cycle': gone from the summary. Correct.
4. Brotli Apple 149717 and 149723: pages list AirPlay, Bluetooth, CoreUtils x2, MediaRemote, rapportd (iOS 18.7.12) and AirPlay, Bluetooth, CoreUtils (watchOS 26.6.1); no brotli entry, no CVE-2026-111497. Correct.
5. Check Point PhiliKit/UNC5221 lineage and the attribution caveat: CPR key findings state both. Correct.
6. BroadWorks (declined): the KEV catalogue (fetched) dates CVE-2026-20320 2026-11-10, outside the 26 h window; the run's kev-window reports 0 additions. Not re-raised.
7. Citrix priority high (declined with facts): facts now in the body (no exploitation, no PoC, DoS-class wording, new monthly release program per heise). Judged a defensible call (unauthenticated, default-configuration, internet-facing gateway row scored 9.3 by the vendor); not re-raised.
8. HomeView in cves[] affected and fixed, Apple entity keys in entities[]: present and correct (page 149851, released 2026-11-12).
9. Huntress T1557 and T1684.001: both in techniques[] and in Huntress's ATT&CK table. Correct.
10. SignDrop 'does not ship in that directory': consistent with Cyderes. The same line now carries a new defect (F3 #1 below).
11. Citrix heise: in sources[] and cited; text matches heise.
12. DarkLunnen cisa-kev tag: removed; tags now vulnerabilities, actively-exploited. Correct.
13. Confluence 'likeliest' clause: removed from the Exposure line. Correct.
14. .NET KBs: MSRC affectedProduct data (fetched) matches every KB, build pair, PowerShell 7.4 to 7.6 and Visual Studio 2017 to 2026; '(ESU)' gone; Microsoft PowerShell in affected_products. Correct.
15. Apache: Ubuntu 20.04 labelled ESM (USN-9090-1: 2.4.41-4ubuntu3.23+esm11); mod_h2 2.0.43 per the researcher repository ('Fixed in: httpd 2.4.71 · mod_h2 2.0.43'). Correct.

### Citation does not support the claim
- #1 F3 signdrop-windows-clfs-authentication-lpe-public-poc-no-patch (claim 9eab64e809). Entry: "file-creation telemetry for hid.dll in the ink directory, which Cyderes ranks highest because the file does not ship in that directory". Cyderes (https://www.cyderes.com/howler-cell/signdrop-zero-day): "Two of these carry the most signal today. A hid.dll creation in the ink directory and a Defender signature update RPC call from outside the Defender service tree are both rare enough in a typical estate to alert on rather than hunt." Table 2 carries no ranking. Fix: say Cyderes counts it, with the signature-update RPC call, among the two highest-signal observables.
- #2 F3 (low confidence) citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws (claim 765b9ac95b). Entry: "Where a logout had occurred, /var/log/httperror.log can hold authentication material (one of the rows), so limit who can read that file and support bundles" cited to CTX697305. The CVE-2026-111348 row says only "Local read access to /var/log/httperror.log on an appliance where any logout had occurred"; the bulletin never mentions support bundles. Fix: drop "and support bundles" or label it an inference.

### Unsupported / hallucinated facts
- #3 F4 (low confidence) wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens (claim 4dc93a7c16). Triage line: "the payload ran where a commit with one of those messages is paired with a deleted run". StepSecurity: "A missing run means the stealer probably ran." and "The gap is the most reliable sign that the stealer ran." The hedge is dropped. Fix: "probably ran".

### Editorial / less-is-more flags (advisory)
- #4 F11 darklunnen-group-ib-fortios-super-admin-swiss-scan-list sourcing_note: "after the previous sweep of this publisher" and "is described in earlier entries" are workflow-internal and store self-references in a reader-facing field.
- #5 F11 cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo: the Exposure line lists no Apple device although the headline and Defender takeaway name the Apple releases.
- #6 F11 citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws sourcing_note: "the row text identifies those rows" refers to a body sentence removed in iteration 2; nothing now identifies the seven omitted rows.
- #7 F11 (low confidence) confluence-dc-cve-2026-90436-apache-axis-remote-api-rce summary: "which it is not by default" drops Atlassian's "for new installations" qualifier (the body keeps it).
- #8 F11 (low confidence) wfx-phantom headline: "cloud persistence survives rotation" is stated as fact; StepSecurity and Endor say the stealer "tries to" and is "designed to" outlast rotation.
- #9 F11 (low confidence) check-point-php2shell-sk1000302-portal-and-vpn-gateways sources[]: the CISA KEV record is dated 2026-10-28 while the KEV feed's dateAdded for both PHP CVEs is 2026-10-26; it is also not cited inline.

### Checked and not flagged
- Citrix: 28 rows, nine scored 9.0 or above (eight 9.3, one 9.5), ten with VC/VI/VA High (CERT-EU), cves[] scores match the bulletin table row for row (CVE-2026-120862 reads 'CVSS v4.0: 8.7'), Console 9.4 adjacent (bulletin) versus 9.3 network (EUVD and CVE record), no Citrix CVE in the KEV feed (fetched, catalogVersion 2026.11.10), heise monthly-release statement, NCSC UNKNOWN.
- WFX: Aikido 4,837 accounts and 1,835 repositories, Endor 8,926 repositories (change log) and the verbatim 1,838-repository quote, BleepingComputer restating Aikido, Fly.io caveat, Aikido versus StepSecurity on forged status checks surfaced as a contradiction.
- Apache: Red Hat API (Critical 9.8; RHSA-2026:98981 and 98978), Debian tracker, Alpine, SUSE pending, Wordfence, researcher repository ASan/TSan evidence, Apache's own page (2.4.71 on 2026-11-11).
- Check Point: sk1000302 Jumbo takes, Spark builds, R81.10 hotfix; sk1000362 (7.8, couple of dozen customers, no take for R81.10/R81); CPR first and second wave, TSGA/TSProxy, PhiliKit, ESXi wiper.
- Huntress, DarkLunnen (datePublished 2026-11-11; 'Mass FortiGate Exploitation' is Group-IB's own heading), Fortinet FG-IR-24-535, .NET (blog, advisories 492/494/495, runtime 136445, Node.js, JFrog, MSRC revision 7), Siemens SSA-045512/443410 fixed versions, Cisco v1.12, Mitel rev 5.0, Apple pages, PTC (CNA record: eleven Windchill and ten FlexPLM lines), Dixell/VulnCheck, ScreenConnect (CNA record, The Record, Blackpoint), N-able CNA scores, Trend Micro status table (as of Nov. 12), ANSSI second report figures (64, 5, 25 of 30, VACAF 1.2 million, 60,000).
- Priority, classification, action discipline (no list over three, no generic action), style (no em dash outside section headings, no IOCs beyond source-listed hunt strings, no pipeline vocabulary in titles, headlines, summaries or bodies), run-record claims (7 new, 9 updated, counts 18/9/5 and 3/4/8 match the findings blocks, 18 stray root files exist, Saxony entry fully gone).
- Coverage: GPUStack (KEV 2026-11-09, SANS ISC 2026-11-12) was returned by the deep read as below the bar for this constituency and is outside the KEV window; no in-window Swiss public-sector incident found by two searches. Coverage looks complete for critical and high signal.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 0, advisory: 6)

### Findings summary (machine-readable)
See verification.iter3.findings.yaml (9 records).
