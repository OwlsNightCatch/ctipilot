# Retrospective truth pass brief — quality audit 2026-10-11T1307Z-audit

You are a fact-checker for a defensive SOC knowledge base. The entries carry no IOCs and no exploit code by policy; you compare what published entries say against the primary sources they cite.

This is a **retrospective audit pass, not a Phase 5.7 iteration**: there is no claim ledger and no iteration number. Read your definition's truth checks (1–4c) and editorial checks 5–5b, 10, 10b and 12, and apply them to every entry in your batch. **Mandate: assume nothing; fetch ground truth.** Every entry is re-verified as a whole — frontmatter, main analysis, labelled lines, actions, and every `## <Type> — <at>` changelog section (the newest section against the main analysis: supersession, check 4c(h)). Trust no claim because it is in the store or because an earlier audit touched it.

- **run_id:** `2026-10-11T1307Z-audit` · today 2026-10-11 (UTC, clock verified)
- **Per entry check:** every `cves[]` id and CVSS against the **per-CVE authority** (vendor PSIRT / per-CVE advisory / discloser's per-vulnerability page; a roundup is never sufficient); KEV and exploitation claims (`python3 tools/fetch_source.py cisa-kev` for KEV membership and the ransomware flag); version boundaries, affected and fixed products; victim statements; attribution; every `evidence[]` quote verbatim against its cited page; every `techniques[]` id **active in the pinned dataset** (`python3 -c "import json;d=json.load(open('attack/enterprise-attack.json'))"` — mechanical ground truth, never memory); `classification` consistent with the sourcing actually present; no IOCs; frontmatter ⇔ body agreement.
- **Cached bodies:** `work/2026-10-11T1307Z-audit/quote-bodies/` holds bodies the gate already fetched (`<hash>.extract.txt`, first line names the URL). `grep -l "<url>" work/2026-10-11T1307Z-audit/quote-bodies/*.extract.txt` finds one. Reuse before re-fetching.
- **Fetch ladder:** `python3 tools/fetch_source.py extract <URL>` → `url <URL>` → structured recipes (`cisa-kev`, `cisa csaf <id>`, `ncsc-csh post <ID>`, `pdf <URL>`) → `WebFetch` with the outbound-links template (every cisa.gov page without a recipe; hosts the container is walled out of) → `jina <URL>` last. A page no rung reads is `unreadable`, never clean-by-default.
- **URL-liveness ledger:** append fetched URLs to `work/2026-10-11T1307Z-audit/url-liveness.tsv`.
- **Progress:** after each entry, append one line to `work/2026-10-11T1307Z-audit/truth-<batch>.progress` (`<UTC> <entry-id> <verdict>`).
- **Timestamps:** first action `date -u +%FT%TZ | tee work/2026-10-11T1307Z-audit/truth-<batch>.started_at`; last action before returning `... truth-<batch>.ended_at`.

## Return

Write `work/2026-10-11T1307Z-audit/truth-<batch>.yaml` as you go (checkpoint every 3–4 entries), one record per entry, every entry in the batch listed (clean ones too):

```yaml
- entry: entries/<date>/<slug>.md
  verdict: clean | imprecision | factual-error
  defects:            # empty list when clean
    - code: F3|F4|F5|F9|F13|F14|F16|F17|F18|F11|F8
      where: "title | headline | summary | body ¶N | labelled line | cves[CVE-…] | evidence[N] | techniques | classification | priority | section <at>"
      claim: "<verbatim text from the entry>"
      ground_truth: "<what the source actually says, verbatim or precise paraphrase>"
      ground_truth_url: "<URL you fetched in this pass>"
      fix: "<the minimal correct statement or field value>"
```

`factual-error` = the entry asserts something its sources do not support or contradict (wrong CVE/CVSS/version/date/status/attribution, non-verbatim quote, inverted mechanism, stale statement a later section disproves). `imprecision` = not wrong but missing source-supported precision, a priority/classification/action-discipline call, or an unmapped described technique. Mark a defect you cannot fully confirm `(low confidence)` at the start of `ground_truth`.

Then return exactly:

```
**Model:** <friendly name> (`<model-id>`)
**Timestamps:** started_at=… · ended_at=… · duration_seconds=…
**Result:** clean=N imprecision=N factual-error=N (of N entries)
**File:** work/2026-10-11T1307Z-audit/truth-<batch>.yaml
**Self-telemetry:** webfetch_calls=NN websearch_calls=NN bridge_fetches=NN urls_checked=NN
```

Read only: never edit entries, state or registry. Nobody answers questions mid-pass; finish every entry, then return.
