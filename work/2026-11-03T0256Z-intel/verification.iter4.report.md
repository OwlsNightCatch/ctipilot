**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-03T05:22:39Z · ended_at=2026-11-03T05:46:55Z · duration_seconds=1456

## Verification report — 2026-11-03T0256Z-intel (iteration 4)

Scope read: all eight updated entries in full with `git diff HEAD` for each, the run record, `entities/registry.yaml` (malware:c3rb3r-ransomware), every claim of the ledger (216 of 216 have a verdict row in `verification.iter4.claims.yaml`: 212 ok, 4 F3 low confidence). Every cited page was fetched this iteration (extract, `url`, `ncsc-csh post`, `cisa-kev`, `pdf`, WebFetch for Akamai x2, The Register, CISA alert, GitHub advisories and the Envoy and .NET advisories). The EUVD pages are a single-page app, so the three WS_FTP EUVD citations were read through the ENISA EUVD API records that carry the same text and vectors.

### Prior-iteration deltas (iteration 3 remediations)

1. Synology SA-24:20 date clause: deleted. SA-24:20's revision table (read in full) has rows 4 to 6 on 2024-11-26 and 2024-12-05, so Synology's "patched in December 2024" fits; the body, summary and record no longer assert a mismatch. Residual wording in the sourcing_note: see F11 below.
2. NetApp: the hotfix clause cites only the advisory data of revision 11.0 (`kb_rev_history` 11.0 20261103 adds 9.12.1P20HF1 and 9.13.1P21HF1; `updated_date` 2026-11-03); "public discussion" is dated 2026-10-21 and the rendered advisory page reads "NetApp is aware of public discussion of this vulnerability." Correct.
3. Synology Exposure: NCSC post 12960 states "Prerequisites: Network access to the DSM management interface"; the clause now cites it. Correct.
4. Synology and registry Cerber wording: BleepingComputer says "borrowed its name from a notorious Ransomware-as-a-Service (RaaS) ... that emerged in 2016"; 360 says "老牌勒索家族Cerber的一个变种“C3RB3R”". Both now appear, attributed. Correct.
5. Admiralty wording: gone from the SIMATIC and Synology sourcing notes. Correct.
6. Kernel Debian clause: gone from the 2026-11-03 section and record summary; the Debian tracker still lists trixie 6.12.113-1 (DSA-6568-1) and the (security) row 6.12.115-2, consistent with the analysis and cves[].fixed. Akamai's "A similar flaw exists when request socket migration is enabled…" is now quoted in kind in the analysis, section and record summary. Correct.
7. Declined items (Danfoss length, Vaud sentence count): unchanged, re-listed below as advisory.

### Citation does not support the claim

- #1 F3 (low confidence) `2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap`, Exposure line and Defender takeaway: "([Trend Micro, 2026-10-30](https://success.trendmicro.com/en-US/solution/KA-0024802)". The page reads "Last updated: 2026/11/02" and "Current Status as of Nov. 2"; the same entry cites this URL as 2026-11-02 elsewhere. Facts hold; relabel 2026-11-02.
- #2 F3 (low confidence) same entry, Quest clauses: "([Quest Software, 2026-10-28](...kb/4385046/...php2shell)". The KB carries Published Time 2026-10-21T09:58:20 and updates dated October 23rd, 27th and 29th; nothing is dated 2026-10-28. Content correct; fix the label.

### Claims missing inline citation

- #3 F5 (low confidence) `2026-11-01/vaud-school-it-support-platform-data-theft-teachers-pupils`, sourcing_note: "SRF, Le Temps and other outlets only relay the release." No SRF or Le Temps page is cited or in sources[]; a search found none. Cite or delete.

### Single-source items missing [SINGLE-SOURCE] flag

- #4 F12 (low confidence) `2026-08-13/cve-2026-58115-simatic-iot2050-node-red-unauth-root`: `verification: multi-source` while `cves[].status` carries `exploited` and the headline rests on VulnCheck's canary alone (the sourcing_note says so; The Register relays it). Consider `single-source`, or leave if the value is read as covering the vendor advisory.

### Editorial / less-is-more flags (advisory)

- #5 F11 (low confidence) Synology sourcing_note "points to its December 2024-era advisory SA-24:20": SA-24:20 revision 1 is 2024-11-05 and BleepingComputer calls it "a November 2024 security advisory".
- #6 F11 (low confidence) Synology Detection, Defender takeaway, actions[1]: ".L0CK3D extension" and "read-me3.txt" are file-name indicators (check 12); keep deliberately or describe generically.
- #7 F11 Danfoss main analysis about 740 words against the 550 bound (declined in iteration 3, acknowledged in the run record).
- #8 F11 Vaud routine incident keeps three sentences plus a takeaway (declined in iteration 3).

### Checked and found sound

Every other claim of the ledger: Synology (SA-26:13 and SA-24:20 tables, NCSC 12960 dated 2026-09-21, CERT-FR first and last version 2026-09-21, heise, 360 dated 2026-10-29 with 27 skipped directories, ChaCha8 and RSA-2048, BleepingComputer 380,000 Shadowserver count); PHP2Shell (Trend Micro table of 2026-11-02, Quest KB updates, NetApp revision 11.0 and the CVSS 4.0 9.2 scores, CISA dateAdded 2026-10-26 for both flaws); SIMATIC (Siemens SSA-834709, VulnCheck, The Register of 2026-11-02, CVE not in the KEV catalog 2026.10.30); kernel (linux-cve-announce, CIQ patched-kernel table with 2026-11-01 builds, AWS bulletin, CloudLinux, Fortinet FG-IR-26-188 with all six named products and no fixed build, Akamai fix list and "not aware of a public working exploit", Debian, Ubuntu tracker last updated 2026-10-30, Red Hat statement, NCSC-NL, Go team, Anthropic); Danfoss second-wave section (BleepingComputer, Guardian incl. Finland, Euronews, Tagesschau, CyberInsider, 20 Minuten, Sabcobel quotes) and the older claims I re-read (CERT-FR alert, NCSC 13054, AFP, Public Sénat, Le Monde, BFMTV, Forescout, Censys, Cooling Post, Dixell PDF, Blick); Vaud (vd.ch release, RTS, Inside IT); Brotli (Patchstack in full, Node.js advisory, CISA alert, Zscaler, ELLIO, Cisco, Palo Alto timeline of 2026-10-29, Broadcom, Envoy, .NET, Imperva, OpenSourceMalware, Tenable, Akamai inflate, Datadog, NCSC 13105); WS_FTP (EUVD API records, four GitHub advisories, NCSC 13128, heise fifteen CVEs and six critical, CSIRT Italia 6 critical and 3 high, KEV CVE-2023-40044 with known ransomware use).

Changelog contract (4c): every record's `updated_at` mirror, section heading, `fields` list and summary agree with the diff (no silent edit seen); the six `update` records carry genuine deltas and the two `improvement` records float nothing. Style: no em dash outside headings, no IOCs beyond F11 #6, no workflow vocabulary in reader-facing text. Priority and classification calibration look right for all eight. Missed angles: two searches (in-window exploited vulnerabilities, Swiss public-sector incidents of 2026-11-02) surfaced nothing I can evidence as missing; coverage looks complete for the window.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 2, advisory: 4). All truth and editorial items are low confidence and small; the page facts themselves held everywhere I checked.

### Findings summary (machine-readable)

See `work/2026-11-03T0256Z-intel/verification.iter4.findings.yaml`.
