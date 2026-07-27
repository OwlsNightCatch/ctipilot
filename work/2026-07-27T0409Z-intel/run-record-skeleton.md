# Run-record scaffolding — 2026-07-27T0409Z-intel

Phase 0 facts (frozen):

- run_id: 2026-07-27T0409Z-intel
- kind: intel
- date: 2026-07-27
- started: 2026-07-27T04:09:04Z
- model: Claude Opus 5 / claude-opus-5 (harness-injected model line; env CLAUDE_FRIENDLY_NAME/CLAUDE_MODEL_ID agree)
- prompt_version: v3.29 (CHANGELOG head 3.29 — matches)
- previous run: 2026-07-27T0110Z-weekly, started 2026-07-27T01:10:13Z, publish_status ok
- gap_hours: 2.98 -> 3
- window_hours: max(24, 3+2) = 24  (hard 24 h floor)
- developing_window_hours: max(72, 3+24) = 72
- window class: intraday (gap <= 12 h) — no coverage-window disclosure line required
- prior coverage: 122 records over 14 days
- window24h snapshot: operational_total 10 (vulnerability 3, threat 1, research 2, updates 4),
  deep_dives_today 0, critical_count 0, high_count 1
- intel/ drops: none (README only) -> no S5
- ATT&CK pin: local v19.1 == upstream latest v19.1 (up to date)
- jina reader pool: trial_balance 10,000,000 — RECOVERED after four consecutive runs
  reporting HTTP 402/401 exhaustion (2026-07-23/24/25/26). Note in the record.
- sources.promotion_due: zscaler-threatlabz (3 contributing runs, last 2026-07-26T2309Z-weekly)
  -> flip to status: active in the Phase 5 source pass and record in sources_changed[].
- fetch_gaps_in_window (rotation priority): cisa-advisories (403 x2), jina-reader-pool (402 x4)

Sub-agent spawn set: S1, S2, S3, S4 (no S5).
