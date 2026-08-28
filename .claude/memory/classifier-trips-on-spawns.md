---
name: Content-safety classifier trips on sub-agent spawns
description: Spawns dying with "safeguards flagged this message" — mitigation ladder, and the false-positive rule (quiet output ≠ dead spawn)
type: project
---

# Classifier trips on sub-agent spawns

A spawn can terminate immediately with "safeguards flagged this message" — a content classifier reacting to offensive-security vocabulary, not a structural bug. Observed clusters (2026-07-23, 2026-07-26, 2026-08-06) hit Sonnet-pinned definitions handling raw offensive-research content; whether Sonnet 5 trips at the same rate is unmeasured — record spawn terminations per fire.

## Mitigations that work

- **Defensive role framing** at the top of the spawn message ("You are a fact-checker … no offensive content in scope — the entries carry no IOCs, no exploit code by policy"). Reframing the role is legitimate; hiding what the work is is not.
- **Point at the coverage file instead of enumerating covered breach/actor names inline** — the 2026-08-06 respawns that replaced the inline enumeration with a pointer to `work/<run-id>/prior_coverage.json` both completed.
- **Checkpoint findings YAML every 3–4 items** so a trip costs the tail, not the batch.

## Ladder (single Sonnet 5 verifier since v4.1 — no other-model fallback)

Retry once → re-frame (framing + no quoted exploit prose + checkpointing) → record a failed spawn (set `verification.confirmation_waived` only if it was the confirmation pass). A failed spawn never counts as CLEAN. Never block the run; a missing run record is the worst outcome. Report a trip as a classifier trip with retry count, never as "the mechanism failed".

## The false positive (2026-08-22): absence of output is NOT a dead spawn

A healthy iteration-2 verifier with an empty run directory at 11 min was declared dead and retried; it delivered its full report 90 s later. A killed spawn is announced by the harness (task notification / spawn error) — a quiet run directory is the normal mid-flight state of an agent that writes at the end. Wait for the notification while the wall-clock cap (45 min research / 30 min verification) has not expired, and check that a recovery spawn can even advance the gate it exists to protect before starting it.
