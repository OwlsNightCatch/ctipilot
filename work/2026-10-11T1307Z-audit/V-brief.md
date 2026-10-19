# Phase 5.7 verifier brief: quality audit 2026-10-11T1307Z-audit

You are the cold-reader verifier for a defensive SOC knowledge base. Entries carry no IOCs and no exploit code by policy. Your definition (`.claude/agents/cti-verification.md`) is the contract: truth checks, editorial checks, F1 to F18, the return format. This brief only scopes your slice.

## The run

- **run_id:** `2026-10-11T1307Z-audit`, a weekly quality audit (`prompts/quality-audit.md`, v4.20). The fire started on 2026-10-11 and was paused by an API session limit until 2026-10-19, when its work was re-based onto the current `main`. Records from fires after 2026-10-11 (for example the 2026-10-18 record on the Citrix CVE-2026-88771 entry) are other fires' work and out of scope; this fire's own Citrix record is dated 2026-10-19, the day it reaches readers.
- **What it changed.**
  - One NEW entry: `entries/2026-10-11/needymantis-modular-post-compromise-framework-storm-3069.md`.
  - 118 EXISTING entries, each now carrying exactly one `updates[]` record with `run_id: 2026-10-11T1307Z-audit`:
    - `correction`, `improvement` or `update`;
    - `internal: true` when metadata-only, with no body section;
    - otherwise one `## <Type> — <at>` section.
  - Many are legacy entries (v2-migrated, May to July) that this audit re-verified whole and rewrote from their sources. On those, the main analysis itself is this fire's text and is in scope.
  - 27 duplicate entries were folded into survivors with `tools/fold_entries.py`. The survivor's record carries `merged_from`, and the duplicate files are deleted, as designed.
- **Gate.** `python3 tools/check_run.py 2026-10-11T1307Z-audit --pre-verify` exited 0 with link checks on. Quote-literal: 3 evidence quotes found verbatim on their cited page. Citation-cve: 13 found on the cited page, 1 not machine-checkable.
- **Dedup context.** `work/2026-10-11T1307Z-audit/prior_coverage.json`, `entities/registry.yaml`.
- **Telemetry and claims about the fire.** `runs/2026-10-11/2026-10-11T1307Z-audit.md` (the run record) and `docs/audits/2026-10-11-quality-audit.md` (the audit report).

## Your slice

The spawn message gives your slice id `sK` and the iteration number `N`.

- **Entries:** `work/2026-10-11T1307Z-audit/verify-scope.iterN.sK.txt`. Read each entry whole: frontmatter, main analysis, labelled lines, and every changelog section, the newest against the main analysis.
- **Claim ledger:** `work/2026-10-11T1307Z-audit/claims.iterN.sK.yaml`. Every claim in it needs a verdict row. A pass that leaves claims unanswered is incomplete and its CLEAN does not count.
- **For each entry:**
  - Confirm this fire's record `summary` states what its section states.
  - For an internal record, confirm the frontmatter change is source-supported and genuinely has no reader-facing delta.
  - Check every field the record's `fields` names against the cited sources.
- **Slice s6 only**, in addition to its entries:
  - Read the run record and the audit report.
  - Verify every checkable claim they make about files, records, counts and state on disk: counts of entries, folds, survivors, the legacy queue (`python3 tools/legacy_review.py --stats`), registry additions, sources changed, the warning acknowledgment in `state/warning_acknowledgments.json`, and the CHANGELOG 4.20 entry against the actual diff (`git diff HEAD -- prompts tools docs/architecture.md`).
  - Report a wrong count or a claim the disk contradicts as F4 (or F5 for an unsupported statement), with the entry field set to the file path.

## Post-fix passes (iteration 2 onward)

- `work/2026-10-11T1307Z-audit/deltas.iterN.sK.yaml` lists the previous iteration's findings on your entries, each with the main agent's `remediation_applied`. Check every one: an "Applied" fix must hold on disk and against the source; a "Declined" or "No change needed" rationale must hold. A fix that did not land, or a rationale that fails, is a finding again.
- Your claim slice holds every ledger claim of your entries; the ones changed since the last iteration are the priority, but every claim needs a verdict row.

## Scratch space and budget

Reuse cached bodies before fetching; fetch each URL at most once per pass. Write helper scripts and temporary files only under `work/2026-10-11T1307Z-audit/v-tmp/iterN.sK/` (create it). Never write into the shared scratchpad or another slice's files: in iteration 2 two slices overwrote each other's helper.

## Fetching

Use your definition's ladder: `python3 tools/fetch_source.py extract <URL>`, then `url <URL>`, then the structured recipes (`cisa-kev`, `cisa csaf <id>`, `ncsc-csh post <ID>`, `pdf <URL>`), then `WebFetch` with the outbound-links template, then `jina <URL>` last.

Cached bodies are in `work/2026-10-11T1307Z-audit/quote-bodies/`; find one with `grep -l "<url>" work/2026-10-11T1307Z-audit/quote-bodies/*.extract.txt`, and reuse it before re-fetching. A page no rung reads gives the verdict `unreadable`, never `ok` by default. Append fetched URLs to `work/2026-10-11T1307Z-audit/url-liveness.tsv`.

## Write

- `work/2026-10-11T1307Z-audit/verification.iterN.sK.claims.yaml`: one row per ledger claim, `{claim_id, verdict: ok | F3 | F4 | F5 | F13 | F14 | unreadable, source_url, passage}`.
- `work/2026-10-11T1307Z-audit/verification.iterN.sK.findings.yaml`: structured findings, `code`, `entry`, `where`, `summary`, `ground_truth`, `ground_truth_url`, `fix`. Prefix `(low confidence)` where it applies.
- `work/2026-10-11T1307Z-audit/verification.iterN.sK.md`: your report.
- Timestamps: first action `date -u +%FT%TZ > work/2026-10-11T1307Z-audit/verification.iterN.sK.started_at`; last action before returning, the same into `.ended_at`.

Read-only otherwise: never edit entries, state or the record.

Return the compact summary your definition specifies:
- `**Model:**`
- `**Timestamps:**`
- `**Verdict:** CLEAN | NEEDS_FIXES`
- `**Counts:** truth N · editorial N · advisory N`
- `**Claims:** in scope N · answered N`
- `**Self-telemetry:**`
- the report paths.

Findings carry evidence: the fetched passage and its URL.
