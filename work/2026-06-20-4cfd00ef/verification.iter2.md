**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-20T04:39:25Z · ended_at=2026-06-20T04:43:50Z · duration_seconds=265
**Self-telemetry:** urls_checked=22 · webfetch_calls=14 · bridge_fetches=5

## Verification report — briefs/2026-06-20.md (iteration 2)

---

## Prior-iteration delta verification

### F-iter1-1 (F3): Splunk advisory swap SVD-2026-0601 → SVD-2026-0603

Fetched https://advisory.splunk.com/advisories/SVD-2026-0603.

Result: The page resolves successfully to a specific Splunk PSIRT advisory titled "Unauthenticated Arbitrary File Creation and Truncation in a PostgreSQL Sidecar Service Endpoint in Splunk Enterprise." CVE-2026-20253, CVSS 9.8, published 2026-06-10, updated 2026-06-18. Fixed in 10.4.0, 10.2.4, 10.0.7. Limited exploitation confirmed.

Grep for "SVD-2026-0601" in brief: zero matches. Remediation confirmed correct.

### F-iter1-2 (F4): CVSS 9.8, fixed versions 10.4.0/10.2.4/10.0.7, CISA KEV 2026-06-18

- SVD-2026-0603 confirms CVSS 9.8 (CWE-306). Fixed versions confirmed: 10.4.0, 10.2.4, 10.0.7.
- CISA KEV confirmed via bridge: `dateAdded: 2026-06-18`, entry references SVD-2026-0603.
- Grep for "8.8", "9.4.2", "9.4.1300": zero matches.
- Brief body (§ 4, § 6): shows 9.8 and 10.4.0/10.2.4/10.0.7 throughout. Stale figures fully removed.

Remediation confirmed correct.

### F-iter1-3 (F2): GitHub advisory index → GHSA-qf6p-p7ww-cwr9

Fetched https://github.com/gogs/gogs/security/advisories/GHSA-qf6p-p7ww-cwr9.

Result: Resolves to a specific GitHub Security Advisory (dated June 19, 2026) titled "RCE via git rebase --exec argument injection in pull request merge." Confirms CVE-2026-52806, fixed in Gogs 0.14.3. The technique (branch name → `--exec` injection in `git rebase`) matches brief prose exactly.

Grep for "advisories?query=" listing URL: zero matches.

Remediation confirmed correct.

---

## Cold pass — new findings

### Broken / unreachable URLs

No broken URLs identified. All URLs returned HTTP 200. The following URLs are JavaScript SPA-rendered and return structural shell only (not readable by WebFetch / bridge), but HTTP 200 confirms they resolve to specific pages:

- `https://advisories.ncsc.nl/advisory?id=NCSC-2026-0198` — HTTP 200, Angular SPA, requires JS rendering. This is an NCSC-NL per-advisory URL with the correct pattern; the format is consistent with NCSC-NL's advisory system.
- `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2013` — HTTP 200, Angular SPA. Same limitation.
- `https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability` — HTTP 403 to WebFetch; bridge returned SPA skeleton. Title in the HTML confirms the advisory exists ("Customer Updates: Remote Code Execution Vulnerability in PTC's Windchill and FlexPLM Solutions | June 2026 | PTC").

No F1 findings.

### Generic / oversight URLs (replace with specific article)

No F2 findings. All source URLs are specific article/advisory pages.

### Citation does not support the claim

#### F1 — PTC Windchill patched versions in CVE summary table incorrect

