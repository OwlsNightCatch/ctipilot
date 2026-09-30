#!/usr/bin/env python3
"""Structured three-way merge for the pipeline's shared state files.

Every fire, every audit and every interactive session edits the same handful
of shared files, and two of them racing is normal (an audit overlapping the
morning intel fire, an operator session merging mid-run). Git's line merge
conflicts on these files whenever both sides appended near each other, and
the historical fallback, `git checkout --ours` / `--theirs` on the whole
file, silently discarded the other side's work: the CVE records a concurrent
fire added, the entities it registered (leaving its entries pointing at keys
that no longer exist), the source-recipe fixes it made. This tool replaces
that fallback with a merge that understands the records inside each file.

    python3 tools/merge_state.py resolve          # after a conflicted `git merge`
    python3 tools/merge_state.py merge <path> <base> <ours> <theirs> [-o OUT]
    python3 tools/merge_state.py --selftest

`resolve` walks the index's conflicted paths, merges every path it knows
from the three index stages (:1 base, :2 ours, :3 theirs), writes the result
and `git add`s it. It exits 0 when every conflicted path is now resolved and
1 when any path remains (an unknown path, or a known path whose merge could
not be proven sound), printing the leftovers, so a caller can abort loudly
instead of guessing.

Record semantics (keys are permanent, lists are append-mostly):

- state/cves_seen.json   union by CVE `id`; first_seen = min, last_seen = max,
                         a text field changed on one side wins; a record one
                         side removed stays removed unless the other side
                         changed it.
- sources/sources.json   per-source, per-field three-way merge by `id`;
                         `notes` (append-only) keeps both sides' appended
                         text; dates take the later value.
- state/source_health.json  regenerated wholesale by its tool: the newer
                         snapshot (by `last_updated`) wins, histories are
                         unioned by `fetched_at` up to `history_cap`.
- entities/registry.yaml block-level merge by entity `key`; both sides'
                         new entities survive; an entity edited on both sides
                         is line-merged, and if that conflicts the edit
                         with more aliases/relations wins and the loss is
                         reported. The result must parse and validate.
- state/coverage_backlog.md  row-level merge; a row struck on either side is
                         struck; an open row edited on both sides keeps the
                         longer (notes are appended, never rewritten).

Stdlib only: this runs inside the routine container and on a bare GitHub
runner (`.github/workflows/auto-merge-claude.yml`).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "site"))

KNOWN_PATHS = (
    "state/cves_seen.json",
    "sources/sources.json",
    "state/source_health.json",
    "entities/registry.yaml",
    "state/coverage_backlog.md",
)

_MISSING = object()


class MergeError(RuntimeError):
    """A merge that cannot be proven sound; the caller must not guess."""


# ---------------------------------------------------------------------------
# JSON helpers
# ---------------------------------------------------------------------------

def _json_style(text: str) -> dict:
    """Infer the dump flags from a live file (the canonical format has
    flipped before, so it is read, never remembered)."""
    lines = text.splitlines()
    indent = 1
    for ln in lines[1:]:
        stripped = ln.lstrip(" ")
        if stripped:
            indent = (len(ln) - len(stripped)) or None
            break
    ensure_ascii = not any(ord(ch) > 127 for ch in text)
    # Key order is preserved, never re-sorted: the merged records keep ours'
    # field order (new fields from theirs append), so an untouched record
    # dumps byte-identical and the diff shows only what the merge changed.
    return {
        "indent": indent,
        "ensure_ascii": ensure_ascii,
        "trailing_newline": text.endswith("\n"),
    }


def _json_dump(obj, style: dict) -> str:
    out = json.dumps(obj, indent=style["indent"], ensure_ascii=style["ensure_ascii"])
    return out + ("\n" if style["trailing_newline"] else "")


def _load_json(text: str | None, label: str):
    if text is None or not text.strip():
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise MergeError(f"{label}: not valid JSON ({exc})") from exc


def _pick3(base, ours, theirs, prefer="ours"):
    """Scalar three-way pick: the side that moved wins; both moved → prefer."""
    if ours == theirs:
        return ours
    if ours == base:
        return theirs
    if theirs == base:
        return ours
    return ours if prefer == "ours" else theirs


def _merge_append_only_text(base: str, ours: str, theirs: str) -> str:
    """`notes`-style append-only strings: keep both sides' appended tails."""
    base = base or ""
    ours = ours or ""
    theirs = theirs or ""
    if ours == theirs:
        return ours
    if ours.startswith(theirs):
        return ours
    if theirs.startswith(ours):
        return theirs
    if ours.startswith(base) and theirs.startswith(base):
        tail_o = ours[len(base):]
        tail_t = theirs[len(base):]
        return base + tail_o + tail_t
    # One side rewrote history (should not happen for append-only text):
    # keep ours and append whatever of theirs is not already in it.
    return ours if theirs in ours else ours + " | " + theirs


