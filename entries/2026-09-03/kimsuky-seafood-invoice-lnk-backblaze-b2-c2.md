---
schema: 1
kind: threat
title: "Kimsuky's seafood-invoice LNK campaign abuses Backblaze B2 cloud storage as C2 and exfiltration infrastructure, keyed by victim BIOS serial number"
headline: "The command-and-control channel is a legitimate cloud storage API, not a registered domain"
summary: >
  AhnLab ASEC attributes a malicious-LNK campaign to Kimsuky based on code and behavioural overlap with prior
  operations. The lure, a spearphishing LNK named for a seafood-purchase invoice, drops a decoy document while
  silently deploying a PowerShell/JScript persistence chain that authenticates to the Backblaze B2 API and uploads
  reconnaissance data to a per-victim path keyed on the BIOS serial number, then polls the same path for follow-up
  commands — using legitimate cloud storage as command-and-control rather than attacker-registered infrastructure.
discovered_at: "2026-09-03T05:18:30Z"
updated_at: null
event_date: "2026-09-01"
run_id: 2026-09-03T0410Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state]
regions: [apac, global]
sectors: [public-sector]
entities:
  - actor:kimsuky
techniques: [T1204.002, T1059.001, T1059.007, T1053.005, T1102, T1082, T1057, T1016.001, T1070.004, T1027]
affected_products: ["Microsoft Windows"]
cves: []
sources:
  - url: "https://asec.ahnlab.com/en/95217/"
    publisher: "AhnLab ASEC"
    date: "2026-09-01"
    role: primary
closed_sources: []
evidence:
  - quote: "In this attack, Backblaze B2 was used not merely as a file storage space but as a C2 infrastructure to exfiltrate information from infected PCs and relay follow-up commands."
    publisher: "AhnLab ASEC"
  - quote: "Based on such similarities in code and behavior, AhnLab determined that this malicious LNK is also linked to the Kim Sukki group."
    publisher: "AhnLab ASEC"
  - quote: "it is configured to execute ping_<FIRST 4 digits of UUID>.Js approximately every 14 minutes via wscript.Exe"
    publisher: "AhnLab ASEC"
verification: single-source
sourcing_note: >
  AhnLab ASEC is the sole source located for this campaign as of 2026-09-03; no independent corroboration exists.
  Rated B/2 on that basis. ASEC's own page names the actor inconsistently between title ("Kim Sooki") and body ("Kim
  Sukki") — an internal translation artefact on the vendor's side, mapped here to the canonical registry
  entity for Kimsuky regardless of spelling.
confidence: medium
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

AhnLab ASEC attributes a new malicious-LNK campaign to Kimsuky based on code and behavioural overlap with prior
Kimsuky LNK operations: matching PowerShell extraction syntax, the same fixed-offset method of extracting data
embedded in the LNK, and the same Task Scheduler registration pattern
([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95217/)). The lure is a spearphishing attachment named
"[Royal Hotel Seoul] Request for Review of Seafood Ingredient Purchases.LNK." Running it uses PowerShell to extract
embedded data: it drops a legitimate-looking decoy .hwp document at the same path, displayed to the victim, while
simultaneously writing an XOR-encrypted ZIP to `C:\ProgramData\systmp\sunshine` containing a PowerShell script
(`termsvc.ps1`) and a JScript file, saved separately as `C:\ProgramData\systmp\ping_<first-4-UUID-digits>.js`
([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95217/)). Persistence is a Scheduled Task named
`MicrosoftOffice2016_<first-4-UUID-digits>` that runs the JS file via `wscript.exe` roughly every 14 minutes; the
obfuscated script checks for the presence of `termsvc.ps1` and bypasses the PowerShell execution policy to run it
hidden ([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95217/)). `termsvc.ps1` collects OS name and
architecture, system timezone, public IP (queried via `api.ipify.org`), username, domain, the running-process list,
and computer name, then authenticates to the Backblaze B2 API and uploads the collected data to a per-victim path
keyed on the BIOS serial number — a legitimate cloud-storage service used as command-and-control infrastructure
rather than attacker-registered domains
([AhnLab ASEC, 2026-09-01](https://asec.ahnlab.com/en/95217/)). It then polls the same B2 path for a follow-up
command file, saves it under an arbitrary name as a `.cmd` in `%TEMP%`, executes it hidden via `cmd.exe /c`, and
deletes the local copy roughly 120 seconds later. The actor deletes the original LNK and the intermediate ZIP
during execution, leaving only the components needed for the persistence loop.

**Triage:** authenticated outbound HTTPS traffic to Backblaze B2 API endpoints from a workstation with no
legitimate backup or storage use case, alongside a Scheduled Task invoking `wscript.exe` against a script under
`C:\ProgramData` on a short (~14-minute) interval, is the reusable detection hook — it generalises beyond this
campaign to "legitimate cloud storage abused as C2," a pattern increasingly common across unrelated actors, not
only Kimsuky. **Defender takeaway:** hunt for the specific Task Scheduler naming pattern and the
`C:\ProgramData\systmp\` / `C:\ProgramData\video\` staging paths on any host that received an unsolicited LNK
attachment; an egress-monitoring baseline that flags first-seen connections to cloud-storage API hostnames from
endpoint processes (rather than approved backup software) would have caught this channel regardless of the lure
content.
