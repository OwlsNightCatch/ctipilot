---
name: Auto-commit/push/deploy for routine fixes
description: User wants routine site/tooling fixes committed, pushed, and deploy-verified without asking each time
type: feedback
---

For routine fixes in this repo (site/build.py, tools/check_run.py, prompt
edits with version bump, doc fixes, similar low-risk in-repo changes), do
the full commit → push → auto-merge wait → deploy-site wait → live URL probe
chain end-to-end without pausing to confirm. Do not stop at "ready to commit"
or "ready to push" and ask the user.

**Why:** the user runs me in auto mode for this repo and treats the
publishing chain (feature branch → auto-merge-claude.yml → main →
deploy-site.yml → ctipilot.ch) as the *expected* finish line for any code
change. Stopping mid-chain forces them to type "commit and push" or
"deploy" to resume — that's pure friction.

**How to apply:**

- After any in-repo edit that fixes a defect or adds a small improvement,
  proceed straight from "tests pass" to commit / push / wait / verify.
- Use the chain documented in CLAUDE.md (sync main → stage specifics → commit
  → second sync → push with retry → poll auto-merge run → poll deploy-site
  run → live URL check). `gh` is available locally; use it for run status,
  fall back to polling if it ever isn't.
- Always include `.claude/memory/` in the staged file list when memory was
  touched in the session.
- **Do still pause** for: destructive operations (force-push, branch delete,
  rm -rf of state files), changes that touch shared infrastructure
  (workflows, branch protection, CNAME), edits that materially change
  editorial policy without a clear user request, or anything I'd flag as
  risky under the system prompt's "executing actions with care" guidance.
- The "user is in auto mode" reminder applies equally — assumption is they
  want momentum, not check-ins.
