---
schema: 1
kind: vulnerability
horizon: operational
title: "UPDATE — the ShieldBreak mechanism is published: two colliding object-manager symlinks named WD_SCAN make Windows Defender's own clean engine write an attacker's DLL into System32, and wermgr.exe loads it as SYSTEM"
headline: "ShieldBreak, mechanically: Defender writes the payload, a scheduled task runs it, and one file path is a near-zero-false-positive hunt"
summary: >
  LevelBlue SpiderLabs published the working mechanism of the unpatched Windows Defender privilege-escalation
  chain this pipeline has tracked as ShieldBreak: a fake Cloud Files sync root, two conflicting object-manager
  symbolic links both named WD_SCAN, an exclusive lock on the CLFS transaction log that freezes Defender's clean
  operation mid-flight, and a symlink swap that redirects the in-flight write so Defender's own remediation engine
  places an attacker-supplied phoneinfo.dll into System32 — after which a crafted Windows Error Report triggers the
  built-in QueueReporting task and wermgr.exe loads that DLL as SYSTEM. Roughly eight to twelve seconds, standard
  user to SYSTEM, on fully patched Windows 11 24H2 and Windows Server 2025 with Defender in its default
  configuration. There is still no vendor fix, so detection is the whole available control — and the mechanism
  supplies it, led by the presence of C:\Windows\System32\phoneinfo.dll, which LevelBlue states is not
  expected to exist natively on supported Windows versions.
discovered_at: "2026-08-24T09:11:00Z"
event_date: "2026-08-19"
run_id: 2026-08-24T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, lpe, priv-esc, no-patch, poc-public, identity]
regions: [global]
sectors: [public-sector, technology]
entities:
  - actor:nightmare-eclipse
  - trend:shieldbreak-defender-rogueplanet-patch-bypass-2026-08
techniques: [T1574.001, T1053.005, T1036.005, T1027.007, T1106, T1218]
affected_products: ["Microsoft Windows 11", "Microsoft Windows Server 2025", "Microsoft Defender Antivirus"]
cves:
  - id: CVE-2026-69414
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [no-patch, poc-public]
    affected: "Windows 11 24H2 and Windows Server 2025 with Windows Defender in its default configuration, fully patched as of the August 2026 updates"
    fixed: "no fix available — Microsoft states a security update is still being worked on"
sources:
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking"
    publisher: "LevelBlue SpiderLabs"
    date: "2026-08-19"
    role: primary
closed_sources: []
evidence:
  - quote: "ShieldBreak is fully self-contained and runs to full SYSTEM completion from a standard user account on any fully patched Windows 11 24H2 or Windows Server 2025 system with Windows Defender in its default configuration."
    publisher: "LevelBlue SpiderLabs"
  - quote: "ShieldBreak is best detected through behavioral correlation rather than any single static indicator."
    publisher: "LevelBlue SpiderLabs"
  - quote: "The set of expected MpClient.dll consumers is small. A load by an unrelated process becomes especially significant when followed by runtime resolution of MpManagerOpen, MpScanStart, MpCleanOpen, MpCleanStart, or MpCleanControl."
    publisher: "LevelBlue SpiderLabs"
verification: single-source
sourcing_note: >
  Single-source for the mechanism: LevelBlue SpiderLabs is the only party to have published it, and its own account
  states its OpsCTI and THOR teams reviewed and reproduced the full chain. One sourcing caveat matters and is stated
  in the body: the LevelBlue post names no CVE anywhere — confirmed by a case-insensitive search of the full fetched
  page body — so tying this mechanism to CVE-2026-69414 is this pipeline's reading of two accounts of the same named
  technique, not a claim either party makes. The CVE record, its 7.8 score and the absence of a fix come from the
  vendor advisory carried in the entry this one updates, not from LevelBlue.
confidence: high
update_of: 2026-08-18/cve-2026-69414-shieldbreak-defender-acknowledged-no-fix
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Hunt for C:\\Windows\\System32\\phoneinfo.dll across the Windows estate now — LevelBlue states the file is not expected to exist natively on supported Windows versions, so an instance on a supported build is either this chain or an unrelated planted DLL, and either warrants investigation."
migrated_from: null
---

**UPDATE (originally covered 2026-08-18):** the entry this one updates recorded that Microsoft had acknowledged ShieldBreak as CVE-2026-69414, rated it 7.8, assessed it "Exploitation More Likely", and stated a security update was still being worked on — with no published mechanism and therefore nothing to detect on. LevelBlue SpiderLabs has now published the mechanism and, with it, a hunting package ([LevelBlue SpiderLabs, 2026-08-19](https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking)). That is the whole delta, and it matters because no fix exists: detection is currently the only control a defender has.

