# Duplicate-consolidation verification brief — quality audit 2026-10-11T1307Z-audit

You are a fact-checker for a defensive SOC knowledge base (no IOCs, no exploit code by policy). One finding must have exactly one entry. The groups below are sets of entries, mostly migrated from the May–July 2026 v2 daily briefs before verification existed, that share a CVE: same-day twins (a brief item and a deep dive), legacy "UPDATE (originally covered …)" entries, or genuinely distinct findings that merely share a CVE. The audit will fold duplicates into one survivor and link distinct findings. Your pass supplies the verified ground truth that the survivor's corrected text will stand on.

Everything in T-brief.md (`work/2026-10-11T1307Z-audit/T-brief.md`) applies: the per-entry truth checks, the fetch ladder, cached bodies, ledger, no IOCs, read-only. Your batch id is given in the spawn message; progress, timestamp and return files are `truth-<batch>.*`. Treat every legacy claim as unverified until you read it on a fetched primary (vendor PSIRT/advisory, CERT, discloser, victim); evidence items quoting "ctipilot v2 brief (migrated)" are the pipeline quoting itself.

## Per group, decide and return

Append to each entry's YAML record (the T-brief shape) these keys:

```yaml
  group: <group id from the spawn message>
  role: survivor | duplicate | distinct
  duplicate_of: <survivor entry id, when role is duplicate>
  unique_material:   # on duplicates only: verified facts the survivor lacks, each with the URL you read it on
    - fact: "..."
      url: "..."
```

And one record per group at the end of the file:

```yaml
- group: <id>
  decision: fold | link | mixed
  survivor: <entry id>
  current_state:      # the verified current truth for the group's finding, as of today, each with its source URL
    cves: [{id, cvss, cvss_source_url, affected, fixed, fixed_source_url, exploited: true|false, exploited_source_url, kev: true|false}]
    key_facts: [{fact, url}]
  wrong_in_survivor: [{claim, ground_truth, url}]
  notes: "why fold or link"
```

Survivor choice: prefer the entry whose text is closest to the verified truth and that carries the most source-supported depth (usually the deep dive or the later entry with changelog records); say why in `notes`. A group is `fold` when its entries report one finding (same flaw / same disclosure and its later developments); `link` when they are distinct findings that share a CVE (different campaign, actor, victim, or a separate flaw chained with it); `mixed` when some members fold and others link (name which).
