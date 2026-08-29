---
name: product-entities
description: "affected_products[] resolves to product: entities — derived at render, curated by alias, never stored on an entry; products never phrase-match prose"
metadata:
  type: project
---

# Products are entities (2026-08-29, prompt v4.6)

Operator directive: "I want to see all vulnerabilities and incidents for a
certain software, also in the graph. E.g. everything for SharePoint on a
similar page as the actors and tools and incidents."

**The entry is never rewritten.** `affected_products[]` stays release-precise
("Microsoft SharePoint Server 2019") and the product KEY is resolved at
render time by `content_model.product_key()`:

1. the registry's `product:` records — `name` + `aliases` are the curated
   merge surface (six SharePoint spellings fold onto
   `product:microsoft-sharepoint`);
2. a mechanical fallback — strip a trailing 4-digit release year, dotted
   version, `vN`/`rN` or edition word, then slugify.

**Bare integers are never stripped.** The 4-digit rule exists because
"Microsoft 365" and "Dynamics 365" are names, not versions; an earlier
`\d+$` rule folded "Microsoft 365" to "Microsoft" and would have attached a
vendor node to a third of the store.

**Products never phrase-match prose.** `build_entities` skips
`type: product` when building the phrase-match specs and attaches them from
`affected_products[]` only. With prose matching ON, "PHP" pulled 54 entries
and "WordPress" 47, products took 2348 of 2603 co-occurrence edges, and the
actor/campaign graph drowned. An entry saying "a PHP deserialization bug" is
not coverage OF PHP. Precision over recall here; recall comes from the
pipeline populating the field, which the prompts already require.

## Consequences worth remembering

- **Merging two products is an alias edit, not a migration.** Add the loser's
  spelling to the winner's `aliases` (or `merged_into`) and re-run
  `tools/sync_products.py`; every entry follows because none stored the key.
- `tools/sync_products.py` owns a marked block at the END of
  `entities/registry.yaml` and rewrites only that block — a full
  `dump_yaml_subset` re-dump reflows all 1692 records (392KB to 409KB) and is
  never the right move. It reads existing records back, so curated fields
  survive; `SEED_ALIASES` in the tool is only a first-run seed.
- `summary` is OPTIONAL on `product` records (`validate_registry` exempts the
  type): a derived index node is not an analytical claim. 481 fabricated
  summaries would have been the alternative.
- `product` is absent from `stix_model.ENTITY_SDO_TYPES` on purpose — the
  faithful shape is the `software` SCO, which carries none of the SDO
  properties the export writes. The relation writer now `.get()`s both
  endpoint types and skips unmapped ones instead of `KeyError`.
- Vendor-only strings ("Microsoft", "Linux") are in `PRODUCT_NON_ENTITIES`
  and never become entities.
- Product slugs are capped at 80 chars (`_cap_slug`) — three entries put a
  whole clause in `affected_products[]` and blew the key regex.
- Relations: `affects` (campaign/incident/malware/tool/trend → product) and
  `exploits` gained `product` as an object. Nothing points OUT of a product
  except `documented-in` / `related-to` — it is the thing attacked.
- `check_run.py --all` gains `product-entities` (WARN, never FAIL: an
  unregistered spelling is one `sync_products.py` away).

Related: [[entity-registry-graph]], [[design-system]], [[customization-framework]].
