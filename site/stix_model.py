#!/usr/bin/env python3
"""STIX 2.1 export model for site/build.py.

Compiles the repo's content store — entries, the entity registry, the CVE
index and the pinned ATT&CK dataset — into STIX 2.1 objects for the
static bundle endpoints under /stix/ (docs/pipeline.md § Machine-readable
surfaces). The markdown store stays the source of truth; this module is a
pure derived layer: no I/O, no identity literals, stdlib only.

Design contract:
  - Deterministic ids. Every STIX id is uuid5 over a permanent store key
    (entry id, registry key, CVE id, relation triple) under a
    project namespace derived from the canonical branding site URL —
    NEVER the SITE_URL env override, so a preview build emits the same
    ids as production. One entity/CVE = one STIX object forever; that
    shared-object graph is how consumers (e.g. OpenCTI) connect briefs
    and deduplicate findings. The spec's SHOULD-use-UUIDv4 for SDOs is
    deliberately traded for byte-identical rebuilds.
  - Pure STIX 2.1. Pipeline metadata with no core property (Admiralty
    reliability, verification, kind, priority, the entry id) travels in
    a property extension under one extension-definition; no x_ custom
    properties.
  - Knowledge products only. The store carries no IOCs (hard gate), so
    there are no indicators, observables or sightings — reports,
    intrusion sets, malware, tools, campaigns, incidents, groupings,
    vulnerabilities, attack patterns, relationships and notes.
  - Timestamps: STIX requires millisecond precision; the store is
    second-precision, so conversions append a literal `.000`.

Mapping summary (registry type → SDO): actor → intrusion-set (ATT&CK /
OpenCTI convention for named groups), campaign → campaign, malware →
malware, tool → tool, incident → incident (2.1 stub), report → report,
trend → grouping (no natural SDO for a named wave), policy → report.
Tombstoned registry records are never emitted; references to them are
remapped to the canonical key before id generation, mirroring
content_model.resolve_entity_key.

Relations: only vocabulary the target platforms accept between the
mapped SDO pair ships under its own name (`uses`, `attributed-to`,
`authored-by`, `variant-of`); every other curated type collapses to
`related-to` with the exact original type preserved in the description
and the extension (`original_type`). Custom relationship strings are
STIX-legal but OpenCTI rejects unknown types between typed pairs and the
full-fidelity vocabulary already ships in data/graph.json.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
import uuid
from typing import Any

import content_model

SPEC_VERSION = "2.1"

# TLP:WHITE marking-definition — STIX 2.1 §7.2.1.4 defines these objects
# verbatim, fixed id included; producers MUST use them unchanged.
TLP_WHITE_ID = "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9"
TLP_WHITE = {
    "type": "marking-definition",
    "spec_version": SPEC_VERSION,
    "id": TLP_WHITE_ID,
    "created": "2017-01-20T00:00:00.000Z",
    "definition_type": "tlp",
    "name": "TLP:WHITE",
    "definition": {"tlp": "white"},
}

# Registry entity type → STIX 2.1 SDO type (see module docstring).
ENTITY_SDO_TYPES = {
    "actor": "intrusion-set",
    "campaign": "campaign",
    "malware": "malware",
    "tool": "tool",
    "incident": "incident",
    "report": "report",
    "trend": "grouping",
    "policy": "report",
    # `product` is deliberately absent. Its natural STIX shape is the
    # `software` SCO, which carries none of the SDO properties this export
    # writes (created/modified/description/external references), so a
    # product would have to be exported as something it is not. Products
    # stay a site-side index surface until a faithful mapping exists.
}

# SDO types that define an `aliases` property (2.1 §4; incident is a stub
# and report/grouping have none — their aliases stay registry-only).
_ALIAS_SDO_TYPES = {"intrusion-set", "campaign", "malware", "tool"}

# Curated relation vocabulary → STIX relationship_type, per (source SDO,
# target SDO) pair. Key: (relation type, source SDO, target SDO). Pairs
# absent here collapse to related-to. `attributed-to` and `uses` from an
# incident are not in the spec's Appendix B (the incident SDO is a stub
# with no relationship rows at all) but are the standard consumer reading
# (OpenCTI supports both), so they keep their names.
SPEC_REL_MAP = {
    ("attributed-to", "campaign", "intrusion-set"): "attributed-to",
    ("attributed-to", "incident", "intrusion-set"): "attributed-to",
    ("attributed-to", "malware", "intrusion-set"): "authored-by",
    ("uses", "intrusion-set", "malware"): "uses",
    ("uses", "intrusion-set", "tool"): "uses",
    ("uses", "campaign", "malware"): "uses",
    ("uses", "campaign", "tool"): "uses",
    ("uses", "incident", "malware"): "uses",
    ("uses", "incident", "tool"): "uses",
    ("variant-of", "malware", "malware"): "variant-of",
}

# NATO Admiralty credibility → STIX confidence, the normative mapping of
# STIX 2.1 Appendix A. Credibility 6 ("truth cannot be judged") maps to
# Not Specified — the property is omitted, exactly like the pre-v3.18
# entries that carry no classification at all.
ADMIRALTY_CONFIDENCE = {"1": 90, "2": 70, "3": 50, "4": 30, "5": 10}

_TS_SECOND_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
_TS_FRACTION_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\.(\d{1,6})Z$")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)

# Ref-carrying properties walked by reference_closure (the subset this
# module ever emits).
_REF_LIST_KEYS = ("object_refs", "object_marking_refs")
_REF_SCALAR_KEYS = ("created_by_ref", "source_ref", "target_ref")


def make_namespace(seed_url: str, configured: str = "") -> uuid.UUID:
    """The project id namespace: the configured UUID (branding
    stix.id_namespace) when set, else uuid5 of the canonical site URL."""
    configured = (configured or "").strip().lower()
    if configured:
        if not _UUID_RE.match(configured):
            raise ValueError(f"stix.id_namespace is not a UUID: {configured!r}")
        return uuid.UUID(configured)
    return uuid.uuid5(uuid.NAMESPACE_URL, seed_url.strip())


def sid(ns: uuid.UUID, stix_type: str, seed: str) -> str:
    """Deterministic STIX id: `<type>--<uuid5(ns, seed)>`. Seeds are
    permanent store keys only — never titles, summaries or any other
    mutable text (a rename must not mint a second object)."""
    return f"{stix_type}--{uuid.uuid5(ns, seed)}"


def stix_ts(value: Any) -> str:
    """A store timestamp (`YYYY-MM-DDTHH:MM:SSZ`), date (`YYYY-MM-DD`) or
    already-fractional upstream timestamp → STIX millisecond precision."""
    s = str(value or "").strip()
    if _TS_SECOND_RE.match(s):
        return s[:-1] + ".000Z"
    m = _TS_FRACTION_RE.match(s)
    if m:
        return f"{m.group(1)}.{m.group(2).ljust(3, '0')[:3]}Z"
    if _DATE_RE.match(s):
        return s + "T00:00:00.000Z"
    raise ValueError(f"not a store timestamp or date: {value!r}")


def confidence_from_credibility(credibility: Any) -> int | None:
    """Admiralty credibility → STIX confidence (Appendix A); None when
    the code is 6 / unknown / absent (STIX: confidence unspecified)."""
    return ADMIRALTY_CONFIDENCE.get(str(credibility).strip())


def _common(obj: dict, *, created_by: str | None) -> dict:
    """Order-independent common-property block; json.dumps(sort_keys=True)
    owns the serialization order, so plain dict merging is safe."""
    out = {"spec_version": SPEC_VERSION, "object_marking_refs": [TLP_WHITE_ID]}
    if created_by:
        out["created_by_ref"] = created_by
    out.update(obj)
    return out


def publisher_identity(ns: uuid.UUID, *, name: str, url: str, anchor_ts: str) -> dict:
    """The publisher identity, created_by_ref of every emitted object.
    `anchor_ts` is a stable store moment (the earliest discovered_at) —
    the object never changes, so created == modified never moves."""
    ts = stix_ts(anchor_ts)
    return {
        "type": "identity",
        "spec_version": SPEC_VERSION,
        "id": sid(ns, "identity", "identity:publisher"),
        "created": ts,
        "modified": ts,
        "name": name,
        "identity_class": "organization",
        "external_references": [{"source_name": name, "url": url}],
        "object_marking_refs": [TLP_WHITE_ID],
    }


def extension_definition(ns: uuid.UUID, *, created_by: str, schema_url: str,
                         anchor_ts: str) -> dict:
    """The one property-extension carrying pipeline metadata that has no
    core STIX property (entry id, kind, priority, verification, the
    Admiralty pair, a downgraded relation's original type)."""
    ts = stix_ts(anchor_ts)
    return {
        "type": "extension-definition",
        "spec_version": SPEC_VERSION,
        "id": sid(ns, "extension-definition", "extension-definition:entry-metadata"),
        "created": ts,
        "modified": ts,
        "created_by_ref": created_by,
        "name": "CTI pipeline entry metadata",
        "description": (
            "Pipeline-native metadata on exported objects: the permanent "
            "entry/registry identifiers, editorial kind and priority, the "
            "sourcing verification tier, the NATO Admiralty rating "
            "(reliability letter has no STIX equivalent; the credibility "
            "digit also drives `confidence` per STIX 2.1 Appendix A), and "
            "the original curated relation type on relationships collapsed "
            "to related-to."
        ),
        "schema": schema_url,
        "version": "1.0",
        "extension_types": ["property-extension"],
        "object_marking_refs": [TLP_WHITE_ID],
    }


def _ext(ext_def_id: str, payload: dict) -> dict:
    return {"extensions": {ext_def_id: {"extension_type": "property-extension", **payload}}}


def _entity_page_url(site_url: str, key: str) -> str:
    return f"{site_url}entities/{urllib.parse.quote(key, safe='')}/"


def entry_report(entry: dict, *, ns: uuid.UUID, ctx: dict) -> dict:
    """One entry → one report SDO. `modified` follows the latest
    changelog record of ANY type (STIX versioning: any change bumps
    modified — deliberately broader than the store's updated_at float
    rule, which only `type: update` records move)."""
    created = stix_ts(entry["discovered_at"])
    record_ts = [str(r.get("at")) for r in entry.get("updates") or []
                 if isinstance(r, dict) and r.get("at")]
    modified = stix_ts(max(record_ts)) if record_ts else created
    labels = sorted({str(v) for v in (
        [entry.get("kind"), entry.get("priority")]
        + list(entry.get("tags") or [])
        + list(entry.get("sectors") or [])
        + list(entry.get("regions") or [])
    ) if v})
    refs = [{"source_name": ctx["publisher_name"],
             "url": ctx["site_url"] + f"entries/{entry['date']}/{entry['slug']}/"}]
    for s in entry.get("sources") or []:
        if isinstance(s, dict) and s.get("url"):
            ref = {"source_name": str(s.get("publisher") or "source"),
                   "url": str(s["url"])}
            if s.get("role"):
                ref["description"] = f"{s['role']} source"
            refs.append(ref)

    object_refs: set[str] = set()
    for key in entry.get("entities") or []:
        canon = content_model.resolve_entity_key(ctx["registry"], str(key))
        stix_id = ctx["entity_ids"].get(canon)
        if stix_id:
            object_refs.add(stix_id)
    for cid in ctx["entry_cve_ids"](entry):
        object_refs.add(ctx["cve_ids"][cid])
    for tid in content_model.entry_technique_ids(entry, ctx["attack_techniques"]):
        stix_id = ctx["technique_ids"].get(tid)
        if stix_id:
            object_refs.add(stix_id)
    for ref_id in entry.get("references") or []:
        stix_id = ctx["report_ids"].get(str(ref_id))
        if stix_id:
            object_refs.add(stix_id)
    if not object_refs:
        # report.object_refs is required non-empty; an entry with nothing
        # linkable anchors on the publisher identity.
        object_refs = {ctx["identity_id"]}

    report = {
        "type": "report",
        "id": ctx["report_ids"][entry["id"]],
        "created": created,
        "modified": modified,
        "published": created,
        "name": str(entry.get("title") or entry["id"]),
        "description": "\n\n".join(
            p.strip() for p in (entry.get("headline"), entry.get("summary")) if p
        ),
        "report_types": ["vulnerability"] if entry.get("kind") == "vulnerability"
        else ["threat-report"],
        "labels": labels,
        "external_references": refs,
        "object_refs": sorted(object_refs),
    }
    cls = entry.get("classification") if isinstance(entry.get("classification"), dict) else {}
    conf = confidence_from_credibility(cls.get("credibility"))
    if conf is not None:
        report["confidence"] = conf
    payload = {
        "entry_id": entry["id"],
        "kind": str(entry.get("kind") or ""),
        "priority": str(entry.get("priority") or ""),
        "verification": str(entry.get("verification") or ""),
    }
    if cls.get("reliability"):
        payload["reliability"] = str(cls["reliability"])
    if cls.get("credibility") is not None:
        payload["credibility"] = str(cls["credibility"])
    report.update(_ext(ctx["ext_def_id"], payload))
    return _common(report, created_by=ctx["identity_id"])


def entity_sdo(key: str, ent: dict, *, ns: uuid.UUID, ctx: dict) -> dict | None:
    """One canonical registry record → one SDO; None for tombstones.
    `modified` follows the latest citing entry's activity moment — the
    registry carries no per-record timestamp, and a new citation changes
    the report/grouping membership consumers see."""
    if ent.get("merged_into"):
        return None
    sdo_type = ENTITY_SDO_TYPES.get(str(ent.get("type") or ""))
    if not sdo_type:
        return None
    created = stix_ts(ent.get("first_seen") or ctx["anchor_ts"])
    citing = ctx["entries_by_entity"].get(key) or []
    activity = [content_model.entry_activity_ts(e) for e in citing]
    activity_ts = max((stix_ts(a) for a in activity if a), default=created)
    modified = max(created, activity_ts)
    labels = sorted({str(v) for v in [ent.get("type"), ent.get("nexus")] if v})
    obj = {
        "type": sdo_type,
        "id": ctx["entity_ids"][key],
        "created": created,
        "modified": modified,
        "name": str(ent.get("name") or key),
        "labels": labels,
        "external_references": [{
            "source_name": ctx["publisher_name"],
            "url": _entity_page_url(ctx["site_url"], key),
        }],
    }
    if ent.get("summary"):
        obj["description"] = str(ent["summary"]).strip()
    aliases = [str(a) for a in ent.get("aliases") or [] if a]
    if aliases and sdo_type in _ALIAS_SDO_TYPES:
        obj["aliases"] = aliases
    if sdo_type == "malware":
        obj["is_family"] = True
    citing_report_ids = sorted(
        ctx["report_ids"][e["id"]] for e in citing if e["id"] in ctx["report_ids"]
    ) or [ctx["identity_id"]]
    if sdo_type == "grouping":
        obj["context"] = "unspecified"
        obj["object_refs"] = citing_report_ids
    elif sdo_type == "report":
        obj["published"] = created
        obj["object_refs"] = citing_report_ids
    obj.update(_ext(ctx["ext_def_id"], {"entity_key": key}))
    return _common(obj, created_by=ctx["identity_id"])


def entity_relationships(registry: dict, *, ns: uuid.UUID, ctx: dict) -> list[dict]:
    """Curated registry relations[] → SROs (see module docstring for the
    vocabulary collapse). Timestamps derive from the sourcing entry."""
    out = []
    for rel in content_model.registry_relations(registry):
        subj = content_model.resolve_entity_key(registry, rel["subject"])
        obj_key = content_model.resolve_entity_key(registry, rel["object"])
        src_id = ctx["entity_ids"].get(subj)
        tgt_id = ctx["entity_ids"].get(obj_key)
        if not src_id or not tgt_id or src_id == tgt_id:
            continue
        # A type with no SDO mapping (product — a derived index node, not a
        # STIX SDO) is not exported, so an edge touching one is skipped
        # rather than emitted with a dangling ref.
        src_sdo = ENTITY_SDO_TYPES.get(str(registry[subj]["type"]))
        tgt_sdo = ENTITY_SDO_TYPES.get(str(registry[obj_key]["type"]))
        if not src_sdo or not tgt_sdo:
            continue
        orig = rel["type"]
        stix_type = SPEC_REL_MAP.get((orig, src_sdo, tgt_sdo), "related-to")
        source_entry = ctx["entries_by_id"].get(str(rel.get("source") or ""))
        ts = stix_ts(source_entry["discovered_at"]) if source_entry else stix_ts(ctx["anchor_ts"])
        sro = {
            "type": "relationship",
            "id": sid(ns, "relationship", f"rel:{subj}|{orig}|{obj_key}"),
            "created": ts,
            "modified": ts,
            "relationship_type": stix_type,
            "source_ref": src_id,
            "target_ref": tgt_id,
        }
        desc = str(rel.get("note") or "").strip()
        if stix_type != orig:
            tag = f"curated relation type: {orig}"
            desc = f"{desc} ({tag})" if desc else tag
            sro.update(_ext(ctx["ext_def_id"], {"original_type": orig}))
        if desc:
            sro["description"] = desc
        if source_entry:
            sro["external_references"] = [{
                "source_name": ctx["publisher_name"],
                "url": ctx["site_url"]
                + f"entries/{source_entry['date']}/{source_entry['slug']}/",
            }]
        out.append(_common(sro, created_by=ctx["identity_id"]))
    out.sort(key=lambda o: o["id"])
    return out


def cve_vulnerability(cid: str, *, ns: uuid.UUID, ctx: dict) -> dict:
    """One CVE → one vulnerability SDO shared by every citing report.
    Details come from the newest citing entry's cves[] record; lifecycle
    dates from state/cves_seen.json when present."""
    seen = ctx["cves_seen"].get(cid) or {}
    citing = ctx["entries_by_cve"].get(cid) or []
    if seen.get("first_seen"):
        created = stix_ts(seen["first_seen"])
    elif citing:
        created = stix_ts(min(str(e["discovered_at"]) for e in citing))
    else:
        created = stix_ts(ctx["anchor_ts"])
    modified = max(created, stix_ts(seen["last_seen"])) if seen.get("last_seen") else created

    statuses: set[str] = set()
    newest_rec: dict = {}
    for e in citing:
        for rec in e.get("cves") or []:
            if isinstance(rec, dict) and rec.get("id") == cid:
                statuses.update(str(s) for s in rec.get("status") or [])
                newest_rec = rec  # citing is sorted ascending by discovered_at
    lines = []
    if seen.get("title"):
        lines.append(str(seen["title"]).strip())
    detail = " · ".join(
        f"{label}: {newest_rec[k]}"
        for label, k in (("CVSS", "cvss"), ("Type", "type"),
                         ("Vector", "vector"), ("Auth", "auth"))
        if newest_rec.get(k)
    )
    if detail:
        lines.append(detail)
    for label, k in (("Affected", "affected"), ("Fixed", "fixed")):
        if newest_rec.get(k):
            lines.append(f"{label}: {newest_rec[k]}")

    refs = [{"source_name": "cve", "external_id": cid}]
    if seen.get("primary_source_url"):
        refs.append({"source_name": "advisory", "url": str(seen["primary_source_url"]),
                     "description": "primary source of first coverage"})
    obj = {
        "type": "vulnerability",
        "id": ctx["cve_ids"][cid],
        "created": created,
        "modified": modified,
        "name": cid,
        "external_references": refs,
    }
    if lines:
        obj["description"] = "\n".join(lines)
    if statuses:
        obj["labels"] = sorted(statuses)
    return _common(obj, created_by=ctx["identity_id"])


def attack_pattern_sdo(tid: str, rec: dict, *, ns: uuid.UUID, ctx: dict) -> dict:
    """A used ATT&CK technique → a minimal attack-pattern SDO under
    MITRE's own upstream STIX id when the pin carries it (consumers merge
    it with connector-imported ATT&CK data), else a deterministic local
    id — still mergeable via the mitre-attack external_id."""
    ts = stix_ts(ctx["attack_upstream_modified"])
    ext_ref = {"source_name": "mitre-attack", "external_id": tid}
    if rec.get("url"):
        ext_ref["url"] = str(rec["url"])
    obj = {
        "type": "attack-pattern",
        "id": ctx["technique_ids"][tid],
        "created": ts,
        "modified": ts,
        "name": str(rec.get("name") or tid),
        "external_references": [ext_ref],
    }
    if rec.get("definition"):
        obj["description"] = str(rec["definition"])
    phases = [{"kill_chain_name": "mitre-attack", "phase_name": str(p)}
              for p in rec.get("tactics") or []]
    if phases:
        obj["kill_chain_phases"] = phases
    return _common(obj, created_by=None)


def correction_notes(entry: dict, *, ns: uuid.UUID, ctx: dict) -> list[dict]:
    """Non-internal `type: correction` changelog records → note SDOs on
    the entry's report — the intelligence-integrity signal worth
    propagating (routine updates only bump the report's modified)."""
    out = []
    for rec in entry.get("updates") or []:
        if not isinstance(rec, dict) or rec.get("type") != "correction":
            continue
        if rec.get("internal") is True or not rec.get("at") or not rec.get("summary"):
            continue
        at = stix_ts(str(rec["at"]))
        out.append(_common({
            "type": "note",
            "id": sid(ns, "note", f"note:{entry['id']}#{rec['at']}"),
            "created": at,
            "modified": at,
            "abstract": "Correction",
            "content": str(rec["summary"]).strip(),
            "labels": ["correction"],
            "object_refs": [ctx["report_ids"][entry["id"]]],
        }, created_by=ctx["identity_id"]))
    return out


def compile_stix(entries: list, registry: dict, *, cves_seen_records: list,
                 attack_dataset: dict | None, ns: uuid.UUID,
                 publisher_name: str, site_url: str,
                 extension_schema_url: str) -> dict:
    """The whole store → {'objects': {stix_id: object}, 'report_ids':
    {entry_id: stix_id}, 'anchor_ids': [...]}. Single compilation entry
    point; bundle builders select from `objects` and close over refs."""
    anchor_ts = min(
        (str(e["discovered_at"]) for e in entries if e.get("discovered_at")),
        default="2000-01-01T00:00:00Z",
    )
    identity = publisher_identity(ns, name=publisher_name, url=site_url,
                                  anchor_ts=anchor_ts)
    ext_def = extension_definition(ns, created_by=identity["id"],
                                   schema_url=extension_schema_url,
                                   anchor_ts=anchor_ts)

    attack_techniques = (attack_dataset or {}).get("techniques") or {}
    entries_by_id = {e["id"]: e for e in entries}
    entries_by_entity: dict[str, list] = {}
    for e in entries:  # entries arrive sorted ascending (collect_entries)
        for key in e.get("entities") or []:
            canon = content_model.resolve_entity_key(registry, str(key))
            entries_by_entity.setdefault(canon, []).append(e)

    def entry_cve_ids(entry: dict) -> list[str]:
        seen: list[str] = []
        for c in entry.get("cves") or []:
            if isinstance(c, dict) and c.get("id") and str(c["id"]) not in seen:
                seen.append(str(c["id"]))
        return seen

    entries_by_cve: dict[str, list] = {}
    for e in entries:
        for cid in entry_cve_ids(e):
            entries_by_cve.setdefault(cid, []).append(e)
    cves_seen = {str(c["id"]): c for c in cves_seen_records
                 if isinstance(c, dict) and c.get("id")}
    all_cves = sorted(entries_by_cve)  # export only CVEs the store analyses

    used_tids = sorted({
        tid for e in entries
        for tid in content_model.entry_technique_ids(e, attack_techniques)
        if tid in attack_techniques
    })

    ctx: dict[str, Any] = {
        "publisher_name": publisher_name,
        "site_url": site_url,
        "registry": registry,
        "identity_id": identity["id"],
        "ext_def_id": ext_def["id"],
        "anchor_ts": anchor_ts,
        "entries_by_id": entries_by_id,
        "entries_by_entity": entries_by_entity,
        "entries_by_cve": entries_by_cve,
        "cves_seen": cves_seen,
        "attack_techniques": attack_techniques,
        "attack_upstream_modified": (attack_dataset or {}).get("upstream_modified")
        or anchor_ts,
        "entry_cve_ids": entry_cve_ids,
        "report_ids": {e["id"]: sid(ns, "report", f"entry:{e['id']}") for e in entries},
        "entity_ids": {
            key: sid(ns, ENTITY_SDO_TYPES[str(ent["type"])], f"entity:{key}")
            for key, ent in registry.items()
            if not ent.get("merged_into") and str(ent.get("type")) in ENTITY_SDO_TYPES
        },
        "cve_ids": {cid: sid(ns, "vulnerability", f"cve:{cid}") for cid in all_cves},
        "technique_ids": {
            tid: (attack_techniques[tid].get("stix_id")
                  or sid(ns, "attack-pattern", f"attack:{tid}"))
            for tid in used_tids
        },
    }

    objects: dict[str, dict] = {TLP_WHITE_ID: TLP_WHITE,
                                identity["id"]: identity, ext_def["id"]: ext_def}
    for key in sorted(ctx["entity_ids"]):
        obj = entity_sdo(key, registry[key], ns=ns, ctx=ctx)
        if obj:
            objects[obj["id"]] = obj
    for cid in all_cves:
        obj = cve_vulnerability(cid, ns=ns, ctx=ctx)
        objects[obj["id"]] = obj
    for tid in used_tids:
        obj = attack_pattern_sdo(tid, attack_techniques[tid], ns=ns, ctx=ctx)
        objects[obj["id"]] = obj
    for e in entries:
        objects[ctx["report_ids"][e["id"]]] = entry_report(e, ns=ns, ctx=ctx)
        for note in correction_notes(e, ns=ns, ctx=ctx):
            objects[note["id"]] = note
    for sro in entity_relationships(registry, ns=ns, ctx=ctx):
        objects[sro["id"]] = sro

    return {
        "objects": objects,
        "report_ids": ctx["report_ids"],
        "entity_ids": ctx["entity_ids"],
        "anchor_ids": [TLP_WHITE_ID, identity["id"], ext_def["id"]],
    }


def reference_closure(objects: dict, seed_ids: set[str] | list[str]) -> set[str]:
    """Transitive closure over embedded refs, plus every relationship and
    note whose endpoints all land inside — a windowed bundle must never
    carry a dangling ref (consumers drop them)."""
    closure: set[str] = set()
    stack = [i for i in seed_ids if i in objects]
    while stack:
        oid = stack.pop()
        if oid in closure:
            continue
        closure.add(oid)
        obj = objects[oid]
        for k in _REF_LIST_KEYS:
            stack.extend(r for r in obj.get(k) or [] if r in objects)
        for k in _REF_SCALAR_KEYS:
            r = obj.get(k)
            if r and r in objects:
                stack.append(r)
    grew = True
    while grew:
        grew = False
        for oid, obj in objects.items():
            if oid in closure:
                continue
            if obj.get("type") == "relationship":
                inside = (obj["source_ref"] in closure and obj["target_ref"] in closure)
            elif obj.get("type") == "note":
                inside = all(r in closure for r in obj.get("object_refs") or [])
            else:
                continue
            if inside:
                closure.add(oid)
                grew = True
    return closure


def make_bundle(ns: uuid.UUID, name: str, objects: list[dict]) -> dict:
    """A STIX 2.1 bundle over the given objects, ascending by (created,
    id). The bundle id derives from the member id:modified set, so it
    changes exactly when the content does."""
    objs = sorted(objects, key=lambda o: (str(o.get("created") or ""), o["id"]))
    digest = hashlib.sha256("\n".join(
        sorted(f"{o['id']}:{o.get('modified', '')}" for o in objs)
    ).encode("utf-8")).hexdigest()
    return {
        "type": "bundle",
        "id": sid(ns, "bundle", f"bundle:{name}:{digest}"),
        "objects": objs,
    }


def serialize(doc: dict) -> str:
    """Canonical serialization — sort_keys + compact separators is the
    byte-identical-rebuild guarantee."""
    return json.dumps(doc, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def extension_schema(ext_def_id: str) -> dict:
    """The JSON Schema the extension-definition's `schema` URL serves."""
    prop = {"type": "string"}
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "entry-metadata-extension",
        "title": "CTI pipeline entry metadata (property extension)",
        "description": (
            "Property extension carried under extension id "
            f"{ext_def_id} on exported reports, entity SDOs and "
            "downgraded relationships."
        ),
        "type": "object",
        "properties": {
            "extension_type": {"const": "property-extension"},
            "entry_id": {**prop, "description": "permanent entry id (YYYY-MM-DD/slug)"},
            "entity_key": {**prop, "description": "permanent registry key (type:slug)"},
            "kind": prop,
            "priority": prop,
            "verification": prop,
            "reliability": {**prop, "description": "NATO Admiralty source reliability A-F"},
            "credibility": {**prop, "description": "NATO Admiralty item credibility 1-6"},
            "original_type": {**prop, "description":
                              "curated relation type behind a related-to"},
        },
        "required": ["extension_type"],
        "additionalProperties": False,
    }
