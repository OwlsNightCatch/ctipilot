---
name: Model identity & verifier rotation
description: Why sub-agent env-var self-reports cannot observe per-definition model pins, and how to record model identity truthfully
type: reference
---

# Model identity & verifier rotation — the env-var scoping pitfall

## The fact (established 2026-07-09)

`CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` are **container-scoped**: they are set
once for the routine container and describe the **main-agent default model**. A
sub-agent definition's `model:` frontmatter pin (`cti-research` → sonnet,
`cti-verification` → opus, `cti-verification-alt` → sonnet) is applied by the
harness at spawn time and is **invisible to the env vars**. A pinned sub-agent
that follows the "env vars are authoritative" self-ID protocol therefore reports
the container default — on an Opus-default container, every sub-agent reports
"Claude Opus 4.8" regardless of what it actually runs on.

**Consequence:** uniform env-reported models across sub-agents / verifier
iterations are a *measurement limitation*, not evidence that model pinning or
the Phase 5.7 rotation failed. From inside the sandbox the discrepancy is
unresolvable; the harness documentation states per-agent frontmatter model/effort
IS honored.

## The incident this corrects

Run record `runs/2026-07-09/2026-07-09T0409Z-intel.md` (§ AI-content
transparency) states as fact that "verifier model rotation did NOT take effect
this run" and an operator notification repeated it, based solely on all four
verifier spawns env-reporting Opus 4.8. That conclusion is **unverified** — the
uniform reports are exactly what the container-scoped env vars produce even when
rotation works. Run records are immutable post-publish, so the correction lives
here and in the v3.12 prompt guidance; treat that record's claim as a
measurement artifact, not an operational finding.

## The protocol (v3.12)

- Sub-agents still report env values verbatim on the `**Model:**` line (only
  harness-provided signal), but never assert them as proof of runtime model and
  never report a rotation/pinning failure from them.
- The main agent records reported values verbatim PLUS the per-iteration
  `subagent_type` (which preserves the definition and thus the model pin). A
  mismatch or uniformity is recorded — if at all — as "env-reported; definition
  pin not independently verifiable at runtime", never as a failure claim.
- If the operator ever needs ground truth, it must come from outside the
  container (harness logs / API billing), not from agent self-reports.
