**Model:** Anthropic Claude (specific model not determined — env vars CLAUDE_FRIENDLY_NAME/CLAUDE_MODEL_ID unset; runtime self-report: Claude Opus 4.8, `claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-05-31T04:40:26Z · ended_at=2026-05-31T04:52:00Z · duration_seconds=694

## Verification report — briefs/2026-05-31.md (iteration 1)

Cold read of a deliberately short quiet-window brief: 3 § 1 items, empty § 2 (justified), 1 § 3 research item, no § 4, no deep dive. Every Source URL fetched this iteration. Dedup/drop logic cross-checked against prior_coverage.json (93 records), state/cves_seen.json, and briefs/2026-05-30.md.

### URL liveness / truth pass — summary of what was fetched and confirmed

- **Mautic § 1** — BSI WID-SEC-2026-1724 is a JavaScript SPA: both `WebFetch` and `tools/fetch_source.py url` returned only the static Angular shell (no rendered advisory body), so the verbatim German Evidence quote could **not** be rendered/confirmed this iteration (tooling limitation, not asserted as a defect). The substantive claims were corroborated independently: GHSA-fcmw-wx57-9p75 confirms CVE-2026-4776 = SQL injection in API contact filtering, post-auth, patched in 7.1.2/6.0.9; the Mautic advisories index confirms a distinct "SSRF in the Mautic Focus component" advisory (GHSA-jmv8-8j9j-rcpc) exists, corroborating the Focus-SSRF claim (CVE-2026-9557). Seven-flaw cluster, post-auth nature, SSRF+SQLi are all supported.
- **Signal § 1** — TechCrunch (May 28, primary) confirms the recovery-key-theft mechanic ("trick Signal users to give up their secret recovery key, which can be used to access online backups containing past messages") and anti-CCP-activist targeting. Malwarebytes (Pieter Arntz, May 29) carries the "will never reach out... never request registration codes, PINs, or recovery keys" line the brief attributes to it. Both quotes supported.
- **23andMe § 1** — OAG release confirms ~7M worldwide / 855,541 Californians, the DNA Relatives "critical coding error", ~14,000 credential-stuffed accounts, and the ransom-negotiation allegation framed as the AG's complaint. BleepingComputer confirms "roughly 6.9 million" + 855,541. The Register URL resolves to a specific article and carries the verbatim ransom quote. Ransom allegation correctly attributed to the complaint, not stated as fact.
- **Talos § 3** — confirmed: author Emmanuel Tacheau, May 28; **no CVE ids and no PoC/exploit code** in the public post (it points to a downloadable white paper); the "holy grail of attack surfaces" + auto-ingest-over-network quotes are verbatim substrings. [SINGLE-SOURCE] flag correctly applied and documented in § 7.
- **Dedup/drops** — CVE-2026-0257 confirmed fully covered in briefs/2026-05-30.md (Immediate Action callout, § 2 entry, full deep dive incl. Rapid7 two-wave / PoC / KEV). No prior-coverage record exists for Mautic / Signal / 23andMe / DICOM-Orthanc — survivors are genuinely new. The three CVE-2026-0257 "UPDATE" drops, the empty § 2, and the large § 7 drop list are all sound and not over-aggressive.

### Citation does not support the claim

- **F3** — § 1 23andMe, prose: *"California Attorney General Rob Bonta filed suit on **2026-05-29** in San Francisco Superior Court"* and inline citation label *"[California OAG, **2026-05-29**]"*. The cited OAG primary page is dated **"Thursday, May 28, 2026"** (verified this iteration). The 2026-05-29 dates appear to be borrowed from the BleepingComputer / Register reporting date, not the primary filing/announcement date. Low-severity, single-day discrepancy — all figures and substance are correct — but the prose date and the OAG citation label should read 2026-05-28 to match the cited primary (or the 05-29 should be attributed to the secondary reporting). Suggested fix: change the prose to "filed suit on 2026-05-28" and the OAG citation label to "California OAG, 2026-05-28".

### Editorial / less-is-more flags (advisory)

- **F11** (advisory) — § 1 Mautic footer lists `CVSS: n/a / n/a / n/a / n/a / n/a / n/a / n/a`. This is honest (BSI does not publish per-CVE CVSS in the rendered advisory and GHSA scores were not all retrievable), and the item is correctly placed in § 1 as a patch advisory rather than § 2, so no action required — noting only that a senior reader will want at least the BSI "hoch" qualitative rating (already in prose). Leave as-is.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)

Single low-severity truth defect: the 23andMe filing-date / citation-date is one day ahead of the cited OAG primary. The brief is otherwise tight, well-sourced, correctly deduped, and editorially strong for the audience — no padding, relevance is high across all four items, § 2 emptiness and the drop list are sound, style discipline clean (no IOCs, English, no workflow leakage). Fix F3 and this publishes.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "California AG sues former 23andMe (Chrome Holding Co.) over the 2023 genetic-data breach"
  url_or_quote: "filed suit on 2026-05-29 ... [California OAG, 2026-05-29](https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023)"
  summary: "Cited OAG primary page is dated 'Thursday, May 28, 2026'; brief prose and citation label both say 2026-05-29 (borrowed from secondary BleepingComputer/Register reporting date). Change prose + OAG citation label to 2026-05-28 to match the cited primary. Figures and substance all correct."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Mautic 7.1.2 / 6.0.9 — seven authenticated flaws"
  url_or_quote: "CVSS: n/a / n/a / n/a / n/a / n/a / n/a / n/a"
  summary: "Per-CVE CVSS all n/a (honest — BSI SPA not renderable, GHSA scores not all retrievable). BSI qualitative 'hoch' rating already in prose. Advisory only; leave as-is."
```
