## Verification report — briefs/2026-05-22.md (iteration 1)

**Model:** Anthropic Claude Opus 4.7 (`claude-opus-4-7`)
**Started:** 2026-05-22T06:40:29Z · **Ended:** 2026-05-22T06:46:02Z · **Duration:** 333s
**Verdict:** NEEDS_FIXES (truth: 4, editorial: 4, advisory: 1)
**URLs checked:** 14 · WebFetch calls: 15 · Bridge fetches: 3 · WebSearch calls: 6

### F1 — Hallucinated "September 2016" date [truth]
- § 1 heading + § 5 Background: "active since at least September 2016"
- All cited sources say "mid-2022". Lumen primary explicitly: "since at least mid-2022". Brief internally contradicts itself (§ 5: "telemetry beginning in mid-2022").
- Fix: change "September 2016" → "mid-2022" in § 1 heading and § 5.

### F2 — TL;DR misattributes Phobos RaaS link to Eurojust [truth]
- TL;DR bullet: "Phobos RaaS infrastructure link confirmed ([Eurojust, 2026-05-21]...)"
- Eurojust press release does not mention Phobos RaaS. That detail is from Help Net Security (cited in § 1 footer).
- Fix: change TL;DR inline citation to Help Net Security; add Help Net Security inline citation in § 1 body sentence on Phobos link.

### F3 — "pre-authenticated" inverts threat model [truth — CRITICAL]
- § 0 callout, § 0 footer, § 2 heading, § 2 body, § 2 footer all say "pre-auth"
- JPCERT (cited primary) says "authenticated attacker"; HKCERT clarifies attacker must already hold admin credentials to Apex One server.
- Fix: change "pre-authenticated" → "authenticated (admin credential required)" throughout; update Auth footer tag to "post-auth".

### F4 — 373/169 figure misattributed to StepSecurity [truth]
- § 4 UPDATE TeamPCP: "373 malicious package versions across 169 npm packages … ([StepSecurity, 2026-05-21])"
- StepSecurity post does not contain that aggregate. Figure appears in Unit 42.
- Fix: re-anchor citation to [Unit 42, 2026-05-21].

### F5 — Lumen + PwC primary sources not cited [editorial]
- Lumen Black Lotus Labs blog is reachable: https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms
- PwC red-lamassu blog also reachable: https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html
- § 7 note about Lumen redirecting to homepage was incorrect — the actual blog URL resolves.
- Fix: promote both as primary Sources in § 1 footer and § 5 footer; demote aggregators to Additional. Update § 7 note.

### F6 — Specific technical claims lack inline citations [advisory]
- X.509 SAN/CN / Chengdu / PNG-stego claims in § 1 and § 5 lack inline citation.
- Resolved by F5 once Lumen primary is added.

### F7 — Aggregator-only confidence note missing from § 7 [editorial]
- § 7 coverage-gap note present but no "reduced confidence — only aggregator sources" line.
- Resolved by F5.

### F8 — Country count discrepancy not reconciled [editorial]
- Brief says "33 servers across 27 countries". Eurojust says "more than 33 servers" (>33, not exactly 33). 27 = server-host countries; 16 = taskforce nations; 7 = JIT nations.
- Fix: soften to "33+ servers across 27 countries"; add reconciliation note distinguishing server-host vs. taskforce vs. JIT counts.

### F9 — Missed primary sources (same as F5) [editorial]
- Resolved by F5.
