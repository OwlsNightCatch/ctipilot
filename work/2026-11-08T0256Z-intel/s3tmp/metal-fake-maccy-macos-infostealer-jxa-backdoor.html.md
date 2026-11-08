---
title: "Fake Maccy: macOS infostealer disguised as a clipboard manager"
author: Researchers Vijay Prakash; Vipin Kiruba; June
url: https://www.manageengine.com/threat-analysis-lab/fake-maccy-macos-infostealer-jxa-backdoor.html
hostname: manageengine.com
description: Fake Maccy is a macOS infostealer posing as Maccy to steal passwords and browser credentials and send them to attackers.
sitename: ManageEngine
date: "2026-06-26"
fingerprint: "995bb33beb1ef84"
---
## Executive summary

## Overview of the attack

## Attack dissection

### The look-alike lure

### The Script Editor JXA dropper

### CIS geo-fencing and a machine-bound C2 URL

### The Finder masquerade and Login Item persistence

```
~/Library/Application Support/com.apple.finder.monitor/     (mimics Apple's reverse-DNS naming convention)
└── Finder.app/
    ├── Contents/
    │   ├── Info.plist      (LSUIElement=true · LSBackgroundOnly=true)
    │   ├── MacOS/
    │   │   └── F8C06C86    (944,464-byte Rust ARM64 infostealer;
    │   │                    8-hex-char name believed to rotate per host)
    │   └── Resources/
    │       └── AppIcon.icns (copied from the genuine Finder in /System/Library/CoreServices/)
    ├── .config             (34 bytes — plaintext C2 URL)
    ├── .lock               (0 bytes — single-instance mutex)
    └── .Maccy              (0 bytes — clipboard-monitoring marker)
```
							
							
							
							
### Credential theft and exfiltration

## The chain, step by step

```
User searches "Maccy" → clicks SEO-positioned look-alike maccyapp[.]com (not the real maccy.app)
   |
   v
maccy.dmg mounted → compiled JXA .scpt opens in Script Editor
   (first-party Apple app; user clicks Run—no Terminal, no paste)
   |
   v
Four CIS geo-fence checks
   (timezone · locale · keyboard · arch; aborts on Russia/CIS)
   |
   v
RC4-decrypt C2 URL from 32-byte machine fingerprint
   (unique per host; not statically extractable)
   |
   v
Rust ARM64 binary downloaded → fake Finder.app built under
   ~/Library/Application Support/com.apple.finder.monitor/
   ad-hoc self-signed; LSUIElement/LSBackgroundOnly hide it
   |
   v
Login Item persistence via LSSharedFileList + SMAppService
   (shows as "Finder"; avoids LaunchAgents/LaunchDaemons)
   |
   +------------------------------+
   v                              v
Second "Finder" process        Credential + clipboard theft
in Activity Monitor            Keychain · browser SQLite ·
(real Finder only ever         NSPasteboard · PAM interception
 runs from CoreServices)          |
                                  v
                               ChaCha20-Poly1305 blob →
                               HTTPS POST to avengerflow[.]com/api/sync
                               (bidirectional—treat host as live implant)
```
							
## How it looks in telemetry

```
parent_process == "Script Editor"
AND child_process performs (network_connect
                            OR file_write to "~/Library/Application Support/"
                            OR codesign
                            OR LSSharedFileListInsertItemURL)
```
							
## Indicators of compromise

### Durable — file system and structural

### Durable — process and identity

### Volatile — network

### Volatile — hashes

## Conclusion

[Explore latest threat research](https://www.manageengine.com/index.html#threat-research?pos=metal-fakemaccy)
