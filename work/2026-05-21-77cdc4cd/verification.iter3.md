# Verification report — briefs/2026-05-21.md (iteration 3)

**Model:** Anthropic Claude Opus 4.7 (1M context) (`claude-opus-4-7[1m]`)
**Timestamps:** started_at=2026-05-21T05:10:43Z · ended_at=2026-05-21T05:20:34Z · duration_seconds=591
**Verdict:** NEEDS_FIXES
**Counts:** truth=8 editorial=1 advisory=1
**Self-telemetry:** webfetch_calls=22 websearch_calls=0 bridge_fetches=1 urls_checked=20

> Persisted by the main agent from the verifier's return message (system-reminder blocks the verifier writing report files directly).

## Significant — cold-read surfaced multiple hallucinated technical specifics in the TeamPCP UPDATE

Iteration 3 ran as the odd-iteration cold-read per v2.53 (no prior-iteration deltas block, no pre-bias from iter-1/2 findings). The verifier surfaced 8 truth-class findings, with five (F3–F7) clustered in the § 4 UPDATE TeamPCP / durabletask sub-paragraph — every technical specific attributed to Wiz was either absent from the Wiz article or drifted from Wiz's actual wording.

This is a sub-agent attribution-discipline regression: S3 and S4 both returned items on the TeamPCP / durabletask campaign with technical detail (`417k monthly downloads`, `AWS-RunShellScript / per profile`, FIRESCALE C2-discovery mechanism, infostealer target list including SSH / Docker / VPN, ~3,800 Grafana repo count) that the main agent surfaced as if attributed to Wiz when in fact those specifics came from other sources (StepSecurity, Endor Labs, Safedep, BleepingComputer about a *separate* breach) or are not present in any cited source.

## Findings

**F1 (claim-not-supported, truth):** Verizon DBIR "AI is compressing exploitation windows from months to hours" presented inside quote marks — Verizon's GlobeNewswire actually says "shrinking the window for defense from months to mere hours". → remediated with verbatim quote.

**F2 (claim-not-supported, truth):** SonicWall "intrusion responders observed pivots to domain controllers within hours" — BleepingComputer says 30-60-minute brute-force / recon / credential-reuse sessions; no DC pivot claim. → remediated with source-accurate description.

**F3 (hallucinated-fact, truth):** Grafana paragraph attributes ~3,800 repos to Grafana — that figure belongs to the GitHub VS Code breach per BleepingComputer; Grafana's own blog gives no count. → remediated by removing the count from the Grafana sub-paragraph.

**F4 (hallucinated-fact, truth):** FIRESCALE C2-discovery mechanism attributed to Wiz — not in the Wiz article. → remediated by removing the entire FIRESCALE sentence.

**F5 (hallucinated-fact, truth):** ~417k monthly downloads attributed to Wiz — not in Wiz. → remediated by dropping the parenthetical.

**F6 (hallucinated-fact, truth):** "AWS Systems Manager `SendCommand` (`AWS-RunShellScript`) up to five instances per profile" — Wiz says "5 targets/host"; document-name specifier absent. → remediated by aligning wording.

**F7 (hallucinated-fact, truth):** Infostealer target list — wrong items, missing Azure/GCP/Kubernetes/Vault, added SSH/Docker/VPN absent from Wiz. → remediated by aligning verbatim.

**F8 (surface-contradiction, editorial):** Grafana TanStack detection date — Grafana's blog says May 11; BleepingComputer says May 1. Brief silently picked May 1 against the primary. → remediated by adopting Grafana's date and surfacing the contradiction in § 7.

**F9 (quantifier-without-source, truth):** DBIR 22,052 / 12,195 figures still not in any cited accessible source after iter-2 hedge. → remediated by replacing with qualitative scale and explicit "not separately confirmed in the cited press-release coverage" attribution.

**F10 (editorial-advisory):** VS Code extension identity not disclosed — added explicit "not publicly named at this writing" to scope the defender hunt correctly.

## Verdict

`NEEDS_FIXES (truth: 8, editorial: 1, advisory: 1)`

Operational implication for the routine: the sub-agent attribution discipline regression in the TeamPCP UPDATE is the kind of defect class that v2.53's `Evidence:` field would have caught at sub-agent return time. The S3 / S4 returns DID include evidence blocks, but the main agent's composition step ingested technical specifics from across all sub-agent returns without checking that each cited URL's evidence supported each specific the brief subsequently asserted. A follow-up to consider: when composing § 4 UPDATEs that synthesise across multiple sub-agent returns, every numeric / named-tool / per-source-flow claim should be matched against the specific Evidence quotes that source returned, not against the aggregated narrative.
