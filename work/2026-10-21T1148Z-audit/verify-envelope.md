# Phase 5.7 verifier envelope, cleanup wave 04 (run 2026-10-21T1148Z-audit)

Shared brief for every slice of every iteration. Your spawn message names the iteration, its role, your slice and its ledger file. Your definition (`.claude/agents/cti-verification.md`) governs everything this brief does not say.

## What this run is

An operator-directed partial audit, cleanup wave 04 of the one-time store cleanup program (`prompts/cleanup-coordinator.md`). It re-verified 75 legacy entries filed 2026-05-10 to 2026-05-22 (migrated from the v2 daily briefs, never audited before) and appended one `correction` or `improvement` record to 74 of them, most of which were rewritten from their sources and gained an Admiralty rating, an ATT&CK mapping and the labelled lines. The 75th, `2026-05-20/prepare-emergency-drupal-patch-window-for-today-17-00-21-00`, was folded into `2026-05-20/drupal-core-highly-critical-pre-patch-warning-unauthenticate` (its id is in that entry's record `merged_from`; the file is gone by design). The run published no new entry.

- run_id: `2026-10-21T1148Z-audit`; today is 2026-10-22 (UTC). The entries describe May 2026 events: a statement is judged as true as of the date it is written for, and "as of" wording is checked against its date.
- Run record: `runs/2026-10-21/2026-10-21T1148Z-audit.md` (telemetry in its frontmatter). Wave report: `docs/audits/2026-10-21-cleanup-wave-04.md`. Its `## Verification` and `## Tracker delta` sections, and the run record's verification block and closing **Verification.** paragraph, are filled after this loop: do not report those placeholders.
- Base commit: `work/2026-10-21T1148Z-audit/base.sha`. The ledger lists only the claims this fire changed on each entry. Read each entry whole for context. A defect in text this fire did not change is an advisory finding marked `(pre-existing)`, except a pre-existing fact no source supports (F4), which is a truth finding.
- Gate: `python3 tools/check_run.py 2026-10-21T1148Z-audit --pre-verify` exits 0 (53 pass, 5 warn, 0 fail). The `quote-literal` check skips migrated entries, so **no evidence quote in this run was machine-checked**: check each `evidence[]` quote whose claim is in your slice verbatim against its page yourself. `citation-cve` likewise found no clause to check.
- The truth passes saved the pages they read under `work/2026-10-21T1148Z-audit/truth-<n>/bodies/` and the repair workers under `work/2026-10-21T1148Z-audit/repair-<n>/src/` (URL on the first line). Use them as cached bodies, and fetch fresh when a body is missing, truncated or may have changed. Cite only what you read in this pass.
- Dedup and registry context: `entities/registry.yaml`, `state/cves_seen.json`. The run record's `entities_added` names the 7 new entities; the wave report's § Registry and state changes describes the summary rewrites and relations, which are checkable against `git diff "$(cat work/2026-10-21T1148Z-audit/base.sha)" -- entities/registry.yaml state/cves_seen.json`.

## Rules worth repeating for this run

- A score, workaround or date that only the CVE record carries (CVE Services API, cve.org, NVD) is not citable; ENISA EUVD per-vulnerability pages are.
- Each inline citation must sit on a clause its page carries. A clause cited to a page that holds only part of it is F3.
- Every `techniques[]` id must be active in `attack/enterprise-attack.json` and name a behavior the body describes and a source supports; an access vector no source states is F4.
- `classification` follows the sourcing (a vendor advisory plus CERT restatements is one assessor). `actions[]` is empty on every entry by design.
- No IOCs, no em dashes and no pipeline self-reference in reader text (record summaries and sections included).

## Outputs (slice-suffixed)

Write your files with your slice suffix: `work/2026-10-21T1148Z-audit/verification.iter<N>.s<k>.md`, `.findings.yaml` and `.claims.yaml` (the `claims:` list, one row per ledger claim in your slice, written as you go), plus `verify.iter<N>.s<k>.started_at` / `.ended_at` / `.progress`. Return the compact summary your definition specifies, with these report paths, plus a `**Claims:** in_scope=N checked=N` line.
