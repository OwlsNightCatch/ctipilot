**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-21T05:10:22Z · ended_at=2026-07-21T05:17:13Z · duration_seconds=411

## Verification report — 2026-07-21T0409Z-intel (iteration 2)

**Prior-iteration deltas verified (all three hold):**
1. `cruciferra-crypter-as-a-service-process-ghosting-byovd` — both evidence[] quotes fetched-and-confirmed as contiguous verbatim substrings of the Proofpoint blog (https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service). Quote 1 ("the malware reads a clean copy of ntdll.dll on disk...") and quote 2 ("Proofpoint observed four campaigns attributed to Chinese-speaking cybercrime actor TA4922...") both found verbatim, correctly attributed to Proofpoint. Body no longer misattributes Infosecurity Magazine phrasing. Fix holds.
2. `cve-2026-2291-dnsmasq-heap-overflow-rce-exodus` — evidence quote "The root cause of the vulnerability is an unsafe strcpy() when a domain name is cached." confirmed verbatim contiguous on the Exodus page (https://blog.exodusintel.com/2026/07/20/dnsmasq-dns-remote-heap-buffer-overflow/). Fix holds.
3. `hugging-face-autonomous-ai-agent-production-breach` — both remediated evidence quotes (the two-code-execution-paths parenthetical restored; the "executing many thousands of individual actions..." fragment) confirmed verbatim contiguous on https://huggingface.co/blog/security-incident-july-2026. Fix holds.

### Unsupported / hallucinated facts

**F4.** Entry: `2026-07-21/hollowgraph-m365-calendar-graph-api-c2-cavern` (DEEP DIVE). `evidence[]` quote 2:

> "we cannot confidently attribute this activity to any previously identified threat actor... we assess a potential link to Lyceum with low confidence"

is attributed as a single quote to Group-IB Threat Intelligence, but it is NOT a contiguous verbatim substring of the Group-IB source (https://www.group-ib.com/blog/hollowgraph-microsoft-365/). Fetched via bridge (`tools/fetch_source.py url`) and confirmed the actual page text reads:

> "Based on the evidence currently available, we cannot confidently attribute this activity to any previously identified threat actor. However, our analysis identified several technical similarities with the Iranian-nexus threat actor Lyceum. While these overlaps are noteworthy, they are not sufficiently unique to support a high-confidence attribution. At this stage, we assess a potential link to Lyceum with low confidence."

The entry's "..." elides two full intervening sentences ("However, our analysis identified several technical similarities with the Iranian-nexus threat actor Lyceum. While these overlaps are noteworthy, they are not sufficiently unique to support a high-confidence attribution.") — a splice of two non-adjacent sentences into one quotation mark pair, exactly the defect class iteration 1 found and fixed in three other entries this run (cruciferra, dnsmasq, hugging-face), but this instance in HOLLOWGRAPH was not caught. The underlying fact (low-confidence Lyceum overlap, no high-confidence attribution) is accurately represented and not itself hallucinated — the defect is quote-fidelity, not fact-invention. Fix: either quote only the first sentence verbatim ("we cannot confidently attribute this activity to any previously identified threat actor.") and separately quote/paraphrase the Lyceum conclusion, or reproduce the full four-sentence span verbatim without eliding the middle two sentences. Quote 1 on the same entry (the "Group-IB Threat Intelligence team has identified HOLLOWGRAPH..." line) was checked and is a clean contiguous substring (only the leading "The" is dropped, a valid partial-quote start) — no issue there.

### Confirmed correct — entity/relation decision

`hollowgraph-m365-calendar-graph-api-c2-cavern` sharing `tool:cavern-c2-framework` with the 2026-07-09 Cavern Manticore entry as a NEW entry (not `update_of`) is the right call: the registry correctly types the link as `variant-of` (not `update_of`/`attributed-to`), Group-IB's own source explicitly frames HOLLOWGRAPH as a technically distinct component with its own novel C2 mechanism (Graph-API calendar dead-drop + DNS-tunneled credential refresh) and its own attribution ceiling (Lyceum overlap at low confidence, distinct from the Cavern Manticore/MOIS framing of the 2026-07-09 entry). This is a materially new finding on a shared framework, not a delta on the same story — `check_run.py`'s dedup WARN on this pairing is correctly addressed in the run record and the entity relation is properly typed and sourced.

### Verification checks performed and passed (no findings)

- All 8 entries' primary + corroborating source URLs fetched and confirmed: specific-article-level (no homepage/listing/NVD/MITRE-only sourcing), content supports the attached claims.
- CVE/CVSS/date/version cross-checks: CVE-2026-6875 (CVSS 9.5, "Actively exploited") confirmed verbatim against NCSC-CH advisory post 12778 and BleepingComputer's Defused attribution ("Attackers have begun exploiting a critical vulnerability (CVE-2026-6875)... according to threat intelligence company Defused," first attempts Friday 2026-07-18). CVE-2026-2291 root-cause mechanism and dnsmasq 2.92rel2/2.93 (2026-05-11) patch confirmed against Exodus. CVE-2026-63030/CVE-2026-60137 (WP2Shell) and its 7.0.2/6.9.5/6.8.6 patch confirmed consistent with the 2026-07-18 `update_of` target in prior_coverage.json.
- JADEPUFFER/ENCFORGE: "doubled down on that bet... a trained AI model", `lockd` binary name, ~180 file extensions, and "same operator with a materially upgraded toolkit" / extortion-contact-match claim all confirmed verbatim/faithful against the Sysdig blog (fetched via bridge after a WebFetch 503).
- ANCPI contradiction: Digi24's "databases have not been affected" / 22 July Gov Cloud migration date, Risky Business News's "wiped systems and backups after failing to extort the agency" quote, and KELA's Zakaria Mahdjoub/Oran Algeria attribution quote all confirmed verbatim on their respective pages. `verification: contradicted` / `credibility: 3` is correctly calibrated to the unresolved contradiction.
- GPT5.6/WP2Shell: both evidence quotes ("Total usage: 50%..." and "No security researcher could have found...") confirmed verbatim on the Searchlight Cyber page; the body's shortened in-prose quote ("50% of weekly usage ... ~ $25 USD") uses an explicit, honestly-marked ellipsis over material already given in full in `evidence[]` — not a defect (the strict contiguous-substring rule targets the `evidence[]` frontmatter field, which here is unelided and clean).
- Priority calibration: one `high` (ServiceNow, exploitation-status flip — clears the TL;DR bar), seven `notable`, no `critical` — consistent with the run record and defensible against the critical/high bars.
- Admiralty classification: all 8 entries carry a `classification` block within vocabulary; reliability letters (A for first-party/national-CERT sources — Hugging Face, NCSC-CH; B for vendor research labs — Proofpoint, Exodus, Sysdig, Group-IB, Searchlight Cyber, Digi24/KELA) and credibility 2/3 values track the run's consistent single-source-vs-press-corroboration convention; no contradiction found.
- Single-source flagging: dnsmasq (Exodus-only) correctly carries `verification: single-source` with a `sourcing_note` naming the discrepancy with NVD framing — correct per F12 criteria. No other entry is single-source without disclosure.
- Action-item discipline: 4 actions across 8 entries (dnsmasq, ServiceNow, JADEPUFFER, Hugging Face), each concrete/self-contained/derived from the entry's own mechanics, no padding, no generic advice, no hedging — no F18.
- No IOCs (hashes/IPs/bracketed domains) found in any entry body.
- `org_triage: null` and `watchlist_hit: false` consistent store-wide with the "no scheme configured" / "no watchlists configured" org profile — no F16.
- Coverage completeness: cross-checked the run record's 5 borderline-drop rationales and coverage-gap notes against a fresh web search for 2026-07-20/21 CH/EU critical-infrastructure incidents and major advisories; found nothing contradicting the run record's stated gaps (cert-eu staleness, un-drilled standard-tier research slices, the recency-dropped Expel item) and no additional plausible in-window miss to name — completeness sweep looks sound.
- `tools/check_run.py 2026-07-21T0409Z-intel` re-run: 36 pass · 1 warn (the cavern-c2-framework dedup WARN, addressed above) · 0 fail.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: operational
  item: "HOLLOWGRAPH: a Cavern-framework backdoor that turns a compromised Microsoft 365 calendar into a Graph-API dead-drop C2"
  url_or_quote: "we cannot confidently attribute this activity to any previously identified threat actor... we assess a potential link to Lyceum with low confidence"
  summary: "evidence[] quote 2 elides two full intervening sentences from the Group-IB source (https://www.group-ib.com/blog/hollowgraph-microsoft-365/) via an ellipsis splice across non-adjacent sentences — not a contiguous verbatim substring. Actual source text: 'Based on the evidence currently available, we cannot confidently attribute this activity to any previously identified threat actor. However, our analysis identified several technical similarities with the Iranian-nexus threat actor Lyceum. While these overlaps are noteworthy, they are not sufficiently unique to support a high-confidence attribution. At this stage, we assess a potential link to Lyceum with low confidence.' Same defect class iteration 1 fixed in 3 other entries this run; the underlying fact is accurate, only the quote fidelity is broken."
```
