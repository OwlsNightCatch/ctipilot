---
schema: 1
kind: threat
title: "MovieReaper: a modular crimeware framework distributed via a torrent-file-repository supply-chain compromise, using the Solana blockchain as a C2 dead-drop resolver"
headline: "Kaspersky: a single compromised torrent-file repository silently poisoned magnet-link resolutions across many unrelated tracker sites"
summary: >
  Kaspersky documents MovieReaper, a previously undocumented Windows crimeware framework active
  since October 2025 and distributed through a supply-chain compromise of itorrents.org, a
  shared public torrent-file repository. The malware resolves its second-stage C2 address via a
  Solana blockchain dead-drop, and Kaspersky counts several hundred victims across Europe, Asia,
  Africa and Latin America, with government among the targeted sectors.
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
  - quote: "we discovered a previously unknown modular, multi-stage framework that we dubbed MovieReaper"
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/"
  - quote: "instead of compromising torrent trackers, the threat actor modified a widely used public repository of torrent files"
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/"
  - quote: "Utilizing the Solana blockchain as a storage layer for next-stage C2 endpoints substantially complicates infrastructure takedown efforts by defenders."
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/"
verification: single-source
sourcing_note: >
  Kaspersky's own primary research, with no independent corroboration found. Kaspersky revised the
  article after first publication, rewording several passages and extending the list in its
  Victims section to Latin America and to Uganda, Colombia, the Netherlands and Belgium, countries
  its introduction already named.
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
updates:
  - at: "2026-09-29T21:37:10Z"
    run_id: 2026-09-29T2134Z-audit
    type: correction
    summary: >
      Kaspersky revised its MovieReaper report after first publication. The three quoted passages now
      read differently, the list in its Victims section now also covers Latin America and names
      Uganda, Colombia, the Netherlands and Belgium, which the introduction already named, and the
      distribution is described as the actor modifying a public torrent-file repository instead of
      compromising the trackers. The analysis, the cited evidence and the summary now follow the
      current text. The third stage's masquerade is described as the report gives it, an Edge-named
      binary in a Telemetry folder.
    fields: [summary, sourcing_note, evidence, body]
migrated_from: null
---

Kaspersky documents MovieReaper, a previously undocumented modular Windows crimeware framework active since at least October 2025, distributed through a supply-chain compromise of itorrents.org, a shared public repository many independent torrent trackers rely on to resolve magnet links. The actor modified that repository instead of compromising the trackers, which lets it reach users of many trackers without compromising each platform individually ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). Kaspersky reports several hundred victims, individuals and organizations, with infection attempts in Russia, Spain, Germany, Finland, Türkiye, Japan, Nepal, Kenya, Tanzania, Ghana, Uganda, Colombia, the Netherlands, Belgium and other countries across Europe, Asia, Africa and Latin America, and targeted organizations spanning enterprise, government, IT, consulting, retail, transportation and agriculture ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). After a user manually runs a first-stage loader disguised under a film-referencing filename, the loader resolves Windows API addresses by manually walking the PEB's loaded-module list rather than calling LoadLibrary or GetProcAddress, then registers a vectored exception handler that triggers a deliberate debug break to redirect control flow into a manually located raw syscall instruction inside ntdll and call NtProtectVirtualMemory directly, before invoking the undocumented ntdll export EtwpCreateEtwThread, which Kaspersky describes as a popular alternative to CreateThread, to execute the mapped shellcode ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). The second stage queries the legitimate Solana blockchain's public getAccountInfo RPC endpoint to retrieve an XOR-encrypted C2 address, which Kaspersky notes gives the operators decentralized storage for C2 addresses that blocking C2 server IP addresses alone does not disrupt ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). A third stage performs a UAC bypass and persistence and copies the original binary to msedge.exe in the Microsoft\Windows\Telemetry folder under ProgramData, so an Edge-named executable runs from outside Edge's install directory, then hands off to a final remote-file-manager module exposing 21 filesystem commands, including preview commands Kaspersky reads as built for pre-exfiltration triage of image and document contents ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)).

**Defender takeaway:** a process calling NtProtectVirtualMemory to mark a region executable shortly before invoking ntdll's EtwpCreateEtwThread export is anomalous for nearly any legitimate application and is a strong process-behavior discriminator for this loader class; outbound HTTPS to Solana public RPC endpoints from a non-wallet, non-Web3 process is a second, independent behavioral signal, since legitimate blockchain-RPC traffic from an enterprise endpoint is otherwise rare.

## Correction — 2026-09-29T21:37:10Z

Kaspersky has revised its report since first publication. It now describes the distribution as the actor modifying the public torrent-file repository instead of compromising the torrent trackers, and the list in its Victims section now adds Latin America to the affected regions and names Uganda, Colombia, the Netherlands and Belgium, countries the introduction named from the start ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)). The earlier text of this entry described the victims as spanning Europe, Asia and Africa only and contrasted the repository compromise with trojanized installers on individual sites. 

The analysis had also described the third stage as masquerading as a Windows Telemetry executable. The report says it copies the original binary to msedge.exe in a Windows Telemetry folder under ProgramData, an Edge name in a Telemetry location, and the analysis now says so ([Kaspersky Securelist, 2026-09-17](https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/)).
