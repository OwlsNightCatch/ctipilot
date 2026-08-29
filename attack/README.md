# `attack/` — the pinned MITRE ATT&CK dataset

`enterprise-attack.json` is the single, versioned MITRE ATT&CK® Enterprise
dataset every consumer in this repo renders and validates against. It is a
compact extraction (technique id → name, tactics, first-paragraph
definition, sub-technique parentage, platforms, lifecycle flags, upstream
STIX id) from the
official STIX 2.1 release bundles published by MITRE at
[mitre-attack/attack-stix-data](https://github.com/mitre-attack/attack-stix-data).
`tools/attack_data.py` is the only writer; treat the JSON as generated —
never hand-edit it.

## Why the dataset is pinned and committed

ATT&CK technique mappings are only meaningful against a specific ATT&CK
release: ids get revoked and merged, tactics are added and renamed (v19
replaced *Defense Evasion* with *Stealth* + *Defense Impairment*, adding
TA0112), and definitions evolve. Committing the extraction gives every
consumer — `site/build.py`, `tools/check_run.py`, the research and
verification agents — the identical, diff-reviewable release, offline, on
every fresh routine container. The site footer of `/attack/`, the entity
TTP sections and the exported Navigator layers all carry the pinned
`attack_version` so downstream users know exactly which matrix they are
looking at.

## Lifecycle semantics (mirror of the registry's tombstones)

Revoked and deprecated techniques are **kept**, flagged. The store is not
rewritten when the pin moves, so a T-id cited in an old entry must still
resolve after MITRE revokes it. `revoked_by` carries the surviving id; consumers resolve it
forward via `content_model.resolve_technique_id` — exactly how
`merged_into` registry tombstones are resolved. New entries reference only
active ids (`tools/check_run.py` WARNs on revoked/deprecated ids with the
forward pointer).

## Updating to a new ATT&CK release

```bash
python3 tools/attack_data.py --check          # is there a new release? (exit 1 = yes)
python3 tools/attack_data.py --update         # rewrite from the latest release
python3 tools/attack_data.py --update --version 19.0   # or pin a specific one
python3 tools/attack_data.py --selftest       # invariants on the committed file
python3 site/build.py && python3 site/test_build.py    # site must build green
```

Commit the regenerated JSON on a normal feature branch and put the
`--update` change summary (new / renamed / newly-revoked techniques, tactic
changes) in the commit message body. The quality-audit routine surfaces
`--check`'s result in its run record so a stale pin never goes unnoticed;
any session may perform the update. `tools/check_run.py` FAILs when the
dataset is missing or violates invariants, and WARNs when entry technique
ids are unknown to the pinned release — the usual signal that the pin is
older than the ids the sources now use.

## Consumers

| Consumer | What it reads |
|---|---|
| `site/content_model.py` | `load_attack_dataset()` / `resolve_technique_id()` — the shared loader every other consumer goes through |
| `site/build.py` | entity/CVE → TTP aggregation, entity-page ATT&CK sections, the `/attack/` matrix + overlap view, `data/attack.json`, per-entity Navigator layer exports |
| `site/stix_model.py` | `stix_id` (each technique's upstream MITRE STIX id) → the `/stix/` bundles reference MITRE's canonical `attack-pattern` objects; a pin written before the field existed falls back to a deterministic local id, still consumer-mergeable via the `mitre-attack` external_id |
| `tools/check_run.py` | dataset presence/invariants; entry `techniques[]` id existence + lifecycle WARNs |
| research / verification agents | technique names + definitions when composing and cold-reading entries |

ATT&CK® is a registered trademark of The MITRE Corporation. The dataset is
© The MITRE Corporation, used under the [ATT&CK Terms of Use](https://attack.mitre.org/resources/legal-and-branding/terms-of-use/).
