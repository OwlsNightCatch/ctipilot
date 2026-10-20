#!/usr/bin/env python3
"""Append, amend or check one fire's changelog record on a published entry.

A finding has one entry for its whole life, and every change to it is a dated
`updates[]` record (docs/pipeline.md § Entry lifecycle). Writing that record by
hand is where fires slip: an `at` that is not strictly later than the previous
record, an `updated_at` moved by a correction, a section heading one second off
its record, a second record from the same fire, a `fields` list that misses a
changed key. The 2026-10-18 audit wrote two run-local helpers for this
(`add_record.py`, `resum.py`); this is their tested, run-agnostic successor.

    # append this fire's record (and, unless internal, its body section)
    python3 tools/entry_record.py add <entry-id> <update|correction|improvement> \\
        --run-id <run-id> --fields cves,body --summary-file s.txt [--section-file sec.md | --internal]

    # replace the summary / fields of THIS fire's own record before it is published
    python3 tools/entry_record.py amend <entry-id> --run-id <run-id> \\
        [--summary-file s.txt] [--fields cves,body | --add-fields tags]

    # the fields this fire changed against a base (default HEAD), as `fields` must name them
    python3 tools/entry_record.py diff <entry-id> --run-id <run-id> [--base <ref>]

`--summary TEXT` may replace `--summary-file`. The record's `at` is the current
UTC second, waiting out a clash with the previous record (`--at` overrides it,
for tests and same-minute retries). `updated_at` moves only for a non-internal
`update` record. The frontmatter is edited as text, so every other byte of the
file stays as it was, and the result is re-parsed with site/content_model.py.
`add` refuses a second record from the same fire (one record per fire per
entry: use `amend`), and `amend` refuses a record that is already on
origin/main (published records are append-only). Stdlib only.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402

TYPES = ("update", "correction", "improvement")
AT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
FIELD_RE = re.compile(r"^[a-z_][a-z0-9_]*$")


class RecordError(Exception):
    pass


def fold(text: str, indent: str, width: int = 100) -> list[str]:
    """Word-wrap a summary into folded-scalar lines (`summary: >`)."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(indent + cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(indent + cur)
    return lines


def entry_path(root: Path, entry_id: str) -> Path:
    eid = entry_id.removeprefix("entries/").removesuffix(".md")
    path = root / "entries" / f"{eid}.md"
    if not path.is_file():
        raise RecordError(f"no entry file {path}")
    return path


def parse_fields(raw: str | None) -> list[str]:
    fields = [f.strip() for f in (raw or "").split(",") if f.strip()]
    bad = [f for f in fields if not FIELD_RE.match(f)]
    if bad:
        raise RecordError(f"not a field name: {bad}")
    return list(dict.fromkeys(fields))


def read_summary(args) -> str | None:
    if getattr(args, "summary", None):
        text = args.summary
    elif getattr(args, "summary_file", None):
        text = Path(args.summary_file).read_text(encoding="utf-8")
    else:
        return None
    text = " ".join(text.split())
    if not text:
        raise RecordError("the summary is empty")
    return text


