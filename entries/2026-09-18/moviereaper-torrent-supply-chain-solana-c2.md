---
schema: 1
kind: threat
title: "MovieReaper: a modular crimeware framework distributed via a torrent-file-repository supply-chain compromise, using the Solana blockchain as a C2 dead-drop resolver"
headline: "Kaspersky: a single compromised torrent-file repository silently poisoned magnet-link resolutions across many unrelated tracker sites"
summary: >
  Kaspersky documents MovieReaper, a previously undocumented Windows crimeware framework active
  since October 2025 and distributed through a supply-chain compromise of itorrents.org, a
  shared public torrent-file repository; the malware resolves its second-stage C2 address via a
  Solana blockchain dead-drop and has confirmed victims including government entities across
  Europe, Asia and Africa.
discovered_at: "2026-09-18T04:58:00Z"
updated_at: null
event_date: "2026-09-17"
run_id: 2026-09-18T0410Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, botnet]
regions: [global]
sectors: [public-sector]
entities: ["malware:moviereaper"]
techniques: [T1195.002, T1204.002, T1620, T1106, T1140, T1102.001, T1548.002, T1036.005]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/"
    publisher: "Kaspersky (Securelist)"
    date: "2026-09-17"
    role: primary
closed_sources: []
evidence:
  - quote: "we have discovered a previously unknown modular, multi-stage framework that we dubbed MovieReaper"
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/"
  - quote: "the threat actors did not compromise the torrent trackers themselves. Instead, they compromised a widely used public repository of torrent files"
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/"
  - quote: "By using Solana blockchain network as a distribution layer of endpoints for a next stage attackers may increase stability of their campaign and resist takedown efforts of defenders."
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/"
verification: single-source
sourcing_note: >
  Kaspersky's own primary research; no independent corroboration found in-window. Kaspersky's
  article carries two only-partially-overlapping victim-country lists in different sections; the
  body below cites the more specific, dedicated "Victims" section list rather than the
  introduction's shorter enumeration.
confidence: high
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

Kaspersky documents MovieReaper, a previously undocumented modular Windows crimeware framework active since at least October 2025, distributed through a supply-chain compromise of itorrents.org — a shared public repository many independent torrent trackers rely on to resolve magnet links — rather than trojanized installers on individual sites, so a single compromise reaches users across many unrelated tracker sites simultaneously ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). Several hundred victims are confirmed across enterprise, government, IT, consulting, retail, transportation and agriculture sectors, spanning Russia, Spain, Germany, Finland, Türkiye, Japan, Nepal, Kenya, Tanzania, Ghana and others across Europe, Asia and Africa ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). After a user manually runs a first-stage loader disguised under a film-referencing filename, the loader resolves Windows API addresses by manually walking the PEB's loaded-module list rather than calling LoadLibrary or GetProcAddress, then registers a vectored exception handler that triggers a deliberate debug break to redirect control flow into a manually located raw syscall instruction inside ntdll and call NtProtectVirtualMemory directly, before invoking the undocumented ntdll export EtwpCreateEtwThread, which Kaspersky describes as a popular alternative to CreateThread, to execute the mapped shellcode ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). The second stage queries the legitimate Solana blockchain's public getAccountInfo RPC endpoint to retrieve an XOR-encrypted C2 address, a dead-drop pattern that lets operators rotate infrastructure without touching the malware itself. A third stage performs a UAC bypass and persistence, masquerades as a Windows Telemetry executable, and hands off to a final remote-file-manager module exposing 21 filesystem commands, including preview commands Kaspersky reads as built for pre-exfiltration triage of image and document contents.

**Defender takeaway:** a process calling NtProtectVirtualMemory to mark a region executable shortly before invoking ntdll's EtwpCreateEtwThread export is anomalous for nearly any legitimate application and is a strong process-behavior discriminator for this loader class; outbound HTTPS to Solana public RPC endpoints from a non-wallet, non-Web3 process is a second, independent behavioral signal, since legitimate blockchain-RPC traffic from an enterprise endpoint is otherwise rare.
