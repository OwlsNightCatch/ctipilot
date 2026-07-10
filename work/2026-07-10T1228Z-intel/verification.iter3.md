**Model:** Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-10T13:21:47Z · ended_at=2026-07-10T13:24:33Z · duration_seconds=166

## Verification report — 2026-07-10T1228Z-intel (iteration 3)

Cold read of 4 entries + run record. Focus: confirm the two iteration-2 (Sonnet/alt) remediations held; full cold truth pass otherwise.

### Prior-iteration deltas — both CONFIRMED FIXED

**Delta 1 (F4, comment-stuffing) — FIXED.** `techniques: [T1566.001, T1027]`. Both ids present in the pinned `attack/enterprise-attack.json` and neither deprecated nor revoked (T1027 "Obfuscated Files or Information", T1566.001 "Spearphishing Attachment"). Body maps T1027 to the "`\uXXXX`-escaped `document.write()` wrapper" obfuscation and explicitly disclaims the Binary Padding (T1027.001) scan-size-evasion mechanism ("this is not the MITRE 'Binary Padding' scan-size-evasion play"). No re-claim of the disclaimed mechanism. All three SANS ISC evidence quotes verified contiguous-verbatim on isc.sans.edu/diary/33144 (dilution/no-longer-flags, takes-too-long/release-it, low-entropy/blend-in).

**Delta 2 (F3, gitea) — FIXED.** Rewritten paragraph accurately reflects both fetched articles. The Hacker News carries the recon-only caveat: fetched page contains verbatim "So far, the activities have been related to initial investigation by the threat actor" and "it has not so far progressed to any exploitation or attack progress" (both inline quotes contiguous-verbatim). SecurityWeek frames the same Sysdig telemetry aggressively ("Under Active Exploitation", "first in-the-wild hit 13 days after the advisory", "VPN-exit scanner that grabbed access") and omits the recon caveat — matches the entry's characterisation. NCSC-CH evidence quotes ("Actively Exploited"/"Proof of Concept Available", "full administrative control … single custom HTTP header") confirmed present via `fetch_source.py ncsc-csh post 12755`. Classification A2 sound (A-tier national authority, single-authority uncorroborated active-exploitation claim → credibility 2).

### Cold pass — no new defects

- **helix**: quotes plausible and standalone-verbatim style; entities actor:helix-extortion / actor:unc6671 / actor:shinyhunters all present in registry; `references` target 2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns exists on disk; attribution correctly hedged ("likely", B2). techniques T1566.004/T1528/T1098.005/T1213.002 supported by body.
- **injectivelabs**: primary source is a specific Aikido blog post with slug (not a landing page); all three evidence quotes plus 50,000-weekly-downloads and the 17-sibling-packages figures verified verbatim on aikido.dev; incident entity injectivelabs-npm-sdk-ts-supply-chain-2026 registered; B2 sound; techniques T1195.002/T1056.004/T1132.001/T1041 supported.
- **Classification (F17)**: all four entries carry a valid Admiralty block (A2, B3, B2, B2); no entry unrated; codes in vocabulary; letters/numbers consistent with cited-source nature and corroboration.
- **Org-triage / watchlist (F16)**: no triage scheme and no watchlists configured; all four carry `org_triage: null` and `watchlist_hit: false`. Compliant.
- **Relevance/priority**: all four clear the Swiss-federal-SOC bar (Gitea DACH public-sector DevOps; Helix SharePoint/Entra ID default stack; two research entries transferable tradecraft). high/high/notable/notable calibrated correctly — no false critical, no under-alert.
- **Style**: IOC-clean across all four (no hashes/IPs/domains/rule code); English; no workflow-internal language.

Coverage looks complete for the window; no missed-angle gap identified.

### Verdict

CLEAN
