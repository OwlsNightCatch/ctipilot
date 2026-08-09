# Run 2026-08-09T0412Z-intel — main-agent working notes

- started: 2026-08-09T04:12:38Z
- prompt_version: v3.30 (CHANGELOG head 3.30)
- model: Claude Opus 5 / claude-opus-5 (harness-injected model line)
- previous run: 2026-08-08T0409Z-intel, started 2026-08-08T04:09:55Z, publish_status ok
- gap_hours: 24 (24.05 exact) -> window_hours: 26, developing_window_hours: 72
- window class: Standard (12-30 h) -> no coverage-window disclosure line required
- intel/ drops: none in window -> no S5
- watchlists: none configured (products / suppliers) -> no `Watchlist:` line
- prior coverage loaded: 148 records, 14-day window, all summaries read into main context
- rolling 24 h before this run: 14 operational entries (incident 2, vulnerability 4,
  research 2, threat 1, annual-report 1 + 4 updates), 0 deep dives today, 0 critical
- deep-dive rotation, last 14 days: annual-report (07-29), other (07-30),
  apt-campaign (07-31, 08-01), identity-infra (08-04, 08-07), web-app-rce (08-05),
  supply-chain (08-06)
- rotation-priority sources promoted to slice tops: prodaft, ssd-disclosure
- sources.promotion_due: nl-times (7 contributing runs) -> promote to active in Phase 5
- ATT&CK pin: enterprise-attack v19.1, 697 active techniques (local check ok)

## Sub-agent spawns (Phase 1)

S1 active-breaking/vulns/vendor-psirt (24 sources: 11 essential + 13 rotational)
S2 ch-eu/gov (26 sources: 13 essential + 13 rotational)
S3 research/news/discovery/ot-ics (13 rotational)
S4 breaches/news/ransomware/sanctions (13 rotational)
All 15 active essential sources are covered by the union of S1 and S2.
