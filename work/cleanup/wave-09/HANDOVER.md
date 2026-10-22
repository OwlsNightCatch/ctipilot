# Wave 09 kickoff (lane A, parallel waves)

Start the session for this wave with this message.

Read `prompts/cleanup-coordinator.md` on `main` and run cleanup wave 09.

Context for this session (left by the wave 03 session, 2026-10-21):

- **This session runs wave 09 (lane A, freed by wave 03)**: row W2-05, legacy batch 5, 76 entries filed 2026-06-21 to 2026-07-03. The batch is the row's `entries` list in `work/cleanup/plan.json`, never `legacy_review.py --next`. The 2026-06-27 The Gentlemen entry left this batch for W4-06 (wave 08), where its twin sits.
- These rows carry no fresh findings, so they need truth passes first (§ C2, § C3): about four `cti-verification` passes of 19 entries in one spawn message, with the envelope of `prompts/quality-audit.md` Phase 1 (wave 03's adapted copy is `work/2026-10-21T1149Z-audit/truth-envelope.md`, and its ledger builder is `work/2026-10-18T1307Z-audit/make_truth_ledgers.py <run-id>`, which reads `audit-plan.json` `truth_batches`). Then about four repair workers, and the rest of the 20 spawns for the verifier loop. Mark the batch with `python3 tools/legacy_review.py --done "$RUN_ID" <ids>`.
- **Start the session inside the repository** (working directory `/home/user/ctipilot` or wherever it is cloned). Wave 03 started outside it, so `.claude/agents/` was not registered at first and its truth pass had to load the `cti-verification` definition by instruction.
- **Run id:** before claiming, check that `work/<RUN_ID>/` does not already exist on `origin/main`. Waves 03 and 05 computed the same run id in the same minute (tracker row W7-17). Take the next free minute if it does.
- Sync first: `git fetch origin main && git merge --no-edit origin/main`, then read `CLAUDE.md` and `prompts/cleanup-coordinator.md` (v4.23) in full. Before the claim, confirm on `main` that the tracker marks this wave `ready` and that `python3 work/cleanup/render_status.py --check-lanes` passes. Write the claim as `partial $STARTED wave=09`, and in the same commit set the wave `in-flight <RUN_ID>` and its rows `in-wave 09 (<RUN_ID>)` in `work/cleanup/plan.json`, then re-render `docs/cleanup/STATUS.md` (§ C1).
- Other waves run at the same time. Touch only the entries your rows list. A fold partner, duplicate or defect on an entry another wave holds becomes a new tracker row and is never edited. A sync conflict on the tracker or the shared state files goes to `python3 tools/merge_state.py resolve`.
- Session budget: at most 20 sub-agent spawns, shared account-wide session limit. Wave 03 hit it twice (a repair worker and a verifier pass); each was resumed once after the reset with `SendMessage`, counted as a continuation, never retried in a loop. Do not start between Saturday 18:00Z and the Sunday audit's record landing on `main`.
- Lessons from waves 01 to 03 (reports under `docs/audits/2026-10-2*-cleanup-wave-*.md`):
  - Write every changelog record with `tools/entry_record.py`. On an entry with no `updates:` key, add `updates: []` as the last frontmatter line first (row W7-16).
  - `check_run.py` page checks skip migrated entries, which is every legacy entry: have the workers `grep -F` each new quote against the saved page body.
  - Bind each citation to the clause its page carries, and attribute a disputed claim (a vendor against a researcher) in the summary and takeaway too, not only in a `**Contradiction:**` line.
  - No file names an attacker chose (archives, batch files, payloads, exported functions): describe the behaviour.
  - A deletion in the analysis is declared in the record summary like an addition.
  - Record summaries say nothing like "this entry", and no rating vocabulary ("credibility number") in reader text.
- End by updating your rows and the wave in `plan.json`, marking ready the waves this one unblocks, re-rendering the tracker, and queuing a session for each newly ready wave (§ C6).
