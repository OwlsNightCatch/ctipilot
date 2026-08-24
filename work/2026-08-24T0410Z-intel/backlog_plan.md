# Backlog disposition plan — run 2026-08-24T0410Z-intel

`state/coverage_backlog.md` carried 8 open rows at the start of this run. Six were
handed over by the 2026-08-24T0110Z weekly stand-down (`disposition: duplicate-week`),
already deep-read and literal-substring-verified by that fire; their extracted facts and
corrected quotes survive in `work/2026-08-24T0110Z-weekly/deepread.yaml` (the raw page
bodies referenced there were not committed, so each primary is re-fetched in this run's
Phase 4 deep read before composition).

Backlog rows are exempt from the recency gate (PD-7): each was verified in-window by the
fire that surfaced it, and its age reflects a pipeline race, not staleness. Every row is
still put to the relevance gate on today's facts and deduplicated against the 14-day
prior-coverage index.

## Publish this run

| Row | Disposition | Planned shape |
|---|---|---|
| ShieldBreak mechanism + hunting package (LevelBlue SpiderLabs, 2026-08-19) | PUBLISH | `update_of: 2026-08-18/cve-2026-69414-shieldbreak-defender-acknowledged-no-fix` — CVE-2026-69414 is already in `state/cves_seen.json`, so a fresh entry carrying it would trip the CVE-duplicate FAIL. Note: the LevelBlue post names no CVE anywhere (confirmed by case-insensitive grep of the full body during the weekly's deep read) — the link to CVE-2026-69414 is this pipeline's reading of two accounts of the same named technique, not a claim either source makes, and must be framed as such. |
| SynkLoader (Expel, 2026-08-20) | PUBLISH | new `threat` entry |
| Rapid7 Labs Quarterly Threat Landscape Report Q2 2026 (2026-08-18) | PUBLISH | new `annual-report` entry; register `report:rapid7-quarterly-threat-landscape-q2-2026` |
| Truffle Security — leaked corporate AWS keys (2026-08-19) | PUBLISH | new `research` entry |
| SOCRadar — FTP banners as dead-drop resolvers, E4del + PINHOLE (2026-08-21) | PUBLISH | new `research` entry; register the two malware families |
| Keycloak CVE-2026-18963 product-state correction | PUBLISH | `update_of: 2026-08-19/cve-2026-18963-keycloak-reset-credentials-account-takeover` — corrects a published error that overstates exposure. Red Hat's product-state table re-parsed from the weekly's saved page in this run: 11 Fixed rows, 2 Not-affected rows; the JBoss EAP Expansion Pack is `Not affected` / `Component not Present` and Red Hat Single Sign-On 7 is `Not affected` / `Vulnerable Code not Present`. Structured evidence persisted at `work/2026-08-24T0410Z-intel/pages/redhat-cve-2026-18963-product-states.json`. |
| SilkParasite dedicated coverage + registry entities (Bitdefender, 2026-08-19) | PUBLISH if budget allows | new `threat` entry; registers five new malware families the store lacks. Lower priority than the six above per the row's own note. |

## Stay open

| Row | Why |
|---|---|
| Zurich LockerGoga / MegaCortex / Nefilim verdict | Verdict is set for 2026-09-10. The row's own instruction is to publish nothing procedural before it. |
| Berlin Landesnetz compromise | Still blocked on the same ground for a fifth consecutive fire: no named authority states an access vector, product or CVE, and an `incident` entry needs an evidence-bound technique mapping. S2 was tasked to re-check this precisely. |
| SSD Secure Disclosure — Unisoc VoLTE-to-kernel chain | Still blocked on transport. The only rung that has ever read this host is the jina reader, and all 7 pool keys are credit-exhausted this run (`live_key_count: 0`, HTTP 402). No new transport invented. Strike at the ~30-day mark (2026-09-17) if the pool has not returned. |
| 1Password "FLAWED" LLM-patch study | Marginal on its own row's assessment; ~30-day strike date is 2026-09-09. |
| Joint advisory AA26-231A (Siemens S7 PLCs) — re-read the primary | Narrow residual: only passages the published entry does not quote. Not a coverage gap. |
| Swiss federal cyber authority half-year 2026 report | Row expected this fire to miss the 09:00 UTC embargo lift. The container stalled ~4.7 h between preflight and Phase 1, which put S2 on the publication instead — S2 was re-tasked mid-flight to fetch it. Disposition decided on what S2 returns. |

## ATT&CK ids validated against the pin (v19.2) before composition

Checked live/active, with two revocations caught that would have FAILed the gate:
`T1574.002` (DLL Side-Loading) is **revoked → T1574.001** (DLL), and `T1562.001`
(Disable or Modify Tools) is **revoked → T1685**. `T1656` (Impersonation) is likewise
revoked → `T1684.001`. Active ids confirmed for use: T1574.001, T1053.005, T1036.005,
T1036.008, T1027.007, T1027.013, T1106, T1566.003, T1204.002, T1204.004, T1056.002,
T1090, T1572, T1113, T1082, T1018, T1059.001, T1071.001, T1102, T1102.001, T1102.002,
T1552.001, T1078.004, T1580, T1055.001, T1055.004, T1497, T1564.004, T1547.001, T1190,
T1556, T1047, T1573.001, T1620, T1685, T1684.001, T1021.005, T1219, T1105, T1140.
