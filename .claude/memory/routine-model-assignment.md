---
name: Routine model assignment (Series 5.5)
description: Intel fires Sonnet 5.5, audit Opus 5.5 (switched 2026-09-29), sub-agents pin generic `sonnet` at xhigh effort, single verifier with same-definition double-CLEAN; the 5.5 prompting deltas; plus the model self-identification protocol
type: project
---

# Routine model assignment (Series 5.5) + self-identification

- **Intel fires run on Claude Sonnet 5.5 (`claude-sonnet-5-5`); the quality audit on Claude Opus 5.5 (`claude-opus-5-5`)**, routine configuration outside the repo, switched by the operator on 2026-09-29 (first 5.5 intel fire 2026-09-30T04:03Z, first 5.5 audit 2026-10-04). Both sub-agent definitions pin the generic `model: sonnet` alias, NEVER a dated id (operator directive 2026-08-28), and `effort: xhigh` (operator directive 2026-08-28; main-agent default is also `xhigh` via `.claude/settings.json` `effortLevel`).
- **Effort is unmeasured on 5.5.** Both 5.5 guides say effort levels were recalibrated and `xhigh` should be kept only where it measurably helps (Sonnet 5.5 at `xhigh` tends to open its own review rounds). The operator kept `xhigh`; the first audit to see a model change runs the generation baseline (`quality-audit.md` Phase 3 item 9) and recommends per role. Never change effort unilaterally.
- **5.5 prompting deltas shipped in v4.13:** unattended turn-ending contract (`cti-run.md` guard #12: a text-only turn stops the fire, four early-stop shapes are named), no self-started review rounds, fetch-don't-recall for mutable facts, real checks for tool edits, `stop_reason: refusal` categories recorded, never ask an agent to write out its reasoning (`reasoning_extraction` declines).
- **One verifier definition** (`cti-verification-alt` deleted). Publish gate = two consecutive CLEAN verdicts, same definition; the two-model requirement is retired and era-gated in `check_run.py` (`SINGLE_VERIFIER_FROM = (4,1)`) and `site/build.py`. Deltas rule: an iteration after a NEEDS_FIXES receives the prior deltas block; a confirmation pass after a CLEAN receives nothing but the fact of the CLEAN.
- Never reintroduce an Opus pin or a second verifier definition. Prompt style that works on Series 5/5.5: literal scope statements, calibrated length, positive examples, named failure shapes; the verifier's bar is evidence not severity (coverage at the finding stage, `(low confidence)` markers instead of self-filtering).
- `site/build.py` `_ops_canonical_model` folds `claude-sonnet-5-5` / `claude-opus-5-5[1m]` / `Sonnet 5.5` to "Claude Sonnet/Opus 5.5" (asserted in `site/test_build.py`), so the AI-content notice renders the point release.

## Self-identification (protocol, probe-verified 2026-07-09)

- **Primary source: the harness-injected model line in each agent's OWN system prompt** ("You are powered by the model named … The exact model ID is …"), generated at spawn time, it sees the definition's pin. Quote it verbatim on the `**Model:**` line.
- Fallback 1: env vars `CLAUDE_FRIENDLY_NAME`/`CLAUDE_MODEL_ID` — **container-scoped, blind to pins**; always carry the marker `— container default, env fallback`. Uniformity among such reports is a measurement limitation, never proof pinning failed. Fallback 2: `Anthropic Claude (specific model not determined)` — never a training-data guess.
- Uniform current-Sonnet across verifier iterations is the EXPECTED healthy shape since the rotation's retirement. Records before 2026-09-30 show "Sonnet 5"; from then on "Sonnet 5.5". Pre-v3.15 records showing uniform Opus across pinned sub-agents are measurement artifacts of the old env-var protocol.
