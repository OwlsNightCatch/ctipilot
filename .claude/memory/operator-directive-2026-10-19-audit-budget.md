---
name: operator-directive-2026-10-19-audit-budget
description: "v4.21 operator directive: audits must not overrun the session limit — one audit at a time (claim on main), primary work = the trailing week, at most 20 sub-agent spawns per fire, verifier loop checks only the fire's own changes, legacy queue and store-wide duplicate scan only in operator-directed partial audits"
type: feedback
---

# Operator directive 2026-10-19 (shipped as prompt v4.21)

The operator's words: "All three audits ran in their own sessions and did not share a limit and overrun the overall session limit. Ensure the audits work and that they focus on the primary work and that is auditing the previous week. All other work should only be done when this is successfully pushed and live. Ensure audits do not overrun their session limits anymore."

**Why:** the 10-04, 10-11 and 10-19 audit fires ran concurrently; the 10-11 fire alone spawned 55 sub-agents (17 for truth passes, re-sweeps, legacy and duplicate work, 38 verifier slices of about 0.6 M tokens each) and stood paused eight days on the session limit. The verifier loop re-read every claim of all 117 touched entries (about 1,900 claims) each pass and never converged, because each pass found new low-confidence nits in legacy text the fire had not written.

**How to apply:** `prompts/quality-audit.md` § Session budget. Claim the audit on `main` before the first spawn (`work/<run-id>/audit.claim`), stand down on a live claim under 48 h old, stand down as `superseded` when a later audit claims over a paused one. At most 20 spawns per fire, logged in `budget.tsv`. `work/<run-id>/base.sha` makes `tools/claim_ledger.py` list only the claims the fire changed. Findings on text the fire did not change are `(pre-existing)` advisories for the next audit, except an unsupported fact (F4). Legacy batches and the store-wide duplicate scan are secondary work. In an interactive session, finish the audit and confirm it is live before doing any other work.
