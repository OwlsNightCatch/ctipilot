**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-11T20:40:50Z · ended_at=2026-07-11T20:46:19Z · duration_seconds=329

## Verification report — 2026-07-11T2009Z-intel (iteration 2)

Scope: 1 new entry (`entries/2026-07-11/praisonai-agentic-framework-three-cves-code-exec-rce-ddli.md`) + run record `runs/2026-07-11/2026-07-11T2009Z-intel.md`. Even-iteration (Sonnet, alt) rotation with prior-iteration deltas supplied — both iteration-1 fixes verified first, then a fresh check for defects the fixes may have introduced or left incomplete.

### Prior-iteration delta verification

1. **F4 (claim-overstatement) fix — VERIFIED CORRECT.** The summary now reads "both reachable by influencing the model's output through prompt injection. CVE-2026-60090 (9.3) is a separate SQL/CQL injection: a caller-controlled vector-store dimension parameter is interpolated into knowledge-store DDL, with no LLM nexus" and the body explicitly frames CVE-2026-60090 as "a different bug class with no LLM nexus — a classic SQL/CQL injection reachable by any caller who can influence collection-creation parameters (for example through a RAG ingestion API), not through the model." I fetched `GHSA-wf65-4jjx-q444` directly (`WebFetch`, full page): "This advisory describes the vulnerability as reachable by conventional injection, not LLM prompt injection. The exact language states: 'A caller that can influence collection creation dimensions can append SQL/CQL tokens to the generated DDL'... The vulnerability requires an attacker to control the `dimension` parameter passed directly to the `create_collection()` API." The fix is fully supported by the source and the transferable-lesson sentence is correctly narrowed to the first two CVEs. No new defect introduced by this edit.

2. **F11 (source-date-drift) fix — PARTIALLY INCOMPLETE.** The remediation corrected the `GHSA-9mp3-24cc-77mg` source date to `2026-06-25` (verified: I fetched the page directly and it shows "published GHSA-9mp3... Jun 25, 2026" per metadata). However, the same class of defect remains uncorrected on the other two source records. I fetched both remaining advisories directly and both show the identical publication date:
   - `GHSA-2xv2-w8cq-5gxw` (cited for CVE-2026-61447): entry's `sources[]` records `date: "2026-07-11"`. Direct fetch: "The advisory page shows: 'published GHSA-2xv2-w8cq-5gxw Jun 25, 2026'."
   - `GHSA-wf65-4jjx-q444` (cited for CVE-2026-60090): entry's `sources[]` records `date: "2026-07-11"`. Direct fetch: "**Published:** Jun 25, 2026."

   All three GHSA advisories were published the same day (2026-06-25); only one of the three source-date fields was corrected. This is a residual instance of the exact defect class iteration 1 flagged — see F11 below (advisory, not blocking).

### Surface contradiction

