---
schema: 1
kind: threat
title: >
  Windows BitLocker "YellowKey" (CVE-2026-45585) and CTFMON "GreenPlasma" (CVE-2026-45586) zero-days:
  public PoCs in May, fixed in the June 2026 Windows updates
headline: >
  Leaked BitLocker bypass "YellowKey" and CTFMON privilege escalation "GreenPlasma" were fixed in the June 2026 updates
summary: >
  Nightmare Eclipse published exploit code in May 2026 for YellowKey (CVE-2026-45585), a physical-access
  BitLocker bypass through the Windows Recovery Environment that defeats TPM-only configurations, and
  GreenPlasma (CVE-2026-45586), a CTFMON elevation of privilege to SYSTEM. Microsoft fixed both in the
  June 2026 Windows updates of 2026-06-09 and marks neither as exploited. Microsoft says TPM+PIN blocks YellowKey, which the researcher disputes.
discovered_at: "2026-05-15T05:00:01Z"
updated_at: "2026-10-21T15:38:35Z"
event_date: 2026-05-13
run_id: 2026-05-15-58b94fbd
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - poc-public
  - patch-available
  - lpe
regions:
  - global
sectors: []
entities:
  - "campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac"
  - "actor:nightmare-eclipse"
techniques: [T1059.003, T1005, T1068]
affected_products:
  - "Microsoft Windows 11"
  - "Microsoft Windows 10"
  - "Microsoft Windows Server 2025"
  - "Microsoft Windows Server 2022"
  - "Microsoft Windows Server 2019"
  - "Microsoft Windows Server 2016"
  - "Microsoft Windows Server 2012 R2"
  - "Microsoft Windows Server 2012"
cves:
  - id: CVE-2026-45585
    cvss: "6.8"
    epss: null
    type: null
    vector: physical
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: "Windows 11 24H2, 25H2 and 26H1 and Windows Server 2025 before the June 2026 updates"
    fixed: "Windows 11 24H2 build 10.0.26100.8655, 25H2 build 10.0.26200.8655, 26H1 build 10.0.28000.2269; Windows Server 2025 build 10.0.26100.32995"
  - id: CVE-2026-45586
    cvss: "7.8"
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: "Windows 10, Windows 11 and Windows Server 2012 to 2025 before the June 2026 updates"
    fixed: "June 2026 updates, for example Windows 11 24H2 build 10.0.26100.8655 and Windows Server 2022 build 10.0.20348.5256"
sources:
  - url: "https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/"
    publisher: "BleepingComputer"
    date: "2026-05-13"
    role: primary
  - url: "https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758"
    publisher: "The Register"
    date: "2026-05-13"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12574"
    publisher: "NCSC-CH Security Hub #12574"
    date: "2026-05-14"
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585"
    publisher: "MSRC CVE-2026-45585"
    date: "2026-05-19"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586"
    publisher: "MSRC CVE-2026-45586"
    date: "2026-06-09"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/"
    publisher: "BleepingComputer (June 2026 fixes)"
    date: "2026-06-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: 'Windows looks for \System Volume Information\FsTx directories on attached drives, and will replay any NTFS logs.'
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/"
  - quote: "that the YellowKey exploit worked with the FsTx files on a USB drive but could not reproduce the bug using the EFI partition"
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/"
  - quote: "No, if you are using TPM+PIN the vulnerability is not exploitable."
    publisher: "MSRC CVE-2026-45585"
    source_url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585"
  - quote: "Added links to June 2026 Windows security updates."
    publisher: "MSRC CVE-2026-45585"
    source_url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585"
  - quote: "An attacker who successfully exploited this vulnerability could gain SYSTEM privileges."
    publisher: "MSRC CVE-2026-45586"
    source_url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586"
  - quote: "On Tuesday, Microsoft fixed the GreenPlasma, MiniPlasma, and YellowKey security vulnerabilities as part of its June 2026 Patch Tuesday"
    publisher: "BleepingComputer (June 2026 fixes)"
    source_url: "https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-20T05:00:11Z"
    run_id: 2026-05-20-a0f7b07f
    type: update
    summary: >
      UPDATE (originally covered 2026-05-15): Microsoft formally assigned CVE-2026-45585 to the
      BitLocker / WinRE bypass disclosed by "Nightmare Eclipse" on 2026-05-12 and confirmed there is
      still no security update.
    fields:
      - actions
      - cves
      - sources
      - body
    merged_from: 2026-05-20/cve-2026-45585-yellowkey-microsoft-formally-assigns-cve-and
  - at: "2026-10-21T15:38:35Z"
    run_id: 2026-10-21T1149Z-audit
    type: update
    summary: >
      Microsoft fixed YellowKey (CVE-2026-45585) and GreenPlasma, now CVE-2026-45586, in the June 2026
      Windows updates of 2026-06-09, after replacing its manual WinRE mitigation with a script on
      2026-05-21; neither is marked exploited, the do-now actions are withdrawn and the priority moves
      from high to notable. The analysis now gives Dormann's USB-only reproduction, the winpeshl.ini
      mechanism, the dispute between the researcher and Microsoft over TPM+PIN and Microsoft's product
      list, and drops an unsourced Microsoft quotation, a zero-day count and mitigation steps no source
      gives.
    fields: [actions, affected_products, body, classification, cves, entities, event_date, evidence, headline, priority, sectors, sources, summary, tags, techniques, title]
migrated_from: briefs/2026-05-15.md
---

On 2026-05-13 BleepingComputer and The Register reported that the researcher Nightmare Eclipse (also Chaotic Eclipse) had published exploit code for two Windows zero-days, YellowKey and GreenPlasma ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)) ([The Register, 2026-05-13](https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758)). The researcher's earlier BlueHammer (CVE-2026-33825) and RedSun drops began to be exploited in the wild shortly after release ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)).

