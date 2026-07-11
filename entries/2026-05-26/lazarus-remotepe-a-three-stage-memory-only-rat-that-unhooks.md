---
schema: 1
kind: threat
horizon: operational
title: "Lazarus \"RemotePE\": a three-stage memory-only RAT that unhooks EDR and blinds ETW"
headline: "Lazarus \"RemotePE\": a three-stage memory-only RAT that unhooks EDR and blinds ETW"
summary: "Deep dive: Fox-IT/NCC Group dissects \"RemotePE\", a three-stage memory-only Lazarus RAT that DPAPI-keys its loader to one host, fetches its final stage into memory only (never on disk), and pairs HellsGate/TartarusGate syscall unhooking with an ETW patch to blind userland EDR telemetry — product-agnostic detection-engineering content for hunters (§ 5) (Fox-IT, 2026-05-22)."
discovered_at: "2026-05-26T05:00:06Z"
event_date: 2026-05-25
run_id: 2026-05-26-ae9d0d4b
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - infostealer
  - north-korea-nexus
regions:
  - global
  - europe
sectors:
  - finance
entities:
  - "tool:remotepe"
cves: []
sources:
  - url: "https://blog.fox-it.com/2026/05/22/remotepe-the-lazarus-rat-that-lives-in-memory/"
    publisher: "Fox-IT, 2026-05-22"
    role: primary
  - url: "https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html"
    publisher: "The Hacker News, 2026-05-25"
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
migrated_from: briefs/2026-05-26.md
---

**Background.** Fox-IT (NCC Group) attributes RemotePE to a Lazarus sub-cluster whose activity overlaps the AppleJeus, Citrine Sleet (UNC4736) and Gleaming Pisces operations against financial and cryptocurrency organisations, and notes capability lineage with the group's earlier PondRAT/POOLRAT tooling — for example a shared file-deletion routine ([Fox-IT, 2026-05-22](https://blog.fox-it.com/2026/05/22/remotepe-the-lazarus-rat-that-lives-in-memory/)). The toolset is not new in the wild — Fox-IT recovered four RemotePE samples compiled between July 2023 and mid-2024 across multiple incident-response engagements — but neither the loader nor the final RAT had appeared on public malware repositories before this write-up, which is the point: the chain is engineered so that the components that matter never touch disk on the analyst's terms. The chain reads as a clean, modern North-Korea-nexus tradecraft reference: environmental keying, on-the-fly EDR unhooking, ETW suppression, and a final stage that exists only in memory ([The Hacker News, 2026-05-25](https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html)).

**Stage 1 — DPAPILoader (on-disk, environmentally keyed).** The first stage decrypts the second stage from disk using the Windows Data Protection API (DPAPI) keyed to the victim machine, so the payload is only decryptable on the intended host and yields nothing if copied to an analyst sandbox ([`T1480.001`](https://attack.mitre.org/techniques/T1480/001/) Environmental Keying; [`T1140`](https://attack.mitre.org/techniques/T1140/) Deobfuscate/Decode), with an additional single-byte XOR layer over the blob ([Fox-IT, 2026-05-22](https://blog.fox-it.com/2026/05/22/remotepe-the-lazarus-rat-that-lives-in-memory/)). For persistence, DPAPILoader is registered as a Windows service DLL masquerading as `C:\Windows\System32\Iassvc.dll` — a near-homograph of the legitimate Internet Authentication Service DLL `iassvcs.dll` (note the dropped trailing `s`) — giving automatic-start execution under `svchost` ([`T1543.003`](https://attack.mitre.org/techniques/T1543/003/) Windows Service). Encrypted payloads are stashed inside `C:\ProgramData\Microsoft\Windows\DeviceMetadataStore\en-US\` among legitimate Cabinet metadata files, blending with normal OS content.

**Stage 2 — RemotePELoader (fetch + unhook + blind).** The second stage beacons over HTTP to a command-and-control server and waits to receive the final stage ([`T1071.001`](https://attack.mitre.org/techniques/T1071/001/) Web Protocols). Before doing anything else it performs two evasion steps. It resolves Windows syscall numbers at runtime using **HellsGate (the TartarusGate variant)** — remapping `ntdll`/`KnownDlls` to recover clean syscall stubs for `NtOpenSection`, `NtMapViewOfSection`, `NtUnmapViewOfSection`, `NtProtectVirtualMemory` and `NtClose`, defeating userland EDR hooks placed on those NTAPI functions ([`T1562.001`](https://attack.mitre.org/techniques/T1562/001/) Disable or Modify Tools; [`T1106`](https://attack.mitre.org/techniques/T1106/) Native API). It then patches `EtwEventWrite()` in-process so the function returns immediately, suppressing Event Tracing for Windows generation and blinding ETW-backed telemetry ([`T1562.006`](https://attack.mitre.org/techniques/T1562/006/) Indicator Blocking).

**Stage 3 — RemotePE (memory-only RAT).** The final stage is a C++ RAT loaded reflectively and executed **entirely in process memory, never written to disk** ([`T1055.002`](https://attack.mitre.org/techniques/T1055/002/) Portable Executable Injection). Its capabilities are deliberately modest and operator-driven: shell command execution, file read/write, file deletion with a multi-pass overwrite (the routine Fox-IT links to PondRAT/POOLRAT), and C2 polling with configurable sleep intervals ([`T1059`](https://attack.mitre.org/techniques/T1059/), [`T1070.004`](https://attack.mitre.org/techniques/T1070/004/) File Deletion). Initial access is social-engineering via Telegram — the actor impersonates a prospective contact and sends scheduling links on look-alike Calendly/Picktime-style domains to lure the target into the loader ([`T1566`](https://attack.mitre.org/techniques/T1566/)).

**Detection concepts (no IOCs).** This chain is built to defeat disk forensics and static signatures, so the detection surface is behavioural and largely in memory:
- **Service-DLL anomaly.** Alert on service-creation (Windows EID `7045`) or service-DLL registration pointing at `Iassvc.dll` — the legitimate IAS DLL is `iassvcs.dll`; the missing `s` is the tell. Compare all service DLLs against a blessed-DLL allowlist.
- **ETW-write tampering.** Monitor for in-process patching of `ntdll!EtwEventWrite` — EDRs that place kernel callbacks on writes to mapped `ntdll` regions will surface this; a sudden cessation of ETW events from a service process is a secondary signal.
- **Syscall-unhooking / KnownDlls remap.** Surfaces as PEB module-list traversal and `\KnownDlls` section-object mapping from a non-loader context — visible via memory-integrity callbacks or process-tampering telemetry.
- **Memory-only payload.** Hunt for HTTP(S) beacons from processes that have no backing PE on disk at the beacon origin, and periodically scan service-process memory for reflective-PE characteristics; disk imaging alone will not recover RemotePE.
- **Decoy-store writes.** Sysmon EID `11` for files written under `DeviceMetadataStore\en-US\` whose extensions are not the expected Cabinet/metadata types.

**Hardening / mitigation.** Enforce a service-DLL allowlist and block service registration of unsigned or unexpected DLLs in `System32`; restrict write access to `DeviceMetadataStore` to `SYSTEM`; enable AMSI and, where available, kernel-mode telemetry that does not depend solely on userland NTAPI hooks (the unhooking specifically targets userland hooks, so kernel-callback-based EDR sensors retain visibility). For the financial/treasury and any crypto-adjacent teams that are the named victim profile — including European financial institutions in Lazarus's target verticals — treat unsolicited Telegram scheduling links as a credential/loader-delivery TTP and route them through the same scrutiny as email attachments.
