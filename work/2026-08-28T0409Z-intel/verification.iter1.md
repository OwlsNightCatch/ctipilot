**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-28T05:40:55Z · ended_at=2026-08-28T05:50:11Z · duration_seconds=556

## Verification report — 2026-08-28T0409Z-intel (iteration 1)

Read: run record; all 36 new entries end to end; all 7 updated entries end to end plus `git diff HEAD` for each; `entities/registry.yaml` lines 5505–5663 (the 18 new records this run added); `state/cves_seen.json` context not separately needed given the run record's own dedup narrative. Fetched ~20 primary/secondary sources directly (`fetch_source.py extract`/`url`/`jina`), including NVD CVE 2.0 API records, the CISA KEV JSON feed, DOJ, AFP, Splunk's advisory, Adobe's APSB26-90, Johnson Controls' CISA CSAF JSON, OffSeq, AndDone, Arctic Wolf, Proofpoint, Troy Hunt's blog, The Register, Manchester Airport's own statement, NCSC UK, SwissCybersecurity.net, cyberattaque.org, CBC News and Infosecurity Magazine. Two sources were unreachable on every transport this iteration (git.kernel.org — Anubis anti-bot challenge; jina pool exhausted across all 7 keys) and one (franceinfo.fr) 403'd with jina also exhausted; where a lower rung reached an equivalent fact (e.g., NVD's mirrored commit-message text for the kernel.org citation) I used it to confirm the claim rather than leaving it unchecked.

### Unsupported / hallucinated facts

**#1 — `2026-08-28/troy-hunt-carhartt-synthetic-breach-data-verification`: three `evidence[]` quotes attributed to "Troy Hunt" are verbatim text authored by "PwnedClaw," Hunt's AI chat assistant, quoted inside a reproduced chat transcript in his own post — not statements Hunt personally wrote.**
Fetched `https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/` directly. The quote `"97.6% of domains appear exactly once — that's not a long tail, that's a signature. Real breach data from a retail company would have thousands of addresses on corporate domains, hundreds on ISP domains, a natural power law. Instead you have 10.1M singleton domains. That's pure TPC-DS generation."` appears in the source immediately after the line `[24/08/2026 17:58] PwnedClaw:` — i.e., it is the AI assistant's chat output, reproduced by Hunt as evidence of the tool's analysis, not Hunt's own prose. Likewise `"Birth year stats are conclusive. The distribution runs 1924-1992 and is perfectly flat..."` sits inside the same `PwnedClaw:`-prefixed block, and `"The conclusion is pretty solid: this is a real Carhartt Databricks breach, but the TPC-DS benchmark data was co-located..."` is the closing line of the same PwnedClaw-authored passage (confirmed by re-fetching and grepping the full page: the line immediately precedes a table PwnedClaw produced and is not preceded by any `Troy Hunt:` marker). The entry's `evidence[]` records all three with `publisher: "Troy Hunt"`, and the body text frames the underlying diagnostic work throughout as "Troy Hunt's ... systematic verification" and "the diagnostic signals were all independently conclusive" — crediting a human researcher's direct analytical judgment for text an AI tool generated (Hunt did do real independent manual work elsewhere in the same post — eyeballing domain lists, the Microsoft-alias/`deactivate-`/`wctest.com`/`carharttdonotship.com` cleanup passes — but that is not what these three quotes evidence). Fix: re-attribute the three quotes to "PwnedClaw (Troy Hunt's AI assistant), quoted by Troy Hunt" and adjust the body's framing of which findings are Hunt's own versus tool-generated.

### Claims missing inline citation / claim contradicted by the source's own conclusion

**#2 — `2026-08-28/troy-hunt-carhartt-synthetic-breach-data-verification`: title, summary and body state "the true figure was roughly 13.3M" as the verified real-record count, but the source's own final, published conclusion is ~12.9M, not 13.3M.**
The fetched article shows Hunt's own multi-step cleanup after the domain-frequency/TPC-DS filtering the entry describes: the corpus first plummets to **13,306,258** (a ~47% drop the article itself calls "still too high"), then a further pass removes Microsoft-365-alias triplicates (→13,300,522), then `deactivate-`-prefixed duplicate rows (→13,014,714), then a `wctest.com` perf-test domain (→12,965,927), then `carharttdonotship.com` perf-test rows (→**12,933,413**). Hunt's own published conclusion, quoted verbatim in the post: *"New breach: Carhartt was the target of a ShinyHunters extortion campaign earlier this month. Data allegedly obtained from the company was later published, including **12.9M unique email addresses**. 83% were already in @haveibeenpwned."* The entry's "roughly 13.3M" is an intermediate step in Hunt's own process (before he removed a further ~373,000 duplicate/test rows), not his final, stated conclusion. This is the entry's core numeric finding and it is off by ~3% from what the cited source itself lands on. Fix: correct "roughly 13.3M" to "roughly 12.9M" throughout title/summary/body, and note the additional cleanup categories (Microsoft-alias triplication, `deactivate-` soft-deletes, `wctest.com`/`carharttdonotship.com` perf-test rows) the entry currently omits from its methodology description.

