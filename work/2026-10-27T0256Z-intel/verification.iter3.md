**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-27T04:51:19Z · ended_at=2026-10-27T05:10:06Z · duration_seconds=1127

## Verification report — 2026-10-27T0256Z-intel (iteration 3)

Scope: post-fix pass. All 232 ledger claims have a verdict row (`verification.iter3.claims.yaml`; the 24 changed claims, every claim of the seven entries remediated in iteration 2, and also the rest of the ledger, since the cited pages were fetched anyway). Sources read this iteration: live Palo Alto PHP2Shell advisory page and JSON (revision timeline to 2026-10-27T04:03Z) and the Brotli advisory, CISA KEV 2026.10.26, CISA alert (WebFetch), php.net archive, CERT-EU, ENISA, Sansec, VulnCheck, Karimi report, SecurityWeek, BleepingComputer, Unit 42, CrowdStrike, Wordfence, Sophos, ISC 33452/33458, SRF, Blick, BACS, QNAP QSA-26-18 and statement, Synology, Apple 149225/149226/149228/149229, Wiz Gheist, GitHub changelog, Belden/Schneider/B&R/HMS PDFs, Wibu, Oracle, SecurityWeek OT roundup, Huntress, Yonhap, BleepingComputer ARTEX, Microsoft Storm-0940, Citrix Tech Zone and CTX697263, NCSC.ch 13105, Ubuntu, Node.js, Imperva, Envoy, .NET, EUVD.

