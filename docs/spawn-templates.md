# Sub-agent definitions

As of prompt v2.38, the daily and weekly routines spawn **named custom sub-agents** instead of `general-purpose` with verbatim prepended templates. The full operational system prompts live in the canonical sub-agent files under [`.claude/agents/`](../.claude/agents/) and are loaded automatically by the Claude Code harness when the main agent calls `Agent` with the matching `subagent_type`.

| Sub-agent | File | Used in |
|---|---|---|
| `cti-research` | [`.claude/agents/cti-research.md`](../.claude/agents/cti-research.md) | Daily Phase 1 (S1–S4 parallel research workers) · Weekly Phase 2 (W1–W2 horizon research) · Phase 4.5 / Phase 3.5 follow-up research (max 3 per verification iteration) |
| `cti-verification` | [`.claude/agents/cti-verification.md`](../.claude/agents/cti-verification.md) | Daily Phase 4.5 · Weekly Phase 3.5 — cold-reader URL-truth + editorial-quality verifier, looped iteratively (cap 3, fresh spawn each time) |

Both sub-agents are defined to run on **Sonnet** with isolated context windows so the main agent (typically Opus) keeps its budget for composition, state update, and the publishing chain.

The sub-agent definitions embed everything the routine previously prepended verbatim from this file:

- defender-vantage opener
- link-discipline clauses
- MANDATORY bridge-fetcher rules for known-403 hosts (CISA / NCSC.ch / CSIRT Italia / UK ICO / Inside IT / PRODAFT / DataBreaches / NCC Group / occasionally Cisco Talos)
- `WebFetch` outbound-links prompt template
- empirical findings on `WebFetch` behaviour (listing pages return zero outbound links; Krebs feed returned 13 outbound links from one article in our test; CERT-FR per-advisory pages carry vendor citations in "Documentation"/"Références"; same shape for BSI WID-SEC, NCSC-NL, NCSC-CH CSH, ENISA EUVD; `<content:encoded>` RSS preserves outbound links while `<description>`-only RSS does not)
- Discovery-trace requirements
- Sub-agent return format (research) and verifier return format with finding categories F1–F11
- Operational guardrails (fetch budget, wall-clock cap, always-return-something rule)
- Read-only constraint on the verifier

## What the main agent passes per spawn

Because the system prompt is now embedded in the sub-agent definition, each `Agent` spawn message is **short** — a thin per-domain envelope around what's already loaded:

**For `cti-research`:**
- Run id (`YYYY-MM-DD-HHMM`) so the sub-agent knows which `work/<run-id>/` directory to checkpoint into.
- Recency window (`window_hours: <N>` for daily, `window_days: <N>` for weekly).
- Domain — one of S1 / S2 / S3 / S4 (daily) or W1 / W2 (weekly), with the source-filter description.
- Source-list slice — the `status: active` subset of `sources/sources.json` matching the domain's category filter.
- Dedup context — CVE IDs from `cves_seen.json`, named entities from `covered_items.json`, headlines from prior briefs in scope.
- Rotation-priority list — sources flagged by Phase 0 as gaps in 2+ recent briefs, filtered to the domain's category.
- Today's ISO date.

**For `cti-verification`:**
- Brief or summary path.
- Iteration number (1, 2, or 3) so the report titles itself correctly.
- Run kind (`kind: daily` or `kind: weekly`) so the verifier applies the right whole-brief checks (W-PD-1 for weekly).
- Dedup context (same as Phase 0 built).
- Relevant slice of `state/run_log.json` (today's `sub_agents`, `fetch_failures`, `items_published`).

Do **not** duplicate the system prompt content in the spawn message — the sub-agent already has it.

## When to update the sub-agent definitions

Per the daily prompt's META — self-evolution authority section, the routine has full authority to edit `.claude/agents/cti-research.md` and `.claude/agents/cti-verification.md` when doing so improves future runs (a new bridge target, a new known-403 host, a recurring URL pattern that should be in the bad-Source allowlist, an empirical finding about `WebFetch` behaviour, a new check class for the verifier). Treat them like any other prompt file: bump `prompts/CHANGELOG.md` in the same commit, surface the change in the run's commit body.

Hard invariants that must never be removed from the sub-agent definitions:

- `cti-research`: link-discipline clauses, bridge-fetcher rule for known-403 hosts, `WebFetch` outbound-links template, Discovery-trace requirement, "always return something" rule.
- `cti-verification`: read-only constraint (no `Edit` / `Write` in tools), iterative refinement requirement (the looping happens in the main agent — the sub-agent itself just returns findings and a verdict).
