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
        "last_intel_run": {...same keys...},   # the previous non-stood-down INTEL fire: the PD-7 gap anchor
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
import re
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
            ids.update(_attempted_ids(sa))
    return {"runs": list(reversed(used)), "ids": sorted(ids)}


def _attempted_ids(sa: dict) -> list:
    """`sources_attempted` as a list of ids, tolerating the older shapes.

    Early run records recorded this as a COUNT (int) and a few as a
    comma-separated string; both carry no ids and contribute nothing here.
    Reading them without this guard raises, which is how a latent crash sat in
    `_recent_attempts` until the rotation ranking walked the whole history.
    """
    v = sa.get("sources_attempted")
    if isinstance(v, list):
        return [x for x in v if isinstance(x, str) and x]
    if isinstance(v, str):
        return [x.strip() for x in v.split(",") if x.strip()]
    return []


def _last_attempted(runs: list) -> dict:
    """{source_id: latest date on which an INTEL fire handed it to a sub-agent}.

    Derived from the committed run records, so it needs no new field in
    `sources.json` and no per-fire bookkeeping step that a fire could forget.
    """
    return {sid: at[:10] for sid, at in _last_attempted_at(runs).items()}


def _last_attempted_at(runs: list) -> dict:
    """{source_id: `started` timestamp of the latest INTEL fire that handed it
    to a sub-agent}. Timestamp precision is what the per-source lookback needs:
    a date alone cannot tell a 26 h revisit from a 47 h one."""
    out: dict = {}
    for run in runs:
        if run.get("kind") != "intel":
            continue
        at = str(run.get("started") or run.get("date") or "")
        if not at:
            continue
        # A fetch that failed outright with no alternate coverage read
        # nothing, so it must not advance the cursor: otherwise the next
        # sweep's lookback anchors at the failed attempt and everything the
        # source published before it is never read (keycloak: succeeded
        # 09-13, failed 09-21, next lookback anchored at 09-21).
        failed = {str(f.get("id")) for f in (run.get("fetch_failures") or [])
                  if isinstance(f, dict) and f.get("id") and f.get("covered_anyway") is not True}
        for sa in (run.get("sub_agents") or {}).values():
            if not isinstance(sa, dict):
                continue
            for sid in _attempted_ids(sa):
                if sid in failed:
                    continue
                if at > out.get(sid, ""):
                    out[sid] = at
    return out


LOOKBACK_CAP_HOURS = 168


