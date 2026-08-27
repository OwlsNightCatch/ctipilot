# Routines & prompts catalog

Canonical reference for **every prompt that drives this pipeline** — both the scheduled-routine
invocation prompts you paste into <https://claude.ai/code/routines> (which live *outside* the repo,
in the routine config) and the master / sub-agent prompts that live *inside* the repo and are loaded
at runtime. If you are setting up or auditing the routines, start here; the operator setup steps are
in [`docs/operating.md` § Set up the routines](operating.md#4-set-up-the-routines).

There are two kinds of prompt:

- **Routine invocation prompts** — the short text the claude.ai routine config runs on each fire.
  Version-controlled here (in this file) so a corrected copy always exists in the repo, but the
  *live* copy is whatever is pasted into the routine config. Keep the two in sync.
- **In-repo prompts** — the master prompts under [`prompts/`](../prompts/) and the sub-agent
  definitions under [`.claude/agents/`](../.claude/agents/). These are the source of truth for the
  pipeline's behaviour; the invocation prompts mostly just `Read` them.

---

## 1. Routine invocation prompts (claude.ai routine config)

### 1a. Intel run — several times per working day

```
Read prompts/cti-run.md and execute it.
```

Cadence-agnostic and self-healing: each fire derives its window from the gap since the previous run
record, so missed fires catch up automatically and the cron can change without touching the prompt.
More fires mean lower latency, never more content — dedup republishes only the new delta.

### 1b. Quality audit — operator-chosen cadence (weekly is typical)

```
Read prompts/quality-audit.md and execute it.
```

Institutionalizes the 2026-07-11 full-store intelligence-quality audit
([`docs/audits/2026-07-11-intelligence-quality-audit.md`](audits/2026-07-11-intelligence-quality-audit.md))
as a standing continuous-improvement routine. Cadence-agnostic like the intel run: each fire audits
the window since the previous `-audit` run record (default 7 days when there is none, self-healing
across missed fires, capped at 21 days): retrospective truth verification of every published entry
against its primary sources, independent coverage re-sweeps diffed against the store,
systemic/operational review (runaway runs, dark-but-green sources, discipline drift), re-check of the
previous audit's watch items, an effectiveness check on its shipped fixes, and the ATT&CK-pin
freshness check (`tools/attack_data.py --check`). The **first fire of each calendar month**
additionally runs the priority-calibration review (priority distribution vs verifier F16 drift — the
monthly review recommended by the 07-11 audit). Output: an audit report
`docs/audits/<date>-quality-audit.md`, a run record (`run_id` suffix `-audit`, `kind: audit`),
recovered entries where coverage gaps still clear PD-11, `correction` / `improvement` changelog
records appended to the published entries it found wrong or thin (never a second entry, never a
silent edit — `docs/pipeline.md` § Entry lifecycle), and fixes shipped under the versioning rule. A
72-h `duplicate-audit` guard makes double fires safe; a clean audit is a healthy outcome and is
reported as such.

> **Retired routine (2026-08-27).** A weekly strategic run (`Read prompts/weekly-summary.md and
> execute it.`) and its backup routine used to be the third and fourth entries here. Both were
> removed by operator decision along with the prompt file, the `/weekly/` pages and the weekly feed;
> the `horizon: strategic` entries they produced stay in the store as archived permalinks. **If the
> live routine config still carries either, delete them** — the prompt they `Read` no longer exists.

**Optional: an intel-run backup.** There is no intel backup configured, and one is rarely needed —
the intel run is cadence-agnostic and the *next* scheduled fire self-heals the missed window from the
gap since the last run record. If you want one anyway, key it on *recency of the latest intel run
record*, e.g. skip when `git grep -l "^kind: intel$" origin/main -- runs/<today>/` shows a record
newer than your staleness threshold, else `Read prompts/cti-run.md and execute it.` The intel run
has no hard duplicate guard, so its safety net is dedup (a re-scan republishes only the new delta,
and a covered finding receives a changelog record instead of a second entry), not a hard stop.

---

## 2. In-repo master prompts ([`prompts/`](../prompts/))

The routines load these at runtime; they are the source of truth for pipeline behaviour. **Editing
any file in this section is governed by the versioning rule** ([`CLAUDE.md`](../CLAUDE.md) §
*Editing the master prompts*): the same commit must carry the banner bump, a
[`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md) entry (`### Why` / `### What changed` / `### What
stays`), and the edit. `tools/check_run.py` cross-checks each run record's `prompt_version` against
the CHANGELOG head.

| Prompt | Role |
|---|---|
| [`prompts/cti-run.md`](../prompts/cti-run.md) | **Intel-run master prompt** (fires on the operator's cadence). Defines the shared machinery once: anti-crash guards, prime directives PD-1…PD-13, entry composition discipline incl. the entry lifecycle (new entry vs `updates[]` record on the existing entry), state lifecycle, the mechanical gate (Phase 5.5), the verification loop (Phase 5.7), and the publishing chain (Phases 6–7). Everything else builds on it. |
| [`prompts/quality-audit.md`](../prompts/quality-audit.md) | **Quality-audit run.** *Builds on* `cti-run.md` — it `Read`s that file at runtime and defines only the audit lens: retrospective truth passes over the window's published entries, independent coverage re-sweeps, systemic review, watch-item carry-forward, fix-effectiveness checks, the ATT&CK-pin freshness check, and the monthly priority-calibration review (Phase 3b, first fire of each calendar month). Root-causes every confirmed defect and ships the fix; corrections and improvements to published entries land as changelog records on those entries; report under `docs/audits/`. Shared machinery is never copied here, so the two prompts cannot drift. |
| [`prompts/verification.md`](../prompts/verification.md) | **Two-source / fake-news verification policy.** The sourcing checklist and the `verification` frontmatter enum that surfaces every entry's sourcing status. Referenced by both master prompts and by the verifier sub-agents. |
| [`prompts/entry-template.md`](../prompts/entry-template.md) | **Canonical entry + run-record skeletons.** The frontmatter contract (incl. `updated_at` / `updates[]`) and section shape the main agent composes against, plus the worked example of appending a changelog record to an existing entry. |
| [`prompts/check-run-fixes.md`](../prompts/check-run-fixes.md) | **Fix recipes for common `tools/check_run.py` FAILs.** Consulted when the Phase 5.5 gate does not exit 0. |
| [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md) | **Editorial-policy audit trail.** One entry per prompt edit; its head version must match the banner of the edited prompt and the `prompt_version` recorded in run records. Not itself a prompt the routine executes. |

The org-specific values inside these prompts live in `ORG-PROFILE` managed blocks generated from
[`config/org-profile.yaml`](../config/org-profile.yaml) by `python3 tools/compose_prompts.py --write`.
Never hand-edit a managed block; edit the config and re-compose in the same commit.

---

## 3. Sub-agent prompts ([`.claude/agents/`](../.claude/agents/))

Isolated-context workers the main agent spawns. Model is bound by each file's YAML frontmatter
(operator-rebindable; both pin `claude-sonnet-5`). **These are master prompts too** — the same
versioning rule applies.

| Sub-agent | Role |
|---|---|
| [`.claude/agents/cti-research.md`](../.claude/agents/cti-research.md) | **Research worker.** One spawned per domain — intel run S1–S4 (+ conditional S5 closed-source intake); the audit's G1–G3 coverage re-sweeps. Reads the prior-coverage index and `entities/registry.yaml` before fetching; returns findings YAMLs (a covered finding comes back as `novelty: update-of:<entry-id>` so the main agent appends a changelog record instead of a second entry), never composes entries. |
| [`.claude/agents/cti-verification.md`](../.claude/agents/cti-verification.md) | **Cold-reader verifier (Claude Sonnet 5).** Phase 5.7. Scope: the run's new entries, every existing entry it appended a changelog record to (whole entry — new section and changed fields against the sources), + the run record. Read-only; spawned fresh on every iteration until a confirmed CLEAN (two consecutive CLEAN verdicts from independent cold passes) or the 8-iteration cap. Two concerns — URL truth and editorial quality (finding categories F1–F18). The `cti-verification-alt` rotation variant was retired in v4.1. |

Self-identification for every agent (main + sub-agents) comes primarily from the model line the
harness injects into that agent's own system prompt (`You are powered by the model named … The
exact model ID is …`) — generated per-agent at spawn time, it reflects the definition's `model:`
pin (verified empirically 2026-07-09). Fallback: the `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` env
vars set in the routine container. The env vars are **container-scoped**: they carry the main-agent
default and cannot see a definition's `model:` pin, so an env-fallback report (marked
`— container default, env fallback` on the `**Model:**` line) shows the container default even
when the harness runs the agent on its pinned model — uniformity among such fallback reports is a
measurement limitation, not evidence the pinning failed. Never spawn
`general-purpose` for research or verification — use the named sub-agents; keep the live routine
allow-list matched to these definitions (see [`docs/operating.md` § Sub-agent capability ceiling](operating.md#sub-agent-capability-ceiling)).

---

## Keeping this catalog honest

- When you add, remove, or rename a routine, update § 1 here and
  [`docs/operating.md` § Set up the routines](operating.md#4-set-up-the-routines) in the same change.
- When you change what an audit fire *writes* (report filename pattern `docs/audits/<date>-quality-audit.md`,
  the `-audit` run-id suffix, `kind: audit`, the changelog records it appends), re-check § 1b here and
  `prompts/quality-audit.md` Phase 0 — the audit's window anchor greps `runs/` for the newest `-audit`
  record, and the monthly calibration duty greps `docs/audits/` for a current-month `## Priority
  calibration` heading.
- The in-repo prompt tables (§ 2, § 3) describe roles, not versions — the live version is always the
  banner at the top of each file and the head of [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md).
