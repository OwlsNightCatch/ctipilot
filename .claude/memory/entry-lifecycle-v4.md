---
name: Entry lifecycle — one living entry per finding
description: The v4 changelog model, the v4.3 modifiability relaxation, and the composition traps
type: project
---

# Entry lifecycle — one living entry per finding

(Normative: docs/pipeline.md § Entry lifecycle; procedure: `prompts/cti-run.md` Phase 4 § Updating an existing entry. Two routines since 2026-08-27: intel at any cadence + quality audit; the weekly is retired, `update_of` is retired and migrated — old URLs redirect via `merged_from`.)

**2026-08-29 — the weekly's entries are deleted, not archived.** Operator directive: all 393 `horizon: strategic` entries removed, and the schema that described them with them. `horizon` and `weekly_section` are DELETED fields (not legacy-tolerated) and `synthesis`/`outlook` are gone from `KINDS`; `ACTIVE_KINDS is KINDS`, and `legacy-shape` now FAILs an entry carrying any of them at all. `weekly` stays in `RUN_KINDS` only so the 21 kept weekly run records validate. Store is 829 entries. Don't reintroduce a horizon filter — `build.operational_entries`/`strategic_entries` and `brief.js`'s two horizon checks are gone because every entry is the same shape now.

- Developments/corrections/improvements = `updates[]` records + `## <Type> — <at>` sections ON the original entry. `internal: true` = metadata-only fix: no section, never rendered, never moves `updated_at`. Only a non-internal `type: update` re-floats the entry in /live/.
- **Modifiability (operator directive 2026-08-28):** only identity (`id`/path, `discovered_at`, `run_id`, `migrated_from`) and the append-only `updates[]` records are untouchable. Frontmatter, main analysis and earlier sections' text may all be revised in place when the modifying fire's record cleanly declares every change (`fields`, `body` included). No gate change — `silent-edit`/`entry-updates` already enforce exactly this.
- Gate labels: `entry-updates` (shape, `updated_at` mirror, strictly increasing `at`, section pairing), `silent-edit`, store-wide `dedup` (`references[]` escape), `updated_entry_ids`/`entries_updated` on the run record.

Traps:
- ONE record per fire per entry; `at` strictly later than the entry's last activity — on an overtake re-read the entry on `origin/main` first ([[scheduler-and-workflow-races]]).
- `actions[]` is the CURRENT do-now set — replace, never accumulate. `headline`/`summary` change only when a summary-only reader must now know something different.
- A correction fixes the wrong text IN PLACE and adds the dated section; grep the same fact across title/headline/summary/body/evidence/cves after ([[verification-lessons]]).
- An update to an old entry lives outside `entries/<RUN_DATE>/` — stage with `git add -u entries/` or Phase 6 ships the record without the entry.
- Bookkeeping that changes nothing a reader acts on is not a record ([[dedup-store-wide-cve-index]]).
- `content_model.load_entry` must deep-copy `ENTRY_DEFAULTS` — a shared `updates: []` default once pooled every entry's records into one list.
