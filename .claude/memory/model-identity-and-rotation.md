---
name: Model identity & verifier rotation
description: Why sub-agent env-var self-reports cannot observe per-definition model pins, and how to record model identity truthfully
type: reference
---

# Model identity & verifier rotation — env vars are blind to pins; the harness prompt line is not

## The facts (established 2026-07-09, twice)

**Fact 1 — env-var scoping.** `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` are
**container-scoped**: they are set once for the routine container and describe
the **main-agent default model**. A sub-agent definition's `model:` frontmatter
pin (`cti-research` → sonnet, `cti-verification` → opus, `cti-verification-alt`
→ sonnet) is applied by the harness at spawn time and is **invisible to the env
vars**. A pinned sub-agent that reports the env vars therefore reports the
container default — on an Opus-default container, every sub-agent reports
"Claude Opus 4.8" regardless of what it actually runs on. Uniform env-reported
models are a *measurement limitation*, never evidence that pinning or the
Phase 5.7 rotation failed.

**Fact 2 — the resolvable signal (supersedes v3.12's "unresolvable from inside
the sandbox").** The harness injects a per-agent model line into each agent's
OWN system prompt — `You are powered by the model named <friendly>. The exact
model ID is <id>.` — generated at spawn time from the same resolution that
applies the definition's pin. Diagnostic probes of all three definitions in an
interactive session (2026-07-09, operator-initiated) confirmed it is
**pin-aware** while the env vars in the SAME spawns uniformly said
"Claude Opus 4.8" / `claude-opus-4-8`:

| Definition | pin | prompt line reported | env vars reported |
|---|---|---|---|
| `cti-research` | sonnet | Sonnet 5 / `claude-sonnet-5` | Opus 4.8 |
| `cti-verification` | opus | Opus 4.8 (1M context) / `claude-opus-4-8[1m]` | Opus 4.8 |
| `cti-verification-alt` | sonnet | Sonnet 5 / `claude-sonnet-5` | Opus 4.8 |

Side finding: pinning and the odd/even verifier rotation **genuinely work** —
the operator's suspicion that "the Sonnet agents were reporting Opus" was
correct, and it was the reporting that was wrong, not the pinning.

## The incident this corrects

Run record `runs/2026-07-09/2026-07-09T0409Z-intel.md` (§ AI-content
transparency) states as fact that "verifier model rotation did NOT take effect
this run" and an operator notification repeated it, based solely on all four
verifier spawns env-reporting Opus 4.8. That conclusion is **unverified** — the
uniform reports are exactly what the container-scoped env vars produce even when
rotation works. Run records are immutable post-publish, so the correction lives
here and in the v3.12 prompt guidance; treat that record's claim as a
measurement artifact, not an operational finding.

## The protocol (v3.15 — supersedes v3.12)

- **Primary:** every agent (main + sub) self-identifies from the harness-injected
  model line in its OWN system prompt and quotes friendly name + model id
  verbatim on the `**Model:**` line — never the name the pin would be
  "expected" to resolve to, never a training-data guess.
- **Fallback 1 (line absent):** the env vars, reported with the mandatory
  provenance marker `— container default, env fallback` inside the Model-line
  parentheses; never as proof of runtime model, never grounds for a
  rotation/pinning-failure claim.
- **Fallback 2:** `Anthropic Claude (specific model not determined)`.
- The main agent records reported values verbatim PLUS the per-iteration
  `subagent_type` (which preserves the definition and thus the model pin).
  Differing models across sub-agents are the EXPECTED healthy signal; only
  uniformity among env-fallback-marked reports is a measurement limitation.
- No schema / dashboard change was needed: `site/build.py`'s canonicaliser
  already resolves "Sonnet 5", `claude-sonnet-5`, and suffixed forms like
  "Opus 4.8 (1M context)" / `claude-opus-4-8[1m]`; a model_id recorded
  verbatim WITH the trailing fallback marker still canonicalises because the
  `^claude-<family>-<version>` prefix regex ignores what follows.
- Pre-v3.15 run records showing uniform Opus across pinned sub-agents are
  measurement artifacts of the superseded protocol — immutable, never edited,
  interpreted via this note.
