# Store Cleanup Coordinator — One-Time Program

> **Prompt version:** v4.23 (tracked in `prompts/CHANGELOG.md` with the master prompts). **Status:** open. The program ends by retiring itself (§ C9), after which no cleanup of old entries is needed again.
>
> **How it runs:** an interactive Claude Code session started with "Read `prompts/cleanup-coordinator.md` on `main` and continue the store cleanup program." The first such session is the **coordinator**: it plans the program, runs the first wave and hands each later wave to a fresh session. Every later session reads the same file and runs the wave its kickoff names ("… and run cleanup wave <NN>."), or, with none named, the lowest-numbered wave the tracker marks `ready`. **From v4.23 waves run in parallel, one session per wave, on lanes the tracker keeps disjoint** (§ Binding rules). The repository is the shared memory: `docs/cleanup/STATUS.md` (tracker) and `work/cleanup/plan.json` (machine-readable plan) on `main`.

## Mandate and definition of done

Clean up everything in ctipilot that is old, wrong or no longer used, so that afterwards the weekly quality audit is the only quality loop the store needs. Done means all of these hold on `main`:

1. **Every published entry has been truth-verified under the current standard at least once since its last substantive change**: claim by claim against fetched sources, with a rating, an ATT&CK mapping and inline citations as its kind requires. The legacy queue is empty (`python3 tools/legacy_review.py --stats` → 0 pending), and no entry is left that no audit truth pass ever covered.
2. **Every known finding is applied or recorded as declined with a reason**:
   - the 188 out-of-week verdicts of the 2026-10-18 audit (`work/2026-10-18T1307Z-audit/truth-*.yaml`; 77 factual errors, 68 imprecisions);
   - the residuals and `(pre-existing)` advisories that audit loops carried forward;
   - the portable hunks on the reference branch.
3. **No duplicate findings remain**, whether they share a CVE or not; each pair is folded with `tools/fold_entries.py` or linked through `references[]`.
4. **The registry is clean**:
   - no duplicate record: an orphan that duplicates another key is tombstoned onto it (keys are permanent, so none is deleted);
   - no relation whose `source` entry is gone;
   - the known summary defects fixed: Eurail's retracted DPA/EDPS review, `incident:daemon-tools-supply-chain-2026` "EU governments targeted", and BeaverTail "an initial loader".
5. **Sources and state are current**:
   - the 2026-10-11 operator recommendations 5–7 are decided on their evidence (Red Canary, `ssd-disclosure`, `google-tag` vs `mandiant-gtig`);
   - no `state/warning_acknowledgments.json` row matches nothing;
   - `state/coverage_backlog.md` holds only live rows.
6. **No dead weight remains in the repository**: unused tools, stale docs, retired code paths and stale `work/` material are removed (rules in § C7). Known gate false positives are fixed in `tools/check_run.py`.
7. **The program is retired** (§ C9).

Throughout: `python3 tools/check_run.py --all` ends `0 warn · 0 fail` after every wave, and `python3 site/build.py` is warning-free.

## Binding rules

- **All of `CLAUDE.md` applies.** In particular:
  - entries change only through changelog records (`correction` / `improvement` / `update`, `internal: true` for metadata-only), with no silent edit and never a second entry for one finding;
  - run records are immutable after their fire;
  - no IOCs, feature branches only, `check_run.py` exits 0 before every commit;
  - the verifier loop always runs at least once;
  - push notifications only for pipeline breakage.
