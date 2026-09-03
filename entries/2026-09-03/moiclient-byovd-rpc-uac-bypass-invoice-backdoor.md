---
schema: 1
kind: threat
title: "MoiClient: an invoice-themed backdoor chains an RPC-based UAC bypass with a vulnerable Lenovo PC Manager driver to kill security products and steal browser credentials"
headline: "A debug-object handle borrowed from winver.exe is enough to hijack a self-elevating system binary with no prompt"
summary: >
  AhnLab ASEC documents MoiClient, a backdoor distributed as an invoice-themed .vhdx archive that DLL-sideloads via
  a repackaged SumatraPDF viewer. Once running, it bypasses UAC through an RPC technique against the AppInfo Service
  resembling Google Project Zero's 2019 disclosure, then drops a vulnerable Lenovo PC Manager kernel driver
  (BootRepair.sys) to terminate Defender, Kaspersky, Bitdefender and four other security products, before deploying
  an in-memory "MoiXD Stealer" that harvests browser-stored credentials.
discovered_at: "2026-09-03T05:17:00Z"
updated_at: null
event_date: "2026-09-01"
run_id: 2026-09-03T0410Z-intel
priority: notable
immediate_action: null
tags: [infostealer, organized-crime]
regions: [apac, global]
sectors: [public-sector]
entities:
  - malware:moiclient
techniques: [T1566.001, T1574.001, T1055.012, T1548.002, T1685, T1053.005, T1555.003]
affected_products: ["Microsoft Windows", "Lenovo PC Manager"]
cves: []
sources:
  - url: "https://asec.ahnlab.com/en/95211/"
    publisher: "AhnLab ASEC"
    date: "2026-09-01"
    role: primary
closed_sources: []
evidence:
  - quote: "MoiClient uses the ncalrpc protocol sequence to connect to the RPC interface of the AppInfo Service, then executes winver.Exe as a debug target and acquires the debug object handle."
    publisher: "AhnLab ASEC"
  - quote: "version 2.5.30.11281 Of BootRepair.Sys—a vulnerable driver in Lenovo PC Manager—was exploited. MoiClient creates this driver in the %Public% Path under the name moimoi.Sys"
    publisher: "AhnLab ASEC"
  - quote: "The registered task runs every 30 minutes. At that time, SumatraPDF—named \"demo.Exe\"—is launched, and \"uxtheme.Dll,\" which is located in the same Path and is actually MoiClient, is reloaded."
    publisher: "AhnLab ASEC"
verification: single-source
sourcing_note: >
  AhnLab ASEC is the sole source located for this campaign as of 2026-09-03; no independent corroboration exists.
  Rated B/2 on that basis. The vendor's own published page renders several technical terms with unusual
  capitalization ("winver.Exe", "moimoi.Sys", "demo.Exe") — confirmed via two independent fetch transports as a
  source-side characteristic, not a citation error — so this entry paraphrases those details in prose rather than
  quoting the odd casing directly, while evidence[] preserves it verbatim as required.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

AhnLab's ASEC documents MoiClient — named for the "moimoi" string in its BYOVD component — distributed as a .vhdx
file disguised as an invoice email attachment. The archive contains `Invoice.Pdf.Exe`, actually the legitimate
SumatraPDF viewer, used to DLL-sideload a same-directory malicious `uxtheme.dll`, plus hidden support files
([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95211/)). Execution moves into a legitimate process via
classic process hollowing: MoiClient spawns `explorer.exe` suspended and overwrites its entry point with shellcode
from a co-located `data.dat`. For privilege escalation, MoiClient connects over `ncalrpc` to the RPC interface of
the AppInfo Service, launches `winver.exe` as a debug target to acquire a debug-object handle, then drives
`ComputerDefaults.exe` — a system binary that auto-elevates — through the same RPC path, clones its process handle,
and sets that cloned handle as the parent of subsequent `sc.exe` and PowerShell processes so they inherit elevated
privileges with no UAC prompt shown
([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95211/)). With elevated rights, MoiClient drops a vulnerable
Lenovo PC Manager kernel driver, version 2.5.30.11281 of BootRepair.sys, under the name `moimoi.sys` in the
`%Public%` path, registers it as a kernel service, and uses its device interface to pass process IDs of running
security products for forced termination — targeting Windows Defender, Malwarebytes, Bitdefender, Kaspersky, Avast,
AVG and McAfee by process name
([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95211/)). A separate technique specifically neutralises
Windows Defender: MoiClient downloads `defendnot.dll` and `defendnot-loader.exe` from its command-and-control
server and runs them through the elevated PowerShell session. Persistence is a Task Scheduler job named
`MicrosoftWindowsUpdateTask<4-digit-number>` (or the existing name with a trailing period appended on a collision)
that fires every 30 minutes, re-launching the renamed SumatraPDF binary to re-trigger the DLL-sideload chain
([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95211/)). The final payload, "MoiXD Stealer," runs in memory
and uses a ChromeElevator-style technique to steal browser-stored passwords.

**Triage:** the RPC-based UAC bypass — cloning a process handle obtained through `winver.exe` as a debug target and
attaching it as the parent of `sc.exe` or PowerShell — resembles a technique class Google Project Zero documented
in 2019 against the AppInfo Service; a `sc.exe` or PowerShell process whose parent-process chain traces back through
`winver.exe` or `ComputerDefaults.exe` rather than a normal interactive shell is not typical UAC-elevation behaviour
and is the observable signature the mechanism supports. **Defender takeaway:** check for unintended `explorer.exe`
processes, a Task Scheduler entry matching the naming pattern above, and the presence of
`%Public%\moimoi.sys`, `%LOCALAPPDATA%\uxtheme.dll`, `%LOCALAPPDATA%\data.dat` or
`%LOCALAPPDATA%\defendnot-loader.exe` — AhnLab provides this as an explicit reader checklist, and any one of these
artefacts on an endpoint that has received an unsolicited invoice attachment warrants immediate isolation.