def _lookback_hours(now: datetime, last_at: str, lsf: str) -> int:
    """Hours a rotational source's next sweep must look back so nothing it
    published since its previous sweep falls between two windows.

    The fire's `window_hours` covers the last ~26 h, so a standard-tier source
    revisited every two or three days would otherwise surface only the posts
    of its final day, and everything before that is never seen by any fire
    (the 2026-09-27 audit recovered 18 research items of exactly this shape).
    Returns hours since the latest of (last attempt, last successful fetch)
    plus a 2 h overlap, capped at LOOKBACK_CAP_HOURS. A source never swept
    gets the cap. The fire takes `max(window_hours, this)` per slice record.
    """
    anchor = None
    for raw in (last_at, lsf):
        if not raw:
            continue
        try:
            ts = datetime.strptime(raw[:19], "%Y-%m-%dT%H:%M:%S") if "T" in raw \
                else datetime.strptime(raw[:10], "%Y-%m-%d")
        except ValueError:
            continue
        ts = ts.replace(tzinfo=now.tzinfo)
        if anchor is None or ts > anchor:
            anchor = ts
    if anchor is None:
        return LOOKBACK_CAP_HOURS
    hours = int((now - anchor).total_seconds() // 3600) + 2
    return max(0, min(LOOKBACK_CAP_HOURS, hours))


def _rotation(srcs: list, runs: list, now: datetime | None = None) -> list:
    """Standard/candidate sources ranked oldest-rotation-cursor first.

    The cursor is `max(last_successful_fetch, last_attempted)`. Ranking on
    `last_successful_fetch` alone does not work, because that field moves only
    when a source is fetched AND used (cti-run.md Phase 5): a source swept
    every fire that yields nothing publishable keeps its stale date forever and
    stays pinned to the head of a ranking that never advances. v4.11 worked
    around that by subtracting the last two fires' attempts, which stopped
    consecutive fires from repeating each other but left the ranking itself
    stable — so the slice cycled with period 3 and everything below the first
    three slices was never reached. Measured over 2026-09-21 to 09-27: mean
    lag-3 slice overlap 82-92 % across all four domains, and 64 of 115
    research sources allocated to no fire at all.

    Counting an ATTEMPT as advancing the cursor makes the ranking a true
    round-robin over the whole pool while `last_successful_fetch` stays what it
    always was, a content-health signal. Essential-tier records are omitted:
    they are attempted every fire by rule and are not part of the rotation.
    """
    last_att_at = _last_attempted_at(runs)
    now = now or datetime.now(timezone.utc)
    rows = []
    for s in srcs:
        sid = s.get("id")
        if not sid or s.get("status") not in ("active", "candidate"):
            continue
        if s.get("tier") == "essential":
            continue
        lsf = s.get("last_successful_fetch") or ""
        la_at = last_att_at.get(sid, "")
        la = la_at[:10]
        rows.append({
            "id": sid,
            "category": list(s.get("category") or []),
            "tier": s.get("tier"),
            "status": s.get("status"),
            "last_successful_fetch": lsf or None,
            "last_attempted": la or None,
            "rotation_key": max(lsf, la) or None,
            "lookback_hours": _lookback_hours(now, la_at, lsf),
        })
    rows.sort(key=lambda r: (r["rotation_key"] or "0000-00-00", r["id"]))
    return rows


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
    # The intel window anchors on the previous INTEL fire that actually swept
    # (PD-7): anchoring on the weekly audit shrank every following fire's
    # window by the audit's offset (gap 15 h instead of 24 h each Monday) and
    # hid real outages from the gap > 24 h backfill trigger.
    intel_runs = [r for r in runs if r.get("kind") == "intel" and not r.get("stood_down")]
    last_intel = intel_runs[-1] if intel_runs else None
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
        "last_intel_run": (
            {k: last_intel.get(k) for k in ("run_id", "kind", "date", "started",
                                            "completed", "publish_status")}
            if last_intel else None
        ),
        "fetch_gaps_in_window": [
            {"id": sid, **rec}
            for sid, rec in sorted(gap_counter.items())
            if rec["runs_failing"] >= gap_runs
        ],
        "recent_attempts": _recent_attempts(runs, attempt_runs),
    }
    # Needs `runs`, so it is filled in after the run collection above.
    out["sources"]["rotation"] = _rotation(srcs, runs, now)

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
    ap.add_argument("--rotation", metavar="CATEGORY", nargs="?", const="",
                    help="print the rotation ranking (oldest cursor first) and exit; "
                         "give a category (research, vulns, breaches, ch-eu, ...) to "
                         "restrict it to that domain's pool")
    ap.add_argument("--rotation-top", type=int, default=20,
                    help="how many rotation rows --rotation prints (default 20; 0 = all)")
    ap.add_argument("--now", help="override 'now' (UTC ISO 8601 Z) for testing")
    args = ap.parse_args()

    # "now" is the Phase 0 network-verified start when the caller passes it
    # (--now "$STARTED") or when --out names the run's work directory; the
    # container clock has been days wrong before (2026-08-24).
    now = None
    if args.now:
        now = datetime.strptime(args.now, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    elif args.out:
        m = re.search(r"(\d{4}-\d{2}-\d{2})T(\d{2})(\d{2})Z-(?:intel|audit)", str(args.out))
        if m:
            now = datetime.strptime(f"{m.group(1)}T{m.group(2)}:{m.group(3)}:00Z",
                                    "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    if now is None:
        now = datetime.now(timezone.utc)
    summary = build_summary(now, args.recent_days, args.gap_runs,
                            args.gap_window, args.promote_after, args.attempt_runs)
    if args.rotation is not None:
        rows = summary["sources"]["rotation"]
        if args.rotation:
            rows = [r for r in rows if args.rotation in (r.get("category") or [])]
        limit = len(rows) if args.rotation_top in (0, None) else args.rotation_top
        print(f"# rotation ranking (oldest cursor first) — {len(rows)} source(s)"
              f"{f' in category {args.rotation}' if args.rotation else ''}, showing {min(limit, len(rows))}")
        print(f"# {'id':<28} {'cursor':<12} {'last_success':<13} {'last_attempted':<15} lookback_h")
        for r in rows[:limit]:
            print(f"{r['id']:<30} {str(r['rotation_key'] or '-'):<12} "
                  f"{str(r['last_successful_fetch'] or '-'):<13} {str(r['last_attempted'] or '-'):<15} "
                  f"{r['lookback_hours']}")
        return 0
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
