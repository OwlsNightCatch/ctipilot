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
    python3 tools/kev_window_diff.py --window-hours 26 --run-id "$RUN_ID"
        # ^ the shape a fire should use: also writes work/<run-id>/kev-window.txt,
        #   so the forensic artefact exists without depending on a shell redirect.

Coverage is an entry's `cves[]` record. Four states: COVERED (an entry
carries the CVE and already says exploited / cisa-kev), COVERED-STALE (an
entry carries it but does not yet say exploited: the listing is the PD-13
exploitation-status change, an `update` record), MENTION-ONLY (only
`state/cves_seen.json` knows it, from a body mention), NOT COVERED.

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


def _store_cve_ids() -> tuple[dict[str, dict], set[str]]:
    """({cve: {"entry": id, "exploited": bool}} for every CVE an entry's
    `cves[]` carries, {cve ids only in state/cves_seen.json}).

    Coverage means an entry's `cves[]` record, never the flat index alone:
    the index also holds CVEs an entry body merely mentions (history,
    comparisons), and 71 KEV CVEs were reported "covered" that way in the
    2026-09-29 tooling review while no entry told the reader they were
    exploited. `stale` lists every carrying entry whose record does not yet
    say `exploited` or `cisa-kev`: for each, the listing is the PD-13
    exploitation-status change that ships as an `update` record (an entry
    whose summary still says "no known exploitation" misleads its reader even
    when a later entry covers the exploitation).
    """
    covered: dict[str, dict] = {}
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
                    if not cid:
                        continue
                    status = set((rec or {}).get("status") or [])
                    eid = data.get("id", str(path))
                    cur = covered.setdefault(cid, {"entry": eid, "stale": []})
                    cur["entry"] = eid  # newest carrying entry
                    if not status & {"exploited", "cisa-kev"}:
                        cur["stale"].append(eid)
    index_only: set[str] = set()
    index = ROOT / "state" / "cves_seen.json"
    if index.is_file():
        data = json.loads(index.read_text(encoding="utf-8"))
        for rec in data.get("cves", []):
            cid = str(rec.get("id") or "").upper()
            if cid and cid not in covered:
                index_only.add(cid)
    return covered, index_only


def _now_from_args(args: argparse.Namespace) -> datetime:
    """The Phase 0 network-verified start (--now, else the run id), never the
    container clock when either is given: the clock has been days wrong."""
    if args.now:
        return datetime.strptime(args.now, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    m = re.match(r"^(\d{4}-\d{2}-\d{2})T(\d{2})(\d{2})Z-", str(args.run_id or ""))
    if m:
        return datetime.strptime(f"{m.group(1)}T{m.group(2)}:{m.group(3)}:00Z",
                                 "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return datetime.now(timezone.utc)


def _since_from_args(args: argparse.Namespace) -> date:
    if args.since:
        return date.fromisoformat(args.since)
    hours = args.window_hours if args.window_hours is not None else 24
    return (_now_from_args(args) - timedelta(hours=hours)).date()


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
    p.add_argument("--now", metavar="YYYY-MM-DDTHH:MM:SSZ",
                   help="the run's verified start (Phase 0 STARTED); default: derived "
                        "from --run-id, else the container clock")
    p.add_argument("--run-id", metavar="RUN_ID",
                   help="also persist this report to work/<RUN_ID>/kev-window.txt "
                        "(the forensic artefact the run record's KEV note refers to)")
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

    covered_map, index_only = _store_cve_ids()

    rows = []
    for v in vulns:
        added = str(v.get("dateAdded") or "")
        if not added or added < since.isoformat():
            continue
        cid = str(v.get("cveID") or "").upper()
        cov = covered_map.get(cid)
        state = ("covered" if cov and not cov["stale"] else
                 "stale" if cov else
                 "mentioned" if cid in index_only else "uncovered")
        rows.append({
            "cve": cid,
            "date_added": added,
            "vendor": v.get("vendorProject"),
            "product": v.get("product"),
            "name": v.get("vulnerabilityName"),
            "ransomware": v.get("knownRansomwareCampaignUse"),
            "state": state,
            "covered": state == "covered",
            "covered_by": (", ".join(cov["stale"]) if cov and cov["stale"] else cov["entry"]) if cov else None,
        })
    rows.sort(key=lambda r: (r["date_added"], r["cve"]))
    uncovered = [r for r in rows if r["state"] != "covered"]

    if args.json:
        payload = json.dumps({"since": since.isoformat(), "total_in_window": len(rows),
                              "uncovered": len(uncovered), "rows": rows}, indent=2)
        print(payload)
        _persist(args.run_id, payload)
        return 0

    out = [f"CISA KEV additions since {since.isoformat()}: {len(rows)} "
           f"({len(uncovered)} not covered by the store)", ""]
    if not rows:
        out.append("  none — the window carries no KEV additions")
    for r in rows:
        mark = {"covered": "COVERED      ", "stale": "COVERED-STALE",
                "mentioned": "MENTION-ONLY ", "uncovered": "NOT COVERED  "}[r["state"]]
        out.append(f"  {mark} {r['date_added']}  {r['cve']:18s} {r['vendor']} {r['product']}")
        out.append(f"                {r['name']}")
        if r["state"] == "covered":
            out.append(f"                already in: {r['covered_by']}")
        elif r["state"] == "stale":
            out.append(f"                carried by {r['covered_by']}, whose cves[] record does not "
                       "yet say exploited: the KEV listing is an exploitation-status change (PD-13), "
                       "an `update` record on that entry")
        elif r["state"] == "mentioned":
            out.append("                only mentioned in an entry body (state/cves_seen.json); no "
                       "entry covers it as a finding")
    if uncovered:
        out += ["", "Every NOT COVERED, MENTION-ONLY and COVERED-STALE row needs a disposition "
                    "in this run: a new entry, an `update` changelog record on the entry that "
                    "already covers the finding (for COVERED-STALE: the record that moves its "
                    "cves[].status to exploited), or an explicit `borderline-drop:` line in the "
                    "run record saying why it is out of scope (PD-11). Silence is not a disposition."]
    report = "\n".join(out)
    print(report)
    _persist(args.run_id, report)
    return 0


def _persist(run_id: str | None, report: str) -> None:
    """Write the report to work/<run-id>/kev-window.txt.

    The artefact requirement in `prompts/cti-run.md` Phase 0 step 6b was purely
    attentional through v4.9 — it asked the fire to `tee` the output — and two
    consecutive audit windows (2026-08-30 → 09-06 and 09-06 → 09-13) found that
    not one fire of fourteen ever wrote the file, even while most discharged the
    KEV duty correctly in prose. A duty that depends on remembering a shell
    redirect is a duty that decays; running the tool now discharges it.
    """
    if not run_id:
        return
    dest = ROOT / "work" / run_id / "kev-window.txt"
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(report + "\n", encoding="utf-8")
        print(f"\n[kev-window] persisted to {dest.relative_to(ROOT)}", file=sys.stderr)
    except OSError as e:  # noqa: BLE001 — never fail the sweep over the artefact
        print(f"[kev-window] could not persist artefact: {e}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
