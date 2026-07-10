---
name: MITRE ATT&CK layer (v3.17)
description: The pinned ATT&CK dataset, derived entity/CVE TTP mappings, the /attack/ overlap matrix, and the metadata-not-prose composition rule
type: project
---

# The MITRE ATT&CK layer — v3.17 (2026-07-09, operator-directed)

## Architecture (normative: docs/pipeline.md § The ATT&CK layer; contract: attack/README.md)

- **Pin:** `attack/enterprise-attack.json` — compact extraction of ONE official ATT&CK Enterprise release (v19.1 at introduction) from `mitre-attack/attack-stix-data` (index.json is the version catalog). Carries id → name, tactics, first-paragraph **definition**, sub-technique parentage, platforms, lifecycle. **Generated file — only `tools/attack_data.py` writes it** (`--check` / `--update [--version X.Y]` / `--selftest` / `--info`). Weekly runs `--check` and must record the result; update = rewrite + selftest + green build + commit with the printed delta.
- **Revoked ids are kept + forwarded** (`revoked_by` → `content_model.resolve_technique_id`) — the ATT&CK analogue of registry `merged_into` tombstones, needed because immutable entries cite old ids forever.
- **Derivation, never assertion:** entity/CVE → technique = union over referencing entries of `content_model.entry_technique_ids` (frontmatter `techniques[]` ∪ dataset-known in-prose T-ids). The 888-entry pre-v3.17 store carries mappings in prose only — prose extraction is a permanent code path, not a migration shim (entries are immutable).
- **Surfaces:** entity/CVE pages get an ATT&CK section (grouped by tactic in matrix order, definitions, evidence links) + `entities/<key>/attack-layer.json` (Navigator layer format 4.5); `/attack/` = full matrix heat-shaded by store coverage + per-technique definitions/evidence directory + client-side multi-entity overlap (`assets/js/attack.js` + `data/attack.json`, modes union / overlap≥2 / common-to-all, `?sel=` shareable, layer export). `techniques[]` also rides `data/briefbook.json` + `data/alerts.json` records and the search index.
- **Gate:** `check_run.py` — `attack-dataset` FAILs a missing/invariant-broken pin; `attack-mapping` WARNs on unknown/revoked/deprecated `techniques[]` ids and (run scope only) prose-mapped ids missing from the frontmatter.

## Why-lines

- **Never hardcode tactic/technique tables** — v19 renamed Defense Evasion into Stealth + Defense Impairment and added TA0112; the matrix must always render from the pin. This is the whole reason the dataset is versioned in-repo.
- Composition rule inversion (v3.17): the old "ATT&CK woven, never listed" rule pushed ids INTO prose while `techniques[]` stayed empty on 888/888 entries — the machine layer never materialized. New rule: metadata complete + prose readable without T-numbers (inline only where essential). The check_run WARN ("prose ids missing from techniques[]") is the enforcement nudge for new runs.
- Prose T-id extraction filters through the pin (`m in attack_techniques`) to kill T-shaped false positives; frontmatter ids are kept even when unknown to the pin (may be newer than the pin — WARN, never silently dropped).
- Site build degrades gracefully without the dataset (features render to nothing); the mechanical gate is what makes the pin mandatory. `site/test_build.py` § "ATT&CK mapping" self-skips when the pin is absent.

## v3.2 addition (2026-07-10)

- **Entry detail pages** now render a first-class `ATT&CK mapping` section (`render_entry_attack_section`, anchor `#attack-mapping`): techniques grouped by tactic, resolved names + pinned definitions, overlap-matrix + MITRE links; the pivot-rail chips show `Tid + name` and jump to it. Derived via `entry_technique_ids` (frontmatter ∪ prose), so legacy prose-only entries get the section too.

## v3.18 addition (2026-07-10) — always mapped

- **Empty `techniques[]` on `threat`/`incident`/`vulnerability` is a check_run FAIL from prompt v3.18** (WARN on `research`/`annual-report`; `policy`/`synthesis`/`outlook` exempt). Version-gated on the run record's `prompt_version` — pre-3.18 records keep WARN so `--all` stays green on immutable history; `--all` gains a `store-ratings` sweep that re-enforces for every v3.18+ run forever. Rationale: behavior kinds always have a mappable access/exploitation vector (RCE→T1190, phishing→T1566, LPE→T1068); completeness of *evidence-supported* mappings, never invention.
