#!/usr/bin/env python3
"""Update state files for 2026-05-20 brief.

- Bump last_seen on existing CVEs referenced in today's brief.
- Insert new CVEs that aren't in cves_seen.json.
- Append/update covered_items.json with today's items.
- Append a record for deep_dive_history.json.
"""
import json
import re
from pathlib import Path

TODAY = "2026-05-20"
BRIEF = Path("briefs/2026-05-20.md")
CVES_SEEN = Path("state/cves_seen.json")
COVERED = Path("state/covered_items.json")
DD_HISTORY = Path("state/deep_dive_history.json")

# Existing CVEs referenced today (bump last_seen)
EXISTING_BUMP = {
    "CVE-2026-44128": "Refers — InfoGuard Labs 2026-05-18 technical write-up; cluster also addressed by v15.0.4",
    "CVE-2026-44277": "Mentioned in § 7 as out-of-window drop (Fortinet FortiAuthenticator unauth RCE; 2026-05-12 PSIRT)",
    "CVE-2026-26083": "Mentioned in § 7 as out-of-window drop (Fortinet FortiSandbox unauth RCE; 2026-05-12 PSIRT)",
    "CVE-2026-45185": "Mentioned in § 7 as out-of-window drop (Exim Dead.Letter UAF; 2026-05-12 oss-security)",
    "CVE-2026-31431": "Cited as background family member — DirtyDecrypt assessed as Copy Fail variant",
    "CVE-2026-43284": "Cited as background family member — DirtyDecrypt assessed as Copy Fail variant",
    "CVE-2026-43500": "Cited as background family member — DirtyDecrypt assessed as Copy Fail variant",
    "CVE-2026-46300": "Cited as background family member — DirtyDecrypt assessed as Copy Fail variant",
}

# New CVEs to add
NEW_CVES = [
    {
        "id": "CVE-2026-2743",
        "title": "SEPPmail Secure E-Mail Gateway — pre-auth path traversal in LFT /v1/file.app → arbitrary file write as nobody → RCE via /etc/syslog.conf overwrite",
        "primary_source_url": "https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/",
    },
    {
        "id": "CVE-2026-26956",
        "title": "vm2 Node.js sandbox — symbol-to-string coercion TypeError sandbox bypass; patched 3.10.5",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
    },
    {
        "id": "CVE-2026-31635",
        "title": "Linux kernel RxGK rxgk_decrypt_skb() page-cache write (missing COW guard) — DirtyDecrypt LPE; affects Fedora / Arch / openSUSE Tumbleweed (CONFIG_RXGK=y)",
        "primary_source_url": "https://moselwal.com/blog/dirtydecrypt-linux-kernel-rxgk-cve-2026-31635",
    },
    {
        "id": "CVE-2026-41091",
        "title": "Microsoft Defender Malware Protection Engine — link-following EoP to SYSTEM (CWE-59); Engine ≤ 1.1.26030.3008; actively exploited",
        "primary_source_url": "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41091",
    },
    {
        "id": "CVE-2026-42096",
        "title": "Sparx Pro Cloud Server — authenticated SQL injection via database API endpoint; PCS ≤ 6.1",
        "primary_source_url": "https://cert.pl/en/posts/2026/05/CVE-2026-42096/",
    },
    {
        "id": "CVE-2026-42097",
        "title": "Sparx Pro Cloud Server — pre-auth bypass via model-parameter omission in POST binary blob → unauthenticated SQL query execution; CVSS4 9.3",
        "primary_source_url": "https://cert.pl/en/posts/2026/05/CVE-2026-42096/",
    },
    {
        "id": "CVE-2026-42098",
        "title": "Sparx Enterprise Architect ≤ 17.1 — client-side RBAC bypass via EA client binary patch (CWE-603); CVSS4 8.7",
        "primary_source_url": "https://cert.pl/en/posts/2026/05/CVE-2026-42096/",
    },
    {
        "id": "CVE-2026-42099",
        "title": "Sparx Pro Cloud Server WebEA — race condition in /data_api/dl_internal_artifact.php → RCE in web-server context (CWE-362); CVSS4 7.7",
        "primary_source_url": "https://cert.pl/en/posts/2026/05/CVE-2026-42096/",
    },
    {
        "id": "CVE-2026-42100",
        "title": "Sparx Pro Cloud Server — malformed SQL crash (DoS); CWE-835",
        "primary_source_url": "https://cert.pl/en/posts/2026/05/CVE-2026-42096/",
    },
    {
        "id": "CVE-2026-43997",
        "title": "vm2 Node.js sandbox — host-object access via BaseHandler.getPrototypeOf trap; sandbox escape to host context; CVSS 10.0; patched 3.11.0",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
    },
    {
        "id": "CVE-2026-43999",
        "title": "vm2 NodeVM allow-list bypass — Module._load() reachable when child_process is explicitly permitted → OS command execution; CVSS 9.9",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
    },
    {
        "id": "CVE-2026-44005",
        "title": "vm2 prototype pollution via attacker-controlled JS; CVSS 10.0; affects 3.9.6 – 3.10.5; patched 3.11.0",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
    },
    {
        "id": "CVE-2026-44006",
        "title": "vm2 code injection via BaseHandler.getPrototypeOf; CVSS 10.0; patched 3.11.0",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
    },
    {
        "id": "CVE-2026-44008",
        "title": "vm2 null-proto exception exploitation; CVSS 9.8; affects ≤ 3.11.1; patched 3.11.2",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
    },
    {
        "id": "CVE-2026-44009",
        "title": "vm2 neutralizeArraySpeciesBatch() bypass via null-proto exception; CVSS 9.8; affects ≤ 3.11.1; patched 3.11.2",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
    },
    {
        "id": "CVE-2026-45584",
        "title": "Microsoft Defender Malware Protection Engine — heap-based buffer overflow over network → unauthenticated RCE in Defender process context; CVSS 8.1",
        "primary_source_url": "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45584",
    },
    {
        "id": "CVE-2026-45585",
        "title": "Windows BitLocker / WinRE — YellowKey command injection (CWE-77); physical access; CVSS 6.8; PoC public; no patch (WinRE BootExecute mitigation)",
        "primary_source_url": "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585",
    },
]


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=False)
        f.write("\n")


