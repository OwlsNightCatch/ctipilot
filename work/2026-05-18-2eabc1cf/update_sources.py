#!/usr/bin/env python3
"""Phase 5 sources/sources.json update — mark sources fetched today + add cryptotimes
candidate (one-new-candidate-per-run cap honoured: depthfirst already exists from
2026-05-15)."""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TODAY = "2026-05-18"

path = REPO / "sources" / "sources.json"
with path.open() as fh:
    src = json.load(fh)

# Sources whose content was used in today's brief (S1/S2/S3/S4 returns)
fetched_today = {
    "ncsc-ch-security-hub",  # S2 bridge — NGINX Rift, Exchange, YellowKey
    "enisa",                  # S2 bridge — DHTMLX EUVD entries
    "msft-ti",                # S3 — Microsoft IR HPOM piece
    "bleepingcomputer",       # S2 + S4 — Tycoon2FA / Funnel / Windows zero-days
    "hackernews",             # S1 + S4 — NGINX Rift exploitation, Tycoon2FA
    "securityaffairs",        # S1 — NGINX Rift corroboration
    "therecord",              # S4 — THORChain primary
    "helpnetsecurity",        # S1 — Week in Review
    "unit42",                 # S3 — AD CS ESC1 piece (deferred but fetched)
    "dfirreport",             # S3 — EtherRAT/TukTuk piece (deferred but fetched)
    "kaspersky-securelist",   # noted in prior coverage check; not used today
}
# Strict: only mark a source as fetched if it actually contributed content to the
# brief. Drop those that were fetched but content was deferred.
contributed_today = {
    "ncsc-ch-security-hub",
    "enisa",
    "bleepingcomputer",
    "hackernews",
    "securityaffairs",
    "therecord",
}

updated = []
for entry in src["sources"]:
    if entry["id"] in contributed_today:
        entry["last_successful_fetch"] = TODAY
        entry["consecutive_failures"] = 0
        updated.append(entry["id"])

# Update depthfirst — already a candidate, bump fetch + contribution counter via notes
for entry in src["sources"]:
    if entry["id"] == "depthfirst":
        # Don't bump fetch date — the in-text citation today is via NCSC-CH / news,
        # not a direct fetch of depthfirst.com. But S2 referenced it as discovery,
        # so a second contribution is plausible. Keep last_successful_fetch as-is
        # (2026-05-15) and append a dated note.
        existing_notes = entry.get("notes", "")
        if "2026-05-18" not in existing_notes:
            entry["notes"] = existing_notes + " | 2026-05-18: referenced as discovery source for NGINX Rift CVE-2026-42945 in-the-wild update; not directly cited in today's brief (citations go to The Hacker News + Security Affairs + NCSC-CH)."
        break

# Add cryptotimes as new candidate — one-new-candidate-per-run cap respected
already = any(e["id"] == "cryptotimes" for e in src["sources"])
if not already:
    src["sources"].append({
        "id": "cryptotimes",
        "publisher": "CryptoTimes (cryptotimes.io)",
        "url": "https://www.cryptotimes.io",
        "category": ["research"],
        "reliability": "MEDIUM",
        "language": ["en"],
        "status": "candidate",
        "fetch_method": "webfetch",
        "last_successful_fetch": TODAY,
        "consecutive_failures": 0,
        "notes": "DeFi / blockchain-security publication; surfaced 2026-05-18 by S4 with detailed technical post-mortem of THORChain GG20 TSS exploit citing Chainalysis / PeckShield / Cyvers synthesis. Strong technical depth on cross-chain bridge and MPC custody incidents relevant to FINMA-supervised digital-asset custodians and EU MiCA-regulated venues. Candidate — promote to active after 3 runs with content contribution."
    })
    updated.append("cryptotimes (new candidate)")

with path.open("w") as fh:
    json.dump(src, fh, indent=2, ensure_ascii=False)

print(f"sources.json updated: {len(updated)} entries — {updated}")
