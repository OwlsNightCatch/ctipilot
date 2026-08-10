# W1 checkpoint notes

## Job1 npm wave
- keyv/cacheable compromise (Aug 4 2026) = CHAINDROP (campaign:shai-hulud-chaindrop-2026-08, already covered 08-06 Elastic, 08-08 Unit42).
- WEEK-LEVEL DELTA: massive cross-vendor convergence — Socket, Datadog, Snyk, Wiz, Aikido, Orca, Cloudsmith, safedep all published Aug 4-5.
  - Socket unique finding: host-level dead-man's switch (gh-token-monitor LaunchAgent/systemd) that evals remote handler on token revocation — hunt BEFORE rotating creds. Scale: ~444 packages / 2,234 poisoned versions. Detection avg 5m18s.
  - Datadog: forensic Git timeline, provenance/Rekor entry 09:29-09:35, keyv@6.0.0 published 09:35.
- Socket also: Miasma/Mini-Shai-Hulud/Hades (Jun 25 - OUT OF WINDOW), PolinRider (Jul 1 - OUT OF WINDOW).