_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")


def _later(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if isinstance(a, str) and isinstance(b, str) and _DATE_RE.match(a) and _DATE_RE.match(b):
        return max(a, b)
    return a


def _earlier(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if isinstance(a, str) and isinstance(b, str) and _DATE_RE.match(a) and _DATE_RE.match(b):
        return min(a, b)
    return a


def _merge_records_by_id(base_list, ours_list, theirs_list, merge_record, id_key="id",
                         keep_sorted=False):
    """Three-way merge of two lists of dict records keyed by `id_key`."""
    base_map = {r.get(id_key): r for r in (base_list or []) if isinstance(r, dict)}
    ours_map = {r.get(id_key): r for r in (ours_list or []) if isinstance(r, dict)}
    theirs_map = {r.get(id_key): r for r in (theirs_list or []) if isinstance(r, dict)}
    result_ids: list = []
    for rid in [r.get(id_key) for r in (ours_list or []) if isinstance(r, dict)]:
        if rid in theirs_map:
            result_ids.append(rid)
        elif rid in base_map:
            # theirs deleted it: stays deleted unless ours changed it
            if ours_map[rid] != base_map[rid]:
                result_ids.append(rid)
        else:
            result_ids.append(rid)  # ours added it
    seen = set(result_ids)
    for rid in [r.get(id_key) for r in (theirs_list or []) if isinstance(r, dict)]:
        if rid in seen:
            continue
        if rid in base_map:
            # ours deleted it: stays deleted unless theirs changed it
            if theirs_map[rid] != base_map[rid]:
                result_ids.append(rid)
                seen.add(rid)
        else:
            result_ids.append(rid)
            seen.add(rid)
    merged = []
    for rid in result_ids:
        o = ours_map.get(rid)
        t = theirs_map.get(rid)
        b = base_map.get(rid)
        if o is None:
            merged.append(t)
        elif t is None:
            merged.append(o)
        else:
            merged.append(merge_record(b or {}, o, t))
    if keep_sorted:
        merged.sort(key=lambda r: str(r.get(id_key)))
    return merged


def _merge_dict_fields(base: dict, ours: dict, theirs: dict, field_rules: dict) -> dict:
    out = {}
    keys = list(ours.keys()) + [k for k in theirs.keys() if k not in ours]
    for k in keys:
        b = base.get(k, _MISSING)
        o = ours.get(k, _MISSING)
        t = theirs.get(k, _MISSING)
        if o is _MISSING:
            if b is not _MISSING and t == b:
                continue  # ours deleted an unchanged field
            out[k] = t
            continue
        if t is _MISSING:
            if b is not _MISSING and o == b:
                continue  # theirs deleted an unchanged field
            out[k] = o
            continue
        rule = field_rules.get(k)
        b_val = None if b is _MISSING else b
        if o == t:
            out[k] = o
        elif rule == "append_text":
            out[k] = _merge_append_only_text(b_val, o, t)
        elif rule == "later":
            out[k] = _later(o, t)
        elif rule == "earlier":
            out[k] = _earlier(o, t)
        else:
            out[k] = _pick3(b_val, o, t)
    return out


# ---------------------------------------------------------------------------
# Per-file mergers
# ---------------------------------------------------------------------------

def merge_cves_seen(base_text, ours_text, theirs_text) -> str:
    base = _load_json(base_text, "cves_seen base") or {}
    ours = _load_json(ours_text, "cves_seen ours")
    theirs = _load_json(theirs_text, "cves_seen theirs")
    if ours is None or theirs is None:
        raise MergeError("cves_seen: one side is missing or empty")
    rules = {"first_seen": "earlier", "last_seen": "later"}

    def merge_record(b, o, t):
        rec = _merge_dict_fields(b, o, t, rules)
        # A text field both sides changed: the fresher sighting wins.
        for field in ("title", "primary_source_url"):
            bo, oo, to = b.get(field), o.get(field), t.get(field)
            if oo != to and oo != bo and to != bo:
                rec[field] = to if (t.get("last_seen") or "") > (o.get("last_seen") or "") else oo
        return rec

    ours_ids = [r.get("id") for r in ours.get("cves", [])]
    keep_sorted = ours_ids == sorted(ours_ids)
    merged = dict(_merge_dict_fields(base, ours, theirs, {"last_updated": "later"}))
    merged["cves"] = _merge_records_by_id(base.get("cves"), ours.get("cves"), theirs.get("cves"),
                                          merge_record, keep_sorted=keep_sorted)
    return _json_dump(merged, _json_style(ours_text))


def merge_sources(base_text, ours_text, theirs_text) -> str:
    base = _load_json(base_text, "sources base") or {}
    ours = _load_json(ours_text, "sources ours")
    theirs = _load_json(theirs_text, "sources theirs")
    if ours is None or theirs is None:
        raise MergeError("sources: one side is missing or empty")
    rules = {"notes": "append_text", "last_successful_fetch": "later", "added": "earlier"}

    def merge_record(b, o, t):
        return _merge_dict_fields(b, o, t, rules)

    ours_ids = [r.get("id") for r in ours.get("sources", [])]
    keep_sorted = ours_ids == sorted(ours_ids)
    merged = dict(_merge_dict_fields(base, ours, theirs, {"last_updated": "later"}))
    merged["sources"] = _merge_records_by_id(base.get("sources"), ours.get("sources"),
                                             theirs.get("sources"), merge_record,
                                             keep_sorted=keep_sorted)
    return _json_dump(merged, _json_style(ours_text))


def merge_source_health(base_text, ours_text, theirs_text) -> str:
    ours = _load_json(ours_text, "source_health ours")
    theirs = _load_json(theirs_text, "source_health theirs")
    if ours is None or theirs is None:
        raise MergeError("source_health: one side is missing or empty")
    newer, older = (theirs, ours) if (theirs.get("last_updated") or "") > (ours.get("last_updated") or "") else (ours, theirs)
    merged = dict(newer)
    runs = {}
    for snap in (older.get("runs") or []) + (newer.get("runs") or []):
        if isinstance(snap, dict) and snap.get("fetched_at"):
            runs[snap["fetched_at"]] = snap
    cap = newer.get("history_cap") or older.get("history_cap") or 12
    merged["runs"] = [runs[k] for k in sorted(runs)][-int(cap):]
    return _json_dump(merged, _json_style(ours_text))


# --- registry (block-level) --------------------------------------------------

_KEY_LINE = re.compile(r'^  - key:\s*"?([^"\s]+)"?\s*$')


def _registry_items(text: str) -> list:
    """Split the registry into ordered items: (item_key, text).

    Entity blocks are keyed `E:<key>`; every other run of lines (header,
    comments, blank separators) is keyed by its text plus an occurrence
    counter so identical separators stay distinct."""
    lines = text.splitlines(keepends=True)
    items: list = []
    buf: list = []
    cur_key = None
    other_counts: dict = {}

    def flush():
        nonlocal buf, cur_key
        if not buf:
            return
        chunk = "".join(buf)
        if cur_key:
            items.append(("E:" + cur_key, chunk))
        else:
            n = other_counts.get(chunk, 0)
            other_counts[chunk] = n + 1
            items.append((f"O:{n}:{chunk}", chunk))
        buf = []
        cur_key = None

    for ln in lines:
        m = _KEY_LINE.match(ln.rstrip("\n"))
        if m:
            flush()
            cur_key = m.group(1)
            buf.append(ln)
            continue
        if cur_key and (ln.startswith("    ") ):
            buf.append(ln)
            continue
        if cur_key:
            flush()
        buf.append(ln)
        # comment / blank / header lines accumulate into one "other" item
        # until the next entity block starts
    flush()
    # merge consecutive "other" items produced line by line into one item
    merged: list = []
    for key, chunk in items:
        if key.startswith("O:") and merged and merged[-1][0].startswith("O:"):
            prev_key, prev_chunk = merged.pop()
            joined = prev_chunk + chunk
            merged.append(("O:" + joined, joined))
        else:
            merged.append((key, chunk))
    # re-key "other" items with occurrence counters after joining
    out: list = []
    counts: dict = {}
    for key, chunk in merged:
        if key.startswith("O:"):
            n = counts.get(chunk, 0)
            counts[chunk] = n + 1
            out.append((f"O:{n}:{chunk}", chunk))
        else:
            out.append((key, chunk))
    return out


def _git_merge_file(base: str, ours: str, theirs: str) -> tuple[str, bool]:
    with tempfile.TemporaryDirectory() as td:
        paths = []
        for name, content in (("ours", ours), ("base", base), ("theirs", theirs)):
            p = Path(td) / name
            p.write_text(content, encoding="utf-8")
            paths.append(str(p))
        proc = subprocess.run(["git", "merge-file", "-p", *paths], capture_output=True, text=True)
        return proc.stdout, proc.returncode == 0


def _entity_weight(block: str) -> int:
    return block.count("\n")


def merge_registry(base_text, ours_text, theirs_text, report: list | None = None) -> str:
    report = report if report is not None else []
    base_items = _registry_items(base_text or "")
    ours_items = _registry_items(ours_text)
    theirs_items = _registry_items(theirs_text)
    base_map = dict(base_items)
    ours_map = dict(ours_items)
    theirs_map = dict(theirs_items)

    result: list = []  # list of keys in order
    for key, _ in ours_items:
        if key in theirs_map:
            result.append(key)
        elif key in base_map:
            if ours_map[key] != base_map[key]:
                result.append(key)  # theirs deleted, ours edited: keep
        else:
            result.append(key)
    present = set(result)
    theirs_order = [k for k, _ in theirs_items]
    for idx, key in enumerate(theirs_order):
        if key in present:
            continue
        if key in base_map and theirs_map[key] == base_map[key]:
            continue  # ours deleted it and theirs never touched it
        # insert after the nearest preceding theirs item already in result
        insert_at = None
        for prev in reversed(theirs_order[:idx]):
            if prev in present:
                insert_at = result.index(prev) + 1
                break
        if insert_at is None:
            insert_at = len(result)
        # Both sides appending after the same anchor: ours' additions first.
        while (insert_at < len(result) and result[insert_at] not in base_map
               and result[insert_at] not in theirs_map):
            insert_at += 1
        result.insert(insert_at, key)
        present.add(key)

    chunks = []
    for key in result:
        o = ours_map.get(key)
        t = theirs_map.get(key)
        b = base_map.get(key)
        if o is None:
            chunks.append(t)
            continue
        if t is None or o == t or t == b:
            chunks.append(o)
            continue
        if o == b:
            chunks.append(t)
            continue
        merged, clean = _git_merge_file(b or "", o, t)
        if clean:
            chunks.append(merged)
            continue
        keep, lose, side = (t, o, "theirs") if _entity_weight(t) > _entity_weight(o) else (o, t, "ours")
        report.append(f"registry: {key[2:]} edited on both sides with conflicting lines; kept {side}'s block")
        chunks.append(keep)
    text = "".join(chunks)
    _validate_registry_text(text)
    return text


def _validate_registry_text(text: str) -> None:
    try:
        import content_model  # type: ignore
    except Exception:  # noqa: BLE001 — validation needs the shared parser
        return
    try:
        doc = content_model.parse_yaml_subset(text)
    except Exception as exc:  # noqa: BLE001
        raise MergeError(f"registry: merged document does not parse ({exc})") from exc
    ents = (doc or {}).get("entities") or []
    keys = [e.get("key") for e in ents if isinstance(e, dict)]
    dupes = {k for k in keys if keys.count(k) > 1}
    if dupes:
        raise MergeError(f"registry: merged document repeats keys {sorted(dupes)[:5]}")
    registry = {e["key"]: e for e in ents if isinstance(e, dict) and e.get("key")}
    errors = [e for e in content_model.validate_registry(registry) if "collid" in e.lower() or "tombstone" in e.lower()]
    if errors:
        raise MergeError("registry: merged document fails validation: " + "; ".join(errors[:3]))


# --- coverage backlog (row-level) --------------------------------------------

def _backlog_parse(text: str):
    """→ (preamble_lines, open_header_lines, open_rows, struck_header_lines, struck_rows, tail_lines)."""
    lines = (text or "").splitlines(keepends=True)
    sections = {"pre": [], "open_hdr": [], "open": [], "struck_hdr": [], "struck": [], "tail": []}
    state = "pre"
    for ln in lines:
        s = ln.strip()
        is_row = s.startswith("| 20")
        if s.startswith("## Open"):
            state = "open_hdr"
        elif s.startswith("## Struck"):
            state = "struck_hdr"
        elif state == "open_hdr" and is_row:
            state = "open"
        elif state == "struck_hdr" and is_row:
            state = "struck"
        elif state == "struck" and not is_row:
            state = "tail"
        sections[state].append(ln)
    return sections


def _row_key(row: str) -> str:
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    title = ""
    for c in cells[1:4]:
        m = re.search(r"\*\*(.+?)\*\*", c)
        if m:
            title = m.group(1)
            break
    if not title and len(cells) > 1:
        title = cells[1][:120]
    return re.sub(r"\W+", " ", title).strip().lower()[:160]


def merge_backlog(base_text, ours_text, theirs_text) -> str:
    b = _backlog_parse(base_text or "")
    o = _backlog_parse(ours_text)
    t = _backlog_parse(theirs_text)

    def rows(sec):
        return [r for r in sec if r.strip().startswith("| 20")]

    struck: dict = {}
    for r in rows(o["struck"]) + rows(t["struck"]):
        struck.setdefault(_row_key(r), r)
    base_open = {_row_key(r): r for r in rows(b["open"])}
    o_open = {_row_key(r): r for r in rows(o["open"])}
    t_open = {_row_key(r): r for r in rows(t["open"])}
    open_keys = [k for k in o_open] + [k for k in t_open if k not in o_open]
    open_rows = []
    for k in open_keys:
        if k in struck:
            continue
        ov, tv, bv = o_open.get(k), t_open.get(k), base_open.get(k)
        if ov is None:
            if bv is not None and tv == bv:
                continue  # ours removed an untouched row
            open_rows.append(tv)
        elif tv is None:
            if bv is not None and ov == bv:
                continue  # theirs removed an untouched row
            open_rows.append(ov)
        elif ov == tv or tv == bv:
            open_rows.append(ov)
        elif ov == bv:
            open_rows.append(tv)
        else:
            open_rows.append(ov if len(ov) >= len(tv) else tv)
    struck_rows = list(struck.values())
    o_struck_keys = [_row_key(r) for r in rows(o["struck"])]
    struck_rows.sort(key=lambda r: (o_struck_keys.index(_row_key(r)) if _row_key(r) in o_struck_keys else len(o_struck_keys)))
    open_trailer = [ln for ln in o["open"] if not ln.strip().startswith("| 20")]
    out = "".join(o["pre"]) + "".join(o["open_hdr"]) + "".join(open_rows) + "".join(open_trailer)
    out += "".join(o["struck_hdr"]) + "".join(struck_rows) + "".join(o["tail"])
    return out


MERGERS = {
    "state/cves_seen.json": merge_cves_seen,
    "sources/sources.json": merge_sources,
    "state/source_health.json": merge_source_health,
    "entities/registry.yaml": merge_registry,
    "state/coverage_backlog.md": merge_backlog,
}


def merge_path(path: str, base: str | None, ours: str, theirs: str, report: list) -> str:
    fn = MERGERS.get(path)
    if fn is None:
        raise MergeError(f"{path}: no structured merger for this path")
    if fn is merge_registry:
        return fn(base, ours, theirs, report)
    return fn(base, ours, theirs)


# ---------------------------------------------------------------------------
# git integration
# ---------------------------------------------------------------------------

def _git(*args, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=check)


def _stage(path: str, n: int) -> str | None:
    proc = _git("show", f":{n}:{path}", check=False)
    return proc.stdout if proc.returncode == 0 else None


def cmd_resolve() -> int:
    conflicted = [p for p in _git("diff", "--name-only", "--diff-filter=U").stdout.splitlines() if p]
    if not conflicted:
        print("merge_state: no conflicted paths")
        return 0
    unresolved = []
    for path in conflicted:
        if path not in MERGERS:
            unresolved.append(path)
            continue
        base, ours, theirs = _stage(path, 1), _stage(path, 2), _stage(path, 3)
        if ours is None or theirs is None:
            unresolved.append(path)
            print(f"merge_state: {path}: a side is missing (added/deleted conflict); left unresolved")
            continue
        report: list = []
        try:
            merged = merge_path(path, base, ours, theirs, report)
        except MergeError as exc:
            unresolved.append(path)
            print(f"merge_state: {path}: {exc}; left unresolved")
            continue
        (ROOT / path).write_text(merged, encoding="utf-8")
        _git("add", "--", path)
        for line in report:
            print(f"merge_state: NOTE {line}")
        print(f"merge_state: {path}: merged structurally")
    if unresolved:
        print("merge_state: unresolved paths:")
        for p in unresolved:
            print(f"  {p}")
        return 1
    return 0


def cmd_merge(path: str, base: str, ours: str, theirs: str, out: str | None) -> int:
    read = lambda p: Path(p).read_text(encoding="utf-8") if p and os.path.exists(p) else None  # noqa: E731
    report: list = []
    try:
        merged = merge_path(path, read(base), read(ours), read(theirs), report)
    except MergeError as exc:
        print(f"merge_state: {exc}", file=sys.stderr)
        return 1
    for line in report:
        print(f"merge_state: NOTE {line}", file=sys.stderr)
    if out:
        Path(out).write_text(merged, encoding="utf-8")
    else:
        sys.stdout.write(merged)
    return 0


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------

def _selftest() -> int:
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    # cves_seen: both sides add different CVEs, one bumps last_seen.
    base = {"cves": [{"id": "CVE-1", "first_seen": "2026-01-01", "last_seen": "2026-01-01", "title": "a", "primary_source_url": "u"}],
            "last_updated": "2026-01-01", "schema_version": 1}
    ours = json.loads(json.dumps(base))
    ours["cves"].append({"id": "CVE-2", "first_seen": "2026-01-02", "last_seen": "2026-01-02", "title": "b", "primary_source_url": "u2"})
    ours["cves"][0]["last_seen"] = "2026-01-03"
    theirs = json.loads(json.dumps(base))
    theirs["cves"].append({"id": "CVE-3", "first_seen": "2026-01-02", "last_seen": "2026-01-02", "title": "c", "primary_source_url": "u3"})
    theirs["cves"][0]["title"] = "a-better"
    d = lambda o: json.dumps(o, indent=1, sort_keys=True) + "\n"  # noqa: E731
    merged = json.loads(merge_cves_seen(d(base), d(ours), d(theirs)))
    ids = [c["id"] for c in merged["cves"]]
    check(ids == ["CVE-1", "CVE-2", "CVE-3"], f"cves union/sort: {ids}")
    check(merged["cves"][0]["last_seen"] == "2026-01-03", "cves last_seen max")
    check(merged["cves"][0]["title"] == "a-better", "cves one-sided title change")
    # removal on one side, untouched on the other → removed
    ours2 = json.loads(json.dumps(base)); ours2["cves"] = []
    merged2 = json.loads(merge_cves_seen(d(base), d(ours2), d(base)))
    check(merged2["cves"] == [], "cves one-sided removal")

    # sources: notes appended on both sides, date max, field changed on one side.
    sb = {"sources": [{"id": "s1", "notes": "n0", "last_successful_fetch": "2026-01-01", "url": "https://a"}], "last_updated": "x"}
    so = json.loads(json.dumps(sb)); so["sources"][0]["notes"] = "n0 | ours note"; so["sources"][0]["last_successful_fetch"] = "2026-01-05"
    st = json.loads(json.dumps(sb)); st["sources"][0]["notes"] = "n0 | theirs note"; st["sources"][0]["url"] = "https://b"
    st["sources"].append({"id": "s2", "notes": "", "url": "https://c"})
    ms = json.loads(merge_sources(d(sb), d(so), d(st)))
    s1 = ms["sources"][0]
    check(s1["notes"] == "n0 | ours note | theirs note", f"sources notes: {s1['notes']!r}")
    check(s1["last_successful_fetch"] == "2026-01-05", "sources date max")
    check(s1["url"] == "https://b", "sources one-sided url change")
    check([s["id"] for s in ms["sources"]] == ["s1", "s2"], "sources union")

    # registry: both sides add a different entity at the end; one side edits one.
    reg_base = 'schema: 1\nentities:\n  - key: "actor:a"\n    type: actor\n    name: "A"\n    aliases: []\n    first_seen: 2026-01-01\n'
    reg_ours = reg_base + '  - key: "actor:b"\n    type: actor\n    name: "B"\n    aliases: []\n    first_seen: 2026-01-02\n'
    reg_theirs = reg_base.replace('aliases: []', 'aliases: ["A1"]') + '  - key: "actor:c"\n    type: actor\n    name: "C"\n    aliases: []\n    first_seen: 2026-01-02\n'
    notes: list = []
    mr = merge_registry(reg_base, reg_ours, reg_theirs, notes)
    check('actor:b' in mr and 'actor:c' in mr, "registry union of new entities")
    check('aliases: ["A1"]' in mr, "registry one-sided edit kept")
    check(mr.index('actor:a') < mr.index('actor:b') < mr.index('actor:c'), "registry order")

    # backlog: ours strikes a row, theirs appends a note to another row and adds a row.
    hdr = "<!-- c -->\n\n## Open\n\n| Surfaced | By run | Item | Why | Primary | Event |\n|---|---|---|---|---|---|\n"
    r1 = "| 2026-01-01 | r1 | **Item one** | why | src | 2026-01-01 |\n"
    r2 = "| 2026-01-02 | r2 | **Item two** | why | src | 2026-01-02 |\n"
    r3 = "| 2026-01-03 | r3 | **Item three** | why | src | 2026-01-03 |\n"
    sh = "\n## Struck\n\n| Surfaced | Item | Resolution |\n|---|---|---|\n"
    s1r = "| 2026-01-01 | **Item one** | published as x |\n"
    bb = hdr + r1 + r2 + sh
    bo = hdr + r2 + sh + s1r
    bt = hdr + r1 + r2.replace("why", "why **note**") + r3 + sh
    mb = merge_backlog(bb, bo, bt)
    check("Item one** | why | src" not in mb.split("## Struck")[0], "backlog struck row leaves Open")
    check("why **note**" in mb and "Item three" in mb, "backlog note + new row kept")
    check(mb.count("Item one") == 1, "backlog struck row once")

    if failures:
        for f in failures:
            print("SELFTEST FAIL:", f)
        return 1
    print("merge_state selftest: all checks passed")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--selftest", action="store_true")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("resolve", help="merge every conflicted known path in the git index")
    m = sub.add_parser("merge", help="merge three versions of one known path")
    m.add_argument("path", choices=sorted(MERGERS))
    m.add_argument("base")
    m.add_argument("ours")
    m.add_argument("theirs")
    m.add_argument("-o", "--out")
    args = p.parse_args(argv)
    if args.selftest:
        return _selftest()
    if args.cmd == "resolve":
        return cmd_resolve()
    if args.cmd == "merge":
        return cmd_merge(args.path, args.base, args.ours, args.theirs, args.out)
    p.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