**YellowKey** is a BitLocker bypass that needs physical access. The researcher says it affects Windows 11 and Windows Server 2022/2025 and works by placing crafted `FsTx` files on a USB drive or the EFI partition, rebooting into the Windows Recovery Environment (WinRE) and holding CTRL to trigger a shell ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)). Will Dormann reproduced it with the files on a USB drive but not on the EFI partition: to boot WinRE, Windows replays the NTFS logs in `\System Volume Information\FsTx` directories on attached drives, the replay deletes `X:\Windows\System32\winpeshl.ini`, and WinRE then opens `CMD.EXE` instead of the recovery environment, with the disk still unlocked ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)). Because it abuses TPM-only automatic unlock, the public exploit works only on the original device, not on a removed drive, and does not work with TPM+PIN ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)). Microsoft tracks it as CVE-2026-45585, a security feature bypass by physical attack (CWE-77, CVSS 6.8), publicly disclosed and not exploited; its fixed builds are Windows 11 24H2 build 10.0.26100.8655, 25H2 build 10.0.26200.8655, 26H1 build 10.0.28000.2269 and Windows Server 2025 build 10.0.26100.32995, and its product table does not list Windows Server 2022 ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)).

**Contradiction:** the researcher says an unpublished variant also defeats TPM+PIN ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)); Microsoft states that "if you are using TPM+PIN the vulnerability is not exploitable" ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)).

**GreenPlasma** is a local privilege escalation in CTFMON: an unprivileged user can create arbitrary memory-section objects within directory objects writable by SYSTEM, and the leaked PoC lacks the component needed for a full SYSTEM shell ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)); in its current state it triggers a UAC consent prompt in default Windows configurations ([The Register, 2026-05-13](https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758)). Microsoft tracks it as CVE-2026-45586, a link-following flaw (CWE-59, CVSS 7.8) in the Windows Collaborative Translation Framework that lets an authorized local attacker gain SYSTEM privileges, released on 2026-06-09 with fixes for Windows 10, Windows 11 and Windows Server 2012 to 2025, publicly disclosed and not exploited ([MSRC CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)).

**Exposure:** for YellowKey, TPM-only BitLocker devices ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)) on Windows 11 24H2, 25H2 or 26H1 or Windows Server 2025 below the fixed builds, given physical access ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)). For GreenPlasma, any Windows 10, Windows 11 or Windows Server 2012 to 2025 system without the June 2026 update, for an attacker who already runs code as a local user ([MSRC CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)).

**Detection:** no cited source describes an artifact YellowKey leaves inside Windows; the attacker's media carries `\System Volume Information\FsTx` directories that WinRE replays at boot ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)). GreenPlasma's public partial PoC raises a UAC consent prompt in default configurations ([The Register, 2026-05-13](https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758)).

**Defender takeaway:** the June 2026 Windows update fixes YellowKey ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)) and GreenPlasma ([MSRC CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)), and Microsoft's interim WinRE script need not be reverted, since the update keeps its behavior ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)). Microsoft says TPM+PIN makes YellowKey not exploitable ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)), which the researcher disputes ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)), and Kevin Beaumont advised TPM+PIN along with a BIOS password ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)).

## Update — 2026-05-20T05:00:11Z

Microsoft formally assigned **CVE-2026-45585** to the BitLocker / WinRE bypass disclosed by "Nightmare Eclipse" on 2026-05-12 and confirmed there is still no security update. The [MSRC update guide entry, published 2026-05-19](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585), classifies it as CWE-77 (command injection in BitLocker / Windows Recovery Environment), CVSS 6.8 (AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), with exploit-code maturity rated `E:P` (proof-of-concept) and remediation level `RL:W` (workaround only).

Microsoft's interim mitigation, which it recommends that customers "consider implementing" if they are concerned their devices and data are at risk of being compromised or stolen, is per-device work: mount the WinRE image, **remove the `autofstx.exe` entry from the `BootExecute` registry value inside the WinRE image**, commit the image, then re-establish BitLocker trust for WinRE ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)). The MSRC FAQ states: ["A successful attacker could bypass the BitLocker Device Encryption feature on the system storage device. An attacker with physical access to the target could exploit this vulnerability to gain access to encrypted data."](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)

A pre-boot PIN avoids depending on the WinRE edit: the public exploit relies on TPM-only automatic unlock and does not work with TPM+PIN ([BleepingComputer, 2026-05-13](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)), and NCSC-CH advises that BIOS passwords and a BitLocker PIN mitigate the current public PoC ([NCSC-CH Security Hub #12574, 2026-05-14](https://security-hub.ncsc.admin.ch/#/posts/12574)).

## Update — 2026-10-21T15:38:35Z

Microsoft fixed both flaws in the June 2026 Windows updates of 2026-06-09. Revision 2 of the CVE-2026-45585 record "Added links to June 2026 Windows security updates", with fixed builds Windows 11 24H2 build 10.0.26100.8655, 25H2 build 10.0.26200.8655, 26H1 build 10.0.28000.2269 and Windows Server 2025 build 10.0.26100.32995 ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)). GreenPlasma received its own identifier, CVE-2026-45586, released the same day with fixes for Windows 10, Windows 11 and Windows Server 2012 to 2025 ([MSRC CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)), and BleepingComputer reported that the June 2026 Patch Tuesday fixed GreenPlasma, MiniPlasma and YellowKey ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/)). Before the fix, on 2026-05-21, Microsoft had replaced its manual WinRE steps with a script that removes `autofstx.exe` from the WinRE `BootExecute` value and re-seals WinRE so BitLocker trust remains intact ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)). Microsoft marks neither flaw as exploited ([MSRC CVE-2026-45585](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585)) ([MSRC CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586)).
