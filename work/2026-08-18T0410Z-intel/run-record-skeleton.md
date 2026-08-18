# Run-record scaffolding — 2026-08-18T0410Z-intel

Fixed facts established in Phase 0 (carry verbatim into `runs/2026-08-18/2026-08-18T0410Z-intel.md`):

- run_id: 2026-08-18T0410Z-intel · kind: intel · date: "2026-08-18"
- started: "2026-08-18T04:10:17Z"
- model: "Opus 5" · model_id: "claude-opus-5"  (harness-injected model line)
- prompt_version: "v3.31"  (matches prompts/CHANGELOG.md head 3.31)
- gap_hours: 24  (previous run 2026-08-17T0413Z-intel started 2026-08-17T04:13:37Z → 23.94 h)
- window_hours: 26  (max(24, gap+2)) · developing_window_hours: 72
- window class: Standard (12–30 h) → no coverage-window disclosure line required
- previous run publish_status: ok (no dead-fire note needed)
- intel/ drops: none → no S5, no closed-source intake line
- watchlists: none configured → NO `Watchlist:` line (omit)
- Phase 0 window24h snapshot: operational_total 2 (threat 2), updates 0, deep_dives_today 0, critical 0, high 1

Standing constraints to disclose:

- jina reader pool exhausted at run start: 7 keys, 0 live, total_balance −13,774,163 (HTTP 402).
  Fourth consecutive fire in this condition. Every sub-agent was told not to plan around it.
- Rotation-priority sources (missed 2+ recent runs): cisa-advisories, cisa-directives,
  siemens-productcert-csaf, jina-reader-pool.
- sources.promotion_due: acronis-tru (3 contributing runs) → flip candidate → active in Phase 5.

Coverage backlog rows open at Phase 0 (state/coverage_backlog.md):

1. 1Password "FLAWED" LLM-patch study (surfaced 2026-08-10, event 2026-08-06) — marginal;
   30-day strike window still open.
2. Bridewell / BCON infostealer exposure across UK critical national infrastructure
   (surfaced 2026-08-16, event 2026-08-13) — blocked on outlet 403 + exhausted reader.
