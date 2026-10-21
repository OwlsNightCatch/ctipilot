---
name: operator-directive-2026-10-21-parallel-waves
description: "v4.23 operator directive: cleanup waves run in parallel, one session per wave, on lanes the tracker keeps disjoint (ready status, after list, render_status.py --check-lanes); claims carry wave=<NN>; merge_state.py merges plan.json, legacy_review.json and re-renders STATUS.md"
type: feedback
---

# Operator directive 2026-10-21 (shipped as prompt v4.23)

The operator asked that the cleanup waves be parallelized so that three new waves can start at once, beside wave 02, which was still in flight.

**Why:** the program had about ten sequential waves left. Running them one at a time would take weeks, and their scopes are mostly disjoint.

**How to apply:**
- Start a wave with "Read `prompts/cleanup-coordinator.md` on `main` and run cleanup wave <NN>." Only a wave the tracker marks `ready`, whose `after` waves are done, and for which `python3 work/cleanup/render_status.py --check-lanes` passes.
- The claim reads `partial <STARTED> wave=<NN>`. The claim commit also marks the wave `in-flight <run-id>` and its rows `in-wave <NN>` in `work/cleanup/plan.json`, so the other sessions see the lane taken.
- A wave touches only its own rows' entries. A legacy batch is its row's entry list, never `legacy_review.py --next`.
- Shared-file conflicts go to `python3 tools/merge_state.py resolve`, which merges plan.json and legacy_review.json and re-renders docs/cleanup/STATUS.md.
- The account-wide session limit is the risk the operator accepted. Every wave keeps its 20-spawn cap, and a rate-limited wave is cut, never retried in a loop.
