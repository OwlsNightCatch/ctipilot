#!/usr/bin/env python3
"""Bump last_successful_fetch on sources that contributed content today."""
import json
from pathlib import Path

SOURCES = Path("sources/sources.json")
TODAY = "2026-05-20"

# Source IDs that contributed in-window content this run (based on cited URLs in brief).
# These should have last_successful_fetch = today + counters reset.
USED_SOURCE_IDS = {
    "msrc-blog",             # MSRC update guide — CVE-2026-41091, 45584, 45585
    "advisories-ncsc-nl",    # cited as part of S1 discovery trace
    "bsi-de",                # BSI WID-SEC-2026-1583 (vm2), WID-SEC-2026-1579 (Drupal)
    "ncsc-ch-security-hub",  # NCSC.ch CSH post 12584 (Drupal)
    "bleepingcomputer",      # DirtyDecrypt PoC, BleepingComputer Storm-2949 corroboration
    "hackernews",            # The Hacker News — Drupal, vm2, SEPPmail, Nx Console, actions-cool
    "securityweek",          # Drupal coverage
    "cert-pl",               # CERT-PL CVE-2026-42096 advisory
    "enisa",                 # EUVD-2026-30931 reference
    "msft-ti",               # Microsoft Threat Intelligence — Fox Tempest + Storm-2949
    "talos",                 # Cisco Talos BadIIS
    "therecord",             # Fox Tempest + Huawei VRP + Ofcom
    "infoguard-ch",          # InfoGuard Labs SEPPmail writeup
    "sans-isc",              # TeamPCP SANS aggregation referenced
    "wiz-blog",              # Mini Shai-Hulud TanStack referenced
}


def main():
    with open(SOURCES) as f:
        data = json.load(f)

    sources = data.get("sources", [])
    by_id = {s["id"]: s for s in sources}

    bumped = 0
    not_found = []

    for sid in USED_SOURCE_IDS:
        if sid in by_id:
            s = by_id[sid]
            s["last_successful_fetch"] = TODAY
            # Reset failure counter if present (compatible with v2.59 schema)
            for key in ("consecutive_fetch_failures", "consecutive_failures",
                        "consecutive_quiet_periods"):
                if key in s:
                    s[key] = 0
            bumped += 1
        else:
            not_found.append(sid)

    with open(SOURCES, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"sources/sources.json: bumped={bumped} not_found={not_found}")


if __name__ == "__main__":
    main()
