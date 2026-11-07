**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-07T06:55:16Z · ended_at=2026-11-07T07:13:13Z · duration_seconds=1077

## Verification report — 2026-11-07T0256Z-intel (iteration 7)

Scope: the 10 changed claims; every claim of the Danfoss, Brotli, Oneconsult and ARTEX entries (59); the OpenSSH entry (its Previdian finding was the declined one); a random 44-claim quarter of the other 178 (seeded sample, drawn from SIMATIC, WordPress, Cisco ESA, OpenSSH, SonicWall, BOSSAI, Kaspersky, Aargau, TUM); the run record read in full (notes claims checked against `sources.json`, the entries, `source_health.json` and the backlog). 121 claim rows written, 0 unreadable. Fresh fetches this iteration: Siemens CSAF for SSA-443410, SSA-045512 and SSA-834709, Mitel MISA-2026-0010, Cisco node-js advisory (version 1.8), SonicWall PSIRT API JSON, OX Security feed, Previdian page, NCSC Security Hub posts 13054 and 13155, NCSC-NL 0282 and 0368, CISA KEV JSON; the gate's saved bodies for the remaining pages.

### Prior-iteration deltas, checked against the sources
- Danfoss / Unit 42 (F3): confirmed fixed. Unit 42 Figure 1 is "internet exposed devices by country, top 10 results - Nov. 5–6 2026" (over 5,000) and Figure 2 is "internet exposed devices in France by date since Oct.1, 2026" (1,853 / 558 / 316); section and record summary now separate them. No new defect.
- Brotli Exposure line (F3): confirmed fixed; the wording matches Cisco's "Impacted Products with Software Fixes" table, which has no CVE column. No new defect; title, headline, summary, `affected`, Exposure now agree.
- Oneconsult reporter (F3): confirmed fixed; page: "The bypass has been reported to Google. Google has made the issue public". Trimmed "in July 2026" is carried by the sourcing note ("its own tests in July 2026"), page: "tests conducted in July 2026".
- Brotli title (F11): confirmed fixed and accurate: Siemens CSAF lists six released fixes and "Currently no fix is available" only for Common Configurator (CC on IEM, CC on Edge); Mitel: update planned, none released for all seven products. The trimmed example configurator versions are in `cves[].fixed` and match the CSAF (V3.0.18, V1.15.1, V1.24.3, V4.0.1, V1.5.7, V2.3.10).
- OpenSSH / Previdian date (F11, declined): decline accepted. The page carries a visible "Updated 07 Nov 2026" and still reads 15 attempts, 10 IPs, 8 countries, first 06 Nov, last 07 Nov; the entry states the figures as read on 2026-11-07; quoted caveat sentence is verbatim.
- Run record DR labels (F11): confirmed fixed; `deepread.DR1-3.yaml` and DR1-3 stamps exist, notes name them.
- ARTEX fake wins (F11): confirmed fixed in the section ("honeypots, decoys, tarpits and fake wins reduced the attack traffic reaching real assets"); residual wording nit in the record summary is finding #2 below.

### Editorial / less-is-more flags (advisory)
1. (low confidence) Danfoss section 2026-11-07, paraphrase drift against NCSC post 13054 ("across all relevant operations"; remote access "only"; record summary "any cooling plant") and against Ransom-ISAC (the "script or bulk-programming" reading is for the 588 writes at 1.6 writes per second, not the 155).
2. (low confidence) ARTEX record summary says controls "cut" attack traffic; Microsoft: "helped reduce the attack traffic reaching real assets".
3. (low confidence) Brotli: "revised daily" (three places); Cisco revision table shows nine versions 2026-10-27 to 2026-11-06 with no revision on 10-31, 11-01, 11-03.
4. (low confidence) Brotli: SSA-045512 V1.2 also lists Gridscale X DSA and Gridscale X PSS(R)E as affected with fixes; the entry's Siemens scope omits them without saying so.
5. (low confidence) Run record notes: "reduced-confidence inclusion: none. Included at reduced confidence ... BOSSAI and Kaspersky GERT" contradicts itself; ARTEX main analysis (726 words) is over the 550-word bound like Danfoss (711) but only Danfoss is named; both unchanged by this run's appended sections.

### Missed angles
None evidenced. The only in-window KEV addition (CVE-2026-19868) is covered; NCSC Security Hub posts 13157 (SonicWall GMS, 2026-11-06) and 13155 (OpenSSH) are covered by the 2026-11-05 entry and the OpenSSH entry; two generic searches (exploited advisories of 2026-11-06; Swiss communal incidents of 2026-11-06) surfaced only out-of-window or already covered items (N-able N-Central AL-2026-118 is dated 2026-09-09 and covered). Coverage looks complete for the critical/high signal.

### Verdict
CLEAN (truth: 0, editorial: 0, advisory: 5). Every advisory item is a wording nit the main agent may leave; none changes a decision a reader takes.

### Findings summary (machine-readable)
See `work/2026-11-07T0256Z-intel/verification.iter7.findings.yaml` (5 records, all F11, all marked low confidence).
