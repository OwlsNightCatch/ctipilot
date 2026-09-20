**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-20T13:49:07Z · ended_at=2026-09-20T14:05:56Z · duration_seconds=1009

## Verification report — 2026-09-20T1308Z-audit (iteration 1)

Scope read in full: the new entry (`entries/2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10.md`), all 10 updated entries plus `git diff HEAD` on each, the run record, and `docs/audits/2026-09-20-quality-audit.md` checked as a claims document against disk (source fetches, store-wide scans, `check_run.py --all`, `site/build.py`).

**What held up.** The Oracle entry's five CVE ids, CVSS 10.0 scores, component names and version strings all match Oracle's own risk matrix verbatim (`extract`'d live); the "153 patches / 78 unauthenticated" figures match Oracle's Fusion Middleware paragraph exactly. All five factual-error corrections (Cisco FMC hardening-release table, Piyolog Japanese original-text substring, Anthropic's "banned accounts associated with the actors" wording, Sansec's "more than 100 thousand" quote, Red Hat's "high risk... known public exploits" quote) were independently re-fetched and match verbatim. The report's numeric claims for: 35-entry scope split (23 new / 12 older-updated), KEV additions (7, all covered), research-source count (111), excluded-id count (76), warning-ledger size (33), CVE-database-API sourcing before/after (12→11 entries, 21→18 records, 5 primary both times), bare-PD-reference count (14→11), `actions[]` shape (15/23 empty, mean 0.48, max 3), the operational-kind priority mix (2 critical / 6 high / 10 notable, n=18), and the per-kind ATT&CK densities (vulnerability 1.4 n=7, incident 1.6 n=5, threat 14.8 n=6, annual-report 8.0 n=1) all reproduce exactly against a fresh scan of the store. `check_run.py --all` exits 0 and `site/build.py` builds clean with zero em dashes reaching any of 6,524 built HTML pages outside `<code>`/`<pre>`.

### Unsupported / hallucinated facts

**#1 (F4).** `2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat` — the 2026-09-20 `correction` record's summary states: "the three NVD API endpoints previously listed as sources are replaced by Red Hat's own per-flaw advisory pages." This is true only of the frontmatter `sources[]` array. The entry's main analysis (unchanged by this run's diff — confirmed via `git diff HEAD`, no `-`/`+` on these lines) still carries three live inline citations: `([NVD/NIST, mirroring the kernel fix commit](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-39682))` and the same for CVE-2025-39964 and CVE-2026-53266. `NVD/NIST` is no longer present anywhere in the entry's `sources[]` list (confirmed by reading the current file), so these three citations are now orphaned from any source record, and they still point at the exact blocked pattern (`services.nvd.nist.gov/rest/json/cves…`) the org rules and `check_run.py`'s `BLOCKED_SOURCE_PATTERNS` table forbid as a citation target (a raw JSON API response, not a readable page) — `check_run.py`'s `check_blocked_sources` only scans frontmatter `sources[]`, not body markdown links, which is why this passed the gate. Fix: replace the three body citations with the corresponding `access.redhat.com/security/cve/cve-…` links now in `sources[]`, and correct the changelog record's summary, which overstates what changed (check 4c(d)).

**#2 (F4).** `2026-09-18/ntc-swiss-solar-inverter-cybersecurity-assessment` — the 2026-09-20 changelog record moves `classification.credibility` from `1` to `2` and populates `sourcing_note` (previously `null`), but is marked `internal: true` with no `## Correction — 2026-09-20T13:29:09Z` body section. Both fields are reader-facing: `site/build.py`'s `render_detail_assessment()` (lines 4330–4369) renders the classification badge (`render_classification_badge`), the "Info credibility" fact row, and the `sourcing_note` text (`<p class="fact-note">`) on every entry's detail page. A reader now sees a different credibility badge (A1→A2) and a sourcing note that did not exist before, with nothing telling them why. The internal-record contract (`docs/pipeline.md` line 400-404) restricts `internal: true` to changes "never rendered anywhere on the site" — this one is. Fix: convert to a non-internal `correction` record with a body section, or accept the existing prose (already written in the record's `summary`) as the section text.

**#3 (F4).** `docs/audits/2026-09-20-quality-audit.md`, "Fixes shipped in this commit" item 5: "Five `correction` records for the five factual errors… and **five `improvement` records**, four of them `internal: true` (Gyazo, Salt, AEPD and Chosen Brick reader-text fixes; **NTC classification**)." Reading the actual entry files: NTC's 2026-09-20 record has `type: correction` (verbatim, confirmed above), not `improvement`. There are only four `improvement` records this run (Gyazo, Salt, Chosen Brick, AEPD), all `internal: true` — not "four of five." The correct tally is six `type: correction` records this run (five reader-facing for the five factual errors, plus NTC's internal one) and four `type: improvement` records, not five-and-five as the report states.

**#4 (F4).** `docs/audits/2026-09-20-quality-audit.md`, § "The em-dash question, closed": "The roughly 2,100 em dashes in entry source files are a silent style defect." Independent count (`grep`/Python, `—` across `entries/*/*.md`): **8,415** em dashes across 906 of 917 entry files — roughly 4× the report's figure. The report's other claim in the same paragraph (zero em dashes reach the rendered site outside `<code>`/`<pre>`) was independently reproduced and holds; only the entry-source-file count is wrong.

**#5 (F4, low confidence).** `docs/audits/2026-09-20-quality-audit.md` / `tools/check_run.py` docstring: "140 of 776 iterations, across 68 of 181 run records" have `truth+editorial+advisory != len(findings)`. I reproduced the totals (776 iterations, 181 records — exact match once a YAML-unparseable record, `runs/2026-05-14/2026-05-14-e05c6e6e.md`, is manually reconciled: its 4 iterations all balance) but reproduced only **112 mismatched iterations across 60 records** using the identical rule (`check_verification_counters`'s own logic: `int(truth)+int(editorial)+int(advisory) != len(findings)`). Low confidence because a store-wide scan of 189 heterogeneous, schema-evolving run records is easy to get subtly wrong in either direction; flagging the ~28-iteration / 8-record gap for the main agent to re-run with the audit's own script rather than asserting my number is the true one.

### Editorial / less-is-more flags (advisory)

**#6 (F11).** The run record's own `## Verification and coverage notes` body — reader-facing per the spawn instructions ("its verification-notes body is published too") — uses the literal terms rule 12 names as forbidden: "the first window in three with no blocked verifier **spawn**"; "the 2026-09-09 Windows entry that killed seven **spawns** across the two previous fires"; "Five of the six research publications the re-sweep recovered came from publishers no **sub-agent** was ever given." The same three terms recur repeatedly through the linked `docs/audits/2026-09-20-quality-audit.md` (e.g. "no blocked spawn," "seven spawns," "no sub-agent was given all week"). Style rule 12 names exactly these tokens ("sub-agent", "spawn") as barred from "any entry or ... the run-record notes." This is a direct, verbatim violation of a named prohibition, not a soft style preference — flagged as F11 only because no other category in the taxonomy fits a whole-run style-discipline defect.

**#7 (F12, low confidence).** `2026-09-17/aepd-first-ai-agent-breach-notification` carries `verification: single-source-national-cert`, and the audit's declined-finding rebuttal (docs report, "Imprecisions documented, no record warranted") defends this against a challenge that AEPD is not on the org profile's enumerated national-CERT carve-out list, arguing the underlying rule text reads "national CERT / **government authority**" and the profile "enumerates CERTs rather than bounding the carve-out." The rendered org-profile carve-out in this deployment's own context block is a closed, named list (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI/CERT-FR, NCSC-UK, NCSC-NL, CISA, CCN-CERT, AGID-CSIRT-IT, CERT.at, CERT-PL) that does not include AEPD; Spain's actual national CERT on that list is CCN-CERT, a different body. Even granting the "government authority" reading, the specific enum value used (`single-source-national-cert`, literally asserting AEPD is a national CERT) seems like the wrong sub-value versus a generic `single-source` with the carve-out explained in `sourcing_note` (which the entry already has). Not asserting the underlying single-source treatment is wrong — flagging the specific verification-value choice as worth a second look, at low confidence since I have not read PD-5's exact master-prompt text, only its rendered summary.

### Verdict

`NEEDS_FIXES (truth: 5, editorial: 1, advisory: 1)`

Everything independently checkable in `docs/audits/2026-09-20-quality-audit.md` reproduced correctly except the two items above (#3 NTC record-type mischaracterization, #4 the em-dash count, and #5 at low confidence) — the report's methodology and most of its arithmetic are sound and its five factual-error corrections all verify against freshly fetched primaries. The two changelog-contract defects (#1, #2) are the kind of thing this audit itself was built to catch, on entries this very audit touched. No coverage gap identified beyond what the report itself already discloses (the seven backlogged items with stated reasons); the Oracle recovery is well-sourced and accurately described.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable)
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat"
  url_or_quote: "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-39682 (and the CVE-2025-39964 / CVE-2026-53266 equivalents), still cited three times in the body as [NVD/NIST, mirroring the kernel fix commit]"
  summary: "Correction record claims the three NVD API endpoints 'previously listed as sources are replaced by Red Hat's own per-flaw advisory pages' but this is true only of frontmatter sources[]; the main analysis body still cites all three NVD JSON API URLs, orphaned from any sources[] record, and check_blocked_sources only scans frontmatter so the gate missed it."
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "2026-09-18/ntc-swiss-solar-inverter-cybersecurity-assessment"
  url_or_quote: "classification.credibility 1 -> 2, plus new sourcing_note, in a record marked internal: true"
  summary: "Both changed fields render on the entry-detail 'Assessment' fact table (site/build.py render_detail_assessment) — a reader-visible credibility-badge change and a brand-new sourcing note — yet the record is internal: true with no body section, contradicting the internal-record contract ('never rendered anywhere on the site')."
- code: F4
  category: hallucinated-fact
  section: audit-report
  item: "docs/audits/2026-09-20-quality-audit.md — Fixes shipped in this commit, item 5"
  url_or_quote: "\"five improvement records, four of them internal: true (Gyazo, Salt, AEPD and Chosen Brick reader-text fixes; NTC classification)\""
  summary: "NTC's actual changelog record has type: correction, not improvement (verified on disk); only 4 improvement records exist this run (all internal), and there are 6 correction records total (5 reader-facing + NTC internal), not 5-and-5 as stated."
- code: F4
  category: hallucinated-fact
  section: audit-report
  item: "docs/audits/2026-09-20-quality-audit.md — The em-dash question, closed"
  url_or_quote: "\"The roughly 2,100 em dashes in entry source files\""
  summary: "Independent count across entries/*/*.md finds 8,415 em dashes (906 of 917 files), about 4x the report's figure; the report's separate claim that zero reach the rendered site outside code/pre spans was independently reproduced and does hold."
- code: F4
  category: hallucinated-fact
  section: audit-report
  item: "docs/audits/2026-09-20-quality-audit.md / tools/check_run.py — verification-counters finding"
  url_or_quote: "\"140 of 776 iterations, across 68 of 181 run records\""
  summary: "(low confidence) Independent store-wide recomputation using the identical truth+editorial+advisory vs len(findings) rule reproduces the 776/181 denominators exactly but finds only 112 mismatched iterations across 60 records, not 140/68; flagging the gap for a second pass with the audit's own script rather than asserting my count is definitive."
- code: F11
  category: editorial-advisory
  section: run-record
  item: "runs/2026-09-20/2026-09-20T1308Z-audit.md — Verification and coverage notes"
  url_or_quote: "\"no blocked verifier spawn\"; \"seven spawns across the two previous fires\"; \"no sub-agent was ever given\""
  summary: "The published run-record notes (and the linked docs/audits/2026-09-20-quality-audit.md) use the literal terms 'spawn' and 'sub-agent' that style rule 12 names explicitly as forbidden workflow-internal language in any entry or the run-record notes."
- code: F12
  category: single-source-flag-missing
  section: updated-entries
  item: "2026-09-17/aepd-first-ai-agent-breach-notification"
  url_or_quote: "verification: single-source-national-cert"
  summary: "(low confidence) AEPD is Spain's data-protection authority, not its enumerated national CERT (CCN-CERT is, per this deployment's carve-out list); the audit's declined-finding rebuttal defends the carve-out's applicability but the specific verification sub-value asserts AEPD is a national CERT, which may be the wrong enum vs a generic single-source value with the carve-out explained in sourcing_note."
```
