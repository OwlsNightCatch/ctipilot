---
schema: 1
kind: research
horizon: operational
title: "Windows Defender ships its own kernel write primitive: BTR.sys, the signed boot-time remediation driver, takes an encrypted job list from an alternate data stream and will delete or create any file or registry value asked of it"
headline: "No exploit, no vulnerability, nothing to blocklist — the driver is a required Defender component, and its instructions live in a hidden stream on its own file"
summary: >
  Check Point Research published an analysis on 2026-08-20 showing that BTR.sys, the Microsoft-signed
  "Boot Time Removal Tool" driver Windows Defender extracts from MpEngine.dll to finish remediation
  actions that need a reboot, exposes a general-purpose kernel-mode file and registry primitive once
  its transaction format is understood. There is no memory corruption and no vulnerability: the driver
  reads an RC4-encrypted job list from an NTFS alternate data stream on its own file and executes six
  action types, two of which amount to arbitrary file write and arbitrary registry write. Because the
  driver is a functionally required Defender component carrying a genuine signature, it cannot be added
  to the vulnerable-driver blocklist or blocked by WDAC without breaking Defender's own remediation,
  and because the tool extracts it from the local MpEngine.dll there is no third-party binary for a
  blocklist to key on. The precondition is pre-existing administrative privilege, which is why MSRC
  declined to service it; Check Point reports no evidence of real-world abuse.
