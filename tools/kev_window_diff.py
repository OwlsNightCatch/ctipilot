#!/usr/bin/env python3
"""tools/kev_window_diff.py — every CISA KEV addition in the window, and which
of them the store has never covered.

Why this exists
---------------
CISA KEV is the pipeline's single highest-value vulnerability source: a listing
is jurisdiction-agnostic confirmation that a flaw is exploited in the wild
(`prompts/cti-run.md` PD-13), which is the fact that most often forces an
out-of-band response for the constituency. Sweeping it has always been a
research sub-agent's job, and a sub-agent returns what it *noticed* — so a KEV
addition can be silently skipped without ever producing a borderline-drop line,
and nothing downstream can tell the difference between "considered and dropped"
and "never seen".

The 2026-08-30 quality audit found exactly that: the 2026-08-28 catch-up fire
fetched the KEV feed and surfaced four in-window additions while
CVE-2026-21962 (Oracle HTTP Server / WebLogic Proxy Plug-in, CVSS 10.0, KEV
2026-08-24, exploited since January) and CVE-2026-60004 (Gitea, CVSS 9.8, KEV
2026-08-25, confirmed exploited) went unmentioned in every artefact of the run.

This tool makes the sweep mechanical instead of attentional. It is deliberately
dumb: it lists what is in the window and says which ids the store has never
recorded. Judgement stays with the agent — an uncovered row may well be out of
scope (PD-11), and saying so in the run record is a valid disposition. What is
no longer possible is not knowing the row existed.

Usage
-----
    python3 tools/kev_window_diff.py --since 2026-08-24
    python3 tools/kev_window_diff.py --window-hours 26          # gap-derived
    python3 tools/kev_window_diff.py --since 2026-08-24 --json  # machine-readable
    python3 tools/kev_window_diff.py --since 2026-08-24 --kev-file kev.json

Coverage is checked against BOTH `state/cves_seen.json` (the flat store-wide
index) and the `cves[]` frontmatter of every entry, so a CVE covered by an
entry whose id never reached the index still reports as covered.

Exit codes: 0 always when the feed was read (uncovered rows are information,
not a gate failure); 2 when the KEV feed could not be fetched or parsed.

Stdlib only, like every other tool in this directory. The feed itself is read
through `tools/fetch_source.py cisa-kev` because cisa.gov 403s the routine UA.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))

import content_model as cm  # noqa: E402

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.I)


def _fetch_kev(kev_file: Path | None) -> dict:
    if kev_file is not None:
        return json.loads(kev_file.read_text(encoding="utf-8"))
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "fetch_source.py"), "cisa-kev"],
        capture_output=True, text=True, timeout=180,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"fetch_source.py cisa-kev exited {proc.returncode}: "
                           f"{proc.stderr.strip()[:400]}")
    return json.loads(proc.stdout)


def _store_cve_ids() -> tuple[set[str], dict[str, str]]:
    """Every CVE id the store knows, plus id -> first entry that carries it."""
    ids: set[str] = set()
    owner: dict[str, str] = {}

    index = ROOT / "state" / "cves_seen.json"
    if index.is_file():
        data = json.loads(index.read_text(encoding="utf-8"))
        for rec in data.get("cves", []):
            cid = str(rec.get("id") or "").upper()
            if cid:
                ids.add(cid)
                owner.setdefault(cid, "state/cves_seen.json")

    entries_dir = ROOT / "entries"
    if entries_dir.is_dir():
        for day in sorted(entries_dir.iterdir()):
            if not day.is_dir() or not cm.DATE_RE.match(day.name):
                continue
            for path in sorted(day.glob("*.md")):
                try:
                    entry = cm.load_entry(path, root=ROOT)
                except Exception:  # noqa: BLE001 — a parse error is not this tool's finding
                    continue
                data = entry.data if hasattr(entry, "data") else entry
                for rec in (data.get("cves") or []):
                    cid = str((rec or {}).get("id") or "").upper()
                    if cid:
                        ids.add(cid)
                        owner[cid] = data.get("id", str(path))
    return ids, owner


def _since_from_args(args: argparse.Namespace) -> date:
    if args.since:
        return date.fromisoformat(args.since)
    hours = args.window_hours if args.window_hours is not None else 24
    return (datetime.now(timezone.utc) - timedelta(hours=hours)).date()


def main() -> int:
    p = argparse.ArgumentParser(
        description="List CISA KEV additions inside a window and flag the ones "
                    "the content store has never covered.")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--since", metavar="YYYY-MM-DD",
                   help="earliest KEV dateAdded to report (inclusive)")
    g.add_argument("--window-hours", type=float, metavar="N",
                   help="derive --since from now minus N hours (the run's window_hours)")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--kev-file", type=Path,
                   help="read the KEV catalog from a local JSON file instead of fetching")
    args = p.parse_args()

    since = _since_from_args(args)

    try:
        kev = _fetch_kev(args.kev_file)
    except Exception as e:  # noqa: BLE001
        print(f"FATAL: could not read the CISA KEV catalog — {e}", file=sys.stderr)
        return 2

    vulns = kev.get("vulnerabilities")
    if not isinstance(vulns, list):
        print("FATAL: KEV payload has no `vulnerabilities` list", file=sys.stderr)
        return 2

    known, owner = _store_cve_ids()

    rows = []
    for v in vulns:
        added = str(v.get("dateAdded") or "")
        if not added or added < since.isoformat():
            continue
        cid = str(v.get("cveID") or "").upper()
        rows.append({
            "cve": cid,
            "date_added": added,
            "vendor": v.get("vendorProject"),
            "product": v.get("product"),
            "name": v.get("vulnerabilityName"),
            "ransomware": v.get("knownRansomwareCampaignUse"),
            "covered": cid in known,
            "covered_by": owner.get(cid),
        })
    rows.sort(key=lambda r: (r["date_added"], r["cve"]))
    uncovered = [r for r in rows if not r["covered"]]

    if args.json:
        json.dump({"since": since.isoformat(), "total_in_window": len(rows),
                   "uncovered": len(uncovered), "rows": rows},
                  sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0

    print(f"CISA KEV additions since {since.isoformat()}: {len(rows)} "
          f"({len(uncovered)} not covered by the store)\n")
    if not rows:
        print("  none — the window carries no KEV additions")
        return 0
    for r in rows:
        mark = "COVERED  " if r["covered"] else "NOT COVERED"
        print(f"  {mark} {r['date_added']}  {r['cve']:18s} {r['vendor']} {r['product']}")
        print(f"              {r['name']}")
        if r["covered"]:
            print(f"              already in: {r['covered_by']}")
    if uncovered:
        print("\nEvery NOT COVERED row needs a disposition in this run: a new entry, "
              "an `update` changelog record on the entry that already covers the "
              "finding, or an explicit `borderline-drop:` line in the run record "
              "saying why it is out of scope (PD-11). Silence is not a disposition.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
