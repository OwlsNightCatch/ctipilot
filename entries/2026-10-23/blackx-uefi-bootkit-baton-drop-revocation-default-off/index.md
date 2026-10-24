---
schema: 1
kind: threat
title: "BlackX: Kaspersky finds a BlackLotus-style UEFI bootkit on fully patched Windows machines of Central Asian diplomatic bodies, because the Baton Drop fix does not revoke the old boot-manager certificate until an administrator triggers it"
headline: "Kaspersky: a UEFI bootkit ran on fully patched Windows because Microsoft's Secure Boot revocation is off by default"
summary: >
  Kaspersky GReAT reports BlackX, a UEFI bootkit similar to BlackLotus that exploits Baton Drop (CVE-2022-21894) to enrol attacker keys
  and load a kernel driver that blinds security products, installed after attackers held administrator rights on networks of
  diplomatic agencies in Tajikistan, Uzbekistan and Turkmenistan; Kaspersky attributes it to APT41 with medium confidence. The
  targeted machines were fully patched, because Microsoft's fix revokes the old boot-manager certificate only when an administrator
  sets a registry flag and runs a scheduled task.
discovered_at: "2026-10-23T03:39:30Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-23T0256Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, china-nexus, actively-exploited]
regions: [global]
sectors: [public-sector]
entities: ["malware:blackx-uefi-bootkit", "actor:apt41"]
techniques: [T1542.003, T1553.006, T1687, T1014, T1685, T1574.001, T1102.002, T1027]
affected_products: ["Microsoft Windows"]
cves:
  - id: CVE-2022-21894
    cvss: null
    epss: null
    type: logic-flaw
    vector: local
    auth: admin-required
    status: [exploited, patch-available]
    affected: "Windows devices that boot with Secure Boot and have not had the Windows Production PCA 2011 revocation applied; Microsoft's mitigations are in the updates of 2024-07-09 and later and are not enabled by default"
    fixed: "mitigation only when the revocation steps in Microsoft's KB5025885 are applied"
  - id: CVE-2023-24932
    cvss: null
    epss: null
    type: logic-flaw
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "Windows devices that boot with Secure Boot and have not had the Windows Production PCA 2011 revocation applied; Microsoft's mitigations are in the updates of 2024-07-09 and later and are not enabled by default"
    fixed: "mitigation only when the revocation steps in Microsoft's KB5025885 are applied"
sources:
  - url: "https://securelist.com/uefi-bootkit-blackx/121539/"
    publisher: "Kaspersky GReAT (Securelist)"
    date: "2026-10-22"
    role: primary
  - url: "https://support.microsoft.com/en-us/servicing/os/windows/2023/03/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023"
    publisher: "Microsoft Support (KB5025885)"
    date: "2026-09-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the targeted machines were fully patched"
    publisher: "Kaspersky GReAT (Securelist)"
    source_url: "https://securelist.com/uefi-bootkit-blackx/121539/"
  - quote: "However, this revocation does not happen automatically upon patch installation"
    publisher: "Kaspersky GReAT (Securelist)"
    source_url: "https://securelist.com/uefi-bootkit-blackx/121539/"
  - quote: "we have attributed this attack to the APT41 threat actor with medium confidence"
    publisher: "Kaspersky GReAT (Securelist)"
    source_url: "https://securelist.com/uefi-bootkit-blackx/121539/"
  - quote: "However, these mitigations are not enabled by default."
    publisher: "Microsoft Support (KB5025885)"
    source_url: "https://support.microsoft.com/en-us/servicing/os/windows/2023/03/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023"
verification: single-source
sourcing_note: >
  The campaign, its technical analysis and the attribution are Kaspersky's alone; Microsoft's own support article independently
  confirms that the revocation mitigations are not enabled by default and gives the procedure. Kaspersky names no victim organization
  and its attribution to APT41 is stated with medium confidence.
confidence: medium
references: ["2026-06-17/fishmonger-i-soon-ports-its-sprysocks-backdoor-to-windows-wi", "2026-07-14/eset-forgotten-uefi-shims-secure-boot-bypass"]
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
Kaspersky GReAT reports that in early 2026 it found BlackX, a UEFI bootkit similar to BlackLotus, used against diplomatic agencies in Tajikistan, Uzbekistan and Turkmenistan after the attackers held administrator privileges: an installer takes an RC4-encrypted package and its key as command-line arguments and drops files to the system and UEFI partitions that exploit Baton Drop (CVE-2022-21894) to enrol attacker-controlled Machine Owner Keys, so arbitrary EFI files load despite Secure Boot ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)). Kaspersky ties the exploitation to Baton Drop alone; CVE-2023-24932, the flaw Microsoft's revocation guidance is titled for, appears in its post only as the one a UEFI component in ESET's FishMonger report might exploit ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)). The bootkit injects a kernel driver, signed with a certificate its issuer has since revoked, that disables process, thread and registry callbacks and ETW providers of security products; the user-mode payloads were a RAT that uses Google Drive, OneDrive or Yandex.Disk for command and control and a sideloaded loader ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)).

The targeted machines were fully patched. Microsoft's fix revokes the Windows Production PCA 2011 certificate only when an administrator sets a Secure Boot registry flag and runs the Secure-Boot-Update scheduled task ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)); Microsoft's own article says the mitigations in the updates of 2024-07-09 and later are not enabled by default and the Enforcement Phase date is still to be announced ([Microsoft Support, 2026-09-30](https://support.microsoft.com/en-us/servicing/os/windows/2023/03/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023)), and Kaspersky says that phase has not been implemented and the certificate's expiry on 2026-10-19 does not stop the vulnerable binaries loading unless it is on the forbidden list ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)). Kaspersky attributes the campaign to APT41 with medium confidence, resting on the identifier "xdd" shared with a kernel implant in ESET's June 2026 FishMonger report, DLL sideloading and OLLVM ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)).

**Exposure:** any Windows device that boots with Secure Boot, has the updates of 2024-07-09 or later and has not had the revocation steps applied; Microsoft's check is that the forbidden-list (DBX) variable contains Microsoft Windows Production PCA 2011, which a PowerShell test returns as True once the revocation is in ([Microsoft Support, 2026-09-30](https://support.microsoft.com/en-us/servicing/os/windows/2023/03/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023)).

**Detection:** the installer needs administrator rights, so the hunt starts with the administrator-level intrusion that precedes it; the behaviors Kaspersky describes are process creation of an executable from a program-data subfolder that takes an encrypted data file and a key as arguments, file writes to the EFI system partition by processes that are not servicing, kernel driver loads signed by an unfamiliar or revoked certificate, a signed executable renamed to look like an updater that loads a sideloaded DLL, and non-browser processes talking to consumer cloud storage ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)). Because the driver disables security-product callbacks and ETW providers, quiet host telemetry after a reboot on a machine that ran the installer is not evidence that nothing ran, although Kaspersky found that the driver's tampering routines, written for Kaspersky and Avast products, failed to interfere with Kaspersky products ([Kaspersky GReAT, 2026-10-22](https://securelist.com/uefi-bootkit-blackx/121539/)).

**Defender takeaway:** a patched Windows fleet is not protected against this class until the revocation is applied, so decide which devices get Microsoft's procedure and in what order; Microsoft warns that the revocation cannot be reverted while Secure Boot is in use, that BitLocker recovery keys should be backed up first, and that recovery and install media must be updated ([Microsoft Support, 2026-09-30](https://support.microsoft.com/en-us/servicing/os/windows/2023/03/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023)).
