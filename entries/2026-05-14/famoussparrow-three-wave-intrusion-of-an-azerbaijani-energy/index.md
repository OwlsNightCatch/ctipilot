---
schema: 1
kind: threat
title: "FamousSparrow Three-Wave Intrusion of an Azerbaijani Energy Operator: ProxyNotShell Re-exploitation and a Wave-1 DLL-Sideload Loader That Overrides Two Hamachi Exports to Defeat Sandbox Analysis"
headline: "FamousSparrow Three-Wave Intrusion of an Azerbaijani Energy Operator: ProxyNotShell Re-exploitation and a Wave-1 DLL-Sideload Loader That Overrides Two Hamachi"
summary: "Deep dive — FamousSparrow (UAT-9244) ran a three-wave intrusion against an Azerbaijani oil & gas operator December 2025–February 2026, re-exploiting the same ProxyNotShell Exchange chain across all three waves despite the victim's attempted remediation, and in Wave 1 deployed Deed RAT via a novel DLL-sideloading technique against a signed LogMeIn Hamachi binary — overriding two specific exported functions (Init, ComMain) and patching StartServiceCtrlDispatcherW so payload execution only fires when the legitimate application's own start-up flow runs. Bitdefender characterises Azerbaijan as a strategic post-Ukraine-transit gas supplier whose deliveries have expanded to 13 European countries (including new flows to Germany and Austria) — making Azerbaijani energy infrastructure a high-value collection target for Chinese state actors monitoring European energy supply dependencies (Bitdefender Labs, 2026-05-13; The Hacker News, 2026-05-13)."
discovered_at: "2026-05-14T05:00:05Z"
event_date: 2026-05-13
run_id: 2026-05-14-e05c6e6e
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
regions:
  - europe
  - apac
sectors:
  - energy
entities: []
cves: []
sources:
  - url: "https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry"
    publisher: "Bitdefender Labs, 2026-05-13"
    role: primary
  - url: "https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html"
    publisher: "The Hacker News, 2026-05-13"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-14.md
---

**Background.** FamousSparrow has been tracked publicly since 2021 as a China-nexus espionage cluster targeting hotels, government and engineering firms; Bitdefender's 2026-05-13 write-up cites tooling and infrastructure overlap with the Earth Estries cluster, and The Hacker News summary additionally notes Salt Typhoon overlap. Recent primary technical detail has been sparse — the Bitdefender Labs publication on 2026-05-13 is the first multi-wave intrusion case study against an energy-sector victim published in some time ([Bitdefender Labs, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry); [The Hacker News, 2026-05-13](https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html)). The Azerbaijan targeting is geopolitically novel for the cluster: Bitdefender characterises Azerbaijani gas-export expansion to 13 European countries (with new flows to Germany and Austria) following the post-Ukraine-transit reconfiguration, making extraction and transit infrastructure intelligence operationally valuable to Chinese state actors monitoring European energy supply dependencies.

**Victim, time-frame, framing.** Bitdefender Labs documented a three-wave intrusion against an unnamed Azerbaijani oil and gas operator spanning **December 2025 to February 2026**, attributed with moderate-to-high confidence to FamousSparrow (also tracked as UAT-9244 in Talos taxonomy). The operationally most consequential framing is not the attribution but the fact that **all three waves re-used the same Exchange initial access vector** despite the victim's attempted remediation — the structural lesson is patch-completeness verification rather than novel-zero-day defence.

