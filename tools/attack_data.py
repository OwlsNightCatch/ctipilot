#!/usr/bin/env python3
"""attack_data.py — build, version and update the repo's MITRE ATT&CK dataset.

The pipeline maps entries, entities and CVEs onto MITRE ATT&CK techniques
(entry `techniques[]` frontmatter + legacy in-prose T-ids). Those mappings
are only meaningful against a *specific* ATT&CK release: technique ids get
revoked and merged, tactics are added and renamed (v19 replaced Defense
Evasion with Stealth + Defense Impairment, adding TA0112), and definitions
evolve. This tool pins the release the whole repo renders and validates
against, as one committed, diff-reviewable JSON file:

    attack/enterprise-attack.json      (contract: attack/README.md)

Upstream is the official MITRE CTI STIX 2.1 repository
(github.com/mitre-attack/attack-stix-data). Its `index.json` is the
version catalog; each release is a self-contained STIX bundle. This tool
extracts the compact subset the pipeline needs — technique id → name,
tactics, first-paragraph definition, sub-technique parentage, platforms,
lifecycle flags (deprecated / revoked + `revoked_by` forwarding, the
ATT&CK analogue of the registry's `merged_into` tombstones), upstream
STIX id (`stix_id`, feeds the site's STIX export) — plus the
tactic table in official matrix order and the release metadata.

Revoked and deprecated techniques are KEPT in the dataset, flagged: entries
are immutable, so a T-id cited in a 2026-05 entry must still resolve after
MITRE revokes it; consumers resolve `revoked_by` forward exactly like
registry tombstones.

Usage:
    python3 tools/attack_data.py --info                     # offline: local dataset summary
    python3 tools/attack_data.py --check                    # network: local vs upstream latest
    python3 tools/attack_data.py --update                   # network: fetch latest, rewrite dataset
    python3 tools/attack_data.py --update --version 19.0    # pin a specific upstream release
    python3 tools/attack_data.py --update --from-file P     # offline: build from a downloaded bundle
    python3 tools/attack_data.py --selftest                 # offline: dataset invariants

Exit codes: --check → 0 up-to-date / 1 update available or dataset missing /
2 error. Everything else → 0 success / 2 error (--selftest → 1 on failed
invariant). Stdlib-only, read-only against upstream; the only file it ever
writes is the dataset itself.

Update procedure (operator or routine self-evolution):
    python3 tools/attack_data.py --check          # is there a new release?
    python3 tools/attack_data.py --update         # rewrite attack/enterprise-attack.json
    python3 tools/attack_data.py --selftest       # invariants on the new file
    python3 site/build.py && python3 site/test_build.py
    git add attack/enterprise-attack.json && git commit  # normal feature-branch flow
The --update summary (added / newly-revoked / renamed techniques, tactic
changes) belongs in the commit message body.
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = ROOT / "attack" / "enterprise-attack.json"

INDEX_URL = (
    "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/index.json"
)
COLLECTION_NAME = "Enterprise ATT&CK"
DOMAIN = "enterprise-attack"

USER_AGENT = "ctipilot-attack-sync/1.0 (+https://ctipilot.ch)"
FETCH_TIMEOUT = 300
MAX_BODY_BYTES = 200 * 1024 * 1024  # STIX bundles are ~55 MB and growing

DATASET_SCHEMA = 1
TECHNIQUE_ID_RE = re.compile(r"^T\d{4}(\.\d{3})?$")
TACTIC_ID_RE = re.compile(r"^TA\d{4}$")
VERSION_RE = re.compile(r"^\d+\.\d+$")

# STIX descriptions carry "(Citation: …)" markers and markdown links; the
# pipeline wants clean prose definitions.
_CITATION_RE = re.compile(r"\s*\(Citation:[^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def _clean_definition(description: str | None) -> str:
    """First paragraph of a STIX description, citation markers stripped."""
    if not description:
        return ""
    first = description.strip().split("\n")[0]
    first = _CITATION_RE.sub("", first)
    first = _MD_LINK_RE.sub(r"\1", first)
    return re.sub(r"\s{2,}", " ", first).strip()


def _http_get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT, context=ctx) as resp:
        data = resp.read(MAX_BODY_BYTES + 1)
    if len(data) > MAX_BODY_BYTES:
        raise RuntimeError(f"response exceeds {MAX_BODY_BYTES} bytes: {url}")
    return data


def _external_id(obj: dict, source_name: str = "mitre-attack") -> str | None:
    for ref in obj.get("external_references") or []:
        if ref.get("source_name") == source_name and ref.get("external_id"):
            return ref["external_id"]
    return None


def _external_url(obj: dict, source_name: str = "mitre-attack") -> str | None:
    for ref in obj.get("external_references") or []:
        if ref.get("source_name") == source_name and ref.get("url"):
            return ref["url"]
    return None


# ---------------------------------------------------------------------------
# Upstream catalog
# ---------------------------------------------------------------------------


def fetch_upstream_versions() -> list:
    """Return the enterprise collection's version list, newest first:
    [{version, url, modified}, …] straight from the official index.json."""
    index = json.loads(_http_get(INDEX_URL).decode("utf-8"))
    for coll in index.get("collections") or []:
        if coll.get("name") == COLLECTION_NAME:
            versions = list(coll.get("versions") or [])
            versions.sort(
                key=lambda v: tuple(int(p) for p in str(v.get("version", "0.0")).split(".")),
                reverse=True,
            )
            return versions
    raise RuntimeError(f"collection {COLLECTION_NAME!r} not found in {INDEX_URL}")


# ---------------------------------------------------------------------------
# Bundle → compact dataset
# ---------------------------------------------------------------------------


def extract_dataset(bundle: dict, source_url: str) -> dict:
    """Extract the compact ATT&CK dataset from a STIX 2.1 bundle."""
    objects = bundle.get("objects") or []
    by_stix_id = {o["id"]: o for o in objects if o.get("id")}

    collection = next(
        (o for o in objects if o.get("type") == "x-mitre-collection"), None
    )
    if collection is None:
        raise RuntimeError("bundle carries no x-mitre-collection object")
    attack_version = str(collection.get("x_mitre_version") or "").strip()
    if not VERSION_RE.match(attack_version):
        raise RuntimeError(f"unexpected collection version {attack_version!r}")

    matrix = next((o for o in objects if o.get("type") == "x-mitre-matrix"), None)
    if matrix is None:
        raise RuntimeError("bundle carries no x-mitre-matrix object")

    # Tactics, in official matrix order.
    tactics = []
    tactic_order: dict = {}
    for stix_ref in matrix.get("tactic_refs") or []:
        t = by_stix_id.get(stix_ref)
        if not t or t.get("type") != "x-mitre-tactic":
            raise RuntimeError(f"matrix tactic_ref {stix_ref!r} does not resolve")
        shortname = t.get("x_mitre_shortname")
        tactic_order[shortname] = len(tactics)
        tactics.append(
            {
                "id": _external_id(t),
                "shortname": shortname,
                "name": t.get("name"),
                "definition": _clean_definition(t.get("description")),
                "url": _external_url(t),
            }
        )

    # revoked-by forwarding (ATT&CK's tombstones).
    revoked_by: dict = {}
    for rel in objects:
        if rel.get("type") != "relationship" or rel.get("relationship_type") != "revoked-by":
            continue
        src = by_stix_id.get(rel.get("source_ref"))
        dst = by_stix_id.get(rel.get("target_ref"))
        if not src or not dst or src.get("type") != "attack-pattern":
            continue
        src_id, dst_id = _external_id(src), _external_id(dst)
        if src_id and dst_id and src_id != dst_id:
            revoked_by[src_id] = dst_id

    techniques: dict = {}
    for obj in objects:
        if obj.get("type") != "attack-pattern":
            continue
        tid = _external_id(obj)
        if not tid or not TECHNIQUE_ID_RE.match(tid):
            raise RuntimeError(f"attack-pattern without a valid T-id: {obj.get('name')!r}")
        phases = [
            p.get("phase_name")
            for p in obj.get("kill_chain_phases") or []
            if p.get("kill_chain_name") == "mitre-attack"
        ]
        phases.sort(key=lambda s: tactic_order.get(s, 999))
        is_sub = bool(obj.get("x_mitre_is_subtechnique"))
        techniques[tid] = {
            "stix_id": obj.get("id"),
            "name": obj.get("name"),
            "tactics": phases,
            "subtechnique": is_sub,
            "parent": tid.split(".")[0] if is_sub else None,
            "platforms": sorted(obj.get("x_mitre_platforms") or []),
            "version": obj.get("x_mitre_version"),
            "deprecated": bool(obj.get("x_mitre_deprecated")),
            "revoked": bool(obj.get("revoked")),
            "revoked_by": revoked_by.get(tid),
            "url": _external_url(obj),
            "definition": _clean_definition(obj.get("description")),
        }

    active = [t for t in techniques.values() if not t["deprecated"] and not t["revoked"]]
    dataset = {
        "schema": DATASET_SCHEMA,
        "domain": DOMAIN,
        "attack_version": attack_version,
        "upstream_modified": collection.get("modified"),
        "source_url": source_url,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_by": "tools/attack_data.py",
        "counts": {
            "tactics": len(tactics),
            "techniques": len(techniques),
            "techniques_active": len(active),
            "subtechniques_active": sum(1 for t in active if t["subtechnique"]),
        },
        "tactics": tactics,
        "techniques": {k: techniques[k] for k in sorted(techniques)},
    }
    return dataset


# ---------------------------------------------------------------------------
# Local dataset + change summary
# ---------------------------------------------------------------------------


def load_dataset(path: Path = DATASET_PATH) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_dataset(dataset: dict, path: Path = DATASET_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dataset, indent=1, ensure_ascii=False, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def summarise_change(old: dict | None, new: dict) -> list:
    """Human-readable delta lines for the commit message / run record."""
    lines = [
        f"ATT&CK {DOMAIN} → v{new['attack_version']}"
        + (f" (was v{old['attack_version']})" if old else " (initial import)")
    ]
    if not old:
        c = new["counts"]
        lines.append(
            f"  {c['tactics']} tactics, {c['techniques_active']} active techniques "
            f"({c['subtechniques_active']} sub-techniques), "
            f"{c['techniques'] - c['techniques_active']} revoked/deprecated kept for resolution"
        )
        return lines
    ot, nt = old.get("techniques", {}), new.get("techniques", {})
    added = sorted(set(nt) - set(ot))
    removed = sorted(set(ot) - set(nt))
    renamed = sorted(
        k for k in set(ot) & set(nt) if ot[k].get("name") != nt[k].get("name")
    )
    newly_gone = sorted(
        k
        for k in set(ot) & set(nt)
        if (nt[k]["revoked"] or nt[k]["deprecated"])
        and not (ot[k]["revoked"] or ot[k]["deprecated"])
    )
    o_tac = [t["shortname"] for t in old.get("tactics", [])]
    n_tac = [t["shortname"] for t in new.get("tactics", [])]
    if o_tac != n_tac:
        lines.append(f"  tactics: {', '.join(o_tac)} → {', '.join(n_tac)}")
    if added:
        lines.append(f"  new techniques ({len(added)}): {', '.join(added[:20])}"
                     + (" …" if len(added) > 20 else ""))
    if newly_gone:
        lines.append(
            f"  newly revoked/deprecated ({len(newly_gone)}): "
            + ", ".join(f"{k}→{nt[k]['revoked_by']}" if nt[k].get("revoked_by") else k
                        for k in newly_gone[:20])
            + (" …" if len(newly_gone) > 20 else "")
        )
    if renamed:
        lines.append(f"  renamed ({len(renamed)}): {', '.join(renamed[:20])}"
                     + (" …" if len(renamed) > 20 else ""))
    if removed:
        lines.append(
            f"  REMOVED upstream ({len(removed)}): {', '.join(removed[:20])}"
            + (" …" if len(removed) > 20 else "")
            + " — ids vanished from the bundle; check entries citing them"
        )
    if len(lines) == 1:
        lines.append("  no technique-level changes")
    return lines


# ---------------------------------------------------------------------------
# Invariants (--selftest, offline)
# ---------------------------------------------------------------------------


def selftest(dataset: dict | None) -> list:
    """Return a list of invariant violations (empty = healthy)."""
    errs: list = []
    if dataset is None:
        return [f"dataset missing: {DATASET_PATH.relative_to(ROOT)} (run --update)"]
    if dataset.get("schema") != DATASET_SCHEMA:
        errs.append(f"schema must be {DATASET_SCHEMA}")
    if dataset.get("domain") != DOMAIN:
        errs.append(f"domain must be {DOMAIN!r}")
    if not VERSION_RE.match(str(dataset.get("attack_version") or "")):
        errs.append(f"attack_version {dataset.get('attack_version')!r} is not MAJOR.MINOR")

    tactics = dataset.get("tactics") or []
    shortnames = [t.get("shortname") for t in tactics]
    if len(tactics) < 10:
        errs.append(f"only {len(tactics)} tactics — expected the full matrix")
    if len(set(shortnames)) != len(shortnames):
        errs.append("duplicate tactic shortnames")
    for t in tactics:
        if not TACTIC_ID_RE.match(str(t.get("id") or "")):
            errs.append(f"tactic {t.get('shortname')!r}: id {t.get('id')!r} is not TA####")
        for field in ("shortname", "name", "definition", "url"):
            if not t.get(field):
                errs.append(f"tactic {t.get('id')!r}: {field} missing")

    techniques = dataset.get("techniques") or {}
    active = 0
    known_shortnames = set(shortnames)
    for tid, t in techniques.items():
        if not TECHNIQUE_ID_RE.match(tid):
            errs.append(f"technique id {tid!r} malformed")
            continue
        lifecycle_gone = t.get("revoked") or t.get("deprecated")
        if not lifecycle_gone:
            active += 1
            if not t.get("tactics"):
                errs.append(f"{tid}: active technique with no tactics")
            if not t.get("definition"):
                errs.append(f"{tid}: active technique with no definition")
        for s in t.get("tactics") or []:
            if s not in known_shortnames:
                errs.append(f"{tid}: unknown tactic shortname {s!r}")
        if not t.get("name"):
            errs.append(f"{tid}: name missing")
        if t.get("subtechnique"):
            parent = t.get("parent")
            if parent != tid.split(".")[0]:
                errs.append(f"{tid}: parent {parent!r} does not match id prefix")
            if parent not in techniques:
                errs.append(f"{tid}: parent {parent!r} not in dataset")
            elif techniques[parent].get("subtechnique"):
                errs.append(f"{tid}: parent {parent!r} is itself a sub-technique")
        elif t.get("parent") is not None:
            errs.append(f"{tid}: non-subtechnique with parent set")
        # `stix_id` is optional (absent on pins written before it was
        # extracted); the STIX export falls back to a deterministic local id.
        sid = t.get("stix_id")
        if sid is not None and not re.match(
            r"^attack-pattern--[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
            str(sid),
        ):
            errs.append(f"{tid}: stix_id {sid!r} is not attack-pattern--<uuid>")
        rb = t.get("revoked_by")
        if rb is not None:
            if rb not in techniques:
                errs.append(f"{tid}: revoked_by {rb!r} not in dataset")
            if not t.get("revoked"):
                errs.append(f"{tid}: revoked_by set but revoked is false")
    if active < 400:
        errs.append(f"only {active} active techniques — bundle looks truncated")

    counts = dataset.get("counts") or {}
    if counts.get("techniques") != len(techniques):
        errs.append("counts.techniques does not match the technique table")
    if counts.get("techniques_active") != active:
        errs.append("counts.techniques_active does not match the technique table")
    return errs


# Consumers resolve `revoked_by` forwarding via
# `site/content_model.resolve_technique_id` — the shared implementation.


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def cmd_info() -> int:
    ds = load_dataset()
    if ds is None:
        print(f"no local dataset at {DATASET_PATH.relative_to(ROOT)} — run --update")
        return 2
    c = ds.get("counts", {})
    print(f"domain:           {ds.get('domain')}")
    print(f"attack_version:   {ds.get('attack_version')}")
    print(f"upstream_modified:{ds.get('upstream_modified')}")
    print(f"generated_at:     {ds.get('generated_at')}")
    print(f"tactics:          {c.get('tactics')}")
    print(
        f"techniques:       {c.get('techniques_active')} active "
        f"({c.get('subtechniques_active')} sub-techniques), "
        f"{(c.get('techniques') or 0) - (c.get('techniques_active') or 0)} revoked/deprecated"
    )
    return 0


def cmd_check() -> int:
    ds = load_dataset()
    local = ds.get("attack_version") if ds else None
    try:
        versions = fetch_upstream_versions()
    except Exception as exc:  # noqa: BLE001 — CLI boundary
        print(f"ERROR: cannot read upstream catalog: {exc}", file=sys.stderr)
        return 2
    latest = versions[0]["version"]
    if ds is None:
        print(f"local: none | upstream latest: v{latest} → run --update")
        return 1
    if local == latest:
        print(f"up to date: local v{local} == upstream latest v{latest}")
        return 0
    print(f"update available: local v{local} → upstream v{latest} "
          f"(published {versions[0].get('modified')}) — run --update")
    return 1


def cmd_update(pin_version: str | None, from_file: str | None) -> int:
    old = load_dataset()
    try:
        if from_file:
            source_url = f"file:{from_file}"
            bundle = json.loads(Path(from_file).read_text(encoding="utf-8"))
        else:
            versions = fetch_upstream_versions()
            if pin_version:
                match = [v for v in versions if v["version"] == pin_version]
                if not match:
                    avail = ", ".join(v["version"] for v in versions[:10])
                    print(f"ERROR: v{pin_version} not in upstream catalog (latest: {avail})",
                          file=sys.stderr)
                    return 2
                chosen = match[0]
            else:
                chosen = versions[0]
            source_url = chosen["url"]
            print(f"fetching {source_url} …")
            bundle = json.loads(_http_get(source_url).decode("utf-8"))
        dataset = extract_dataset(bundle, source_url)
    except Exception as exc:  # noqa: BLE001 — CLI boundary
        print(f"ERROR: update failed: {exc}", file=sys.stderr)
        return 2
    if pin_version and dataset["attack_version"] != pin_version:
        print(f"ERROR: bundle self-reports v{dataset['attack_version']}, "
              f"not requested v{pin_version}", file=sys.stderr)
        return 2
    errs = selftest(dataset)
    if errs:
        print("ERROR: extracted dataset fails invariants; not writing:", file=sys.stderr)
        for e in errs[:30]:
            print(f"  - {e}", file=sys.stderr)
        return 2
    write_dataset(dataset)
    for line in summarise_change(old, dataset):
        print(line)
    print(f"wrote {DATASET_PATH.relative_to(ROOT)}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--info", action="store_true", help="print local dataset summary (offline)")
    ap.add_argument("--check", action="store_true", help="compare local vs upstream latest")
    ap.add_argument("--update", action="store_true", help="fetch and rewrite the dataset")
    ap.add_argument("--version", metavar="X.Y", help="with --update: pin an upstream release")
    ap.add_argument("--from-file", metavar="PATH",
                    help="with --update: build from an already-downloaded STIX bundle")
    ap.add_argument("--selftest", action="store_true", help="offline dataset invariants")
    args = ap.parse_args(argv)

    if args.check:
        return cmd_check()
    if args.update:
        return cmd_update(args.version, args.from_file)
    if args.selftest:
        errs = selftest(load_dataset())
        if errs:
            print(f"SELFTEST FAIL — {len(errs)} invariant violation(s):")
            for e in errs:
                print(f"  - {e}")
            return 1
        print("SELFTEST OK")
        return 0
    return cmd_info()


if __name__ == "__main__":
    sys.exit(main())
