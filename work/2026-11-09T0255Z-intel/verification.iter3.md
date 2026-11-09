**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-09T03:56:34Z · ended_at=2026-11-09T04:04:18Z · duration_seconds=464

## Verification report — 2026-11-09T0255Z-intel (iteration 3)

Scope: all 45 claims of claims.iter3.yaml walked (post-fix pass over a two-entry run, nothing sampled). Rows in verification.iter3.claims.yaml: 45 rows, 42 ok, 3 non-ok (all low confidence). Pages read live this iteration: GTIG/Mandiant LLMjacking post (extract), Wiz incident page (extract), Datadog Security Labs article (extract), SANS ISC diary 33498 (extract), Previdian CVE page (extract, counter shows 20/13/9, last observed 08 Nov, updated 09 Nov), OpenSSH 10.6p2 release notes, NCSC Security Hub post 13155 (ncsc-csh), Alpine advisory, heise, The Hacker News, OX Security (page 403 on every transport; read through the WordPress feed `url --direct https://www.ox.security/feed/`, pubDate 2026-11-05), CISA KEV catalogue (version 2026.11.06, no CVE-2026-123158), Help Net Security, CSO, BleepingComputer, Cloudflare Radar (no production-compromise report found). Registry, ATT&CK pin (all 16 ids active, T1548.005 active), prior_coverage and the Obsidian entry (CVE-2026-40217 Contradiction line holds) checked.

### Prior-iteration deltas (iteration 2 findings, all six confirmed fixed)

1. Record summary no longer claims a peak or decline: 713 on 2026-11-06 is the highest value in ISC's table; 11-08 marked as the publication day. Supported.
2. "quite a few of those login attempts" now scoped to the first scanners ISC lists (its 11-05 table sums to 232). Supported.
3. Wiz citation ends after "linked to the billing account"; watch advice is the entry's own clause. Wiz page supports starts-with search-ad phishing, external billing administrators, foreign projects.
4. "accounts with model services not enabled are in scope too, because the actors enabled them" supported by GTIG ("LLM services were not enabled at the time of compromise ... allowed the threat actor to modify and enable LLM API services").
5. Second paragraph: each sentence now carries a GTIG citation; each cited clause is supported.
6. T1555.006 and T1213.003 added; GTIG supports secret-manager exfiltration and repository enumeration/cloning for hardcoded secrets.
No remediation introduced a new unsupported statement apart from the clause-level items below.

### Citation does not support the claim

- #1 (F3, low confidence) llmjacking summary: "actors used exposed or stolen cloud identities, service-account keys and GitHub tokens to enable managed model services such as Amazon Bedrock and the Gemini API". GTIG lists GitHub PATs among the initial-access tokens (one actor combined a stolen PAT for private code repositories with a web-app flaw in a container) and credits the enabling of model services to "Abuse of access keys". The summary chains GitHub tokens to the enabling. Fix: say the tokens gave initial access and the actors then enabled the services.
- #2 (F3, low confidence) llmjacking Detection: "Datadog saw similar probing at 12 customers in 30 days: failed ListFoundationModels calls across several regions". Datadog: "In the last 30 days, we've observed 12 organizations display similar malicious behavior. In the majority of instances, we have seen failed ListFoundationModels API calls in multiple regions", and one case differs (successful list calls, then Converse AccessDenied). The clause drops "in the majority of instances" and says "customers" where the page says "organizations".

### Unsupported / hallucinated facts

- #3 (F4, low confidence) sshole Detection: "no source publishes an indicator beyond that". The ISC page this run added lists scanner source addresses and the behavior "attempts that used an all "A" password"; Previdian's timeline shows "Indicators of compromise added (13)" (Pro tier). The sentence is no longer literally true after the newest section; reword to a log indicator and say listed scanner addresses are omitted.
- #4 (F4, low confidence) sshole sourcing_note: "OX Security's analysis is the source of the mechanism, the condition that an account's password field is `*`, the CVSS score and the Alpine fixed-package table". Alpine's own advisory (a listed source) carries the mechanism ("musl's crypt() returns the string * as an error indicator when the key is over 256 bytes long"), the `*` account condition and the fixed-package table (edge 10.6_p2-r0 ... 3.16 9.0_p1-r6). Only the CVSS score is outside the vendor sources. Re-attribute in the note (and consider citing the Alpine advisory over OX in the body where it carries the same fact).

### Editorial / less-is-more flags (advisory)

- #5 (F11) llmjacking techniques[]: GTIG "exploited token-creation privileges to generate temporary credentials for high-privilege service accounts" maps to T1548.005 (Temporary Elevated Cloud Access, active in the pin), not in techniques[]; metadata-only, no body words.
- #6 (F11) sshole Improvement section: "writing of the first scanners, its author expects ..." is a garbled clause; suggest "after listing the first scanners, its author expects ...".

### Checks with no finding

- All five new-entry evidence quotes and the six sshole evidence quotes are contiguous substrings of pages read this iteration; sources[] dates equal the pages' own dates (GTIG 11-02, Wiz 10-20, Datadog 10-06, ISC 11-08, Previdian 11-05, OX 11-05 by feed pubDate).
- Updated-entry contract: the diff shows only the changes the improvement record's fields name (sources, evidence, sourcing_note, summary, body); `updated_at` untouched; section and record states agree; an independent second sensor set fits the improvement definition in docs/pipeline.md.
- LLMjacking: analysis 544 words (bound 550); no IOCs, no em dash, no pipeline vocabulary; classification B/2 matches mandiant-gtig reliability B; actions empty; references[] link to the 2026-08-07 entry; no CVE overlap with the store (the LiteLLM CVE id is deliberately absent, the run record's Contradiction line is accurate: the Obsidian entry carries CVE-2026-40217 as a Custom Code Guardrails RCE).
- Run record: counts and updated_entry_ids match the files; notes' claims about the GTIG id and the store hold. No missed angle I can name with a plausible in-window source (NCSC hub newest items are 2026-11-06 and covered; KEV has no new addition).

### Verdict

NEEDS_FIXES (truth: 4, editorial: 0, advisory: 2). All four truth items are low-confidence clause-level imprecisions; no hallucinated entity, broken URL, wrong date or unsupported number was found.
