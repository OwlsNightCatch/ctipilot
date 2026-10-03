---
schema: 1
kind: threat
title: "ValleyRAT (Winos 4.0) hides inside a re-signed Chinese wallpaper app: DLL sideloading, a self-restoring svchost injection, and a Windows Defender kill switch"
headline: "Kaspersky documents ValleyRAT distributed through a trojanized adware installer that disables Defender before loading the backdoor via DLL sideloading"
summary: >
  Kaspersky's Securelist documents a ValleyRAT (Winos 4.0) distribution chain hidden inside a
  re-signed copy of QN Wallpaper, a genuine Chinese desktop-wallpaper adware tool. The installer
  disables Windows Defender via the registry before a signed process sideloads a malicious DLL
  that decrypts and launches the backdoor, which can optionally mark itself a critical process and
  inject a self-restoring watchdog into svchost. Kaspersky attributes the campaign to Silver Fox and
  separately recorded over 100,000 detections of ValleyRAT across all of 2026, concentrated in China
  and India.
discovered_at: "2026-09-01T04:11:32Z"
updated_at: null
event_date: "2026-08-31"
run_id: 2026-09-01T0411Z-intel
priority: notable
immediate_action: null
tags: [espionage, organized-crime, infostealer]
regions: [apac]
sectors: []
entities: ["actor:silver-fox", "malware:valleyrat"]
techniques: [T1574.001, T1055, T1055.012, T1027, T1056.001, T1115, T1547.001, T1685, T1518.001]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/valleyrat-backdoor-adware/121175/"
    publisher: "Kaspersky Securelist"
    date: "2026-08-31"
    role: primary
  - url: "https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html"
    publisher: "The Hacker News"
    date: "2026-08-31"
    role: corroborating
  - url: "https://news.risky.biz/risky-bulletin-china-arrests-members-of-silver-fox-cybercrime-group/"
    publisher: "Risky Bulletin"
    date: "2026-06-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Over the course of 2026, we detected the ValleyRAT backdoor and its associated malware more than 100,000 times, with more than 1500 unique users affected, primarily in China and India."
    publisher: "Kaspersky Securelist"
  - quote: "After unpacking, the installer uses the DisableAntiSpyware registry key to disable Windows Defender and then launches QnWallpaper.exe."
    publisher: "Kaspersky Securelist"
  - quote: "This attack geography, combined with the use of the ValleyRAT backdoor, points to Silver Fox, a known operator of this malware family, as the likely group behind the campaign."
    publisher: "Kaspersky Securelist"
  - quote: "When the logged-in user lacks administrator rights, the malware relaunches itself with `runas` to acquire them."
    publisher: "The Hacker News"
  - quote: "Restarting on an unhandled exception. This protection mechanism is always active, regardless of the backdoor’s configuration."
    publisher: "Kaspersky Securelist"
  - quote: "Arrests took place across five provinces and targeted everyone from developers to phishing site operators and various affiliates."
    publisher: "Risky Bulletin"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Kaspersky's Securelist published an analysis on 2026-08-31 of a ValleyRAT (Winos 4.0) distribution chain hidden inside a re-signed copy of QN Wallpaper, a genuine Chinese desktop-wallpaper and adware-bundling tool. The installer drops a modified QN Wallpaper build and adds it to autorun; before launching the adware, it flips the `DisableAntiSpyware` registry key to disable Windows Defender, relaunching itself via `runas` first if the logged-in user lacks administrator rights ([Kaspersky Securelist, 2026-08-31](https://securelist.com/valleyrat-backdoor-adware/121175/); [The Hacker News, 2026-08-31](https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html)). QnWallpaper.exe then loads a malicious `libcef.dll` placed alongside it — DLL sideloading through a signed, trusted process — which decrypts an AES-encrypted ValleyRAT payload and hands it control via `DllMain`; the backdoor's own command-and-control configuration is stored as a reversed key:value string to defeat static string scanning ([Kaspersky Securelist, 2026-08-31](https://securelist.com/valleyrat-backdoor-adware/121175/)).

Runtime protections are read from the malware's own configuration and each can be switched on or off independently: marking the process critical (so killing it forces a system crash), injecting a watchdog into `svchost` that toggles its memory region from no-access to fully executable to relaunch the implant if interrupted, and enumerating open windows to detect security or traffic-analysis tooling before proceeding; a fourth resilience mechanism — restarting the backdoor on an unhandled exception — is always active regardless of that configuration ([Kaspersky Securelist, 2026-08-31](https://securelist.com/valleyrat-backdoor-adware/121175/)). Spyware functions run through DirectInput8 hooks for keystroke capture and a separate clipboard-capture routine, both writing collected data to disk; on operator command the backdoor can pull and execute additional modules, using process hollowing into `svchost` when a module arrives as raw shellcode. Kaspersky's account of this specific campaign is based on one installer submitted by a customer, and its report stops short of attaching a victim count to this adware-distribution route; separately, and across all of 2026 rather than this campaign alone, Kaspersky recorded over 100,000 detections of ValleyRAT and associated malware affecting more than 1,500 unique users, concentrated in China and India ([The Hacker News, 2026-08-31](https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html)). Kaspersky attributes the campaign to Silver Fox, an established ValleyRAT operator, on geography and payload grounds ([Kaspersky Securelist, 2026-08-31](https://securelist.com/valleyrat-backdoor-adware/121175/)). DLL sideloading through signed, legitimate software is an established part of Silver Fox's toolkit, previously documented by Cato Networks against a Japanese manufacturer roughly five weeks earlier ([The Hacker News, 2026-08-31](https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html)). That campaign postdates a June 2026 Chinese police crackdown that arrested 67 people linked to Silver Fox across five provinces — evidence the group's operations continued despite the arrests; this QN Wallpaper campaign's own timing is not independently established beyond Kaspersky's 2026-08-31 publication date, so it cannot be dated relative to the arrests with the same confidence ([Risky Bulletin, 2026-06-17](https://news.risky.biz/risky-bulletin-china-arrests-members-of-silver-fox-cybercrime-group/)).

**Defender takeaway:** the reliable discriminator is not the DLL name but the behavioral pairing, where the malware's optional runtime protections are enabled. Process-creation telemetry showing a signed but uncommon binary (here, `QnWallpaper.exe`) loading a `libcef.dll` from a non-browser install path, combined — where the watchdog option is active — with a memory region inside `svchost.exe` that toggles from no-access to fully executable roughly a minute after code injection, is a strong signal with very low false-positive risk when it occurs — legitimate Chromium Embedded Framework consumers do not exhibit that memory-protection flip. A process that disables Windows Defender via the `DisableAntiSpyware` key is itself a strong indicator regardless of which optional protections happen to be enabled in that sample. Application allow-listing that blocks unmanaged desktop-customization and wallpaper utilities removes the delivery vector entirely, since the technique depends on the user being permitted to install arbitrary signed third-party software.

**Triage:** genuine Chromium Embedded Framework processes (many legitimate desktop apps embed CEF) load `libcef.dll` from their own install directory and never inject code into `svchost` that toggles between no-access and executable memory states; that combination — a wallpaper or adware-class binary invoking CEF at all, paired with the `svchost` memory-protection change — is what separates this chain from ordinary CEF usage when that optional watchdog is present in the sample.
