---
name: Routine model assignment (Series 5)
description: Intel fires Sonnet 5, audit Opus 5, sub-agents pin generic `sonnet` at xhigh effort, single verifier with same-definition double-CLEAN; plus the model self-identification protocol
type: project
---

# Routine model assignment (Series 5) + self-identification

- **Intel fires run on Claude Sonnet 5; the quality audit on Claude Opus 5** (routine configuration, outside the repo). Both sub-agent definitions pin the generic `model: sonnet` alias — NEVER a dated id (operator directive 2026-08-28; the alias tracks the current Sonnet generation) — and `effort: xhigh` (operator directive 2026-08-28; main-agent default effort is also `xhigh` via `.claude/settings.json` `effortLevel`).
- **One verifier definition** (`cti-verification-alt` deleted). Publish gate = two consecutive CLEAN verdicts, same definition; the two-model requirement is retired and era-gated in `check_run.py` (`SINGLE_VERIFIER_FROM = (4,1)`) and `site/build.py`, so history and the acknowledgment ledger stay green. Deltas rule: an iteration after a NEEDS_FIXES receives the prior deltas block; a confirmation pass after a CLEAN receives nothing but the fact of the CLEAN.
- Never reintroduce an Opus pin or a second verifier definition. Series-5 prompt style: literal scope statements, calibrated length, positive examples; the verifier's bar is evidence not severity (coverage at the finding stage, `(low confidence)` markers instead of self-filtering).

## Self-identification (protocol, probe-verified 2026-07-09)

- **Primary source: the harness-injected model line in each agent's OWN system prompt** ("You are powered by the model named … The exact model ID is …") — generated at spawn time, it sees the definition's pin. Quote it verbatim on the `**Model:**` line.
- Fallback 1: env vars `CLAUDE_FRIENDLY_NAME`/`CLAUDE_MODEL_ID` — **container-scoped, blind to pins**; always carry the marker `— container default, env fallback`. Uniformity among such reports is a measurement limitation, never proof pinning failed. Fallback 2: `Anthropic Claude (specific model not determined)` — never a training-data guess.
- Uniform "Claude Sonnet 5" across verifier iterations is the EXPECTED healthy shape since the rotation's retirement. Pre-v3.15 records showing uniform Opus across pinned sub-agents are measurement artifacts of the old env-var protocol.
