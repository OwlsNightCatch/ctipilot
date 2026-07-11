---
schema: 1
kind: threat
horizon: operational
title: "Windows BitLocker \"YellowKey\" and CTFMON \"GreenPlasma\" zero-days: public PoC, no patch, TPM-only BitLocker bypassed"
headline: "Windows BitLocker \"YellowKey\" and CTFMON \"GreenPlasma\" zero-days: public PoC, no patch, TPM-only BitLocker bypassed"
summary: "Windows BitLocker \"YellowKey\" zero-day (no CVE) bypasses TPM-only disk encryption via WinRE NTFS transaction replay; working PoC is public; no patch available; add BitLocker pre-boot PIN to close the current PoC (BleepingComputer, 2026-05-13)."
discovered_at: "2026-05-15T05:00:01Z"
event_date: 2026-05-14
run_id: 2026-05-15-58b94fbd
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - poc-public
  - no-patch
  - lpe
regions:
  - global
sectors:
  - public-sector
  - defense
  - education
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/"
    publisher: "BleepingComputer, 2026-05-13"
    role: primary
  - url: "https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758"
    publisher: "The Register, 2026-05-13"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12574"
    publisher: "NCSC-CH Security Hub #12574, 2026-05-14"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "**Enforce BitLocker pre-boot PIN on all managed Windows laptops and enforce BIOS/UEFI boot password** — YellowKey (no CVE) bypasses TPM-only BitLocker via WinRE with a public PoC. Group Policy path: `Computer Configuration > Administrative Templates > Windows Components > BitLocker Drive Encryption > Operating System Drives > Require additional authentication at startup` → Enable + require PIN. Disable WinRE access where operationally viable (`reagentc /disable`)."
migrated_from: briefs/2026-05-15.md
---

Researcher "Nightmare Eclipse" published two new unpatched Windows zero-days on 2026-05-12–13 as full-disclosure drops after a disclosure dispute with Microsoft, bringing the total of unpatched Nightmare Eclipse Windows zero-days to four ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/) · [The Register, 2026-05-13](https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758) · [NCSC-CH Security Hub #12574, 2026-05-14](https://security-hub.ncsc.admin.ch/#/posts/12574)). **YellowKey** exploits a Windows Recovery Environment (WinRE) bug in NTFS transaction-log (TxF/FsTx) replay: crafted `FsTx` folder contents placed on a USB drive or the EFI partition are replayed by WinRE during startup, deleting `winpeshl.ini` — the file that suppresses the recovery shell — and dropping the attacker into a CMD prompt with the BitLocker-protected volume already mounted and readable. The current public PoC defeats TPM-only BitLocker configurations on Windows 11 and Windows Server 2022/2025; the researcher asserts the full bypass also defeats TPM+PIN but the unpublished variant is unconfirmed. MITRE ATT&CK: T1542.001 (Pre-OS Boot: System Firmware), T1006 (Direct Volume Access). **GreenPlasma** is a local privilege-escalation flaw in the CTFMON (Collaborative Translation Framework) service: an unprivileged user creates arbitrary section objects in SYSTEM-writable directories, which can be leveraged to manipulate privileged services for a SYSTEM token; the public PoC is partial and the exploit chain triggers a UAC prompt in default configurations. MITRE ATT&CK: T1134 (Access Token Manipulation), T1068 (Exploitation for Privilege Escalation). Neither vulnerability has been assigned a CVE nor received a Microsoft patch as of 2026-05-15; Microsoft states it is "actively investigating." A previous drop by the same researcher (BlueHammer, CVE-2026-33825, now patched) was confirmed used in real-world intrusions by Huntress in April 2026, demonstrating that this researcher's PoCs are operationally adopted. Immediate mitigations: require BitLocker pre-boot PIN (Group Policy `Computer Configuration > Administrative Templates > Windows Components > BitLocker Drive Encryption > Require additional authentication at startup`); set BIOS/UEFI boot password and disable USB/external-media boot; disable WinRE where operationally viable (`reagentc /disable`).
