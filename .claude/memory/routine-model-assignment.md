---
name: Routine model assignment (Series 5)
description: Operator directive 2026-08-27 — intel fires on Claude Sonnet 5, quality audit on Claude Opus 5, both sub-agent definitions pinned claude-sonnet-5, single verifier, same-definition double-CLEAN gate (prompt v4.1)
type: project
---

# Routine model assignment — Series 5 (operator directive 2026-08-27, shipped as prompt v4.1)

- **Intel fires (`prompts/cti-run.md`) run on Claude Sonnet 5.** The quality audit (`prompts/quality-audit.md`) runs on Claude Opus 5. Both are routine-configuration facts (set where the routine is scheduled, not in the repo); the prompts state them so the agents know their own model.
- **Both sub-agent definitions pin `model: claude-sonnet-5`** (`cti-research`, `cti-verification`) — the explicit model id, not the `sonnet` alias, so the pin cannot drift with the alias and never follows the main agent. `cti-verification` runs at `effort: xhigh` (the pipeline's hardest agentic task; previously Opus at `high`).
- **One verifier definition.** `cti-verification-alt` (the Sonnet rotation variant of v3.23–v4.0) is deleted; `tools/compose_prompts.py`, `.github/workflows/compose-profile.yml` and the org-profile comments no longer list it. The lockstep-regeneration rule for the two verifier files is gone with it.
- **Publish gate = two consecutive CLEAN verdicts, same definition.** The two-different-models requirement is retired. `check_run.py` (`SINGLE_VERIFIER_FROM = (4, 1)`) and `site/build.py` (`_SINGLE_VERIFIER_FROM`) era-gate the old `verification-rotation` check and the same-model WARN to v3.23–v4.0 records, so `--all` on immutable history and the existing `warning_acknowledgments.json` rows are unaffected.
- **Deltas block rule (replaces the odd/even split):** an iteration that follows a NEEDS_FIXES receives the prior-iteration deltas block and walks it before its own cold pass; a confirmation pass after a CLEAN receives nothing but the fact of the previous CLEAN.
- **Blocked-spawn ladder without an other-model fallback:** retry once → re-frame the spawn message → record a failed spawn (waiver only if it was the confirmation pass). There is no definition to switch to.
- **Series-5 prompt style applied:** literal scope statements, calibrated (not fixed) length, positive examples, minimal narration; the Opus 5 audit prompt told not to add verification passes or spawn sub-agents to re-check its own work; the Sonnet 5 verifier told that the bar is evidence, not severity (coverage at the finding stage, `(low confidence)` marker instead of self-filtering).
- **Landed on top of v4.0** (the concurrent retire-the-weekly / one-living-entry change by another session, same day): the verifier definition keeps v4.0's updated-entry scope and truth check 4c verbatim.

**Why:** the operator moved the routine to the Series 5 models and wanted the verifier chain simplified — one Sonnet 5 verifier, two independent CLEAN passes — and every prompt written for how these models actually read instructions.

**How to apply:** never reintroduce an Opus pin or a second verifier definition; keep `model:` values as explicit ids; when you touch the verifier loop, keep the deltas-after-NEEDS_FIXES rule and the cold confirmation pass. Related: [[model-identity-and-rotation]], [[classifier-trips-on-spawns]], [[entry-lifecycle-v4]].
