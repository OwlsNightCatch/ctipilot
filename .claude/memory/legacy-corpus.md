---
name: legacy-corpus
description: Half the store (478 entries, May to July 2026) came from the v2 briefs unverified; how to treat it, the repair queue, and the duplicate-folding mechanism (2026-09-30)
type: project
---

# The legacy corpus (v2-brief migration)

**Fact (2026-09-30):** 478 of 966 entries carry `migrated_from: briefs/...`. They were written before claim verification, inline citations, the entry lifecycle and the verifier loop existed, and the weekly audits only re-verify their trailing window, so before 2026-09-30 only 3 had ever received a record from an audit.

**What an honest look found** (the 2026-09-30 audit correction run, first pass outside the window): claims the cited source does not make, not just stale ones. ABW cited for an APT28/APT29/UNC1151 attribution it never published; the Ivanti EPMM cluster marking five CVEs exploited and KEV-listed where Ivanti reported one, framing two separate flaws as an exploited chain, and moving four European public bodies into the wrong exploitation wave; Eurail regulator reviews that never opened; Dragos statistics absent from the report; invented distribution kernel package versions. Evidence items quoting "ctipilot v2 brief (migrated)" are the pipeline quoting itself.

**Why:** a reader or triage agent cannot tell a legacy entry from a verified one, so a hallucinated attribution or exploitation flag in the old half poisons lookups by CVE or actor.

**How to apply:**
- Treat any legacy entry as unverified until `state/legacy_review.json` marks it reviewed. Never build on its claims (references, registry relations, dedup "already covered") without checking the primary.
- The audit works the queue: `python3 tools/legacy_review.py --next 20`, re-verify, correct or rewrite from sources, `--done <run-id> <ids>`.
- Touching a legacy entry pulls it under current gates: it needs a classification and a non-empty `techniques[]` (kind permitting) in the same record.
- Duplicates (legacy "UPDATE (originally covered ...)" entries, brief/deep-dive twins) are folded with `tools/fold_entries.py` after the survivor's record is written; `merged_from` may be a list; deletion is only legal that way. 24 unfolded UPDATE entries and about 19 same-finding twin groups remained after the Ivanti fold.
