"""Whole-entry claim ledgers for the audit's retrospective truth passes.

Reuses tools/claim_ledger.py's claim extraction, treating every entry of a
batch as whole-entry scope (frontmatter claims, main analysis, every
changelog section). Writes work/<run-id>/truth-<batch>.ledger.yaml.
"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "site")); sys.path.insert(0, str(ROOT / "tools"))
import content_model as cm
import claim_ledger as cl

run_id = sys.argv[1]
plan = json.loads((ROOT / "work" / run_id / "audit-plan.json").read_text())
for batch, paths in plan["truth_batches"].items():
    claims = []
    for p in paths:
        e = cm.load_entry(ROOT / p)
        main, sections = cm.split_update_sections(e.get("body") or "")
        claims += cl._field_claims(e, None)
        claims += cl._prose_claims(e["id"], "body", main)
        for sec in sections:
            claims += cl._prose_claims(e["id"], f"section {sec.get('at')}", sec.get("body") or "")
        for r in e.get("updates") or []:
            if isinstance(r, dict) and r.get("summary"):
                t = " ".join(str(r["summary"]).split())
                claims.append({"claim_id": cl._cid(e["id"], f"record {r.get('at')}", t), "entry": e["id"],
                               "surface": f"record {r.get('at')}", "kind": "record-summary", "text": t, "urls": []})
    seen, uniq = set(), []
    for c in claims:
        if c["claim_id"] not in seen:
            seen.add(c["claim_id"]); uniq.append(c)
    out = ROOT / "work" / run_id / f"truth-{batch}.ledger.yaml"
    out.write_text(cl._dump(uniq, {"run_id": run_id, "batch": batch, "entries": len(paths), "claims": len(uniq)}), encoding="utf-8")
    print(batch, len(paths), "entries", len(uniq), "claims")
