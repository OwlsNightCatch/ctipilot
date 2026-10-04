# Remediation brief, run 2026-09-30T0639Z-audit, iteration 1 findings

You apply the verifier's findings for ONE slice of this audit run's changed entries. Other workers handle other slices in parallel, so touch ONLY the entry files listed in your slice's scope file (`work/2026-09-30T0639Z-audit/scope.iter1.s<K>.txt`). Do not edit any other file except your own log. Never commit, push, or run git commands that change the index or working tree.

## Inputs

- Findings: `work/2026-09-30T0639Z-audit/verification.iter1.s<K>.findings.yaml` (and the report `.md` beside it for detail).
- Repo rules: `CLAUDE.md`, `prompts/cti-run.md` Phase 4 (§ Updating an existing entry, § The actionability contract), `docs/pipeline.md` § Entry lifecycle.
- The KEV feed as fetched this run: `work/2026-09-30T0639Z-audit/kev.json`.
- Read pages with `python3 tools/fetch_source.py extract <URL>` (PDF: `pdf <URL>`). Avoid WebFetch for bodies.

## How to decide each finding

1. Check it yourself against the cited page before acting. The verifier is usually right, but a finding can be wrong; decline it with the passage that refutes it.
2. Truth findings (F3, F4, F5, F13, F14, F9 source conflicts): fix the claim where it stands, in the frontmatter, the main analysis or an earlier section alike. Narrow it to what the source says, re-cite it to a page that says it, or remove it (and whatever depends on it). An unsourced actor link, exploitation claim, version or number is removed or narrowed, never kept on trust. A source conflict is stated as a conflict.
3. Editorial (F5 citation gaps, F6, F7, F8, F11, F12, F16, F18): apply when clearly right and cheap. Remove leftover tables or passages about other findings, pipeline narration in reader text ("this entry", "this run", carve-out, Admiralty letters, registry keys, "tracked here"), attacker file names, domains or other indicators, and US federal KEV deadlines used as a reason to act. For F16/F7 priority findings, re-grade against the `high` bar and the incident floor in `prompts/cti-run.md` Phase 4. For a routine incident with no vector, you may trim the body, but keep the facts cited.
4. Never invent. Every sentence you add carries an inline citation `([Publisher, YYYY-MM-DD](url))` to a page you fetched, and the source must be in `sources[]` (add it with `add_source`).
5. Text you write: English, no em dashes, no semicolons in new sentences where a full stop works, plain wording.

## Changelog mechanics (strict)

Each of your entries already carries exactly ONE `updates[]` record with `run_id: 2026-09-30T0639Z-audit`. Never add a second record for this run. Instead:

```python
import sys; sys.path.insert(0, "/tmp/claude-0/-home-user-ctipilot/0a7eecc7-5a32-5a0c-b51d-f1dddc8b40df/scratchpad")
from fixlib import *          # read, write (validates and restores the file on error), sub, wsub (whitespace-flexible),
                              # set_scalar, replace_block, add_source, drop_source, replace_source, promote_source,
                              # set_cve_status, set_body_main, set_section, amend_record, make_public, kev_cite, KEV_URL, fold
t = read(eid)                 # eid like "2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x"
t = wsub(t, "old text", "new text")
t = amend_record(t, ["body", "cves"], "One plain sentence saying what else changed.")   # adds fields + summary sentence
write(eid, t)
```

- `amend_record(text, extra_fields, extra_summary)` extends this run's record. Name every frontmatter key you change (`body` for any change to the main analysis or an earlier section).
- If this run's record is `internal: true` and your change alters a claim a reader sees in the body (more than removing narration, indicators, inline ATT&CK ids or re-pointing a citation), convert it with `make_public(text, section)`, where `section` is one short inline-cited paragraph stating the reader-facing correction, never record-keeping narration ("the entry previously said" is fine once, "this entry" is not).
- If this run's record already has a section (non-internal), edit that section with `set_section(text, at, new_body)` when the correction belongs there, rather than adding a new one. The record's `at` is on its `  - at:` line.
- Do not touch `updated_at`, `discovered_at`, `run_id`, or earlier records' YAML. Earlier `## <Type> — <at>` sections may be corrected in place (declare `body`).
- Do not add CVE ids that are not already in `state/cves_seen.json` and do not edit `entities/registry.yaml`: list any such need in your log instead. Removing an entity key from an entry is fine.

## Finish

1. Run `python3 tools/check_run.py 2026-09-30T0639Z-audit --pre-verify` and fix every FAIL or WARN that names one of YOUR entries (ignore run-record, sub_agents, verification-block lines and the Die Linke aggregator-only warning).
2. Write `work/2026-09-30T0639Z-audit/remediation.iter1.s<K>.yaml`: one item per finding: `code`, `entry`, `finding` (short), `remediation_applied` (what you changed, or `declined: <reason with passage>`), `verify_in_this_iteration` (one question for the next verifier). Plus `needs_main_agent:` for anything outside your authority (registry, cves_seen, other entries).
3. Return a short summary: counts applied / declined, entries touched, anything needing the main agent.
