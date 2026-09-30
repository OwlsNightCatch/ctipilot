---
name: setup-review-2026-09-29
description: Operator-directed whole-setup review (v4.17) — what the measurements showed and the mechanisms added; read before changing the verifier loop, priority bars, backlog rules or state-file merging
type: project
---

# Whole-setup review, 2026-09-29 (prompt v4.17)

Operator directive: review every detail and fix/improve everything so ctipilot gives human and agent readers the most actionable intelligence. Six parallel reviews (prompts/docs, tools, entry quality, site, sources, run telemetry); findings and fixes are in `prompts/CHANGELOG.md` 4.17. The non-obvious deltas:

- **The verifier loop was a sampler.** Sept 2026: 15 of 27 fires hit the 8-iteration cap, 4 confirmed double-CLEANs, iteration 1 found 23% of all findings, 8 of 14 CLEANs refuted by the next pass. Fix: `tools/claim_ledger.py` + every pass answers for every claim in scope (`verification.iter<N>.claims.yaml`); an incomplete pass's CLEAN never counts. If the loop still does not converge, look at claim coverage first (`--coverage N`), not at adding passes.
- **`high` was graded on event size.** 43% high in the 09-16..29 window (a $388M crypto theft, a US military data breach). Fix: the `high` bar in cti-run.md Phase 4 (constituency exposure + a 7-day decision; disqualifiers) and the incident floor (no vector/actor/behavior ⇒ routine, two sentences). About a quarter high is the audit's alarm level, never a cap.
- **Updates left the main text stale.** Six entries contradicted their own update sections. Fix: mandatory supersession sweep (Phase 4 § Updating step 4) + verifier 4c(h) + `exploitation-consistency` WARN. Recounting unchanged source material is a `correction`, never an `update` (it re-floated Oracle's entry as news).
- **The backlog became a carry-forward dump** (70 KB, one row with 23 "no change" notes, a CVSS 10.0 IBM MQ row held while saying it cleared PD-11). Fix: every row is published, struck, or held with a named, dated condition and a 14-day expiry; no carry-forward notes.
- **Whole-file `--ours`/`--theirs` lost data** on concurrent merges (a concurrent fire's entities vanished while its entries referenced them). Fix: `tools/merge_state.py` in the workflow, Phase 6 and session start.
- **Actionability contract**: every entry closes with `**Exposure:**`, `**Detection:**`, `**Triage:**` (honest only), `**Defender takeaway:**`; the site lifts the labels; agents read them.
- **Source gaps**: no vendor PSIRT for Palo Alto, Fortinet, Ivanti, SAP, GitLab, Siemens, and the MSRC update guide was unused; BACS press releases missing. Added (PSIRT feeds verified by direct fetch). heise bodies now read with `extract` (no reader).
- Tools now take "now" from the run id / `--now "$STARTED"` (verified clock), the intel window anchors on `runs.last_intel_run` (the audit shrank Monday windows), and a failed fetch no longer advances a source's rotation cursor.