discovered_at: "2026-08-23T04:55:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, priv-esc, lpe, no-patch, poc-public, default-config]
regions: [global, europe]
sectors: [public-sector, energy, water, transport, healthcare, finance, telco]
entities: [tool:btr-sys-loldriver-primitive]
techniques: [T1685, T1564.004, T1543.003, T1112, T1547.001, T1027]
affected_products: ["Microsoft Windows Defender", "Microsoft Windows"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/"
    publisher: "Check Point Research"
    date: "2026-08-20"
    role: primary
  - url: "https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html"
    publisher: "The Hacker News"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "What if a signed Microsoft remediation driver could be instructed to execute arbitrary file and registry operations from Ring 0 – without exploits, vulnerabilities, or memory corruption?"
    publisher: "Check Point Research"
  - quote: "BTR.sys carries a valid Microsoft signature, meaning it would normally pass signature enforcement, though this does not guarantee permanent trust or classification as \"Known Good\" in all contexts."
    publisher: "Check Point Research"
  - quote: "MSRC confirmed that these findings do not meet the criteria for immediate servicing, as the technique relies on pre-existing administrative privileges (SeLoadDriverPrivilege)."
    publisher: "Check Point Research"
  - quote: "During our analysis across all collected samples and telemetry sources, we did not observe evidence of real-world abuse of BTR.sys in the manner demonstrated in this research. This suggests the technique is currently unknown or unused by threat actors, making proactive detection engineering feasible before weaponization appears in the wild."
    publisher: "Check Point Research"
  - quote: "Recognize that the Microsoft Vulnerable Driver Blocklist (WDAC) does not protect against the abuse of functionally intended drivers like BTR.sys."
    publisher: "Check Point Research"
verification: multi-source
sourcing_note: >
  Check Point Research is the sole assessor of the technical findings; The Hacker News republishes
  Check Point's own statements verbatim rather than corroborating them independently, and is cited
  here only for the two facts it reports in its own right — the Black Hat USA 2026 and DEF CON 34
  presentation venue, which does not appear in Check Point's article text, and the researcher's
  "no patch is planned" characterization, which The Hacker News sources to the tool's own repository
  documentation and explicitly notes Microsoft has not publicly confirmed. The credibility rating
  reflects one assessor with two publishers rather than two independent observations.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: windows-lpe
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Enumerate which accounts and groups hold SeLoadDriverPrivilege across your Windows estate and remove it wherever it is not required — it is the sole precondition for this technique and the only control Microsoft's servicing decision leaves you."
migrated_from: null
---

**Background.** This is not the first time Defender's own remediation driver has drawn scrutiny, and not the first time a legitimate built-in Windows driver has been turned into a kernel-mode weapon against endpoint security. In February 2021 SentinelLabs researcher Kasif Dekel disclosed CVE-2021-24092, a local privilege-escalation flaw in the same BTR.sys file that let an unprivileged user overwrite arbitrary files through a hard link planted at the driver's log path; Microsoft patched it on 2021-02-09, and Dekel's own explanation for why it had gone unnoticed for years is the same property that makes the driver interesting now — it is normally absent from disk entirely, dropped under a random name only when needed and purged afterwards, so routine static scanning never sees it ([The Hacker News, 2026-08-21](https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html)). Separately, FIN7's AvNeutralizer tooling previously demonstrated the same class of move — repurposing genuinely built-in Windows drivers rather than importing a known-vulnerable third-party one — against endpoint security software ([The Hacker News, 2026-08-21](https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html)). What Check Point adds is a fully documented, general-purpose primitive in a component every Windows install carries.

**What the driver is.** BTR.sys — "Boot Time Removal Tool" — is a genuine Microsoft-signed kernel driver embedded as a PE resource inside `MpEngine.dll`. Defender extracts it to `System32\drivers` under a randomised filename, with a matching randomised service name, only when a remediation action cannot complete without a reboot, such as deleting a file held under an exclusive lock. It is a one-shot design: it loads, executes a queued list of transactions, writes a status report, and requests its own unload. Check Point's researcher found it by accident during an incident response, where telemetry that looked like attacker kernel-loader tradecraft — a randomly named driver, a transient service, RC4 routines, alternate-data-stream interaction and self-cleanup — turned out to be this legitimate Defender mechanism ([Check Point Research, 2026-08-20](https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/)). The framing question the research opens with is the whole finding: *"What if a signed Microsoft remediation driver could be instructed to execute arbitrary file and registry operations from Ring 0 – without exploits, vulnerabilities, or memory corruption?"*

**How it takes instructions.** The driver exposes no IOCTL interface. At load time it reads the `Args` value of its own transient service registry key, which points at an NTFS alternate data stream on the driver file itself — the configuration is hidden data attached to the driver's own file object rather than a separate visible file. That stream holds an RC4-encrypted transaction blob. Check Point assembled eighteen unique Microsoft-signed 64-bit builds of the driver — collected from a public Windows-binary index and a malware-sample service, then de-duplicated — and reports that all of them share the same hard-coded 256-byte key, noting *"a remarkable consistency in the internal BTR.sys codebase"* across that set. That is a best-effort sample collection rather than a census of every build ever shipped, but it spans a long enough range for the reuse to be the point. Integrity uses a modified CRC-32 in which the final inversion step is omitted, applied independently to each of the four structures in the format rather than cumulatively, so tampering with one structure cannot be compensated for in a later one. On completion the driver returns `STATUS_DELETE_PENDING` rather than success — the code that tells the kernel to unload it immediately and mark its object for deletion, so it does not linger for a live-response kernel-module enumeration to find.

**The primitive.** The decrypted transaction is a list of items, each carrying a four-byte action ID, and Check Point enumerates six: delete file (kernel-level, bypassing exclusive locks), delete directory, move or quarantine, delete registry key, delete registry value, and set registry value. Two of the six are the ones that matter. Of the move action, Check Point writes: *"Weaponization: If Dest Path is empty, this acts as a Delete operation. If Dest Path is valid, this allows Arbitrary File Write/Move (e.g., dropping a malicious DLL into System32)."* Of the set-value action: *"Weaponization: Can be used to establish persistence (Run keys, Services) or disable security controls (Tamper Protection, EDR configs). Creates not only a value but possibly the registry key path itself."* Everything else in the chain is ordinary administrative work.

**Why no blocklist helps.** The driver carries a real signature, so signature enforcement is simply not engaged — *"BTR.sys carries a valid Microsoft signature, meaning it would normally pass signature enforcement, though this does not guarantee permanent trust or classification as \"Known Good\" in all contexts."* Adding it to Microsoft's Vulnerable Driver Blocklist or blocking it under WDAC would disable Defender's own boot-time remediation on every Windows install, which is why neither control has been applied. Check Point's own conclusion is blunt: *"Recognize that the Microsoft Vulnerable Driver Blocklist (WDAC) does not protect against the abuse of functionally intended drivers like BTR.sys."* This is the distinction between bring-your-own-vulnerable-driver and living-off-the-land-driver technique: BYOVD depends on a third-party signed driver that can be blocklisted once identified, whereas here the driver is extracted from the machine's own `MpEngine.dll` each time, leaving no external binary or hash for a blocklist to key on.

**The boot-order window.** Check Point found the driver cannot run at `SERVICE_BOOT_START`, because its entry routine needs file I/O before the Object Manager has established the SystemRoot symbolic link and the storage stack is ready — *"empirical testing confirms a hard architectural constraint: BTR.sys cannot function as a SERVICE_BOOT_START (Start=0) driver."* Staged instead as `SERVICE_SYSTEM_START` in the "Boot Bus Extender" load-order group — exactly as `MpEngine.dll` stages it legitimately — it lands early in the next phase. Check Point's own boot-time trace on a fully patched Windows 11 25H2 puts execution roughly 0.32 seconds after Defender's minifilter loads, about 56 milliseconds *before* the User Choice Protection driver, and some 34 seconds before the user-mode Defender service starts. In that window the minifilter is present but operating without user-mode intelligence behind it, and the service that would lock and self-protect Defender's own binaries has not started. Check Point's tests in that window deleted the minifilter, the Defender service binary and the network-inspection driver before the service could start, and deleted Defender service registry keys at runtime despite Tamper Protection being active — because Tamper Protection is enforced primarily against user-mode processes, and these operations originate from a signed kernel driver.

**Vendor position.** Following disclosure, per Check Point's account, *"MSRC confirmed that these findings do not meet the criteria for immediate servicing, as the technique relies on pre-existing administrative privileges (SeLoadDriverPrivilege)."* No CVE has been assigned. Check Point frames the underlying issue as an architectural trust boundary crossable by an attacker who already holds administrative rights rather than a vulnerability in the traditional sense. A separate claim that no patch is planned comes from the researcher's own tool documentation as relayed by The Hacker News, which notes Microsoft has not confirmed it publicly. A proof-of-concept implementing the full pipeline has been published under an open-source licence; this entry does not link it.

**Detection.** Check Point's own detection opportunities are behavioural and, unusually, apply to a technique with no in-the-wild use yet — *"During our analysis across all collected samples and telemetry sources, we did not observe evidence of real-world abuse of BTR.sys in the manner demonstrated in this research. This suggests the technique is currently unknown or unused by threat actors, making proactive detection engineering feasible before weaponization appears in the wild."* Leading with the telemetry class: in **file-stream creation telemetry** (Sysmon event ID 15), alert on an alternate data stream named `:changelist` created on a `.sys` file — Check Point calls this high fidelity, and its stated discriminator between legitimate and abusive use is where the *feedback* report is written, since Defender's own usage directs it to a standalone file under a protected ProgramData path while the research tool directs it to a second stream on the driver file. In **driver-load telemetry** (event ID 6), the anchor is lineage: a legitimate load is dropped and registered by the Defender service, so a matching driver loaded by a shell, a script host or an unknown binary is the signal. In **registry telemetry** (event IDs 12 and 13), a service key whose `Args` value references a `:changelist` stream and whose group is "Boot Bus Extender" is notable specifically for what does *not* accompany it — no service-installation event (Windows event ID 7045), because creating the key directly and loading through the undocumented syscall bypasses the Service Control Manager entirely. In **file-deletion telemetry** (event ID 23), correlate deletions attributed to the System process immediately following such a driver load, and watch for the rapid creation and deletion of the driver's hardcoded boot-clean log, which fires regardless of caller.

**Defender takeaway:** driver-hash matching and signature trust are both structurally unable to catch this, and Microsoft's servicing decision means neither will change. The control surface that remains is the privilege that gates it — audit and reduce `SeLoadDriverPrivilege` holdings — and behavioural rules that treat a security vendor's own driver loading outside that vendor's expected process lineage as suspicious regardless of its signature. **Triage:** every artefact this technique produces is also produced by Defender doing its job, so no single event distinguishes them; the separators are the process lineage behind the driver load, the absence of a service-installation event alongside the service key, and the destination of the feedback stream. A `:changelist` stream on a `.sys` file is expected on a machine where Defender has scheduled a boot-time removal — it is the combination with an unexpected parent, or with no corresponding service-installation record, that is worth an analyst's time.
