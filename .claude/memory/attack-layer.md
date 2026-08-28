---
name: MITRE ATT&CK layer
description: The pinned dataset, derived TTP surfaces, and the mapping rules that are not obvious from CLAUDE.md
type: project
---

# ATT&CK layer — the non-obvious parts

(Normative: docs/pipeline.md § The ATT&CK layer; contract: attack/README.md. CLAUDE.md carries the composition rule.)

- Pin: `attack/enterprise-attack.json`, written ONLY by `tools/attack_data.py`. The quality audit runs `--check` every fire and records the result. **Never hardcode tactic/technique tables** — v19 renamed Defense Evasion into Stealth + Defense Impairment.
- Revoked ids are kept + forwarded (`revoked_by` → `content_model.resolve_technique_id`) — the ATT&CK analogue of registry tombstones; the store is never rewritten when the pin moves.
- Entity/CVE TTP profiles, `/attack/` matrix and Navigator layers all derive from `entry_technique_ids` (frontmatter ∪ dataset-known prose ids) — prose extraction is a permanent code path for the pre-v3.17 tail, never a migration shim. An audit may lift a single legacy entry via an `improvement` record, never the store.
- Empty `techniques[]` on `threat`/`incident`/`vulnerability` FAILs (v3.18+, version-gated; `research`/`annual-report` WARN) — but the completeness floor is EVIDENCE: when no source states the access vector, do not map one; if the honest mapping would be empty, the entry is describing too little to publish.
- Site build degrades gracefully without the pin; the mechanical gate is what makes it mandatory.
