#!/usr/bin/env python3
"""Fold duplicate entries of one finding into the surviving entry (v4.19).

One finding has exactly one entry for its whole life (docs/pipeline.md
§ Entry lifecycle). The v4.0 migration folded every `update_of` entry into
its root, but the store still holds duplicates it could not see: legacy
"UPDATE (originally covered …)" entries that never carried `update_of`, and
same-day twins the v2 brief migration split into a brief item and a deep
dive. A triage agent that looks a CVE up gets two or three entries that can
disagree (the 2026-09-30 audit found swapped exploitation statuses between
two CVE-2026-50751 twins). This tool performs the mechanical half of a fold;
the editorial half stays with the composer:

  1. The composer first brings the surviving entry to the current, verified
     state and writes ONE changelog record for this fire on it (usually an
     `improvement` or `correction`, with its section when the reader gains
     something). Material facts that only the duplicate carried are carried
     over with their citations; unverified legacy text is left behind.
  2. This tool then adds every folded id to that record's `merged_from`
     (a list), re-points `references[]` in every other entry and
     `relations[].source` in the entity registry from the duplicate to the
     survivor (an entry it re-points gets an internal record for this fire,
     or its existing record for this fire gains `references` in `fields`),
     and deletes the duplicate files (`git rm` in a checkout).
  3. `site/build.py` emits a redirect stub at each folded id's permalink, so
     old links keep working.

    python3 tools/fold_entries.py --run <run-id> --into <entry-id> <dup-id> [<dup-id> …] [--dry-run]

Refuses to run when the survivor lacks a record for --run, when a duplicate
is missing, or when a duplicate is the survivor. Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402

ENTRIES = ROOT / "entries"
REGISTRY = ROOT / "entities" / "registry.yaml"


def _path(eid: str) -> Path:
    return ENTRIES / f"{eid}.md"


def _split(text: str) -> tuple[str, str]:
    end = text.index("\n---", 4)
    return text[:end], text[end:]


def _record_span(lines: list[str], run_id: str) -> tuple[int, int] | None:
    """Line span [start, end) of the single updates[] record carrying run_id."""
    hits = [i for i, l in enumerate(lines) if l.strip() == f"run_id: {run_id}" and l.startswith("    ")]
    if len(hits) != 1:
        return None
    i = hits[0] - 1  # the "  - at:" line
    j = hits[0] + 1
    while j < len(lines) and lines[j].startswith("    "):
        j += 1
    return i, j


def _set_merged_from(text: str, run_id: str, ids: list[str]) -> str:
    fm, rest = _split(text)
    lines = fm.split("\n")
    span = _record_span(lines, run_id)
    if span is None:
        raise SystemExit(f"survivor has no single record for {run_id}: write it first")
    i, j = span
    rec = lines[i:j]
    existing: list[str] = []
    k = next((n for n, l in enumerate(rec) if l.startswith("    merged_from:")), None)
    if k is not None:
        raw = rec[k].split(":", 1)[1].strip()
        existing = [x.strip().strip('"') for x in raw.strip("[]").split(",") if x.strip()]
        del rec[k]
    merged = existing + [x for x in ids if x not in existing]
    rec.append("    merged_from: [" + ", ".join(merged) + "]")
    lines[i:j] = rec
    return "\n".join(lines) + rest


def _now_at(taken: set[str]) -> str:
    t = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    while t.strftime("%Y-%m-%dT%H:%M:%SZ") in taken:
        t += dt.timedelta(seconds=1)
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def _repoint_refs(text: str, mapping: dict[str, str], self_id: str, run_id: str) -> tuple[str, bool]:
    fm, rest = _split(text)
    changed = False

    def fix(m: re.Match) -> str:
        nonlocal changed
        old = m.group(0)
        new = old
        for dup, keep in mapping.items():
            new = new.replace(dup, keep)
        if new != old:
            changed = True
        return new

    # inline form references: [a, b]  or block form under "references:"
    lines = fm.split("\n")
    out = []
    in_refs = False
    seen: list[str] = []
    for l in lines:
        if l.startswith("references:"):
            in_refs = not l.strip().endswith("]") and l.strip() != "references: []"
            if not in_refs:
                vals = [x.strip().strip('"') for x in l.split(":", 1)[1].strip().strip("[]").split(",") if x.strip()]
                new = []
                for v in vals:
                    v2 = mapping.get(v, v)
                    if v2 != v:
                        changed = True
                    if v2 != self_id and v2 not in new:
                        new.append(v2)
                out.append("references: [" + ", ".join(f'"{v}"' for v in new) + "]" if new else "references: []")
                continue
            out.append(l)
            continue
        if in_refs:
            if l.startswith("  - "):
                v = l[4:].strip().strip('"')
                v2 = mapping.get(v, v)
                if v2 != v:
                    changed = True
                if v2 == self_id or v2 in seen:
                    changed = True
                    continue
                seen.append(v2)
                out.append(f"  - {v2}" if not l[4:].strip().startswith('"') else f'  - "{v2}"')
                continue
            in_refs = False
        out.append(l)
    if not changed:
        return text, False
    fm = "\n".join(out)
    if re.search(r"^references:\n(?!  - )", fm + "\n", re.MULTILINE):
        fm = re.sub(r"^references:$", "references: []", fm, count=1, flags=re.MULTILINE)
    lines = fm.split("\n")
    span = _record_span(lines, run_id)
    if span is not None:
        i, j = span
        for n in range(i, j):
            m = re.match(r"^    fields: \[(.*)\]$", lines[n])
            if m:
                fields = [f.strip() for f in m.group(1).split(",") if f.strip()]
                if "references" not in fields:
                    fields.append("references")
                lines[n] = "    fields: [" + ", ".join(fields) + "]"
        fm = "\n".join(lines)
    else:
        taken = set(re.findall(r'^  - at: "([^"]+)"', fm, re.MULTILINE))
        rec = [f'  - at: "{_now_at(taken)}"', f"    run_id: {run_id}", "    type: improvement",
               "    internal: true", "    summary: >",
               "      A referenced entry was folded into the surviving entry for the same finding; the",
               "      reference now points at the survivor.",
               "    fields: [references]"]
        if re.search(r"^updates: \[\]$", fm, re.MULTILINE):
            fm = re.sub(r"^updates: \[\]$", "updates:\n" + "\n".join(rec), fm, count=1, flags=re.MULTILINE)
        elif re.search(r"^updates:$", fm, re.MULTILINE):
            lines = fm.split("\n")
            s = lines.index("updates:")
            j = s + 1
            while j < len(lines) and (lines[j].startswith("  ") or not lines[j].strip()):
                j += 1
            lines[j:j] = rec
            fm = "\n".join(lines)
        else:
            fm = fm.rstrip("\n") + "\nupdates:\n" + "\n".join(rec)
    return fm + rest, True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run", required=True, help="the fire's run id (its record on the survivor carries merged_from)")
    ap.add_argument("--into", required=True, help="surviving entry id")
    ap.add_argument("dups", nargs="+", help="duplicate entry ids to fold")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    keep = a.into
    if not _path(keep).is_file():
        raise SystemExit(f"survivor {keep} not found")
    for d in a.dups:
        if d == keep:
            raise SystemExit("a duplicate cannot be the survivor")
        if not _path(d).is_file():
            raise SystemExit(f"duplicate {d} not found")
    mapping = {d: keep for d in a.dups}

    plan: list[str] = []
    text = _path(keep).read_text(encoding="utf-8")
    text = _set_merged_from(text, a.run, a.dups)
    text, _ = _repoint_refs(text, mapping, keep, a.run)
    writes = {_path(keep): text}
    plan.append(f"survivor {keep}: merged_from += {a.dups}")

    for p in sorted(ENTRIES.glob("*/*.md")):
        eid = f"{p.parent.name}/{p.stem}"
        if eid == keep or eid in mapping:
            continue
        t = p.read_text(encoding="utf-8")
        if not any(d in t for d in a.dups):
            continue
        t2, changed = _repoint_refs(t, mapping, eid, a.run)
        if changed:
            writes[p] = t2
            plan.append(f"references re-pointed in {eid}")
        elif any(d in t for d in a.dups):
            plan.append(f"NOTE: {eid} mentions a folded id outside references[] (body link?) — fix by hand")

    reg = REGISTRY.read_text(encoding="utf-8")
    reg2 = reg
    for d in a.dups:
        reg2 = re.sub(rf'(source:\s*"?){re.escape(d)}("?)', rf"\g<1>{keep}\g<2>", reg2)
    if reg2 != reg:
        writes[REGISTRY] = reg2
        plan.append("registry relations[].source re-pointed")

    for line in plan:
        print(line)
    if a.dry_run:
        print("dry run: nothing written")
        return 0
    for p, t in writes.items():
        p.write_text(t, encoding="utf-8")
    for d in a.dups:
        rel = str(_path(d).relative_to(ROOT))
        r = subprocess.run(["git", "rm", "-q", rel], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            _path(d).unlink()
        print(f"removed {rel}")
    for p in writes:
        if p.parent.parent == ENTRIES:
            e = cm.load_entry(p)
            errs = cm.validate_entry(e, cm.parse_taxonomy(), None)
            if errs:
                print(f"VALIDATION {e['id']}: {errs[:3]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
