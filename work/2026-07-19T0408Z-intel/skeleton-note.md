# Run skeleton scratch — 2026-07-19T0408Z-intel

- model: Claude Opus 4.8 / claude-opus-4-8
- prompt_version: v3.28
- gap_hours: 16 (prev run 2026-07-18T1208Z-audit started 2026-07-18T12:08:23Z)
- window_hours: 24 (floor), developing_window_hours: 72
- window class: Standard (12-30h) — no coverage-window disclosure line needed
- intel drops: none (README only) → no S5
- ATT&CK pin: v19.1 (up to date)
- watchlists: none configured → sweep lines omitted
- fetch_gaps_in_window: [] → no rotation priorities

## Heavy recent coverage to dedup against (do NOT republish as new):
- SharePoint cluster (CVE-2026-58644 confirmed exploited/KEV, 55040, 55944, 50522, 32201, 56164)
- VMware Avi Load Balancer VMSA-2026-0005 (07-18, 8 CVEs)
- Siemens RUGGEDCOM ROX II Unit42 chain (07-18)
- SonicWall SMA1000 UTA0533 kill chain (07-18 deep dive, 15409/15410)
- WordPress WP2Shell pre-auth RCE chain (07-18, 63030/60137)
- Moodle local_o365 JWT forgery (07-18, 54733)
- GoServpent backdoor / TetrisPhantom (07-18)
- Abbott/Exact Sciences ShinyHunters vishing (07-18)
- Metro Mondego TheGentlemen ransomware (07-18)
- Contagious Interview OtterCookie SVG stego (07-18)
- Oracle EBS CVE-2026-46817 KEV (07-16)
- Joomla file-upload RCE wave (multiple)
- M365 identity attacks, npm supply-chain wave, AI-abuse tradecraft