**Vulnerability mechanics & initial access.** Initial access in every wave exploited the ProxyNotShell chain — **CVE-2022-41040** (SSRF in the Exchange front-end Auto-discover handler) chained with **CVE-2022-41082** (deserialisation in the back-end PowerShell remoting endpoint) against an on-premises Microsoft Exchange Server. The vulnerable surface is the front-end Exchange `Autodiscover.svc` accepting a crafted IIS request that triggers internal SSRF to the Mailbox role's PowerShell remoting endpoint; the deserialisation in the chained PowerShell context yields code execution under the Exchange application-pool identity (typically `LocalSystem` on the mailbox server). The re-exploitation across three waves indicates either incomplete cumulative-update application (Microsoft's [HealthChecker.ps1](https://github.com/microsoft/CSS-Exchange) is the canonical verification harness) or a persistence foothold — likely a web shell or scheduled task — that survived clean-up rounds and re-armed the same vulnerable code path.

**Exploitation chain mapped to ATT&CK.** Each wave deployed distinct payload combinations on top of the same initial-access foothold:

- **T1190 Exploit Public-Facing Application** — ProxyNotShell against Exchange (each wave).
- **T1505.003 Server Software Component: Web Shell** — surviving persistence from an earlier wave is the most plausible explanation for re-exploitation across remediation attempts.
- **T1059.001 Command and Scripting Interpreter: PowerShell** — Exchange PowerShell remoting deserialisation gadget yields PowerShell execution; subsequent reconnaissance and tooling drop.
- **Wave 1: Deed RAT (Snappybee) deployed via DLL sideloading against a signed LogMeIn Hamachi binary** — Deed RAT is the ShadowPad successor lineage (encrypted C2, file I/O, command execution, process injection). The sideloading is the technique-novelty highlight: per Bitdefender the malicious DLL overrides two of Hamachi's exported functions (`Init`, `ComMain`) and patches `StartServiceCtrlDispatcherW`, so the payload only executes when Hamachi's own service-start path runs. T1574.002 Hijack Execution Flow: DLL Side-Loading is the ATT&CK umbrella, but the override-and-patch detail is what defeats sandbox harnesses: stub harnesses that call DllMain or a small set of obvious exports never trigger `Init` / `ComMain` in the right order and the payload stays dormant.
- **Wave 2: TernDoor deployed via DLL sideloading against a renamed-but-legitimate `deskband_injector64.exe`** — Bitdefender records the second wave as introducing TernDoor as a second backdoor family. The sideloading host is `deskband_injector64.exe` renamed `USOShared.exe` and placed in `C:\ProgramData\USOShared\`; the malicious loader is `winmm.dll` in the same directory. (No legitimate Microsoft "USOShared" signed binary is involved — the directory name is reused for camouflage.)
- **Wave 3: Modified Deed RAT with updated C2 infrastructure** — Bitdefender's third wave is an evolution of Wave 1's implant (refreshed C2, no novel sideloading host), confirming the operator's preference for iterating on the Deed RAT line rather than abandoning it.
- **T1078 Valid Accounts + T1021.001 RDP / T1021.002 SMB** — lateral movement via Impacket, RDP, SMB tooling once the Exchange-server foothold is established.

**Named clusters and shared tooling.** Bitdefender's overlap assessment places FamousSparrow / UAT-9244 in operational relationship with Earth Estries (Trend Micro taxonomy); The Hacker News summary additionally connects the cluster to Salt Typhoon (Microsoft taxonomy). Implants observed include Deed RAT (Snappybee), TernDoor, Mofu Loader and ShadowPad ancestry; the LogMeIn Hamachi sideloading host is freshly observed for this cluster and indicates active tooling rotation rather than reuse of a known signed-binary host.

**Detection and hunt concepts.** Defender-actionable, behavioural — not IOCs:

- **Exchange patch-verification audit**: Run Microsoft's `HealthChecker.ps1` against every on-premise Exchange server and review the output for `Exchange Build` and `Hotfix Applied` lines. CU-level patch status alone is insufficient — the cumulative-update installer occasionally rolls back fixes if an OWA front-end customisation conflicts. Cross-reference IIS log analysis for repeated POST requests to `/autodiscover/autodiscover.json` with non-empty bodies, especially when the same external IP returns over a span of days — the ProxyNotShell exploitation pattern leaves this footprint.
- **Web-shell survival sweep**: Audit the Exchange `FrontEnd\HttpProxy\owa\auth\` and `FrontEnd\HttpProxy\ecp\auth\` directories for files modified post-patch, and the Exchange transport-agents folder for unsigned scheduled tasks. Persistence outliving clean-up was the structural enabler of re-exploitation in this case.
- **LogMeIn Hamachi / signed-binary sideload anomalies**: Hunt for `hamachi*.exe` or `logmein*.exe` loading DLLs from non-standard installation paths, or any legitimately signed binary whose child process tree spawns `cmd.exe` / `powershell.exe` with encoded arguments. The export-override gating makes the loader resilient against generic sandbox detection, but the eventual payload still spawns shell children — Sysmon event ID 1 with `ParentImage` filter on known signed binaries and `CommandLine` patterns for `-EncodedCommand` / `-enc` remains effective. Wave 2's sideloading is the same class of abuse using a renamed legitimate binary — extend the hunt to `deskband_injector64.exe` running from non-standard paths (Bitdefender placed it as `C:\ProgramData\USOShared\USOShared.exe`) and to any `winmm.dll` load from a `ProgramData` subdirectory rather than from the system search path.
- **DLL load-order anomaly hunt**: T1574.002 sideloading depends on a writable DLL search path adjacent to the host binary. Hunt Sysmon event ID 7 (Image Load) records for the Hamachi process loading DLLs from `%LOCALAPPDATA%\Temp\` or other writable user-context paths rather than from the legitimate `Program Files\LogMeIn Hamachi\` install directory.
- **Lateral-movement signatures**: alert on Impacket execution patterns (`smbexec.py` / `wmiexec.py`) — process command lines containing `\\127.0.0.1\admin$` and Win32 service installations with randomly-named binaries (`__output` style) on member servers. RDP from Exchange servers to non-administrative workstations is anomalous regardless of source-account legitimacy.

**Hardening / mitigation.** Concrete configuration toggles, not advice:

- **Exchange**: Apply the latest cumulative update and verify with `HealthChecker.ps1`; deploy Microsoft's mitigation script for ProxyNotShell-class URL rewriting if running an Exchange version still affected. Consider the broader move to Exchange Online for organisations that have not migrated — on-premises Exchange remains a top initial-access vector across China-nexus campaigns.
- **Application-allow-listing**: Enforce Windows Defender Application Control (WDAC) or AppLocker policies that disallow LOLBin-style execution of `logmein*.exe` / `hamachi*.exe` from `%TEMP%` / `%LOCALAPPDATA%` paths. Even legitimately signed binaries should not run from user-writable directories.
- **EDR / Microsoft Defender for Endpoint**: enable "Block executable content from email client and webmail" and "Block all Office applications from creating child processes" ASR rules; these do not directly catch the Hamachi sideload but harden adjacent ingress paths.
- **Conditional Access**: Require modern-authentication and device-compliance for OWA / EAS / Outlook desktop where Exchange Online or hybrid mailboxes are in use; legacy authentication on hybrid setups continues to expose ProxyNotShell-adjacent paths.

**Operationally critical context for Swiss / EU public-sector SOCs.** Per Bitdefender, Azerbaijani gas exports now reach 13 European countries including Germany and Austria — so energy-sector intelligence collection against an Azerbaijani operator is structurally collection against the upstream end of European energy supply. The ProxyNotShell-re-exploitation pattern documented here is not Azerbaijan-specific — any organisation in CH / EU with an on-premise Exchange server that received CU patches but lacks `HealthChecker.ps1`-level verification carries the same exposure. The Wave-3 export-gated sideloading technique generalises to any legitimate signed binary an operator chooses to abuse; defenders should treat it as a class problem (DLL sideloading from signed hosts) rather than a Hamachi-specific signature.
