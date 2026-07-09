---
name: Entity registry graph conventions (v3.16)
description: merged_into tombstones, related edges, and the naming convention introduced by the 2026-07-09 registry overhaul
type: project
---

# Entity registry graph (v3.16, 2026-07-09)

Operator-directed overhaul of `entities/registry.yaml` (interactive session, branch `claude/cti-pilot-graph-review-tu722w`). What every future session must know:

- **Naming convention is enforced editorially**: `name` = concise canonical entity name ONLY (never the reporting vendor, never a headline sentence, never truncated); every alternate public name goes in `aliases`. Aliases are load-bearing twice: dedup matching AND `site/build.py` phrase-matching that attaches entries to entity pages (an entity with empty aliases misses most of its story timeline).
- **`merged_into: <canonical-key>` tombstones** are the ONLY way to merge a duplicate whose key is referenced by published entries (keys permanent, entries immutable). No chains; tombstones exempt from alias-collision check; consumers resolve via `content_model.resolve_entity_key`. New entries must never reference a tombstone key. Orphan duplicates (zero entry references) are deleted outright, names folded into the canonical record's aliases.
- **`related: []`** = curated, evidence-bound graph edges (actor↔campaign↔tool↔incident). Rendered symmetrically with a `linked` badge; survive the co-occurrence top-8 cap. Only add edges a cited source states.
- **Type fixes**: an orphan key with the wrong type prefix may be renamed (it IS a key change — allowed only because nothing references it); a referenced mistyped key gets a tombstone pointing at a new correctly-typed record (8 were done this way, e.g. `campaign:eu-cyber-resilience-act` → `policy:eu-cyber-resilience-act`).
- **Why orphans exist at scale**: 227/376 registry keys had zero explicit entry references (entries under-link `entities:`); phrase matching papers over this at render time, but composers should keep linking explicitly — explicit keys are what dedup sees.
- `vietnam-nexus` was added to `site/taxonomy.yaml` `nexus:` (OceanLotus).
- Normative contract: `docs/pipeline.md` § Entity registry; prompt guidance: `prompts/cti-run.md` § Entity linking + Phase 5 registry section (v3.16).
