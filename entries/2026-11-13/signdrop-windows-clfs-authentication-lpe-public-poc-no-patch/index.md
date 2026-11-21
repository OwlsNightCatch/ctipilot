---
schema: 1
kind: vulnerability
title: 'SignDrop: a public Windows local privilege escalation to SYSTEM that turns Microsoft''s CLFS authentication mitigation against itself through Defender''s signature-update RPC; proof of concept published 2026-11-10, no CVE and no patch, no exploitation reported'
headline: 'SignDrop: public Windows LPE to SYSTEM through CLFS and Defender; no CVE or patch; check CLFS authentication Mode'
summary: Cyderes Howler Cell reproduced SignDrop, a Windows local privilege escalation from a standard user to SYSTEM that was published on GitHub on 2026-11-10, the day of Patch Tuesday, with no coordinated disclosure, no CVE and no patch. It makes Defender's signature-update RPC and symbolic links get clfs.sys to write a SYSTEM-owned authentication file where the attacker chooses, so it applies where the CLFS authentication Mode is 0 or 1; no exploitation is reported, Microsoft has not commented, and the researcher's claim that about 80% of Windows installations are exposed is unsubstantiated.
discovered_at: '2026-11-13T04:03:00Z'
updated_at: null
event_date: '2026-11-10'
run_id: 2026-11-13T0256Z-intel
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - lpe
  - priv-esc
  - zero-day
  - poc-public
  - no-patch
regions:
  - global
sectors: []
entities:
  - actor:nightmare-eclipse
  - product:microsoft-windows
  - product:microsoft-defender-antivirus
techniques:
  - T1068
  - T1574.001
  - T1070.004
  - T1106
affected_products:
  - Microsoft Windows 11
  - Microsoft Windows Server 2025
  - Microsoft Defender Antivirus
cves: []
sources:
  - url: https://www.cyderes.com/howler-cell/signdrop-zero-day
    publisher: Cyderes Howler Cell
    date: '2026-11-12'
    role: primary
  - url: https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/
    publisher: BleepingComputer
    date: '2026-11-12'
    role: corroborating
  - url: https://securityonline.info/signdrop-windows-clfs-zero-day-poc/
    publisher: SecurityOnline
    date: '2026-11-11'
    role: corroborating
closed_sources: []
evidence:
  - quote: The exploit was published on November 10, 2026, under the MSNightmare handle on GitHub. No coordinated disclosure, no CVE, no patch.
    publisher: Cyderes Howler Cell
    source_url: https://www.cyderes.com/howler-cell/signdrop-zero-day
  - quote: Alert on any creation of hid.dll in the ink directory. The file does not ship there with Windows, so any appearance indicates a successful write regardless of variant.
    publisher: Cyderes Howler Cell
    source_url: https://www.cyderes.com/howler-cell/signdrop-zero-day
  - quote: The researcher estimates 80% of Windows installations are vulnerable, though no data supports that figure.
    publisher: Cyderes Howler Cell
    source_url: https://www.cyderes.com/howler-cell/signdrop-zero-day
verification: single-source
sourcing_note: 'Cyderes is the only source with its own technical reproduction; BleepingComputer and SecurityOnline restate the exploit author''s README, which is the author''s own claim, and no Microsoft advisory exists. Cyderes and BleepingComputer differ on the labels of the Mode values (Cyderes and Microsoft''s documentation: 0 enforced, 1 learning); the numeric scope, 0 or 1, is the same in every source.'
confidence: medium
references:
  - 2026-10-08/bigdiskbuster-defender-update-starvation-disk-exhaustion-poc
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

Cyderes Howler Cell reports that the exploit was published on 2026-11-10 under a GitHub handle, the same day as November Patch Tuesday, with no coordinated disclosure, no CVE and no patch, and that its team reproduced a SYSTEM shell from a standard user session ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)). The chain is a logic bug with no memory corruption: CLFS containers are created through Object Manager symbolic links, an oplock on a bait file confirms that Microsoft Defender has engaged, a call to Defender's signature-update RPC makes clfs.sys create its .cnpf authentication-signature file as SYSTEM at an attacker-chosen path, here hid.dll in the Common Files\microsoft shared\ink directory, a file that does not ship in that directory; the content is replaced with a payload DLL and a runas request makes consent.exe load it, which starts a SYSTEM conhost.exe on the user's desktop ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)). Like every release of the same cluster it needs a foothold on the host first. It applies where the CLFS authentication Mode value, under HKLM\SYSTEM\CurrentControlSet\Services\CLFS\Authentication, is 0 or 1 ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)).

Cyderes says the feature ships enabled on current Windows versions and that the researcher tested Windows 11 26H2 and experimental builds of Windows 11 and Windows Server 2025; the researcher's estimate that 80% of Windows installations are vulnerable has no data behind it ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)). The researcher adds that, because the privileged file creation appears to come from the antimalware engine's own process, the technique can be used against any antimalware engine's self-defense; that claim rests on his statement alone ([BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/)). No source reports exploitation, and Microsoft had not commented publicly as of 2026-11-11 ([SecurityOnline, 2026-11-11](https://securityonline.info/signdrop-windows-clfs-zero-day-poc/)).

**Exposure:** any Windows host on which an attacker can already run code as a standard user and whose CLFS authentication Mode is 0 or 1; Cyderes tells defenders to read the Mode value on every host to size the population ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)).

**Detection:** file-creation telemetry for hid.dll in the ink directory, which Cyderes counts, with the Defender signature-update RPC call, among its two highest-signal observables because the file does not ship in that directory; that RPC called from a process outside the Defender service tree; symbolic-link churn under \BaseNamedObjects\Restricted\ correlated with Defender RPC activity; consent.exe loading a DLL from the ink directory; and a SYSTEM conhost.exe on the interactive desktop right after a hid.dll write. The exploit deletes hid.dll afterwards, so keep file-creation and image-load telemetry rather than relying on a disk sweep ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)).

**Triage:** Cyderes calls a hid.dll creation in the ink directory and a Defender signature-update RPC from outside the Defender service tree rare enough in a typical estate to alert on rather than hunt, and the first is a successful write whatever the variant ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)).

**Defender takeaway:** no patch exists, so inventory the Mode value, restrict untrusted local code execution with application and script control, and do not switch CLFS authentication off as a workaround, because that re-exposes the older memory-corruption attacks it blocks; Cyderes counts sixteen public releases from the same researcher in roughly thirty-one weeks, so expect more ([Cyderes, 2026-11-12](https://www.cyderes.com/howler-cell/signdrop-zero-day)).
