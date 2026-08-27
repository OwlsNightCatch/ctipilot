# check_run.py — fix recipes for common FAILs

Referenced from `prompts/cti-run.md` Phase 5.5. The script is read-only —
every FAIL is yours to fix, then re-run until exit 0. Check ids below match
`tools/check_run.py` output labels.

| FAIL | What it means | Fix |
|---|---|---|
| `entry-parse` / `run-parse` | Frontmatter steps outside the strict YAML subset (tabs, flow nesting, bad indent) | Re-write the frontmatter within the subset (`docs/pipeline.md` § Frontmatter); `site/content_model.py` is the reference parser |
| `entry-schema` | Missing/invalid field, taxonomy value, enum, slug/date mismatch | The error names the field — fix the value against `site/taxonomy.yaml` / `docs/pipeline.md`; folder date must equal `discovered_at`'s UTC date |
| `entry-schema` (priority) | `priority: critical` without `immediate_action`, or vice versa | Either add the immediate_action block (only if the stop-and-act bar truly holds) or demote to `high` |
| `entry-schema` (evidence) | Exploited-status CVE or critical entry without `evidence[]` | Populate verbatim quotes from the findings YAML (`work/<run-id>/findings.*.yaml`); if none exist, re-assess whether the exploited status is actually sourced |
| `entry-schema` (verification) | `multi-source` with <2 sources | Set the correct `verification` value (`single-source*`) + `sourcing_note`, or add the genuinely independent second source you already fetched |
| `entry-schema` (entities) | Entity key not in `entities/registry.yaml` | Register the entity (key, type, name, aliases, sourced summary, first_seen) — or fix the key to the existing entity (check aliases first) |
| `registry` | Alias/name collision or malformed registry record | Merge the duplicate into the existing key (aliases append-only); never mint a second key for a known entity |
| `registry` (relations) | Unknown relation type, endpoint-type violation, tombstone endpoint, duplicate edge, missing/unresolvable `source` entry, or a leftover untyped `related` key | Follow `docs/pipeline.md` § Relationships: vocabulary type + canonical direction, `to` = canonical key, symmetric edges stored once, `source` = the entry id whose cited reporting establishes the edge; migrate any `related` list to typed `relations[]` |
| `dedup` | A NEW entry shares a CVE id with an existing entry anywhere in the store (any age) and does not list that entry in `references[]` | One living entry per finding (docs/pipeline.md § Entry lifecycle): delete the new file and append an `updates[]` changelog record + `## Update — <at>` section to the existing entry (the delta only, frontmatter brought to the current state); if it is genuinely a distinct finding building on the older one, declare it — add the older entry id to `references[]` |
| `dedup` (WARN, entity overlap) | A NEW entry shares an entity key with an entry from the last 14 days | Confirm it is a distinct story; if it is a development of that entry's finding, fold it into that entry's changelog instead |
| `entry-schema` (updates[]) | Changelog shape: a record missing `at`/`run_id`/`type`/`summary`, `at` not later than the previous record / `discovered_at`, `updated_at` ≠ last record's `at`, or body `## <Type> — <at>` sections not pairing 1:1 in order with the records | Fix the record or the heading so they match exactly (`content_model.update_section_heading`): one section per record, same order, same `at`, type ∈ update / correction / improvement; set `updated_at` to the last record's `at` |
| `entry-schema` (update_of) | An entry carries a non-null `update_of` | Retired in v4.0 — never a second entry: append the delta to the existing entry as a changelog record and delete this file |
| `entry-updates` | A record's `run_id` resolves to no run record; two records from the same fire on one entry; `fields` names a non-frontmatter key | Use this run's id; fold this fire's changes into ONE record per entry; `fields` lists frontmatter keys (or `body`) |
| `silent-edit` | An entry file was modified in the working tree without a changelog record for this run (or an entry file was deleted) | Every change ships as an `updates[]` record with this run's id + a `## <Type> — <at>` section (a correction fixes the wrong text AND says what changed); restore any deleted entry — runs never remove entries |
| `legacy-shape` | A v4.0+ run wrote a `synthesis`/`outlook` entry, a `horizon: strategic` entry, a `weekly_section`, or the run record's kind is `weekly` | The weekly routine is retired: v4 entries are `operational` with a kind from `content_model.ACTIVE_KINDS`; run kinds are `intel` / `audit` |
| `cve-sync` | CVE in an entry but not in `state/cves_seen.json` | Append the CVE record to `cves_seen.json` (id, title, primary_source_url, first_seen, last_seen) |
| `blocked-source` | Source URL is an NVD/MITRE per-CVE page, homepage, category landing, or advisory index | Replace with the specific vendor PSIRT / article / advisory URL you actually fetched; NVD/MITRE pages are auto-referenced by the site and never citable |
| `source-urls` (404) | A cited URL doesn't resolve — usually fabricated | Re-pivot to the real URL via WebSearch / the bridge; if none exists, the claim is unsourced — drop it (and possibly the entry) |
| `run-record` | Missing/incomplete run record, bad verification counters | Complete the frontmatter per `docs/pipeline.md` § Run records; `verification_residual_count` = final-iteration truth+editorial on NEEDS_FIXES, 0 on CLEAN |
| `run-record` (verification block, BEFORE Phase 5.7) | `verification.iterations missing or empty` on the gate run that precedes the first verifier spawn | Expected at that stage — run the pre-loop gate as `check_run.py "$RUN_ID" --pre-verify` (downgrades exactly this class to WARN). NEVER hand-write a verification block a verifier didn't produce; once iteration 1 is recorded, use the plain invocation |
| `run-counters` | `entries_published` (new files with this run_id) / `entries_updated` (existing entries carrying this run's changelog record) / `updated_entry_ids` (their ids — REQUIRED on v4.0+ records, `[]` when none) / `deep_dive` don't match the disk | Recount and correct — the record must describe what the run actually wrote and updated |
| `prompt-version` | Record's `prompt_version` ≠ newest `prompts/CHANGELOG.md` heading | If you edited a prompt this run: add the CHANGELOG entry + bump the banner. Otherwise correct the record to the current version |
| `sources-touched` | No source has `last_successful_fetch` = run date | Phase 5 bookkeeping was skipped — update `sources/sources.json` for every source that contributed |
| `sources-schema` | Malformed source record (e.g. `category` as string, `name` instead of `publisher`) | Use the canonical candidate shape in `prompts/cti-run.md` Phase 5 — `category` is ALWAYS a list; the field is ALWAYS `publisher` |
| `classification` (code) | An entry's `classification.reliability` / `.credibility` is outside the configured vocabulary (A–F / 1–6) | Set a defined code — reliability from the cited source's own letter in `sources/sources.json`, credibility from corroboration (see the § Intel classification scheme) |
| `classification` (missing rating) | A v3.18+ entry ships with neither rating — a non-triage entry missing `classification`, or (no triage scheme configured) a triage-kind entry missing it too | Add the Admiralty block: reliability from the cited source's letter, credibility from corroboration. Every entry carries exactly one rating — never zero |
| `classification` (triage-kind drift, WARN) | A triage-kind entry carries `classification` while a configured triage scheme owns that kind | Move the rating to `org_triage` per the scheme and set `classification: null` |
| `org-triage` | Scheme configured but a v3.18+ triage-kind entry misses `org_triage`, or names an undefined category | Apply the scheme's criteria to the entry's cited facts and set `org_triage: {category, rationale}`; no matching criteria → the scheme's default with the reason stated |
| `attack-mapping` (empty techniques[]) | A v3.18+ `threat`/`incident`/`vulnerability` entry has an empty `techniques[]` | Map every technique the sources support — at minimum the access/exploitation vector (exposed-service RCE → T1190, phishing → T1566, LPE → T1068, …); evidence-bound, never invented; active ids per `attack/enterprise-attack.json` |
| `closed-source` (WARN) | A `closed_sources` citation doesn't trace to a file under `intel/` | Point `ref`/`title` at the actual drop file so the verifier can `Read` it (there is no TLP gate — everything in `intel/` is processable) |
| `ioc-scan` | Hash / routable IP in an entry | Rewrite to the *behaviour*, not the indicator; version strings near the match are auto-suppressed, so a real hit is a real IOC |
| `fetch-failure-bridge-required` | Known-403 source logged as failed without a bridge attempt | Re-fetch via `python3 tools/fetch_source.py <subcommand>`; the record's `attempted_methods` must show the bridge |
| `test-build` | `site/test_build.py` failing | Read the test output tail — usually an entry that breaks a renderer assumption; fix the entry, not the test |

**WARNs are all worth acting on — the zero-warning discipline (v3.28) makes every WARN a work item.** Fix every warning this run caused or can fix before commit. What a run legitimately leaves behind: its own telemetry facts (e.g. this run's runaway `duration_seconds` — explain in the notes) and settled history on prior run records; the quality audit sweeps those to zero, fixing causes (an entry defect is fixed through the entry's changelog) or acknowledging genuinely unfixable ones in `state/warning_acknowledgments.json` (check + specific match + reason + date — audit-only; a run never self-acknowledges). A `ack-ledger` FAIL means a malformed/unreadable ledger record — fix the JSON shape (`check`, `match` ≥12 chars pinning the subject, `reason`).

Frequent WARN recipes:
`registry-relations` (the edge's `source` entry neither keys nor names an
endpoint — confirm the entry actually establishes the connection, or point
`source` at the one that does),
`single-source-flag` (fix the `verification` value), `evidence-binding`
(attribute quotes to a listed publisher), `aggregator-only` (find the
primary), `attack-mapping` on `research`/`annual-report` (map the described
tradecraft unless the piece genuinely carries no TTP content),
`essential-coverage` (disclose the miss in the run record). The `composition` line is
informational only (rolling-24 h entry/deep-dive/critical counts) — volume
follows relevance, not a quota, so there is nothing there to fix.
