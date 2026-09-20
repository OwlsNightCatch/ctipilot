#!/usr/bin/env python3
"""Emit a compact state digest for the pipeline main agent (v3).

The main agent must not load the full state files or scan `entries/` /
`runs/` wholesale into its context. This script distils exactly what
Phase 0 needs into one small JSON:

    {
      "today": "2026-07-03",
      "now": "2026-07-03T14:02:11Z",
      "cves": {                        # from state/cves_seen.json
        "count": 190,
        "ids": ["CVE-2026-0300", ...],
        "recent": [{"id", "first_seen", "last_seen", "title"}]   # last N days
      },
      "sources": {                     # from sources/sources.json
        "active_count": 78,
        "active_ids": [...], "demoted_ids": [...], "candidate_ids": [...],
        # Candidates that have met the promotion rule (cited by published
        # entries from >= promote_after distinct runs). A stateless per-fire
        # agent cannot count prior runs itself, so the digest counts for it.
        "promotion_due": [{"id", "contributing_runs", "last_run_id"}]
      },
      "runs": {                        # from runs/** (content_model)
        "count": 71,
        "last_run": {"run_id", "kind", "date", "started", "completed", "publish_status"},
        "fetch_gaps_in_window": [{"id", "runs_failing", "last_status"}]
      },
      "window24h": {                   # budget snapshot from entries/**
        "operational_total": 5,          # operational entries first published in the last 24 h
        "entries_by_kind": {"threat": 2, "vulnerability": 2, "research": 1},
        "entries_updated": 1,            # entries that received an updates[] changelog record in the last 24 h
        "updates": 1,                    # alias of entries_updated (kept for the prompt's older wording)
        "deep_dives_today": 1,         # deep_dive entries with today's folder date
        "critical_count": 0,           # priority: critical in last 24 h
        "high_count": 2
      }
    }

Usage:
    python3 tools/run_summary.py [--out PATH] [--recent-days N] \
        [--gap-runs N] [--gap-window N] [--now ISO8601Z]
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402


def _load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None


def _host(url: str) -> str:
    """Normalised host of a URL: lowercase, no leading `www.`, no port."""
    if not url:
        return ""
    rest = url.split("//", 1)[-1]
    host = rest.split("/", 1)[0].split("@")[-1].split(":", 1)[0].lower()
    return host[4:] if host.startswith("www.") else host


def _promotion_due(srcs: list, promote_after: int) -> list:
    """Candidates that have earned promotion to `active`.

    The source lifecycle promotes `candidate` → `active` after N contributing
    runs, but a fire has no memory of earlier fires, so nothing was ever
    counting — the 2026-07-26 audit found 11 candidates long past the bar,
    one of them cited by 11 distinct runs. A contributing run is a distinct
    `run_id` among the published entries whose frontmatter `sources[]` cites
    the candidate's host (or a subdomain of it).
    """
    cand_hosts: dict[str, str] = {}
    for s in srcs:
        if s.get("status") != "candidate" or not s.get("id"):
            continue
        host = _host(s.get("url") or "") or _host(s.get("rss_url") or "")
        if host:
            cand_hosts[s["id"]] = host
    if not cand_hosts:
        return []
    runs_by_cand: dict[str, set] = {cid: set() for cid in cand_hosts}
    for e in cm.collect_entries():
        rid = e.get("run_id")
        if not rid:
            continue
        hosts = {_host(rec.get("url") or "")
                 for rec in (e.get("sources") or []) if isinstance(rec, dict)}
        hosts.discard("")
        for cid, chost in cand_hosts.items():
            if any(h == chost or h.endswith("." + chost) for h in hosts):
                runs_by_cand[cid].add(rid)
    return [
        {"id": cid, "contributing_runs": len(rids), "last_run_id": max(rids)}
        for cid, rids in sorted(runs_by_cand.items(),
                                key=lambda kv: (-len(kv[1]), kv[0]))
        if len(rids) >= promote_after
    ]


def _recent_attempts(runs: list, attempt_runs: int) -> dict:
    """Source ids the last `attempt_runs` INTEL fires already handed to a
    sub-agent, as {"runs": [run_id, ...], "ids": [source_id, ...]}.

    The staleness rotation (cti-run.md Phase 0 allocation rule 2) ranks
    standard-tier sources oldest-`last_successful_fetch` first, and that field
    moves only when a source is fetched AND used. A source swept every fire
    that yields nothing publishable therefore keeps its stale date, stays
    pinned to the head of a stable ranking, and is re-selected indefinitely
    while everything below it starves. Over 2026-09-13 to 09-20 six
    consecutive fires drew an almost identical S3 slice and four research
    publishers that published in-window were allocated to no fire at all; the
    audit recovered six publishable items from them. This list is what the
    rotation subtracts so the ranking can actually advance.

    Audit records are excluded: the audit's own re-sweeps are not the
    rotation's work and must not suppress a source for the next intel fire.
    """
    ids: set = set()
    used: list = []
    for run in reversed(runs):
        if run.get("kind") != "intel":
            continue
        if len(used) >= attempt_runs:
            break
        used.append(run.get("run_id"))
        for sa in (run.get("sub_agents") or {}).values():
            if not isinstance(sa, dict):
                continue
            for sid in (sa.get("sources_attempted") or []):
                if isinstance(sid, str) and sid:
                    ids.add(sid)
    return {"runs": list(reversed(used)), "ids": sorted(ids)}


def build_summary(now: datetime, recent_days: int, gap_runs: int,
                  gap_window: int, promote_after: int = 3,
                  attempt_runs: int = 2) -> dict:
    today = now.strftime("%Y-%m-%d")
    out: dict = {"today": today, "now": now.strftime("%Y-%m-%dT%H:%M:%SZ")}

    # --- CVEs -------------------------------------------------------------
    cves_doc = _load_json(ROOT / "state" / "cves_seen.json") or {}
    cves = cves_doc.get("cves") or []
    cutoff = (now - timedelta(days=recent_days)).strftime("%Y-%m-%d")
    out["cves"] = {
        "count": len(cves),
        "ids": sorted({c.get("id") for c in cves if c.get("id")}),
        "recent": [
            {k: c.get(k) for k in ("id", "first_seen", "last_seen", "title")}
            for c in cves if (c.get("last_seen") or "") >= cutoff
        ],
    }

    # --- Sources ----------------------------------------------------------
    src_doc = _load_json(ROOT / "sources" / "sources.json") or {}
    srcs = src_doc.get("sources") or []
    by_status = {"active": [], "demoted": [], "candidate": []}
    for s in srcs:
        by_status.setdefault(s.get("status", ""), []).append(s.get("id"))
    out["sources"] = {
        "active_count": len(by_status["active"]),
        "active_ids": sorted(i for i in by_status["active"] if i),
        "demoted_ids": sorted(i for i in by_status["demoted"] if i),
        "candidate_ids": sorted(i for i in by_status["candidate"] if i),
        "promotion_due": _promotion_due(srcs, promote_after),
    }

    # --- Runs (runs/** via content_model) ----------------------------------
    runs = cm.collect_runs()
    last = runs[-1] if runs else None
    gap_counter: dict = {}
    for run in runs[-gap_window:]:
        for f in run.get("fetch_failures") or []:
            if not isinstance(f, dict) or not f.get("id"):
                continue
            rec = gap_counter.setdefault(f["id"], {"runs_failing": 0, "last_status": None})
            rec["runs_failing"] += 1
            rec["last_status"] = f.get("status_code", f.get("code", f.get("status")))
    out["runs"] = {
        "count": len(runs),
        "last_run": (
            {k: last.get(k) for k in ("run_id", "kind", "date", "started",
                                      "completed", "publish_status")}
            if last else None
        ),
        "fetch_gaps_in_window": [
            {"id": sid, **rec}
            for sid, rec in sorted(gap_counter.items())
            if rec["runs_failing"] >= gap_runs
        ],
        "recent_attempts": _recent_attempts(runs, attempt_runs),
    }

    # --- 24 h budget snapshot (entries/**) ----------------------------------
    since = now - timedelta(hours=24)
    by_kind: dict = {}
    updates = deep_dives_today = critical = high = operational = 0
    for e in cm.collect_entries():
        if e.get("deep_dive") and e.get("date") == today:
            deep_dives_today += 1
        # v4.0 entry lifecycle: an entry counts as UPDATED in the window when
        # any of its changelog records was made inside it (regardless of
        # when the entry was first published).
        if any(isinstance(u, dict)
               and (uts := cm.parse_ts(u.get("at"))) is not None
               and since <= uts <= now + timedelta(minutes=5)
               for u in (e.get("updates") or [])):
            updates += 1
        ts = cm.parse_ts(e.get("discovered_at"))
        if ts is None or ts < since or ts > now + timedelta(minutes=5):
            continue
        operational += 1
        by_kind[e.get("kind", "?")] = by_kind.get(e.get("kind", "?"), 0) + 1
        if e.get("priority") == "critical":
            critical += 1
        elif e.get("priority") == "high":
            high += 1
    out["window24h"] = {
        "operational_total": operational,
        "entries_by_kind": by_kind,
        "entries_updated": updates,
        "updates": updates,
        "deep_dives_today": deep_dives_today,
        "critical_count": critical,
        "high_count": high,
    }
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", help="write JSON here instead of stdout")
    ap.add_argument("--recent-days", type=int, default=14)
    ap.add_argument("--gap-runs", type=int, default=2)
    ap.add_argument("--gap-window", type=int, default=7)
    ap.add_argument("--promote-after", type=int, default=3,
                    help="contributing runs after which a candidate source is "
                         "listed under sources.promotion_due (default 3)")
    ap.add_argument("--attempt-runs", type=int, default=2,
                    help="how many previous INTEL fires' sources_attempted lists feed "
                         "runs.recent_attempts, the anti-starvation exclusion set the "
                         "rotation subtracts (default 2)")
    ap.add_argument("--recent-attempts", action="store_true",
                    help="print only the recent-attempts source ids, one per line, and exit")
    ap.add_argument("--now", help="override 'now' (UTC ISO 8601 Z) for testing")
    args = ap.parse_args()

    now = (
        datetime.strptime(args.now, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        if args.now else datetime.now(timezone.utc)
    )
    summary = build_summary(now, args.recent_days, args.gap_runs,
                            args.gap_window, args.promote_after, args.attempt_runs)
    if args.recent_attempts:
        ra = summary['runs']['recent_attempts']
        print(f"# attempted by {len(ra['runs'])} previous intel fire(s): {', '.join(ra['runs']) or 'none'}")
        for sid in ra['ids']:
            print(sid)
        return 0
    payload = json.dumps(summary, indent=1, ensure_ascii=False) + "\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(payload, encoding="utf-8")
        print(f"run_summary: wrote {args.out} ({len(payload)} bytes)")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
