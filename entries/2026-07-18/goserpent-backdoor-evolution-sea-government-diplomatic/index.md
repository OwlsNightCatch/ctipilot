---
schema: 1
kind: threat
title: "GoSerpent evolves: staged collect-then-return espionage against Southeast Asian government and diplomatic targets"
headline: "Kaspersky details GoSerpent's re-tooled chain — ChaCha20 C2, a file-harvesting Windows service, and a weeks-long silent-collection stage before exfiltration"
summary: >
  Kaspersky GReAT published (2026-07-16) a full analysis of the evolved GoSerpent backdoor, a
  Go-based RAT used since 2021 against government and diplomatic entities in Southeast Asia. The
  current chain decrypts its C2 address from AES-CBC-encrypted command-line arguments, talks
  ChaCha20 to its C2, deploys a document-harvesting Windows service plus Mimikatz and
  QuarksDumpLocalHash, deliberately waits a few weeks while files accumulate, then returns with the
  Stowaway proxy and a dedicated exfiltration toolset. Kaspersky notes a potential — not confirmed —
  link to the TetrisPhantom actor. Published as an audit-recovered item: the primary fell below the
  visible fold of the Securelist listing sweep on the publication date.
discovered_at: "2026-07-18T13:05:00Z"
event_date: "2026-07-16"
run_id: 2026-07-18T1208Z-audit
priority: notable
immediate_action: null
tags: [espionage, nation-state]
regions: [apac]
sectors: [public-sector]
entities: [malware:goserpent, actor:tetrisphantom]
techniques: [T1059, T1027, T1573.001, T1543.003, T1036.005, T1005, T1560.001, T1003.001, T1003.002, T1090.001, T1090.002]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/goserpent-backdoor-in-southeast-asia/120687/"
    publisher: "Kaspersky Securelist"
    date: "2026-07-16"
    role: primary
closed_sources: []
evidence:
  - quote: "The backdoor connects to command-and-control servers using ChaCha20 encryption for communications, with the SHA256 hash of the communication password serving as the encryption key."
    publisher: "Kaspersky Securelist"
  - quote: "the attackers allowed a few weeks for the ThumbcacheService to silently collect sensitive files without exfiltrating them"
    publisher: "Kaspersky Securelist"
  - quote: "While the exact attribution of the GoSerpent campaign remains uncertain, there are indications of a potential link to the TetrisPhantom threat actor."
    publisher: "Kaspersky Securelist"
verification: single-source
sourcing_note: "Single-source: Kaspersky GReAT is the sole publisher at time of writing (research-lab primary with full first-hand technical analysis; no independent corroboration found). The TetrisPhantom connection is Kaspersky's own hedged assessment — 'indications of a potential link' from shared victimology, capabilities and methods — and is carried here strictly as that claim, not as attribution."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Kaspersky GReAT published a full analysis of the evolved GoSerpent backdoor — a Go-based RAT it has tracked against victims in Southeast Asia since 2021, whose current campaign "targeted government and diplomatic entities in Southeast Asia and showed a level of sophistication that caught our attention" ([Kaspersky Securelist, 2026-07-16](https://securelist.com/goserpent-backdoor-in-southeast-asia/120687/)). Where early versions took their configuration as plain-text command-line arguments, the re-tooled backdoor receives base64-encoded, AES-CBC-encrypted arguments carrying the C2 server address and a communication password whose SHA-256 hash becomes the ChaCha20 key for all subsequent C2 traffic. Its command set covers file upload/download, remote shell execution, port forwarding, and starting a SOCKS5 proxy on the infected machine so the operators can route further access through compromised hosts; a companion Go tool, McMx, replicates the proxy/remote-shell core in simpler form ([Kaspersky Securelist, 2026-07-16](https://securelist.com/goserpent-backdoor-in-southeast-asia/120687/)).

The campaign's defining shape is staged patience. After the initial deployment the operators typically wait several days, then install the collection layer: ThumbcacheService, a malicious DLL registered as a Windows service that hunts `.doc`, `.docx`, `.pdf`, `.xls` and `.xlsx` files (including monitoring `$Recycle.Bin`), archives them with 7-Zip under a predefined password with a 20 MB per-archive cap, and obfuscates its strings with single-byte-XOR; credential theft runs in parallel through Mimikatz (LSASS) and QuarksDumpLocalHash (local account hashes). The attackers then "allowed a few weeks for the ThumbcacheService to silently collect sensitive files without exfiltrating them" before returning — in the observed intrusion, in May 2026 — with an evolved toolset (the Stowaway proxy plus a TmcLoader/TmcPayload pair) to exfiltrate the accumulated archives over network shares using stolen credentials. Components persist under filenames that mimic legitimate system processes, such as `lass.exe` and `updates.exe`. Kaspersky hedges attribution: "there are indications of a potential link to the TetrisPhantom threat actor" based on similarities in victim targeting, technical capabilities and operational methodology ([Kaspersky Securelist, 2026-07-16](https://securelist.com/goserpent-backdoor-in-southeast-asia/120687/)).

**Defender takeaway:** for a government or diplomatic-facing SOC the transferable lesson is the split between a quiet, service-resident collection stage and a much later exfiltration event — an intrusion model in which the noisy phase can postdate initial compromise by weeks. In service and process telemetry, review newly installed Windows services whose DLLs live outside managed paths and whose names imitate system components; in file telemetry, watch for sustained enumeration of office-document extensions paired with password-protected archive creation on hosts with no archiving business; in network telemetry, surface SOCKS5 listeners appearing on workstations and bulk transfers to internal shares from accounts that do not normally write there. **Triage:** backup agents and DLP scanners also enumerate document trees and create archives — the discriminators here are the archive tool arriving with its own service persistence, the password-protected 7-Zip output with a fixed size cap, near-name-collision binaries (`lass.exe` vs `lsass.exe`) in the process lineage, and collection activity that persists for weeks with no corresponding egress until a distinct later toolset appears. No Swiss or European targeting is reported; this entry carries the campaign's tradecraft model, not a home-region threat.

*Provenance note: this entry was published by the 2026-07-18 weekly quality audit. The intel run on the publication date missed the item because the Securelist listing renders several posts without visible dates to a plain fetch, pushing the new post below the visible fold — the audit's per-publisher listing re-sweep surfaced it; a source-recipe note ships with the same audit.*
