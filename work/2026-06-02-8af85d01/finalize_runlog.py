#!/usr/bin/env python3
import json, pathlib, subprocess
from datetime import datetime
ROOT = pathlib.Path("/home/user/ctipilot")

# refresh main.ended_at to true end (verification included) for accurate duration
ended = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"]).decode().strip()
(ROOT / "work/2026-06-02-8af85d01/main.ended_at").write_text(ended + "\n")

p = ROOT / "state/run_log.json"
rl = json.loads(p.read_text())
rec = next(r for r in rl["runs"] if r["run_id"] == "2026-06-02-8af85d01")

iter3 = {
    "n": 3,
    "model": "Claude Opus 4.8",
    "model_id": "claude-opus-4-8",
    "started_at": "2026-06-02T05:01:22Z",
    "ended_at": "2026-06-02T05:05:17Z",
    "duration_seconds": 235,
    "verdict": "CLEAN",
    "truth": 0, "editorial": 0, "advisory": 0,
    "findings": [],
    "telemetry": {"webfetch_calls": 12, "websearch_calls": 0, "bridge_fetches": 4, "urls_checked": 16},
}
rec["verification"]["iterations"].append(iter3)
rec["verification_iterations"] = 3
rec["verification_residual_count"] = 0  # final iteration CLEAN
rec["items_dropped_by_verification"] = 0

f = "%Y-%m-%dT%H:%M:%SZ"
rec["completed"] = ended
rec["duration_seconds"] = int((datetime.strptime(ended, f) - datetime.strptime(rec["started"], f)).total_seconds())

rl["last_updated"] = "2026-06-02"
p.write_text(json.dumps(rl, indent=2, ensure_ascii=False) + "\n")
print(f"run_log finalized: 3 iterations, final CLEAN, residual=0, duration={rec['duration_seconds']}s, completed={ended}")
