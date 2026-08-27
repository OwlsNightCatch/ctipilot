---
name: entry-lifecycle-v4
description: Operator directive 2026-08-27 — weekly routine retired, one living entry per finding with an updates[] changelog; the gate labels and the practical traps of appending an update
type: project
---

# Entry lifecycle v4.0 — one living entry per finding (operator directive 2026-08-27)

**The directive.** Remove the weekly briefing everywhere; keep only two routines — the intel run (any cadence) and the quality audit. Corrections, improvements and developments go INTO the original entry as dated update/correction notes; one entry per finding for its whole life; the update timestamp floats the entry back to the top of the live page; every change is clearly timestamped and kept as a changelog on the entry. Normative: `docs/pipeline.md` § Entry lifecycle.

**The contract, in one screen.**
- `discovered_at`, `run_id`, entry id/path, `migrated_from` never change. `updated_at` == `updates[-1].at` (null until the first record). Activity moment = `max(discovered_at, updated_at)` — the live brief, briefbook, alerts and feeds key on it.
- `updates[]` is append-only, oldest first: `{at, run_id, type: update|correction|improvement, summary, fields?, merged_from?}`; each record pairs 1:1, in order, by exact `at` with a body section headed `## <Type> — <at>` (`content_model.update_section_heading`). The section carries the delta only, inline-cited; new sources/quotes go into `sources[]` / `evidence[]`.
- `update` = material development → frontmatter moves to the new current state. `correction` = the entry was wrong → fix the wrong text WHERE IT STANDS (declare `fields`, incl. `body`) AND write the section saying what was wrong / right / ground truth. `improvement` = precision added without reversing a claim.
- `update_of` is RETIRED (gate FAILs any non-null value). Migrated 2026-08-27 by `tools/migrate_updates.py`: 180 update entries folded into 114 roots (report `work/migration-v4-updates/report.json`); old permalinks redirect via each record's `merged_from`. `horizon: strategic`, `weekly_section`, kinds `synthesis`/`outlook` and run kind `weekly` are legacy-only (FAIL on v4+ runs).
- Gate labels: `entry-updates` (shape, `updated_at` mirror, strictly increasing `at`, section pairing, record `run_id` resolves), `silent-edit` (an entry modified in the working tree without a record for THIS run FAILs), `dedup` (a NEW entry sharing a CVE with ANY existing entry FAILs unless that entry is in `references[]` — store-wide, not 14 days), `run-counters` (`entries_updated` == entries carrying this run's record; `updated_entry_ids[]` names them, required on v4+ records), `legacy-shape`.

**Why:** two entries per finding split the reader's and the triage agent's view of the current state, and the weekly re-framed facts it never fetched (see [[weekly-synthesis-citation-traps]]); a changelog on the entry keeps one URL current and auditable.

**How to apply — the traps:**
- ONE record per fire per entry; fold every change of this fire into it. `at` must be strictly later than the entry's last activity — on an overtake, re-read the entry on `origin/main` for a newer record before appending yours ([[scheduler-and-workflow-races]]).
- `actions[]` is the CURRENT do-now set — replace, never accumulate. `headline`/`summary` change only when a summary-only reader must now know something different.
- A correction is two edits: the wrong sentence/field fixed in place AND the dated section; grep the same fact across title/headline/summary/body/evidence/cves after the fix (the partial-remediation trap in [[weekly-synthesis-citation-traps]] still applies).
- An update to an OLD entry lives outside `entries/<RUN_DATE>/` — stage it (`git add -u entries/`), or Phase 6 ships the record without the entry.
- Bookkeeping that changes nothing a reader acts on (a `cisa-kev` flag on a CVE the entry already calls exploited) is not a record ([[dedup-store-wide-cve-index]]).
- Code lesson: `content_model.load_entry` must deep-copy `ENTRY_DEFAULTS` — a shared `updates: []` default silently pooled every entry's records into one list during the migration dry run; the validator caught it before anything was written.
- The audit's immutability-exception ledger is retired — the changelog IS the ledger ([[entry-immutability-exceptions]] is history).
