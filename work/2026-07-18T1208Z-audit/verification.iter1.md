**Model:** Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-18T12:45:57Z · ended_at=2026-07-18T12:56:00Z · duration_seconds=603
**Self-telemetry:** urls_checked=9 · webfetch_calls=8 · websearch_calls=0 · bridge_fetches=5

## Verification report — 2026-07-18T1208Z-audit (iteration 1)

Cold read of the three recovered entries + run record + audit report. Truth checks: every primary URL fetched (Searchlight slcyber, WordPress.org 7.0.2 release, both WordPress GHSA advisories, Kaspersky Securelist GoSerpent, Microsoft o365-moodle GHSA, The Hacker News; BSI and the Moodle GHSA CVSS confirmed via jina after the SPAs/sidebar defeated WebFetch). EUVD (both records) is a JS-only SPA that returned only an "Application Unavailable" shell to WebFetch and the bridge; its facts (contested CVSS inversion, 6.8.x SQLi reachability) are independently corroborated by THN and the two WordPress GHSA severity labels, so no finding rests on that unreachability. All 15 ATT&CK ids across the three entries are active in the pinned v19.1 dataset and their technique names match the described behaviors. All evidence[] quotes verbatim except as noted. Special-duty on-disk checks all hold (see § Special-duty).

### Unsupported / hallucinated facts

**F4 — WP2Shell entry: "detection-only PoC ... explicitly not a working RCE exploit" is uncited and contradicted by its own cited source. (truth)**
- Entry, summary: "a detection-only PoC repo is already public".
- Entry, body (no inline citation on the sentence): "A public GitHub repository already offers a detection-only proof of concept (time-based blind SQL-injection and route-confusion probing, explicitly not a working RCE exploit)."
- Cited source The Hacker News (fetched this iteration, exact wording returned twice): "Since Friday, the full mechanism has been published, and a working proof-of-concept has gone up on GitHub."
- The entry tells the reader the public PoC is explicitly NOT a working exploit and leads its summary with this as a reassuring qualifier; a cited source says a working PoC is public. Exploitation readiness is decision-relevant to the `high` prioritisation and the "exploitation expected short-term" framing. The entry resolves the conflict silently toward the less-urgent reading.
- Remediation options: (a) attribute the detection-only characterization to the specific repo the writer inspected AND add a `Contradiction:` line in § Verification Notes reconciling with THN's working-PoC report; or (b) soften the claim to match the cited sources (a working PoC is reported public). Do not leave the blanket "explicitly not a working RCE exploit" standing uncited against a cited source that says the opposite.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

One decision-relevant truth defect on the WP2Shell entry (F4). The other two entries (GoSerpent, Moodle local_o365) are clean: primaries fetched, all evidence quotes verbatim (incl. the BSI German quote, confirmed via jina), CVE ids/CVSS consistent with the owning advisories (WordPress GHSA rates CVE-2026-63030 Critical = 9.8 tier and CVE-2026-60137 Moderate = 5.9 tier, matching the entry's chosen WPScan-CNA scores over the disclosed CISA-ADP 7.5/9.1 inversion; Moodle GHSA rates CVE-2026-54733 Critical, consistent with 9.3 CVSS 4.0), ATT&CK ids active and correctly mapped, single-source flags correct, classification codes defensible, priorities calibrated (0 criticals is correct — no confirmed ITW exploitation on any of the three), no IOCs.

### Special-duty — audit-report claims verified on disk

1. **Recovered-entry paths + priorities:** all three exist; WP2Shell = `high`, GoSerpent = `notable`, Moodle local_o365 = `notable` — match the report. ✓
2. **Shipped fixes:** CHANGELOG head = v3.26 with the weekly citation-date + per-fact-attribution entry ✓; weekly-summary.md carries the v3.26 banner and the new Phase 4 bullet (line 176) ✓; sources.json carries the four described notes (enisa-euvd, kaspersky-securelist, ncsc-ch-incidents, searchlight-cyber) + the wordpress-org-news candidate ✓; registry carries malware:goserpent + actor:tetrisphantom with a sourced hedged overlaps-with edge ✓; cves_seen.json carries CVE-2026-63030, CVE-2026-60137, CVE-2026-54733 ✓.
3. **Verdict numbers:** truth-B{1..4}.yaml on disk = 14/2/0, 15/1/0, 15/0/0, 3/8/4 (B4 uses label `factual-error` with a hyphen — my first grep on `factual_error` mis-counted 0; the 4 factual-errors are present). 45 operational (14+16+15, B2's single imprecision resolved as a false alarm) + 3 weekly clean = 48/62 — reconciles. ✓
4. **Priority-calibration window row (0/17/44/1):** full 07-11→07-18 file range = 0 critical / 19 high / 52 notable / 1 routine; 0 criticals is exact, and the high/notable deltas (−2/−8) correspond to the pre-anchor 07-11 entries + the 3 recovered + post-cutoff 07-18 dailies excluded from the audited 62. Consistent. ✓
5. **Run records:** window = 16 records all publish_status: ok (full range shows 19 ok + 1 pending, the pending being this audit run itself) ✓; 5 confirmation_waived runs ✓; daily cadence gap_hours=24 across 07-16/07-17/07-18 dailies ✓.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "WP2Shell: pre-auth RCE chain in stock WordPress core (CVE-2026-63030 + CVE-2026-60137)"
  url_or_quote: "entry: 'explicitly not a working RCE exploit' (uncited) vs cited The Hacker News: 'a working proof-of-concept has gone up on GitHub'"
  summary: "Entry asserts the public GitHub PoC is detection-only / not a working RCE exploit, uncited and in both summary and body; its own cited THN source reports a working PoC public. Decision-relevant exploitation-readiness conflict resolved silently. Reconcile (source + Contradiction note) or soften to match cited sources."
```