### Prior-iteration deltas (all remediations checked against the live source)
- PAN-OS revision (F3/F4): CONFIRMED. The live advisory JSON timeline ends 2026-10-27T04:03Z ("Removed the ETAs for 12.1.7-h11 and 12.2.4-h1 as these versions are released."). The page table now shows exactly eleven builds without ETA (10.2.13-h27, 10.2.16-h12, 10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11, 12.2.4-h1) and nine with ETAs 10/27 to 10/30 (12.1.4-h13, 12.1.10-h3, 11.2.4-h23, 11.2.7-h23, 11.2.13-h4, 11.2.16-h1, 11.1.7-h12, 10.2.7-h39, 10.2.10-h42). Headline, summary, title, section, record summary, PHP body clause and cves[].fixed all agree. Two residuals below (actions[0] rationale; uncited ETA).
- QNAP ARM32 qualifier: CONFIRMED ("QVR Surveillance 3.0.3 and earlier (ARM32 models)Resolved QVR Surveillance 3.0.3.1756" on the live table).
- Camping.Care backport clause: CONFIRMED dropped; the CISA alert lists 8.5.12, 8.4.27, 8.3.36, 8.2.35.
- PHP "the one production victim the sources name": the quantifier is now fine, but the same clause says "Swiss booking-system supplier" (see F3 #1).
- Wibu anchor: CONFIRMED (id c61269 exists; the advisory is its own content element, last updated 2026-10-23 7:00 pm CEST).
- "Notes Station 3" prose spelling: CONFIRMED (QSA-26-18 says "Notes Station 3"); affected_products keeps "Note Station 3" by design.
- Gheist GhostAction reference: CONFIRMED (entry exists; Wiz: "Gheist is distinct from GhostAction").
- Roundup Schneider citation and sourcing_note: CONFIRMED (SESB-2026-295-01 v2.0.0 read page by page: "Version 1.48.4.0 of Security Expert includes a fix for this vulnerability").
- Run record "failing on every run since 2026-10-19": consistent with the counter.
- Summary length: PHP, Apple, QNAP, PAN-OS are three sentences each.

### Claim does not support the claim
- #1 (F3) php-critical-release-pre-announced-cve-2026-109618-109619, summary: "the one production victim the sources name is a Swiss booking-system supplier whose theft SRF links to the flaws without naming a CVE". Blick (cited in the entry): "Über das Buchungssystem der holländischen Firma werden unter anderem Reservationen für sämtliche Campingplätze des Touring Club Schweiz (TCS) abgewickelt." Camping.Care is Dutch; the Swiss party is its customer. The Camping.Care entry and the registry record say Dutch. Fix: "a Dutch booking-system supplier of TCS Camping".
- #2 (F3, low confidence) pan-os-panorama-php2shell-mgmt-interface-no-fixed-release, actions[0]: "...until its hotfix ships, due 2026-10-27 to 2026-10-30, because Palo Alto lists no other workaround." The advisory's Workarounds and Mitigations section lists Threat Prevention coverage ("Customers with a Threat Prevention subscription are provided with coverage against this vulnerability by enabling Threat ID 543004 ...", four conditions) and Frontier Virtual Patching. The entry's own Defender takeaway says "no workaround beyond that restriction and the Threat Prevention coverage". Fix: add the qualifier or drop the because-clause.
- #3 (F3, low confidence) gheist-stolen-github-tokens-secret-dumping-workflows, first paragraph: "On 2026-10-19 the second variant added a job for repositories with a self-hosted runner". Wiz: "On October 19, Tool B added echo X | base32 -w 120 between the dumps ... Hours later it pushed a second job, sync-host". Only the separator change is dated October 19; the job followed "hours later". Hedge the date ("on or just after").

### Claims missing inline citation
- #4 (F5, low confidence) pan-os entry, cves[CVE-2026-109618/109619].fixed: "11.2.10-h16 (11.2.10-h17, ETA 10/27, adds the Brotli fix)". The ETA 10/27 is on Palo Alto's Brotli advisory (">= 11.2.10-h17 (ETA: 10/27)"), which is not among this entry's sources; the cited PHP2Shell advisory only says 11.2.10-h17 includes both fixes. Add that source or drop the ETA.

### Surface contradiction
- #5 (F9, low confidence) cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi versus the PAN-OS entry. Brotli entry: "PAN-OS hotfixes 12.2.4-h1, 12.1.4-h13, 12.1.7-h11, ... (estimated 2026-10-27 to 2026-10-30)" and action 3 "until the hotfix ... is installed, due 2026-10-27 to 2026-10-30". The PHP2Shell advisory (timeline 2026-10-27T04:03Z) lists 12.2.4-h1 and 12.1.7-h11 as released and its FAQ says "the same hotfix covers both the PHP and brotli vulnerabilities"; the Brotli advisory (last revised 2026-10-26T23:40Z) still says "ETA: 10/28" for both. The Brotli entry is faithful to its own source, but the two entries now give two states for the same builds; add a Contradiction line.

### Editorial / less-is-more flags (advisory)
- #6 (F11) cve-2026-86950-apple-coregraphics-zero-day-kev, cves[].epss "0.01242" is the 2026-10-11 reading; FIRST's API returns 0.26166 (2026-10-26) and EUVD shows 26.17%. cves[] was rewritten by this run; refresh or null.
- #7 (F11, low confidence) pan-os entry: the section and record are stamped 2026-10-27T03:40:45Z but report the 12.1.7-h11 and 12.2.4-h1 release of 2026-10-27T04:03Z (record amended after the revision). Text is right; the stamp reads earlier than the event.
- #8 (F11, low confidence) run record, Coverage gaps: "community.citrix.com Tech Zone NetScaler post (403 on every transport ...)". `extract` returned the post this iteration through the reader fallback ("Last updated on: October 22, 2026", fixes planned for 2026-10-27, no shipped-fix statement), so the NetScaler claims are verifiable; whether the fixes shipped stays unconfirmed.

### Checks that held (no finding)
- Truth: every PHP body, section and record claim (CISA alert, KEV, Karimi report, SecurityWeek, BleepingComputer, VulnCheck extended builds, Unit 42 retraction, Sansec, CrowdStrike, SANS, Red Hat, vendor statuses of Citrix, Cisco v1.7, Fortinet, Splunk, Tenable, Siemens, WatchGuard, BACS, Inside IT, ReliaQuest, Basel-Stadt, Publica) matches the pages read. KEV lists both CVEs, vendorProject "PHP Group", dateAdded 2026-10-26. Apple 149225 lists iPhone XS, XS Max, XR, iPad 7th generation (and further devices already covered by 26.7.1); KEV names only 149226, 149228, 149229; SANS ISC 33458 confirms the iOS 18 delivery. QNAP table as of today matches the entry (QVR ARM32 3.0.3.1756, TVR OS 1.0.5 resolved; Notes Station 3 and QNE (ADRA) "Fixing"; QuMagie not listed; revision history ends V1.1 2026-10-24). Gheist, roundup (Belden image-read, Schneider image-read, B&R, HMS, Wibu, Oracle Rev 2, SecurityWeek), ARTEX (Yonhap Korean original, BleepingComputer), ConnectWise (Huntress), NetScaler (Tech Zone, CTX697263), Brotli (NCSC.ch 13105, Ubuntu, PHP Windows rebuild, Node.js release notes, Imperva, Envoy, .NET, EUVD) all match.
- Quotes in evidence[] checked by hand: the NCSC.ch "Proof of Concept Available" (the gate could not read it) is verbatim in post 13105.
- No IOCs, no em dash outside `## <Type> — <at>` headings, no workflow-internal language in reader-facing fields; headlines within 120 characters; Admiralty codes present and consistent; no org_triage or watchlist use; actions are task-shaped (Gheist artifact names stay by design).
- Missed angles: none found. WebSearch for Swiss incidents dated 2026-10-26/27 and for a NetScaler fix release surfaced nothing new; the KEV window holds only the two PHP CVEs. Coverage looks complete for the critical/high signal.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 2, advisory: 3)

### Findings summary (machine-readable)
See work/2026-10-27T0256Z-intel/verification.iter3.findings.yaml
