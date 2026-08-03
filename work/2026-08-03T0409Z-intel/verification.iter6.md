**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-03T06:10:05Z · ended_at=2026-08-03T06:16:34Z · duration_seconds=389

## Verification report — 2026-08-03T0409Z-intel (iteration 6)

Cold read of all three entries + run record. Live-fetched: N-able blog (bridge jina fallback), N-able status page (WebFetch), Huntress blog (WebFetch + jina raw text grep), NVD REST API for CVE-2026-18577/18556, Bouncy Castle release notes (raw githubusercontent), four Bouncy Castle per-CVE wiki pages (12852, 59638, 8763, and attempted 59643/59644/59652), CISA KEV catalog (bridge api), NVD REST API for all six CentreStack CVEs, VulnCheck's CVE-2026-54363 advisory. 25 URLs checked. Re-verified: N-able critical-rating elements, both single-source gradings' sourcing notes, the KEV "three vs four" CentreStack correction from iteration 2, all 32 Bouncy Castle CVE one-line bindings against the release notes, four spot-checked evidence quotes per entry, the out-of-window Gladinet publication's honesty controls, and classification blocks against the Admiralty vocabulary.

### Unsupported / hallucinated facts

- **F4** — `2026-08-03/cve-2026-18577-n-able-n-central-auth-bypass-exploited`: the evidence-block quote `"Exploitation is active in the wild; a compromised N-central server can be used to run scripts, push tools, and open remote sessions across every downstream endpoint it manages."` (attributed to Huntress, `evidence[]` line 80) and the identically-worded body quote at paragraph 2 (`Huntress states that "a compromised N-central server can be used to run scripts, push tools, and open remote sessions across every downstream endpoint it manages"`) are **not a verbatim substring of the cited Huntress page** (`https://www.huntress.com/blog/n-able-vulnerability-exploitation`). I fetched the page directly (jina raw text) and confirmed the actual sentences are three separate items:
  - "Push new scripts and jobs to many or all managed endpoints." (bullet, line 44 of the fetched text)
  - "Initiate remote‑control sessions into servers and workstations, including domain controllers and other critical systems." (bullet, line 48)
  - "a compromised RMM can be used as a force multiplier against every downstream client you manage" (line 176, in a different paragraph about the shutdown-decision tradeoff)
  - The opening clause "Exploitation is active in the wild" does not appear verbatim anywhere; the closest source text is "confirming active exploitation in the wild" (line 24) and "N-able has confirmed **active exploitation** of N-central" (line 36).

  This is exactly the splice pattern check 4b names explicitly ("a splice of two source sentences… is F4 — the quote must be copyable from the page unchanged"), except here it is a splice of three separate Huntress statements from two different sections of the article, stitched into one sentence and presented with quotation marks as if it were a single direct quote — in both the machine-consumed `evidence[]` frontmatter and the body prose. The underlying facts are all individually true and sourced elsewhere on the same page, but the sentence as quoted is not what Huntress wrote, and a reader (or an automated system ingesting `evidence[]` as ground truth) would be right to expect it to be copyable verbatim from the source.

  Remediation suggestion (not applied — read-only): either (a) drop the quotation marks and cite the paraphrase as reported prose, attributing it to Huntress without implying verbatim wording, or (b) replace with an actual short verbatim quote such as "Push new scripts and jobs to many or all managed endpoints" plus a second cited clause for the remote-session capability, keeping the "downstream" framing as un-quoted synthesis.

Everything else checked against a live fetch held:
- All three N-able evidence quotes at lines 74, 76, 78 are exact verbatim substrings of the N-able blog (confirmed by direct fetch).
- The evidence quote at line 82-83 ("N-able's initial security advisory linked this critical vulnerability to CVE-2026-18556; while the subsequent hotfix pointed to CVE-2026-18577.") is an exact verbatim substring of the Huntress page (line 26 of the fetched text, ignoring markdown link syntax around the CVE ids).
- CVE-2026-18577: CVSS 8.2, `exploitMaturity: ATTACKED` (E:A) confirmed against the live NVD record — matches the entry's `cves[]` note about "Exploitation Maturity E:A (Attacked)".
- CVE-2026-18556: CVSS 8.2, CWE-288, affected through 2026.1 confirmed against NVD.
- The status page confirms verbatim: the Cloudflared service name, the `svchost.exe` under a user's Documents-folder artifact, "all N-central instances not running 2026.3.1" affected-range wording, and the future-tense hosted-instance upgrade-notification language the entry now uses (fixed in iteration 1).
- All 32 Bouncy Castle CVE one-line bindings match the live release notes exactly, including the four flaws' "does not affect BC-LTS" framing (spot-checked CVE-2026-12852 directly: "Issue affecting: BC before 1.85 (from 1.73)" / "Fixed versions: BC 1.85" with no BC-LTS build listed, consistent with the entry).
- Bouncy Castle evidence quotes for CVE-2026-58062, CVE-2026-59638 and CVE-2026-8763 are all exact verbatim substrings of their respective per-CVE wiki pages.
- Gladinet CVE-2026-54363's two evidence quotes and CVSS 9.3 are exact verbatim matches against both the VulnCheck advisory and the live NVD record; spot-checked the other five CentreStack CVEs' CVSS scores (54367: 8.8, 54365: 8.7, 54366: 8.7, 54368: 8.7, 54364: 6.9) against NVD — all match the entry's `cves[]` block exactly.
- The "three earlier CentreStack CVEs in the exploited-vulnerabilities catalog" claim (corrected from four in iteration 2) is confirmed against the live CISA KEV catalog: four Gladinet entries total, but CVE-2025-12480 is scoped to "Gladinet Triofox" only — not CentreStack — so three is the correct count for CentreStack specifically.
- The run record's "no KEV additions since 2026-07-29" claim is confirmed against the live catalog (latest addition: CVE-2026-20316, dated 2026-07-29).

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)`

One genuine, source-checked defect survived five prior iterations: a Huntress attribution in both `evidence[]` and body prose is a paraphrase/splice of three separate sentences from two different sections of the cited article, presented as if it were a single direct quotation. Every other claim, quote, CVE id, CVSS score, count, single-source grading, the critical-priority calibration, and the out-of-window Gladinet publication's honesty controls held up against live re-fetches. This is not a padded finding — the exact source text is quoted above showing the gap, and the fix is narrow (one sentence in two places).

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-03
  item: "CVE-2026-18556 / CVE-2026-18577 — N-able N-central: unauthenticated admin access to the RMM console, exploited in the wild, and the day-one fix was itself bypassable"
  url_or_quote: "Exploitation is active in the wild; a compromised N-central server can be used to run scripts, push tools, and open remote sessions across every downstream endpoint it manages."
  summary: "Not a verbatim substring of the cited Huntress page (evidence[] line 80 and body paragraph 2, both attributed to Huntress with quotation marks). The actual source has three separate sentences in two different sections: 'Push new scripts and jobs to many or all managed endpoints.', 'Initiate remote-control sessions into servers and workstations, including domain controllers and other critical systems.', and 'a compromised RMM can be used as a force multiplier against every downstream client you manage' (this last one from an unrelated paragraph about the shutdown-decision tradeoff). The opening clause 'Exploitation is active in the wild' also does not appear verbatim; the source says 'confirming active exploitation in the wild' / 'N-able has confirmed active exploitation'."
```
