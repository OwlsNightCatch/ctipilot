---
title: Active Exploitation of CVE-2026-110936 in Siemens Software Center
url: https://productcert.siemens.com/news/2026/10/19/active-exploitation-of-cve-2026-110936-in-siemens-software-center/
hostname: siemens.com
sitename: productcert.siemens.com
date: "2026-10-19"
fingerprint: ae8438bfe2e34e00
---
# Active Exploitation of CVE-2026-110936 in Siemens Software Center

Siemens has validated that there is an active exploitation of [CVE-2026-110936](https://www.cve.org/CVERecord?id=CVE-2026-110936), a DLL side-loading vulnerability in **Siemens Software Center**. Siemens fixed the weakness in version **4.0.9.8** and published advisory [**SSA-580366**](https://productcert.siemens.com/productcert/html/ssa-580366.html) on 15 October. Existing installations update automatically the next time they start.

No Siemens system, product or update channel was breached to our knowledge. EDR vendors and authorities have been engaged for intelligence sharing, enabling broader detection coverage and coordinated defensive actions.

## What Happened

The attackers used a genuine copy of Siemens Software Center with a valid signature and placed their own files next to it. They chose this program as a carrier because it is signed and trusted, and because version 3.5.8.7, the latest version at the time, loaded helper files from its own folder without checking them.

The Siemens program was not modified. The malicious code is in the DLL files the attackers supplied, which the vulnerable version loaded when it started.

## Indicators of Compromise

The table below lists the infrastructure we have seen in this campaign. Indicators are defanged to prevent accidental clicks.

| Type | Indicator | Status | Role | 
|---|---|---|---|
| IP address | `96.62.218[.]59` | **Active** | Payload hosting / Command and control | 
| Domain | `wizardexpensive[.]com` | **Active** | Payload hosting / Command and control | 
| IP address | `2.27.248[.]127` | Inactive | Distribution channel of the malware bundle `AllMyBasic.msi` | 

**Active** indicators were still reachable when this post was published. Block them and look for them in your logs. The **inactive** distribution channel no longer serves files, but systems that downloaded from it before it went offline may still be infected.

### Malicious File Hashes

| File | SHA-256 | 
|---|---|
| `AllMyBasic.msi` | `f4d7c5321bb0d1bda439304a753bcf9b467b98ca53c7e9493b9c2c3451092e4a` | 
| `archive.dll` | `3fdcc7d7d049a89711fb31fb236940a1c5a09d899143ffd20c3c41fb1f2cf491` | 

### Threat Actor Attribution

Romulus multi-platform ClickFix campaign

## How to Tell if a PC Is Affected, and What to Do

### Warning signs on a PC

- "Siemens Software Center" in the start-up apps or Task Scheduler of a PC that never had it installed
- A folder called `SM Software Provisioning Service` inside `AppData\Local\Programs` is created by the malware
- Files named `activate.bak` or `statinfosta.DB` next to `SiemensSoftwareCenter.exe`
- A folder called `FTSuite` containing a file `ftc.uml` inside `AppData\Local`
- Network connections to `96.62.218[.]59`

### What everyone should do

- Never paste a command from a web page into Win+R, the Run box or PowerShell. A real "I am not a robot" check never asks for this.
- Keep Siemens Software Center up to date (4.0.9.8 or later).

### What defenders should do

- Block `96.62.218[.]59`, `wizardexpensive[.]com` and `2.27.248[.]127`
- Look for `SiemensSoftwareCenter.exe` running from `AppData\Local\Programs` and started by `msiexec`
- If found: isolate the PC, stop the process first, then remove the start-up entry and task, and reset passwords
- Detect on folder and behaviour, not on the Siemens file fingerprint: **the file itself is genuine**

## Recommendations

- **Update Siemens Software Center** to version 4.0.9.8 or later. Starting the application installs the update automatically.
- **Only download Siemens software from [official Siemens sources](https://www.siemens.com/en-us/support/siemens-software-center/).** The attackers distributed the signed program together with their malicious files outside official channels.
- **Block the active IP address and domain** listed above on firewalls, proxies and DNS resolvers.
- **Search your logs** for connections to the indicators above, including the inactive distribution channel.
- **Look for unexpected DLL files** next to `Siemens Software Center` executables outside the default installation folder.
- If you find signs of compromise, isolate the affected system and follow your incident response process.

## References

\[1\] [Siemens Security Advisory SSA-580366](https://productcert.siemens.com/productcert/html/ssa-580366.html)

\[2\] [CVE-2026-110936](https://www.cve.org/CVERecord?id=CVE-2026-110936)

\[3\] [Siemens Software Center Download](https://www.siemens.com/en-us/support/siemens-software-center/)

## Contact

Report suspected security issues in Siemens products to [Siemens ProductCERT](https://productcert.siemens.com/#get-in-touch-with-siemens-productcert-or-siemens-cert)
