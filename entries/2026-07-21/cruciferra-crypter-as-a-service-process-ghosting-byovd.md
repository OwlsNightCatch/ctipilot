---
schema: 1
kind: threat
horizon: operational
title: "Cruciferra: a crypter-as-a-service using kernel-aware process ghosting and BYOVD EDR termination, tied to China-nexus TA4922"
headline: "Proofpoint details Cruciferra, a commercial crypter that hides payloads with process ghosting and kills EDR via a vulnerable signed driver"
summary: >
  Proofpoint documented (2026-07-20) Cruciferra, a Mono/.NET crypter-as-a-service used across multiple
  criminal groups to pack commodity RATs and infostealers, combining a modified process-ghosting loader,
  memory-query and hotpatch tampering, indirect syscalls from a clean ntdll copy, and BYOVD EDR
  termination via a vulnerable signed driver. Proofpoint attributes four campaigns using it to deliver
  AsyncRAT to the China-nexus actor TA4922, whose tax-authority-themed lures target finance, healthcare
  and government — sectors central to this constituency.
discovered_at: "2026-07-21T04:41:00Z"
event_date: "2026-07-20"
run_id: 2026-07-21T0409Z-intel
priority: notable
immediate_action: null
tags: [infostealer, organized-crime, nation-state, china-nexus]
regions: [global]
sectors: [finance, healthcare, public-sector]
entities: [actor:ta4922, tool:cruciferra-crypter]
techniques: [T1055, T1685, T1027, T1027.002]
affected_products: []
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service"
    publisher: "Proofpoint Threat Insight"
    date: "2026-07-20"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/cruciferra-crypter-process-ghosting/"
    publisher: "Infosecurity Magazine"
    date: "2026-07-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the malware reads a clean copy of ntdll.dll on disk and stores all stub pointers in a global structure for later usage."
    publisher: "Proofpoint Threat Insight"
  - quote: "Proofpoint observed four campaigns attributed to Chinese-speaking cybercrime actor TA4922 using Cruciferra to ultimately deliver AsyncRAT."
    publisher: "Proofpoint Threat Insight"
verification: multi-source
sourcing_note: null
confidence: high
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

Proofpoint's analysis details Cruciferra, a Mono/.NET-based crypter-as-a-service advertised on underground forums since late 2025 and used by several unrelated criminal groups to pack commodity payloads (AsyncRAT/DCRAT, Agent Tesla, XWorm, Formbook/XLoader, Remcos, Snake Keylogger and others). Its distinguishing feature is an evasion stack aimed squarely at endpoint defenses ([Proofpoint, 2026-07-20](https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service)). Payloads are encrypted with one of over 90 polymorphic cipher routines assembled from primitives such as Keccak, Feistel, SPECK and Threefish and stored Base16-encoded in the PE's `.reloc` section, so no two samples share an identical routine. Execution uses a variant of process ghosting: a temporary file is marked for deletion, then mapped as a PE image section (`NtCreateSection` with `SEC_IMAGE`) before the delete completes, leaving a running process whose backing image is never scannable on disk. Cruciferra hardens that trick with two anti-EDR steps — patching `ZwQueryVirtualMemory` so endpoint tools misread mapped memory, and neutering `NtManageHotPatch` to defeat image-integrity validation — alongside Import Address Table unhooking and indirect syscalls: per Proofpoint, "the malware reads a clean copy of ntdll.dll on disk and stores all stub pointers in a global structure for later usage." For EDR/AV termination it loads a legitimate-but-vulnerable signed driver (Proofpoint names `GoFlyDrv.sys` among the alternates) and issues control codes to kill security processes — classic BYOVD.

Attribution matters here: "Proofpoint observed four campaigns attributed to Chinese-speaking cybercrime actor TA4922 using Cruciferra to ultimately deliver AsyncRAT," behind landing pages mimicking government tax portals, against finance, healthcare and government targets. **Defender takeaway:** Cruciferra is packer infrastructure shared across many intrusions, so its evasion signatures are worth hunting independent of any single payload. **Triage:** developer and installer tooling legitimately maps image sections and loads signed drivers — the discriminators are a running process whose backing PE section maps to an already-deleted temporary file (the ghosting signature), a driver-load event for a known-vulnerable helper driver such as `GoFlyDrv.sys` outside its expected vendor context, and a thread polling `EnumWindows` to suppress a console window; any one alone is weak, the combination on a non-developer host is the signal.
