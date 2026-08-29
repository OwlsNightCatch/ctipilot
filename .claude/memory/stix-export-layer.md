---
name: stix-export-layer
description: "STIX 2.1 derived layer under /stix/ — id-stability rules, relation collapse, canonical ATT&CK ids, what would silently break consumers"
metadata: 
  node_type: memory
  type: project
  originSessionId: 38129f13-4433-46b8-9c2f-69426344a9f9
  modified: 2026-08-29T09:50:01.132Z
---

# STIX 2.1 export layer (added 2026-08-29, operator-directed)

`site/stix_model.py` compiles the store into STIX 2.1 bundles under
`/stix/` on every build (`bundle.json` full, `recent.json` = briefbook
window reference-closed poll target, `entities.json` core graph,
`sector-<slug>.json` per RSS slice, `extension-schema.json`). Operator
decisions: derived layer only (markdown store stays source of truth),
**bundle URLs only — NO TAXII surface** (GitHub Pages can't serve the
TAXII 2.1 media type / X-TAXII headers / query filtering, all MUSTs),
actor → `intrusion-set`, pure STIX (property extension, no `x_opencti_*`).

Non-obvious invariants a later session could silently break:

- **Id stability is the contract.** Every id is uuid5 over the permanent
  store key under a namespace from the CANONICAL branding `site.url`
  (never the `SITE_URL` env override) or `stix.id_namespace`. Changing
  the namespace, a seed string, or `site.url` re-mints every object id
  for downstream consumers. `test_build.py` pins literal uuid vectors so
  an accidental change fails the gate — don't "fix" those vectors
  without operator sign-off.
- **Never put mutable text (titles, summaries) in a uuid5 seed.**
- **Relation collapse table** `SPEC_REL_MAP` in stix_model.py: only
  uses / attributed-to (incl. incident, malware→authored-by) /
  variant-of(malware) keep their names; everything else → `related-to`
  with `original_type` in the extension. OpenCTI hard-rejects unknown
  relationship types between typed pairs — don't re-emit custom strings.
- **`report.object_refs` / `grouping.object_refs` are required
  non-empty** — bare objects fall back to `[publisher identity id]`.
- STIX timestamps need ms precision — `stix_ts()` appends `.000`.
- The ATT&CK pin carries `stix_id` per technique since the 2026-08-29
  regeneration (tools/attack_data.py extracts it; optional field, no
  schema bump — bumping would fail the gate on an old pin). All exported
  attack-patterns use MITRE's canonical ids; the uuid5 fallback exists
  only for a pin written without the field.
- Report `modified` follows the latest changelog record of ANY type —
  deliberately broader than [[entry-lifecycle-v4]]'s updated_at float
  rule (STIX semantics: any change bumps modified).
- stix2-validator is dev-only, never CI (build stays stdlib); pypi is
  blocked in the sandbox — validation there is the manual lint pattern.
