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
- `aliases` carries every public alias; collisions with any other entity's
  key, name, or aliases FAIL `tools/check_run.py`.
- `summary` is a 1–3 sentence sourced definition. Attribution claims stay
  claim-attributed ("GTIG attributes…"), same as everywhere else.
- CVEs are **not** registry entities (`state/cves_seen.json` + per-entry
  `cves[]` carry the CVE model). Regions / sectors / theme tags live in
  `site/taxonomy.yaml`.
- The main agent adds new entities in the same commit as the entries that
  first reference them. Never rename a key; add aliases instead.
