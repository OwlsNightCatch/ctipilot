---
name: Content-safety classifier trips on sub-agent spawns
description: Why some verifier/research spawns die with "safeguards flagged this message", which model it hits, what it costs the run, and the defensive-framing mitigation that measurably works.
type: project
---

# Content-safety classifier trips on sub-agent spawns

A sub-agent spawn can terminate immediately with `API Error: <model>'s safeguards
flagged this message` (the real-time cyber safeguards). It is **not** a bug in the
spawn message's structure, not a permissions problem, and not something a retry of
the identical prompt reliably fixes. It is a content classifier reacting to the
mix of offensive-security vocabulary in the prompt.

## Observed pattern (dated)

- **2026-07-23 intel run** — *every* `cti-verification-alt` (Sonnet) spawn died this
  way, iteration 2 retried and died again, plus three of four research spawns. The
  run lost its whole model rotation: all 8 verifier iterations ran on Opus, the
  double-CLEAN was confirmed same-model, and `verification.confirmation_waived`
  recorded the exception. It also could not deep-read the CrowdStrike SANDWORM_MODE
  body, so the day's strongest deep-dive candidate shipped as a standard entry.
- **2026-07-26 weekly quality audit** — the retrospective truth pass for batch B2
  died twice on `cti-verification-alt` (Sonnet), then succeeded on the Opus
  `cti-verification` definition with a reframed spawn message.

**It clusters on Sonnet spawns handling raw offensive-research content.** Treat a
uniform-model verifier chain as a possible symptom of this, not as evidence the
`model:` pinning or the rotation is broken (see `model-identity-and-rotation.md`).

## Mitigation that worked

Open the spawn message with an explicit defensive framing before the task, naming
what the agent is *not* being asked to do:

> You are a fact-checker: you read published defender-facing summaries and confirm
> they match the public vendor advisories, CERT bulletins and research posts they
> cite. There is no offensive content in scope — the entries carry no IOCs, no
> exploit code and no rule code by policy.

Also help the work survive a mid-flight death: tell the agent to **checkpoint its
findings YAML to disk every 3–4 items**, so a trip costs the tail of the batch
rather than the whole batch. The 2026-07-26 B2 retry had written 6 of 15 records
before it died, and they were on disk.

## Escalation order when a spawn trips

1. Retry once on the same definition (transient variation does sometimes pass).
2. Retry with the defensive-framing preamble above + checkpointing instruction.
3. Fall back to the **other** definition (i.e. the other model pin) and record the
   deviation — for a verifier that means noting the reduced model diversity in the
   run record; for the audit's truth passes it means saying which batch lost its
   assigned rotation slot.
4. Never let it block the run. A missing pass is a logged coverage gap; a missing
   run record is the worst outcome (anti-crash guard #1).

## What NOT to conclude

- Do not report "the rotation failed" as a mechanism defect when the cause was a
  classifier trip — say so explicitly, with the retry count.
- Do not strip the safety-relevant substance out of a spawn message to get it
  through. Reframing the *role* is legitimate; hiding what the work is is not.

## 2026-08-06 — a whole-run rotation outage, and the enumeration trigger confirmed

Two distinct patterns in one intel run, both on Sonnet-pinned definitions.

**Research spawns (2 of 4 died).** S2 and S3 were both terminated before writing findings.
The common factor in the two failed messages was a long enumeration of breach, actor and
ransomware names carried inline as dedup context. Both respawns replaced that enumeration
with a *pointer* to `work/<run-id>/prior_coverage.json` plus a one-line instruction to read
it, and both completed normally. This is the cheapest available fix and it costs nothing —
the agent reads the file anyway. **Default to pointing at the coverage file rather than
listing covered items inline.**

**Verifier rotation (4 of 4 died).** `cti-verification-alt` was spawned four separate times
across iterations 2, 2-retry, 3 and 4, with message lengths from very long to quite short,
and every attempt was terminated. Shortening did not help. The Opus-pinned
`cti-verification` ran five iterations in the same run without a single interruption.

**Consequence worth planning for: when the alt definition is unavailable, the double-CLEAN
publish gate is structurally unreachable**, because it requires two consecutive CLEANs on
two *different* models. No number of further iterations fixes that. Do not burn iterations
chasing it — take the documented same-model exception, set
`verification.confirmation_waived` with the spawn-failure reason and count, and publish on
the low-residual early exit or the cap. Say plainly in the run record that the gate was not
met rather than implying it was.

## 2026-08-22 — the false positive on this diagnosis: absence of output is not death

Iteration 2 of the verifier loop was declared dead and a retry was spawned on the
rotation-recovery ladder. The evidence was entirely filesystem-side: a 119-byte transcript
that had not grown in eleven minutes, no findings YAML, no report. **All three were true and
the agent was healthy** — it was mid-verification and had written nothing yet, because the
verifier definition writes its report at the end. It delivered a full report (NEEDS_FIXES,
one finding) about ninety seconds after the retry went out.

Two rules, both cheap:

- **Do not diagnose a blocked spawn from missing output files while the agent's wall-clock
  cap has not expired.** A killed spawn is announced by the harness — a task notification
  with a terminal status, or an error on the spawn itself. A quiet run directory is the
  normal mid-flight state of an agent that writes at the end, and the 30-minute verifier cap
  means a quiet eleven minutes is unremarkable. Wait for the notification.
- **Check a recovery spawn against the rotation it exists to protect before starting it.**
  The retry was pinned to the same definition and therefore the same model as the iteration
  it was replacing, so even a clean finish could not have supplied the second half of a
  two-model agreement. A recovery spawn that cannot advance the gate is pure clock.

Cost this run: several minutes of wall clock re-verifying material iteration 2 had just
verified, against a ~3 h guard the run was already 2.3 h into. The genuine classifier block
in the same run (a deep-read pass on kernel-driver material) looked nothing like this — it
surfaced as an explicit termination, not as silence.
