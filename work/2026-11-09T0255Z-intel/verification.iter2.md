**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-09T03:46:32Z · ended_at=2026-11-09T03:54:44Z · duration_seconds=492

## Verification report — 2026-11-09T0255Z-intel (iteration 2)

Scope: 46 of 46 ledger claims walked (all rows in verification.iter2.claims.yaml: 38 ok, 3 F3, 1 F14, 3 F5, 0 unreadable; the F5 rows are truth-supported but unlinked). Prior-iteration deltas: all 14 remediations re-checked against the cited pages (below). OX Security's page answers 403 on every rung (extract, url, jina, WebFetch); its claims were read in the full-content RSS copy of the same post saved by the 2026-11-06 run (work/2026-11-06T0255Z-intel/bodies/ox-feed.xml, pubDate Thu 05 Nov 2026). Gate: check_run exit 0, 58 pass 0 warn (re-run this pass).

### Delta check (iteration 1 findings)
1. Triage line: GTIG "Any calls to disable logging by non-IaC (Infrastructure as Code) principals should be treated as high severity." (AWS Bedrock bullet). Fix supported.
2. "One actor ... another": GTIG has a single actor harvesting GitHub-exposed keys; Ollama is a separate actor (Figure 2). Fix supported.
3. Exposure keeps internet-reachable endpoints only; GTIG: "identifying publicly exposed LLM endpoints". Fix supported.
4. Persistence sentence: GTIG "established persistence by creating unauthorized IAM and service accounts and injecting SSH keys"; the review step is the entry's own advice. Fix supported.
5. Takeaway: Azure "require Diagnostic Logs to be enabled", GCP Data Access logs "disabled by default". Fix supported.
6. sourcing_note Datadog: frontend bundle of one platform (KMON_NOC), two Python scripts, "12 organizations" in 30 days, "We cannot establish a link between the script analyzed ... and the telemetry". Fix supported.
7. Composition sentence removed. Confirmed absent.
8. LiteLLM /key/regenerate, Ollama and "burn and rotate" present and match GTIG (the LiteLLM sentence is unlinked, see F5 below).
9. ISC hosting/telecom spread: scoped to the 2026-11-05 initial-scanner table (COLT, Datacamp, SERVER-MANIA, DMZHOST, Uzbektelekom, Telecom Armenia, Korea Telecom ...). Fix supported.
10. ISC 255-character limit and the author's expectation are attributed to ISC. Fix mostly supported; scope nit below (F3 #2).
11. Previdian: JSON-LD datePublished 2026-11-05T15:46:26Z (dateModified 2026-11-08T03:10:36Z); sources[] date and both inline labels are right.
12. Previdian counter: page shows 20 attempts, 13 unique attacker IPs, 9 countries, last observed 08 Nov 2026; summary and section match.
13. Datadog evidence quote: "Valid credentials then undergo a separate check for Bedrock access" verbatim on the page.
14. Run record: discovery note matches findings.S3.yaml discovery_trace (Infosecurity Magazine and Dark Reading titles of 2026-11-03, then the GTIG post). The CVE contradiction line is true: the store's 2026-06-16 Obsidian entry carries CVE-2026-40217 as the LiteLLM Custom Code Guardrails exec() flaw; GTIG attaches it to a /key/regenerate user-ID rebind. Leaving the id out is defensible; a web search found no LiteLLM advisory for /key/regenerate.

### Citation does not support the claim
- #1 (F3, low confidence) 2026-11-06/cve-2026-123158-...-sshole, record 2026-11-09T03:25:45Z summary: "peaking on 2026-11-06 and lower by 2026-11-08". ISC (https://isc.sans.edu/diary/33498) states no trend; its table counts "long passwords" (ISC says buggy brute-force scripts also produce them) and the page's "Last Updated: 2026-11-08 15:44:33 UTC" means 51 on 11-08 is a partial day. Drop "lower by 2026-11-08" and flag 51 as a partial day (or drop the trend).
- #2 (F3, low confidence) same entry, Improvement section: "its author expects that quite a few of the attempts succeeded on its honeypots". ISC: "I expect quite a few of these login attempts were successful for our honeypots", directly after the 2026-11-05 initial-scanner table. The entry widens it to the whole 232/713/246/51 series. Scope it to the 2026-11-05 scanners.
- #3 (F3, low confidence) 2026-11-09/llmjacking-..., Detection: "ends with external billing administrators and foreign projects linked to the billing account, which are the events to watch ([Wiz, ...])". Wiz describes the behavior and gives no detection guidance; the watch advice is the entry's own. End the cited clause after "billing account".

### Quantifier without source
- #4 (F14, low confidence) 2026-11-09/llmjacking-..., Exposure: "an account that never used model services is in scope, because the actors enabled them". GTIG: "In multiple incidents that Mandiant investigated, LLM services were not enabled at the time of compromise." Nothing says the accounts had never used them. Use "an account where model services are not enabled".

### Claims missing inline citation
- #5 (F5, low confidence) 2026-11-09/llmjacking-..., second paragraph: three consecutive factual sentences ("After the foothold the actors created ...", "In multiple incidents the model services were not enabled at compromise ...", "A follow-on cluster holding pre-validated virtual keys exploited the victim's LiteLLM gateway ...") carry no link. GTIG supports each (checked), so this is a link omission, not a truth defect; add the GTIG link after each (no word cost).

### Editorial / less-is-more flags (advisory)
- #6 (F11) 2026-11-09/llmjacking-..., techniques[]: GTIG describes exfiltrating "infrastructure credentials, internal database passwords, and third-party API keys from cloud secret managers" (T1555.006) and cloning codebases to search for hardcoded secrets (T1213.003); both are active in the pin and unmapped.

### Checked, no defect
Updated entry contract (4c): record type `improvement` with a `## Improvement` section of the same `at`, `updated_at` untouched (2026-11-07T03:52:19Z), `fields` match the diff (sources, evidence, sourcing_note, summary, body), no silent edit; the genuine new material is independent corroboration of an existing exploitation status, so `improvement` is defensible. Supersession: the 2026-11-07 section's "as read on" counts are dated and followed by the refreshed counter. KEV: catalogue 2026.11.06 carries no CVE-2026-123158 row. Classification A/2 and B/2 consistent (NCSC-CH primary with corroboration; GTIG source rated B in sources.json, corroborated by Wiz and Datadog on the pattern). No IOCs, no em dash outside the two section headings, no workflow-internal language. No in-window omission I can evidence; web searches for 2026-11-08 zero-days and Swiss public-sector incidents surfaced nothing newer than the store's coverage. Coverage looks complete.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 1)

All five numbered findings are low-confidence and small; each fix is a clause-level edit with no word-count cost except #4 (neutral) and #1/#2 (neutral). The CLEAN chain restarts after remediation.

### Findings summary (machine-readable)
See work/2026-11-09T0255Z-intel/verification.iter2.findings.yaml.
