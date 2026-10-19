**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T16:59:10Z · ended_at=2026-10-11T17:15:34Z · duration_seconds=984

## Verification report — 2026-10-11T1307Z-audit (iteration 3, slice s5)

Scope: 10 entries (GLPI CERTFR-2026-AVI-0551, Spring CVE-2026-40982, Dirty Frag, Apobank court case, Exchange CVE-2026-42897, Ghost CVE-2026-26980, NCSC-CH week 23, Liechtenstein VwbP, Plugin4Shell, Virtualizor). Role: post-fix pass after a NEEDS_FIXES iteration 2. All 201 ledger claims have a verdict row (196 ok, 4 F4, 1 F5; the other findings attach to text outside the ledger or to claims already answered ok). Every cited page was fetched in this iteration (cached extract bodies where present, otherwise `extract`/`url`, `ncsc-csh post` for 12547 and 12577, `cisa-kev` for the KEV date, the CVE record API for the Dirty Frag scores, the FIRST EPSS API with date parameter, GitHub release pages for the Ghost fix date). No WebFetch or jina was needed.

### Prior-iteration deltas walked (23 findings)

| Delta | Verdict on the remediation |
|---|---|
| F7 Virtualizor (declined) | Rationale fails. See F7 below. |
| F18 Spring action | Holds: `actions: []`. But the record summary still says "one action covering every branch" (new F4 below). |
| F4 Ghost record summary | Holds: now "unauthenticated arbitrary database read", which Ghost, XLab and BleepingComputer state. |
| F4 / F13 Liechtenstein | Headline and takeaway fixed and the shutdown sentence now quotes the government's reason (presseportal 100941500). The same unsourced Swiss nexus survives in two other sections (new F4 below). |
| F9 Apobank | Holds: the contradiction line matches heise (login through the favourites bar) and Borncity (QR code to a manipulated page). |
| F11 Ghost sourcing_note | Holds: clean provenance. |
| F11 Liechtenstein (declined) | Stands as advisory; three takeaways remain. |
| F7 NCSC-CH week 23 (declined) | Accepted: home-region national-CERT review, one transferable malware chain, 230 words. |
| F3 Plugin4Shell | Holds: the section now follows THN ("not exposed to the branch-name variant", Gemini not established as safe). |
| F3 / F5 / F4 Exchange (Russia-aligned, May blog cite, event_date) | Hold: Proofpoint says "Russia-aligned"; the Exchange Online sentence cites the May blog ("Exchange Online is not impacted"); event_date 2026-05-14 matches MSRC "Released: May 14, 2026" and the blog's datePublished. |
| F11 Exchange 2026-08-30 section | Holds: plain language, no rating codes. |
| F3 x3, F4, F5, F18, F11, F1 Dirty Frag | All hold against V4bel README/write-up, Aikido, Red Hat, Microsoft, Ubuntu, NCSC-CH 12547 (hub URL form), CVE record scores (8.8 CNA / 7.8 CISA-ADP; 7.8). |
| F11 GLPI x2 | Hold: takeaway grammatical; all seven GHSA pages carry CVSS 4.0 scores 5.1, 8.4, 7.0, 8.4, 7.1, 7.0, 5.9, matching `cves[]`. |

### Claim ledger

All per-CVE scores, versions, dates, quotes (evidence[] quotes and their `original:` fields checked against presseportal, NZZ, Inside IT, Exxpress, MSRC, Proofpoint, VulnCheck, AIR, XLab) and cited statements in the 10 entries were checked against the pages. Verdict rows: `verification.iter3.s5.claims.yaml`.

### Citation does not support the claim (F3)

- **#1** `2026-05-18/cve-2026-42897-...`, title: "mitigation must be removed by hand" (low confidence). MSRC: mitigations "can be removed after July 2026 update is installed"; June blog "if you choose to remove mitigations"; July blog "you should". Fix: "the update does not remove the mitigation".
- **#2** same entry, Update 2026-07-31: "which Microsoft tracks as Void Blizzard" cited to Proofpoint (low confidence). The Proofpoint page lists "TA488 (Void Blizzard, Laundry Bear)" and never says who tracks it.

