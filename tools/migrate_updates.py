#!/usr/bin/env python3
"""One-shot v3 → v4.0 migration: fold `update_of` entries into their root entry.

v3 modelled developments and corrections as SEPARATE entry files linked by
`update_of: <original id>`. v4.0 (docs/pipeline.md § Entry lifecycle) keeps
ONE living entry per finding: every development, correction or improvement
is appended to that entry as a timestamped `updates[]` changelog record
paired with a `## <Type> — <at>` body section, and `updated_at` floats the
entry back to the top of the live brief.

This tool performs the migration of the existing store, once:

  1. Every entry carrying `update_of` is folded into the ULTIMATE root of
     its chain (an update-of-an-update lands on the same root), oldest
     first, as one changelog record:
         {at: <update's discovered_at>, run_id: <update's run_id>,
          type: correction|update, summary: <update's summary>,
          fields: [<frontmatter fields the fold changed>],
          merged_from: <the update entry's id>}
     plus a body section `## <Type> — <at>` carrying the update's body
     (with the redundant "**UPDATE (originally covered …):**" opener
     removed). `type` is `correction` when the update's title/headline says
     so, else `update`.
  2. The root's frontmatter is brought to the CURRENT state the chain
     described: per-CVE records are replaced by the update's newer record
     (new CVEs appended); sources / evidence / entities / techniques /
     affected_products / tags / regions / sectors / references / actions /
     closed_sources are unioned in order; priority escalates when the update
     carried a higher priority (adopting its immediate_action when it went
     critical); everything else (title, headline, summary, classification,
     verification, confidence, event_date, deep_dive) keeps the root's value.
  3. `references[]` on every entry and `relations[].source` in the entity
     registry that pointed at a folded update entry are re-pointed to the
     root (the id that still exists).
  4. The folded update files are removed (`git rm` when in a git checkout,
     plain delete otherwise). Old permalinks keep resolving: `site/build.py`
     emits a redirect stub for every `merged_from` id.

Idempotent by construction — a store with no `update_of` entries is a
no-op. Run `--dry-run` first; it prints the plan and writes nothing.
Kept in the repo for provenance, like tools/migrate_briefs.py.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402

# Frontmatter keys as they are meant to read top to bottom (prompts/entry-template.md).
CANONICAL_ORDER = [
    "schema", "kind", "horizon", "title", "headline", "summary", "discovered_at",
    "updated_at", "event_date", "run_id", "priority", "immediate_action", "tags", "regions",
    "sectors", "entities", "techniques", "affected_products", "cves", "sources",
    "closed_sources", "evidence", "verification", "sourcing_note", "confidence",
    "references", "weekly_section", "deep_dive", "deep_dive_category", "org_triage",
    "classification", "watchlist_hit", "actions", "updates", "migrated_from", "nexus",
]
META_KEYS = {"slug", "date", "id", "path", "body"}
UNION_LIST_FIELDS = (
    "tags", "regions", "sectors", "entities", "techniques", "affected_products",
    "references", "actions",
)
# The redundant opener v3 update bodies carried (the styled lead already cited it).
_BODY_UPDATE_PREFIX_RE = re.compile(
    r"^\s*\*\*\s*(?:update|correction)\b[^*\n]*?\b(?:originally|covered)\b[^*\n]*?\*\*\s*[:\-–—]*\s*",
    re.IGNORECASE,
)


def _frontmatter_of(entry: dict) -> dict:
    fm = {k: v for k, v in entry.items() if k not in META_KEYS}
    # Drop defaults that the original file did not carry? No — keep what the
    # loader produced; every entry file carries the full key set anyway.
    return fm


def _ordered(fm: dict) -> dict:
    out = {}
    for k in CANONICAL_ORDER:
        if k in fm:
            out[k] = fm[k]
    for k, v in fm.items():
        if k not in out:
            out[k] = v
    return out


def _union(a: list, b: list) -> list:
    out = list(a or [])
    for x in b or []:
        if x not in out:
            out.append(x)
    return out


def _strip_update_prefix(body: str) -> str:
    stripped = _BODY_UPDATE_PREFIX_RE.sub("", body or "", count=1).lstrip()
    if stripped and stripped != (body or "").lstrip() and stripped[0].islower():
        stripped = stripped[0].upper() + stripped[1:]
    return stripped.strip()


def _root_of(eid: str, by_id: dict) -> str:
    seen = set()
    cur = eid
    while cur in by_id and by_id[cur].get("update_of") and cur not in seen:
        seen.add(cur)
        nxt = str(by_id[cur]["update_of"])
        if nxt not in by_id:
            break
        cur = nxt
    return cur


def _update_type(update: dict) -> str:
    text = f"{update.get('title') or ''} {update.get('headline') or ''}"
    return "correction" if re.search(r"\bcorrection\b", text, re.IGNORECASE) else "update"


def fold(root: dict, upd: dict) -> dict:
    """Merge `upd` into `root` (in place) and return the changelog record."""
    before = {k: json.dumps(root.get(k), sort_keys=True) for k in root if k not in META_KEYS}
    at = str(upd["discovered_at"])
    last_at = root.get("updated_at") or root["discovered_at"]
    if at <= str(last_at):
        raise SystemExit(
            f"{upd['id']}: discovered_at {at} is not later than the root's last activity "
            f"{last_at} ({root['id']}) — chains must run forward in time")

    # --- per-CVE records: the update's record is the newer truth --------
    cves = list(root.get("cves") or [])
    idx = {str(c.get("id")): i for i, c in enumerate(cves) if isinstance(c, dict)}
    for c in upd.get("cves") or []:
        if not isinstance(c, dict):
            continue
        cid = str(c.get("id"))
        if cid in idx:
            cves[idx[cid]] = c
        else:
            cves.append(c)
            idx[cid] = len(cves) - 1
    root["cves"] = cves

    # --- sources / evidence / closed sources: append new ones -----------
    have_urls = {str(s.get("url")) for s in root.get("sources") or [] if isinstance(s, dict)}
    for s in upd.get("sources") or []:
        if isinstance(s, dict) and str(s.get("url")) not in have_urls:
            root.setdefault("sources", []).append(s)
            have_urls.add(str(s.get("url")))
    have_q = {str(ev.get("quote")) for ev in root.get("evidence") or [] if isinstance(ev, dict)}
    for ev in upd.get("evidence") or []:
        if isinstance(ev, dict) and str(ev.get("quote")) not in have_q:
            root.setdefault("evidence", []).append(ev)
            have_q.add(str(ev.get("quote")))
    for c in upd.get("closed_sources") or []:
        if c not in (root.get("closed_sources") or []):
            root.setdefault("closed_sources", []).append(c)

    # --- ordered unions ---------------------------------------------------
    for f in UNION_LIST_FIELDS:
        extra = [x for x in (upd.get(f) or []) if not (f == "references" and x == root["id"])]
        root[f] = _union(root.get(f) or [], extra)
    root["references"] = [r for r in root.get("references") or [] if r != root["id"]]

    # --- priority escalation ------------------------------------------------
    rank = {p: i for i, p in enumerate(cm.PRIORITIES)}
    if rank.get(upd.get("priority"), 9) < rank.get(root.get("priority"), 9):
        root["priority"] = upd["priority"]
        if upd["priority"] == "critical":
            root["immediate_action"] = upd.get("immediate_action")
    if root.get("priority") != "critical":
        root["immediate_action"] = None
    if upd.get("watchlist_hit"):
        root["watchlist_hit"] = True

    changed = sorted(
        k for k in root if k not in META_KEYS and k in before
        and json.dumps(root.get(k), sort_keys=True) != before[k]
    ) + ["body"]

    # --- body section --------------------------------------------------------
    rtype = _update_type(upd)
    section_body = _strip_update_prefix(upd.get("body") or "")
    if not section_body:
        section_body = str(upd.get("summary") or "").strip()
    root["body"] = (
        (root.get("body") or "").rstrip() + "\n\n"
        + cm.update_section_heading(rtype, at) + "\n\n" + section_body + "\n"
    )

    record = {
        "at": at,
        "run_id": upd.get("run_id"),
        "type": rtype,
        "summary": " ".join(str(upd.get("summary") or "").split()),
        "fields": changed,
        "merged_from": upd["id"],
    }
    root.setdefault("updates", []).append(record)
    root["updated_at"] = at
    return record


def write_entry(entry: dict, root_dir: Path) -> None:
    fm = _ordered(_frontmatter_of(entry))
    fm.pop("update_of", None)
    path = root_dir / "entries" / entry["date"] / f"{entry['slug']}.md"
    path.write_text(cm.compose_frontmatter_doc(fm, entry["body"]), encoding="utf-8")


def repoint_references_textually(path: Path, mapping: dict, self_id: str) -> bool:
    """Re-point `references[]` list items in an entry FILE without
    re-serialising its frontmatter (keeps the diff to the changed lines).
    Returns True when the file changed."""
    text = path.read_text(encoding="utf-8")
    fm_text, body = cm.split_frontmatter(text)
    lines = fm_text.split("\n")
    out: list = []
    i = 0
    changed = False
    while i < len(lines):
        line = lines[i]
        out.append(line)
        i += 1
        m_inline = re.match(r"^references:\s*\[(.*)\]\s*$", line)
        if m_inline:
            items = [x.strip().strip('"').strip("'") for x in m_inline.group(1).split(",") if x.strip()]
            new_items: list = []
            for it in items:
                tgt = mapping.get(it, it)
                if tgt != self_id and tgt not in new_items:
                    new_items.append(tgt)
            if new_items != items:
                changed = True
                quoted = '"' in m_inline.group(1)
                out[-1] = "references: [" + ", ".join(
                    (f'"{x}"' if quoted else x) for x in new_items) + "]"
            continue
        if re.match(r"^references:\s*$", line):
            block: list = []
            while i < len(lines) and re.match(r"^\s+- ", lines[i]):
                block.append(lines[i])
                i += 1
            seen: list = []
            new_block: list = []
            for bl in block:
                m = re.match(r'^(\s+- )"?([^"\s]+)"?\s*$', bl)
                if not m:
                    new_block.append(bl)
                    continue
                tgt = mapping.get(m.group(2), m.group(2))
                if tgt == self_id or tgt in seen:
                    changed = True
                    continue
                seen.append(tgt)
                if tgt != m.group(2):
                    changed = True
                    bl = f'{m.group(1)}"{tgt}"' if '"' in bl else f"{m.group(1)}{tgt}"
                new_block.append(bl)
            if not new_block:
                out[-1] = "references: []"
                changed = True
            out.extend(new_block)
    if changed:
        path.write_text("---\n" + "\n".join(out) + "\n---\n\n" + body.strip() + "\n", encoding="utf-8")
    return changed


def repoint_registry(reg_path: Path, mapping: dict, dry_run: bool) -> int:
    text = reg_path.read_text(encoding="utf-8")
    n = 0
    for old, new in mapping.items():
        pat = re.compile(r'(source:\s*")' + re.escape(old) + r'(")')
        text, k = pat.subn(r"\g<1>" + new + r"\g<2>", text)
        n += k
    if n and not dry_run:
        reg_path.write_text(text, encoding="utf-8")
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true", help="print the plan, write nothing")
    ap.add_argument("--root", default=None, help="content root (default: repo root)")
    args = ap.parse_args()
    root_dir = Path(args.root).resolve() if args.root else ROOT

    entries = cm.collect_entries(root_dir / "entries", root=root_dir)
    by_id = {e["id"]: e for e in entries}
    updates = [e for e in entries if e.get("update_of")]
    if not updates:
        print("no update_of entries — nothing to migrate")
        return 0

    mapping: dict = {}          # folded update id -> root id
    touched: dict = {}          # root id -> root entry (mutated)
    plan: list = []
    for u in updates:           # collect_entries is discovered_at-ascending
        rid = _root_of(u["id"], by_id)
        if rid == u["id"] or rid not in by_id:
            raise SystemExit(f"{u['id']}: update_of chain does not resolve to an existing root")
        root = by_id[rid]
        rec = fold(root, u)
        mapping[u["id"]] = rid
        touched[rid] = root
        plan.append({"update": u["id"], "root": rid, "type": rec["type"], "at": rec["at"],
                     "fields": rec["fields"]})

    # Re-point references[] on every entry. Folded roots are re-serialised
    # anyway (their dict is mutated); untouched entries get a textual edit of
    # the reference lines only, so their diff shows nothing but the re-point.
    ref_changed = 0
    ref_textual: list = []
    for e in entries:
        if e["id"] in mapping:
            continue
        refs = e.get("references") or []
        new_refs: list = []
        for r in refs:
            tgt = mapping.get(str(r), str(r))
            if tgt != e["id"] and tgt not in new_refs:
                new_refs.append(tgt)
        if new_refs != refs:
            e["references"] = new_refs
            ref_changed += 1
            if e["id"] in touched:
                touched[e["id"]] = e
            else:
                ref_textual.append(e)

    print(f"plan: fold {len(updates)} update entries into {len({p['root'] for p in plan})} roots; "
          f"{ref_changed} entries re-pointed via references[]; "
          f"types: {sum(1 for p in plan if p['type'] == 'correction')} correction / "
          f"{sum(1 for p in plan if p['type'] == 'update')} update")
    for p in plan[:8]:
        print(f"  {p['update']}  →  {p['root']}  [{p['type']} @ {p['at']}] fields={p['fields']}")
    if len(plan) > 8:
        print(f"  … {len(plan) - 8} more")

    reg_path = root_dir / "entities" / "registry.yaml"
    n_rel = repoint_registry(reg_path, mapping, dry_run=True) if reg_path.exists() else 0
    print(f"registry: {n_rel} relations[].source value(s) re-pointed")

    if args.dry_run:
        print("dry run — nothing written")
        return 0

    # Validate every mutated root before writing anything.
    taxonomy = cm.parse_taxonomy(root_dir / "site" / "taxonomy.yaml") if (root_dir / "site" / "taxonomy.yaml").exists() else cm.parse_taxonomy()
    registry = cm.load_registry(reg_path) if reg_path.exists() else {}
    errs: list = []
    for e in touched.values():
        e2 = dict(e)
        e2.pop("update_of", None)
        errs.extend(cm.validate_entry(e2, taxonomy, registry_keys=set(registry)))
    if errs:
        print("VALIDATION FAILED on migrated roots — nothing written:")
        for x in errs[:40]:
            print("  ·", x)
        return 1

    for e in touched.values():
        write_entry(e, root_dir)
    for e in ref_textual:
        repoint_references_textually(root_dir / "entries" / e["date"] / f"{e['slug']}.md",
                                     mapping, e["id"])
    if reg_path.exists():
        repoint_registry(reg_path, mapping, dry_run=False)
    in_git = (root_dir / ".git").exists() or subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"], cwd=root_dir,
        capture_output=True, text=True).returncode == 0
    removed = 0
    for old in mapping:
        path = root_dir / "entries" / f"{old}.md"
        if not path.exists():
            continue
        if in_git:
            subprocess.run(["git", "rm", "-q", "--", str(path.relative_to(root_dir))],
                           cwd=root_dir, check=True)
        else:
            path.unlink()
        removed += 1
    report_dir = root_dir / "work" / "migration-v4-updates"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "report.json").write_text(json.dumps({
        "folded": plan, "mapping": mapping,
        "roots_rewritten": sorted(touched), "references_repointed": sorted(e["id"] for e in ref_textual),
        "registry_sources_repointed": n_rel,
    }, indent=1, sort_keys=True), encoding="utf-8")
    print(f"written: {len(touched)} entries rewritten, {removed} update files removed, "
          f"report → {report_dir / 'report.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
