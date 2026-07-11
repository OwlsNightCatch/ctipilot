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

### 1b. Weekly run — once per week

```
Read prompts/weekly-summary.md and execute it.
```

Fires on an operator-chosen day/time. Summarises the most recently completed ISO week. Refuses to
fire twice for the same ISO week (Phase 0 `duplicate-week` guard).

### 1c. Weekly backup run — resilience net for the weekly

A second routine that fires *after* the primary weekly slot and produces the weekly only if the
primary did not. Its whole job is to answer one question — *did a `-weekly` run record for the
relevant week reach `main`?* — and, only if not, run the weekly itself.

**Current correct prompt (paste this into the backup routine config):**

```
Backup run for the weekly CTI summary. This repo has NO `briefs/weekly/<week>.md` file: the
weekly output is `horizon: strategic` entry files plus one run record `runs/<date>/<run-id>.md`
whose run_id ends `-weekly` and whose frontmatter carries `week: <YYYY-Www>`. The weekly always
summarises the most recently COMPLETED ISO week — the week ending on the most recent Sunday
(today itself when today is Sunday), NOT the calendar week the current weekday falls in.

First determine whether that week's summary already published:

    u=$(date -u +%u); back=$(( u % 7 ))                 # Mon=1..Sun=7 -> days back to that Sunday
    TARGET_WEEK=$(date -u -d "-${back} days" +%G-W%V)   # ISO label of the most recent completed week
    git fetch origin main
    if git grep -q -e "^week: ${TARGET_WEEK}$" origin/main -- runs/; then
        echo "backup: weekly for ${TARGET_WEEK} already on origin/main - no action"; exit 0
    fi

If the grep matches, a `-weekly` run record for ${TARGET_WEEK} is already on `main` - the primary
run succeeded; print the message and exit without producing anything. If it does NOT match,
`Read prompts/weekly-summary.md` and execute it in full. That prompt's Phase 0 duplicate-week
guard independently re-derives the week and stops with `duplicate-week` if a record already
covers it, so running it is safe even in a race - no duplicate content can result.
```

**Why the check is written this way**

- **It checks the artifact that actually exists.** The v3 pipeline has no weekly brief file — the
  weekly's output is `horizon: strategic` entry files plus a per-fire run record
  `runs/<date>/<run-id>-weekly.md`, *rendered* to `/weekly/<YYYY-Www>/` by the site build (see
  [`docs/pipeline.md`](pipeline.md)). The record's frontmatter `week:` key is the durable, unique
  signal a week published; only weekly records carry that key, so grepping `runs/` for
  `^week: <TARGET_WEEK>$` is unambiguous. The per-fire run-id (date + `HHMM`) is not a fixed path,
  so a `git cat-file` on a guessed filename can't work — the content grep is what's robust.
- **It targets the week the weekly actually covers.** The weekly summarises the most recently
  *completed* ISO week — the week ending on the most recent Sunday, inclusive of today when today is
  Sunday. `back = $(date +%u) % 7` is the number of days back to that Sunday (Sun→0, Mon→1, … Sat→6),
  and its ISO label is `date -d "-${back} days" +%G-W%V`. This matches the primary on every weekday:
  a Sunday-night primary fire and a Monday-morning backup both resolve to the same week, and a backup
  that fires mid-week never prematurely targets the still-open current week.
- **The duplicate-week guard is the authoritative backstop.** Even if the pre-check is stale (the
  routine container's git proxy mirrors `github.com` on a schedule, not per-pull — see
  [`docs/operating.md`](operating.md)) and the backup proceeds to run, `weekly-summary.md`'s Phase 0
  re-derives the week and stops with `duplicate-week`. No duplicate content can be produced. The
  pre-check is a compute-saving optimisation layered on top of that guarantee, not the guarantee.

> **Superseded prompt (do not use).** The earlier backup prompt computed `date -u +%G-W%V` (the
> *current* calendar week, which on Mon–Sat is the still-open week, not the completed one) and tested
> `git cat-file -e origin/main:briefs/weekly/<week>.md` — a path that does not exist in the v3 model.
> Both faults made the check report "missing" on every fire, so the backup could never confirm a
> primary success via its intended signal; it leaned entirely on the downstream `duplicate-week`
> guard to avoid double-publishing (wasteful) and could not distinguish a healthy state from a real
> primary failure. The prompt above fixes both.

