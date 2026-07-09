# entities/

`registry.yaml` is the global entity registry: the single controlled list of
named things the pipeline tracks — threat actors, campaigns, malware
families, offensive tools, named incidents, and recurring threat reports.

Its purpose is **canonical linkage**: every entry in `entries/` references
entities by registry key (e.g. `actor:shinyhunters`), research agents read
the registry (keys + aliases) before naming anything, and the dedup gate
matches candidate items against keys *and aliases* — so "UNC6240" and
"ShinyHunters" can never become two separately-tracked things.

Contract (normative version in [`docs/pipeline.md`](../docs/pipeline.md)):

- `key` = `<type>:<kebab-slug>`, `type ∈ {actor, campaign, malware, tool,
  incident, report, trend, policy}`. Keys are permanent — entries
  reference them.
- `name` is the concise canonical entity name only — never the reporting
  vendor, never a headline sentence. Every other public name goes in
  `aliases`; collisions with any other entity's key, name, or aliases FAIL
  `tools/check_run.py`.
- `summary` is a 1–3 sentence sourced definition. Attribution claims stay
  claim-attributed ("GTIG attributes…"), same as everywhere else.
- `related` (optional) carries curated registry keys linking the entity
  into the threat graph (actor ↔ campaign ↔ tool ↔ incident); targets must
  be existing canonical keys.
- `merged_into` (optional) marks a duplicate record as a tombstone pointing
  at its canonical entity. Tombstoned keys stay resolvable (published
  entries reference them) but new entries must use the canonical key.
  Duplicates referenced by zero entries are deleted outright, their names
  folded into the canonical record's `aliases`.
- CVEs are **not** registry entities (`state/cves_seen.json` + per-entry
  `cves[]` carry the CVE model). Regions / sectors / theme tags live in
  `site/taxonomy.yaml`.
- The main agent adds new entities in the same commit as the entries that
  first reference them. Never rename a key; add aliases instead — or, for
  a true duplicate, tombstone it with `merged_into`.
