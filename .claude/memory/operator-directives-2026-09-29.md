---
name: operator-directives-2026-09-29
description: "v4.14 operator directive: no time limits on runs or sub-agents but every run must end (structural termination + inactivity-based hang detection), and every non-termination number is a guide, not a rule (entry counts, criticals, deep dives, category rotation, campaign cadence, candidate sources, audit batches)"
type: feedback
---

# Operator directive 2026-09-29 (shipped as prompt v4.14)

1. **No time limits, and every run ends.** The operator's words: "Remove the time limits and allow a run to take as long as it needs. But ensure that every run ends." The 45-min research cap, the 30-min verifier cap, the ~3 h main-run watchdog and the phase time estimates are gone. Termination is guaranteed by structure: finite work lists (slices, findings, the will-publish set), one continuation per research domain, the 8-iteration verifier cap with fail-open, one retry per fetch, three push attempts, nothing self-re-spawns. The only timing rule is hang detection on **inactivity**: 60 minutes with no write under `work/<run-id>/` and no completion notification = stalled. Sub-agents append a line to `work/<run-id>/<domain>.progress` (research) or `verify.iter<N>.progress` (verifier) per unit finished so a working agent is never mistaken for a hung one. The Phase 7 publish poll keeps its 10-min bound because it is how a run ends, not a work limit.
2. **Numbers are guides.** "Do not force the runs to produce certain amount of entries. No entry is also okay... there can be multiple critical per day or days with nothing. Same for the topic rotation and so on... the agent can judge itself." Zero entries is a healthy run. Several criticals or deep dives in a day are correct when each clears its bar; none is equally normal. Deep-dive category rotation is a tie-breaker, never a reason to pass over the most deserving item. Slice size (~10–14), campaign cadence (~1 update/week), candidate sources (~1/run), audit batches (~20) and the audit window (~21 days) are all guides.
3. **Gate:** `check_run.py` `RUNAWAY_RUN_SECONDS` moved 3 h → 24 h (stall class only); the 14 acknowledgment rows for 3–24 h runs became dead and were pruned by the 2026-09-29T2134Z-audit.

**Why:** the operator wants depth and completeness never traded for a clock, and wants the agent's judgement, not arithmetic, to decide volume and treatment.

**How to apply:** never cut, rush or sample work because of elapsed time; never add a count-based rule; when a number appears in a prompt, read it as the typical case unless it is one of the termination bounds above. Related: [[operator-directives-2026-08-28]], [[scheduler-and-workflow-races]].
