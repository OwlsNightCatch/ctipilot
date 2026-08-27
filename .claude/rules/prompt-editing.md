---
paths:
  - "prompts/**"
  - ".claude/agents/**"
---

# Editing the master prompts and agent definitions

Moved verbatim from the root `CLAUDE.md` (2026-08-27) — loads only when a session works with files under `prompts/` or `.claude/agents/`.

## Editing the master prompts — versioning rule (ALWAYS)

Any edit to `prompts/cti-run.md`, `prompts/quality-audit.md`, `prompts/verification.md`, `prompts/entry-template.md`, `prompts/check-run-fixes.md`, or any `.claude/agents/*.md` MUST ship all three of: banner bump + `prompts/CHANGELOG.md` entry (`### Why` / `### What changed` / `### What stays`) + the edit itself, in the same commit. Both banner-versioned master prompts (`cti-run.md`, `quality-audit.md`) move in lockstep. **Exemption:** ORG-PROFILE block regeneration after a config-value change is not a prompt edit. `check_run.py` cross-checks the run record's `prompt_version` against the CHANGELOG head and FAILs on mismatch.

### Intel-run ↔ audit — shared machinery lives in one place; the lens stays divergent (ALWAYS)

v3 ended the v2 copy-drift problem structurally, and v4 keeps the pattern with one dependent: `prompts/quality-audit.md` **builds on** `prompts/cti-run.md` (it instructs a runtime `Read` of the intel-run prompt and defines only the audit divergences — retrospective truth passes, coverage re-sweeps, systemic review, the fix classes, the report). Shared machinery (anti-crash guards, PD-1…13, composition discipline incl. § Updating an existing entry, state lifecycle, gate, verifier loop, publishing chain) is edited ONLY in `cti-run.md`. When an edit to `cti-run.md` changes a phase contract the audit references, re-read `quality-audit.md` in the same commit to confirm the reference still holds.