**Optional: an intel-run backup.** There is no intel backup configured, and one is rarely needed —
the intel run is cadence-agnostic and the *next* scheduled fire self-heals the missed window from the
gap since the last run record. If you want one anyway, mirror the pattern above but key on
*recency of the latest intel run record* rather than an ISO week, e.g. skip when
`git grep -l "^kind: intel$" origin/main -- runs/<today>/` shows a record newer than your staleness
threshold, else `Read prompts/cti-run.md and execute it.` The intel run has no `duplicate-week`
guard, so its safety net is dedup (a re-scan republishes only the new delta), not a hard stop.

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
| [`prompts/cti-run.md`](../prompts/cti-run.md) | **Intel-run master prompt** (fires N×/day). Defines the shared machinery once: anti-crash guards, prime directives PD-1…PD-13, entry composition discipline, state lifecycle, the mechanical gate (Phase 5.5), the verification loop (Phase 5.7), and the publishing chain (Phases 6–7). Everything else builds on it. |
| [`prompts/weekly-summary.md`](../prompts/weekly-summary.md) | **Weekly strategic run.** *Builds on* `cti-run.md` — it `Read`s that file at runtime and defines only the divergent weekly lens (W-PD-1 inclusion gate, ISO-week recency + `duplicate-week` guard, weekly dedup polarity, `weekly_section` placement). Shared machinery is never copied here, so the two prompts cannot drift. |
| [`prompts/verification.md`](../prompts/verification.md) | **Two-source / fake-news verification policy.** The sourcing checklist and the `verification` frontmatter enum that surfaces every entry's sourcing status. Referenced by both master prompts and by the verifier sub-agents. |
| [`prompts/entry-template.md`](../prompts/entry-template.md) | **Canonical entry + run-record skeletons.** The frontmatter contract and section shape the main agent composes against. |
| [`prompts/check-run-fixes.md`](../prompts/check-run-fixes.md) | **Fix recipes for common `tools/check_run.py` FAILs.** Consulted when the Phase 5.5 gate does not exit 0. |
| [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md) | **Editorial-policy audit trail.** One entry per prompt edit; its head version must match the banner of the edited prompt and the `prompt_version` recorded in run records. Not itself a prompt the routine executes. |

The org-specific values inside these prompts live in `ORG-PROFILE` managed blocks generated from
[`config/org-profile.yaml`](../config/org-profile.yaml) by `python3 tools/compose_prompts.py --write`.
Never hand-edit a managed block; edit the config and re-compose in the same commit.

---

## 3. Sub-agent prompts ([`.claude/agents/`](../.claude/agents/))

Isolated-context workers the main agent spawns. Model is bound by each file's YAML frontmatter
(operator-rebindable). **These are master prompts too** — the same versioning rule applies, and the
two verifier definitions move in lockstep (edit `cti-verification.md`, regenerate the alt body
byte-identically in the same commit).

| Sub-agent | Role |
|---|---|
| [`.claude/agents/cti-research.md`](../.claude/agents/cti-research.md) | **Research worker.** One spawned per domain — intel run S1–S4 (+ conditional S5 closed-source intake); weekly W1–W2 (+ conditional W3). Reads the prior-coverage index and `entities/registry.yaml` before fetching; returns findings YAMLs, never composes entries. |
| [`.claude/agents/cti-verification.md`](../.claude/agents/cti-verification.md) | **Cold-reader verifier (Opus default).** Phase 5.7. Scope: the run's new entries + run record. Read-only; re-spawned fresh until CLEAN or the 5-iteration cap. Two concerns — URL truth and editorial quality (finding categories F1–F18). Spawned on **odd** iterations. |
| [`.claude/agents/cti-verification-alt.md`](../.claude/agents/cti-verification-alt.md) | **Verifier, Sonnet rotation variant.** Byte-identical operational body to `cti-verification.md`; only the model frontmatter differs. Spawned on **even** iterations so model-specific blind spots surface. |

Self-identification for every agent (main + sub-agents) comes primarily from the model line the
harness injects into that agent's own system prompt (`You are powered by the model named … The
exact model ID is …`) — generated per-agent at spawn time, it reflects the definition's `model:`
pin (verified empirically 2026-07-09). Fallback: the `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` env
vars set in the routine container. The env vars are **container-scoped**: they carry the main-agent
default and cannot see a definition's `model:` pin, so an env-fallback report (marked
`— container default, env fallback` on the `**Model:**` line) shows the container default even
when the harness runs the agent on its pinned model — uniformity among such fallback reports is a
measurement limitation, not evidence the pinning or rotation failed. Never spawn
`general-purpose` for research or verification — use the named sub-agents; keep the live routine
allow-list matched to these definitions (see [`docs/operating.md` § Sub-agent capability ceiling](operating.md#sub-agent-capability-ceiling)).

---

## Keeping this catalog honest

- When you add, remove, or rename a routine, update § 1 here and
  [`docs/operating.md` § Set up the routines](operating.md#4-set-up-the-routines) in the same change.
- When you change what a weekly run *writes* (the artifact the backup keys on), re-check the backup
  prompt in § 1c — the pre-check greps `runs/` for `^week: <TARGET_WEEK>$`, which assumes the weekly
  record keeps carrying a `week:` frontmatter key.
- The in-repo prompt tables (§ 2, § 3) describe roles, not versions — the live version is always the
  banner at the top of each file and the head of [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md).
