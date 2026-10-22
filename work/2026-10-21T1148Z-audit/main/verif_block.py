"""Render the run record's verification.iterations[] block from the verifier outputs (cleanup wave 04).

Usage: python3 verif_block.py > block.yaml
Iteration 1 = the three first-pass slices (one iteration, findings from all three); iteration 2 = the
post-fix pass. Remediation text per finding comes from main/iter1-remediation.md (iteration 1) and
main/iter2-remediation.md (iteration 2), keyed by the finding refs (s<k>#<n> / i2#<n>).
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

W = Path(__file__).resolve().parents[1]
TRUTH = {"F1", "F2", "F3", "F4", "F13", "F14", "F15"}
EDIT = {"F5", "F6", "F7", "F8", "F9", "F10", "F12", "F16", "F17", "F18"}


def q(s):
    return json.dumps(s, ensure_ascii=False)


def remed(log, ref):
    pat = re.compile(rf"(?<![\w#]){re.escape(ref)}(?!\d)")
    lines = [l.lstrip("- ").strip() for l in log if pat.search(l)]
    return " | ".join(lines) if lines else "not logged"


def secs(a, b):
    f = "%Y-%m-%dT%H:%M:%SZ"
    return int((datetime.strptime(b, f) - datetime.strptime(a, f)).total_seconds())


def counts(fs):
    t = sum(f["code"] in TRUTH for f in fs)
    e = sum(f["code"] in EDIT for f in fs)
    return t, e, len(fs) - t - e


def emit(it, role, start, end, verdict, fs, refs, log, tokens, in_scope, checked, extra=None):
    t, e, a = counts(fs)
    out = [f"    - iteration: {it}", '      subagent_type: "cti-verification"', '      model: "Sonnet 5.5"',
           '      model_id: "claude-sonnet-5-5"', f"      role: {q(role)}", f'      started_at: "{start}"',
           f'      ended_at: "{end}"', f"      duration_seconds: {secs(start, end)}", f"      verdict: {verdict}",
           f"      truth: {t}", f"      editorial: {e}", f"      advisory: {a}",
           f"      claims_in_scope: {in_scope}", f"      claims_checked: {checked}", f"      subagent_tokens: {tokens}"]
    for k, v in (extra or {}).items():
        out.append(f"      {k}: {v}")
    out.append("      findings:" if fs else "      findings: []")
    for f, ref in zip(fs, refs):
        out += [f"        - code: {f['code']}", f"          entry: {q(f['section'])}",
                f"          summary: {q(f['item'] + ': ' + f['summary'])}",
                f"          remediation_applied: {q(ref + ' ' + remed(log, ref))}"]
    return out


def main():
    log1 = (W / "main/iter1-remediation.md").read_text().splitlines()
    fs, refs = [], []
    for k in (1, 2, 3):
        s = yaml.safe_load((W / f"verification.iter1.s{k}.findings.yaml").read_text())
        fs += s
        refs += [f"s{k}#{n}" for n in range(1, len(s) + 1)]
    starts = [(W / f"verify.iter1.s{k}.started_at").read_text().strip() for k in (1, 2, 3)]
    ends = [(W / f"verify.iter1.s{k}.ended_at").read_text().strip() for k in (1, 2, 3)]
    out = ["  iterations:"]
    out += emit(1, "first pass, three slices of 532, 493 and 510 claims (the 1,535 claims this fire changed on the 74 updated entries, ledger against base 7e74158), the run record and the wave report against disk",
                min(starts), max(ends), "NEEDS_FIXES", fs, refs, log1, 144491 + 707116 + 714492, 1535, 1535)
    f2 = W / "verification.iter2.findings.yaml"
    if f2.exists():
        meta = json.loads((W / "main/iter2-meta.json").read_text())
        log2 = (W / "main/iter2-remediation.md").read_text().splitlines()
        fs2 = yaml.safe_load(f2.read_text()) or []
        out += emit(2, meta["role"], (W / "verify.iter2.started_at").read_text().strip(),
                    (W / "verify.iter2.ended_at").read_text().strip(), meta["verdict"], fs2,
                    [f"i2#{n}" for n in range(1, len(fs2) + 1)], log2, meta["tokens"],
                    meta["in_scope"], meta["checked"])
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
