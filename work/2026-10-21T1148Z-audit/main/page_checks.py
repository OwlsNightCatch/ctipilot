"""Cited-page pre-pass (quality-audit Phase 0 step 5b) scoped to this wave's rows."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "site"))
import check_run as cr
RUN_ID = "2026-10-21T1148Z-audit"
ids = set(json.load(open(ROOT / f"work/{RUN_ID}/entries.json")))
entries, errors = cr.collect_entries_tolerant(ROOT / "entries", ROOT)
scope = [e for e in entries if e["id"] in ids]
print(f"page checks: {len(scope)} entries in wave scope")
print("== evidence quotes are verbatim on their cited page ==")
cr.check_evidence_quotes_literal(scope, RUN_ID, skip=False)
print("\n== clauses naming a CVE cite a page that carries it ==")
cr.check_citation_cves(scope, RUN_ID, skip=False)
cr._summary()