- **Parallel waves on disjoint lanes (v4.23, operator directive 2026-10-21).** Several waves run at the same time, each in its own session, as the tracker plans them:
  - A wave starts only when `work/cleanup/plan.json` marks it `ready`, every wave its `after` list names is `done`, and `python3 work/cleanup/render_status.py --check-lanes` passes on `main` (the waves ready or in flight share no entry). Never two sessions on one wave.
  - A wave changes only the entries its own rows list. A fold partner, duplicate or defect it finds on an entry another wave holds, or on an entry no row lists, goes back to the tracker as a new row and is never edited in passing.
  - Shared files merge structurally: `tools/merge_state.py resolve` merges `state/cves_seen.json`, `entities/registry.yaml`, `sources/sources.json`, `state/legacy_review.json` and `work/cleanup/plan.json`, and re-renders `docs/cleanup/STATUS.md`. The auto-merge workflow runs it on every conflict, and a wave runs it when its own sync conflicts.
  - All sessions draw on one account-wide session limit, which the intel fires (daily, about 02:56Z) and the Sunday audit share. In October 2026 three audits at once exhausted it, so parallel waves are the operator's accepted trade-off: every wave keeps its own spawn cap, a wave that hits a rate limit is cut under § C8 instead of retrying in a loop, and no wave starts between Saturday 18:00Z and the Sunday audit's record landing on `main`.
  - A wave's `partial` claim never blocks the scheduled audit (v4.22). A wave that sees the scheduled audit's open claim spawns nothing until that record lands, then merges `origin/main` and continues (`prompts/quality-audit.md` Phase 0 step 2). Claims of different waves never stand each other down.
- **One wave per session, at most 20 sub-agent spawns per wave**, retries and continuations included (the v4.21 bound). Log every spawn in `work/<run-id>/budget.tsv` with the `subagent_tokens` its completion notification reports.
  - A spent budget is a forced cut: no further spawns, `verification.budget_cut` set, and the remaining rows go back to the tracker.
  - The run record and the report always ship.
- **Merge continuously.**
  - Every finished wave is committed and pushed on its own `claude/cleanup-wave-<NN>-<suffix>` branch; the auto-merge workflow lands it on `main`.
  - A wave is finished only when Phase 7 shows its record on `main` and on the site.
  - A small standalone change, such as a tool fix or a doc removal, ships the same way the moment it is done and green; it never waits for a wave.
  - Never push to `main`.
- **The reference branch `cleanup/2026-10-18-carry-forward` is never merged.**
  - It holds unverified drafts from the 2026-10-18 audit: its `docs/cleanup/CARRY-FORWARD-2026-10-18.md` says what is portable and what the 2026-10-11 audit superseded.
  - Ports are re-derived on top of `main`, re-verified and re-recorded under the porting wave's own run id.
- **Sub-agents** (pinned definitions in `.claude/agents/`):
  - `cti-verification` for truth passes and the Phase 5.7 verifier;
  - `cti-research` only when a fix needs a source nobody has found yet;
  - `Explore` for read-only repository inventories;
  - repair workers (§ C4) as `subagent_type: claude`: they compose from verified findings and neither research nor verify, so the "never `general-purpose` for research or verification" rule is not touched.
  - Give every sub-agent its own subdirectory, `work/<run-id>/<name>/`, for helpers and scratch files. Sub-agents that shared one scratch directory have overwritten each other's helpers.
  - Sub-agents never commit or push, and never edit shared state files (`entities/registry.yaml`, `state/*.json`, `sources/sources.json`); they list the change they need in their report and the main agent applies it.

## C0 — Bootstrap (coordinator only; skip when `docs/cleanup/STATUS.md` exists on `main`)

1. Sync: `git fetch origin main && git merge --no-edit origin/main`. Read:
   - `CLAUDE.md`;
   - `prompts/quality-audit.md`: § Session budget, Phase 0, § Secondary work, Phases 5 to 7;
   - `prompts/cti-run.md`: Phase 4 (§ Updating an existing entry, § The actionability contract, `actions[]`), Phases 5.5, 5.7, 6 and 7;
   - `docs/pipeline.md` § Entry lifecycle and § Entity registry;
   - `docs/audits/2026-10-18-quality-audit.md` and the recommendations and watch items of `docs/audits/2026-10-11-quality-audit.md`;
   - `git show origin/cleanup/2026-10-18-carry-forward:docs/cleanup/CARRY-FORWARD-2026-10-18.md`.
