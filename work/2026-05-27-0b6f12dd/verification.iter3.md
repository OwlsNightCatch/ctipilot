**Model:** Claude Opus 4.7 (`claude-opus-4-7[1m]`)
**Timestamps:** started_at=2026-05-27T04:58:14Z · ended_at=2026-05-27T05:01:43Z · duration_seconds=209
**Self-telemetry:** webfetch_calls=11 · websearch_calls=0 · bridge_fetches=3 · urls_checked=13

## Verification report — briefs/2026-05-27.md (iteration 3)

Cold read, odd iteration (no prior-iteration deltas received). Every inline source URL was fetched in this iteration. EUVD (`EUVD-2026-32027`) is a JavaScript-rendered SPA that returns no body via WebFetch or the bridge; the CVE-2026-9312 claims attached to it were independently corroborated against the GitHub Security Advisory `GHSA-fwfp-h68w-2hcr` (fetched this run), which confirms CVE id, GHES product, unauthenticated SSRF via upload-endpoint path traversal, CVSS 4.0 = 9.2, all six fixed versions, "prior to 3.22", and GitHub Bug Bounty reporting. The GitHub docs release-notes anchor URL also returned no usable body (anchor-fragment render), but the same GHSA corroborates the version list — not flagged as broken since liveness passed the mechanical gate and the substance is corroborated.

Sources fully verified as supporting their claims: The Record + Euronews + LRT (Lithuania, § 1); BleepingComputer Charter + CyberInsider Charter + BleepingComputer 7-Eleven + CyberInsider 7-Eleven (§ 4 ShinyHunters); Tenable TRA-2026-44 (§ 2 Delta DIAView); CERT-FR CERTFR-2026-ACT-023 (§ 4 Mini Shai-Hulud — exact package list, atool/@antv 300+, source-code leak 13 May 2026 to Breached.st all confirmed); Check Point Research + The Hacker News (§ 4 Nimbus Manticore — MiniFast, CheckForUpdates export, C2 endpoints, 14-opcode set, Zoom task hijack, SEO poisoning, Operation Epic Fury, two SSL.com certs, three waves, svchost.exe validation all confirmed); Elastic Security Labs (§ 5 Tycoon 2FA — both variants, client IDs, two-tier architecture, takedown roster, 10-20 min handoff, anomalousToken→aiConfirmedSafe false negative all confirmed).

Dedup context (prior_coverage.json / state-summary.json) confirms all three § 4 UPDATE topics and the § 5 deep-dive topic were previously covered, so the UPDATE framings and "last covered" claims are genuine deltas, not recycled news. The § 7 drops (MuddyWater out-of-window, ransomnews census single-source vanity-metric, Oncology Institute 8-K 403/single-verifiable-source) and the CVE non-promotions (SharePoint CVE-2026-45659 post-auth/<9.0; mcp-gitlab-server niche) are well-reasoned and hold up. The [SINGLE-SOURCE] flag on CVE-2026-9642 (Delta DIAView, Tenable-only) is correctly applied with a § 7 single-source line.

### Citation does not support the claim

- **F3** — § 0 TL;DR and § 4 ShinyHunters UPDATE. Claim quoted: "7-Eleven confirmed 185,000 **franchise-applicant** records including SSNs and driver's licences" (TL;DR) and "roughly 185,000 **franchise applicants**" (§ 4). The two cited sources both describe the affected population as **job applicants / applicants**, not "franchise applicants": BleepingComputer (`/7-eleven-data-breach-exposes-personal-information-of-185-000-people/`) titles them "185,000 people" and CyberInsider (`/7-eleven-data-breach-exposes-personal-information-of-185000-applicants/`) says "over 185,000 **job applicants**" / "a third-party vendor managing 7-Eleven's **recruitment** systems." The load-bearing SSN + driver's-licence claim IS supported (CyberInsider explicitly lists "Social Security numbers, driver's license information, and government-issued identification details"). Only the "franchise" qualifier is unsupported — and is mildly contradicted by the "recruitment / job applicants" framing. Remediation: change "franchise applicant" to "job applicant" (or simply "applicant") in both the TL;DR bullet and the § 4 UPDATE to match the cited sources.

### Quantifier without source

- **F14** — § 5 Deep Dive, Background paragraph. Claim quoted: "Elastic's 2026-05-26 analysis is **the first detailed detection-engineering treatment** of the kit's current operator architecture and is the basis for the technique mapping below." The cited Elastic article does **not** claim to be "the first" detailed detection-engineering treatment; on direct check, the only use of "first" in the article is "First observed in August 2023 and attributed to Storm-1747" (referring to when Tycoon 2FA was discovered, not the article's novelty). The "first detailed detection-engineering treatment" superlative is brief-authored and unsupported by the cited source. Remediation: drop the "first ... treatment" superlative — e.g. "Elastic's 2026-05-26 analysis is a detailed detection-engineering treatment of the kit's current operator architecture and is the basis for the technique mapping below." (The two-tier architecture and "Microsoft-only" device-code framing in the same section are both confirmed by the source — no change needed there.)

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 0)

Both findings are narrow text fixes; everything else in the brief — every URL, every named CVE / actor / campaign / version / date, the UPDATE deltas, the § 7 dispositions, the [SINGLE-SOURCE] flag — verified clean against fetched sources. No broken/generic URLs, no hallucinated entities, no missing citations, no contradiction left unsurfaced beyond these two, no analytical-link-as-fact, no name-collision. The Charter 40M (BleepingComputer) vs 42M (CyberInsider) figure differs between the two cited sources, but the brief's 42M is traceable to a cited source and the § 7 contradiction note already frames Charter's dispute of the record count — not raised as a finding.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: tldr-and-updates
  item: "UPDATE: ShinyHunters Salesforce campaign — 7-Eleven 185,000 with SSNs"
  url_or_quote: "\"7-Eleven confirmed 185,000 franchise-applicant records\" / \"roughly 185,000 franchise applicants\""
  summary: "Both cited sources (BleepingComputer, CyberInsider) call them job applicants / recruitment-system applicants, not 'franchise applicants'. SSN+DL claim is supported by CyberInsider; only the 'franchise' qualifier is unsupported and mildly contradicted. Change to 'job applicant'/'applicant'."
- code: F14
  category: quantifier-without-source
  section: deep-dive
  item: "Tycoon 2FA deep dive — Background"
  url_or_quote: "\"Elastic's 2026-05-26 analysis is the first detailed detection-engineering treatment of the kit's current operator architecture\""
  summary: "Cited Elastic article makes no 'first treatment' claim; its only 'first' is 'First observed in August 2023'. Brief-authored superlative unsupported by source. Drop 'the first' — say 'a detailed detection-engineering treatment'."
```
