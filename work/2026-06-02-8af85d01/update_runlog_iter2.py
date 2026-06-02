#!/usr/bin/env python3
import json, pathlib
ROOT = pathlib.Path("/home/user/ctipilot")

# fix covered_items Dragon Weave delta to not propagate the SteppeDriver/UNC5221 attribution error
cip = ROOT / "state/covered_items.json"
ci = json.loads(cip.read_text())
for it in ci["items"]:
    if it["key"] == "campaign:operation-dragon-weave":
        for ap in it["appearances"]:
            if ap["date"] == "2026-06-02":
                ap["delta_summary"] = ("First coverage + deep dive. RUSTCLOAK Rust dropper -> DLL side-load -> "
                                       "AZUREVEIL (AdaptixC2) with Azure Blob Storage dead-drop C2. Seqrite attributes to a "
                                       "China-based cluster (moderate confidence), no named group; no source connects it to SteppeDriver/UNC5221.")
cip.write_text(json.dumps(ci, indent=2, ensure_ascii=False) + "\n")
print("covered_items: Dragon Weave delta corrected")

# record iter2 in run_log
p = ROOT / "state/run_log.json"
rl = json.loads(p.read_text())
rec = next(r for r in rl["runs"] if r["run_id"] == "2026-06-02-8af85d01")
iter2 = {
    "n": 2,
    "model": "Claude Sonnet 4.6",
    "model_id": "claude-sonnet-4-6",
    "started_at": "2026-06-02T04:51:54Z",
    "ended_at": "2026-06-02T04:56:01Z",
    "duration_seconds": 247,
    "verdict": "NEEDS_FIXES",
    "truth": 2,
    "editorial": 0,
    "advisory": 0,
    "findings": [
        {"code": "F13", "category": "analytical-link-as-fact", "section": "deep-dive",
         "item": "Operation Dragon Weave",
         "url_or_quote": "link to SteppeDriver/UNC5221 tooling comes from The Hacker News",
         "summary": "iter1 remediation incomplete: THN presents SteppeDriver/UNC5221 as distinct clusters with no stated connection to Dragon Weave; opening clause still implied THN established a link.",
         "remediation_applied": "Rewrote attribution: states the clusters are distinct/separate and that neither Seqrite nor THN connects Dragon Weave to them; removed 'link to ... tooling' framing.",
         "remediation_outcome": "fixed-clean"},
        {"code": "F5", "category": "missing-citation", "section": "tldr",
         "item": "TL;DR Netlogon bullet",
         "url_or_quote": "stack-based buffer overflow in `netlogon.dll`",
         "summary": "BleepingComputer says 'Windows Netlogon' not 'netlogon.dll'; DLL filename unsupported by cited source.",
         "remediation_applied": "Replaced `netlogon.dll` with 'the Windows Netlogon service' in the TL;DR bullet.",
         "remediation_outcome": "fixed-clean"},
    ],
    "telemetry": {"webfetch_calls": 15, "websearch_calls": 0, "bridge_fetches": 1, "urls_checked": 19},
}
rec["verification"]["iterations"].append(iter2)
rec["verification_iterations"] = 2
rec["verification_residual_count"] = 2  # provisional, matches NEEDS_FIXES iter2; reset to 0 if iter3 CLEAN
rl["last_updated"] = "2026-06-02"
p.write_text(json.dumps(rl, indent=2, ensure_ascii=False) + "\n")
print("run_log: iter2 recorded; verification_iterations=2")
