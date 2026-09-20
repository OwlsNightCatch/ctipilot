**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-20T14:56:12Z · ended_at=2026-09-20T15:02:35Z · duration_seconds=383

## Verification report — 2026-09-20T1308Z-audit (iteration 5)

### Prior-iteration deltas — walked and confirmed

1. **F4 (Oracle `sourcing_note` dual-axis language).** Current text: "NCSC-NL republished the Fusion Middleware half of the release as its own advisory and assigned it a high priority, which is a second assessment of severity rather than an independent assessment of the underlying facts." Fetched `https://advisories.ncsc.nl/2026/ncsc-2026-0372.html` (via the `/advisory?id=` → dated-URL redirect): the page carries a single `Prioriteit` field, value `Hoog`, and no separate likelihood/damage axis. Grepped the whole entry file for "likelihood and damage", "damage rating", "dual" — no hits anywhere (frontmatter, body, or the two changelog sections). Remediation confirmed correct and complete on this surface.
2. **F4 low-confidence (28 Oracle CVE-index records).** Reproduced independently with a fresh word-boundary regex (`oracle|weblogic|peoplesoft|hyperion|e-business suite|fusion middleware`) against `state/cves_seen.json`'s 1,129 records: **28**. Matches the report's corrected figure and stated cause exactly.
3. **F8 (Hyperion framing split).** Body now reads: "Five of them are the single-sign-on, directory and application-server tiers... The sixth sits elsewhere: Hyperion Financial Management is a financial-consolidation application from Oracle's separate Hyperion family, so it is the finance estate rather than the identity estate that needs checking for it." Accurate and introduces no new unsupported claim — confirmed against Oracle's own risk matrix (fetched `cspusep2026.html`), which lists Hyperion Financial Management as a distinct product row from WebLogic/Access Manager/Forms/Internet Directory/Platform Security for Java.

### Cold pass — verified clean

