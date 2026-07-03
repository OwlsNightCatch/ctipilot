---
schema: 1
kind: research
horizon: operational
title: "SANS ISC — Akira ransomware kill chain reconstructed entirely from SSLVPN syslog and Windows EVTX, no EDR"
headline: "SANS ISC — Akira ransomware kill chain reconstructed entirely from SSLVPN syslog and Windows EVTX, no EDR"
summary: "SANS ISC handler Manuel Humberto Santander Pelaez published a forensic walkthrough on 2026-05-27 reconstructing an Akira ransomware intrusion using only two log sources — SSLVPN syslog and Windows EVTX exports — joined by source IP and normalised time (SANS Internet Storm Center, 2026-05-27). [SINGLE-SOURCE] …"
discovered_at: "2026-05-28T05:00:10Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: notable
immediate_action: null
tags:
  - ransomware
  - identity
  - organized-crime
regions:
  - global
sectors:
  - public-sector
  - education
  - manufacturing
entities:
  - "campaign:sans-isc-akira-kill-chain-sslvpn-syslog-evtx-no-edr"
  - "actor:akira"
cves: []
sources:
  - url: "https://isc.sans.edu/diary/rss/33024"
    publisher: SANS Internet Storm Center
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-28.md
---

SANS ISC handler Manuel Humberto Santander Pelaez published a forensic walkthrough on 2026-05-27 reconstructing an Akira ransomware intrusion using only two log sources — SSLVPN syslog and Windows EVTX exports — joined by source IP and normalised time ([SANS Internet Storm Center, 2026-05-27](https://isc.sans.edu/diary/rss/33024)). **[SINGLE-SOURCE]** — high-reliability technical primary, but no independent corroboration of the specific kill chain. Initial access (`T1078.001` / `T1133`): non-distributed brute force from a single hosting-provider IP against a single local SSLVPN account that had been deprovisioned in Active Directory but remained provisioned as a local firewall user with no MFA. Discovery: EID 4688 captures `nltest.exe /dclist:`, `net.exe group "Domain Admins" /domain`, `net.exe group "Enterprise Admins" /domain`, `whoami.exe /all`, and a renamed `AdFind.exe` variant, all parented `explorer.exe → cmd.exe`. Credential access (`T1558.003` Kerberoasting): a cluster of EID 4769 RC4-encrypted TGS requests for multiple SPNs from a single workstation within a 90-second window. Lateral movement (`T1021.001`): EID 4624 Logon Type 10 chain from jump host to file server, domain controllers, backup server; EID 4672 special-logon privileges on DC. Defense evasion + impact: EID 1102 security-log clear; `sc.exe` / `net stop` of endpoint-protection services (System EID 7036); `vssadmin delete shadows /all /quiet`.

**Why it matters to us:** the diary is a forensic-primer for any SOC operating without full EDR coverage — the standard scenario in smaller public-sector entities and DACH commune networks. Concrete takeaways the SANS ISC author makes directly: reconcile local SSLVPN account directories against AD source-of-truth (`deprovisioned-in-AD-but-retained-in-firewall` is the recurring initial-access pathway in this class); alert on > 50 failed SSLVPN auths from a single source per hour; enable EID 4688 process auditing on every Windows host, set Security log size ≥ 1 GB; alert on RC4 TGS-REP (EID 4769 `EncryptionType=0x17`) for multiple SPNs from one workstation in a short window; EID 1102 security-log clear is incident-grade in every case; time-sync every host including the firewall to the same NTP source so perimeter-to-endpoint joins remain reliable.