The chain turns Windows Defender's own remediation path into the write primitive. The proof-of-concept registers its working directory as a **Cloud Files sync root**, self-identifying as a sync provider with a hardcoded provider GUID and creating a placeholder file. It then creates two directories beneath the object manager's `\BaseNamedObjects\Restricted\` namespace and, inside them, **two conflicting symbolic links both named `WD_SCAN`** — one initially resolving to the working directory holding the placeholder, the other to a path used by the Common Log File System. It opens Defender's interface directly, resolving the management, scanning and clean functions out of `MpClient.dll` at runtime, and asks Defender to scan the placeholder through a `\\.\globalroot\...\WD_SCAN\` path. A background thread watches for the CLFS transaction log that Defender's clean operation creates, and the instant it appears takes an **exclusive lock** on it — freezing Defender mid-transaction. With the operation held open, the proof-of-concept deletes the shadow `WD_SCAN` link and recreates it pointing at `\??\UNC\127.0.0.1\C$\Windows\System32\phoneinfo.dll`, so the already-in-flight path resolves somewhere new without any NTFS junction being involved; it then restarts Cloud Files hydration with the file size set to the DLL's rather than the original's, so the hydration callback supplies the attacker's bytes while Defender's clean engine performs the write. Because `MsMpEng.exe` is the process that writes the file, the write itself looks expected — which LevelBlue flags as a triage detail that must be correlated rather than dismissed. The proof-of-concept then maps the resulting DLL as an executable image to stop remediation removing it, crafts a Windows Error Report into the report queue, and triggers the **built-in `QueueReporting` scheduled task through the Task Scheduler COM interface method `ITaskService::Run()`**; that task runs as SYSTEM, so the signed Windows error-reporting binary `wermgr.exe` processes the report and loads `phoneinfo.dll` with SYSTEM privileges — a trusted system binary acting as the proxy that executes the attacker's code, which is how the payload runs without the attacker ever launching a process of their own. LevelBlue states the whole sequence takes approximately eight to twelve seconds on an unloaded system, and that it "is fully self-contained and runs to full SYSTEM completion from a standard user account on any fully patched Windows 11 24H2 or Windows Server 2025 system with Windows Defender in its default configuration."

Detection, in the report's own framing, "is best detected through behavioral correlation rather than any single static indicator" — but one static indicator is close to free. LevelBlue identifies **`C:\Windows\System32\phoneinfo.dll`** as the strongest single indicator in the chain and states the file **is not expected to exist natively on supported Windows versions** — so its creation warrants a high-priority look regardless of the process that wrote it. (The hedge is the source's own and is worth keeping: "not expected on supported versions" is what it will bear, not a guarantee about every Windows build ever shipped.) Beyond that, and led by telemetry class: in image- and module-load telemetry, `MpClient.dll` loaded by a process that is not one of Defender's own small set of expected consumers — the report names `MsMpEng.exe`, `MpCmdRun.exe`, `NisSrv.exe`, `ConfigSecurityPolicy.exe` and `MpSigStub.exe` — is the compound signal, and LevelBlue is specific about what makes it load-bearing: "The set of expected MpClient.dll consumers is small. A load by an unrelated process becomes especially significant when followed by runtime resolution of MpManagerOpen, MpScanStart, MpCleanOpen, MpCleanStart, or MpCleanControl." The same telemetry should surface `wermgr.exe` loading `phoneinfo.dll`. In scheduled-task audit records, the `QueueReporting` task being started programmatically through the Task Scheduler COM interface is the execution step. In registry or filter telemetry, a sync-root registration call issued by a process that is not a cloud-sync client is the setup step. And in named-pipe telemetry this specific proof-of-concept creates a pipe with a hardcoded name, with a SYSTEM-integrity process then connecting to a pipe a normal user created — though that name is an artefact of this build rather than of the technique.

**Triage:** every individual event here has a benign twin, which is why the sequence is the detection. `MsMpEng.exe` writing into System32 is normal remediation behaviour; a cloud-sync provider registering a sync root is normal on a machine running OneDrive or a similar client; `wermgr.exe` running as SYSTEM off a scheduled task is normal error reporting. The discriminators are the process identities and the ordering: a sync-root registration from something that is not a sync client, `MpClient.dll` resolved by a non-Defender process followed by that specific clean-function set, and a `QueueReporting` run driven through COM rather than by the ordinary error-reporting trigger — with the whole chain completing inside roughly ten seconds. Hardening is the awkward part: because the abused component is Defender itself in its default configuration and Microsoft has declined to ship a fix so far, there is no configuration change to apply, and the vulnerable-driver blocklist and application-control policies have nothing third-party to key on.