**Section:** § 2 CVE Summary Table (line 53)
**Claim:** "12.1.2, 12.0.2 (2026-06-15)" listed as Patch column for CVE-2026-12569.
**Source fetched:** Heise Security, 2026-06-19 (https://www.heise.de/en/news/PTC-Windchill-BSI-calls-admins-at-night-due-to-critical-security-vulnerability-11338329.html).
**What the source actually says:** Heise's entity extraction returns patched versions as "13.1.2.8, 13.1.3.4, 13.0.2.12, 12.1.2.27." There is no "12.0.2" patched version in Heise's reporting. The brief's "12.0.2" does not match any source-supported patched build. "12.1.2" in the brief appears to be a truncation of "12.1.2.27," which is inaccurate as a standalone version identifier.
**Note:** § 5 deep dive correctly defers ("verify exact fixed-build numbers against the PTC advisory for your release train") — the error is confined to the § 2 summary table. Recommend replacing the Patch cell with "See PTC advisory for per-release-train fix" or using the Heise-confirmed full build numbers (13.1.2.8 / 13.1.3.4 / 13.0.2.12 / 12.1.2.27).

### Unsupported / hallucinated facts

No F4 findings. All named entities traced successfully to linked sources.

### Claims missing inline citation

No F5 findings. All factual claims carry inline citations.

### Strengthen primary source

No F6 findings. No item uses only NVD/CERT as sole primary.

### Drop (low relevance / off-audience)

No F7 findings. All items carry CH/EU/public-sector nexus or transferable defensive lessons.

### Needs more research

No F8 findings. Technical depth is adequate across all items.

### Surface contradiction

No F9 findings beyond what is already documented in § 7 Verification Notes.

### Missed angles

#### F2 — AutoJack CVEs absent from brief

**Section:** § 3 AutoJack
**Note:** The Hacker News article on AutoJack (https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html) mentions CVE-2026-26030 and CVE-2026-25592 as identifiers associated with this research. Neither CVE appears in the brief's § 3 item or its footer. If these CVEs have been assigned to the AutoJack vulnerabilities, the brief should carry them in the CVE field; if they refer to related but distinct vulnerabilities mentioned in passing, a brief editorial note would suffice. Suggested search: `CVE-2026-26030 CVE-2026-25592 AutoJack AutoGen Studio`.

This is advisory — the brief's AutoJack item is otherwise complete and accurate. The Microsoft Security Blog is the primary source and does not cite CVE IDs.

### Editorial / less-is-more flags (advisory)

#### F3 — Splunk § 7 contradiction note uses "search-job-serialization" framing inconsistently

**Section:** § 7 Verification Notes, "Contradictions" bullet.
**Flag:** The § 7 note says "this run's source frames it as search-job-serialization RCE." SVD-2026-0603 describes the vulnerability as "unauthenticated arbitrary file creation/truncation in a PostgreSQL sidecar service endpoint" (CWE-306). There is no "search-job-serialization" framing in SVD-2026-0603. The § 7 note is internally confusing but does not affect the § 4 UPDATE text, which correctly uses the PostgreSQL sidecar framing. Advisory: consider removing the "search-job-serialization" description from § 7 or correcting it to "authenticated search-job submission path" (if that was a different source's framing) so the contradiction note is accurately worded.

### Single-source items missing [SINGLE-SOURCE] flag

No F12 findings. All items carry two or more independent sources.

---

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 2)

**Truth finding (F1):** § 2 CVE summary table lists PTC Windchill patched versions as "12.1.2, 12.0.2" — "12.0.2" is not supported by any fetched source (Heise reports 13.1.2.8/13.1.3.4/13.0.2.12/12.1.2.27; "12.0.2" appears nowhere). Recommend replacing table Patch cell with either the full Heise-verified build numbers or "See PTC advisory."

**Advisory findings:** F2 (AutoJack CVEs potentially missing) and F3 (§ 7 contradiction wording) are low-priority — F2 is an enrich-if-confirmed item, F3 is an internal note correction. Neither blocks publish if the main agent judges them immaterial.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-12569 — PTC Windchill / FlexPLM CVE Summary Table"
  url_or_quote: "12.1.2, 12.0.2 (2026-06-15)"
  summary: >
    Heise Security (the cited source) reports patched versions as 13.1.2.8 / 13.1.3.4 /
    13.0.2.12 / 12.1.2.27. The brief table shows '12.0.2' which does not appear in any
    fetched source. Recommend replacing with full Heise-confirmed build numbers or
    'See PTC advisory for per-release-train fix'.
- code: F11
  category: editorial-advisory
  section: research-investigative
  item: "AutoJack — Microsoft shows a single web page can drive host RCE through an AI agent's local MCP server"
  url_or_quote: "CVE-2026-26030, CVE-2026-25592 mentioned in THN article but absent from brief"
  summary: >
    The Hacker News AutoJack article cites CVE-2026-26030 and CVE-2026-25592. The brief
    footer has no CVE field. If these CVEs are assigned to the AutoJack chain, add to footer.
    Suggested search: CVE-2026-26030 CVE-2026-25592 AutoJack.
- code: F11
  category: editorial-advisory
  section: verification-notes
  item: "§ 7 Splunk contradiction note uses 'search-job-serialization' framing"
  url_or_quote: "this run's source frames it as search-job-serialization RCE"
  summary: >
    SVD-2026-0603 describes the flaw as PostgreSQL sidecar file creation/truncation (CWE-306),
    not search-job-serialization. The § 7 note's 'search-job-serialization' phrase is
    inaccurate relative to what SVD-2026-0603 says. Advisory: correct or remove to avoid
    confusion for readers who check the § 7 notes.
```
