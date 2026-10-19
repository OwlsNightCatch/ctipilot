"""Append one changelog record (and, unless internal, its body section) to an entry.

Run-local helper for the 2026-10-18 audit. Usage:
  python3 add_record.py <entry-id> <type> <fields,csv> <summary-file> [--section <file>] [--internal]

The record's `at` is the current UTC second. `updated_at` moves only for a
non-internal `update` record (docs/pipeline.md § Entry lifecycle). The
frontmatter is edited textually so the rest of the file stays byte-identical;
the result is re-parsed with site/content_model.py to prove it is still valid.
"""
import argparse, re, sys, time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm

RUN_ID = "2026-10-18T1307Z-audit"
HEAD = {"update": "Update", "correction": "Correction", "improvement": "Improvement"}


def fold(text: str, indent: str, width: int = 100) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(indent + cur); cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(indent + cur)
    return lines


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("entry"); ap.add_argument("type", choices=list(HEAD)); ap.add_argument("fields")
    ap.add_argument("summary_file"); ap.add_argument("--section"); ap.add_argument("--internal", action="store_true")
    a = ap.parse_args()
    path = ROOT / "entries" / f"{a.entry}.md"
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm, body = m.group(1), text[m.end():]
    prev = cm.load_entry(path)
    last = max([str(u.get("at")) for u in prev.get("updates") or []] + [str(prev.get("discovered_at"))])
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    while now <= last:
        time.sleep(1); now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    summary = " ".join(Path(a.summary_file).read_text(encoding="utf-8").split())
    fields = [f.strip() for f in a.fields.split(",") if f.strip()]
    rec = [f'  - at: "{now}"', f"    run_id: {RUN_ID}", f"    type: {a.type}"]
    if a.internal:
        rec.append("    internal: true")
    rec.append("    summary: >")
    rec += fold(summary, "      ")
    rec.append(f"    fields: [{', '.join(fields)}]")
    lines = fm.split("\n")
    idx = next(i for i, l in enumerate(lines) if l.startswith("updates:"))
    if lines[idx].strip() == "updates: []":
        lines[idx] = "updates:"
        insert_at = idx + 1
    else:
        insert_at = idx + 1
        while insert_at < len(lines) and (lines[insert_at].startswith("  ") or lines[insert_at] == ""):
            insert_at += 1
    lines[insert_at:insert_at] = rec
    if a.type == "update" and not a.internal:
        hit = [i for i, l in enumerate(lines) if l.startswith("updated_at:")]
        if hit:
            lines[hit[0]] = f'updated_at: "{now}"'
        else:
            lines.insert(idx, f'updated_at: "{now}"')
    new_fm = "\n".join(lines)
    if not a.internal:
        if not a.section:
            sys.exit("a non-internal record needs --section")
        sec = Path(a.section).read_text(encoding="utf-8").strip()
        body = body.rstrip("\n") + f"\n\n## {HEAD[a.type]} — {now}\n\n{sec}\n"
    elif a.section:
        sys.exit("an internal record carries no section")
    path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
    e = cm.load_entry(path)  # re-parse: raises on a malformed result
    assert str((e.get("updates") or [])[-1].get("at")) == now
    print(f"{a.entry}: {a.type}{' (internal)' if a.internal else ''} at {now}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
