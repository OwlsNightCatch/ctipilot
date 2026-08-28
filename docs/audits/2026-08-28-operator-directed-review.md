# Operator-directed review — 2026-08-28 (run 2026-08-28T1500Z-audit, prompt v4.2)

Interactive session on the operator's sandbox (read-only git — the operator stages and commits on the host). Directives: review the 2026-08-28T0409Z fire's findings; keep pipeline internals out of reader-facing text; corrections get no new timestamp; quality over quantity; English-only output including quotations; generic `sonnet` model pins; confirm the operator-named critical sources (NCSC-CH, Heise Security, Inside-IT) deliver article detail.

## Systemic finding

The first Sonnet 5 intel fire (2026-08-28T0409Z, 36 entries) had one recurring editorial defect class: **composition-rationale narration in reader-facing text**. Most entries carried sentences addressed to a reviewer rather than a responder — "`actions[]` is empty because…", "`techniques[]` maps only… to avoid overstating", "per this pipeline's house rules", registry keys in prose, "as of this run". A metadata-only correction on the Lazarus AFD.sys entry additionally rendered its record-field mechanics as a reader-facing `## Correction` section and re-floated a 16-day-old entry to the top of /live/. Root cause addressed in the prompts (v4.2), not just the instances.

## Fixes shipped (working tree — operator to commit)

1. **v4.2 lifecycle mechanics** — `internal: true` changelog records (changelog-only, no section, never rendered); `updated_at` mirrors only the last non-internal `type: update` record. Code: `site/content_model.py`, `site/build.py`; normative: `docs/pipeline.md`; rules: both master prompts, `cti-verification.md`, `CLAUDE.md`. Migration: 8 entries' `updated_at` recomputed; Lazarus correction converted to internal; Gemini CLI correction section rewritten reader-facing (the CVSS 4.0 10.0 vs CVSS 3.1 7.8 divergence is the intel; the record-field narration was not).
2. **Editorial pass over all 36 new entries + 2 older ones** (two read-only review sub-agents, fixes applied centrally): internals removed, worst padding cut (details in each entry's git diff; every touched entry carries one internal `improvement` record, run id `2026-08-28T1500Z-audit`). Two stale/overlong `actions[]` lists trimmed (Keycloak — one action contradicted the entry's own 2026-08-24 correction; Unit 42 autonomous-AI — two actions merged). One wrong word fixed ("chipset-free" → configuration-driven, ownCloud entry).
3. **English-only quotations** — German/French quotes in the Martigny, SUEZ, Protection Civile and Berlin Landesnetz entries replaced with marked English translations; verbatim originals preserved in `evidence[].original` (new optional field) so verification can still match them against the fetched pages. Rule + verifier contract updated.
4. **Model pins** — `cti-research` / `cti-verification` now pin `sonnet` (generic alias).
5. **Prompt hardening for Sonnet 5** — explicit scope statements ("every entry, not the first one"), a positive model of a complete short entry, the defect sentence-shapes named for deletion, PD-11 rebalanced (sound throughout; complete on critical/high; below that, shorter or not at all). `.claude/settings.json` sets `"outputStyle": "Concise"`.
6. **Sources** — `heise-sec`, `inside-it-ch` promoted to `tier: essential` (neither was attempted by the 08-28 fire under rotation; heise last contributed 2026-06-20). NCSC-CH is healthy (essential, fetched and used via the Security Hub API recipe).
7. **Zero-warning discipline** — 2 warnings fixed (action lists), 3 acknowledged in `state/warning_acknowledgments.json` (Unisoc aggregator-only sourcing pending reader-pool refill; two research entries with genuinely no TTP content).

## Verification

Four `cti-verification` iterations (Sonnet 5, internal-consistency only — the sandbox has no external network, so URL-level truth checks fall to the next network-enabled audit). Iterations 1–3 each caught genuine remediation gaps (a dropped fact in the Taiwan attribution compression, a hedge silently upgraded in the kernel-KEV entry, two missed evidence translations, a systemic `fields[]` inaccuracy fixed by recomputing all records from the git diff, leftover self-references); iteration 4 confirmed everything CLEAN with zero findings. Final gate: `check_run.py 2026-08-28T1500Z-audit` — 40 pass · 0 fail; the two surviving warnings (session duration; the documented confirmation waiver) are this run's own telemetry facts for the next audit's sweep. Two of the 0409Z fire's 7 residuals were also resolved along the way (DOJ 2018-dating splice; YOOtheme spliced quote — fixed in both evidence[] and body).

## Operator action items

- **Refill the jina reader keys** — the 08-28 fire exhausted all 7 (`JINA_API_KEYS`); heise article bodies are reader-dependent (`fetch_method: jina`, TollBit-gated direct), so Heise is headline-only until refilled. `ssd-disclosure` was also lost to the dead pool this fire.
- This sandbox's egress allowlist blocks all non-Anthropic domains, so live probes of heise/inside-it/bacs were not possible from here; the promotion to essential plus the next fire's telemetry will confirm delivery end to end.

## Backlog for the next scheduled audit

- Pre-v4.2 entries (July–August) still carry internal jargon (PD-numbers, `cves[]` mentions) in bodies/sourcing notes — mostly retired weekly entries; sweep opportunistically, archived strategic entries lowest priority.
- Non-English quotes remain in pre-directive entries (e.g. `2026-08-23/weekly-w34-the-disclosure-arrived-the-facts-did-not`); translate on next touch.
- The 08-28 fire's 7 fail-open verification residuals (flagged in its run record, iteration 6) still need the audit's disposition; this session's editorial pass did not adjudicate them.
