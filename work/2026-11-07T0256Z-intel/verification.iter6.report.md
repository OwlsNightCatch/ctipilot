**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-07T06:34:05Z · ended_at=2026-11-07T06:52:25Z · duration_seconds=1100

## Verification report — 2026-11-07T0256Z-intel (iteration 6)

Scope walked: all 15 changed claims, every claim of the four remediated entries (Brotli 19, Cisco SEG 37, OpenSSH 26, Oneconsult 18) and, beyond the required quarter, nearly every claim of the remaining nine entries (35 drawn at random, seed 61107, then the rest of IoT2050, ARTEX, WordPress, SonicWall, BOSSAI, Kaspersky, Aargau, TUM and the Danfoss 2026-11-07 section and record read against cached pages). 236 of 237 ledger claims have a row in verification.iter6.claims.yaml (232 ok, 4 F3); the one omitted claim is the Danfoss entry summary (97e7bde6d4), whose older sentences come from earlier fires and were not re-read here (its last sentence, NCSC edit and the Ransom-ISAC 743 writes, was). The run record's notes were read in full and its checkable statements tested against the KEV catalogue, sources.json, the source-health log and the work directory.

### Prior-iteration deltas (iteration 5 findings, re-verified against live pages)

1. Brotli Cisco wording (F3): title, headline, summary and cves[].affected now say Cisco lists Duo Network Gateway and RoomOS in its combined advisory; the page (version 1.8, 2026-NOV-06) still has one "Impacted Products with Software Fixes" table for four CVEs and no CVE column. The Exposure line was NOT hedged the way the remediation record says (finding #2 below).
2. OpenSSH Previdian (F3): previdian.com/CVE-2026-123158 read in this iteration: "15 exploitation attempts, 10 unique attacker IPs, and 8 countries ... First observed Nov 06, 2026; last observed Nov 07, 2026", "Updated 07 Nov 2026", "Not in CISA KEV"; raw HTML timeline "05 Nov 2026 17:30 UTC Public PoC available". Section, summary, record summary and the evidence quote ("Previdian sensor observations are exploitation attempts ... or that the attempt succeeded.") match. The dropped first-observation time is consistent with the page (timeline 06 Nov 00:05, table 09:53). Confirmed fixed.
3. Cisco SEG Triage (F8): the Triage line now carries the S/MIME caveat. PR 22024: "the ECS SQLi (i.e. this module) was the only one that generated this matching IOC"; PR 22018 doc: "this appears to be CVE-2026-76443 rather than CVE-2026-76461 based on the IOCs available for CVE-2026-76461". Confirmed.
4. Brotli tags/status (F11): exploited and actively-exploited added; sourcing note says the status rests on CISA's listing and Cisco reports no malicious use (CISA alert of 2026-10-27 read via WebFetch: "based on evidence of active exploitation"; KEV dateAdded 2026-10-27). Confirmed.
5. Brotli summary Cisco clause (F11): now "among its products with fixes, a longer list of which is dated up to 2027"; the table dates belong to other products. Confirmed.
6. Brotli takeaway split (F11): confirmed; Siemens SSA-443410 attaches the uninstall mitigation to Common Configurator on IEM and "Stop Common Configurator on Device" to the Edge variant.
7. Run record "either module" (F11): confirmed.
8. Oneconsult regions (F11): regions is [global]. Confirmed.

### Citation does not support the claim

**#1** `2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack` (section 2026-11-07T03:53:29Z, claim 122cc2adfd; record summary, claim 076bf0c907): "Unit 42 counts over 5,000 internet-exposed devices from the manufacturers CERT-FR names on 5 and 6 November, with 1,853 in the first half of October, 558 in the second half and 316 in the first six days of November". Unit 42 (https://unit42.paloaltonetworks.com/europes-refrigeration-systems-attacks/) has two series: Figure 1 "Graph of internet exposed devices by country, top 10 results - Nov. 5-6 2026" (over 5,000; France 234) and Figure 2 "Graph of internet exposed devices in France by date since Oct.1, 2026" (1,853 / 558 / 316). The section joins the France-only trend to the multi-country total, and the record summary says "over 5,000 exposed devices with a falling trend". Fix: state that the trend is France and the 5,000+ is the 5-6 November count across countries.

**#2** `2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo` (body Exposure line, claim 9839bd780e): (low confidence) "or a Cisco Duo Network Gateway or RoomOS device below the builds above" still asserts exposure to this flaw; Cisco's advisory says "Cisco is investigating its product line to determine which products may be affected by these vulnerabilities" and its single table covers four CVEs. The run record says the Exposure line now states the combined-advisory qualifier; it does not. Fix: "a Cisco Duo Network Gateway or RoomOS device that Cisco lists in its combined advisory, below the builds above".

**#3** `2026-11-07/file-system-access-api-browser-persistence-chrome-edge` (body, claim 909cb607a5): (low confidence) "Oneconsult says it reported the issue to Google, which made it public"; the page says "The bypass has been reported to Google. Google has made the issue public" without naming the reporter. Fix: "notes that the bypass has been reported to Google, which made the issue public".

### Editorial / less-is-more flags (advisory)

**#4** Brotli title and headline: "Mitel and Industrial Edge fixes are still planned" / "fixes pending". (low confidence) Siemens SSA-443410 lists released fixed versions for six Industrial Edge applications and says it "has released new versions for several affected products" and "is preparing further fixes"; only Common Configurator has none. Body is right, title over-generalises.

**#5** OpenSSH Previdian citation date 2026-11-07: (low confidence) JSON-LD datePublished is 2026-11-05T15:46:26Z, dateModified 2026-11-06T09:54:00Z; the visible "Updated 07 Nov 2026" supports the date and the entry says "as read on 2026-11-07". Left to the main agent.

**#6** Run record notes: (low confidence) "FU1 to FU3" are the work directory's DR1 to DR3 (identical start and end stamps); the notes do not say so.

**#7** ARTEX section: (low confidence) "tarpits and decoys that present convincing evidence of success" attaches the fake-win property to tarpits and decoys; Microsoft's testing sentence covers "these controls" together.

### Checked, no finding

- Cisco SEG (37 claims): Cisco SEG advisory (v1.2, mail_logs, TAC case, 15.5.5-014 footnote, Cloud 16.5.0-780), hardening advisory (v1.1, five CWE groupings, footnotes, fixed tables), NCSC-NL (original Dutch literal), KEV (dateAdded 2026-09-14, forensicTriage Yes), PR 22024 and 22018 (pages, .diff, mergedTime 2026-11-05T19:41:01Z and 2026-10-28T01:47:42Z), Rapid7 wrap-up of 2026-11-06. Evidence quotes are literal. The edited 2026-11-04 section is declared by the `body` field. Note PR 22018's module carries `IOC_IN_LOGS`; its description and the author's attribution statement still support the "no mail_logs pattern" reading.
- Brotli (19): Siemens SSA-045512 V1.2 (Desigo CC V8, V9), SSA-443410 V1.1 (six fixed apps, Common Configurator no fix, "No Management Applications installed: No action is required"), Mitel MISA-2026-0010 rev 5.0 (versions, KB000129034/100/114, note 1, 8.1), Cisco v1.8, CISA alert and KEV record.
- OpenSSH (26): NCSC hub 13155 (via ncsc-csh), OpenSSH release notes, OX Security (read from its feed), heise, Alpine advisory, The Hacker News.
- Oneconsult (18): article (JSON-LD datePublished 2026-11-02) and Oz write-up; regions now [global].
- Other entries: IoT2050 (SSA-834709 V1.1 raw table with four variants and order numbers, CERT-FR and NCSC-NL list Advanced only, VulnCheck, The Register), Danfoss section (NCSC hub 13054 edit reason and checklist, Ransom-ISAC figures, CERT-FR steps), ARTEX (Microsoft 2026-10-21 and 2026-11-06, Check Point, Expel), WordPress (THN, Picus, Wordfence, Patchstack, wordpress.org), SonicWall (PSIRT API JSON: seven CVEs, CVSS, affected and fixed builds, no workaround; BleepingComputer; CISA), BOSSAI (Acronis TRU), Kaspersky (Securelist, "No VM escape was required."), Aargau (ag.ch communiqué, Netzwoche), TUM (notice status 06.11.2026 12:20, heise).
- Style: no em dash outside `## <Type> — <at>` headings, no IOCs, no pipeline vocabulary in any entry field; run-record claims about KEV dates (Plex 2026-10-20, SiteGuard 2026-10-20, four old CVEs 2026-08-26), 298 sources, shadowserver `max_staleness_days: 120` and ec-presscorner-api `general-news` hold.
- Missed angles: none found. Microsoft's 2026-11-05 exposed-secrets post is covered by `2026-11-06/exposed-app-credentials-entra-signins-msp-clients-artex`; the only in-window KEV addition is CVE-2026-19868 (covered); two WebSearch sweeps found no dated in-window item the run lacks. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 4)

The Danfoss Unit 42 figures are a confirmed splice of two Unit 42 series; the other two truth items are low confidence and a clause each.

### Findings summary (machine-readable)

See work/2026-11-07T0256Z-intel/verification.iter6.findings.yaml (7 records).