2. Build the inventory with the main agent plus at most two `Explore` spawns (they count toward the 20). Size each workstream:
   - **W1 carry-forward findings:** the 2026-10-18 out-of-week YAMLs, plus every `(pre-existing)` advisory and residual named in audit reports and records since 2026-09-27, plus the portable reference-branch hunks.
   - **W2 legacy queue:** `python3 tools/legacy_review.py --stats` and `--next`.
   - **W3 never-verified entries:** entries that are not in the legacy queue and that no audit truth pass ever covered. Derive them by collecting every entry id named in `work/*-audit/{truth-*.yaml,audit-plan.json}` and `runs/*-audit.md` `updated_entry_ids`.
   - **W4 duplicates:** every CVE-sharing pair store-wide, plus non-CVE twins by entity and title, such as RoguePlanet 2026-06-19 vs 2026-07-09, the 2026-05-17 Pwn2Own roundup, and Nightmare Eclipse 2026-05-30 vs YellowKey 2026-05-15.
   - **W5 registry**, **W6 sources and state**, **W7 repository dead weight and tooling:** see § C7.
3. Write `docs/cleanup/STATUS.md`:
   - one table row per work item: workstream, item or entry ids, size, planned wave, status (`open` / `in-wave <NN>` / `done <run-id>` / `declined: <reason>`);
   - a header with the definition of done and the current totals.
   
   Write the same plan as `work/cleanup/plan.json`. Order the waves:
   1. W7 tooling first, which makes every later wave cheaper (§ C7 items 1–2);
   2. W1 non-legacy factual errors (16 entries from passes T1–T9, filed 2026-05-18 to 2026-10-10);
   3. W4 duplicates, before their members are re-verified, so twins are not verified twice;
   4. W2 legacy, oldest first, about 60 to 100 entries a wave, then W3;
   5. W5 and W6 interleaved as small standalone merges;
   6. C9 last.
4. Ship the tracker and the plan alone on a `claude/cleanup-plan-<suffix>` branch, wait for them to land on `main`, then run wave 1 (§ C1–C6).

## C1 — Wave preflight

1. Run `prompts/cti-run.md` Phase 0 step 0 verbatim (verified clock, stale-clone check) with the run-id suffix `-audit`, so `RUN_ID` looks like `2026-10-21T0912Z-audit`.
2. Sync `main`, then write `work/${RUN_ID}/base.sha` and `work/${RUN_ID}/main.started_at`.
3. Run the claim check from `prompts/quality-audit.md` Phase 0 step 2 and the Saturday/Sunday rule above. An open claim under 48 h old that names this wave (`wave=<NN>`) → stop and report. Open claims of other waves are expected. Then confirm on the synced `main` that the tracker marks this wave `ready`, every wave in its `after` list is `done`, and `python3 work/cleanup/render_status.py --check-lanes` passes. If any of these fails, stop and report.
4. Write `partial $STARTED wave=<NN>` to `work/${RUN_ID}/audit.claim`. In `work/cleanup/plan.json`, set the wave to `in-flight ${RUN_ID}` and each of its rows to `in-wave <NN> (${RUN_ID})`, then re-render `docs/cleanup/STATUS.md`. Commit these three files alone on `claude/cleanup-wave-<NN>-<suffix>` and push. Once the claim is on `main`, re-run the check: if another session's claim for the same wave landed first, stand down and report. Re-run the check before every spawn batch.
5. Work only this wave's rows from here on. The rows other sessions hold are marked `in-wave` on `main` and are not this wave's to touch.

## C2 — Choose the wave's rows

The wave's rows are the ones `plan.json` assigns to it (`wave: "<NN>"`). A legacy batch is its row's `entries` list, never `python3 tools/legacy_review.py --next`, which would hand every parallel session the same oldest entries. Rows that do not fit the budget go back to the tracker as `open` with a reason. Spend about 10 of the 20 spawns on producing and applying fixes and keep about 10 for the verifier loop. Rows with fresh findings (W1) need no truth pass. Rows without them (W2, W3, W4) get one `cti-verification` truth pass per batch of about 20 entries, using the envelope of `prompts/quality-audit.md` Phase 1: the findings YAML, claim rows and the progress file.

## C3 — Truth passes (only for rows without fresh findings)