def update_cves_seen():
    data = load_json(CVES_SEEN)
    cves_list = data.get("cves", [])
    by_id = {c["id"]: c for c in cves_list}

    bumped = 0
    added = 0

    for cve_id, note in EXISTING_BUMP.items():
        if cve_id in by_id:
            if by_id[cve_id]["last_seen"] < TODAY:
                by_id[cve_id]["last_seen"] = TODAY
                bumped += 1

    for new in NEW_CVES:
        if new["id"] not in by_id:
            entry = {
                "first_seen": TODAY,
                "id": new["id"],
                "last_seen": TODAY,
                "primary_source_url": new["primary_source_url"],
                "title": new["title"],
            }
            cves_list.append(entry)
            added += 1
        else:
            # already there from prior — bump last_seen
            if by_id[new["id"]]["last_seen"] < TODAY:
                by_id[new["id"]]["last_seen"] = TODAY

    # Sort by id
    cves_list.sort(key=lambda c: c["id"])
    data["cves"] = cves_list
    save_json(CVES_SEEN, data)
    print(f"cves_seen.json: added={added} bumped={bumped} total={len(cves_list)}")


# COVERED ITEMS

COVERED_RECORDS = [
    # § 0 Immediate Action / § 1 Drupal
    {
        "key": "item:drupal-core-highly-critical-pre-patch-warning-psa-2026-05-18",
        "type": "incident",
        "title": "Drupal core highly critical pre-patch warning — PSA-2026-05-18, patch window today 17:00-21:00 UTC; pre-auth, unauthenticated, full-site compromise; no CVE yet",
        "section": "active_threats",
        "primary_source_url": "https://www.drupal.org/psa-2026-05-18",
        "delta_summary": "PSA-2026-05-18 + NCSC.ch Security Hub post 12584 + Immediate Action callout — emergency patch window today 17-21 UTC; all supported branches + EOL emergency manual patches",
    },
    {
        "key": "item:microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-servi",
        "type": "incident",
        "title": "Microsoft DCU disrupts Fox Tempest MSaaS — 1,000+ Artifact Signing certs revoked; SDNY court order; downstream Rhysida, INC, Qilin, Akira + Vanilla Tempest, Storm-0501 / 2561 / 0249",
        "section": "active_threats",
        "primary_source_url": "https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/",
        "delta_summary": "First-coverage; Microsoft Threat Intel + DCU legal action + The Record corroboration; defender takeaways on cert-validity hunting and Conditional Access on Artifact Signing tenant creation",
    },
    {
        "key": "actor:fox-tempest",
        "type": "actor",
        "title": "Fox Tempest — financially motivated MSaaS operator; signspace[.]cloud seized 2026-05-19",
        "section": "active_threats",
        "primary_source_url": "https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/",
        "delta_summary": "First introduction to brief tracking; tied to Vanilla Tempest (Rhysida); active since May 2025",
    },
    {
        "key": "item:sparx-enterprise-architect-pro-cloud-server-five-cve-chain-c",
        "type": "vulnerability-trend",
        "title": "Sparx Enterprise Architect / Pro Cloud Server — five-CVE chain (CVE-2026-42096 to 42100); pre-auth SQL injection + WebEA race-condition RCE; CVSSv4 10.0 chained; PoC public; no vendor patch",
        "section": "active_threats",
        "primary_source_url": "https://cert.pl/en/posts/2026/05/CVE-2026-42096/",
        "delta_summary": "First-coverage; CERT-PL coordinated disclosure 2026-05-19; sploit.tech technical writeup; ENISA EUVD-2026-30929 to 30932",
    },
    {
        "key": "item:actions-cool-issues-helper-github-action-compromised-53-tag",
        "type": "incident",
        "title": "actions-cool/issues-helper GitHub Action compromised — 53 tags moved to imposter commit 1c9e803 reading Runner.Worker /proc/PID/mem for secrets; Mini Shai-Hulud cluster link",
        "section": "active_threats",
        "primary_source_url": "https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials",
        "delta_summary": "First-coverage; StepSecurity 2026-05-18 disclosure; Socket confirms exfil domain overlaps Mini Shai-Hulud cluster",
    },
    {
        "key": "item:nx-console-vs-code-extension-18-95-0-compromised-stolen-publ",
        "type": "incident",
        "title": "Nx Console VS Code extension 18.95.0 compromised — stolen publisher credentials; 11-minute window 2026-05-18 12:36-12:47 UTC; multi-channel stealer + macOS Python backdoor",
        "section": "active_threats",
        "primary_source_url": "https://cybersecuritynews.com/nx-console-vs-code-extension-compromised/",
        "delta_summary": "First-coverage; 2.2M-install extension; harvests GitHub/npm/AWS/HashiCorp/K8s/1Password secrets; safe ver 18.100.0+",
    },
    {
        "key": "item:huawei-vrp-enterprise-router-zero-day-post-luxembourg-2025-o",
        "type": "incident",
        "title": "Huawei VRP enterprise-router zero-day caused POST Luxembourg nationwide telecom outage (23 July 2025); no CVE assigned 10 months later",
        "section": "active_threats",
        "primary_source_url": "https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage",
        "delta_summary": "First-coverage; Recorded Future News investigation; SINGLE-SOURCE high-reliability journalism; vendor advisory-portal disclosure-gap structural finding",
    },
    # § 2 CVEs
    {
        "key": "CVE-2026-41091",
        "type": "cve",
        "title": "Microsoft Defender Engine link-following EoP — CWE-59; actively exploited; Engine ≤ 1.1.26030.3008 vulnerable",
        "section": "trending_vulns",
        "primary_source_url": "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41091",
        "delta_summary": "First-coverage; MSRC 2026-05-19 publication with exploited=Yes, publiclyDisclosed=Yes",
    },
    {
        "key": "CVE-2026-45584",
        "type": "cve",
        "title": "Microsoft Defender Engine network RCE — heap buffer overflow; CVSS 8.1; same Engine update closes both this and CVE-2026-41091",
        "section": "trending_vulns",
        "primary_source_url": "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45584",
        "delta_summary": "First-coverage; MSRC 2026-05-19; no exploitation observed but companion to actively-exploited CVE-2026-41091",
    },
    {
        "key": "CVE-2026-31635",
        "type": "cve",
        "title": "DirtyDecrypt — Linux kernel RxGK rxgk_decrypt_skb() page-cache write; affects Fedora / Arch / openSUSE Tumbleweed; PoC released 2026-05-19",
        "section": "trending_vulns",
        "primary_source_url": "https://moselwal.com/blog/dirtydecrypt-linux-kernel-rxgk-cve-2026-31635",
        "delta_summary": "First-coverage; Zellic/V12 disclosure; kernel patch from 2026-04-25; assessed as Copy Fail family variant",
    },
    {
        "key": "CVE-2026-43997",
        "type": "cve",
        "title": "vm2 sandbox escape via BaseHandler.getPrototypeOf — host-object access; CVSS 10.0; patched 3.11.0",
        "section": "trending_vulns",
        "primary_source_url": "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583",
        "delta_summary": "First-coverage; BSI WID-SEC-2026-1583 flagged 2026-05-19; cluster of 12 vm2 CVEs",
    },
    # § 4 UPDATES
    {
        "key": "CVE-2026-45585",
        "type": "cve",
        "title": "YellowKey BitLocker / WinRE bypass — CVE formally assigned 2026-05-19; MSRC WinRE BootExecute mitigation; no patch",
        "section": "updates",
        "primary_source_url": "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585",
        "delta_summary": "UPDATE: CVE formally assigned (prior coverage 2026-05-15 had no CVE); MSRC published interim WinRE registry mitigation; remains exploit-code-maturity E:P / RL:W",
    },
    {
        "key": "CVE-2026-2743",
        "type": "cve",
        "title": "SEPPmail LFT pre-auth path traversal → arbitrary file write as nobody → RCE via syslog.conf overwrite; CVSS 10.0; addressed by v15.0.4",
        "section": "updates",
        "primary_source_url": "https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/",
        "delta_summary": "UPDATE on 2026-05-09 deep dive cluster: InfoGuard Labs full technical writeup 2026-05-18 reveals new CVE-2026-2743 (CVSS 10.0) atop the prior 6-CVE cluster",
    },
    {
        "key": "item:thegentlemen-raas-czech-university-finance-administration-de",
        "type": "campaign",
        "title": "TheGentlemen RaaS lists Czech University of Finance and Administration (VSFS) and Swiss DEVO-Tech AG on leak site",
        "section": "updates",
        "primary_source_url": "https://www.dexpose.io/thegentlemen-target-university-of-finance-and-administration-in-czech-republic/",
        "delta_summary": "UPDATE on 2026-05-14 backend leak coverage: new EU higher-education + Swiss SMB engineering victims listed (not confirmed); TTPs unchanged",
    },
    # § 5 Deep Dive
    {
        "key": "item:storm-2949-sspr-to-key-vault-azure-cloud-wide-kill-chain",
        "type": "campaign",
        "title": "Storm-2949 SSPR-to-Key-Vault Azure kill chain — voice-phishing SSPR → Entra ID → M365 Graph → App Service Kudu → Key Vault → SQL → Storage → Azure VM, no malware",
        "section": "deep_dive",
        "primary_source_url": "https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/",
        "delta_summary": "First-coverage; Microsoft Threat Intelligence 2026-05-18 incident analysis; BleepingComputer corroboration; defender takeaways on phishing-resistant MFA on privileged Azure roles + SSPR Conditional Access + Defender for Cloud across Key Vault/App Service/Storage/SQL",
    },
    {
        "key": "actor:storm-2949",
        "type": "actor",
        "title": "Storm-2949 — financially motivated, no nation-state attribution; SSPR voice-phishing → multi-resource Azure abuse",
        "section": "deep_dive",
        "primary_source_url": "https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/",
        "delta_summary": "First introduction to brief tracking; Microsoft Threat Intel 2026-05-18 published",
    },
    # § 3 Research
    {
        "key": "item:cisco-talos-badiis-demo-pdb-maas-isapi-backdoor-lwxat-dragon",
        "type": "campaign",
        "title": "Cisco Talos — demo.pdb BadIIS commodity MaaS ISAPI backdoor; lwxat developer alias; builder tool recovered; UAT-8099 / DragonRank link; 1,800+ IIS servers compromised globally",
        "section": "research",
        "primary_source_url": "https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/",
        "delta_summary": "First-coverage; Cisco Talos 2026-05-19; primarily APAC focus; IIS-pipeline hijack pattern relevant for any IIS-fronted CMS",
    },
]


