# Wave 10 kickoff (lane B, parallel waves)

Start the session for this wave with this message.

Read `prompts/cleanup-coordinator.md` on `main` and run cleanup wave 10.

Context for this session (left by the wave 04 session, 2026-10-22):

- **This session runs wave 10 (lane B, freed by wave 04)**: row W3-01, the 71 entries filed 2026-07-03 to 2026-08-28 that no audit truth pass ever covered (they are not legacy entries, so `legacy_review.py --done` does not apply to them), and row W6-05, four research entries whose empty `techniques[]` is acknowledged in `state/warning_acknowledgments.json`. Fix W6-05 through records (map the tradecraft or justify the empty list in the entry), never through a new acknowledgment, and drop each acknowledgment row the fix makes stale. The batch is the rows' `entries` lists in `work/cleanup/plan.json`.
- These rows carry no fresh findings, so they need truth passes first (§ C2, § C3), with the envelope of `prompts/quality-audit.md` Phase 1. Wave 04's adapted copy is `work/2026-10-21T1148Z-audit/truth-envelope.md`, and its ledger builder is `work/2026-10-21T1148Z-audit/main/make_truth_ledgers.py`.
- **Budget the verifier loop first.** Wave 04 spent 16 of its 20 spawns on four truth passes, four repair workers and eight continuations after two session-limit stops. That left four for the loop: three first-pass slices and one post-fix pass, and the loop ended on `budget_cut` with a residual of 12. Keep at least six spawns for Phase 5.7. Slice a pass at about 300 claims: two of wave 04's first-pass slices of about 500 claims used about 0.7 M tokens each.
- **Start the session inside the repository** (working directory `/home/user/ctipilot` or wherever it is cloned), so `.claude/agents/` registers and `cti-verification` can be spawned by name. Wave 04 started outside it and ran its truth passes as emulated verifiers.
- **Run id:** before claiming, check that `work/<RUN_ID>/` does not already exist on `origin/main` (row W7-17). Take the next free minute if it does.
- Sync first: `git fetch origin main && git merge --no-edit origin/main`, then read `CLAUDE.md` and `prompts/cleanup-coordinator.md` (v4.23) in full. Before the claim, confirm on `main` that the tracker marks this wave `ready` and that `python3 work/cleanup/render_status.py --check-lanes` passes. Write the claim as `partial $STARTED wave=10`, and in the same commit set the wave `in-flight <RUN_ID>` and its rows `in-wave 10 (<RUN_ID>)` in `work/cleanup/plan.json`, then re-render `docs/cleanup/STATUS.md` (§ C1).
- Other waves run at the same time. Touch only the entries your rows list. A fold partner, duplicate or defect on an entry another wave holds becomes a new tracker row and is never edited. A sync conflict on the tracker or the shared state files goes to `python3 tools/merge_state.py resolve`, then rerun `python3 tools/sync_products.py` so the product block reflects both sides.
- Session budget: at most 20 sub-agent spawns, shared account-wide session limit. A stopped agent is resumed once with `SendMessage` after the reset and counted as a continuation. Do not start between Saturday 18:00Z and the Sunday audit's record landing on `main`.
- Lessons from wave 04 (`docs/audits/2026-10-21-cleanup-wave-04.md`), on top of the wave 09 handover's list:
  - Before the verifier loop, compare every record's `fields` with `python3 tools/entry_record.py diff <id> --run-id <RUN_ID>` and amend each mismatch. After any `amend --summary-file`, re-read the record: one wave 04 fix pasted another entry's summary into the Ivanti record.
  - A CVE id newly named in a body needs its `state/cves_seen.json` record, or the gate FAILs `cve-sync`.
  - Record summaries render on the site: state the finding, never the edit ("the analysis gains ...", "is mapped", "replaces the landing page as a source", "rather than a high-priority item").
  - A `sourcing_note` says which source carries which fact, never that a page failed to load.
  - Recount the report's and run record's tallies from disk after the last fix (mappings and distinct ids, CVEs added, product entities, summaries, priority moves), and regenerate the per-entry table from the final record summaries.
- End by updating your rows and the wave in `plan.json`, marking ready the waves this one unblocks, re-rendering the tracker, and queuing a session for each newly ready wave (§ C6).
