**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-09T03:34:16Z · ended_at=2026-11-09T03:42:03Z · duration_seconds=467

## Verification report — 2026-11-09T0255Z-intel (iteration 1)

Scope read: new entry `2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale`; updated entry `2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole` (whole entry, `git diff HEAD`, Improvement record and section); run record. All 25 ledger claims walked (rows in `verification.iter1.claims.yaml`: 17 ok, 7 F3/F14, 1 F4). Sources fetched this iteration: GTIG/Mandiant post (extract), Wiz (extract), Datadog (extract), SANS ISC diary 33498 (extract), Previdian (extract and raw JSON-LD), The Hacker News (extract), Alpine advisory (extract). OX Security's page answered 403 on every rung (extract, url, WebFetch, jina), so its pre-existing claims were checked against the cached full-text feed copy in `work/2026-11-06T0255Z-intel/bodies/ox-feed.xml` (Detection advice, CVSS 8.1 v3.1, Alpine fixed table, doas on alpine user, container carve-out and rebuild advice all present). No `closed_sources`. Gate: 6 evidence quotes verbatim (rechecked; all present on pages I read). Dedup: no overlap with the 14-day prior-coverage index (only the sshole entry matches); `references[]` target `2026-08-07/ai-api-token-jacking-transfer-station-resale` exists; the store's CVE-2026-40217 is the Obsidian entry's different LiteLLM flaw, as the run record says.

### Citation does not support the claim

- **#1 (F3), LLMjacking, Triage line.** Entry: "GTIG treats a change to model invocation logging by a principal outside infrastructure-as-code as high severity". GTIG: "Any calls to disable logging by non-IaC (Infrastructure as Code) principals should be treated as high severity." The entry widens "disable" to any "change". Fix the verb.
- **#2 (F3, low confidence), LLMjacking, Exposure line.** "any model endpoint or LiteLLM gateway reachable from the internet". GTIG: actors "focus on either identifying publicly exposed LLM endpoints or obtaining valid LLM API keys"; the LiteLLM gateway was attacked after a follow-on cluster acquired "pre-validated Virtual Keys". No internet-reachability statement for LiteLLM.
- **#3 (F3, low confidence), LLMjacking, Detection line.** "Revoking a stolen key does not remove the accounts, policy attachments and SSH keys GTIG describes as the actors' persistence". GTIG describes the persistence, not that revocation leaves it; this is the entry's inference under a GTIG citation.
- **#4 (F3, low confidence), LLMjacking sourcing_note.** "Datadog reads the AWS validation logic from one platform's frontend code and did not observe its AWS API activity." True of KMON_NOC only; Datadog also analyses two Python validators, recaps two earlier harvesting platforms (GetCallerIdentity, ListFoundationModels, InvokeModel) and reports "In the last 30 days, we've observed 12 organizations display similar malicious behavior".
- **#5 (F3, low confidence), sshole Improvement section.** "from sources spread across commercial hosting and telecom networks" is attached to the 11-03 to 11-08 series; ISC's only breakdown is the "initial scanners" table whose counts sum to 232, the 2026-11-05 figure.
- **#6 (F3, low confidence), sshole Improvement section.** "The honeypots keep only the first 255 characters of a password, so the counts show attempts, not success". ISC states the 255-character limit and "I expect quite a few of these login attempts were successful for our honeypots"; the "so ... show attempts, not success" is the entry's inference. The section also explains only the 23 of 11-01 and leaves 5 (11-03) and 58 (11-04), both before disclosure and before ISC's "first actual exploit attempt ... November 5th", unexplained.
- **#7 (F3, low confidence, pre-existing), sshole `sources[]` Previdian.** Entry date 2026-11-07; page JSON-LD `datePublished` 2026-11-05T15:46:26Z, `dateModified` 2026-11-08T03:10:36Z. Prose says "as read on 2026-11-07", but the source date field and inline cite drift two days from publication.

### Unsupported / hallucinated facts

- **#8 (F4, low confidence), LLMjacking Defender takeaway.** "Switch on the model-call logs the cloud keeps off by default, or abuse stays invisible." GTIG gives default-off only for Google Cloud Data Access logs and says Azure invocations "require Diagnostic Logs to be enabled"; nothing on AWS defaults. "Abuse stays invisible" conflicts with the entry's own Detection line (control-plane enablement events stay visible, and GTIG calls them critical).

