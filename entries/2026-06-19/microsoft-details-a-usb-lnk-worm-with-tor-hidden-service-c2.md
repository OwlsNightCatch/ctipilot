---
schema: 1
kind: threat
horizon: operational
title: Microsoft details a USB-LNK worm with Tor hidden-service C2 driving a cryptocurrency clipboard hijacker
headline: Microsoft details a USB-LNK worm with Tor hidden-service C2 driving a cryptocurrency clipboard hijacker
summary: "Microsoft Threat Intelligence documented a multi-component campaign (detected as Trojan:Win32/CryptoBandits.A/B and Trojan:JS/CryptoBandits.A/B), active since at least February 2026, that pairs a removable-media worm with a Tor-fronted clipboard hijacker (Microsoft Security, 2026-06-17; The Hacker News …"
discovered_at: "2026-06-19T05:20:53Z"
event_date: 2026-06-18
run_id: 2026-06-19-c306b105
priority: notable
immediate_action: null
tags:
  - infostealer
  - cryptocrime
  - botnet
regions:
  - global
sectors:
  - finance
  - public-sector
entities:
  - "campaign:cryptobandits-usb-lnk-tor-clipper"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/"
    publisher: Microsoft Security
    role: primary
  - url: "https://thehackernews.com/2026/06/microsoft-details-windows-clipper.html"
    publisher: The Hacker News
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
actions: []
migrated_from: briefs/2026-06-19.md
---

Microsoft Threat Intelligence documented a multi-component campaign (detected as `Trojan:Win32/CryptoBandits.A`/B and `Trojan:JS/CryptoBandits.A`/B), active since at least February 2026, that pairs a removable-media worm with a Tor-fronted clipboard hijacker ([Microsoft Security, 2026-06-17](https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/); [The Hacker News, 2026-06-18](https://thehackernews.com/2026/06/microsoft-details-windows-clipper.html)). The worm scans attached USB drives for `.doc`/`.xlsx`/`.pdf` files, sets the originals hidden, and replaces them with same-named `.lnk` shortcuts that launch the payload on user interaction — the classic air-gap-crossing removable-media vector. Once resident, it establishes scheduled-task persistence, launches a renamed portable Tor client opening a SOCKS5 proxy on `localhost:9050`, and beacons to `.onion` hidden services over three HTTP endpoints (`/route.php` beacon, `/recvf.php` upload, `/stub.php` payload). The clipboard component polls for cryptocurrency addresses (Bitcoin, Ethereum, Tron, Monero) and silently swaps them, and the C2 supports an `EVAL` remote-code-execution command.
**Why it matters to us:** the crypto-theft payload is secondary to the propagation model — USB-LNK worms have historically reached isolated and air-gapped administrative environments still common in Swiss public-sector data-transfer workflows, and Tor-fronted C2 defeats domain/IP egress blocking. Detection: `WScript`/`CScript` spawning `curl.exe`/`cmd.exe`/`powershell.exe`; outbound SOCKS5 to `localhost:9050`; scheduled-task creation referencing obfuscated script payloads. Hardening: enforce `NoAutorun`/`NoDriveTypeAutorun`, block LNK execution from removable media via ASR, restrict `wscript.exe`/`cscript.exe` to signed scripts, and block Tor egress.
