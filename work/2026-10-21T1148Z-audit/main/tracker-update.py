"""Wave 04 tracker update (cleanup-coordinator § C5 step 5), applied to the plan.json synced from main.

Usage: python3 tracker-update.py "<one-line wave outcome>"
Closes W2-01 and W4-09, adds the rows wave 04 files, notes W4-07, W4-08 and W4-10,
marks wave 04 done and wave 12 ready once wave 05 is done too. Idempotent on the row ids.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = ROOT / "work" / "cleanup" / "plan.json"
RUN = "2026-10-21T1148Z-audit"
DAY = "2026-10-22"
SRC = f"wave 04 ({RUN}), docs/audits/2026-10-21-cleanup-wave-04.md"

NEW = [
    ("W4-12", "W4", "12", "Tycoon 2FA after the March 2026 takedown, 2026-05-18 (OAuth device authorization) vs 2026-05-27 (two-tier AiTM operation): check whether they are one finding; fold or link through references[]. The 2026-05-18 member was re-verified by wave 04, the 2026-05-27 one sits in W2-02 (wave 05)",
     ["2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori", "2026-05-27/tycoon-2fa-after-the-march-2026-takedown-two-tier-aitm-opera"]),
    ("W4-13", "W4", "07", "Datadog Security Labs on the leaked TeamPCP Shai-Hulud framework (2026-05-15) vs TeamPCP open-sourcing its Mini Shai-Hulud framework (2026-06-09): check whether the later entry is a development of the same finding; fold, link or leave. The 2026-05-15 member was re-verified by wave 04",
     ["2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off", "2026-06-09/teampcp-open-sources-its-mini-shai-hulud-framework-spawning"]),
    ("W4-14", "W4", "12", "West Pharmaceutical Services 8-K Item 1.05 (2026-05-12) and its 8-K/A confirming full operational restoration (2026-05-22): one incident, the later filing a development of it; fold 2026-05-22 into 2026-05-12 carrying its verified facts. The 2026-05-12 member was re-verified by wave 04, the 2026-05-22 one sits in W2-02 (wave 05)",
     ["2026-05-12/west-pharmaceutical-services-files-sec-form-8-k-item-1-05-da", "2026-05-22/west-pharmaceutical-services-8-k-a-confirms-full-operational"]),
    ("W4-15", "W4", "06", "Link candidates (references[] only, internal records): Microsoft MDASH (2026-05-13), which Microsoft says found CVE-2026-41089 and CVE-2026-41096, and the 2026-05-13 entry covering those CVEs; the Grafana Labs CoinbaseCartel breach (2026-05-19) and the 2026-05-28 Nx Console / TanStack / Daemon Tools cascade entry, which says Grafana Labs traced its breach to the TanStack compromise. Check each against its sources before linking",
     ["2026-05-13/microsoft-mdash-multi-model-agentic-vulnerability-discovery", "2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898", "2026-05-19/grafana-labs-coinbasecartel-breach-victim-confirms-source-co", "2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands"]),
    ("W4-16", "W4", "12", "Link candidate (references[] only): F5 BIG-IP/BIG-IQ iControl REST CVE-2026-41225 (2026-05-17) and the 2026-05-15 nginx / F5 WAF CVE-2026-42945 entry; SecurityWeek counts BIG-IP, BIG-IQ and NGINX fixes in one F5 notification, so link only if the two entries cover the same release",
     ["2026-05-17/cve-2026-41225-f5-big-ip-big-iq-icontrol-rest-manager-role-a", "2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea"]),
    ("W4-17", "W4", "09", "Link candidate (references[] only): CERT Polska's SzafirHost CVE-2026-44088 JAR/ZIP polyglot (2026-05-17) and CERT Polska's 2026-06-30 JAR parser confusion RCE (CVE-2026-13165) in the same product, a different flaw; link the later entry to the earlier one if its sources build on it",
     ["2026-05-17/cert-pl-cve-2026-44088-szafirhost-jar-zip-polyglot-bypass-in", "2026-06-30/cert-polska-discloses-a-jar-parser-confusion-rce-in-the-szaf"]),
    ("W5-07", "W5", "standalone", "actor:webworm-fishmonger-aquatic-panda-eset-echocreep-graphworm-eu lists FishMonger, Aquatic Panda, SixLittleMonkeys and Space Pirates as aliases, which ESET (2026-05-20) treats as related or tenuously linked groups, not other names; campaign:fishmonger-isoon-sprysocks-windows-kernel-rootkit is attributed-to Webworm (source 2026-06-17/fishmonger-i-soon-ports-its-sprysocks-backdoor-to-windows-wi) only through that alias. Move the aliases to typed relations (related-to / overlaps-with) where a source states them and re-key the FishMonger edge",
     []),
    ("W5-08", "W5", "12", "Registry summaries wave 04 found unsupported on records keyed by entries of other waves: actor:kimsuky (HTTPSpy RAT and European targets, check against 2026-05-30/kimsuky-velvet-chollima-deploys-httpspy-rat-and-rust-based-h); campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac (MiniPlasma 'the third PoC', no June 2026 CVE-2020-17103 fix); actor:akira ('edge-device CVE chains and intermittent-encryption EDR evasion' is unsourced, CISA AA24-109A gives VPN access through known CVEs and full or partial encryption); campaign:clickfix-macos-2026 ('expands to macOS ... bypass Gatekeeper': per Microsoft 2026-05-06 the campaign shifted from disk images to ClickFix Terminal commands)",
     []),
    ("W5-09", "W5", "standalone", "incident:drupal-core-highly-critical-pre-patch-warning-psa-2026-05-18 is keyed by no entry and its summary says no CVE at announcement (CVE-2026-9082 since); wave 04 folded the Drupal twin into 2026-05-20/drupal-core-highly-critical-pre-patch-warning-unauthenticate. Fix the summary and key it from the survivor, or tombstone it if it duplicates a live key",
     []),
    ("W6-08", "W6", "standalone", "Coverage gap: CVE-2026-41940 (cPanel & WHM authentication bypass, CISA KEV since 2026-04-30 with known ransomware use) has no entry of its own; the 2026-05-10 cPanel entry mentions it in passing. Research it from cPanel's advisory and the KEV record and publish it, or record why it does not clear the gate",
     ["2026-05-10/cpanel-whm-second-emergency-tsr-in-10-days-embargo-lifted-on"]),
    ("W7-18", "W7", "standalone", "Operator decision: law-enforcement entries without attacker TTP content (2026-05-16 BKA Dream Market arrest, kind threat, a laundering indictment) cannot meet the threat/incident attack-mapping gate honestly; wave 04 kept T1597.002 (the market sold stolen personal data) as the only sourced behavior. Decide on a kind or a gate rule for such entries",
     ["2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in"]),
]

NOTES = {
    "W4-07": "wave 04 re-verified the Calypso member: neither Lumen nor PwC uses the name Bronze Medley, so the alias on campaign:calypso-red-lamassu-showboat-jfmbackdoor-linux-windows-telco is unsourced; PwC names the actor Red Lamassu (Calypso), which has no actor record yet.",
    "W4-08": "wave 04 added CyberInsider's later update to the 2026-05-19 entry (Charter dataset leaked, 4.9 million email addresses per Have I Been Pwned); when resolving, the Charter facts belong with the 2026-05-27 entry.",
    "W4-10": "wave 04 re-verified and corrected the 2026-05-19 Chaotic Eclipse entry; it still lacks the 2026-06-09 CVE-2020-17103 fix. See also 2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes (wave 03).",
}


def main():
    outcome = sys.argv[1]
    p = json.loads(P.read_text(encoding="utf-8"))
    rows = {r["id"]: r for r in p["rows"]}
    rows["W2-01"]["status"] = f"done {RUN}"
    rows["W4-09"]["status"] = f"done {RUN}: the patch-window entry folded into the PSA-2026-05-18 entry"
    for rid, text in NOTES.items():
        old = rows[rid].get("note")
        if text not in (old or ""):
            rows[rid]["note"] = f"{old} {DAY}: {text}" if old else f"{DAY}: {text}"
    for rid, ws, wave, item, entries in NEW:
        if rid in rows:
            continue
        r = {"id": rid, "workstream": ws, "item": item, "entries": entries, "size": max(1, len(entries)),
             "wave": wave, "status": "open", "source": SRC, "note": None}
        p["rows"].append(r)
        rows[rid] = r
    waves = {w["wave"]: w for w in p["waves"]}
    waves["04"]["status"] = f"done {RUN}: {outcome}"
    done = {k for k, w in waves.items() if w["status"].startswith("done")}
    readied = []
    for k, w in waves.items():
        if w["status"] == "planned" and all(a in done for a in w["after"]):
            w["status"] = "ready"
            readied.append(k)
    w12 = waves["12"]
    if "W4-12" not in w12["rows"]:
        w12["rows"] += "; W4-12, W4-14, W4-16, W5-08 (wave 04)"
    for k, extra in (("06", "W4-15 (wave 04)"), ("07", "W4-13 (wave 04)"), ("09", "W4-17 (wave 04)")):
        if extra.split()[0] not in waves[k]["rows"]:
            waves[k]["rows"] += f", {extra}"
    new_ids = ", ".join(r[0] for r in NEW)
    p["log"].append(f"{DAY}: wave 04 ({RUN}) done: W2-01 closed (74 records, one fold that closes W4-09); "
                    f"new rows {new_ids}; notes on W4-07, W4-08 and W4-10"
                    + (f"; wave(s) {', '.join(readied)} marked ready" if readied else "")
                    + ". Report docs/audits/2026-10-21-cleanup-wave-04.md.")
    P.write_text(json.dumps(p, indent=1, ensure_ascii=True) + "\n", encoding="utf-8")
    print("ok; readied:", readied)


if __name__ == "__main__":
    main()
