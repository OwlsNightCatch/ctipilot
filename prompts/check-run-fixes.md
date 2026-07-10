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
| `dedup` | Non-update entry shares CVEs with the last 14 days | Either convert to an update note (`update_of: <prior entry id>`, body = delta only) or delete the entry (it's covered) |
| `update-target` | `update_of` unresolved, later-dated, or cyclic | Point at the real prior entry id (`YYYY-MM-DD/slug`); chains must run backwards in time |
| `cve-sync` | CVE in an entry but not in `state/cves_seen.json` | Append the CVE record to `cves_seen.json` (id, title, primary_source_url, first_seen, last_seen) |
| `blocked-source` | Source URL is an NVD/MITRE per-CVE page, homepage, category landing, or advisory index | Replace with the specific vendor PSIRT / article / advisory URL you actually fetched; NVD/MITRE pages are auto-referenced by the site and never citable |
| `source-urls` (404) | A cited URL doesn't resolve — usually fabricated | Re-pivot to the real URL via WebSearch / the bridge; if none exists, the claim is unsourced — drop it (and possibly the entry) |
| `run-record` | Missing/incomplete run record, bad verification counters | Complete the frontmatter per `docs/pipeline.md` § Run records; `verification_residual_count` = final-iteration truth+editorial on NEEDS_FIXES, 0 on CLEAN |
| `run-record` (verification block, BEFORE Phase 5.7) | `verification.iterations missing or empty` on the gate run that precedes the first verifier spawn | Expected at that stage — run the pre-loop gate as `check_run.py "$RUN_ID" --pre-verify` (downgrades exactly this class to WARN). NEVER hand-write a verification block a verifier didn't produce; once iteration 1 is recorded, use the plain invocation |
| `run-counters` | `entries_published` / `entries_updated` / `deep_dive` don't match the files on disk | Recount and correct — the record must describe what the run actually wrote |
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

WARNs worth acting on before Phase 5.7:
`single-source-flag` (fix the `verification` value), `evidence-binding`
(attribute quotes to a listed publisher), `aggregator-only` (find the
primary), `attack-mapping` on `research`/`annual-report` (map the described
tradecraft unless the piece genuinely carries no TTP content),
`essential-coverage` (disclose the miss in the run record). The `composition` line is
informational only (rolling-24 h entry/deep-dive/critical counts) — volume
follows relevance, not a quota, so there is nothing there to fix.
