---
name: operator-directive-2026-10-20-cleanup-program
description: "v4.22 operator directive: one coordinated, one-time store cleanup program (prompts/cleanup-coordinator.md, tracker docs/cleanup/STATUS.md); sequential waves, each a partial audit merged to main when done; reference branch cleanup/2026-10-18-carry-forward is never auto-merged; ends by retiring the legacy queue"
type: feedback
---

# Operator directive 2026-10-20 (shipped as prompt v4.22)

The operator asked that the cleanup work deferred by the 2026-10-18 audit be preserved on a dedicated branch that is not auto-merged, and that one coordinator session take it up. That session is to clean up everything old or unused in ctipilot, distribute the work to sub-agents and across sessions, and merge each finished piece into `main`, so that afterwards no cleanup of old entries is needed.

**Why:** the trailing-week audit (v4.21) leaves out-of-week defects alone (188 verdicts with 77 factual errors in the 2026-10-18 audit alone, plus 408 unverified legacy entries), and running that work inside the weekly audit is what overran the session limit in October 2026.

**How to apply:**
- Start or continue the program with "Read `prompts/cleanup-coordinator.md` on `main` and continue the store cleanup program."
- One wave per session, at most 20 spawns per wave. Each wave writes a `partial` claim, which the scheduled weekly audit ignores, and yields to the weekly audit's claim. From v4.23 (2026-10-21) waves run in parallel on disjoint lanes: see operator-directive-2026-10-21-parallel-waves.md.
- Each wave ships on its own `claude/cleanup-wave-*` branch, so the auto-merge lands it.
- The reference branch `cleanup/2026-10-18-carry-forward` holds unverified drafts. It is never merged; ports are re-verified and re-recorded under the porting wave's run id.
- The program ends by retiring `quality-audit.md` § Secondary work and `tools/legacy_review.py`.
