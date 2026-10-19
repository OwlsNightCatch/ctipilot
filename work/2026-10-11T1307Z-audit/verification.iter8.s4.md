**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T18:42:44Z · ended_at=2026-10-19T19:16:35Z · duration_seconds=2031

## Verification report — 2026-10-11T1307Z-audit (iteration 8)

Slice s4, post-fix pass. 26 entries read whole; ledger `claims.iter8.s4.yaml` walked in full: 241 claims in scope, 241 verdict rows written (all `ok`; no F3/F5/F13/F14 claim-level defect). The slice also owns the fire's own documents (audit report, CHANGELOG 4.20, run record), re-read against disk and git.

### Unsupported / hallucinated facts

1. F4 (low confidence), `docs/audits/2026-10-11-quality-audit.md` factual-errors table row 14 and the internal record `2026-10-11T13:44:58Z` in `entries/2026-09-24/openai-agent-australia-medicare-portal-breach.md`. Claim: "ACSC alert cited at an address that now answers 404" / "the old address answers 404". Live fetch this pass: the old cyber.gov.au address returned HTTP 200 with a body of the same size (1,541,402 bytes) as the new `/alert/...` URL and a canonical link pointing at the new address; a bogus path in the same directory returned 404. The re-point to the new address is still the better citation; the "answers 404" statement is what the fetch does not show. Fix in the audit report (reword to "moved; canonical now /alert/..."); the record summary is append-only.
2. F4, `prompts/CHANGELOG.md` section 4.20: "117 existing entries received a record from this fire: 102 corrections, 13 improvements and two updates, of which 25 are internal." Disk recount of every record carrying `run_id: 2026-10-11T1307Z-audit`: 117 entries; corrections 86 non-internal + 16 internal; improvements 5 non-internal + 8 internal; updates 2 non-internal. Internal total 24, not 25 (the Check Point record `2026-10-19T18:34:47Z` is non-internal and has its section). Change 25 to 24.
3. F4, `docs/audits/2026-10-11-quality-audit.md` fold table (the `| 1 entry each | the rest |` row): rows sum to 26 folded duplicates against 27 stated in the prose and the run record. The Oracle EBS CVE-2026-46817 survivor received 2 folded entries and is not listed as such. Add its row or restate the remainder so the table sums to 27.

### Editorial / less-is-more flags (advisory)

4. F11 (low confidence), PHP SOAP `entries/2026-05-11/cve-2026-6722-php-soap-use-after-free-in-soap-global-ref-map.md`: CVE-2026-7262 carries `6.3 (CVSS 4.0, PHP advisory)`; the CNA record (cveawg) scores 2.9 Low. Sourced to the advisory, so advisory only.
5. F11 (low confidence), `entries/2026-09-23/virtualizor-billing-hook-unauth-root-rce.md`: "a product outside the typical public-administration estate" has no cited source.
6. F11 (low confidence), `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md`: action `8f5420317c` "and rotate every credential" has ambiguous scope.
7. F11 (low confidence), same entry, hunt sentence `1c3204e41f`: "from external or unexpected source ranges", the "external" qualifier is not stated by the source.
8. F11 (low confidence), `entries/2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou.md`: the Infosecurity Magazine source in `sources[]` is never cited inline.
9. F11 (low confidence), `entries/2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev.md`: `sources[0]` is a JSON API endpoint; it resolves and carries the cited text.
10. F11, em dashes in reader-facing text of PeopleSoft (6 lines), Liechtenstein (13 lines) and the Acronis title; declined by the main agent in iteration 7 as stripped at render.

### Prior-iteration (iteration 7) deltas, re-checked

| Delta | Disposition on disk and source |
|---|---|
| F11 em dashes (nginx, LiteLLM, Liechtenstein; ChainDrop, Lazarus, SAP) | Declined; occurrences remain in this slice's PeopleSoft/Liechtenstein/Acronis entries (finding 10). Advisory. |
| F11 Liechtenstein "(updated)" takeaway label | Declined; the label marks the Swiss-register takeaway, a different jurisdiction's finding; the main takeaway still stands for Liechtenstein. Accepted, no new finding. |
| F11 PHP SOAP CNA 2.9 vs advisory 6.3 | Declined, unchanged; finding 4. |
| F11 priority-field narration in PHP SOAP and Exchange Correction sections | Declined; the sections state why priority moved (no exploitation, vendor fix since 2026-09-01, ...), a reader-facing fact. Accepted. |
| F3 Instructure disclosure date | Applied: the 2026-05-01 disclosure is cited to BleepingComputer, the 2026-04-29 detection to The Register; both pages confirm their date. Correct. |
| F4 PeopleSoft blanket assume-compromise | Applied: the action now asks to investigate an exposed hub for compromise. Correct against Mandiant. |
| F4 PeopleSoft "better-evidenced" | Applied: zero occurrences on disk. |
| F5 PeopleSoft bulk-query alert | Applied: marked "in analyst judgement". |
| F5 PeopleSoft "Strasbourg" | Applied: zero occurrences on disk. |
| F11 PeopleSoft repeated zstd sentence | Applied: one occurrence left. |
| F5 FortiBleed device-config sentence | Applied: marked as analyst judgement. |
| F11 FortiSandbox / SonicWall / Check Point sector tags | Declined; profile relevance call. Accepted. |
| F11 Austria / Virtualizor Improvement-section restatement | Declined; accepted. |

### Fire documents re-read against disk

- `docs/audits/2026-10-11-quality-audit.md` (471 lines): counts recomputed from `git show 430fbdf:` and the working tree: calibration table, model-baseline table, October discipline statistics, entry-shape counts, KEV window, registry (+2 entities) and sources (13 changed) diffs, `state/cves_seen.json` (+1 new, 5 refreshed), tool changes (`_page_skeletons` in `check_run.py`, `_pdf_streams` in `fetch_source.py`; `test_fetch_source_pdf.py` 14/14 pass), `state/warning_acknowledgments.json` (+1 entry), the legacy queue (`legacy_review.py --stats`), the 17 sub-agents and telemetry sums, the 89/79/69 sweep figures and the priority moves all hold. Exceptions: findings 1 and 3.
- `prompts/CHANGELOG.md` section 4.20 against `git diff HEAD -- prompts tools docs/architecture.md`: the banner bump v4.20, the LAST_AUDIT loop, partial-audit list, duplicate guard and step 5b, the `docs/architecture.md` change all match. Exception: finding 2.
- `runs/2026-10-11/2026-10-11T1307Z-audit.md`: frontmatter parses; 17 sub-agents; `sources_changed` 13; `entities_added` 2; placeholders `verification_iterations: 7` and `verification_residual_count: 19` expected. Gate summaries: start 25 pass · 1 warn · 0 fail · 23 acknowledged, end 25 pass · 1 warn · 0 fail · 24 acknowledged, consistent with one new acknowledgment.

### Considered, no finding

Every ledger claim was decided against a page fetched this pass (cached bodies first; MSRC SUG API, CERT-Bund CSAF JSON, cveawg and the Acronis JSON advisory read for per-CVE authority). No IOCs, no `watchlist` tag, no `org_triage` block, Admiralty `classification` present on all 26 entries, no workflow-internal language in reader-facing fields, no priority miscalibration found in the slice.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 7). The three truth findings are document and record-count corrections (one low confidence). Iteration 8 is the cap, so the run publishes with them logged as residuals.

### Findings summary (machine-readable)

See `work/2026-10-11T1307Z-audit/verification.iter8.s4.findings.yaml` (10 records).