### Quantifier without source

- **#9 (F14), LLMjacking paragraph 1.** "Other actors harvested LLM API keys from public GitHub repositories and validated them with single-token requests". GTIG: "a threat actor opportunistically harvested exposed corporate LLM API keys from public GitHub repositories ... the group conducted automated credential validation sweeps". One actor.

### Needs more research

- **#10 (F8), LLMjacking.** `affected_products` lists LiteLLM and Ollama and `entities` carries `product:litellm`, but the body never says a LiteLLM flaw was exploited or that Ollama appears. GTIG: "exploited a user ID rebind vulnerability in the /key/regenerate endpoint ... to elevate standard Virtual Keys into full PROXY_ADMIN", "Gateway Patch Management ... (e.g., LiteLLM)", Figure 2 "Threat Actor tests publicly exposed Ollama endpoints and attempts to register their own models". Also dropped though observable: "burn and rotate" creation and deletion of short-lived service accounts, GPU provisioning across regions with quota-increase requests, and a containerized agent backdoor. The CVE id can stay out; add the behavior and the patch advice.

### Editorial / less-is-more flags (advisory)

- **#11 (F11), LLMjacking sourcing_note.** "GTIG attaches a CVE identifier to the LiteLLM key-regeneration flaw; it is not repeated here because no LiteLLM advisory read confirms it." Composition rationale in a reader-facing field, referring to a flaw the body does not describe. The actual conflict (the store's 2026-06-16 Obsidian entry carries CVE-2026-40217 as the Custom Code Guardrails RCE; GTIG binds it to /key/regenerate) sits in the run record under "Contradiction: none".
- **#12 (F11), sshole.** The run's saved Previdian body (fetched 03:21Z today) reads "20 exploitation attempts, 13 unique attacker IPs, and 9 countries ... last observed Nov 08, 2026"; the entry still shows 15/10/8 "as read on 2026-11-07". Accurate as dated, stale against a figure in hand.
- **#13 (F11), LLMjacking evidence[4].** "Attackers use similar tactics when targeting LLM resources in AWS." Verbatim, but "similar" points to the preceding SES/SNS sentence; read alone it carries nothing. The STS GetCallerIdentity then Bedrock-check sentence would carry the cited fact.
- **#14 (F11, low confidence), run record notes.** "First coverage through the `mandiant-gtig` lookback" versus S3's discovery_trace ("first seen at: infosec-magazine feed ... and darkreading feed", then a pivot to the GTIG feed); `mandiant-gtig`, `datadog-security-labs` and `sans-isc` are in no sub-agent's `sources_attempted`/`sources_used` yet `sources_changed` marks them fetched and used.

### Updated entry, changelog contract (4c)

Record `2026-11-09T03:25:45Z` / `improvement` / fields `[sources, evidence, sourcing_note]`: section `## Improvement — 2026-11-09T03:25:45Z` present with the same `at`; `updated_at` correctly unchanged (`2026-11-07T03:52:19Z`); `discovered_at`, `run_id`, path untouched; the diff shows no change outside the three named fields, the record and the section. The ISC counts (5, 58, 232, 713, 246, 51, and 23 on 11-01) and the first-attempt date match the page; the new evidence quote is verbatim. The record's summary matches the section (first attempts 2026-11-05, peak 2026-11-06, lower by 2026-11-08, two sensor sets, no compromised production host). `improvement` fits the docs' definition ("a second independent source"). Supersession: the old "one telemetry vendor" sentence in `sourcing_note` was replaced; no other statement is disproved by the new section. Only the #5 and #6 wording above need attention.

### Missed angles

Coverage looks complete for the window. Searches for exploited vulnerabilities and Swiss public-sector incidents dated 2026-11-08/09 surfaced nothing newer that the store lacks (the Cisco SD-WAN CVE-2026-20245 hit was a June item, already covered). The CERT.LV refrigeration drop is defensible (Estonia and Finland already in the Danfoss entry; the Latvian warehouse is the only new fact), although "the entry is past the word bound" is a weak stated reason.

### Verdict

NEEDS_FIXES (truth: 9, editorial: 1, advisory: 4)

### Findings summary (machine-readable)

See `work/2026-11-09T0255Z-intel/verification.iter1.findings.yaml` (14 records).
