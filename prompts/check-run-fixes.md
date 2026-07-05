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
| `run-counters` | `entries_published` / `entries_updated` / `deep_dive` don't match the files on disk | Recount and correct — the record must describe what the run actually wrote |
| `prompt-version` | Record's `prompt_version` ≠ newest `prompts/CHANGELOG.md` heading | If you edited a prompt this run: add the CHANGELOG entry + bump the banner. Otherwise correct the record to the current version |
| `sources-touched` | No source has `last_successful_fetch` = run date | Phase 5 bookkeeping was skipped — update `sources/sources.json` for every source that contributed |
| `sources-schema` | Malformed source record (e.g. `category` as string, `name` instead of `publisher`) | Use the canonical candidate shape in `prompts/cti-run.md` Phase 5 — `category` is ALWAYS a list; the field is ALWAYS `publisher` |
| `closed-source-tlp` | Above-CLEAR closed-source citation on a public deployment | Remove the citation AND any detail only the restricted document supports; the document may only be a lead to public sources |
| `ioc-scan` | Hash / routable IP in an entry | Rewrite to the *behaviour*, not the indicator; version strings near the match are auto-suppressed, so a real hit is a real IOC |
| `fetch-failure-bridge-required` | Known-403 source logged as failed without a bridge attempt | Re-fetch via `python3 tools/fetch_source.py <subcommand>`; the record's `attempted_methods` must show the bridge |
| `test-build` | `site/test_build.py` failing | Read the test output tail — usually an entry that breaks a renderer assumption; fix the entry, not the test |

WARNs worth acting on before Phase 5.7: `budget` (justify or cut),
`single-source-flag` (fix the `verification` value), `evidence-binding`
(attribute quotes to a listed publisher), `aggregator-only` (find the
primary), `org-triage` (align with the profile scheme), `essential-coverage`
(disclose the miss in the run record).
