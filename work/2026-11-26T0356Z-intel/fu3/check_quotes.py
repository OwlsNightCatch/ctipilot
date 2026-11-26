#!/usr/bin/env python3
"""Check that every quote in deepread.yaml is a contiguous single-line substring
of its saved body (grep -F equivalent), and that entry sentences are contiguous
substrings of a line of the entry file."""
import sys, os, yaml

BASE = "/home/user/ctipilot/work/2026-11-26T0356Z-intel/fu3"
REPO = "/home/user/ctipilot"

def lines_of(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().split("\n")

cache = {}
def has(path, needle):
    if path not in cache:
        cache[path] = lines_of(path)
    return any(needle in ln for ln in cache[path])

doc = yaml.safe_load(open(os.path.join(BASE, "deepread.yaml"), encoding="utf-8"))
bad = 0
ok = 0
report = []
for item in doc["items"]:
    entry_path = os.path.join(REPO, item["entry"])
    for c in item.get("delta_claims", []):
        quotes = []
        if "quote" in c:
            quotes.append(c["quote"])
        quotes += c.get("quotes", [])
        gv = c.get("grep_verified", True)
        for q in quotes:
            p = os.path.join(BASE, c["body_file"])
            if has(p, q):
                ok += 1
                report.append(f"OK    {c['id']:8} {c['body_file']}" + ("" if gv else "  (webfetch-notes: transcript, not raw body)"))
            else:
                bad += 1
                report.append(f"FAIL  {c['id']:8} {c['body_file']} :: {q[:100]!r}")
        for key in ("supersedes_entry_quote", "tension_with_entry_quote"):
            if key in c:
                if has(entry_path, c[key]):
                    ok += 1
                    report.append(f"OK    {c['id']:8} entry:{key}")
                else:
                    bad += 1
                    report.append(f"FAIL  {c['id']:8} entry:{key} :: {c[key][:100]!r}")
        for s in c.get("also_stale_entry_sentences", []):
            if has(entry_path, s):
                ok += 1
                report.append(f"OK    {c['id']:8} entry:also_stale")
            else:
                bad += 1
                report.append(f"FAIL  {c['id']:8} entry:also_stale :: {s[:100]!r}")
    for st in item.get("entry_statements_now_stale_or_incomplete", []):
        if has(entry_path, st["sentence"]):
            ok += 1
            report.append(f"OK    item{item['id']} stale-list: {st['location'][:40]}")
        else:
            bad += 1
            report.append(f"FAIL  item{item['id']} stale-list: {st['sentence'][:100]!r}")
print("\n".join(report))
print(f"\nSUMMARY ok={ok} fail={bad}")
sys.exit(1 if bad else 0)