Spawn the batches in one message. Each pass re-verifies its entries whole against fetched primaries and writes `work/${RUN_ID}/truth-<n>.yaml`. The pass reports duplicates it notices within its batch as groups, with a proposed survivor.

## C4 — Repairs

Hand each batch of findings (about 12 to 20 entries) to one repair worker (`subagent_type: claude`). Small sets go to the main agent instead. The spawn message carries:
- the findings file and entry ids;
- the wave's `RUN_ID`;
- the rules of `prompts/cti-run.md` Phase 4 § Updating an existing entry, the actionability contract and the no-IOC rule;
- the record tool from § C7 item 1;
- `tools/fold_entries.py --run "$RUN_ID"` for folds.

The worker's duties:
- Re-read the cited or ground-truth source for every sentence it writes, quote only verbatim, never construct a URL, and cite the specific page.
- Fix a wrong statement where it stands. Rewrite the analysis from its sources when most of it is unsupported.
- Give a legacy entry the rating, ATT&CK mapping (active ids in `attack/enterprise-attack.json`) and labelled lines (`**Exposure:**`, `**Detection:**`, `**Triage:**` only with an honest discriminator, `**Defender takeaway:**`) its kind requires, where the sources support them.
- Append exactly one record per entry for the wave, whose `fields` name every changed field plus `body`. A reader-facing change gets its `## <Type> — <at>` section; a metadata-only one is `internal: true`.
- Decline a finding it cannot confirm, with the reason.
- Write `work/${RUN_ID}/repair-<n>.md`, listing per entry the record type, the fields, the declined findings, and the registry and `cves_seen` changes it needs. Return a compact summary.

## C5 — Gate, verify, publish

1. The main agent:
   - applies the shared-state changes the workers listed;
   - runs `python3 tools/sync_products.py` and `python3 tools/legacy_review.py --done "$RUN_ID" <ids>` for legacy rows;
   - runs `python3 tools/check_run.py "$RUN_ID" --pre-verify` and fixes every FAIL and every warning the wave caused.
2. Phase 5.7 as `prompts/quality-audit.md` scopes it for audits:
   - `python3 tools/claim_ledger.py "$RUN_ID" --iteration N` (it reads `base.sha`, so updated entries contribute only their changed claims, and folded survivors are read whole);
   - slices of about 300 claims, at most three for iteration 1 and for a confirmation pass, one for a post-fix pass;
   - double-CLEAN gate, cap 8, fail-open, and `budget_cut` when the spawns run out.