### Unsupported / hallucinated facts (F4)

- **#3** `2026-05-09/cve-2026-40982-...`, record summary of this fire: "one action covering every branch". The file reads `actions: []` (iteration-2 remediation emptied it). Fix: revise this fire's record summary.
- **#4** Exchange headline/summary: "outlives the patch" / "survives patching" (low confidence). Proofpoint: persistence "requires deliberate removal"; credential rotation and re-imaging will not evict. Patching is never mentioned.
- **#5** `2026-08-04/liechtenstein-...`: "lands in the inboxes of Swiss and European trustees and advisers" (Update 2026-08-05) and "for Swiss fiduciaries, trustees and banks, both jurisdictions' registers reach the same client population" (Update 2026-09-02 takeaway), low confidence. The iteration-2 F4 was fixed in the headline and main takeaway only. Government release 2026-08-04: the Amt informs the legal entities, which inform the beneficial owners; no cited page names Swiss or EU administrators.
- **#6** same entry, "the Federal Council's 2025 proposal" / "the 2025 count" (low confidence). NZZ 2025-06-13: the Council of States approved the register "im vergangenen Dezember", so the proposal predates 2025, and the 500,000 is a projection, not a count.

### Claims missing inline citation (F5)

- **#7** Spring Defender takeaway: "because Config Server normally sits inside the service mesh" (low confidence). HeroDevs: "sometimes deployed on internal networks".

### Drop (F7)

- **#8** `2026-09-23/virtualizor-...` (low confidence; iteration-2 finding stands). The decline says the entry "already reads as a short patch-cycle item". The body is about 880 words of code-path detail for an item the fire's own record rates routine, unexploited, fixed since 2026-09-01 and outside the constituency's estate. Cut to two to four sentences or drop.

### Surface contradiction (F9)

- **#9** Ghost record summary "The fix shipped on 2026-02-16" (low confidence). Ghost release 6.19.1 and the advisory carry 2026-02-16; the cited BleepingComputer says "released on February 19" and XLab "publicly disclosed as early as February 19". Not surfaced.

### Editorial / less-is-more flags (advisory, F11)

- Dirty Frag: the cited EPSS URL has no date parameter and returns 0.0247 / 0.0226 today; the entry's 0.9324 / 0.9286 are the 2026-09-04 values (time series confirms; drop on 2026-09-24). Cite the dated URL or refresh the field.
- Exchange: headline "Russian espionage actor" vs Proofpoint "Russia-aligned"; six em dashes in reader-facing sections edited this fire.
- Liechtenstein: three takeaways coexist (one labelled "(updated)"); em dashes in summary, sourcing_note and seven body places; "In the entry's assessment"; Inside IT cited as 2026-10-06 while datePublished is 2026-10-07T19:38:30Z.
- Plugin4Shell: `sectors: [public-sector]` is on none of the four cited pages.
- Virtualizor: an internal record changes a factual statement of the main analysis ("none exists" to "none demonstrated"); two em dashes in the takeaway.
- Ghost: T1491.002 (External Defacement) mapped to silent script injection; systemic: non-internal record summaries narrate metadata their sections do not state.

### Action-item discipline (F18)

- **#10** Virtualizor actions[0] (low confidence): a "patch ... now" do-now task on an entry rated routine and outside the estate, restating the takeaway. Empty actions[].

### Missed angles

None raised for this slice. The slice's entries are all in-window or legacy rewrites; the run record's coverage telemetry is slice s6's scope.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 4, advisory: 6)

The only finding I hold with full confidence is the Spring record summary (#3, a record statement the file contradicts). The others are marked low confidence and are small; the F7 on Virtualizor is a re-raise because the decline rationale does not match the entry.

### Findings summary (machine-readable)

See `work/2026-10-11T1307Z-audit/verification.iter3.s5.findings.yaml` (16 records: F3 x2, F4 x4, F5, F7, F9, F18, F11 x6).