- **F9** — entry: `praisonai-agentic-framework-three-cves-code-exec-rce-ddli`. The entry ships CVSS **9.3** (Critical range) for CVE-2026-60090, sourced per `sourcing_note` to "NVD carry the same VulnCheck-assigned ids with CVSS 4.0 vectors... consistent with the 10.0 / 9.4 / 9.3 base scores" — confirmed accurate: NVD/VulnCheck CNA lists CVSS 4.0 = 9.3 CRITICAL (`CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`) and CVSS 3.1 = 9.8 CRITICAL for this CVE (both fetched directly from nvd.nist.gov). But the entry's own cited **primary source** for this CVE, `GHSA-wf65-4jjx-q444` (`role: primary` in `sources[]`), rates the same vulnerability **"Severity: Moderate"** with no numeric CVSS shown on the advisory page itself (confirmed via two separate direct fetches of the GHSA page). This is a genuine, verifiable contradiction between the cited primary source's own severity self-assessment and the CVSS score the entry actually publishes for the same CVE — the entry silently adopts the higher NVD/CNA number without surfacing that its own primary source disagrees. (The other two CVEs do not show this gap: GHSA-2xv2 self-rates "Critical (CVSS 10.0)" matching the entry's 10.0, and GHSA-9mp3 self-rates "Critical, CVSS 9.9" — both consonant with a Critical framing, so no contradiction there.) Recommend a `Contradiction:` line in the entry or run-record verification notes noting the GHSA "Moderate" self-rating vs. the CNA-assigned CVSS 9.3/9.8 Critical score for CVE-2026-60090.

### Single-source items missing [SINGLE-SOURCE] flag

None — entry carries three GHSA primaries plus a corroborating TheHackerWire source; `verification: multi-source` is correct.

### Editorial / less-is-more flags (advisory)

- **F11** — entry: `praisonai-agentic-framework-three-cves-code-exec-rce-ddli`. Residual source-date drift on two of three `sources[]` records (see delta-verification #2 above): `GHSA-2xv2-w8cq-5gxw` and `GHSA-wf65-4jjx-q444` both record `date: "2026-07-11"` in frontmatter and inline citation, but both advisories were actually published `2026-06-25` per direct fetch of each page's own metadata ("published ... Jun 25, 2026" / "Published: Jun 25, 2026"). Only `GHSA-9mp3` was corrected to the accurate date in the iteration-1 remediation. Recommend correcting the remaining two source dates (frontmatter `sources[]` and the two inline citations in the body, currently rendered `[PraisonAI GHSA-2xv2-w8cq-5gxw, 2026-07-11]` and `[PraisonAI GHSA-wf65-4jjx-q444, 2026-07-11]`) to `2026-06-25`, and consider broadening the `sourcing_note` clause (currently singles out only GHSA-9mp3 as "had been public on GitHub since 2026-06-25") to note that all three underlying advisories share that publication date, with the CVE-id/NVD-EUVD publication on 2026-07-11 as the sole in-window anchor. Advisory, non-blocking.

### Other checks performed, no new defect found

- Re-verified all three CVSS scores against NVD/VulnCheck directly (CVE-2026-61447: CVSS 4.0 = 10.0; CVE-2026-61445: CVSS 4.0 = 9.4; CVE-2026-60090: CVSS 4.0 = 9.3) — all three match frontmatter exactly, confirming the entry consistently used the CVSS 4.0 CNA score (not a mismatched version), correcting a plausible failure mode this run.
- TheHackerWire URL re-checked: resolves (200 via bridge), lands on the specific dated article (not a landing page), `datePublished: 2026-07-11T15:59:55+00:00` confirmed via the page's own JSON-LD — no F1.
- Dedup: `CVE-2026-61447` / `-61445` / `-60090` and the PraisonAI title are not present anywhere in `work/2026-07-11T2009Z-intel/prior_coverage.json` (172 records checked) and appear in `state/cves_seen.json` only as this run's own additions — no duplicate-coverage issue.
- Evidence quote spot-check: the DDL-injection evidence quote ("A caller that can influence collection creation dimensions can append SQL/CQL tokens to the generated DDL executed by the database driver.") is a verbatim match against the directly-fetched GHSA-wf65 page text.
- `actions[]` (single item, concrete upgrade instruction naming both package/version pairs) — not generic, not a restatement, not padded. No F18.
- Priority (`notable`) and relevance framing (narrow self-hosted exposure, transferable technique-class lesson) remain internally consistent and are not contradicted by anything fetched this iteration.

### Verdict

NEEDS_FIXES (truth: 0, editorial: 1, advisory: 1)

### Findings summary (machine-readable)

```yaml
- code: F9
  category: surface-contradiction
  section: trending-vulnerabilities
  item: "PraisonAI agent framework: three CVEs — unsandboxed LLM code execution, tool-call RCE, and vector-store DDL injection"
  url_or_quote: "GHSA-wf65-4jjx-q444: 'Severity: Moderate' (no CVSS shown) vs NVD/VulnCheck CVSS 4.0 = 9.3 CRITICAL / CVSS 3.1 = 9.8 CRITICAL for CVE-2026-60090"
  summary: "Entry's own cited primary source rates the CVE 'Moderate' while the entry ships CVSS 9.3 sourced to NVD/VulnCheck, without surfacing the disagreement"
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "PraisonAI agent framework: three CVEs — unsandboxed LLM code execution, tool-call RCE, and vector-store DDL injection"
  url_or_quote: "sources[]: GHSA-2xv2-w8cq-5gxw date '2026-07-11'; GHSA-wf65-4jjx-q444 date '2026-07-11'"
  summary: "Both advisories were actually published 2026-06-25 per direct fetch of each page ('published ... Jun 25, 2026'); iteration-1 fix corrected only the GHSA-9mp3 date, leaving these two uncorrected instances of the same defect class"
```
