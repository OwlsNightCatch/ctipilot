**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-09T04:05:33Z · ended_at=2026-11-09T04:10:19Z · duration_seconds=286

## Verification report — 2026-11-09T0255Z-intel (iteration 4)

Scope: new entry llmjacking-stolen-cloud-keys-enable-model-services-resale; updated entry 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole (improvement record 2026-11-09T03:25:45Z, git diff HEAD read); run record. Claim ledger: all 45 claims walked (4 changed claims, every other claim of both entries), rows in verification.iter4.claims.yaml, all `ok`.

### Prior-iteration deltas (all six remediations confirmed)
1. LLMjacking summary: GTIG says tokens are the "dominant initial access vector" and "Abuse of access keys allowed the threat actor to modify and enable LLM API services (e.g. Bedrock, Gemini API, etc.)". The summary now says tokens gave initial access and actors then enabled the services. Supported.
2. LLMjacking Datadog clause: Datadog "In the last 30 days, we've observed 12 organizations display similar malicious behavior. In the majority of instances, we have seen failed ListFoundationModels API calls in multiple regions". Body now reads "12 organizations in 30 days, mostly as failed ListFoundationModels calls across several regions". Supported.
3. sshole Detection line: "no source publishes a further log indicator". Alpine and OX give only the `Accepted password for` search plus doas/users/keys review; ISC's all-A password and scanner list come from honeypot logs, not an sshd authentication log. Clause holds.
4. sshole sourcing_note: Alpine's advisory (read this iteration) carries the mechanism ("musl's crypt() returns the string * as an error indicator when the key is over 256 bytes long"), the `*` condition and the fixed-package table; OX Security (read through its RSS feed, the page itself answers 403 on every rung) carries CVSS 3.1 8.1. Supported.
5. T1548.005: GTIG "one threat actor exploited token-creation privileges to generate temporary credentials for high-privilege service accounts". Mapping supported.
6. sshole clause "after listing the first scanners, its author expects": ISC "Here is a list with initial scanners ... I expect quite a few of these login attempts were successful for our honeypots". Reads correctly and is supported.

### Cold pass
- All five evidence quotes of the LLMjacking entry and all six of the sshole entry are verbatim in the fetched pages (ISC quote with the all "A" password matches; OX quote matched in the OX feed item).
- ISC counts (232/713/246/51, 11-08 partial day), Previdian counter (20 attempts, 13 IPs, 9 countries, last observed 08 Nov, page updated 09 Nov), NCSC advisory date and fields, Alpine fixed-package table, heise statements, THN honeypot statement: all match. Source dates match (GTIG 2026-11-02, Wiz 2026-10-20, Datadog 2026-10-06, Previdian 2026-11-05, ISC 2026-11-08).
- Changelog contract 4c: record `improvement`, fields (sources, evidence, sourcing_note, summary, body) cover every changed line in the diff (the earlier section's Previdian date labels follow the `sources` date change); `updated_at` unchanged; section present and cited; record summary equals the section; no supersession left behind (the "one telemetry vendor" statement was replaced; the 2026-11-07 section keeps its dated "as read on 2026-11-07" figures as history).
- Dedup: no earlier in-window entry carries LLMjacking, LiteLLM `/key/regenerate` or UNC6993; the 2026-08-07 token-jacking entry is declared in `references[]`. CVE-2026-40217 left out deliberately; the run record's Contradiction line holds (store carries it on the 2026-06-16 Obsidian LiteLLM entry as a different flaw, custom-code guardrail execution).
- Style: no em dash outside section headings, no IOCs, no pipeline vocabulary in reader-facing text; analyses at 546 and 549 words.
- Run record: KEV claim holds (kev_window_diff 0 rows; catalogue 2026.11.06, newest addition 2026-11-06); updated_entry_ids match.
- Missed angles: two WebSearch probes (in-window exploited zero-days, Swiss cantonal/communal incidents) surfaced nothing dated in the window that the store lacks (the Chrome V8 zero-day CVE-2026-11645 is already covered since 2026-06-10). Coverage looks complete for the window.
- Considered and not raised: Detection line of the sshole entry could mention the post-login recon commands and the all-A password, but both are already in the sections below and the analysis is at its word bound; `cves[].fixed` credits the Alpine table "per OX Security" while the sourcing note names Alpine's advisory (both carry the identical table).

### Verdict
CLEAN