def _split(text: str) -> tuple[list[str], str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise RecordError("no frontmatter block")
    return m.group(1).split("\n"), text[m.end():]


def _record_spans(lines: list[str]) -> tuple[int, list[tuple[int, int]]]:
    """Index of the `updates:` line and the [start, end) line span of each record."""
    idx = next((i for i, ln in enumerate(lines) if re.match(r"^updates:", ln)), None)
    if idx is None:
        raise RecordError("frontmatter has no `updates:` key")
    spans, start, i = [], None, idx + 1
    while i < len(lines) and (lines[i].startswith("  ") or lines[i] == ""):
        if lines[i].startswith("  - "):
            if start is not None:
                spans.append((start, i))
            start = i
        i += 1
    if start is not None:
        spans.append((start, i))
    return idx, spans


def _next_at(entry: dict, at: str | None) -> str:
    last = max([str(u.get("at")) for u in entry.get("updates") or []]
               + [str(entry.get("discovered_at"))])
    if at:
        if not AT_RE.match(at):
            raise RecordError(f"--at must be YYYY-MM-DDTHH:MM:SSZ, got {at!r}")
        if at <= last:
            raise RecordError(f"--at {at} is not later than the entry's last stamp {last}")
        return at
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    while now <= last:  # a record in this very second: wait it out (bounded by the clock)
        time.sleep(1)
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return now


def add(root: Path, entry_id: str, rtype: str, run_id: str, fields: list[str], summary: str,
        section: str | None, internal: bool, at: str | None = None) -> str:
    if rtype not in TYPES:
        raise RecordError(f"type must be one of {TYPES}")
    if not run_id:
        raise RecordError("--run-id is required")
    if internal and section:
        raise RecordError("an internal record carries no section")
    if not internal and not (section or "").strip():
        raise RecordError("a non-internal record needs its section (--section-file)")
    path = entry_path(root, entry_id)
    entry = cm.load_entry(path, root=root)
    if str(entry.get("run_id")) == run_id:
        raise RecordError("this fire created the entry: edit it directly, it needs no record")
    if any(str(u.get("run_id")) == run_id for u in entry.get("updates") or []):
        raise RecordError(f"{entry['id']} already carries a record from {run_id}: one record per "
                          "fire per entry, use `amend`")
    at = _next_at(entry, at)
    lines, body = _split(path.read_text(encoding="utf-8"))
    rec = [f'  - at: "{at}"', f"    run_id: {run_id}", f"    type: {rtype}"]
    if internal:
        rec.append("    internal: true")
    rec.append("    summary: >")
    rec += fold(summary, "      ")
    rec.append(f"    fields: [{', '.join(fields)}]")
    idx, spans = _record_spans(lines)
    if lines[idx].strip() == "updates: []":
        lines[idx] = "updates:"
        insert_at = idx + 1
    else:
        insert_at = spans[-1][1] if spans else idx + 1
        while insert_at > idx + 1 and lines[insert_at - 1] == "":
            insert_at -= 1
    lines[insert_at:insert_at] = rec
    if rtype == "update" and not internal:
        hit = [i for i, ln in enumerate(lines) if ln.startswith("updated_at:")]
        if hit:
            lines[hit[0]] = f'updated_at: "{at}"'
        else:
            lines.insert(idx, f'updated_at: "{at}"')
    if not internal:
        heading = cm.update_section_heading(rtype, at)
        body = body.rstrip("\n") + f"\n\n{heading}\n\n{section.strip()}\n"
    _write(path, root, "\n".join(lines), body, at)
    return at


def amend(root: Path, entry_id: str, run_id: str, summary: str | None,
          fields: list[str] | None, add_fields: list[str] | None, check_published: bool = True) -> str:
    if summary is None and fields is None and not add_fields:
        raise RecordError("nothing to amend: give --summary(-file), --fields or --add-fields")
    path = entry_path(root, entry_id)
    if check_published and _published(root, path, run_id):
        raise RecordError(f"the {run_id} record on {entry_id} is already on origin/main: published "
                          "records are append-only, write a record for a new fire instead")
    entry = cm.load_entry(path, root=root)
    recs = [u for u in entry.get("updates") or [] if str(u.get("run_id")) == run_id]
    if not recs:
        raise RecordError(f"{entry['id']} carries no record from {run_id}")
    at = str(recs[-1].get("at"))
    lines, body = _split(path.read_text(encoding="utf-8"))
    _, spans = _record_spans(lines)
    span = next(((s, e) for s, e in spans if lines[s].strip() == f'- at: "{at}"'), None)
    if span is None:
        raise RecordError(f"record at {at} not found in the frontmatter text")
    s, e = span
    block = lines[s:e]
    while block and block[-1] == "":
        block.pop()
    tail = lines[s + len(block):e]
    if summary is not None:
        i = next((k for k, ln in enumerate(block) if re.match(r"^    summary:", ln)), None)
        if i is None:
            raise RecordError("record has no summary key")
        j = i + 1
        if block[i].rstrip().endswith((">", "|", ">-", "|-")):
            while j < len(block) and block[j].startswith("      "):
                j += 1
        block[i:j] = ["    summary: >"] + fold(summary, "      ")
    if fields is not None or add_fields:
        old = [str(f) for f in (recs[-1].get("fields") or [])]
        new = fields if fields is not None else old + [f for f in add_fields if f not in old]
        i = next((k for k, ln in enumerate(block) if re.match(r"^    fields:", ln)), None)
        j = i + 1 if i is not None else None
        if i is not None:
            while j < len(block) and block[j].startswith("      - "):
                j += 1
            block[i:j] = [f"    fields: [{', '.join(new)}]"]
        else:
            block.append(f"    fields: [{', '.join(new)}]")
    lines[s:e] = block + tail
    _write(path, root, "\n".join(lines), body, at)
    return at


def changed_fields(root: Path, entry_id: str, run_id: str, base: str = "HEAD") -> list[str]:
    """The keys `fields` must name: changed top-level frontmatter keys (bar the
    changelog's own) plus `body` when the analysis or an earlier section changed,
    the same rule as check_run.py `changelog-fields`."""
    path = entry_path(root, entry_id)
    rel = path.relative_to(root).as_posix()
    show = subprocess.run(["git", "show", f"{base}:{rel}"], capture_output=True, text=True,
                          cwd=root, timeout=15)
    if show.returncode != 0:
        raise RecordError(f"cannot read {rel} at {base}: {show.stderr.strip()}")
    fm_b, body_b = cm.split_frontmatter(show.stdout)
    fm_a, body_a = cm.split_frontmatter(path.read_text(encoding="utf-8"))
    before, after = cm.parse_yaml_subset(fm_b), cm.parse_yaml_subset(fm_a)
    changed = {k for k in set(before) | set(after)
               if k not in ("updates", "updated_at") and before.get(k) != after.get(k)}
    own = {str(u.get("at")) for u in after.get("updates") or [] if str(u.get("run_id")) == run_id}
    main_a, secs_a = cm.split_update_sections(body_a)
    main_b, secs_b = cm.split_update_sections(body_b)
    kept = [main_a.strip()] + [f"{x.get('at')}\n{(x.get('body') or '').strip()}"
                               for x in secs_a if str(x.get("at")) not in own]
    prior = [main_b.strip()] + [f"{x.get('at')}\n{(x.get('body') or '').strip()}" for x in secs_b]
    if kept != prior:
        changed.add("body")
    return sorted(changed)


def _published(root: Path, path: Path, run_id: str) -> bool:
    rel = path.relative_to(root).as_posix()
    try:
        show = subprocess.run(["git", "show", f"origin/main:{rel}"], capture_output=True,
                              text=True, cwd=root, timeout=15)
    except Exception:
        return False
    return show.returncode == 0 and re.search(rf"^    run_id: {re.escape(run_id)}$",
                                              show.stdout, re.M) is not None


def _write(path: Path, root: Path, fm: str, body: str, at: str) -> None:
    original = path.read_text(encoding="utf-8")
    path.write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8")
    try:
        e = cm.load_entry(path, root=root)
        assert any(str(u.get("at")) == at for u in e.get("updates") or []), "record not re-read"
        heads = [str(x.get("at")) for x in cm.split_update_sections(e["body"])[1]]
        recs = [str(u.get("at")) for u in e["updates"] if not u.get("internal")]
        assert heads == recs, f"sections {heads} do not pair with records {recs}"
    except Exception as exc:
        path.write_text(original, encoding="utf-8")
        raise RecordError(f"the result did not re-parse, file left unchanged: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="append this fire's record")
    a.add_argument("entry")
    a.add_argument("type", choices=TYPES)
    a.add_argument("--run-id", required=True)
    a.add_argument("--fields", required=True, help="comma-separated, e.g. cves,body")
    a.add_argument("--summary")
    a.add_argument("--summary-file")
    a.add_argument("--section-file")
    a.add_argument("--internal", action="store_true")
    a.add_argument("--at")
    m = sub.add_parser("amend", help="replace this fire's own unpublished record's summary/fields")
    m.add_argument("entry")
    m.add_argument("--run-id", required=True)
    m.add_argument("--summary")
    m.add_argument("--summary-file")
    g = m.add_mutually_exclusive_group()
    g.add_argument("--fields")
    g.add_argument("--add-fields")
    d = sub.add_parser("diff", help="the fields this fire changed against a base")
    d.add_argument("entry")
    d.add_argument("--run-id", required=True)
    d.add_argument("--base", default="HEAD")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    try:
        if args.cmd == "add":
            summary = read_summary(args)
            if summary is None:
                raise RecordError("give --summary or --summary-file")
            section = (Path(args.section_file).read_text(encoding="utf-8")
                       if args.section_file else None)
            at = add(root, args.entry, args.type, args.run_id, parse_fields(args.fields),
                     summary, section, args.internal, args.at)
            print(f"{args.entry}: {args.type}{' (internal)' if args.internal else ''} at {at}")
        elif args.cmd == "amend":
            at = amend(root, args.entry, args.run_id, read_summary(args),
                       parse_fields(args.fields) if args.fields else None,
                       parse_fields(args.add_fields) if args.add_fields else None)
            print(f"{args.entry}: record at {at} amended")
        else:
            print(",".join(changed_fields(root, args.entry, args.run_id, args.base)))
    except RecordError as exc:
        print(f"entry_record: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