### Citation does not support the claim

**#3 — `2026-08-10/coding-agent-ci-harness-trust-boundary-shared-checkout` (this run's `correction` record, 2026-08-28T04:55:00Z): the record inverts NVD's own "Primary"/"Secondary" designation between the two CVSS scores it just corrected.**
The correction's `summary`, `cves[].cvss` field and body all state: *"The CNA's own CVSS 4.0 rating ... is 10.0 CRITICAL ... NVD's own secondary CVSS 3.1 rating on the same record is 7.8."* Fetching `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-12537` directly shows the opposite labeling in NVD's own data: the CVSS v3.1 metric (baseScore 7.8, `source: "nvd@nist.gov"`) is tagged `"type":"Primary"`, while the CVSS v4.0 metric (baseScore 10.0, `source` = the CNA's UUID, not NVD) is tagged `"type":"Secondary"`. So the record this run introduced — itself a correction of an earlier defect — calls the NVD-sourced 7.8 score "secondary" when NVD's own API marks it `Primary`, and implicitly treats the CNA's 10.0 as the primary/authoritative figure when NVD's schema marks that one `Secondary`. The practical triage guidance (use the more severe 10.0/zero-click reading) is not undermined by this, but the factual characterization of which score NVD itself designates as primary is backwards, sourced to the very page fetched to make the correction. Fix: swap "primary"/"secondary" between the two scores in the `cves[].cvss` string, the correction's `summary`, and the body paragraph.

### Editorial / less-is-more flags (advisory)

**#4 (low confidence) — `2026-08-28/splunk-svd-2026-0801-embedded-report-session-hijack`: headline/body state "fixes roughly 55 CVEs," but the fetched advisory table lists 60 distinct CVE ids** (CVE-2026-76251 through -76263, and CVE-2026-76309 through -76355 — counted directly from `https://advisory.splunk.com/advisories/SVD-2026-0801`). "Roughly" provides some cushion, but 60 rounds to "roughly 60," not 55; a ~9% undercount on the entry's own headline metric. Every CVE this entry actually itemises (76310/76311/76312/76350/76351) matches Splunk's page exactly, so this is a scope-count issue rather than a mis-cited CVE.

**#5 (low confidence) — `2026-08-28/ncsc-uk-ot-edge-device-disruptive-targeting-advisory`: `techniques: [T1190, T1078]` maps T1078 (Valid Accounts) to the advisory's mitigation guidance rather than to any described access technique.** Fetched `https://www.ncsc.gov.uk/news/disruptive-cyber-activity-highlights-risk-from-internet-exposed-systems-and-edge-devices` directly (JSON-LD confirms `datePublished: "27 August 2026"`, so the entry's dating is correct despite trafilatura's own metadata misreading it as 2025-09-29 — not a defect). The advisory states only that it observed "increased targeting ... resulted in some limited real-world disruption" and separately recommends, as generic hardening, eliminating default/shared credentials — it never states that credential abuse was the technique used in the disruption it describes. The entry's own body is self-aware of this ("both directly supported by the advisory text rather than inferred beyond it"), and the T1190 mapping (exposed PLC/HMI interfaces) is solidly supported, but T1078 rests on a mitigation recommendation, not an observed-behavior statement — a thinner basis than the entry's framing suggests.

**#6 (low confidence) — `2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli`: `classification: {reliability: B, credibility: 1}` under `verification: multi-source`, where the second source (NVD/MITRE CVE record) confirms only the CVE id, affected-version range and coordinating authority (CERT.LV), not any of the entry's substantive technical claims** (the four vulnerable code paths, the `Dazadi.sql_txt()` gap, the PoC results). Confirmed by fetching `offseq.com` directly — the technical substance rests on OffSeq alone. Credibility 1 ("confirmed by other independent sources," per this store's own convention of single-source entries carrying credibility 2) may be slightly generous for a corroboration that only indexes the finding's existence rather than independently verifying its content; 2 would be more defensible. Low confidence because the pipeline's own stated policy (check 6) treats NVD/MITRE as legitimate second-tier corroboration, and the entry does not claim more than the source shows.

### Verdict

No F1/F2/F5–F13/F15–F18 findings this pass: every URL sampled resolved to a specific article/advisory (not a homepage or landing page); every named CVE, CVSS score, KEV-addition date and vendor-fix version checked against NVD, the CISA KEV JSON feed, Splunk's own advisory, Adobe's APSB26-90, and Johnson Controls' CISA CSAF JSON matched exactly (including the Johnson Controls entry's own self-flagged CWE-918/deserialization inconsistency, which is CISA's own document contradicting itself, correctly reported as such rather than silently resolved); the 18 new `entities/registry.yaml` records are typed, sourced, free of duplicate keys, and match the run record's `entities_added[]` list one-for-one; no `watchlist_hit: true`, no `org_triage` block, and no entry carries a missing/out-of-vocabulary `classification` on any entry sampled; `actions[]` lists sampled were all concrete and mechanism-derived, none padded past 2 items; no IOCs, vanity metrics or workflow-internal language found in any entry or the run-record notes. Coverage looks complete against the run record's own telemetry and the dedup narrative it documents (backlog clearance, single-assessor caveats on the vCenter update and SUEZ entry, the two shared-entity new-vs-update decisions) — I did not identify a plausible in-window gap this run's sources would have surfaced.

The three truth findings above are genuine and evidenced, but narrow: two sit in a single entry (Troy Hunt/Carhartt) and are fixable by re-attributing three quotes and correcting one number; the third is a labeling inversion in a same-run correction record that does not change the entry's triage guidance. None is a hallucinated URL, a fabricated entity, or a claim with zero source support — all three are "the source says something different/more precise than the entry states" defects, exactly the class the pipeline's audits have flagged as the dominant residual risk.

**NEEDS_FIXES (truth: 3, editorial: 0, advisory: 3)**

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-08-28/troy-hunt-carhartt-synthetic-breach-data-verification"
  url_or_quote: "https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/"
  summary: "Three evidence[] quotes attributed to publisher \"Troy Hunt\" (the 97.6%-singleton-domains, birth-year, and \"conclusion is pretty solid\" quotes) are verbatim text from \"PwnedClaw,\" Hunt's AI chat assistant, inside a reproduced chat transcript — not statements Hunt personally wrote. Re-attribute and adjust body framing of which findings are Hunt's own vs. AI-generated."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "2026-08-28/troy-hunt-carhartt-synthetic-breach-data-verification"
  url_or_quote: "\"the true figure was roughly 13.3M\""
  summary: "Source shows 13.3M (13,306,258/13,300,522) was an intermediate step; Hunt's own further cleanup (Microsoft-alias triplicates, deactivate- duplicates, wctest.com/carharttdonotship.com perf-test rows) brings his final published figure to 12,933,413, and his own tweet states \"12.9M unique email addresses.\" Entry's headline number should be ~12.9M, not ~13.3M."
- code: F3
  category: claim-not-supported
  section: updated-entries
  item: "2026-08-10/coding-agent-ci-harness-trust-boundary-shared-checkout (correction, 2026-08-28T04:55:00Z)"
  url_or_quote: "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-12537"
  summary: "Correction record calls the CVSS 3.1 score (7.8, source nvd@nist.gov) \"NVD's own secondary\" rating and the CVSS 4.0 score (10.0, source = CNA) \"the CNA's own rating.\" NVD's own API labels the 3.1 metric type=\"Primary\" and the 4.0 metric type=\"Secondary\" — the opposite of what the correction states. Triage guidance unaffected; factual labeling is inverted."
- code: F14
  category: quantifier-without-source
  section: new-entries
  item: "2026-08-28/splunk-svd-2026-0801-embedded-report-session-hijack"
  url_or_quote: "\"fixes roughly 55 CVEs\""
  summary: "(low confidence) Fetched Splunk advisory (SVD-2026-0801) table lists 60 distinct CVE ids, not ~55 — a ~9% undercount on the entry's own headline scope claim."
- code: F16
  category: org-triage
  section: new-entries
  item: "2026-08-28/ncsc-uk-ot-edge-device-disruptive-targeting-advisory"
  url_or_quote: "techniques: [T1190, T1078]"
  summary: "(low confidence) T1078 (Valid Accounts) is mapped from the advisory's generic credential-hardening recommendation, not from any described access technique in the disruptive activity the advisory reports; thinner support than the entry's self-aware caveat suggests."
- code: F17
  category: classification
  section: new-entries
  item: "2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli"
  url_or_quote: "classification: {reliability: B, credibility: 1}"
  summary: "(low confidence) Credibility 1 rests on NVD/MITRE corroboration that confirms only the CVE id/range/coordinating authority, not the entry's substantive technical claims (all from OffSeq alone); credibility 2 may be more defensible."
```