def update_covered_items():
    data = load_json(COVERED)
    items_list = data.get("items", [])
    by_key = {it["key"]: it for it in items_list}
    appended = 0
    updated = 0

    for rec in COVERED_RECORDS:
        key = rec["key"]
        appearance = {
            "date": TODAY,
            "section": rec["section"],
            "brief_path": str(BRIEF),
            "delta_summary": rec["delta_summary"],
        }
        if key in by_key:
            item = by_key[key]
            item["last_covered"] = TODAY
            item.setdefault("appearances", []).append(appearance)
            if rec.get("primary_source_url"):
                item["primary_source_url"] = rec["primary_source_url"]
            updated += 1
        else:
            new_item = {
                "key": key,
                "type": rec["type"],
                "title": rec["title"],
                "first_covered": TODAY,
                "last_covered": TODAY,
                "primary_source_url": rec["primary_source_url"],
                "appearances": [appearance],
            }
            items_list.append(new_item)
            appended += 1

    data["items"] = items_list
    save_json(COVERED, data)
    print(f"covered_items.json: appended={appended} updated={updated} total={len(items_list)}")


def update_deep_dive_history():
    data = load_json(DD_HISTORY)
    entries = data.get("entries", [])

    new_entry = {
        "date": TODAY,
        "category": "cloud-saas",
        "title": "Storm-2949 SSPR-to-Key-Vault Azure cloud-wide kill chain — SSPR voice-phishing → Entra MFA hijack → App Service Kudu → Key Vault → SQL / Storage → Azure VM with no malware",
        "primary_cve": None,
        "brief_path": str(BRIEF),
    }

    # avoid duplicate if rerun
    if not any(e.get("date") == TODAY for e in entries):
        entries.append(new_entry)

    # Cap at 30 most recent
    if len(entries) > 30:
        entries = entries[-30:]

    data["entries"] = entries
    data["last_updated"] = TODAY
    save_json(DD_HISTORY, data)
    print(f"deep_dive_history.json: entries total={len(entries)}; latest={entries[-1]['title'][:50]}...")


if __name__ == "__main__":
    update_cves_seen()
    update_covered_items()
    update_deep_dive_history()
    print("State files updated.")
