---
name: changelog-hygiene
description: Version history lives only in prompts/CHANGELOG.md — never annotate rules with vN.M
type: project
---

# Changelog hygiene — no version annotations outside prompts/CHANGELOG.md

- **Rule (operator-set, 2026-07-02):** `prompts/CHANGELOG.md` is the ONLY place that records when a behaviour changed. The two master-prompt banners (`> **Prompt version:** vN.M`) are the only version markers allowed anywhere else. Do NOT write "(v2.53)", "NEW in v2.66", "removed in v2.64" or similar into prompts, agent definitions, CLAUDE.md, docs, config comments, or tool output strings — put the history in the CHANGELOG entry and state the rule timelessly in the file itself.
- **Why:** history annotations are noise every agent re-reads on every run, they go stale (several were pointing at wrong section numbers and superseded caps), and they duplicate the changelog's job.
- When editing a rule, keep any operational rationale inline (e.g. dated incident references like the 2026-05-15 fabrication trace) — only the version framing is banned.
- `tools/check_run.py` `prompt-version` check cross-checks the run record's `prompt_version` against the CHANGELOG's newest `## N.M —` heading: FAIL when the record under check is uncommitted (pre-commit gate), WARN when it's already committed (changelog moved on after publication).
