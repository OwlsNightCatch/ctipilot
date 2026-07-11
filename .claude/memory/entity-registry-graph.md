---
name: Entity registry graph conventions (v3.16 → v3.20)
description: merged_into tombstones, typed relations[] edges (v3.20), the /graph/ surface, and the naming convention from the 2026-07-09 registry overhaul
type: project
---

# Typed relationships + threat graph (v3.20, 2026-07-11)

Operator-directed rework (branch `claude/cti-entity-relationships-graph-qb9j9j`) — supersedes the v3.16 `related: []` model below:

- **`relations[]` replaced `related` with NO backward compatibility** — `check_run.py` FAILs a leftover `related` key. Edge shape: `{to, type, source, note}`; 10-type vocabulary with direction + endpoint constraints in `content_model.RELATION_TYPES` (normative prose: `docs/pipeline.md` § Relationships). `source` (REQUIRED) = the entry id whose cited reporting establishes the edge — this is what makes every curated edge evidence-bound and dated. Symmetric types (`collaborates-with`, `overlaps-with`, `related-to`) are stored ONCE, on either endpoint; the mirror declaration is a duplicate-edge FAIL. Directed types live on the SUBJECT record — `attributed-to` sits on the campaign/incident/malware/tool pointing AT the actor, so most legacy actor→incident edges flipped in migration.
- **Semantics guardrails**: relate only what a cited source states; `overlaps-with` is the honest middle ground and is never upgraded to `attributed-to`/`successor-of` beyond the claim; a suspected same-entity is an alias or a `merged_into` tombstone, never a relation. New corroboration ≠ new edge; a materially evolved relationship updates the edge's `type`/`source`/`note` in place (relations are registry state, not immutable entries). Tombstoning moves the loser's edges to the canonical record.
- **Derived edges never stored**: entry co-occurrence, entity↔CVE, entity↔technique are computed by `site/build.py` each build with supporting entry ids. Curated vs derived stay visually distinct everywhere.
- **Analyst surfaces**: `/graph/` (canvas force layout over entities + connected CVEs + technique layer; search, filters, detail panel with per-edge provenance, shortest-path tracing, `?focus=`/`?to=` deep links; `assets/js/graph.js` + `data/graph.json`) and the entity pages' grouped "Relationships" section (typed rows with source-entry links) above the derived "Co-occurring entities" list.
- **Research agents** may return `relation_suggestions: [{subject, object, basis}]` for source-stated connections; the main agent maps them onto the vocabulary and owns the registry write.
- **`check_run.py` advisory**: `registry-relations` WARN when an edge's source entry neither keys nor names an endpoint (token-based name matching; short all-caps acronyms like "INC" match case-sensitively).
- Migration note: 81 untyped edges → 71 typed canonical-direction edges; 2 dropped (`actor:oceanlotus`→`tool:zichatbot`, `actor:scarcruft`→`tool:birdcall`) because no in-store entry supports them (pre-v3 coverage only) — re-add with a source when an entry covers them.

# Entity registry graph (v3.16, 2026-07-09 — historical; `related` since retired)

Operator-directed overhaul of `entities/registry.yaml` (interactive session, branch `claude/cti-pilot-graph-review-tu722w`). What every future session must know:

- **Naming convention is enforced editorially**: `name` = concise canonical entity name ONLY (never the reporting vendor, never a headline sentence, never truncated); every alternate public name goes in `aliases`. Aliases are load-bearing twice: dedup matching AND `site/build.py` phrase-matching that attaches entries to entity pages (an entity with empty aliases misses most of its story timeline).
- **`merged_into: <canonical-key>` tombstones** are the ONLY way to merge a duplicate whose key is referenced by published entries (keys permanent, entries immutable). No chains; tombstones exempt from alias-collision check; consumers resolve via `content_model.resolve_entity_key`. New entries must never reference a tombstone key. Orphan duplicates (zero entry references) are deleted outright, names folded into the canonical record's aliases.
- **`related: []`** = curated, evidence-bound graph edges (actor↔campaign↔tool↔incident). Rendered symmetrically with a `linked` badge; survive the co-occurrence top-8 cap. Only add edges a cited source states.
- **Type fixes**: an orphan key with the wrong type prefix may be renamed (it IS a key change — allowed only because nothing references it); a referenced mistyped key gets a tombstone pointing at a new correctly-typed record (8 were done this way, e.g. `campaign:eu-cyber-resilience-act` → `policy:eu-cyber-resilience-act`).
- **Why orphans exist at scale**: 227/376 registry keys had zero explicit entry references (entries under-link `entities:`); phrase matching papers over this at render time, but composers should keep linking explicitly — explicit keys are what dedup sees.
- `vietnam-nexus` was added to `site/taxonomy.yaml` `nexus:` (OceanLotus).
- Normative contract: `docs/pipeline.md` § Entity registry; prompt guidance: `prompts/cti-run.md` § Entity linking + Phase 5 registry section (v3.16).
