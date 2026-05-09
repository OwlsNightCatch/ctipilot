# `tools/check_brief.py` — common FAILs and how to fix them

Phase 5.5 of the daily and weekly Claude Code routines runs `python3 tools/check_brief.py` as a non-negotiable gate before commit. The script is read-only — it surfaces drift, you fix it. Below is the operator playbook for the common FAIL patterns the script emits.

The full check list (1–19) lives inline in `prompts/daily-cti-brief.md` § Phase 5.5; this doc is the remediation handbook.

---

## How to fix common FAILs

| FAIL | Fix |
|---|---|
| `cve-sync: missing from cves_seen.json: [...]` | Append the listed CVE entries under § Phase 5 / `state/cves_seen.json` (historical-context CVEs and deferred CVEs count too — anything with a `CVE-…` token in the brief). |
| `footer-presence: items without v2 footer` | Re-`Edit` the affected H3 to append a `— *Source: [Title](URL) · Tags: … · Region: …*` line. |
| `run-log-fields: ... missing keys` | Rewrite today's record in `state/run_log.json` to match the schema in § Phase 5 (`sub_agents`, `fetch_failures`, `items_published`, `deep_dive`, `verification_iterations`, `verification_residual_count` are all required). |
| `run-log-subagents: sub-agent records incomplete` | Each of S1, S2, S3, S4 must have `{sources_attempted: [...], sources_used: [...], items_returned: N, returned: true|false}`. Empty arrays are fine on a stalled sub-agent (`returned: false`). |
| `sources-touched: no source has last_successful_fetch == today` | Update `last_successful_fetch` on every source you actually fetched today. |
| `footer-taxonomy: unknown ...` | Either correct the footer or extend `site/taxonomy.yaml` in the same commit. |
| `fetch-source-403: 403/429 on known-403 hosts not mitigated` | Re-run the affected URL via `python3 tools/fetch_source.py …` and update the source bookkeeping. |
| `multi-cve-cvss: N CVEs but single CVSS` | Either confirm both CVEs share that CVSS (single value is fine) or write per-CVE: `CVSS: 9.1 / 7.2` or `CVSS: 9.1 (CVE-…), 7.2 (CVE-…)`. |
| `blocked-source: ... cites https://nvd.nist.gov/vuln/detail/CVE-…` | Replace with the vendor PSIRT advisory or research blog. NVD/MITRE/cve.org per-CVE pages are blocked as Sources — they are derived. The build still surfaces them automatically as External References on every per-CVE page. |
| `blocked-source: ... cites <publisher>/news/` (or any landing) | Re-fetch and link the **specific article URL** (i.e. the article's own page with its own slug, not the section landing). Generic landings are not Sources. |
| `source-urls: <url> returns 404` | The URL is fabricated or moved. Re-do the primary-source pivot (`WebSearch` for the topic, fetch the result, swap the citation). If the original primary genuinely doesn't exist, drop the item. |

---

## WARN-level signal (not blocking)

- **`primary-source-quality` WARNs** — items whose first source is NVD or a CERT/NCSC. Re-pivot to the vendor advisory / research-lab post / vendor blog and put NVD or the CERT as `Additional source:` instead.
- **`covered-items` WARNs** — `covered_items.json` drift relative to the brief. The next run rebuilds from the brief, so this is observability, not a hard block.

---

## Operating principle

The script is read-only by design — drift is what *you* fix; the script just surfaces it. Maintaining `tools/check_brief.py` is part of the agent's self-evolution authority — when a new check would catch a class of drift slipping through, add it in the same run as the brief.

If `tools/check_brief.py` itself fails to start (`SystemExit 2`, import error, missing taxonomy), proceed to Phase 6 anyway and log the script-level error in § 8 — never let tooling block the brief. The CRITICAL anti-crash header at the top of the daily prompt always wins.
