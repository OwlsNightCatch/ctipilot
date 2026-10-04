#!/usr/bin/env python3
"""Claim ledger: the exhaustive checklist a verifier pass walks (v4.17).

Why this exists. Over the 27 intel fires of September 2026 the Phase 5.7 loop
hit its 8-iteration cap 15 times and reached a confirmed double-CLEAN only 4
times. The telemetry analysis of the 2026-09-29 setup review found why: each
cold pass SAMPLES the claims it checks, so iteration 1 surfaced only 23% of all
findings, 40% of flagged entries got their first finding at iteration 2 or
later, and 8 of 14 CLEAN verdicts were refuted by the next pass on defects that
were already in the text the CLEAN pass had read. More passes of a sampler do
not converge; a pass that must answer for every claim does.

This tool turns a run's reader-facing prose into a numbered list of claims:
every inline-citation clause (the text a citation vouches for, per
`check_run._citation_clauses`), every sentence that carries no citation at all
(the F5 surface), and the frontmatter statements a reader or a triage agent
acts on (headline, summary, immediate_action, each action, each cves[] record).
The verifier writes one verdict row per claim; its pass is complete only when
every claim has a row.

    python3 tools/claim_ledger.py <run-id>                 # write work/<run-id>/claims.yaml
    python3 tools/claim_ledger.py <run-id> --iteration N   # also snapshot claims.iterN.yaml
                                                           # and list what changed since N-1
    python3 tools/claim_ledger.py <run-id> --coverage N    # compare the verifier's
                                                           # verification.iterN.claims.yaml
                                                           # against the ledger

Scope: the run's NEW entries (whole entry) and, on entries the run UPDATED,
the sections this run wrote plus every frontmatter field its records declare.
Claim ids are content hashes, so an unchanged claim keeps its id across
iterations and a remediated one gets a new id: `--iteration` lists exactly the
claims a post-fix pass must re-check.

Output is a YAML subset the verifier can Read directly (one mapping per claim).
Stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "site"))
sys.path.insert(0, str(ROOT / "tools"))

import content_model as cm  # noqa: E402

_LINK_RE = re.compile(r"\[[^\]\n]+\]\((https?://[^)\s]+)\)")
_SENT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z(*`\"'\[])")
_LABEL_RE = re.compile(r"^\*\*\s*(Exposure|Detection|Triage|Defender takeaway|Hunt(?:ing)?)\s*:?\s*\*\*",
                       re.IGNORECASE)


def _citation_clauses(text: str) -> list[tuple[str, list[str]]]:
    try:
        import check_run  # type: ignore
        return check_run._citation_clauses(text)  # noqa: SLF001 — one definition of "clause"
    except Exception:  # noqa: BLE001 — fallback: whole sentences with their links
        out = []
        for sent in _SENT_RE.split(text):
            urls = _LINK_RE.findall(sent)
            if urls:
                out.append((sent, urls))
        return out


def _cid(entry_id: str, surface: str, text: str) -> str:
    norm = re.sub(r"\s+", " ", text).strip().lower()
    return hashlib.sha1(f"{entry_id}|{surface}|{norm}".encode("utf-8")).hexdigest()[:10]


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", _LINK_RE.sub(lambda m: "", text)).strip()


def _prose_claims(entry_id: str, surface: str, text: str) -> list[dict]:
    claims = []
    for clause, urls in _citation_clauses(text):
        t = _plain(clause)
        if len(t) < 12:
            continue
        claims.append({"claim_id": _cid(entry_id, surface, t), "entry": entry_id,
                       "surface": surface, "kind": "cited", "text": t, "urls": urls})
    # Sentences with no citation: F5 candidates, or derived analysis (the
    # labelled lines), which the verifier checks follows from cited facts.
    for para in re.split(r"\n\s*\n", text):
        derived = bool(_LABEL_RE.match(para.strip()))
        for sent in _SENT_RE.split(para):
            if _LINK_RE.search(sent):
                continue
            t = _plain(sent)
            if len(t) < 25 or t.startswith("#"):
                continue
            claims.append({"claim_id": _cid(entry_id, surface, t), "entry": entry_id,
                           "surface": surface, "kind": "derived" if derived else "uncited",
                           "text": t, "urls": []})
    return claims


def _field_claims(e: dict, fields: set[str] | None) -> list[dict]:
    eid = e["id"]
    out = []

    def add(surface: str, text: str, kind: str = "frontmatter"):
        t = re.sub(r"\s+", " ", str(text or "")).strip()
        if t:
            out.append({"claim_id": _cid(eid, surface, t), "entry": eid, "surface": surface,
                        "kind": kind, "text": t, "urls": []})

    def wants(name: str) -> bool:
        return fields is None or name in fields

    if wants("headline"):
        add("headline", e.get("headline"))
    if wants("summary"):
        add("summary", e.get("summary"))
    ia = e.get("immediate_action")
    if isinstance(ia, dict) and wants("immediate_action"):
        add("immediate_action", f"{ia.get('title') or ''}: {ia.get('action') or ''}")
    if wants("actions"):
        for i, a in enumerate(e.get("actions") or []):
            add(f"actions[{i}]", a)
    if wants("cves"):
        for c in e.get("cves") or []:
            if isinstance(c, dict):
                add(f"cves[{c.get('id')}]", json.dumps(
                    {k: c.get(k) for k in ("id", "cvss", "status", "affected", "fixed", "auth", "vector")},
                    ensure_ascii=False))
    return out


def build(run_id: str) -> list[dict]:
    claims: list[dict] = []
    for e in cm.collect_entries():
        is_new = str(e.get("run_id") or "") == run_id
        recs = [r for r in (e.get("updates") or [])
                if isinstance(r, dict) and str(r.get("run_id") or "") == run_id]
        if not is_new and not recs:
            continue
        main, sections = cm.split_update_sections(e.get("body") or "")
        if is_new:
            claims += _field_claims(e, None)
            claims += _prose_claims(e["id"], "body", main)
            for sec in sections:
                claims += _prose_claims(e["id"], f"section {sec.get('at')}", sec.get("body") or "")
            continue
        fields = {str(f) for r in recs for f in (r.get("fields") or [])}
        claims += _field_claims(e, fields)
        if "body" in fields:
            claims += _prose_claims(e["id"], "body", main)
        own = {str(r.get("at")) for r in recs}
        for sec in sections:
            if str(sec.get("at")) in own:
                claims += _prose_claims(e["id"], f"section {sec.get('at')}", sec.get("body") or "")
        for r in recs:
            if r.get("summary"):
                t = re.sub(r"\s+", " ", str(r["summary"])).strip()
                claims.append({"claim_id": _cid(e["id"], f"record {r.get('at')}", t), "entry": e["id"],
                               "surface": f"record {r.get('at')}", "kind": "record-summary",
                               "text": t, "urls": []})
    seen = set()
    unique = []
    for c in claims:
        if c["claim_id"] in seen:
            continue
        seen.add(c["claim_id"])
        unique.append(c)
    return unique


def _dump(claims: list[dict], header: dict) -> str:
    lines = [f"# {k}: {v}" for k, v in header.items()]
    lines.append("claims:")
    for c in claims:
        lines.append(f"  - claim_id: {c['claim_id']}")
        lines.append(f"    entry: {c['entry']}")
        lines.append(f"    surface: {json.dumps(c['surface'], ensure_ascii=False)}")
        lines.append(f"    kind: {c['kind']}")
        lines.append(f"    text: {json.dumps(c['text'], ensure_ascii=False)}")
        if c["urls"]:
            lines.append("    urls: [" + ", ".join(json.dumps(u) for u in c["urls"]) + "]")
    return "\n".join(lines) + "\n"


def _load_ids(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    # Verifiers write rows as block or flow mappings, with or without JSON
    # quoting ("claim_id": "…"); accept every YAML spelling of the key.
    return set(re.findall(r"""["']?claim_id["']?\s*:\s*["']?([0-9a-f]{10})""", path.read_text(encoding="utf-8")))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run_id")
    ap.add_argument("--iteration", type=int, help="snapshot the ledger for verifier iteration N")
    ap.add_argument("--coverage", type=int, metavar="N",
                    help="report how many ledger claims verification.iterN.claims.yaml answered")
    args = ap.parse_args(argv)
    work = ROOT / "work" / args.run_id
    work.mkdir(parents=True, exist_ok=True)

    if args.coverage:
        ledger = _load_ids(work / f"claims.iter{args.coverage}.yaml") or _load_ids(work / "claims.yaml")
        answered = _load_ids(work / f"verification.iter{args.coverage}.claims.yaml")
        missing = sorted(ledger - answered)
        print(f"claim coverage iteration {args.coverage}: {len(ledger & answered)}/{len(ledger)} "
              f"claims answered; {len(missing)} missing")
        for cid in missing[:40]:
            print(f"  missing {cid}")
        return 0 if not missing else 1

    claims = build(args.run_id)
    by_kind: dict[str, int] = {}
    for c in claims:
        by_kind[c["kind"]] = by_kind.get(c["kind"], 0) + 1
    header = {"run_id": args.run_id, "claims": len(claims),
              "by_kind": json.dumps(by_kind, sort_keys=True)}
    (work / "claims.yaml").write_text(_dump(claims, header), encoding="utf-8")
    msg = f"claim ledger: {len(claims)} claims {by_kind} -> work/{args.run_id}/claims.yaml"
    if args.iteration:
        snap = work / f"claims.iter{args.iteration}.yaml"
        snap.write_text(_dump(claims, header), encoding="utf-8")
        prev = _load_ids(work / f"claims.iter{args.iteration - 1}.yaml") if args.iteration > 1 else set()
        if prev:
            changed = [c for c in claims if c["claim_id"] not in prev]
            (work / f"claims.changed.iter{args.iteration}.yaml").write_text(
                _dump(changed, {**header, "changed_since_iteration": args.iteration - 1,
                                "changed": len(changed)}), encoding="utf-8")
            msg += (f"; {len(changed)} new or changed since iteration {args.iteration - 1} -> "
                    f"work/{args.run_id}/claims.changed.iter{args.iteration}.yaml")
    print(msg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
