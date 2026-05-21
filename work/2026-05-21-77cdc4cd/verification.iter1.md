# Verification report — briefs/2026-05-21.md (iteration 1)

**Model:** Anthropic Claude Opus 4.7 (1M context) (`claude-opus-4-7[1m]`)
**Timestamps:** started_at=2026-05-21T04:36:42Z · ended_at=2026-05-21T04:48:41Z · duration_seconds=719
**Verdict:** NEEDS_FIXES
**Counts:** truth=4 editorial=2 advisory=1
**Self-telemetry:** webfetch_calls=14 websearch_calls=3 bridge_fetches=1 urls_checked=15

> Note on persistence: this report was inlined in the iter-1 verifier's return message because a generic system-reminder in the verifier's harness blocked writing report/findings .md files. The main agent persisted both this human-readable Markdown file and the machine-readable `verification.iter1.findings.yaml` to disk in Phase 5.7 by parsing the verifier's message, so the v2.59 § 6 forensic-audit guarantee is preserved.

## Unsupported / hallucinated facts

**F1 — CrowdStrike 2026 Financial Services Threat Landscape Report publication date.**
- Brief claim: "CrowdStrike published its 2026 Financial Services Threat Landscape Report on 2026-05-20"
- Both cited CrowdStrike URLs carry publication date **2026-05-14** (verified via WebFetch). The report is **6 days outside the brief's stated 36 h recency window** and should be treated consistently with the § 7 out-of-window deferrals for SAP / Fortinet (both also 2026-05-12).
- Remediation: dropped from § 3; added § 7 line.

**F2 — GraphWorm "Go implant" unsupported.**
- ESET WeLiveSecurity primary explicitly identifies **EchoCreep** as Go-written ("EchoCreep is a new backdoor, written in Go") but never specifies GraphWorm's language. The Hacker News additional source likewise does not.
- Remediation: removed "Go" qualifier from GraphWorm.

**F3 — ChromaDB "73 % of internet-accessible deployments" misattribution.**
- Hadrian's primary article contains no percentage and no scan methodology. The 73 % figure originates from BleepingComputer (Shodan queries) and frames the population as "running a vulnerable version of Chroma", not "use the Python server".
- Remediation: re-attributed to BleepingComputer in-line and reframed to "running a vulnerable version".

**F4 — Drupal "typically emerge within hours" inflation of source language.**
- Drupal PSA verbatim: "exploits *might* be developed within hours or days" — conditional, vulnerability-specific.
- TL;DR + § 6 Action Item drifted to "typically emerge within hours" — a stronger empirical paraphrase.
- Remediation: reverted TL;DR + § 6 to the conditional wording; § 4 UPDATE blockquote already had it right.

## Editorial — drop / softening

**F6 — CrowdStrike item: drop (same root as F1).**
**F7 — Drupal Steward marketing claim needs inline source or softening.** Remediation: softened and added inline link to https://www.drupal.org/drupal-steward.

## Advisory

**F10 — § 4 TeamPCP UPDATE density.** Remediation: added bold sub-leads (`**GitHub:**` / `**durabletask:**` / `**Grafana:**`) at top of each blockquote paragraph for skim-readability.

## Not counted as defects (advisory observations)

- F8 (Wiz vs Hunt.io C2 ordering): both sources can be reconciled; not flagged in brief. Surfaced in § 7 in iter-2.
- F9 (missed angle: Proximus NXT Luxembourg ALDO deployment): suggested as a next-run search angle, not a current-brief gap.
