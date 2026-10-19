"""Replace the folded summary of THIS fire's own (unpublished) changelog record, located by its `at`.
  python3 resum.py <entry-id> <at> <summary-file>"""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site")); import content_model as cm
sys.path.insert(0, str(Path(__file__).parent)); from add_record import fold
eid, at, sf = sys.argv[1:4]
p = ROOT / "entries" / f"{eid}.md"; t = p.read_text(encoding="utf-8")
m = re.search(r'(  - at: "' + re.escape(at) + r'"\n    run_id: 2026-10-18T1307Z-audit\n(?:    [a-z_]+: [^\n]*\n)*?    summary: >\n)((?:      [^\n]*\n)+)', t)
assert m, "record not found"
new = "\n".join(fold(" ".join(Path(sf).read_text(encoding="utf-8").split()), "      ")) + "\n"
t = t[:m.start(2)] + new + t[m.end(2):]
p.write_text(t, encoding="utf-8"); cm.load_entry(p); print(eid, "summary replaced at", at)