3. Write `docs/audits/<RUN_DATE>-cleanup-wave-<NN>.md` covering scope, clean/total, findings applied and declined, folds, tool and doc changes, what the budget did not reach, and the tracker delta.
4. Write the run record `runs/<RUN_DATE>/<RUN_ID>.md`:
   - `kind: audit` and the current `prompt_version`;
   - `sub_agents` keys `truth-<n>` / `repair-<n>` / `explore-<n>`, never `G…` (a `G` key would move the weekly audit's window anchor);
   - `entries_updated` and `updated_entry_ids` naming every entry with a record from this wave;
   - the spawn total and token sum in the notes.
5. Update the tracker rows to `done <RUN_ID>` or back to `open`, with reasons, and set the wave to `done <RUN_ID>: <one-line outcome>`. Mark `ready` each planned wave whose `after` waves are now all done, provided `--check-lanes` still passes. Re-render `docs/cleanup/STATUS.md`.
6. Run `check_run.py "$RUN_ID"` and `--all`: 0 FAIL, and no warning but the run's own telemetry. Run `site/build.py` and `site/test_build.py`.
7. Stage specific paths, then commit, sync `main` and push with the Phase 6 retry shape. A sync conflict on the tracker or the shared state files is resolved with `python3 tools/merge_state.py resolve` (other waves land on `main` while this one runs); re-run `check_run.py "$RUN_ID"` after it.
8. Phase 7: poll until the record is on `main` and the run is in `https://ctipilot.ch/data/briefbook.json`, then ship the publish-status amendment.

## C6 — Hand over

When the wave is published (or cut and published), hand over before the session ends:
- For each wave the tracker now marks `ready` that no session holds (no open claim names it), queue one session with the kickoff line "Read `prompts/cleanup-coordinator.md` on `main` and run cleanup wave <NN>." Use the session tool that suggests a new task (`spawn_task`), one task per wave, when it is available; otherwise print the lines for the operator. The operator decides how many run at once.
- The tracker's header names the ready waves, the waves still waiting and what they wait for, and the earliest start time (the Saturday/Sunday rule).
- Never start another wave in the same session.

## C7 — Non-entry cleanup (W5–W7)

1. **Record tool** (first). Promote `work/2026-10-18T1307Z-audit/add_record.py` (append one changelog record with a strictly later `at`, the section and `updated_at` rule, re-parse) and `resum.py` (re-fold this fire's own unpublished record) into one tested `tools/entry_record.py` with `--run-id`. Add a row to the `CLAUDE.md` Key commands table. Every repair worker uses it.
2. **Gate false positives:**
   - Port the reference branch's `_page_skeletons` fix: extract text skips the tag stripper, `meta description` / `og:description` text is kept, and "(opens in a new window/tab)" labels are removed.
   - Make `citation-cve` report an image-only PDF as unreadable, not as "does not mention".
   - Add tests for both.
3. **Registry (W5):**
   - Registry keys are permanent: never delete or rename one. An orphan (no entry, relation or alias uses it) that duplicates another key is tombstoned with `merged_into: <canonical-key>`; an orphan with no canonical twin stays as it is.
   - Repair the known summaries.
   - Re-point or drop relations whose `source` entry was folded away.
4. **Sources and state (W6):**
   - Decide the 2026-10-11 recommendations 5–7 on the evidence in `state/source_health.json` and the feeds: retire or repoint the source record, with the reason in its notes.
   - Drop acknowledgment rows that match no current warning.
   - Trim struck backlog rows older than 30 days.
5. **Dead weight (W7):**
   - Remove what nothing reads: a tool no workflow, prompt, test or doc command uses (check `tools/migrate_briefs.py` and `tools/migrate_updates.py`, one-time v2 migrations), stale doc sections describing retired behaviour, and code paths for fields or kinds that are already retired. Keep the FAIL checks that guard against their return.
   - Committed `work/<run-id>/` directories older than 60 days are forensic history that git keeps, so remove them from the tree only when no tool, prompt or test reads them (check `build_prior_coverage.py`, the `check_run.py` page-check caches and liveness ledgers, `claim_ledger.py`). List what went and the commit that removed it in the wave report.
   - Never remove a run record, an entry outside a fold, an audit report or `prompts/CHANGELOG.md` history.
6. Each item ships as its own small merge when green (§ Binding rules).

## C8 — When something breaks

- A rate limit or stalled sub-agent follows `prompts/quality-audit.md`: never block the run record, record the cut, and return unfinished rows to the tracker.
- A conflict on shared state files is resolved with `python3 tools/merge_state.py resolve`.
- A real FAIL the wave cannot fix is fixed first or its change is reverted; nothing ships red.

## C9 — Retirement (last wave)

When every tracker row is `done` or `declined` and no other wave is in flight, ship one versioned change (banner bump and `prompts/CHANGELOG.md` entry; `cti-run.md` and `quality-audit.md` in lockstep):
- `prompts/quality-audit.md` § Secondary work is removed. The weekly audit, which verifies every new or changed entry each week and carries `(pre-existing)` advisories to the next truth pass, is the only steady-state quality loop.
- `tools/legacy_review.py` and `state/legacy_review.json` are removed (their final stats go in the report), and so are their `CLAUDE.md` and `docs/` mentions.
- This file's banner reads `Status: completed <date>, <run-id>`. It stays as history.
- A dated memory note records the closure.
- The final report `docs/audits/<date>-cleanup-final.md` gives before/after metrics: entries verified, corrections, folds, registry records, removed files, and warnings.

Finally, delete the reference branch `cleanup/2026-10-18-carry-forward` (`git push origin --delete cleanup/2026-10-18-carry-forward`) once the tracker shows every one of its rows ported or discarded.
