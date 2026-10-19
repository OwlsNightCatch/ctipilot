"""Rewrite an entry's mutable frontmatter and main analysis while preserving
its lifecycle fields verbatim (run-local helper, 2026-10-18 audit).

  python3 rewrite.py <entry-id> <frontmatter-file> <body-file>

The frontmatter file holds the new mutable keys (title ... actions) as YAML
text in this repo's subset. Preserved from the original, byte for byte:
schema, discovered_at, run_id, migrated_from, merged_from, updated_at and the
whole updates[] list. Earlier `## <Type> — <at>` sections are kept after the
new main analysis. The caller then appends this fire's record with
add_record.py (which also re-parses the file).
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm

eid, fm_file, body_file = sys.argv[1:4]
path = ROOT / "entries" / f"{eid}.md"
text = path.read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
old_fm, old_body = m.group(1), text[m.end():]
lines = old_fm.split("\n")


def grab(key: str) -> list[str]:
    for i, l in enumerate(lines):
        if l.startswith(f"{key}:"):
            j = i + 1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j] == ""):
                j += 1
            return lines[i:j]
    return []


keep = {k: grab(k) for k in ("discovered_at", "run_id", "migrated_from", "merged_from", "updated_at", "updates")}
new_mut = Path(fm_file).read_text(encoding="utf-8").strip("\n").split("\n")
for k in keep:
    assert not any(l.startswith(f"{k}:") for l in new_mut), f"{k} must not be in the new frontmatter"
out = ["schema: 1"]
# discovered_at / run_id sit after summary in the canonical order; put them first among the preserved block
out += new_mut[:new_mut.index(next(l for l in new_mut if l.startswith("summary:"))) + 1]
rest = new_mut[len(out) - 1:]
# keep any continuation lines of a folded summary
while rest and rest[0].startswith(" "):
    out.append(rest.pop(0))
out += keep["discovered_at"] + keep["run_id"] + rest
for k in ("migrated_from", "merged_from"):
    out += keep[k]
out += keep["updated_at"] or ["updated_at: null"]
out += keep["updates"] or ["updates: []"]
main, sections = cm.split_update_sections(old_body)
first = cm.UPDATE_HEADING_RE.search(old_body)
sec_text = old_body[first.start():] if first else ""
new_body = "\n" + Path(body_file).read_text(encoding="utf-8").strip("\n") + "\n"
if sec_text:
    new_body += "\n" + sec_text.lstrip("\n")
path.write_text("---\n" + "\n".join(out) + "\n---\n" + new_body, encoding="utf-8")
e = cm.load_entry(path)
print(eid, "rewritten:", e["priority"], len(e.get("cves") or []), "cves,", len(sections), "earlier sections kept")
