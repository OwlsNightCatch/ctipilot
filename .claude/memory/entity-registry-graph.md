---
name: Entity registry graph conventions
description: Typed relations[] edges, merged_into tombstones, naming/alias discipline, and the /graph/ surface
type: project
---

# Entity registry — graph conventions

(Normative: docs/pipeline.md § Entity registry + § Relationships; vocabulary: `content_model.RELATION_TYPES`.)

- Typed edges `{to, type, source, note}` replaced the untyped `related` list (retired; `check_run.py` FAILs it). `source` (required) = the entry id whose cited reporting establishes the edge — evidence-bound and dated. Symmetric types stored ONCE (mirror declaration = duplicate-edge FAIL); directed types live on the SUBJECT (`attributed-to` sits on the campaign/incident pointing AT the actor).
- Relate only what a source states: an overlap claim is `overlaps-with`, never upgraded; a suspected same-entity is an alias or a tombstone, not a relation. New corroboration ≠ new edge; a materially evolved relationship updates the edge's `type`/`source`/`note` in place (relations are registry state, not entries). Co-occurrence, entity↔CVE and entity↔technique edges are derived at render time, never stored.
- `name` = concise canonical entity name only (never the reporting vendor, never a headline); aliases are load-bearing twice — dedup matching AND the build's phrase-matching that attaches entries to entity pages. Composers still link `entities:` explicitly — explicit keys are what dedup sees.
- Duplicates: `merged_into: <canonical-key>` tombstone (no chains; edges move to the canonical record); never reference a tombstone in new entries. Orphan duplicates (zero references) may be deleted outright, names folded into aliases; a referenced mistyped key gets a tombstone pointing at a new correctly-typed record.
- Research agents may return `relation_suggestions: [{subject, object, basis}]`; the main agent maps onto the vocabulary and owns the write. Analyst surface: `/graph/` (per-edge provenance, `?focus=`/`?to=`).