- Oracle risk matrix fetched directly (`https://www.oracle.com/security-alerts/cspusep2026.html`): all six CVE ids, CVSS 10.0, AV:N/AC:L/PR:N/UI:N/S:C, the C:H/I:H/A:H-for-five-and-A:None-for-Hyperion split, and all affected-version strings in the entry's `cves[]` match the fetched matrix row-for-row, including the 11.2.26.0.000 Hyperion version added at iteration 3.
- NCSC-NL advisory fetched directly: confirms only the five Fusion Middleware CVEs at CVSS 10.0 (`CVE-2026-71133, CVE-2026-83099, CVE-2026-83059, CVE-2026-83020, CVE-2026-83021`) and that CVE-2026-87230 (Hyperion) is absent from its CVE list — consistent with the entry's own framing that NCSC-NL covers only "the Fusion Middleware half."
- Six `correction` records cross-checked against their cited sources this iteration: Cisco FMC (fetched the PSIRT advisory — revision 2.6, "Replaced hot fixes with the security hardening releases," Fixed Releases table matches verbatim), Brevo (fetched Sansec — "more than 100 thousand customer sites" verbatim), Linux kernel KEV (fetched all three Red Hat pages — the retained "corner case" quote is a verbatim substring of Red Hat's CVE.org-sourced description; the raw-HTML `url` fetch confirms the "This CVE is high risk and there are known public exploits..." string is a genuine Red Hat page string (an i18n message key), matching The Hacker News's quote of it; the removed skb_store_bits quote is correctly gone from the body), Japan Digital Agency (fetched Piyolog — the new `original:` Japanese text is a literal, verbatim substring of the page), GTG-27005 (fetched Anthropic's report — "We identified nine accounts associated with this group; eight were used only for ordinary freelance work... we banned accounts associated with the actors" matches the corrected text exactly, no "banned all nine" claim survives), NTC (now correctly non-internal with its own `## Correction` section, `credibility: 2`, consistent sourcing_note).
- Four `internal: true` improvement records (Salt, Chosen Brick, AEPD, Gyazo) checked: none carries a body section, each is a genuine metadata/plain-language-only change, and the Gyazo sourcing_note duplication flagged at iteration 2 is gone with no new duplication introduced.
- `check_run.py 2026-09-20T1308Z-audit` re-run this iteration: 48 pass · 0 warn · 0 fail (1 acknowledged), matching the run record and report.
- Em-dash figure (8,416 across 906 of 917 `entries/*/*.md` files) reproduced exactly with an independent script.
- Run record's four `verification.iterations` blocks: each iteration's `truth + editorial + advisory` reconciles with its own `findings[]` length (checked all four by hand); `verification_residual_count: 3` correctly equals iteration 4's `truth(2) + editorial(1)`.
- Both `references[]` entries on the Oracle entry resolve to real files (`2026-08-20/oracle-august-2026-cpu-three-unauthenticated-cvss-10.md`, `2026-06-18/cve-2026-46978-cve-2026-35278-oracle-june-2026-cspu-unauthen.md`).
- Swept the run record and report for every remaining "five" occurrence: all are either about the unrelated "5 factual errors" count, correctly-scoped past-tense narration of the iteration-2/3 defect history, or the deliberately-immutable slug (explicitly called out as such). No stale "five" survives as a live claim about the Oracle flaw count in the entry, run record, or report body.

### Unsupported / hallucinated facts

**#1 (new).** `sources/sources.json`, the `oracle-cpu` record's `notes` field, appended by this run: "...the September 2026 CSPU (2026-09-15, **five** unauthenticated CVSS 10.0 flaws) passed six consecutive fires unremarked although the store had already published the June and August CSPUs." This is the same count this run's own iteration 2 corrected to six everywhere else (entry frontmatter/body/actions, run record, report). This is a fourth surface of the exact "fix applied to one place, not its siblings" pattern this run's own report devotes its systemic section 4 (and watch item) to — this time in `sources/sources.json` rather than in an entry, run record, or report. Fix: change "five" to "six" in that note. Low severity (an internal source-metadata note, never reader-facing) but it is the same defect class and would mislead the next fire reading that source record.

### Editorial / less-is-more flags (advisory)

**#1 (low confidence).** Recommendation 5 of the report states: "Re-measured precisely: **80** entries under the strict pattern in `sourcing_note`..." Reproducing `check_run.py`'s own `_SELF_REF_RE` regex (`\b(?:as of )?th(?:is|is|e) (?:run|fire|pipeline|store)\b|...`) against every entry's `sourcing_note` field this iteration gives **81**, not 80 (list of 81 file paths enumerated). I cannot rule out a difference in how my quick script extracts frontmatter versus the shipped checker (e.g. YAML block-scalar edge case), so this is flagged low-confidence rather than as a confirmed miscount — but given this exact class of off-by-one has recurred four times already in this run (em-dash count, CVE-index count, sources[] record count, and now possibly this one), it is worth a second look before publish. Not blocking.

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)**

One genuine truth-class residual: the `sources/sources.json` `oracle-cpu` note still states "five" where the finding, once corrected, is six — the fourth surface of this run's own repeating propagation failure, this time outside the entry/run-record/report triad the prior three iterations swept. Everything inside the entry itself, the run record's Oracle-related text, and the report's live (non-historical) claims about the Oracle count is now clean and reproducible. The six changelog corrections and four internal improvements on the other ten entries were re-verified against their cited sources this iteration and hold without exception. One low-confidence advisory item (an 80-vs-81 count on a non-blocking recommendation) is noted for the record but does not by itself withhold CLEAN.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: sources.json
  item: "oracle-cpu source record (state file touched by this run)"
  url_or_quote: "the September 2026 CSPU (2026-09-15, five unauthenticated CVSS 10.0 flaws) passed six consecutive fires unremarked"
  summary: "sources/sources.json's oracle-cpu notes field, appended by this run, still says the CSPU carried five unauthenticated CVSS 10.0 flaws; every other surface (entry frontmatter/body/actions, run record, report) was corrected to six by iteration 2. Fourth surface of the same propagation failure this run's own systemic section 4 and watch item describe, occurring in source metadata rather than an entry."
- code: F11
  category: editorial-advisory
  section: docs/audits/2026-09-20-quality-audit.md recommendation 5
  item: "production-process self-reference sweep count"
  url_or_quote: "Re-measured precisely: 80 entries under the strict pattern in sourcing_note"
  summary: "(low confidence) Reproducing check_run.py's _SELF_REF_RE regex against every entry's sourcing_note this iteration gives 81, not 80. Could be a frontmatter-extraction difference in my own script rather than a real miscount; flagged for a second look given the run's repeated off-by-one pattern on other counts, not blocking."
```
